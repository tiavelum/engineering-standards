---
id: documentation
title: Documentation
version: 10.0.0
status: active
applies_to: [all]
summary: "Rules for every document of a repository, the README included: placement, writing, language, open items, directory READMEs, decision records, comments in source, change notes and maintenance."
---

# Documentation

Prefix: `DOC`

## Placement

**DOC-1** Documentation MUST live in the repository it describes.

**DOC-2** Documentation beyond the README SHOULD live in `docs/`.

**DOC-37** A file in `docs/` SHOULD cover one topic.

NAM-2 governs the name of a file in `docs/`, as it does every file name.

**DOC-3** A fact MUST have exactly one home. Where it is needed elsewhere, it MUST be linked, not copied.

**DOC-4** Reference material that can be generated from source MUST be generated, not written by hand.

## Writing

**DOC-5** Documentation MUST be written for the reader who will act on it.

**DOC-35** Documentation MUST state what the reader does, not what the author did.

**DOC-6** Documentation MUST describe the current state.

Historical narrative belongs in git history and, where it matters, in a decision record.

**DOC-7** Every document MUST open with one sentence stating what it covers and for whom.

**DOC-8** Instructions MUST be verifiable: a reader can follow them and observe the stated result.

**DOC-46** A command the reader runs MUST be given in a fenced code block, not inline in running text.

Correct: "Install the checks:" followed by a fenced block holding `pip install -r requirements.txt`
Incorrect: "Install the checks with `pip install -r requirements.txt` before you start."

**DOC-9** A document MUST NOT be published with TODOs, placeholders or empty sections.

**DOC-33** A file in a repository MUST refer to the repository's owner by the owner's account handle or not at all, and MUST NOT use the owner's personal name.

Correct: `octocat's repositories`
Incorrect: `Mona's repositories`

**DOC-47** A document MUST NOT name the repository's owner.

A document says what the repository does, not whose it is. Where a sentence needs a person, a role such as the user or the developer names them; DOC-33 governs a file that has to name the owner, such as a license.

Correct: `A sailing logbook built from the photos of each charter trip.`
Incorrect: `A logbook of the charter trips octocat skippers.`

## Language

**DOC-30** A repository's README and every other document about the repository MUST be written in English.

A document that is the repository's content rather than about it, such as a German CV or a German handbook, keeps the language that is the point of it.

## Open items

An open item is any identified piece of future work: a defect to fix, a change to make, a question to answer, or an intent to act on later. It is distinct from a record of the current state, which describes how things are rather than what remains to be done, such as a deviation (PR-5), a known limitation (RM-18) or a decision record (DOC-10).

**DOC-21** An open item MUST be recorded as a GitHub issue on the repository it concerns.

**DOC-22** An open item MUST NOT be recorded in a file committed to the repository. A file whose purpose is to list outstanding work, such as `open-items.md`, `todo.md` or `backlog.md`, MUST NOT exist.

Such a file has to be pruned by hand. In practice it is not, and it becomes the stale document that DOC-20 calls a defect. A GitHub issue closes itself when the commits made for it reach the default branch, so the list stays accurate without anyone maintaining it.

The prohibition covers the file's purpose, not its name. A file listing outstanding work is forbidden whatever it is called; a file whose name happens to resemble one of the examples but which records the current state is not.

**DOC-38** An issue's title MUST state the work as an imperative phrase.

Correct: `Split the rules that hold two independent requirements`, `Decide whether source files may sit at the root`
Incorrect: `Rule splitting`, `Source files at the root?`, `Two rules disagree on .editorconfig`

**DOC-24** An issue MUST state what is to be done and why, in terms a reader who was not present when it was raised can act on.

**DOC-39** An issue MUST state the condition under which it is done.

The condition lets anyone close the issue, or see that it is not done yet, without asking its author.

**DOC-40** An issue that asks for a decision MUST list the options it knows, each with its consequence.

**DOC-41** An issue that asks for a decision SHOULD name the option its author recommends, with the reason.

**DOC-42** An issue MUST be written in English.

An issue has the readers of the repository's documentation, which DOC-30 requires in English.

**DOC-43** An issue MUST NOT duplicate an open issue of the same repository.

**DOC-44** An issue closed without commits made for it MUST carry a comment stating how it was resolved.

DOC-25 lets the commits made for an issue record its resolution. An issue resolved any other way, by a decision, a setting or work already done, has no such record unless the comment gives it.

**DOC-25** An issue MUST be closed by a closing keyword that reaches the default branch with the commits made for it.

A pull request carries the keyword in its description; the first commit of a repository, which has no pull request, carries it in its message.

**DOC-26** Work that spans several issues SHOULD be held by one tracking issue that links each of them.

These rules name GitHub because that is where these repositories live. A repository hosted elsewhere uses the equivalent issue tracker of its host; what the rules require is the mechanism, not the vendor.

## Directory READMEs

**DOC-45** A rule that constrains how the content of one directory is built, and is not obvious from that content, MUST be described in the README of that directory.

Whoever changes the content of a directory meets its README first, since a forge shows it below the listing. That README is written for them rather than for the user of the repository, and it describes the current rules of the content, not how they came about.

## Decision records

**DOC-10** A decision that constrains future work across more than one directory and is not obvious from the code MUST be recorded as a decision record in `docs/decisions/`.

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
