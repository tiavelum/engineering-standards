---
id: git-workflow
title: Git workflow
version: 8.0.0
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

WR-1 governs the language of a commit message, and WR-5 the length of its first line.

**GW-5** A commit MUST leave the repository in a working state.

The tip of the default branch is a commit, so the default branch always works.

**GW-33** A commit that reaches the default branch without a pull request MUST carry as its message a title and a description that GW-6, GW-7, GW-25 and WR-2 allow for a pull request, the title as the message's first line and the description as its body.

Under GW-2 such a commit is the first commit of a repository, which creates the default branch; every later commit there comes from merging a pull request.

**GW-10** A commit MUST carry only work for the issue it is made for.

## Pull requests

WR-1 governs the language of a pull request's title and description, WR-2 what the description states for a reader who was not present when it was written, and WR-5 the length of the title.

A repository that merges by squash turns the title of a pull request into the first line of the commit its merge makes on the default branch, and the description into that commit's body. The rules on what that commit message says are therefore rules on these two texts.

**GW-6** A pull request's title MUST take the form `<type>: <summary>`, where `<type>` is one of `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`, `revert`.

The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope and with the types limited to this list.

**GW-7** The `<summary>` of a pull request's title MUST begin with a lowercase verb in the imperative and MUST NOT end with a period.

What does not fit in the title goes in the description.

Correct: `docs: add consumer contract to meta layer`, `fix: correct the README links`
Incorrect: `docs: Added consumer contract.`, `docs: consumer contract`, `updates`, `wip`

**GW-25** A pull request's description MUST NOT describe the process of arriving at the change.

Correct: `Read the port from PORT, which the container sets.`
Incorrect: `Tried a config file first; CI could not find it, so switched to PORT.`

**GW-14** A pull request MUST NOT be merged with failing checks.

**GW-15** A pull request SHOULD stay small enough to review in one sitting.

**GW-27** A large mechanical change SHOULD be made in a pull request of its own.

A change is mechanical when it changes no behaviour and applies one transformation throughout, such as formatting, a rename or moving files. Commits within one pull request do not keep it apart once the pull request is squashed into one commit; a pull request of its own keeps it apart in the history and lets it be checked on its own.

**GW-30** A pull request that states that behaviour is unchanged MUST name the check that shows it.

A diff shows what changed in the code, not what stayed the same in its results, so the claim is the one part of such a pull request a reviewer cannot verify by reading it.

**GW-32** A pull request that removes, skips or weakens a test the default branch has MUST state, for the behaviour the test checked, what checks it after the change or why it is no longer required.

A test is weakened when a change makes it accept a result it rejected before, such as a wider tolerance, a looser assertion or a new expected value. Changing the source and changing the test both turn a failing test green, which is all GW-14 asks; the diff shows that the test changed, not whether the behaviour it guarded is still checked or still required. A test skipped or marked as expected to fail until a defect is fixed leaves a behaviour that is still required checked by nothing, so neither statement is true: the defect is fixed first, or the test stays as it is and GW-14 holds the merge.

Correct: `The nine tests of tests/run.sh moved to tests/import.sh unchanged`, `Import now stops at a corrupt file, so skipping one is no longer required`, `Skips the import test on the Linux runner; the macOS job runs it`
Incorrect: `Fixes the failing test`, `Skips the import test until the parser fix is merged`

**GW-24** A review MUST take place on a pull request, with its findings recorded as comments there and not in a committed file.

A file of review findings has to be pruned by hand once they are resolved. A pull request closes with the change it reviews.

**GW-34** A pull request MUST NOT be merged unless, after its last commit, the repository's owner has submitted a review of it, or a party that neither wrote nor directed its changes has submitted a review of it that lists its findings or states that it found none.

The owner's review counts whoever wrote the changes. A party is a person or an agent session; a person and the agent sessions that act under that person's account are separate parties, so a review submitted by a session under the owner's account is not the owner's review. A review submitted as a review of the pull request, rather than as a comment in its conversation, shows there whichever account submits it. A commit made after a review leaves that commit unreviewed, so the review is made again.

Correct: a review submitted on the pull request with its three findings as its comments, a review submitted on the pull request that states it found nothing
Incorrect: findings summarised in the pull request's description, findings posted as a comment in the pull request's conversation, a review by the session that wrote the changes or by the session that directed their writing

## History

**GW-16** History on a shared branch MUST NOT be rewritten.

The default branch is a shared branch, so a force push to it rewrites shared history.

**GW-19** A committed secret MUST be treated as compromised and rotated.

Removing it from history does not undo the exposure.
