---
id: naming
title: Naming
version: 1.2.0
status: active
applies_to: [all]
summary: Names for files, directories, branches, tags and repositories.
---

# Naming

Prefix: `NAM`

## General

**NAM-1** A name MUST describe what the thing is, not when it was made, who made it, or what was done to it.

**NAM-2** File and directory names MUST use lowercase words separated by single hyphens.

Correct: `crew-handbook.md`, `api-reference.md`, `repo-layout.md`
Incorrect: `Crew Handbook.md`, `crew_handbook.md`, `crewHandbook.md`

**NAM-3** Names MUST NOT contain spaces, underscores, camelCase, or characters outside `a-z`, `0-9` and `-`.

**NAM-4** A name MUST NOT carry a version, date or status suffix such as `-v2`, `-final`, `-new`, `-old`, `-2026-09`. Version control holds that information. A date that identifies the subject rather than the revision is permitted under NAM-18.

**NAM-5** Abbreviations MUST NOT be used unless they are unambiguous in the repository's domain and used consistently.

**NAM-6** Files whose name is fixed by an external tool or convention are exempt from NAM-2 and NAM-3. Examples: `README.md`, `LICENSE`, `Dockerfile`, `Makefile`, `CODEOWNERS`, `.editorconfig`.

## Dates and periods

**NAM-18** A date or period MAY appear in a name only where it is subject matter of what the repository is about.

A time word earns its place when the thing being named genuinely is that period. `august.md` in a calendar application names a month the application is about. The test: the name would mean the same to someone who knows the domain and nothing whatsoever about how or when the work was done.

Correct: `august.md` in a calendar application, `q3-tax-rates.md` in a tax engine where those rates are the data

**NAM-19** A name MUST NOT refer to when work was done, nor to a unit of the development process or a term from a development methodology.

This is the stricter half and it is absolute. A name is not a place to record that something happened last August, belonged to a particular sprint, or came out of a given phase. That information is in the history, and putting it in a name fixes a moment of the process onto an artifact that outlives it.

Incorrect: `session-notes-august.md`, `notes-august.md`, `refactor-2026-09.md`, `sprint-4-notes.md`, `iteration-2-plan.md`, `phase-3-layout.md`, `milestone-2-scope.md`

## Directories

**NAM-7** Directory names MUST be plural when they hold a collection of like items, singular when they hold one thing's parts.

Correct: `standards/`, `templates/`, `docs/`, `build/`
Incorrect: `standard/` holding six standards

**NAM-8** A directory MUST NOT be named `misc`, `other`, `stuff`, `temp` or `new`.

**NAM-17** A file MUST NOT be named `readme.md`, in any casing, unless it is the README of the directory that holds it.

Forges render any file named `readme` below a directory listing. A file that borrows that slot gains attention it has not earned and occupies the place a real directory README would take.

Correct: `standards/readme-contract.md` for a standard about READMEs
Incorrect: `standards/readme.md` for the same file

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
