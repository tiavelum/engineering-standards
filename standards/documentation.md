---
id: documentation
title: Documentation
version: 6.1.0
status: active
applies_to: [all]
summary: "Documentation beyond the README: where it lives, open items, decision records, comments, change notes."
---

# Documentation

Prefix: `DOC`

## Placement

**DOC-1** Documentation MUST live in the repository it describes.

**DOC-2** Documentation beyond the README SHOULD live in `docs/`, one topic per file, named per `NAM-2`.

**DOC-3** A fact MUST have exactly one home. Where it is needed elsewhere, it MUST be linked, not copied.

**DOC-4** Reference material that can be generated from source MUST be generated, not written by hand.

## Writing

**DOC-5** Documentation MUST be written for the reader who will act on it.

**DOC-35** Documentation MUST state what the reader does, not what the author did.

**DOC-6** Documentation MUST describe the current state.

Historical narrative belongs in git history and, where it matters, in a decision record.

**DOC-7** Every document MUST open with one sentence stating what it covers and for whom.

**DOC-8** Instructions MUST be verifiable: a reader can follow them and observe the stated result.

**DOC-9** A document MUST NOT be published with TODOs, placeholders or empty sections.

**DOC-33** A file in a repository MUST refer to the repository's owner by the owner's account handle or not at all, and MUST NOT use the owner's personal name.

Correct: `octocat's repositories`
Incorrect: `Mona's repositories`

## Language

**DOC-30** A repository's README and its other documentation MUST be written in English.

**DOC-31** Content whose language is part of what it is MUST be exempt from DOC-30.

DOC-30 governs documentation about the repository. A German CV or a German handbook is the repository's content, and its language is the point of it.

**DOC-32** Documentation that already exists in another language MUST keep that language until the repository's owner asks for a translation.

## Open items

An open item is any identified piece of future work: a defect to fix, a change to make, a question to answer, or an intent to act on later. It is distinct from a record of the current state, which describes how things are rather than what remains to be done.

**DOC-21** An open item MUST be recorded as a GitHub issue on the repository it concerns.

**DOC-22** An open item MUST NOT be recorded in a file committed to the repository. A file whose purpose is to list outstanding work, such as `open-items.md`, `todo.md` or `backlog.md`, MUST NOT exist.

Such a file has to be pruned by hand. In practice it is not, and it becomes the stale document that DOC-20 calls a defect. A GitHub issue closes itself when the pull request that resolves it is merged, so the list stays accurate without anyone maintaining it.

The prohibition covers the file's purpose, not its name. A file listing outstanding work is forbidden whatever it is called; a file whose name happens to resemble one of the examples but which records the current state is not.

**DOC-23** The following MUST be treated as records of the current state rather than open items, governed by their own rules rather than by DOC-21 and DOC-22: the deviations file required by PR-5, the known limitations required by RM-18, and decision records under DOC-10.

**DOC-24** An issue MUST state what is to be done and why, in terms a reader who was not present when it was raised can act on.

**DOC-25** A pull request that resolves an issue MUST reference that issue with a closing keyword, so that merging the pull request closes the issue.

**DOC-26** Work that spans several issues SHOULD be held by one tracking issue stating the intent and the method, linking each child issue as it is opened.

These rules name GitHub because that is where these repositories live. A repository hosted elsewhere uses the equivalent issue tracker of its host; what the rules require is the mechanism, not the vendor.

## Decision records

**DOC-10** A decision that constrains future work and is not obvious from the code MUST be recorded as a decision record in `docs/decisions/`.

**DOC-11** A decision record MUST be named `<nnnn>-<short-title>.md` with a zero padded sequence number.

**DOC-36** A decision record MUST contain: context, the decision, the alternatives considered, and the consequences.

**DOC-12** A decision record MUST NOT be edited after acceptance except to mark it superseded and name its successor.

## Comments in source

**DOC-13** A comment MUST explain why, not what. A comment restating the code MUST be removed.

**DOC-14** A comment marking a known compromise MUST state the condition under which it can be removed.

**DOC-15** Commented out code MUST NOT be committed.

## Change notes

**DOC-16** Change notes MUST be published as the notes of the GitHub release they describe, and MUST NOT be kept in a committed file.

A changelog file repeats what the release holds and has to be kept in step with it by hand. The release is created once, with the tag it describes.

**DOC-17** Release notes MUST be written for the user of the release: what changed for them, what breaks, what they must do.

**DOC-18** Release notes MUST NOT be a dump of commit messages.

## Maintenance

**DOC-19** A change that invalidates a document MUST update that document in the same pull request.

**DOC-20** A document that no longer describes reality MUST be corrected or deleted.

Leaving it in place is a defect.
