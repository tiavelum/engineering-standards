---
id: git-workflow
title: Git workflow
version: 7.0.0
status: active
applies_to: [all]
summary: Branching, commit messages, pull requests and history hygiene.
---

# Git workflow

Prefix: `GW`

## Branches

**GW-2** A commit MUST reach the default branch through a pull request, once the default branch exists.

A repository without commits has no default branch; its first commit creates it.

**GW-29** A commit MUST be made for an issue of the repository it is committed to.

The issue records what the work is before it begins, and `NAM-12` carries its number into the branch name.

**GW-31** A pull request MUST carry only commits made for one issue.

An issue may take several pull requests, for example when its work lands in steps or recurs; a pull request never mixes issues.

**GW-4** A merged branch MUST be deleted.

## Release lines

**GW-20** A release branch MUST exist only while more than one MAJOR line is supported.

**GW-28** A release branch MUST be named `release/<major>.<minor>` or `release/<major>.x`.

**GW-21** A fix MUST be committed to the default branch before it is cherry picked or backported to a release branch.

Fixing a release branch first is how a fix gets lost in the next major line. The commit exists where it was needed and nowhere else, and nothing notices until the line it was missing from ships.

**GW-22** A release branch MUST NOT receive a MAJOR increment.

A MAJOR increment on a maintenance branch contradicts the reason the branch exists. The branch carries a line that consumers chose because it does not break.

## Commits

WR-1 governs the language of a commit message.

**GW-5** A commit MUST leave the repository in a working state.

The tip of the default branch is a commit, so the default branch always works.

**GW-6** A commit message MUST take the form `<type>: <summary>`, where `<type>` is one of `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`, `revert`.

The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope and with the types limited to this list.

**GW-7** The summary MUST be imperative, lowercase after the type, at most 65 characters including the type and excluding any reference a forge appends on merge, and MUST NOT end with a period.

Anything that does not fit goes in the body. The limit governs what a person or an agent writes. A forge that appends its own reference on merge adds to that, and the sum still fits a line that reads without wrapping.

Correct: `docs: add consumer contract to meta layer`
Incorrect: `Added consumer contract.`, `updates`, `wip`

**GW-8** A commit message MUST describe what changed and, where not obvious, why.

**GW-25** A commit message MUST NOT describe the process of arriving at the change.

**GW-26** A commit body MUST be separated from the summary by a blank line and wrapped at 72 characters.

**GW-10** A commit MUST carry only work for the issue it is made for.

## Pull requests

WR-2 governs what the description of a pull request states for a reader who was not present when it was written.

**GW-14** A pull request MUST NOT be merged with failing checks.

**GW-15** A pull request SHOULD stay small enough to review in one sitting.

**GW-27** Large mechanical changes SHOULD be separated from behavioural ones.

**GW-30** A pull request that states that behaviour is unchanged MUST name the check that shows it.

A diff shows what changed in the code, not what stayed the same in its results, so the claim is the one part of such a pull request a reviewer cannot verify by reading it.

**GW-32** A pull request that removes, skips or weakens a test the default branch has MUST state, for the behaviour the test checked, what checks it after the change or why it is no longer required.

A test is weakened when a change makes it accept a result it rejected before, such as a wider tolerance, a looser assertion or a new expected value. Changing the source and changing the test both turn a failing test green, which is all GW-14 asks; the diff shows that the test changed, not whether the behaviour it guarded is still checked or still required. A test skipped or marked as expected to fail until a defect is fixed leaves a behaviour that is still required checked by nothing, so neither statement is true: the defect is fixed first, or the test stays as it is and GW-14 holds the merge.

Correct: `The nine tests of tests/run.sh moved to tests/import.sh unchanged`, `Import now stops at a corrupt file, so skipping one is no longer required`, `Skips the import test on the Linux runner; the macOS job runs it`
Incorrect: `Fixes the failing test`, `Skips the import test until the parser fix is merged`

**GW-24** A review MUST take place on a pull request, with its findings recorded as comments there and not in a committed file.

A file of review findings has to be pruned by hand once they are resolved. A pull request closes with the change it reviews.

## History

**GW-16** History on a shared branch MUST NOT be rewritten.

The default branch is a shared branch, so a force push to it rewrites shared history.

**GW-19** A committed secret MUST be treated as compromised and rotated.

Removing it from history does not undo the exposure.
