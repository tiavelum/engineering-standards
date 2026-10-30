#!/usr/bin/env python3
"""Fail on a soft line break in any tracked Markdown file.

A soft line break is a line break inside a paragraph. Markdown renders it as a
space, so two lines written one under the other render as one run of text.

Run from the repository root:

    python3 scripts/check-line-breaks.py

Exits 0 when no file has a soft line break, 1 otherwise.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent

# CommonMark with tables, as GitHub renders them, so that the rows of a table
# are not read as the lines of a paragraph.
PARSER = MarkdownIt("commonmark").enable("table")


def markdown_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True, check=True
    )
    return result.stdout.split()


def blank_front_matter(text: str) -> str:
    """Blank out YAML front matter, keeping its lines so line numbers still match.

    The parser does not know front matter and would read its lines as a paragraph.
    """
    lines = text.split("\n")
    if lines[0] != "---":
        return text
    for end in range(1, len(lines)):
        if lines[end] == "---":
            return "\n" * (end + 1) + "\n".join(lines[end + 1 :])
    return text


def soft_breaks(text: str) -> list[int]:
    """Return the 1-based first line of each paragraph that has a soft line break."""
    return [
        token.map[0] + 1
        for token in PARSER.parse(blank_front_matter(text))
        if token.type == "inline"
        and token.map is not None
        and any(child.type == "softbreak" for child in token.children or [])
    ]


def main() -> int:
    errors = []
    for path in markdown_files():
        text = (ROOT / path).read_text(encoding="utf-8")
        for line in soft_breaks(text):
            errors.append(
                f"{path}:{line}: soft line break in the paragraph that starts here: "
                "end each of its lines but the last with a backslash, "
                "or separate them with a blank line"
            )
    for error in errors:
        print(error)
    if errors:
        print(f"\n{len(errors)} soft line break(s)")
        return 1
    print("No soft line breaks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
