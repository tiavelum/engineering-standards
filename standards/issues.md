---
id: issues
title: Issues
version: 1.1.0
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

Such a file has to be pruned by hand. In practice it is not, and it becomes the stale document that DOC-6 rules out. A GitHub issue closes itself when the commits made for it reach the default branch, so the list stays accurate without anyone maintaining it.

The prohibition covers the file's purpose, not its name. A file listing outstanding work is forbidden whatever it is called; a file whose name happens to resemble one of the examples but which records the current state is not.

**ISS-3** An issue MUST NOT duplicate an open issue of the same repository.

## Content

**ISS-4** An issue's title MUST state the work as an imperative phrase.

Correct: `Split the rules that hold two independent requirements`, `Decide whether source files may sit at the root`
Incorrect: `Rule splitting`, `Source files at the root?`, `Two rules disagree on .editorconfig`

**ISS-5** An issue MUST state what is to be done and why, in terms a reader who was not present when it was raised can act on.

**ISS-6** An issue MUST state the condition under which it is done.

The condition lets anyone close the issue, or see that it is not done yet, without asking its author.

**ISS-13** An issue that defers its work MUST state the condition under which the work becomes due, and MUST NOT give a date as that condition.

The condition lets anyone see that the wait is over without asking the author; a date passes whether or not the work has become necessary.

Correct: `Due when a second repository needs the same check`
Incorrect: `Due in January 2027`, `Revisit in three months`

**ISS-7** An issue that asks for a decision MUST list the options it knows, each with its consequence.

**ISS-8** An issue that asks for a decision SHOULD name the option its author recommends, with the reason.

**ISS-9** An issue MUST be written in English.

An issue has the readers of the repository's documentation, which DOC-30 requires in English.

**ISS-10** Work that spans several issues SHOULD be held by one tracking issue that links each of them.

## Closing

**ISS-11** An issue MUST be closed by a closing keyword that reaches the default branch with the commits made for it.

A pull request carries the keyword in its description; the first commit of a repository, which has no pull request, carries it in its message.

**ISS-12** An issue closed without commits made for it MUST carry a comment stating how it was resolved.

ISS-11 lets the commits made for an issue record its resolution. An issue resolved any other way, by a decision, a setting or work already done, has no such record unless the comment gives it.
