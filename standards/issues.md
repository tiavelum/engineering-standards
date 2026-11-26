---
id: issues
title: Issues
version: 7.0.0
status: active
applies_to: [all]
summary: When work becomes an issue, what an issue states, how it is labelled while it waits on a person, and how it is closed.
---

# Issues

This file governs the issues of a repository: when work becomes an issue, what an issue states, how it is labelled while it waits on a person, and how it is closed.

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

Work that spans several issues SHOULD be held by one tracking issue that lists each of them as an item of a task list in its description, ticked once that issue closes.

> Correct: `- [x] #407` and `- [ ] #410` in the description of the tracking issue
>
> Incorrect: the issues linked in running text, with their state reported in comments

### ISS-20

An issue other than a tracking issue of ISS-10 MUST be completed by at most one pull request.

Work that needs more pull requests is split into issues first, so that each issue closes with the change that completes it.

### ISS-19

Each run of a procedure that a repository's documentation describes for running more than once, such as a migration, a machine setup or the replay of a repository, SHOULD be recorded in an issue of its own that holds the run's inputs, its state and what it hit.

Whoever takes over a stopped run resumes it from that issue, and the next run learns from it; a tracking issue under ISS-10 holds work across issues, not one run.

> Correct: `Run: replay octocat/tool into octocat/tool-new`, holding the options chosen, each stop with its cause and fix, and the result of the check
>
> Incorrect: the same run recorded only in comments on the issue that built the replay script, between those on the script's own changes

### ISS-14

A decision that an answer raises MUST be asked in a new issue.

The answered issue closes once its answer is carried out, and a question added to it would close with it.

## Content

WR-10 sets how an issue's description opens: with what the work is and why.

### ISS-4

An issue's title MUST state the work as an imperative phrase.

> Correct: `Split the rules that hold two independent requirements`, `Decide whether source files may sit at the root`
>
> Incorrect: `Rule splitting`, `Source files at the root?`, `Two rules disagree on .editorconfig`, `Refactor: split the rules on branch names`

### ISS-6

An issue MUST state the condition under which it is done.

The condition lets anyone see whether the issue is done without asking its author.

### ISS-21

An issue whose done condition names more than one piece of work MUST list them in its description as a task list, each item ticked once its change is merged or its decision carried out, and MUST NOT report that progress in a comment instead.

Whoever opens the issue sees what is left without reading its comments.

### ISS-7

An issue that asks for a decision MUST list its options, numbered, each with its consequence, and recommend one of them by its number, with the reason.

### ISS-13

An issue that asks for a decision MUST ask for exactly one.

One decision per issue lets each be answered, carried out and closed on its own.

## Waiting on a person

### ISS-15

An issue that waits on a decision only one person can make MUST carry the label `<handle>-decides`, with that person's handle on the forge.

> Correct: `octocat-decides`
>
> Incorrect: `needs-decision`, `decides-octocat`

### ISS-16

An issue that waits on a step only one person can take MUST carry the label `<handle>-acts`, with that person's handle on the forge.

> Correct: `octocat-acts`
>
> Incorrect: `waiting`, `action-needed`

### ISS-17

An issue whose awaited answer or report has been read MUST carry the label `answer-acknowledged` beside the label of ISS-15 or ISS-16.

The first label still says whose answer it was; the second says nobody waits on that person any more.

## Closing

### ISS-12

An issue closed without a merged change MUST carry a comment that states how it was resolved.

An issue resolved by a decision, a setting or work already done has no other record of its resolution.
