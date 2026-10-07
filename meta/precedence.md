---
id: precedence
title: Precedence and deviation
version: 1.1.0
status: active
applies_to: [all]
summary: How conflicts between these standards, a consuming repository and a task instruction are resolved, and how a deviation is recorded.
---

# Precedence and deviation

## Order of precedence

**PR-1** When sources conflict, the following order MUST apply, highest first:

1. An explicit instruction from the repository owner for the task at hand.
2. A constraint imposed by an external system that cannot be changed: a platform requirement, a package manager convention, a language's mandatory layout.
3. A documented deviation recorded in the consuming repository (see below).
4. These standards.
5. Community defaults for the language or framework in use.

**PR-2** A lower source MUST NOT be used to override a higher one silently. If a standard is set aside, it MUST be recorded per PR-5.

**PR-3** Where these standards are silent, the community default MUST be applied, and the silence MUST NOT be read as a prohibition.

## Conflicts between standards

**PR-4** If two standards in this repository conflict, the more specific one MUST be applied.

**PR-9** A conflict between two equally specific standards MUST be raised as an issue and MUST NOT be resolved case by case.

Such a conflict is a defect in the standards, not a choice left to the reader.

## Deviation

**PR-5** A repository that deviates from a MUST rule MUST record it in a file named `deviations.md` at its root, with one entry per deviation containing: the rule id, the reason, and the date.

**PR-6** A deviation entry MUST give a reason specific to that repository.

"Not applicable" without explanation is not a reason.

**PR-7** A deviation from a SHOULD rule does not need to be recorded.

**PR-8** A deviation that turns out to apply to several repositories SHOULD be raised as a change to the standard rather than repeated.

## Example

```markdown
# Deviations

## RL-3: no `.gitignore`

This repository holds two text files, and nothing that works on them writes
build output, caches or local settings into it.
Recorded 2026-09-01.
```
