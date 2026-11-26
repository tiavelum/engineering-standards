---
id: git-workflow
title: Git workflow
version: 13.0.0
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

A pull request's title MUST take the form `<type>(<scope>)!: <summary>`, where `(<scope>)` and `!` may each be left out, `<type>` is a type of the table of GW-44 and `<scope>` is set by GW-45.

The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), with the types limited to the table of GW-44.

> Correct: `feat: add a rule on scopes`, `fix(replay): keep the labels of closed issues`, `feat!: drop the --legacy flag`
>
> Incorrect: `installer: add zsh`, `Feat: add a rule`, `feat(replay, rewrite): share the gh stub`

### GW-44

A pull request's `<type>` MUST be the type of the first row of the following table whose condition its change meets.

| Type | Condition |
|---|---|
| `revert` | An earlier change is undone |
| `docs` | Only documents about the repository change, such as its README |
| `test` | Only tests change |
| `ci` | Only the CI configuration changes |
| `build` | Only how the repository is built or checked changes, such as its linters and their configuration |
| `style` | Only the formatting of code changes |
| `refactor` | Only the structure of the code changes, and nothing it does |
| `perf` | Only the speed or the resources of what it does change |
| `fix` | Something that did not work as intended now does |
| `feat` | Whoever uses the repository gets something new or different, such as a new alias, a new rule or an app the Brewfile installs |
| `chore` | Anything else, such as a license |

The narrow types come first, so the type says what alone changed, and `feat` takes every other change that whoever uses the repository notices.

> Correct: `feat: install spotify from the brewfile`, `fix: put an empty line before the files of every message`, `docs: fix the clone command in the README`
>
> Incorrect: `chore: install spotify from the brewfile`, `feat: fix the clone command in the README`

### GW-45

A pull request's title MUST NOT carry a scope other than one that "Contributing" of the root README (RM-1) lists, naming a part of the repository that holds every change the pull request makes.

A listed name lets `git log --grep '(replay)'` find every change to that part.

> Correct: `fix(replay): keep the labels of closed issues`, where "Contributing" lists the scope `replay` for `replay/` and `docs/replay/`
>
> Incorrect: the same title where "Contributing" lists no scopes, or where the change also touches `rewrite/`

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

A pull request MUST NOT be merged until every check reported on its last commit has concluded `success`, `neutral` or `skipped`.

A check is a check run or a commit status, whether or not a ruleset requires it; one still running, cancelled or failed has not passed.

> Correct: merging once `test (ubuntu-24.04)` has concluded `success` and a lint job has concluded `skipped`, as its own `if:` decided.
>
> Incorrect: merging while `test (macos-15)` still runs, because no ruleset requires it.

### GW-43

A pull request on whose last commit no check is reported MUST NOT be merged until a person or an AI agent that did not make its change has reviewed it on the pull request.

Without a check, that review is the only test the change gets before it reaches the branch it merges into.

### GW-37

A step to be taken by hand after the merge, for the change to take effect, MUST be stated in a comment on the pull request, as a command where one performs it.

A comment can be added whenever the step becomes known, without rewriting the description.

### GW-42

A pull request that waits on a step only one person can take MUST carry the label of ISS-16.

## Commits

### GW-40

A squash or merge commit that merging a pull request creates MUST have the pull request's title as its first line, apart from a number the forge appends, and as its body, apart from trailers, either nothing or a summary of the description without HTML or the pull request's URL.

The appended number leads to the pull request and its description; tags such as `<details>` show as noise in `git log`, and WR-5 limits the body's length.

> Correct: `gh pr merge 415 --squash --body "Gives each section of a README a fixed heading."`
>
> Incorrect: `gh pr merge 415 --squash --body "$(gh pr view 415 --json body -q .body)"`, which pastes the description, `<details>` sections included

### GW-33

A commit that reaches the default branch without a pull request MUST have a first line that GW-6 and GW-7 allow for a title, and a body that states what and why.

Under GW-2 such a commit is the first commit of a repository.

## History

### GW-16

History on the default branch or a release branch MUST NOT be rewritten.

### GW-19

A committed secret MUST be treated as compromised and rotated.

Removing it from history does not undo the exposure.
