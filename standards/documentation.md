---
id: documentation
title: Documentation
version: 13.2.3
status: active
applies_to: [all]
summary: "Rules for every document of a repository, the README included: placement, content, manual steps, directory READMEs, decision records, comments in source, change notes and maintenance."
---

# Documentation

Prefix: `DOC`

## Placement

### DOC-1

Documentation MUST live in the repository it describes.

### DOC-2

Documentation beyond the README SHOULD live in `docs/`.

### DOC-37

A file in `docs/` SHOULD cover one topic.

NAM-2 governs the name of a file in `docs/`, as it does every file name.

### DOC-3

A fact MUST have exactly one home. Where it is needed elsewhere, it MUST be linked, not copied.

### DOC-4

Reference material that can be generated from source MUST be generated, not written by hand.

## Content

WR-1 governs the language of a document, WR-6 how it names a person, and WR-8 and WR-9 how it links a source outside the repository.

### DOC-35

Documentation MUST state what the reader does, not what the author did.

### DOC-6

Documentation MUST describe the current state.

Historical narrative belongs in git history. A decision record describes a decision that is in force, which is current state.

### DOC-7

Every document MUST open with one sentence stating what it covers and for whom.

### DOC-8

Instructions MUST be verifiable: a reader can follow them and observe the stated result.

### DOC-46

A command the reader runs MUST be given in a fenced code block, not inline in running text.

> Correct: "Install the checks:" followed by a fenced block holding `pip install -r requirements.txt`
>
> Incorrect: "Install the checks with `pip install -r requirements.txt` before you start."

### DOC-9

A document MUST NOT be published with TODOs, placeholders or empty sections.

## Manual steps

### DOC-48

A step that the user of the repository has to take by hand for what it delivers to work, because no committed tool performs it, MUST be described in a document of the repository.

### DOC-49

The description DOC-48 requires MUST be added by the pull request whose commits make the step necessary.

Such a step usually comes to light while the change is tested. Written down with the change, it reaches whoever sets the repository up next; left in a conversation or a review comment, it does not. A step taken only to develop or debug the change is not a step of what the repository delivers.

### DOC-50

The description DOC-48 requires MUST stand in the section that gives the steps of the task that needs the step, in whichever document of the repository that section is; where a first result needs the step, that section is the README's "Getting started" (RM-1).

"Getting started" has to be usable on its own (RM-8), and a step a first result needs that stands elsewhere leaves it incomplete. RM-34 sets the form the step takes there.

> Correct: signing in to the sync account of photo-sync, which its first run needs, described in "Getting started"; granting photo-sync access to the Photos library, which only the import that `docs/import.md` describes needs, described in the section of `docs/import.md` that gives the steps of the import
>
> Incorrect: the same sign-in described only in `docs/accounts.md`; the same access described only in the README's "Getting started", though a first result does not need it

## Directory READMEs

### DOC-45

A rule that constrains how the content of one directory is built, and is not obvious from that content, MUST be described in the README of that directory.

The README of a directory is written for whoever uses or changes the content of that directory. It holds the details of that content that the README at the root leaves out, such as what a program in it prints and does when it cannot complete its task (DOC-52), and it describes the current rules of the content, not how they came about.

### DOC-52

A description, in a document of the repository, of what a program prints and does when it cannot complete its task, where the files of the repository that make up the program or that it runs or reads all lie within one directory below the root, MUST stand in the README of the deepest directory that holds them all.

The README at the root shows what works and links to these details (RM-41), so it stays short. The output of a program tells its user, as it happens, that it cannot complete its task; the README of its directory is for whoever wants more without reading the program. A program is outside this rule where no directory below the root holds all those files, as where one of them lies at the root. That a program prints a line about a step the user takes by hand or about a known limitation does not move it into the README of the directory: DOC-50 places the step, where a first result needs it, in the README's "Getting started" at the root, and RM-18 has the README state the limitation where it affects whether a reader should use the repository.

> Correct: what `sync/photo-sync.sh` prints, and which photos it has already copied, when the Photos library cannot be read, described in `sync/README.md`
>
> Incorrect: the same described in the "Troubleshooting" of the README at the root, or in `docs/troubleshooting.md`

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

## Change notes

### DOC-16

Change notes MUST be published as the notes of the GitHub release they describe, and MUST NOT be kept in a committed file.

A changelog file repeats what the release holds and has to be kept in step with it by hand. The release already holds the notes, so a second copy only adds work and a place where the two can differ.

### DOC-17

Release notes MUST be written for the user of the release: what changed for them, what breaks, what they must do.

## Maintenance

### DOC-19

A pull request whose commits invalidate a document MUST update that document.

### DOC-51

Every link in a document of the repository, as WR-8 defines it, other than a link written only as an example, MUST resolve before merge: a link within the repository to the path it names and, where it has a fragment, to the heading the fragment names; a link to a page outside the repository to that page.

A link that does not resolve sends its reader nowhere, and WR-8 puts links to outside sources into every document, not only the README. A heading of the repository's own files is what its changes break, and a tool can check it in every link within the repository; the fragment of a link to an outside page is not part of what has to resolve, since checking it means fetching and parsing each page. A link written only as an example, such as `[LICENSE](LICENSE)` in a sample README that a document shows in a code block, is not followed by a reader.

> Correct: a link in `docs/setup.md` to `https://semver.org/spec/v2.0.0.html`, which opens the specification when the pull request is merged; a link in the README to `docs/setup.md#install-the-tools`, where `docs/setup.md` has the heading "Install the tools"
>
> Incorrect: the same link after the page has moved, so that it returns "404 Not Found" when the pull request is merged; the same link to `docs/setup.md#install-the-tools` after the pull request renames that heading to "Tools"
