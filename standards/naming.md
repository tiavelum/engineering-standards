---
id: naming
title: Naming
version: 6.0.0
status: active
applies_to: [all]
summary: Names for files, directories, branches, tags and repositories.
---

# Naming

Prefix: `NAM`

## General

**NAM-1** A name MUST describe what the thing is, not when it was made, who made it, or what was done to it.

A date or period belongs in a name only where it is what the thing is about. A version, a status, a step of the work or the owner says when the thing was made, what was done to it or who made it; version control and the account hold those.

Correct: `design.md`, `retrospective.md`, `august.md` in a calendar application, `q3-tax-rates.md` in a tax engine whose data those rates are
Incorrect: `report-v2.md`, `notes-final.md`, `session-notes-august.md`, `sprint-4-notes.md`, `refactor-2026-09.md`, a directory named `misc`, `other`, `stuff`, `temp` or `new`, `octocat-tools` for a repository of the account octocat

**NAM-2** A file, directory or repository name that no tool or convention fixes MUST consist, apart from a file's extension, of lowercase words of `a-z` and `0-9` separated by single hyphens.

A name a tool or convention fixes keeps the form it fixes, for example `README.md`, `LICENSE`, `Dockerfile`, `Makefile`, `CODEOWNERS`, `.editorconfig`.

Correct: `crew-handbook.md`, `api-reference.md`, `engineering-standards`
Incorrect: `Crew Handbook.md`, `crew_handbook.md`, `crewHandbook.md`

**NAM-5** Abbreviations MUST NOT be used unless they are unambiguous in the repository's domain and used consistently.

## Directories

**NAM-7** Directory names MUST be plural when they hold a collection of like items, singular when they hold one thing's parts.

Correct: `standards/`, `templates/`, `docs/`, `build/`
Incorrect: `standard/` holding six standards

**NAM-17** A file MUST NOT be named `readme.md`, in any casing, unless it is the README of the directory that holds it.

Forges render any file named `readme` below a directory listing. A file that borrows that slot gains attention it has not earned and occupies the place a real directory README would take.

Correct: `standards/readme-contract.md` for a standard about READMEs
Incorrect: `standards/readme.md` for the same file

## Repositories

**NAM-10** A repository name SHOULD be a noun phrase naming the artifact, not a sentence or an action.

Correct: `engineering-standards`, `sailing-trip-doc`
Incorrect: `my-stuff`, `do-the-thing`

## Branches

**NAM-12** A branch name MUST take the form `<type>/<issue>-<description>`: `<type>` one of the types `GW-6` allows, `<issue>` the number of the issue its commits are made for, and `<description>` at most five words in the form of NAM-2.

Correct: `fix/142-broken-links`, `feat/88-index-schema`
Incorrect: `my-branch`, `feature/AddNewIndexSchema`, `fix/broken-links`

## Tags

**NAM-16** A tag MUST NOT be moved once pushed.
