---
id: git-workflow
title: Git workflow
version: 1.0.0
status: active
applies_to: [all]
summary: Branching, commit messages, pull requests and history hygiene.
---

# Git workflow

Prefix: `GW`

## Branches

**GW-1** `main` MUST always be in a working state. Anything merged to `main` runs.

**GW-2** Work MUST happen on a branch named per `NAM-12`, not directly on `main`, unless the repository is single author and the change is trivial.

**GW-3** A branch MUST address one concern. A branch that grows a second concern MUST be split.

**GW-4** A merged branch MUST be deleted.

## Commits

**GW-5** A commit MUST leave the repository in a working state.

**GW-6** A commit message MUST take the form `<type>: <summary>`, where `<type>` is one of `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

**GW-7** The summary MUST be imperative, lowercase after the type, at most 72 characters, and MUST NOT end with a period.

Correct: `docs: add consumer contract to meta layer`
Incorrect: `Added consumer contract.`, `updates`, `wip`

**GW-8** A commit message MUST describe what changed and, where not obvious, why. It MUST NOT describe the process of arriving at the change.

**GW-9** A commit body MUST be used when the summary cannot carry the reason. It is separated from the summary by a blank line and wrapped at 72 characters.

**GW-10** A commit MUST NOT mix unrelated changes.

**GW-11** Commit messages MUST NOT contain `wip`, `misc`, `stuff`, `fixes`, or a bare file name.

## Pull requests

**GW-12** A pull request description MUST state what changes and why, in terms a reviewer who did not write it can follow.

**GW-13** A pull request that changes a documented convention MUST update the documentation in the same pull request.

**GW-14** A pull request MUST NOT be merged with failing checks.

**GW-15** A pull request SHOULD stay small enough to review in one sitting. Large mechanical changes SHOULD be separated from behavioural ones.

## History

**GW-16** History on a shared branch MUST NOT be rewritten. Force pushing to `main` is prohibited.

**GW-17** A local branch MAY be rebased or squashed before it is shared.

**GW-18** A mistake in a shared branch MUST be corrected with a new commit, not by rewriting.

**GW-19** A committed secret MUST be treated as compromised and rotated. Removing it from history does not undo the exposure.
