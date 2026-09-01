---
id: readme
title: README contract
version: 1.0.0
status: active
applies_to: [all]
summary: Required sections, ordering and acceptance criteria for the README of any repository.
---

# README contract

Prefix: `RM`

The README is written for the user of the repository, not for its author. Assume a reader who has never seen the repo, has about thirty seconds to decide whether it is relevant, and wants a working result before understanding the internals.

## Required sections

**RM-1** A README MUST contain the following sections, in this order. Sections marked SHOULD MAY be omitted when not applicable; sections marked MUST may not.

| # | Section | Required | Answers |
|---|---------|----------|---------|
| 1 | Title and one-line summary | MUST | What is this? |
| 2 | What it is for | MUST | Why would I use it, and when not? |
| 3 | Getting started | MUST | How do I run it in the next five minutes? |
| 4 | Example | MUST | What does using it look like? |
| 5 | Content and structure | MUST | How is this repo laid out? |
| 6 | Mental model | SHOULD | How should I think about it? |
| 7 | Configuration | SHOULD | What can I change? |
| 8 | Troubleshooting | SHOULD | What goes wrong, and what do I do? |
| 9 | Contributing and support | SHOULD | How do I report or change something? |
| 10 | License | MUST (public) | What may I do with it? |

**RM-2** Section order MUST NOT be changed. Sections MAY be renamed to fit the repository as long as the role is preserved.

## Section rules

**RM-3** The summary MUST state in one or two sentences what the repository is and who it is for, in plain language, before any badge, logo or table of contents.

**RM-4** "What it is for" MUST name the concrete problem solved and MUST state the scope boundary: what the repository does not do.

**RM-5** "What it is for" MUST NOT consist of adjectives such as fast, flexible or modern.

**RM-6** "Getting started" MUST list prerequisites with versions, and MUST give install and run steps as copy-pasteable commands in fenced code blocks.

**RM-7** "Getting started" MUST end with a command that produces visible output, together with the expected output.

**RM-8** "Getting started" MUST be usable without reading any other section.

**RM-9** Every command in a README MUST have been executed successfully against the current default branch before merge.

**RM-10** "Example" MUST show at least one real usage with concrete values and its actual output, not a bare signature or an all-placeholder command.

**RM-11** "Content and structure" MUST describe the top-level directories and MUST name the entry point files a reader opens first.

**RM-12** "Configuration" MUST list only options a normal user changes, each with its default and effect. Exhaustive references MUST be linked, not inlined.

**RM-13** "Troubleshooting" MUST list only failure modes actually observed, symptom first, fix second.

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

**RM-22** A README is done when a reader who has never seen the repository can do all of the following:

- say what it is and who it is for, after the first paragraph;
- decide whether it fits their problem, after section 2;
- get a working result by copy-pasting from section 3 alone;
- find the file to open next, from section 5;
- know where to go for anything deeper.

**RM-23** Before merge, the following MUST hold: all commands verified against the default branch, all links resolve, no required section missing or empty, no MUST NOT rule violated.

## Maintenance trigger

**RM-24** The README MUST be re-checked against this standard whenever any of the following change: install or run commands, prerequisites or their versions, top-level layout, the primary use case, the license.

## Skeleton

````markdown
# <Repo name>

<One or two sentences: what this is and who it is for.>

## What it is for

<The problem it solves. The case it fits. Where it does not apply.>

## Getting started

### Prerequisites

- <tool> >= <version>

### Install

```bash
<commands>
```

### First run

```bash
<command>
```

Expected output:

```
<output>
```

## Example

<One real use case, with command and output.>

## Content and structure

| Path | Contains |
|------|----------|
| `src/` | <what> |

Start here: `<entry point>`

## Mental model

<Core concepts and how they relate. Input, processing, output.>

## Configuration

| Option | Default | Effect |
|--------|---------|--------|
| `<name>` | `<value>` | <effect> |

## Troubleshooting

**<Symptom>** <Cause and fix.>

## Contributing

<How to raise an issue, how to propose a change.>

## License

<Name>. See [LICENSE](LICENSE).
````
