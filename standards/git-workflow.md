---
id: git-workflow
title: Git workflow
version: 10.0.0
status: active
applies_to: [all]
summary: How a change reaches a repository, from the issues it serves through a branch and a pull request to its merge, and the history it leaves.
---

# Git workflow

This file governs how a change reaches a repository: from the issues it serves through a branch and a pull request to its merge, and the history it leaves.

Prefix: `GW`

## Branches

### GW-2

A commit MUST reach the default branch or a release branch through a pull request, once that branch exists.

A repository without commits has no default branch; its first commit creates it.

### GW-4

The head branch of a merged pull request MUST be deleted.

## Pull requests

WR-10 sets how a pull request's description opens: with what the pull request merges and why, for one issue or several.

### GW-29

A pull request MUST be made for one or more issues of its own repository, which its description names.

### GW-41

A pull request MUST NOT carry work for an issue its description does not name.

### GW-6

A pull request's title MUST take the form `<type>: <summary>`, where `<type>` is one of `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`, `revert`.

The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope and with the types limited to this list.

### GW-7

The `<summary>` of a pull request's title MUST begin with a lowercase verb in the imperative and MUST NOT end with a period.

> Correct: `docs: add consumer contract to meta layer`, `fix: correct the README links`
>
> Incorrect: `docs: Added consumer contract.`, `docs: consumer contract`, `updates`, `wip`

### GW-38

A pull request's description MUST carry a closing keyword, such as `Closes #12 (Rename setup.sh to install.sh)`, for each issue whose work the pull request completes.

### GW-39

A pull request's description MUST name a step a reviewer can take to see that the change works, with the result the step shows, where such a step exists.

> Correct: `To check, run ./install.sh --dry-run: it prints the four install steps and exits with status 0.`
>
> Incorrect: `Tested locally.`, `To check, run ./install.sh --dry-run.`

### GW-27

A mechanical change SHOULD be made in a pull request of its own.

A change is mechanical when it changes no behaviour and applies one transformation throughout, such as formatting, a rename or moving files.

### GW-32

A pull request MUST NOT remove, skip or weaken a test while the behaviour the test checks is still required and nothing else checks it.

A test is weakened when it accepts a result it rejected before, such as through a wider tolerance or a looser assertion.

### GW-24

A review of a pull request MUST record its findings on the pull request, not in a committed file.

### GW-14

A pull request MUST NOT be merged until its checks have passed on its last commit.

### GW-37

A step to be taken by hand after the merge, for the change to take effect, MUST be stated in a comment on the pull request, as a command where one performs it.

A comment can be added whenever the step becomes known, without rewriting the description.

## Commits

### GW-40

A squash or merge commit that merging a pull request creates MUST have the pull request's title as its first line, apart from a number the forge appends, and as its body a short summary of the description and the pull request's URL.

### GW-33

A commit that reaches the default branch without a pull request MUST have a first line that GW-6 and GW-7 allow for a title, and a body that states what and why.

Under GW-2 such a commit is the first commit of a repository.

## History

### GW-16

History on the default branch or a release branch MUST NOT be rewritten.

### GW-19

A committed secret MUST be treated as compromised and rotated.

Removing it from history does not undo the exposure.
