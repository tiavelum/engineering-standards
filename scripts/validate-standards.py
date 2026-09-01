#!/usr/bin/env python3
"""Validate this repository against its own standards.

Run from the repository root:

    python3 scripts/validate-standards.py

Exits 0 when every check passes, 1 on any error. Warnings do not fail the run.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.yaml"
RULE_DIRS = ("standards", "meta")

FRONT_MATTER_FIELDS = ("id", "title", "version", "status", "applies_to", "summary")
VALID_STATUS = {"active", "draft", "deprecated"}

RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_RULE = re.compile(r"^\*\*([A-Z]{2,3})-(\d+)\*\*", re.MULTILINE)
RE_FILENAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$")
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#]+?)(?:#[^)]*)?\)")
RE_MARKER = re.compile(r"\b(TODO|FIXME|TBD|XXX)\b\s*[:(]|^\s*(TODO|FIXME|TBD)\b")

# Names fixed by an external tool or convention, exempt per NAM-6.
EXEMPT_NAMES = {
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CODEOWNERS",
    "Dockerfile",
    "Makefile",
}

errors: list[str] = []
warnings: list[str] = []


def error(where: str, rule: str, message: str) -> None:
    errors.append(f"{where}: [{rule}] {message}")


def warn(where: str, rule: str, message: str) -> None:
    warnings.append(f"{where}: [{rule}] {message}")


def strip_code_blocks(text: str) -> str:
    """Blank out fenced code blocks so prose checks ignore templates and examples."""
    out: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if fence is None:
            match = re.match(r"^(`{3,})", stripped)
            if match:
                fence = match.group(1)
                out.append("")
                continue
            out.append(line)
        else:
            if stripped.startswith(fence):
                fence = None
            out.append("")
    return "\n".join(out)


def split_front_matter(text: str, where: str) -> dict | None:
    """Return the parsed front matter, or None if it is missing or malformed."""
    if not text.startswith("---\n"):
        error(where, "RF-5", "file does not begin with YAML front matter")
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        error(where, "RF-5", "front matter is not terminated")
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        error(where, "RF-5", f"front matter is not valid YAML: {exc}")
        return None
    if not isinstance(data, dict):
        error(where, "RF-5", "front matter is not a mapping")
        return None
    return data


def rule_files() -> list[Path]:
    found: list[Path] = []
    for directory in RULE_DIRS:
        found.extend(sorted((ROOT / directory).glob("*.md")))
    return found


def check_index_loads() -> dict:
    if not INDEX.exists():
        error("index.yaml", "CO-1", "index is missing")
        sys.exit(report())
    try:
        data = yaml.safe_load(INDEX.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        error("index.yaml", "CO-9", f"index is not valid YAML: {exc}")
        sys.exit(report())
    if not isinstance(data, dict) or "schema_version" not in data:
        error("index.yaml", "CO-9", "index must be a mapping carrying schema_version")
        sys.exit(report())
    return data


def index_entries(index: dict) -> list[dict]:
    entries: list[dict] = []
    for section in ("meta", "standards"):
        for entry in index.get(section) or []:
            entry = dict(entry)
            entry["_section"] = section
            entries.append(entry)
    return entries


def check_catalogue(index: dict, entries: list[dict]) -> None:
    catalogued = set()
    seen_ids: dict[str, str] = {}

    for entry in entries:
        where = f"index.yaml:{entry.get('id', '?')}"
        path = entry.get("path")
        if not path:
            error(where, "CO-1", "entry has no path")
            continue
        catalogued.add(path)

        if not (ROOT / path).exists():
            error(where, "CO-1", f"path does not exist: {path}")

        entry_id = entry.get("id", "")
        if not RE_ID.match(entry_id):
            error(where, "RF-6", f"id is not lowercase hyphen separated: {entry_id!r}")
        if entry_id in seen_ids:
            error(where, "RF-6", f"id duplicates {seen_ids[entry_id]}")
        seen_ids[entry_id] = where

        if not entry.get("summary"):
            error(where, "RF-8", "entry has no summary")
        if not entry.get("applies_to"):
            error(where, "CO-2", "entry has no applies_to")
        if entry["_section"] == "standards":
            version = str(entry.get("version", ""))
            if not RE_SEMVER.match(version):
                error(where, "RF-17", f"version is not semantic: {version!r}")

    for path in rule_files():
        relative = path.relative_to(ROOT).as_posix()
        if relative not in catalogued:
            error(relative, "CO-1", "file is not listed in index.yaml")


def check_rule_file(path: Path, entries_by_path: dict[str, dict]) -> list[tuple[str, str]]:
    relative = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    found_rules: list[tuple[str, str]] = []

    front = split_front_matter(text, relative)
    if front is None:
        return found_rules

    for field in FRONT_MATTER_FIELDS:
        if field not in front or front[field] in (None, "", []):
            error(relative, "RF-5", f"front matter is missing {field}")

    if front.get("status") not in VALID_STATUS:
        error(relative, "RF-7", f"status is not one of {sorted(VALID_STATUS)}")

    entry = entries_by_path.get(relative)
    if entry:
        if entry.get("id") != front.get("id"):
            error(relative, "RF-6", "front matter id does not match the index entry id")
        if "version" in entry and str(entry["version"]) != str(front.get("version")):
            error(relative, "RF-19", "front matter version does not match the index entry")
        if entry.get("title") != front.get("title"):
            error(relative, "RF-19", "front matter title does not match the index entry")

    summary = str(front.get("summary", ""))
    if summary.count(".") > 1:
        warn(relative, "RF-8", "summary looks like more than one sentence")

    prefixes = set()
    numbers: dict[str, int] = {}
    for match in RE_RULE.finditer(text):
        prefix, number = match.group(1), int(match.group(2))
        prefixes.add(prefix)
        rule_id = f"{prefix}-{number}"
        if rule_id in numbers:
            error(relative, "RF-11", f"rule {rule_id} appears more than once")
        numbers[rule_id] = number
        found_rules.append((rule_id, relative))

    if len(prefixes) > 1:
        error(relative, "RF-10", f"file mixes rule prefixes: {sorted(prefixes)}")
    if not prefixes and relative.startswith("standards/"):
        error(relative, "RF-10", "standard contains no identified rules")

    line_count = text.count("\n")
    if relative.startswith("standards/") and line_count > 200:
        warn(relative, "RF-9", f"file is {line_count} lines, over the 200 line guideline")

    # A rule may legitimately name these markers, so skip rule statements and
    # code blocks and look only for an actual unfinished marker.
    prose = strip_code_blocks(text)
    for line in prose.splitlines():
        if RE_RULE.match(line):
            continue
        if RE_MARKER.search(line):
            error(relative, "RF-21", f"file contains an unfinished marker: {line.strip()[:60]}")

    return found_rules


def check_names() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(".git/"):
            continue
        name = path.name
        if name in EXEMPT_NAMES or name.startswith("."):
            continue
        if not RE_FILENAME.match(name):
            error(relative, "NAM-2", "file name is not lowercase hyphen separated")
        if name.lower() == "readme.md" and path.parent != ROOT:
            error(relative, "NAM-17", "only a directory's own README may be named readme.md")

    for path in ROOT.rglob("*"):
        if path.is_dir() and path.name in {"misc", "other", "stuff", "temp", "new"}:
            error(path.relative_to(ROOT).as_posix(), "NAM-8", "directory name is not descriptive")


def check_links() -> None:
    for path in list(rule_files()) + [ROOT / "README.md"]:
        relative = path.relative_to(ROOT).as_posix()
        text = strip_code_blocks(path.read_text(encoding="utf-8"))
        for match in RE_MD_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                error(relative, "RM-23", f"relative link does not resolve: {target}")


def check_rule_prefix_uniqueness(all_rules: list[tuple[str, str]]) -> None:
    prefix_owner: dict[str, str] = {}
    seen: dict[str, str] = {}
    for rule_id, relative in all_rules:
        prefix = rule_id.split("-")[0]
        if prefix in prefix_owner and prefix_owner[prefix] != relative:
            error(relative, "RF-10", f"prefix {prefix} is already used by {prefix_owner[prefix]}")
        prefix_owner.setdefault(prefix, relative)
        if rule_id in seen and seen[rule_id] != relative:
            error(relative, "RF-11", f"rule {rule_id} also defined in {seen[rule_id]}")
        seen.setdefault(rule_id, relative)


def report() -> int:
    for line in warnings:
        print(f"warning  {line}")
    for line in errors:
        print(f"error    {line}")
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"All checks passed. {len(warnings)} warning(s).")
    return 0


def main() -> int:
    index = check_index_loads()
    entries = index_entries(index)
    check_catalogue(index, entries)

    entries_by_path = {e["path"]: e for e in entries if e.get("path")}
    all_rules: list[tuple[str, str]] = []
    for path in rule_files():
        all_rules.extend(check_rule_file(path, entries_by_path))

    check_rule_prefix_uniqueness(all_rules)
    check_names()
    check_links()
    return report()


if __name__ == "__main__":
    sys.exit(main())
