---
id: readme-contract
title: README contract
version: 11.0.0
status: active
applies_to: [all]
summary: What every README of a repository must answer, in which order the reader meets it, and what it leaves to other documents.
---

# README contract

This file governs every README of a repository: what it answers, in which order, and what it leaves to other documents, for a reader who has never seen the repository and wants a first result; it fixes no headings.

Prefix: `RM`

The rules of `standards/documentation.md` apply to a README as to every other document.

## Scope

### RM-39

This standard MUST be applied to every README of a repository: the README at its root and the README of each directory below it.

A rule that names the root README applies to that README alone.

## What a README answers

### RM-1

The root README MUST answer every question the following table marks as required.

| Role | Required at the root | Answers | For example headed |
|---|---|---|---|
| Summary | MUST | What is this? | The title and the first paragraph |
| What it is for | Optional | When do I use it, and when not? | What it is for, Scope |
| Getting started | MUST | How do I get a first result? | Getting started, Setup, Usage |
| Example | Optional | What does using it look like? | Example |
| Content and structure | Optional | What is in it, and where? | Files, Contents, Content and structure |
| Documentation | Optional | Where do I read on? | Documentation |
| License | MUST (public) | What may I do with it? | License |

### RM-42

A README MUST NOT hold a section that answers a question the table of RM-1 does not name.

What a reader needs beyond a first result stands in a document of `docs/` (DOC-2), one topic per file (DOC-37), which a README links (RM-43).

> Correct: `replay/README.md` ends "Getting started" with the first replay, and `docs/replay/stopping-and-resuming.md` explains how a stopped replay resumes
>
> Incorrect: a section "Stopping and resuming", "Troubleshooting" or "How it works" in `replay/README.md`

### RM-38

A role named in quotes in this standard MUST be read as the section that answers that role's question, whatever its heading.

One section may answer several questions, and one question may take several sections.

### RM-30

A section that answers a question the table of RM-1 marks as optional MUST carry content that no other section of the README states.

A "Content and structure" that lists only the files "Getting started" already names, or a "Documentation" that repeats its links, is left out.

## Order

### RM-27

The summary and, where present, "What it is for" MUST precede every other section.

### RM-28

"Getting started" SHOULD be the first section after them.

### RM-25

In a README that has "Getting started", at most 200 words MUST precede its heading in the README source.

## Section rules

### RM-3

The summary MUST state in one or two sentences what the repository or directory is, before any badge, logo or table of contents.

### RM-4

"What it is for" MUST name the concrete problem solved.

### RM-33

"What it is for" MUST state the scope boundary: what the repository does not do.

### RM-18

The root README MUST state the known limitations that affect whether a reader should use the repository.

### RM-8

"Getting started" MUST be usable without reading any other section.

### RM-6

Where a repository has something to install or run, "Getting started" MUST list prerequisites with versions.

### RM-44

Where a repository has something to install or run, the first step of "Getting started" MUST start on a machine that has only the prerequisites and get the repository's files where the reader needs a copy, or link the README whose "Getting started" does.

> Correct: `git clone https://github.com/octocat/photo-sync.git` and `cd photo-sync` as the first block; a first step in `sync/README.md` that links "Getting started" of the root README
>
> Incorrect: `./install.sh` as the first block, which assumes a clone and a shell inside it

### RM-34

Where a repository has something to install or run, "Getting started" MUST give each step as a command where one performs it, and otherwise as the exact manual action with its visible result.

> Correct: `brew install shellcheck` in a fenced block; `In photo-sync, open Settings > Account and sign in. The status bar then reads "Signed in".`
>
> Incorrect: `Install ShellCheck with Homebrew.`; `Sign in to photo-sync.`, which says neither where nor what shows that it worked

### RM-45

A step of "Getting started" MUST state its result in a sentence and MUST NOT show what a command prints, other than text the reader uses in a later step, such as a URL.

The sentence stays true when ordinary work changes the output, such as the number of tests.

> Correct: `pytest` in a fenced block, followed by `All tests pass.`
>
> Incorrect: the same block followed by a block holding `412 passed in 3.21s`

### RM-7

Where a repository has something to install or run, "Getting started" MUST end with the step that shows the first result.

### RM-26

Where a repository has nothing to install or run, "Getting started" MUST name what the reader opens or reads first.

### RM-10

"Example" MUST show at least one real usage with concrete values and its actual output, not a bare signature or an all-placeholder command.

### RM-35

"Content and structure" MUST name the entry point files a reader opens first.

## Commands

### RM-46

A command block in a README MUST run at most one script or tool of the repository, beside the commands that prepare it; a sequence with its own logic, such as variables, conditions or loops, MUST be a script of the repository that the block runs.

> Correct: `scripts/review-pr.sh 40` in a fenced block; `git switch main && git pull --ff-only` followed by `./setup-mac.sh`
>
> Incorrect: a block that sets `pr=40`, looks up a run with `gh run list` and downloads it inside an `if`

### RM-47

A README MUST NOT explain how a tool from outside the repository works.

That explanation has its home in the tool's own documentation, which a step links where the reader needs more than the command.

> Correct: `gh auth login` in a fenced block, with a link to the GitHub CLI manual for its options
>
> Incorrect: a paragraph on how forks, branches and pull requests work on GitHub

### RM-9

Every command in the README that a change adds or changes, or whose effect it changes, MUST have run successfully before the change reaches the default branch, with the change applied to the current default branch where one exists.

> Correct: `make install` run before merging a pull request that adds a package to `packages.txt`, which `make install` reads
>
> Incorrect: the same pull request merged without running `make install`, because its line in the README did not change

## From the root to directories and documents

### RM-48

The role of each directory whose role no tool fixes MUST be stated in its own README or in the README of a directory that contains it.

A tool fixes a directory's role where it gives that directory its meaning, such as `.github/workflows/`.

> Correct: `replay/README.md` opens with what `replay/` holds, and the root README says in one sentence that `tests/` holds the tests
>
> Incorrect: a `scripts/` directory with no README of its own and named in no README

### RM-41

A README that names a file or directory below its own directory MUST link the README of the deepest directory below its own that is or holds it and has a README.

### RM-49

A description of files that all lie in one directory below the root MUST stand in the README of the deepest directory that holds them all, or in a document that this README links and that is not a README, except what a rule requires of another document.

> Correct: `sync/README.md` describes how `sync/photo-sync.sh` matches photos, or links `docs/photo-matching.md`, which does; the root README says in one sentence what `sync/` does and links there
>
> Incorrect: the same description in the root README, or in `docs/photo-matching.md` with no link to it from `sync/README.md`

### RM-43

Each document in `docs/` MUST be linked from a README, in a sentence, list item or table row that says when a reader needs it.

> Correct: `To resume a stopped replay, follow [stopping and resuming](../docs/replay/stopping-and-resuming.md).` in `replay/README.md`
>
> Incorrect: a file in `docs/` that no README links, or a list of the files in `docs/` that says nothing of when to read them

## Examples

Both READMEs below are complete: each answers the required questions and has no section beyond what its reader needs for a first result.

A tool. Its summary already says what it does not do, so it needs no "What it is for".

````markdown
# csv-tidy

A command-line tool for anyone who imports CSV exports into a spreadsheet. It trims whitespace, unifies dates and drops empty rows; it does not merge files.

## Usage

Requires Python 3.10 or later.

```bash
pip install csv-tidy
csv-tidy orders.csv
```

The tidied rows are now in `orders.tidy.csv`, beside `orders.csv`.

## Files

`src/csv_tidy/` holds the tool, with the `csv-tidy` command in `cli.py`, and `tests/` its tests.

## License

MIT. See [LICENSE](LICENSE).
````

A repository that is read. It has no command to give, so "Getting started" names the file to open (RM-26).

````markdown
# hiking-checklists

Printable checklists for hikers preparing a day walk or a hut tour in the Alps.

## Getting started

Open `day-walk.md` and print it.

## Contents

| File | For |
|---|---|
| `day-walk.md` | A single day, back by evening |
| `hut-tour.md` | Two to five nights in mountain huts |

## License

CC BY 4.0. See [LICENSE](LICENSE).
````
