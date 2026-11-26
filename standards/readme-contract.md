---
id: readme-contract
title: README contract
version: 12.0.0
status: active
applies_to: [all]
summary: What every README of a repository must answer, under which headings and in which order the reader meets it, and what it leaves to other documents.
---

# README contract

This file governs every README of a repository: what it answers, in which order, and what it leaves to other documents, for a reader who has never seen the repository and wants a first result; it fixes the level-2 headings and leaves the others free.

Prefix: `RM`

The rules of `standards/documentation.md` apply to a README as to every other document.

## Scope

### RM-39

This standard MUST be applied to every README of a repository: the README at its root and the README of each directory below it.

### RM-50

In the README of a directory below the root, "the repository" in a rule of this standard MUST be read as that directory, unless the rule names the root README.

> Correct: `replay/README.md` lists the prerequisites of what `replay/` runs, as RM-6 asks
>
> Incorrect: `replay/README.md` lists every prerequisite of the whole repository

### RM-54

The README of a directory below the root that has something to install or run MUST have "Getting started".

> Correct: `replay/README.md`, whose directory holds `replay.py`, with `## Getting started` leading to a first replay
>
> Incorrect: the same README with the steps of a replay under `## Steps` and no `## Getting started`

## What a README answers

### RM-1

The root README MUST answer every question the following table marks as required.

| Role | Required at the root | Answers | Heading |
|---|---|---|---|
| Summary | MUST | What is this? | None: the title and the text before the first level-2 heading |
| What it is for | Optional | When do I use it, and when not? | `## What it is for` |
| Getting started | MUST | How do I get a first result? | `## Getting started` |
| Example | Optional | What does using it look like? | `## Example` |
| Files | Optional | What is in it, and how is it structured? | `## Files` |
| Known limits | Optional | What does it not do, or not do well? | `## Known limits` |
| Contributing | Optional | How do I check a change? | `## Contributing` |
| Documentation | Optional | Where do I read on? | `## Documentation` |
| License | MUST (public) | What may I do with it? | `## License` |

### RM-42

The level-2 headings of a README MUST be distinct headings of the last column of the table of RM-1.

What a reader needs after the first result stands in a document of `docs/` (DOC-2), which a README links (RM-43).

> Correct: `## Getting started`, `## Files` and `## License`, with `### Replaying a test repository` under the first
>
> Incorrect: `## Usage`, `## How it works`, `## Taking over the source's name`, or `## Getting started` twice

### RM-38

A role named in quotes in this standard MUST be read as the section under the heading that the table of RM-1 gives for that role, down to the next level-2 heading.

### RM-30

A section that answers a question the table of RM-1 marks as optional MUST carry content that no other section of the README states.

A "Files" that lists only the files "Getting started" already names, or a "Documentation" that repeats its links, is left out.

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

### RM-52

Where a repository has something to install or run, the first sentence of "Getting started" MUST name the first result it leads to.

> Correct: `These steps take a new Mac to a passing run of the tests.`; `These steps replay a test repository into a new one.`
>
> Incorrect: a "Getting started" that opens with `Install the prerequisites:`

### RM-6

Where a repository has something to install or run, "Getting started" MUST list prerequisites with versions.

### RM-44

Where a repository has something to install or run, the first step of "Getting started" MUST start on a machine that has only the prerequisites and get the repository's files where the reader needs a copy, or link the README whose "Getting started" does.

> Correct: `git clone https://github.com/octocat/photo-sync.git` and `cd photo-sync` as the first block; a first step in `sync/README.md` that links "Getting started" of the root README
>
> Incorrect: `./install.sh` as the first block, which assumes a clone and a shell inside it; `git clone git@github.com:octocat/photo-sync.git` where the prerequisites name no SSH key

### RM-34

Where a repository has something to install or run, "Getting started" MUST give each step as a command where one performs it, and otherwise as the exact manual action with its visible result.

> Correct: `brew install shellcheck` in a fenced block; `In photo-sync, open Settings > Account and sign in. The status bar then reads "Signed in".`
>
> Incorrect: `Install ShellCheck with Homebrew.`; `Sign in to photo-sync.`, which says neither where nor what shows that it worked

### RM-51

"Getting started" MUST NOT show what a command prints, in a block or in a sentence, other than a value the reader copies or compares with their own, such as a URL.

A statement of the result stays true when ordinary work changes the output, such as the number of tests.

> Correct: `All tests pass.`; `It prints ssh; if it prints https, run the next block.` after `gh config get git_protocol`
>
> Incorrect: `All 412 tests pass in 3.2 seconds.`; a block holding `412 passed in 3.21s`

### RM-7

Where a repository has something to install or run, "Getting started" MUST end with the step that shows the first result, with what the reader then sees (RM-34 gives the form).

### RM-26

Where a repository has nothing to install or run, "Getting started" MUST name what the reader opens or reads first.

### RM-10

"Example" MUST show at least one real usage with concrete values and what it produces, not a bare signature or an all-placeholder command.

### RM-35

"Files" MUST name the entry point files a reader opens first.

## Commands

### RM-46

A command block in a README MUST NOT set a variable, substitute a command's output or branch on a command's result; a sequence that needs one of these MUST be a script of the repository that the block runs.

Commands joined by `&&` only stop at the first failure and do not branch.

> Correct: `scripts/review-pr.sh 40` in a fenced block; `git switch main && git pull --ff-only && ./setup-mac.sh`
>
> Incorrect: `pr=40` followed by `scripts/review-pr.sh $pr`; `id=$(gh api repos/octocat/tool/issues/3 --jq .id)`; `test -d tool || mkdir tool`

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

> Correct: the root README names `replay/replay.py` and links `replay/README.md`
>
> Incorrect: the root README names `replay/replay.py` and links nothing, or links only `replay/replay.py`

### RM-49

A description of files that all lie in one directory below the root MUST stand in the README of the deepest directory holding them all that has a README, or in a non-README document it links, except what a rule requires of another document.

> Correct: `sync/README.md` describes how `sync/photo-sync.sh` matches photos, or links `docs/photo-matching.md`, which does; the root README says in one sentence what `sync/` does and links there
>
> Incorrect: the same description in the root README, or in `docs/photo-matching.md` with no link to it from `sync/README.md`

### RM-43

Each document in `docs/` MUST be linked from a README, in a sentence, list item or table row that names the task or question it serves.

> Correct: `To resume a stopped replay, follow [stopping and resuming](../docs/replay/stopping-and-resuming.md).` in `replay/README.md`
>
> Incorrect: `docs/replay/file-formats.md` linked from no README; `See also: [file-formats.md](../docs/replay/file-formats.md)`

## Examples

Both READMEs below are complete: each answers the required questions and has no section beyond what its reader needs for a first result.

A tool. Its summary already says what it does not do, so it needs no "What it is for".

````markdown
# csv-tidy

A command-line tool for anyone who imports CSV exports into a spreadsheet. It trims whitespace, unifies dates and drops empty rows; it does not merge files.

## Getting started

These steps tidy a first CSV export. They need Python 3.10 or later.

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

## Files

| File | For |
|---|---|
| `day-walk.md` | A single day, back by evening |
| `hut-tour.md` | Two to five nights in mountain huts |

## License

CC BY 4.0. See [LICENSE](LICENSE).
````
