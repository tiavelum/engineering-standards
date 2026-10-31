---
id: documentation
title: Documentation
version: 14.0.0
status: active
applies_to: [all]
summary: "Rules for every document of a repository, the README included: where it lives, what it states, manual steps, directory READMEs, decision records, comments in source, release notes and upkeep."
---

# Documentation

This file governs every document of a repository, the README included: where it lives, what it states and how it is kept current.

Prefix: `DOC`

## Placement

### DOC-1

Documentation MUST live in the repository it describes.

### DOC-2

Documentation other than a README SHOULD live in `docs/`.

### DOC-37

A file in `docs/` SHOULD cover one topic.

### DOC-3

A fact MUST have exactly one home among the documents of the repository, as WR-8 defines them; where another document needs it, it MUST be linked, not copied.

### DOC-4

Reference material that can be generated from source MUST be generated, not written by hand.

## Content

### DOC-7

Every document MUST open with one sentence stating what it covers and for whom.

### DOC-35

Documentation MUST state what the reader does, not what the author did.

### DOC-6

Documentation MUST describe the current state.

History belongs in git history. A decision record describes a decision in force, which is current state.

### DOC-8

Instructions MUST be verifiable: a reader can follow them and observe the stated result.

### DOC-46

A command the reader runs MUST stand in a fenced code block, not inline in running text.

> Correct: "Install the checks:" followed by a fenced block holding `pip install -r requirements.txt`
>
> Incorrect: "Install the checks with `pip install -r requirements.txt` before you start."

### DOC-9

A document MUST NOT be published with TODOs, placeholders or empty sections.

## Manual steps

### DOC-48

A pull request that adds a step the user of the repository takes by hand MUST describe that step in the repository's documentation, with the other steps of the task that needs it.

Written down with the change, the step reaches whoever sets the repository up next; left in a conversation, it does not.

## Directory READMEs

### DOC-45

A rule for how the content of a directory is built MUST be documented where that content does not make it obvious.

### DOC-53

A description of files that all lie in one directory below the root MUST stand in the README of the deepest directory that holds them all, except what a rule requires of another document.

> Correct: how `sync/photo-sync.sh` matches photos, in `sync/README.md`; the root README says in one sentence what `sync/` does and links there
>
> Incorrect: the same description in the root README or in `docs/sync.md`

## Decision records

### DOC-10

A decision that constrains future work across more than one directory and is not obvious from the code MUST be recorded as a decision record in `docs/decisions/`.

### DOC-11

A decision record MUST be named `<nnnn>-<short-title>.md` with a zero padded sequence number.

### DOC-36

A decision record MUST contain: context, the decision, the alternatives considered, and the consequences.

### DOC-12

A decision record MUST NOT be edited after acceptance except to mark it superseded and name its successor.

## Comments in source

### DOC-13

A comment MUST explain why, not what.

### DOC-14

A comment marking a known compromise MUST state the condition under which it can be removed.

### DOC-15

Commented out code MUST NOT be committed.

## Release notes

### DOC-16

Release notes MUST be published as the notes of the GitHub release they describe, not kept in a committed file.

A committed changelog repeats what the release holds and has to be kept in step with it by hand.

### DOC-17

Release notes MUST be written for the user of the release: what changed for them, what breaks, what they must do.

## Upkeep

### DOC-19

A pull request whose commits invalidate a document MUST update that document.

### DOC-51

Before merge, every link in a document of the repository, other than one written only as an example, MUST resolve: a link outside the repository to its page, a link within it to its path and to the heading its fragment names.
