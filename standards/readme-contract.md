---
id: readme-contract
title: README contract
version: 4.0.0
status: active
applies_to: [all]
summary: What the README of any repository must answer, in which order the reader meets it, and when it is done.
---

# README contract

Prefix: `RM`

The README is written for the user of the repository, not for its author. Assume a reader who has never seen the repo, has about thirty seconds to decide whether it is relevant, and wants a working result before understanding the internals.

This standard fixes what a README answers and in which order the reader meets it. It does not fix headings or a list of sections: a README is as long as its repository gives the reader questions, and no longer.

## What a README answers

**RM-1** A README MUST answer every question the following table marks as required.

| Role | Required | Answers | For example headed |
|---|---|---|---|
| Summary | MUST | What is this, and who is it for? | The title and the first paragraph |
| What it is for | MAY | When do I use it, and when not? | What it is for, Scope |
| Getting started | MUST | How do I get a first result? | Getting started, Setup, Usage |
| Example | MAY | What does using it look like? | Example |
| Tasks | MAY | How do I do a particular thing with it? | Named for the task, such as After changing a file |
| Content and structure | MUST | What is in it, and where? | Files, Contents, Content and structure |
| How it works | MAY | How do the parts work together? | How it works, Design |
| Configuration | MAY | What can I change? | Configuration |
| Troubleshooting | MAY | What goes wrong, and what do I do? | Troubleshooting |
| Known limits | MAY | What does it not do, or not do well? | Known limits |
| Contributing and support | MAY | How do I report or change something? | Contributing |
| License | MUST (public) | What may I do with it? | License |

**RM-2** A section's heading MAY be chosen to fit the repository, and a role named in quotes in this standard refers to the section that answers its question, whatever its heading.

One section may answer several questions, and one question may take several sections where its answer is long.

## Order

**RM-27** The summary and, where present, "What it is for" MUST precede every other section.

**RM-28** "Getting started" SHOULD be the first section after them.

The reader came for a first result. The list of files is what they consult once they have one, so it rarely belongs first.

**RM-29** "How it works" SHOULD follow "Getting started", "Example" and every task section.

Beyond these, the order follows what the reader needs next and is not fixed.

## Optional sections

**RM-30** A section that answers a question marked MAY MUST carry content that no other section of the README states.

This is what keeps a small README small. A "What it is for" that repeats the summary, a "Configuration" that says there is nothing to configure, or a "How it works" that restates the file table fails it and is left out.

## Section rules

**RM-3** The summary MUST state in one or two sentences what the repository is and who it is for, in plain language, before any badge, logo or table of contents.

**RM-4** "What it is for" MUST name the concrete problem solved and MUST state the scope boundary: what the repository does not do.

**RM-5** "What it is for" MUST NOT consist of adjectives such as fast, flexible or modern.

**RM-6** Where a repository has something to install or run, "Getting started" MUST list prerequisites with versions, and MUST give install and run steps as copy-pasteable commands in fenced code blocks.

**RM-7** Where a repository has something to install or run, "Getting started" MUST end with a command that produces visible output, together with the expected output.

**RM-26** Where a repository has nothing to install or run, "Getting started" MUST name what the reader opens or reads first.

A repository that is read, such as a knowledge base, has no command to give. Its README keeps every other rule of this standard and is shorter for it.

**RM-8** "Getting started" MUST be usable without reading any other section.

**RM-25** At most 150 words MUST precede the "Getting started" heading in the README source.

A screen cannot be measured; a word count can. The count covers everything above the heading: the title, the summary and "What it is for".

**RM-9** Every command in a README MUST have been executed successfully against the current default branch before merge.

**RM-10** "Example" MUST show at least one real usage with concrete values and its actual output, not a bare signature or an all-placeholder command.

**RM-11** "Content and structure" MUST describe the top-level directories and MUST name the entry point files a reader opens first.

**RM-12** "Configuration" MUST list only options a normal user changes, each with its default and effect. Exhaustive references MUST be linked, not inlined.

**RM-13** "Troubleshooting" MUST list only failure modes actually observed, symptom first, fix second.

**RM-31** A task section MUST open with the command or the first step of the task.

**RM-32** "How it works" MUST describe how parts named in "Content and structure" depend on each other.

## Global rules

**RM-14** A README MUST describe the current state of the repository, not its history.

**RM-15** A README MUST NOT narrate work that was done, for example "we refactored" or "this was migrated from".

**RM-16** A README MUST NOT duplicate a changelog, roadmap or release notes.

**RM-17** A README MUST NOT contain TODOs, placeholders or empty sections.

**RM-18** A README MUST state known limitations honestly where they affect whether the reader should use it.

**RM-19** Content that drifts quickly, such as a full API surface or exhaustive flags, MUST be linked or generated, not hand copied into the README.

**RM-20** README length SHOULD be proportional: a small tool takes half a page, a framework takes structure plus links out.

**RM-21** A README MUST be scannable: headings, short paragraphs, fenced code blocks.

## Definition of done

**RM-22** A README MUST let a reader who has never seen the repository do all of the following:

- say what it is and who it is for, after the first paragraph;
- decide whether it fits their problem, before reaching "Getting started";
- get a working result by following "Getting started" alone;
- find the file to open next, from "Content and structure";
- know where to go for anything deeper.

**RM-23** Before merge, the following MUST hold: all commands verified against the default branch, all links resolve, no required section missing or empty, no MUST NOT rule violated.

## Maintenance trigger

**RM-24** The README MUST be re-checked against this standard whenever any of the following change: install or run commands, prerequisites or their versions, top-level layout, the primary use case, the license.

## Examples

A small tool. It answers the four required questions and nothing more, so a summary and three sections carry it; "Usage" and "Files" are its names for "Getting started" and "Content and structure", and its summary states the scope boundary, so it needs no "What it is for".

````markdown
# csv-tidy

A command-line tool for anyone who imports CSV exports into a spreadsheet. It trims whitespace, unifies dates and drops empty rows; it does not merge files.

## Usage

Requires Python 3.10 or later.

```bash
pip install csv-tidy==1.4.0
csv-tidy orders.csv
```

```
orders.csv: 1204 rows read, 17 empty rows dropped, written to orders.tidy.csv
```

## Files

| Path | Contains |
|---|---|
| `src/csv_tidy/` | The tool |
| `tests/` | Its tests, run with `pytest` |

## License

MIT. See [LICENSE](LICENSE).
````

A repository that is read. "Getting started" names the file to open, as RM-26 requires, and the list of contents follows it.

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
