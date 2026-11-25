---
id: documentation
title: Documentation
version: 18.0.0
status: active
applies_to: [all]
summary: "Rules for every document of a repository, the README included: where it lives, what it states, manual steps, directory READMEs, comments in source, release notes and upkeep."
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

Every document written for people MUST state what it covers and for whom in its first sentence, or in its front matter where its format begins with one.

### DOC-35

Documentation MUST state what the reader does, not what the author did.

### DOC-6

Documentation MUST describe the current state.

History belongs in git history.

### DOC-54

A document that states a constraint its subject does not make obvious MUST give the reason for it in a clause that links to the issue that decided it.

Whoever changes the work meets the constraint and its reason where they work, and the alternatives keep one home: the issue, which stays as answered when a later issue changes the decision.

> Correct: `Labels are created before the issues, since an issue replayed before its label loses it ([octocat/tool#62](https://github.com/octocat/tool/issues/62)).` in `replay/README.md`
>
> Incorrect: `Labels are created before the issues, since an issue replayed before its label loses it.` with no link to the issue, or the reason only in `docs/decisions/0002-create-labels-first.md`

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

A pull request that adds a step the user of the repository takes by hand, or that serves the issue of a run of a documented task, MUST describe in the documentation, with the other steps of that task, each step it adds or the run took by hand.

Written down with the change, the step reaches whoever sets the repository up or runs the task next; left in a conversation or in the notes of a run, it does not.

> Correct: the pull request for `Run: replay octocat/tool into octocat/tool-new` adds the step the run took by hand, turning off Actions in the target, to `replay/README.md`
>
> Incorrect: the same pull request fixes only the script the run stopped in, and turning off Actions stays in the run's issue

## Directory READMEs

### DOC-45

A rule for how the content of a directory is built MUST be documented where that content does not make it obvious.

### DOC-53

A description of files that all lie in one directory below the root MUST stand in the README of the deepest directory that holds them all, except what a rule requires of another document.

> Correct: how `sync/photo-sync.sh` matches photos, in `sync/README.md`; the root README says in one sentence what `sync/` does and links there
>
> Incorrect: the same description in the root README or in `docs/sync.md`

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
