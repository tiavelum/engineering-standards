---
id: issues
title: Issues
version: 2.1.0
status: active
applies_to: [all]
summary: When future work is recorded as an issue, what an issue states, and how it is closed.
---

# Issues

This file governs the issues of a repository for everyone who opens, works on or closes one: when future work becomes an issue, what the issue states, and how it ends.

Prefix: `ISS`

An open item is any identified piece of future work: a defect to fix, a change to make, a question to answer, or an intent to act on later. It is distinct from a record of the current state, which describes how things are rather than what remains to be done, such as a deviation (PR-5), a known limitation (RM-18) or a decision record (DOC-10).

These rules name GitHub because that is where these repositories live. A repository hosted elsewhere uses the equivalent issue tracker of its host; what the rules require is the mechanism, not the vendor.

## Recording

**ISS-1** An open item MUST be recorded as a GitHub issue on the repository it concerns.

**ISS-2** An open item MUST NOT be recorded in a file committed to the repository. A file whose purpose is to list outstanding work, such as `open-items.md`, `todo.md` or `backlog.md`, MUST NOT exist.

Such a file has to be pruned by hand. In practice it is not, and it becomes the stale document that DOC-6 rules out. A GitHub issue [closes itself](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) when the commits made for it reach the default branch, so the list stays accurate without anyone maintaining it.

The prohibition covers the file's purpose, not its name. A file listing outstanding work is forbidden whatever it is called; a file whose name happens to resemble one of the examples but which records the current state is not.

**ISS-3** An issue MUST NOT duplicate an open issue of the same repository.

## Content

WR-1 governs the language of an issue, WR-2 what it states for a reader who was not present when it was written, WR-5 the length of its title, WR-6 the form of a person's name in it and in the comments on it, and WR-7 how its description and the comments on it reference an issue or a pull request.

**ISS-4** An issue's title MUST state the work as an imperative phrase.

Correct: `Split the rules that hold two independent requirements`, `Decide whether source files may sit at the root`
Incorrect: `Rule splitting`, `Source files at the root?`, `Two rules disagree on .editorconfig`

**ISS-13** An issue's description MUST open with a section headed `In short` that states in at most three sentences what WR-2 requires the issue to state.

WR-2 sets what an issue states; this rule sets where its reader finds it and how long it takes to read. Besides whoever does or decides the work, an issue is read in lists by someone choosing what to read next, and both learn from its first lines what it is about. Sentences are counted rather than lines, which depend on the width of the screen, and the fixed heading lets a tool or an issue template find the section.

Correct: a description that opens with a section headed `In short` that reads `photo-sync copies every photo again after the Photos library is moved, because it recognises a photo by its path. Decide whether it recognises photos by a checksum instead, which makes its first run after the change read every photo once.`
Incorrect: the two sentences of the correct example under the heading `Summary`; the same section after a section headed `Logs` that holds the pasted error output `photo-sync: error: 12400 photos not found at their recorded path`; the same section followed by the sentences `Python's hashlib would compute the checksum. Its code would live in sync/checksum.py.`, four sentences in all; a section headed `In short` that reads only `Decide whether photo-sync recognises photos by a checksum.`, which leaves out why

**ISS-15** The `In short` section of an issue MUST be written in words that a reader who has not followed the work understands without opening a link.

The section is what a reader takes in before deciding whether to read on; a term or identifier that only a link explains makes them open the link first.

Correct: the `In short` section of the ISS-13 example
Incorrect: a section headed `In short` that reads `The path key from #41 (Add the import) breaks on a relocated library, as finding F3 of its review shows. Decide whether to replace it.`, which needs #41 and its review opened

**ISS-6** An issue MUST state the condition under which it is done.

The condition lets anyone close the issue, or see that it is not done yet, without asking its author.

**ISS-7** An issue that asks for a decision MUST list the options it knows, each with its consequence.

**ISS-8** An issue that asks for a decision SHOULD name the option its author recommends, with the reason.

**ISS-14** An issue that asks for a decision MUST show the case it decides in at least one concrete example.

Options stated in general terms, or by the identifiers of the rules they touch, leave whoever decides to picture the case alone; an example of the case shows what each option does to it.

Correct: `After the Photos library moved from the internal disk to the external disk Photos-2, the next run of photo-sync copied all 12 400 photos again and filled the backup drive.` in the issue of the ISS-13 example
Incorrect: `Moving the library has side effects on the sync.`, or the same issue with its options and no example

**ISS-10** Work that spans several issues SHOULD be held by one tracking issue that links each of them.

## Closing

**ISS-11** An issue MUST be closed by a closing keyword that reaches the default branch with the commits made for it.

A pull request carries [the keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) in its description; the first commit of a repository, which has no pull request, carries it in its message.

**ISS-12** An issue closed without commits made for it MUST carry a comment stating how it was resolved.

ISS-11 lets the commits made for an issue record its resolution. An issue resolved any other way, by a decision, a setting or work already done, has no such record unless the comment gives it.
