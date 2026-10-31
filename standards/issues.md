---
id: issues
title: Issues
version: 5.0.0
status: active
applies_to: [all]
summary: When work becomes an issue, what an issue states, and how it is closed.
---

# Issues

This file governs the issues of a repository: when work becomes an issue, what the issue states, and how it is closed.

Prefix: `ISS`

An open item is work identified and not yet done, such as a defect to fix, a change to make or a question to answer; a record of how things are, such as a deviation (PR-5), is not one.

## Recording

### ISS-1

An open item MUST be recorded as an issue of the repository it concerns.

### ISS-2

An open item MUST NOT be recorded in a file of the repository, such as `todo.md` or `backlog.md`.

Such a file has to be pruned by hand and goes stale; an issue is closed with the change that settles it.

### ISS-3

An issue MUST NOT duplicate an open issue of the same repository.

### ISS-10

Work that spans several issues SHOULD be held by one tracking issue that links each of them.

## Content

WR-10 sets how an issue's description opens: with what the work is and why.

### ISS-4

An issue's title MUST state the work as an imperative phrase.

> Correct: `Split the rules that hold two independent requirements`, `Decide whether source files may sit at the root`
>
> Incorrect: `Rule splitting`, `Source files at the root?`, `Two rules disagree on .editorconfig`

### ISS-6

An issue MUST state the condition under which it is done.

The condition lets anyone see whether the issue is done without asking its author.

### ISS-7

An issue that asks for a decision MUST list its options, each with its consequence, and recommend one of them, with the reason.

## Closing

### ISS-12

An issue closed without a merged change MUST carry a comment that states how it was resolved.

An issue resolved by a decision, a setting or work already done has no other record of its resolution.
