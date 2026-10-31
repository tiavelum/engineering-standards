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
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.yaml"
RULE_DIRS = ("standards", "meta")

# The one name in RULE_DIRS that is not a standard file, per the definition at
# the top of meta/rule-format.md: a directory's own README.
DIRECTORY_README = "README.md"

FRONT_MATTER_FIELDS = ("id", "title", "version", "status", "applies_to", "summary")
VALID_STATUS = {"active", "draft", "deprecated"}

# The top level of index.yaml, RF-27. Closed like the entry: any other key is
# an error.
INDEX_KEYS = ("schema_version", "meta", "standards")

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

# The fields an entry and its file's front matter must agree on, RF-30.
MATCHED_FIELDS = ("id", "title", "version", "status", "summary", "applies_to")

# Prefixes of removed files, which RF-40 keeps any other file from taking.
RETIRED_PREFIXES = frozenset({"LC", "PA"})

# Standard files not yet shortened to the limits of RF-14, RF-47 and RF-48.
# A breach of those limits in one of them is a warning, not an error. Each file
# leaves the list once it is refactored to the limits.
LENGTH_PENDING = frozenset(
    {
        "standards/documentation.md",
        "standards/git-workflow.md",
        "standards/issues.md",
        "standards/module-layers.md",
        "standards/readme-contract.md",
        "standards/repo-layout.md",
        "standards/tooling.md",
        "standards/versioning.md",
        "standards/writing.md",
    }
)

# The limits of RF-47, RF-48 and RF-14, in characters of the Markdown source.
MAX_RULE = 250
MAX_EXAMPLE_LINE = 200
MAX_REASON = 250

RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
# The heading RF-12 puts above each rule, and the bold form it replaced.
RE_RULE = re.compile(r"^### ([A-Z]{2,3})-(\d+)\b(.*)$")
RE_BOLD_RULE = re.compile(r"^\*\*[A-Z]{2,3}-\d+\*\*")
# The marker RF-34 puts in the heading of a rule under review.
RE_DRAFT = re.compile(r"^ \(draft: #\d+\)$")
RE_FILENAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$")
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#]*)(?:#([^)]*))?\)")
RE_INLINE_CODE = re.compile(r"`[^`\n]*`")
RE_HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
RE_MARKER = re.compile(r"\b(TODO|FIXME|TBD|XXX)\b\s*[:(]|^\s*(TODO|FIXME|TBD)\b")
# Blocks below a rule that are neither its text, an example nor a reason.
RE_TABLE_OR_LIST = re.compile(r"^\s*(\||[-*+]\s|\d+\.\s)")

# The RFC 2119 keywords RF-13 requires, uppercase only.
RE_RFC2119 = re.compile(r"\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b")

# A reference to another standard, in the two forms RF-26 permits.
RE_XREF_RULE = re.compile(r"\b([A-Z]{2,3})-\d+\b")
RE_XREF_PATH = re.compile(r"\b((?:standards|meta)/[a-z0-9-]+\.md)\b")

# A range of rule identifiers, which RF-49 rules out.
RE_RANGE = re.compile(
    r"\b[A-Z]{2,3}-\d+\s*(?:to|through|-|\N{EN DASH}|\N{EM DASH}|\.\.)\s*(?:[A-Z]{2,3}-)?\d+\b"
)

# Terms of the shape RF-43 describes that name something other than a rule.
# RF-43 accepts such a term only if a rule here carries its identifier or it
# names something else, so a file that writes one, such as UTF-8, adds it here.
NOT_RULE_IDS = frozenset({"UTF-8"})

# Names a tool or convention fixes, which NAM-2 does not govern.
FIXED_NAMES = {
    "README.md",
    "CLAUDE.md",
    "LICENSE",
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


def length_issue(where: str, rule: str, message: str) -> None:
    """A breach of a length limit: an error, or a warning while LENGTH_PENDING holds the file."""
    if where in LENGTH_PENDING:
        warn(where, rule, message)
    else:
        error(where, rule, message)


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
    """The standard files: every Markdown file of RULE_DIRS but a directory README."""
    found: list[Path] = []
    for directory in RULE_DIRS:
        found.extend(
            path
            for path in sorted((ROOT / directory).glob("*.md"))
            if path.name != DIRECTORY_README
        )
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
    for key in sorted(set(index) - set(INDEX_KEYS)):
        error("index.yaml", "RF-27", f"index carries an unrecognised top-level key: {key}")

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
            error(where, "RF-35", f"id is not lowercase hyphen separated: {entry_id!r}")
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
        elif Path(path).name == DIRECTORY_README:
            error(where, "RF-31", f"path names a directory README, not a standard file: {path}")
        elif not str(path).startswith(f"{entry['_section']}/"):
            error(where, "RF-31", f"entry for {path} stands under {entry['_section']}")

    for path in rule_files():
        relative = path.relative_to(ROOT).as_posix()
        if relative not in catalogued:
            error(relative, "RF-32", "file is not listed in index.yaml")


def rule_sections(text: str) -> list[tuple[re.Match, list[list[tuple[int, str]]]]]:
    """Each rule's heading with the blocks below it, up to the next heading.

    A block is a run of non-blank lines, each kept with its line number. Fenced
    code is blanked first, so a sample in a code block ends a block.
    """
    sections: list[tuple[re.Match, list[list[tuple[int, str]]]]] = []
    blocks: list[list[tuple[int, str]]] | None = None
    for number, line in enumerate(strip_code_blocks(text).splitlines(), start=1):
        if RE_HEADING.match(line):
            match = RE_RULE.match(line)
            blocks = [] if match else None
            if match:
                sections.append((match, blocks))
            continue
        if blocks is None:
            continue
        if not line.strip():
            if blocks and blocks[-1]:
                blocks.append([])
            continue
        if not blocks:
            blocks.append([])
        blocks[-1].append((number, line))
    return [(match, [block for block in found if block]) for match, found in sections]


def check_rule_body(relative: str, rule_id: str, blocks: list[list[tuple[int, str]]]) -> None:
    """RF-12, RF-13 and the limits of RF-14, RF-47 and RF-48 for one rule."""
    if not blocks or RE_TABLE_OR_LIST.match(blocks[0][0][1]) or blocks[0][0][1].startswith(">"):
        error(relative, "RF-12", f"rule {rule_id} has no text paragraph below its heading")
        return

    text = blocks[0]
    # RF-13 wants the keyword in the first line of the rule's text. This is a
    # floor: a keyword named rather than used still passes, which RF-1 leaves
    # to a person's check.
    if not RE_RFC2119.search(text[0][1]):
        error(relative, "RF-13", f"rule {rule_id} states no RFC 2119 keyword")
    length = len(" ".join(line.strip() for _, line in text))
    if length > MAX_RULE:
        length_issue(relative, "RF-47", f"rule {rule_id} is {length} characters, over {MAX_RULE}")

    reasons = 0
    for block in blocks[1:]:
        first = block[0][1]
        if first.startswith(">"):
            for number, line in block:
                if len(line) > MAX_EXAMPLE_LINE:
                    length_issue(
                        relative,
                        "RF-48",
                        f"line {number}, an example of {rule_id}, is {len(line)} characters, "
                        f"over {MAX_EXAMPLE_LINE}",
                    )
        elif RE_TABLE_OR_LIST.match(first):
            continue
        else:
            reasons += 1
            length = len(" ".join(line.strip() for _, line in block))
            if length > MAX_REASON:
                length_issue(
                    relative,
                    "RF-14",
                    f"reason at line {block[0][0]}, of {rule_id}, is {length} characters, "
                    f"over {MAX_REASON}",
                )
    if reasons > 1:
        length_issue(relative, "RF-14", f"rule {rule_id} has {reasons} reason paragraphs, not one")


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
        for field in MATCHED_FIELDS:
            if str(entry.get(field)) != str(front.get(field)):
                error(relative, "RF-30", f"front matter {field} does not match the index entry")

    summary = str(front.get("summary", ""))
    if summary.count(".") > 1:
        warn(relative, "RF-8", "summary looks like more than one sentence")

    prefixes = set()
    numbers: dict[str, int] = {}
    rule_text_lines: set[int] = set()
    for match, blocks in rule_sections(text):
        prefix, number = match.group(1), int(match.group(2))
        prefixes.add(prefix)
        rule_id = f"{prefix}-{number}"
        if rule_id in numbers:
            error(relative, "RF-11", f"rule {rule_id} appears more than once")
        numbers[rule_id] = number
        found_rules.append((rule_id, relative))

        rest = match.group(3)
        if rest.lstrip().startswith("(draft"):
            if not RE_DRAFT.match(rest):
                error(relative, "RF-34", f"rule {rule_id} carries a malformed draft marker")
        elif rest:
            error(relative, "RF-12", f"heading of {rule_id} carries more than its identifier")

        check_rule_body(relative, rule_id, blocks)
        if blocks:
            rule_text_lines.update(number for number, _ in blocks[0])

    if len(prefixes) > 1:
        error(relative, "RF-10", f"file mixes rule prefixes: {sorted(prefixes)}")
    if not prefixes and relative.startswith("standards/"):
        error(relative, "RF-10", "standard contains no identified rules")

    # A rule may legitimately name these markers, so skip rule texts and code
    # blocks and look only for an actual unfinished marker.
    prose = strip_code_blocks(text)
    for number, line in enumerate(prose.splitlines(), start=1):
        if RE_BOLD_RULE.match(line):
            error(relative, "RF-12", f"line {number} opens a rule in bold instead of a heading")
        if number in rule_text_lines:
            continue
        if RE_MARKER.search(line):
            error(relative, "DOC-9", f"file contains an unfinished marker: {line.strip()[:60]}")

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
        if name in FIXED_NAMES or name.startswith("."):
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
            error(relative.as_posix(), "NAM-1", "directory name is not descriptive")


def heading_anchors(path: Path) -> set[str]:
    """The fragments GitHub gives the headings of a Markdown file, lowercased.

    The rules are those of GitHub's "Section links":
    https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
    Markup is reduced to its text first; HTML in a heading is not, since no
    file here puts any there. Fragments are compared lowercased, because
    GitHub's own example links a heading with an uppercase letter kept.
    """
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in strip_code_blocks(path.read_text(encoding="utf-8")).splitlines():
        match = RE_HEADING.match(line)
        if not match:
            continue
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", match.group(1))
        text = re.sub(r"[`*]|(?<!\w)_|_(?!\w)", "", text).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", text).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        anchors.add(slug if number == 0 else f"{slug}-{number}")
    return anchors


def readmes() -> list[Path]:
    """The root README and any directory README of RULE_DIRS."""
    found = [ROOT / "README.md"]
    for directory in RULE_DIRS:
        candidate = ROOT / directory / DIRECTORY_README
        if candidate.exists():
            found.append(candidate)
    return found


def check_links() -> None:
    """DOC-51 for the READMEs and every file listed in the index.

    A link within the repository must reach its path and, for a Markdown file,
    the heading its fragment names. Outside links are not fetched, and code,
    fenced or inline, is skipped, since a link there is written as an example.
    """
    for path in [*rule_files(), *readmes()]:
        relative = path.relative_to(ROOT).as_posix()
        text = RE_INLINE_CODE.sub("", strip_code_blocks(path.read_text(encoding="utf-8")))
        for match in RE_MD_LINK.finditer(text):
            target = match.group(1).strip()
            fragment = match.group(2)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve() if target else path
            if not resolved.exists():
                error(relative, "DOC-51", f"relative link does not resolve: {target}")
                continue
            if (
                fragment
                and resolved.is_file()
                and resolved.suffix == ".md"
                and unquote(fragment).lower() not in heading_anchors(resolved)
            ):
                error(relative, "DOC-51", f"link names no heading of its file: {target}#{fragment}")


def check_rule_prefix_uniqueness(all_rules: list[tuple[str, str]]) -> None:
    prefix_owner: dict[str, str] = {}
    seen: dict[str, str] = {}
    for rule_id, relative in all_rules:
        prefix = rule_id.split("-")[0]
        if prefix in RETIRED_PREFIXES and prefix not in prefix_owner:
            error(relative, "RF-40", f"prefix {prefix} belonged to a removed file")
        if prefix in prefix_owner and prefix_owner[prefix] != relative:
            error(relative, "RF-40", f"prefix {prefix} is already used by {prefix_owner[prefix]}")
        prefix_owner.setdefault(prefix, relative)
        if rule_id in seen and seen[rule_id] != relative:
            error(relative, "RF-11", f"rule {rule_id} also defined in {seen[rule_id]}")
        seen.setdefault(rule_id, relative)


def check_cited_ids(all_rules: list[tuple[str, str]]) -> None:
    """Every rule identifier the index or a rule file writes must be a rule's, per RF-43.

    The whole text is read, fenced examples and YAML comments included.
    """
    defined = {rule_id for rule_id, _ in all_rules}
    for path in [INDEX, *rule_files()]:
        relative = path.relative_to(ROOT).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, start=1):
            for match in RE_XREF_RULE.finditer(line):
                token = match.group(0)
                if token in NOT_RULE_IDS:
                    continue
                if token not in defined:
                    error(relative, "RF-43", f"line {number} cites {token}, which no rule defines")


def check_ranges() -> None:
    """No range of rule identifiers in the index, a rule file or a README, per RF-49.

    Code, fenced or inline, is skipped, since a range there is written as an
    example, as RF-49 itself writes one.
    """
    for path in [INDEX, *rule_files(), *readmes()]:
        relative = path.relative_to(ROOT).as_posix()
        text = strip_code_blocks(path.read_text(encoding="utf-8"))
        for number, line in enumerate(text.splitlines(), start=1):
            for match in RE_RANGE.finditer(RE_INLINE_CODE.sub("", line)):
                error(relative, "RF-49", f"line {number} cites a range: {match.group(0)}")


def check_requires(entries: list[dict], all_rules: list[tuple[str, str]]) -> None:
    """Every standard a file references must appear in its entry's requires, per RF-25.

    References take the two forms RF-26 permits: a rule identifier, resolved
    through the prefix that owns it, or a repository relative path. A prefix
    that owns no rule here is ignored, so a token of the same shape that is
    not a rule identifier, such as UTF-8, does not register as a reference.
    Fenced blocks are read too, since RF-25 counts a reference in an example
    the same as one in a rule. An active entry must not require a draft, per
    RF-50.
    """
    id_by_path = {e["path"]: e.get("id") for e in entries if e.get("path")}
    known_ids = {i for i in id_by_path.values() if i}
    status_by_id = {e.get("id"): e.get("status") for e in entries}

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
            elif entry.get("status") == "active" and status_by_id.get(name) == "draft":
                error(where, "RF-50", f"active entry requires the draft entry {name}")

        text = (ROOT / path).read_text(encoding="utf-8")
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
    check_cited_ids(all_rules)
    check_ranges()
    check_requires(entries, all_rules)
    check_names()
    check_links()
    return report()


if __name__ == "__main__":
    sys.exit(main())
