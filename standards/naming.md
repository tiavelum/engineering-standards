---
id: naming
title: Naming
version: 1.0.0
status: active
applies_to: [all]
summary: Names for files, directories, branches, tags and repositories.
---

# Naming

Prefix: `NAM`

## General

**NAM-1** A name MUST describe what the thing is, not when it was made, who made it, or what was done to it.

**NAM-2** File and directory names MUST use lowercase words separated by single hyphens.

Correct: `session-notes-august.md`, `open-actions.md`, `repo-layout.md`
Incorrect: `Session Notes August.md`, `session_notes.md`, `sessionNotes.md`

**NAM-3** Names MUST NOT contain spaces, underscores, camelCase, or characters outside `a-z`, `0-9` and `-`.

**NAM-4** A name MUST NOT carry a version, date or status suffix such as `-v2`, `-final`, `-new`, `-old`, `-2026-09`. Version control holds that information.

**NAM-5** Abbreviations MUST NOT be used unless they are unambiguous in the repository's domain and used consistently.

**NAM-6** Files whose name is fixed by an external tool or convention are exempt from NAM-2 and NAM-3. Examples: `README.md`, `LICENSE`, `Dockerfile`, `Makefile`, `CODEOWNERS`, `.editorconfig`.

## Directories

**NAM-7** Directory names MUST be plural when they hold a collection of like items, singular when they hold one thing's parts.

Correct: `standards/`, `templates/`, `docs/`, `build/`
Incorrect: `standard/` holding six standards

**NAM-8** A directory MUST NOT be named `misc`, `other`, `stuff`, `temp` or `new`.

## Repositories

**NAM-9** A repository name MUST be lowercase, hyphen separated, and readable without the owner prefix.

**NAM-10** A repository name SHOULD be a noun phrase naming the artifact, not a sentence or an action.

Correct: `engineering-standards`, `sailing-trip-doc`
Incorrect: `my-stuff`, `do-the-thing`

**NAM-11** A repository name MUST NOT include the owner's name when the account already provides it.

## Branches

**NAM-12** A branch name MUST take the form `<type>/<short-description>`, where `<type>` is one of `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

**NAM-13** The description part MUST be lowercase, hyphen separated, and at most five words.

Correct: `feat/index-schema`, `fix/broken-readme-links`
Incorrect: `andi-branch`, `feature/AddNewIndexSchema`, `patch-1`

**NAM-14** A branch that resolves a tracked issue SHOULD include the issue number: `fix/142-broken-links`.

## Tags and releases

**NAM-15** Release tags MUST take the form `v<major>.<minor>.<patch>`.

**NAM-16** A tag MUST NOT be moved once pushed.
