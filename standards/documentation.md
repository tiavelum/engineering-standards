---
id: documentation
title: Documentation
version: 1.0.0
status: active
applies_to: [all]
summary: "Documentation beyond the README: where it lives, decision records, comments, changelogs."
---

# Documentation

Prefix: `DOC`

## Placement

**DOC-1** Documentation MUST live in the repository it describes.

**DOC-2** Documentation beyond the README MUST live in `docs/`, one topic per file, named per `NAM-2`.

**DOC-3** A fact MUST have exactly one home. Where it is needed elsewhere, it MUST be linked, not copied.

**DOC-4** Reference material that can be generated from source MUST be generated, not written by hand.

## Writing

**DOC-5** Documentation MUST be written for the reader who will act on it, and MUST state what the reader does, not what the author did.

**DOC-6** Documentation MUST describe the current state. Historical narrative belongs in git history and, where it matters, in a decision record.

**DOC-7** Every document MUST open with one sentence stating what it covers and for whom.

**DOC-8** Instructions MUST be verifiable: a reader can follow them and observe the stated result.

**DOC-9** A document MUST NOT be published with TODOs, placeholders or empty sections.

## Decision records

**DOC-10** A decision that constrains future work and is not obvious from the code MUST be recorded as a decision record in `docs/decisions/`.

**DOC-11** A decision record MUST be named `<nnnn>-<short-title>.md` with a zero padded sequence number, and MUST contain: context, the decision, the alternatives considered, and the consequences.

**DOC-12** A decision record MUST NOT be edited after acceptance except to mark it superseded and name its successor.

## Comments in source

**DOC-13** A comment MUST explain why, not what. A comment restating the code MUST be removed.

**DOC-14** A comment marking a known compromise MUST state the condition under which it can be removed.

**DOC-15** Commented out code MUST NOT be committed.

## Changelog

**DOC-16** A repository with releases MUST keep a `CHANGELOG.md`, grouped by version, newest first.

**DOC-17** A changelog entry MUST be written for the user of the release: what changed for them, what breaks, what they must do.

**DOC-18** A changelog MUST NOT be a dump of commit messages.

## Maintenance

**DOC-19** A change that invalidates a document MUST update that document in the same pull request.

**DOC-20** A document that no longer describes reality MUST be corrected or deleted. Leaving it in place is a defect.
