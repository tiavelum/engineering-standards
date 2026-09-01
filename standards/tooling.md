---
id: tooling
title: Tooling and enforcement
version: 1.0.0
status: active
applies_to: [all]
summary: The boundary between what a tool enforces and what a written standard covers, plus the required baseline configuration.
---

# Tooling and enforcement

Prefix: `TL`

## The boundary

**TL-1** Anything a tool can check automatically MUST be enforced by that tool and MUST NOT be written as prose in this repository.

**TL-2** Written standards cover only what tooling cannot check: structure, naming intent, scope boundaries, documentation content, decision hygiene.

**TL-3** Tool configuration MUST be committed to the repository it governs, so that the configuration is the rule.

**TL-4** When a tool and a written standard disagree, the tool wins and the standard is a defect to be fixed.

## Baseline configuration

**TL-5** Every repository MUST commit an `.editorconfig` covering at minimum: charset, indentation style and width, end of line, final newline, trailing whitespace.

**TL-6** Every repository containing code MUST commit a formatter configuration and MUST apply the formatter to the whole repository, not selectively.

**TL-7** Formatting MUST NOT be a matter of discussion in review. If it is being discussed, the formatter is missing or misconfigured.

**TL-8** Every repository containing code MUST commit a linter configuration.

**TL-9** Linter rules MUST be enabled deliberately. A suppression MUST carry a reason on the line that suppresses it.

## Automation

**TL-10** Checks that gate a merge MUST run in CI, not only locally.

**TL-11** CI MUST fail the build on a violation. A check that only warns does not gate and MUST NOT be described as enforced.

**TL-12** Local hooks MAY be provided for speed, but MUST NOT be the only place a check runs.

**TL-13** A check that is routinely bypassed MUST be either fixed or removed.

## Dependencies

**TL-14** Dependency versions MUST be pinned or locked, and the lock file MUST be committed.

**TL-15** Tool versions used in CI MUST be pinned, so that a build is reproducible.

**TL-16** A dependency MUST be added only when it is used. Unused dependencies MUST be removed.

## Secrets

**TL-17** Secret scanning MUST be enabled on every repository that can enable it.

**TL-18** Secrets MUST be supplied by the environment or a secret store, never by a committed file.

**TL-19** A repository MUST commit an example environment file listing required variable names with placeholder values, and MUST ignore the real one.
