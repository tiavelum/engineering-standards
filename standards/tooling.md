---
id: tooling
title: Tooling and enforcement
version: 14.0.0
status: active
applies_to: [all]
summary: The boundary between what a tool enforces and what a written standard covers, plus the required baseline configuration.
---

# Tooling and enforcement

This file governs what a tool enforces instead of a written standard, and the tool configuration, checks, dependencies and secrets every repository keeps.

Prefix: `TL`

## The boundary

### TL-2

A written standard MUST NOT prescribe a formatting property of a source file of a programming or scripting language, such as indentation, line length, quote style or import order.

Such a property belongs in the formatter or linter configuration that TL-6 and TL-8 require. A standard may require that the configuration covers it, as TL-5 does.

### TL-3

Tool configuration MUST be committed to the repository it governs.

The committed configuration is then the rule for what TL-2 keeps out of a standard.

### TL-31

A rule MUST NOT be removed from a standard because an automated check enforces it, unless TL-2 keeps what it states out of a standard.

A check reports a violation once the work is done; the rule tells the author how to do it right in the first place. A repository setting is not such a check.

### TL-22

Where a committed formatter governs a file, its configuration MUST be the authority for any formatting property another committed configuration also sets.

Another configuration may repeat it for tools that do not read the formatter's, but it never decides.

## Baseline configuration

A tool supports a language where it can run in CI and its own documentation lists that language as supported, in part or in full.

### TL-5

The default branch of every repository MUST contain at its root an `.editorconfig` covering at minimum: charset, indentation style and width, end of line, final newline, trailing whitespace.

### TL-6

A repository MUST commit a formatter configuration for each programming or scripting language of its source files that a formatter supports.

> Correct: Python and zsh code, with a configuration for ruff and, as [shfmt lists zsh](https://github.com/mvdan/sh), shfmt options in `.editorconfig`
>
> Incorrect: Python and zsh code, with a formatter configuration for the Python alone

### TL-8

A repository MUST commit, for each programming or scripting language of its source files, a linter configuration or, where no linter supports that language, a CI step that parses those files without running them.

### TL-23

A committed formatter MUST check, in CI, every file in a language it supports, other than a copy of another project's file and a file a tool generates.

A copy would differ from its source at its next update, and a generated file is overwritten by its generator.

### TL-33

A committed linter MUST check, in CI, every file in a language it supports, other than the files TL-23 leaves out.

### TL-24

A linter suppression, in a source file or in a configuration file, MUST carry its reason in a comment on the line that suppresses it.

## Automation

### TL-10

Checks that gate a merge MUST run in CI, not only locally.

### TL-11

A check that gates a merge MUST fail the build on a violation.

### TL-32

Whether a change passes a check MUST be decided by the check's run in CI, whichever tool version a local run of the check uses.

A local run may use another version than the one CI pins, and so find more or less.

### TL-21

Publication to a package or image registry MUST happen only from a build of a tag whose commit is reachable from the default branch or from a release branch.

## Dependencies

### TL-14

Dependency versions a build or CI run installs MUST be pinned or locked in a committed file.

### TL-15

Every tool and runtime CI installs MUST be named by an exact version, every action by a full commit SHA, and every runner by a label that names an operating system version.

A tag or a range can move under a workflow, so a build could not be repeated.

### TL-16

A repository MUST NOT declare a dependency it does not use.

## Secrets

### TL-18

A repository MUST read its secrets from the environment or a secret store.

### TL-19

A repository that reads configuration from the environment MUST commit an example environment file listing the required variable names with placeholder values.
