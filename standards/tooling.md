---
id: tooling
title: Tooling and enforcement
version: 11.0.2
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

**TL-31** A rule of a standard that states something other than a property TL-2 keeps out of a standard MUST NOT be removed, or reduced to a reference, on the ground that an automated check enforces it.

A check reports a violation once the file is written; the author needs the rule to write the file right in the first place. A repository setting is not an automated check under this rule; TL-30 governs a rule that a setting enforces.

> Correct: the rule TL-17 reduced to a reference to the `security_and_analysis` setting, which is a repository setting (TL-30)
>
> Incorrect: a rule that every pull request MUST name the issue it closes removed because a CI check fails a pull request without a closing keyword

**TL-22** Where a committed formatter governs a file, its configuration MUST be the authority for any formatting property another committed configuration also sets.

A second configuration may repeat the first for tools that do not read the formatter, but it never decides. Two configurations that have to be kept in step by hand will drift, and the one that drifts is not the one doing the formatting.

## Repository settings

**TL-29** Every repository that `repo-settings.sh` checks MUST be in a state for which `repo-settings.sh`, run without `--apply` from an unmodified checkout of the default branch of tiavelum/github-setup, prints `ok` for that repository.

A repository setting or ruleset enforces a requirement only on the repositories it is applied to. [tiavelum/github-setup](https://github.com/tiavelum/github-setup) holds the values and applies them. Run without `--apply`, `repo-settings.sh` [prints `diff` for a repository whose settings differ](https://github.com/tiavelum/github-setup#getting-started), so a repository that falls out of its management shows as differing.

**TL-30** Where a setting in `repo-settings.json` of tiavelum/github-setup enforces the whole requirement of a rule on every repository that `repo-settings.sh` checks and the rule applies to, the rule MUST state that requirement only as a reference to the setting.

A requirement written out next to the setting that enforces it drifts from the setting the day the setting changes; a reference cannot. The reference keeps the rule's identifier and keyword, so it can still be cited.

A rule whose requirement a setting enforces only in part, or only on some of the repositories `repo-settings.sh` checks and the rule applies to, stays written in full. Which repositories `repo-settings.sh` checks, and which settings reach which of them, is defined in tiavelum/github-setup and not restated here.

> Correct: `**TL-17** Secret scanning MUST be enabled where the security_and_analysis setting in repo-settings.json of tiavelum/github-setup enables it.`
>
> Incorrect: `**TL-17** Secret scanning MUST be enabled on every repository that can enable it.`, while that setting enforces it on every repository `repo-settings.sh` checks that can enable it

## Baseline configuration

**TL-5** The default branch of every repository MUST contain an `.editorconfig` covering at minimum: charset, indentation style and width, end of line, final newline, trailing whitespace.

**TL-6** Every repository containing code MUST commit, for the code in each of its languages, a formatter configuration for that language or, where no formatter exists that can run in CI and whose own documentation lists that language as supported, in part or in full, the `.editorconfig` that TL-5 requires.

The rule applies per language, since a formatter for one language leaves the code of another unformatted. A tool's own documentation decides whether it supports a language, because every reader can check it.

> Correct: a repository of Python and zsh code that commits a formatter configuration for its Python and, since [the documentation of shfmt lists zsh](https://github.com/mvdan/sh), formatting options for its zsh in the `.editorconfig` that shfmt reads
>
> Incorrect: a Python repository whose CI runs no formatter and that commits only the `.editorconfig`, a repository of Python and zsh code that commits a formatter configuration for its Python alone

**TL-23** A committed formatter MUST be applied to the whole repository, not selectively.

**TL-8** Every repository containing code MUST commit, for the code in each of its languages, a linter configuration for that language or, where no linter exists that can run in CI and whose own documentation lists that language as supported, in part or in full, a CI step that parses that code without running it.

The rule applies per language and a tool's own documentation decides, as under TL-6. A parse check finds code that does not parse.

> Correct: a repository of Python and zsh code that commits a linter configuration for its Python and, since [the documentation of zsh-lint lists zsh](https://github.com/z-shell/zsh-lint), one for its zsh
>
> Incorrect: a Python repository whose CI runs no linter and that commits only a CI step that parses its code, a repository of Python and zsh code that commits a linter configuration for its Python alone

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

**TL-32** Whether a change passes a check MUST be decided by the check's run in CI, whichever tool version a local run of the check uses.

A local run is advisory. It can use the version a platform's package manager installs, which can report a finding the version CI pins does not, or miss one that version reports; the pinned version gates the merge (TL-10, TL-15).

**TL-16** A repository MUST NOT declare a dependency it does not use.

## Secrets

**TL-17** Secret scanning MUST be enabled where the `security_and_analysis` setting in `repo-settings.json` of tiavelum/github-setup enables it.

**TL-18** A repository MUST read its secrets from the environment or a secret store.

**TL-19** A repository that reads configuration from the environment MUST commit an example environment file listing the required variable names with placeholder values.

A repository that reads nothing from the environment has no variable names to list. Requiring the file of it produces a placeholder that documents nothing, or a deviation under PR-5 explaining an absence, which PR-6 refuses as a reason.
