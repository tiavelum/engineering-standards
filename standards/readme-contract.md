---
id: readme-contract
title: README contract
version: 9.1.1
status: active
applies_to: [all]
summary: What the README at the root of any repository must answer, in which order the reader meets it, and when it is done.
---

# README contract

Prefix: `RM`

The README is written for the user of the repository, not for its author. Assume a reader who has never seen the repo, has about thirty seconds to decide whether it is relevant, and wants a working result before understanding the internals.

This standard fixes what a README answers and in which order the reader meets it. It does not fix headings or a list of sections: a README is as long as its repository gives the reader questions, and no longer.

**RM-39** This standard MUST be applied to the README at the root of a repository and MUST NOT be applied to the README of a directory below it.

A directory README is written for whoever uses or changes that directory's content, and `standards/documentation.md` governs it, DOC-45 and DOC-52 among its rules.

## What a README answers

**RM-1** A README MUST answer every question the following table marks as required.

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

**RM-38** A role named in quotes in this standard MUST be read as the section that answers that role's question, whatever its heading.

One section may answer several questions, and one question may take several sections where its answer is long.

## Order

**RM-27** The summary and, where present, "What it is for" MUST precede every other section.

**RM-28** "Getting started" SHOULD be the first section after them.

The reader came for a first result. The list of files is what they consult once they have one, so it rarely belongs first.

**RM-29** "How it works" SHOULD follow "Getting started", "Example" and every task section.

Beyond these, the order follows what the reader needs next and is not fixed.

## Optional sections

**RM-30** A section that answers a question the table of RM-1 marks as optional MUST carry content that no other section of the README states.

This is what keeps a small README small. A "What it is for" that repeats the summary, a "Configuration" that says there is nothing to configure, or a "How it works" that restates the file table fails it and is left out.

## Section rules

**RM-3** The summary MUST state in one or two sentences what the repository is, before any badge, logo or table of contents.

**RM-4** "What it is for" MUST name the concrete problem solved.

**RM-33** "What it is for" MUST state the scope boundary: what the repository does not do.

**RM-6** Where a repository has something to install or run, "Getting started" MUST list prerequisites with versions.

**RM-34** Where a repository has something to install or run, "Getting started" MUST give each step as a command where a command can perform it, and otherwise as the exact manual action with the visible result DOC-8 requires.

A step such as signing in to an account in an application's settings has no command; the exact action lets the reader take it, and what they see afterwards shows that it worked.

Correct: `brew install shellcheck` in a fenced block; `In photo-sync, open Settings > Account and sign in. The status bar then reads "Signed in".`
Incorrect: `Install ShellCheck with Homebrew.`, where `brew install shellcheck` performs the step; `Sign in to photo-sync.`, which says neither where nor what shows that it worked

**RM-7** Where a repository has something to install or run, "Getting started" MUST end with a command that produces visible output, together with the expected output.

**RM-26** Where a repository has nothing to install or run, "Getting started" MUST name what the reader opens or reads first.

A repository that is read, such as a knowledge base, has no command to give. Its README keeps every other rule of this standard and is shorter for it.

**RM-8** "Getting started" MUST be usable without reading any other section.

**RM-25** At most 200 words MUST precede the "Getting started" heading in the README source.

A screen cannot be measured; a word count can. The count covers everything above the heading: the title, the summary and "What it is for".

**RM-10** "Example" MUST show at least one real usage with concrete values and its actual output, not a bare signature or an all-placeholder command.

**RM-11** "Content and structure" MUST describe each top-level directory, so that a reader can tell which directory holds what without opening files.

**RM-35** "Content and structure" MUST name the entry point files a reader opens first.

**RM-12** "Configuration" MUST list only options a normal user changes.

**RM-37** An exhaustive reference of options MUST be linked from "Configuration", not inlined.

**RM-36** Each option in "Configuration" MUST carry its default and its effect.

**RM-13** "Troubleshooting" MUST list only failure modes actually observed, symptom first, fix second.

**RM-31** A task section MUST open with the command or the first step of the task.

**RM-32** "How it works" MUST describe how parts named in "Content and structure" depend on each other.

## Global rules

The rules of `standards/documentation.md` apply to a README as to every other document.

**RM-18** A README MUST state the known limitations that affect whether a reader should use the repository.

**RM-41** A section of the README MUST link to every README that, for a file or a directory below the root that the section names in its text, a table or a command, is the README of the deepest directory that lies below the root, has a README, and is or contains that file or directory.

The README at the root shows what works and is the entry point to everything the repository concerns. The details of a directory's content stand in that directory's README: the rules of how it is built (DOC-45) and what a program in it prints and does when it cannot complete its task (DOC-52). The link takes the reader there from the section where they meet that content.

Correct: a "Getting started" that runs `sync/photo-sync.sh` twice and links to `sync/README.md` once, and a "Content and structure" that describes `sync/` and links to the same file
Incorrect: the same "Getting started" without a link to `sync/README.md`, because "Content and structure" already links to it

## Before merge

**RM-9** Every command in the README that a pull request adds or changes, or whose effect it changes, MUST have been executed successfully before merge, with the pull request's changes applied to the current default branch.

A command's effect changes without its text when the pull request changes what the command reads or runs. A command the pull request adds exists only with its changes applied.

Correct: `make install` executed before the merge of a pull request that adds a package to `packages.txt`, which `make install` reads, though its line in the README stays the same
Incorrect: the same pull request merged without `make install` executed, because its line in the README did not change

**RM-40** The description of a pull request MUST name each command that RM-9 requires to have been executed for it, with where it was executed or, until it has been, that it has not been executed.

A command that needs a platform or an account the author does not work on stays marked as not executed while the pull request is under review, and the merge waits until whoever can run it has done so (RM-9). The description then shows, after the merge too, which commands were run and where.

Correct: `make install-agent: executed on macOS 15.1`, and before that `make install-agent: not executed, needs macOS`
Incorrect: `All commands tested.`, or a description that does not mention a command the pull request added

DOC-51 covers the links of the README.

## Examples

Both READMEs below are complete. Each answers the four required questions under headings of its own, puts the first result before the list of files, and has no other section, because its repository gives the reader no other question.

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
| `tests/` | Its tests, run with `pytest` |

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
