---
id: readme-contract
title: README contract
version: 10.0.1
status: active
applies_to: [all]
summary: What the README at the root of any repository must answer, in which order the reader meets it, and when it is done.
---

# README contract

This file governs what the README at the root of a repository answers and in which order, for a reader who has never seen the repository and wants a first result; it fixes no headings and no list of sections.

Prefix: `RM`

The rules of `standards/documentation.md` apply to a README as to every other document.

## Scope

### RM-39

This standard MUST be applied to the README at the root of a repository and MUST NOT be applied to the README of a directory below it.

## What a README answers

### RM-1

A README MUST answer every question the following table marks as required.

| Role | Required | Answers | For example headed |
|---|---|---|---|
| Summary | MUST | What is this? | The title and the first paragraph |
| What it is for | Optional | When do I use it, and when not? | What it is for, Scope |
| Getting started | MUST | How do I get a first result? | Getting started, Setup, Usage |
| Example | Optional | What does using it look like? | Example |
| Tasks | Optional | How do I do a particular thing with it? | Named for the task, such as After changing a file |
| Content and structure | MUST | What is in it, and where? | Files, Contents, Content and structure |
| How it works | Optional | How do the parts work together? | How it works, Design |
| Configuration | Optional | What can I change? | Configuration |
| Troubleshooting | Optional | What goes wrong, and what do I do? | Troubleshooting |
| Known limits | Optional | What does it not do, or not do well? | Known limits |
| Contributing and support | Optional | How do I report or change something? | Contributing |
| License | MUST (public) | What may I do with it? | License |

### RM-38

A role named in quotes in this standard MUST be read as the section that answers that role's question, whatever its heading.

One section may answer several questions, and one question may take several sections.

### RM-30

A section that answers a question the table of RM-1 marks as optional MUST carry content that no other section of the README states.

A "Configuration" that says there is nothing to configure, or a "How it works" that restates the file table, is left out.

## Order

### RM-27

The summary and, where present, "What it is for" MUST precede every other section.

### RM-28

"Getting started" SHOULD be the first section after them.

### RM-29

"How it works" SHOULD follow "Getting started", "Example" and every task section.

### RM-25

At most 200 words MUST precede the "Getting started" heading in the README source.

## Section rules

### RM-3

The summary MUST state in one or two sentences what the repository is, before any badge, logo or table of contents.

### RM-4

"What it is for" MUST name the concrete problem solved.

### RM-33

"What it is for" MUST state the scope boundary: what the repository does not do.

### RM-8

"Getting started" MUST be usable without reading any other section.

### RM-6

Where a repository has something to install or run, "Getting started" MUST list prerequisites with versions.

### RM-34

Where a repository has something to install or run, "Getting started" MUST give each step as a command where one performs it, and otherwise as the exact manual action with its visible result.

> Correct: `brew install shellcheck` in a fenced block; `In photo-sync, open Settings > Account and sign in. The status bar then reads "Signed in".`
>
> Incorrect: `Install ShellCheck with Homebrew.`; `Sign in to photo-sync.`, which says neither where nor what shows that it worked

### RM-7

Where a repository has something to install or run, "Getting started" MUST end with the step that shows the first result, with what the reader then sees (RM-34 gives the form).

### RM-26

Where a repository has nothing to install or run, "Getting started" MUST name what the reader opens or reads first.

### RM-10

"Example" MUST show at least one real usage with concrete values and its actual output, not a bare signature or an all-placeholder command.

### RM-31

A task section MUST open with the command or the first step of the task.

### RM-11

"Content and structure" MUST describe each top-level directory, so that a reader can tell which directory holds what without opening files.

### RM-35

"Content and structure" MUST name the entry point files a reader opens first.

### RM-32

"How it works" MUST describe how parts named in "Content and structure" depend on each other.

### RM-12

"Configuration" MUST list only options a normal user changes.

### RM-36

Each option in "Configuration" MUST carry its default and its effect.

### RM-13

"Troubleshooting" MUST list only failure modes actually observed, symptom first, fix second.

### RM-18

A README MUST state the known limitations that affect whether a reader should use the repository.

### RM-41

A section of the README that names a file or directory below the root MUST link to the README of the deepest directory below the root that is or holds it and has a README.

## Commands run before they reach the default branch

### RM-9

Every command in the README that a change adds or changes, or whose effect it changes, MUST have run successfully before the change reaches the default branch, with the change applied to the current default branch where one exists.

> Correct: `make install` run before merging a pull request that adds a package to `packages.txt`, which `make install` reads
>
> Incorrect: the same pull request merged without running `make install`, because its line in the README did not change

## Examples

Both READMEs below are complete: each answers the four required questions and has no other section, because its repository gives the reader no other question.

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

```
orders.csv: 1204 rows read, 17 empty rows dropped, written to orders.tidy.csv
```

## Files

| Path | Contains |
|---|---|
| `src/csv_tidy/` | The tool |
| `src/csv_tidy/cli.py` | The entry point of the `csv-tidy` command |
| `tests/` | Its tests |

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
