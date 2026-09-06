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

# The index entry contract, RF-28 and RF-29. The entry is closed: a field
# named by neither tuple is an error rather than something to ignore.
ENTRY_REQUIRED_FIELDS = (
    "id",
    "path",
    "title",
    "version",
    "status",
    "summary",
    "applies_to",
)
ENTRY_OPTIONAL_FIELDS = ("tags", "requires")

RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_RULE = re.compile(r"^\*\*([A-Z]{2,3})-(\d+)\*\*", re.MULTILINE)
RE_FILENAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$")
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#]+?)(?:#[^)]*)?\)")
RE_MARKER = re.compile(r"\b(TODO|FIXME|TBD|XXX)\b\s*[:(]|^\s*(TODO|FIXME|TBD)\b")

# A reference to another standard, in the two forms RF-26 permits.
RE_XREF_RULE = re.compile(r"\b([A-Z]{2,3})-\d+\b")
RE_XREF_PATH = re.compile(r"\b((?:standards|meta)/[a-z0-9-]+\.md)\b")

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


def ignored_dirs() -> set[str]:
    """Directory names .gitignore excludes, which the validator does not walk.

    RL-13 puts build output and local environment files in .gitignore, so that
    file is where this fact lives and DOC-3 forbids restating it here. Only
    entries of the form `name/` are honoured; anything more needs a real
    gitignore implementation, which nothing in this repository requires.
    """
    names = {".git"}
    gitignore = ROOT / ".gitignore"
    if gitignore.exists():
        for line in gitignore.read_text(encoding="utf-8").splitlines():
            entry = line.strip()
            if entry.startswith("#") or not entry.endswith("/"):
                continue
            names.add(entry.strip("/"))
    return names


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
        error("index.yaml", "RF-27", "index is missing")
        sys.exit(report())
    try:
        data = yaml.safe_load(INDEX.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        error("index.yaml", "RF-27", f"index is not valid YAML: {exc}")
        sys.exit(report())
    if not isinstance(data, dict) or "schema_version" not in data:
        error("index.yaml", "RF-27", "index must be a mapping carrying schema_version")
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
    for section in ("meta", "standards"):
        if not index.get(section):
            error("index.yaml", "RF-27", f"index has no {section} section")

    catalogued: dict[str, str] = {}
    seen_ids: dict[str, str] = {}

    for entry in entries:
        where = f"index.yaml:{entry.get('id', '?')}"

        for field in ENTRY_REQUIRED_FIELDS:
            if field not in entry or entry[field] in (None, "", []):
                error(where, "RF-28", f"entry is missing {field}")

        extra = set(entry) - set(ENTRY_REQUIRED_FIELDS) - set(ENTRY_OPTIONAL_FIELDS)
        for field in sorted(extra - {"_section"}):
            error(where, "RF-29", f"entry carries an unrecognised field: {field}")

        entry_id = entry.get("id", "")
        if not RE_ID.match(str(entry_id)):
            error(where, "RF-6", f"id is not lowercase hyphen separated: {entry_id!r}")
        if entry_id in seen_ids:
            error(where, "RF-6", f"id duplicates {seen_ids[entry_id]}")
        seen_ids[entry_id] = where

        version = str(entry.get("version", ""))
        if not RE_SEMVER.match(version):
            error(where, "RF-28", f"version is not semantic: {version!r}")

        path = entry.get("path")
        if not path:
            continue
        if path in catalogued:
            error(where, "RF-32", f"path is already listed by {catalogued[path]}")
        catalogued[path] = where

        if not str(path).startswith(("standards/", "meta/")):
            error(where, "RF-31", f"path is not in standards/ or meta/: {path}")
        elif not (ROOT / path).exists():
            error(where, "RF-31", f"path does not exist: {path}")

    for path in rule_files():
        relative = path.relative_to(ROOT).as_posix()
        if relative not in catalogued:
            error(relative, "RF-32", "file is not listed in index.yaml")


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
        if str(entry.get("version")) != str(front.get("version")):
            error(relative, "RF-30", "front matter version does not match the index entry")
        if entry.get("title") != front.get("title"):
            error(relative, "RF-30", "front matter title does not match the index entry")

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
    skip = ignored_dirs()

    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in skip for part in relative.parts):
            continue
        if not path.is_file():
            continue
        name = path.name
        if name in EXEMPT_NAMES or name.startswith("."):
            continue
        if not RE_FILENAME.match(name):
            error(relative.as_posix(), "NAM-2", "file name is not lowercase hyphen separated")
        if name.lower() == "readme.md" and path.parent != ROOT:
            error(
                relative.as_posix(),
                "NAM-17",
                "only a directory's own README may be named readme.md",
            )

    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in skip for part in relative.parts):
            continue
        if path.is_dir() and path.name in {"misc", "other", "stuff", "temp", "new"}:
            error(relative.as_posix(), "NAM-8", "directory name is not descriptive")


def check_links() -> None:
    """RF-33 covers a file listed in the index; RM-23 covers the README."""
    for path in [*rule_files(), ROOT / "README.md"]:
        relative = path.relative_to(ROOT).as_posix()
        rule = "RM-23" if relative == "README.md" else "RF-33"
        text = strip_code_blocks(path.read_text(encoding="utf-8"))
        for match in RE_MD_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                error(relative, rule, f"relative link does not resolve: {target}")


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


def check_requires(entries: list[dict], all_rules: list[tuple[str, str]]) -> None:
    """Every standard a file references must appear in its entry's requires, per RF-25.

    References take the two forms RF-26 permits: a rule identifier, resolved
    through the prefix that owns it, or a repository relative path. A prefix
    that owns no rule here is ignored, so placeholders such as REQ-<n> in
    standards/lifecycle.md do not register as references.
    """
    id_by_path = {e["path"]: e.get("id") for e in entries if e.get("path")}
    known_ids = {i for i in id_by_path.values() if i}

    owner_by_prefix: dict[str, str] = {}
    for rule_id, relative in all_rules:
        owner_by_prefix.setdefault(rule_id.split("-")[0], relative)

    for entry in entries:
        path = entry.get("path")
        entry_id = entry.get("id")
        if not path or not (ROOT / path).exists():
            continue
        where = f"index.yaml:{entry_id}"

        declared = entry.get("requires") or []
        if not isinstance(declared, list):
            error(where, "RF-25", "requires is not a list")
            continue
        for name in declared:
            if name == entry_id:
                error(where, "RF-25", "requires names the entry itself")
            elif name not in known_ids:
                error(where, "RF-25", f"requires names an unknown entry: {name}")

        text = strip_code_blocks((ROOT / path).read_text(encoding="utf-8"))
        referenced: set[str] = set()
        for match in RE_XREF_RULE.finditer(text):
            owner = owner_by_prefix.get(match.group(1))
            if owner and owner != path:
                referenced.add(id_by_path[owner])
        for match in RE_XREF_PATH.finditer(text):
            target = match.group(1)
            if target != path and target in id_by_path:
                referenced.add(id_by_path[target])
        referenced.discard(entry_id)

        for name in sorted(referenced - set(declared)):
            error(path, "RF-25", f"references {name} but the index entry does not require it")
        for name in sorted(set(declared) - referenced):
            if name in known_ids:
                warn(where, "RF-25", f"requires {name} but the file does not reference it")


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
    check_requires(entries, all_rules)
    check_names()
    check_links()
    return report()


if __name__ == "__main__":
    sys.exit(main())
