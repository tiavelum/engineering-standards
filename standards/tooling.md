---
id: tooling
title: Tooling and enforcement
version: 14.4.0
status: active
applies_to: [all]
summary: The boundary between what a tool enforces and what a written standard covers, plus the required baseline configuration.
---

# Tooling and enforcement

This file governs what a tool enforces instead of a written standard, and the tool configuration, checks, tests, dependencies and secrets every repository keeps.

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

A committed formatter MUST gate merges, in CI, on every file in a language it supports, other than a copy of another project's file and a file a tool generates.

A copy would differ from its source at its next update, and a generated file is overwritten by its generator.

### TL-33

A committed linter MUST gate merges, in CI, on every file in a language it supports, other than the files TL-23 leaves out.

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

### TL-34

A workflow that runs on pull requests MUST cancel its run for a pull request's commit once a newer commit of the same pull request starts a run of it.

Only the checks of a pull request's last commit decide its merge, so a superseded run only holds a runner the newest commit waits for.

> Correct: `concurrency: { group: "${{ github.workflow }}-${{ github.head_ref || github.run_id }}", cancel-in-progress: true }`
>
> Incorrect: no `concurrency` key, so a fix pushed to a pull request waits for the macOS runner its superseded run still holds.

### TL-35

A job of a workflow that runs on pull requests MUST run at least one check of the change, such as a formatter, a linter or a test.

A job that checks nothing still concludes `success`, which reads as a pass to whoever merges and to auto-merge; a repository without a check has no such workflow yet.

> Correct: the pull request that adds a repository's first Python file adds its workflow, with a job that runs `ruff check .`.
>
> Incorrect: a placeholder job that only runs `actions/checkout`, so every pull request shows a green check that checked nothing.

### TL-36

CI MUST run every check that the README asks a contributor to run before opening a pull request.

> Correct: the README lists `python3 scripts/validate-standards.py` for contributors, and the workflow runs it.
>
> Incorrect: the README lists `pytest` for contributors, and the workflow runs only `ruff check .`.

### TL-37

Every script of the repository that a command block of its README runs MUST be run in CI by a check that fails when the script exits with a failure status.

A script the README runs is what the repository offers its users; a linter shows that it parses, not that it works.

> Correct: the README runs `./repo-settings/repo-settings.sh`, and a test in CI runs it against a stub `gh` and fails on a non-zero exit status.
>
> Incorrect: the README runs `./setup-local.sh`, and CI only lints it with `shellcheck`.

### TL-21

Publication to a package or image registry MUST happen only from a build of a tag whose commit is reachable from the default branch or from a release branch.

## Tests

A runner can run a single test where one command selects exactly that test, by its name or its place in the suite, as pytest does by node id.

### TL-38

A test SHOULD be written in the programming or scripting language of the code it tests.

A test in another language becomes the template of the next one, and its runner often cannot run a single test, so every change runs the whole suite.

> Correct: Python scripts tested by a pytest suite that runs them as processes against a fake `gh`.
>
> Incorrect: Python scripts tested by a shell script that holds Python in heredocs and runs each check as a quoted condition through `eval`.

### TL-39

A test of a suite whose runner can run a single test MUST give the same result run on its own as run within the whole suite.

A test that relies on what an earlier test left passes in the suite and fails alone, or the reverse; fixtures, not the order of the tests, set up what a test needs.

> Correct: each test asks for a fixture of session scope that builds the source repository once.
>
> Incorrect: a test reads a file that only the test before it in the same file writes.

### TL-40

A README that gives the command running a suite whose runner can run a single test MUST give, beside it in the same code block or sentence, a command that runs a single test of that suite.

Whoever changes one test, or code that only some tests cover, can then run those tests alone, while CI runs the whole suite as TL-36 requires.

> Correct: "Getting started" runs `pytest tests` and, beside it, `pytest tests/test_plan.py::test_leave_behind` for one test.
>
> Incorrect: "Getting started" runs only `pytest tests`.

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
