---
id: naming
title: Naming
version: 7.0.0
status: active
applies_to: [all]
summary: Names for files, directories, branches, tags and repositories.
---

# Naming

This file governs the names of files, directories, repositories, branches and tags.

Prefix: `NAM`

## Files, directories and repositories

### NAM-1

The name of a file, directory or repository MUST describe what the thing is, not when it was made, who made it or what was done to it.

A date, version or number is part of what a thing is where the thing is about it, or where it tells the thing apart from others of its kind in use beside it.

> Correct: `design.md`, `q3-tax-rates.md` in a tax engine, `api/v2/` beside `api/v1/`, `0004-use-postgres.md` as a decision record
>
> Incorrect: `report-v2.md`, `notes-final.md`, `sprint-4-notes.md`, a directory named `misc` or `temp`, `octocat-tools` for a repository of the account octocat

### NAM-2

A file, directory or repository name that no tool or convention fixes MUST consist, apart from a file's extension, of lowercase words of `a-z` and `0-9` separated by single hyphens.

A name a tool or convention fixes keeps its form, such as `README.md`, `LICENSE`, `Dockerfile` or `.editorconfig`.

> Correct: `crew-handbook.md`, `api-reference.md`, `engineering-standards`
>
> Incorrect: `Crew Handbook.md`, `crew_handbook.md`, `crewHandbook.md`

### NAM-17

A file whose name, apart from its extension and in any casing, is `readme` MUST be the README of the directory that holds it.

A reader takes such a file for the README of its directory.

> Correct: `standards/readme-contract.md` for a standard about READMEs
>
> Incorrect: `standards/readme.md` for the same file

### NAM-10

A repository name SHOULD be a noun phrase naming the artifact, not a sentence or an action.

> Correct: `engineering-standards`, `sailing-trip-doc`
>
> Incorrect: `this-tool-syncs-photos`, `do-the-thing`

## Branches

### NAM-12

A branch other than the default branch or a release branch MUST be named `<type>/<issue>-<description>`: `<type>` a type GW-6 allows, `<issue>` the number of one of the issues its work is for, `<description>` at most five words in the form of NAM-2.

> Correct: `fix/142-broken-links`, `feat/88-index-schema`
>
> Incorrect: `my-branch`, `feature/AddNewIndexSchema`, `fix/broken-links`

## Tags

### NAM-16

A tag MUST NOT be moved once pushed.
