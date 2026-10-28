---
id: tooling
title: Tooling and enforcement
version: 7.1.0
status: active
applies_to: [all]
summary: The boundary between what a tool or a repository setting enforces and what a written standard covers, plus the required baseline configuration.
---

# Tooling and enforcement

Prefix: `TL`

## The boundary

**TL-2** A written standard MUST NOT prescribe a formatting property of files, such as indentation, line length, quote style or import order.

Such a property belongs in the formatter or linter configuration of the repository it governs (TL-6, TL-8). A standard may require that the configuration exists and what it covers, as TL-5 does.

**TL-3** Tool configuration MUST be committed to the repository it governs.

The committed configuration is then the rule.

**TL-4** When a tool and a written standard disagree, the standard MUST be treated as the defect and corrected.

**TL-22** Where a committed formatter governs a file, its configuration MUST be the authority for any formatting property another committed configuration also sets.

A second configuration may repeat the first for tools that do not read the formatter, but it never decides. Two configurations that have to be kept in step by hand will drift, and the one that drifts is not the one doing the formatting.

## Repository settings

**TL-29** A repository on GitHub whose `archived` and `fork` properties, as the GitHub API returns them, are both `false` MUST be in a state for which `repo-settings.sh`, run from an unmodified checkout of the default branch of tiavelum/github-setup, prints `ok` for that repository.

A repository setting or ruleset enforces a requirement only on the repositories it is applied to. tiavelum/github-setup holds the values and applies them. Run without `--apply`, `repo-settings.sh` prints `diff` for a repository whose settings differ, so a repository that falls out of its management shows as differing. It prints `skipped` for a repository whose `archived` or `fork` property is `true`, the repositories TL-29 leaves out.

## Baseline configuration

**TL-5** The default branch of every repository MUST contain an `.editorconfig` covering at minimum: charset, indentation style and width, end of line, final newline, trailing whitespace.

**TL-6** Every repository containing code MUST commit a formatter configuration.

**TL-23** A committed formatter MUST be applied to the whole repository, not selectively.

**TL-8** Every repository containing code MUST commit a linter configuration.

**TL-24** A linter suppression MUST carry a reason on the line that suppresses it.

## Automation

**TL-10** Checks that gate a merge MUST run in CI, not only locally.

**TL-11** CI MUST fail the build on a violation.

**TL-25** A check that only warns MUST NOT be described as enforced.

A check that only warns does not gate.

**TL-21** Publication to a registry MUST happen only from a build of a tag on a protected branch.

## Dependencies

**TL-14** Dependency versions MUST be pinned or locked in a committed file.

**TL-15** Tool versions used in CI MUST be pinned.

A build is reproducible only with pinned tools.

**TL-16** A repository MUST NOT declare a dependency it does not use.

## Secrets

**TL-17** Secret scanning MUST be enabled on every repository that can enable it.

**TL-18** A repository MUST read its secrets from the environment or a secret store.

**TL-19** A repository that reads configuration from the environment MUST commit an example environment file listing the required variable names with placeholder values.

A repository that reads nothing from the environment has no variable names to list. Requiring the file of it produces a placeholder that documents nothing, or a deviation under PR-5 explaining an absence, which PR-6 refuses as a reason.
