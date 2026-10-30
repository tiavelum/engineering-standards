---
id: naming
title: Naming
version: 7.0.0
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

**NAM-7** A directory name that no tool or convention fixes MUST be plural when the directory holds a collection of like items, singular when it holds one thing's parts.

A name a tool fixes keeps its number as it keeps its form: GitHub [reads issue templates from the directory `.github/ISSUE_TEMPLATE`](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates), a singular name for a collection of templates.

Correct: `standards/`, `templates/`, `docs/`, `build/`
Incorrect: `standard/` holding six standards

**NAM-17** A file MUST NOT be named `readme.md`, in any casing, unless it is the README of the directory that holds it.

A reader takes a file of that name for the README of its directory, and GitHub [surfaces a README it finds in the root, `docs` or `.github` directory](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) to visitors of the repository. A file that borrows the name gains attention it has not earned and occupies the place a real directory README would take.

Correct: `standards/readme-contract.md` for a standard about READMEs
Incorrect: `standards/readme.md` for the same file

## Repositories

**NAM-10** A repository name SHOULD be a noun phrase naming the artifact, not a sentence or an action.

Correct: `engineering-standards`, `sailing-trip-doc`
Incorrect: `this-tool-syncs-photos`, `do-the-thing`

## Branches

**NAM-12** The name of a branch that a pull request is made from MUST take the form `<type>/<issue>-<description>`: `<type>` one of the types `GW-6` allows, `<issue>` the number of the issue its commits are made for, and `<description>` at most five words in the form of NAM-2.

A pull request carries the commits of one issue (GW-31), so the branch it is made from has one issue number to show. The default branch and a release branch (GW-28) are branches a pull request is merged into, not made from.

Correct: `fix/142-broken-links`, `feat/88-index-schema`
Incorrect: `my-branch`, `feature/AddNewIndexSchema`, `fix/broken-links`

## Tags

**NAM-16** A tag MUST NOT be moved once pushed.
