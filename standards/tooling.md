---
id: tooling
title: Tooling and enforcement
version: 5.1.1
status: active
applies_to: [all]
summary: The boundary between what a tool enforces and what a written standard covers, plus the required baseline configuration.
---

# Tooling and enforcement

Prefix: `TL`

## The boundary

**TL-1** A property that a committed tool configuration governs MUST NOT be restated in prose in the same repository.

The configuration is the rule (TL-3), and a second statement of it drifts. A rule that a tool implements but that a person or an agent has to read to follow, such as a naming rule or the form of a file, is not such a property and is written down.

**TL-2** A written standard MUST NOT prescribe a formatting property of files, such as indentation, line length, quote style or import order.

Such a property belongs in the formatter or linter configuration of the repository it governs (TL-6, TL-8). A standard may require that the configuration exists and what it covers, as TL-5 does.

**TL-3** Tool configuration MUST be committed to the repository it governs.

The committed configuration is then the rule.

**TL-4** When a tool and a written standard disagree, the standard MUST be treated as the defect and corrected.

**TL-22** Where a committed formatter governs a file, its configuration MUST be the authority for any formatting property another committed configuration also sets.

A second configuration may repeat the first for tools that do not read the formatter, but it never decides. Two configurations that have to be kept in step by hand will drift, and the one that drifts is not the one doing the formatting.

## Baseline configuration

**TL-5** Every repository MUST commit an `.editorconfig` covering at minimum: charset, indentation style and width, end of line, final newline, trailing whitespace.

**TL-6** Every repository containing code MUST commit a formatter configuration.

**TL-23** A committed formatter MUST be applied to the whole repository, not selectively.

**TL-7** Formatting MUST NOT be a matter of discussion in review.

If it is being discussed, the formatter is missing or misconfigured.

**TL-8** Every repository containing code MUST commit a linter configuration.

**TL-9** Linter rules MUST be enabled deliberately.

**TL-24** A linter suppression MUST carry a reason on the line that suppresses it.

## Automation

**TL-10** Checks that gate a merge MUST run in CI, not only locally.

**TL-11** CI MUST fail the build on a violation.

**TL-25** A check that only warns MUST NOT be described as enforced.

A check that only warns does not gate.

**TL-12** Local hooks MAY be provided for speed, but MUST NOT be the only place a check runs.

**TL-13** A check that is routinely bypassed MUST be either fixed or removed.

**TL-21** Publication to a registry MUST happen only from a build of a tag on a protected branch.

## Dependencies

**TL-14** Dependency versions MUST be pinned or locked.

**TL-26** A lock file MUST be committed.

**TL-15** Tool versions used in CI MUST be pinned.

A build is reproducible only with pinned tools.

**TL-16** A dependency MUST be added only when it is used.

**TL-27** An unused dependency MUST be removed.

## Secrets

**TL-17** Secret scanning MUST be enabled on every repository that can enable it.

**TL-18** Secrets MUST be supplied by the environment or a secret store, never by a committed file.

**TL-19** A repository that reads configuration from the environment MUST commit an example environment file listing the required variable names with placeholder values.

**TL-28** A repository that reads configuration from the environment MUST ignore its real environment file.

A repository that reads nothing from the environment has no variable names to list. Requiring the file of it produces a placeholder that documents nothing, or a deviation under PR-5 explaining an absence, which PR-6 refuses as a reason.
