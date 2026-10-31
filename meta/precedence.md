---
id: precedence
title: Precedence and deviation
version: 3.0.0
status: active
applies_to: [all]
summary: How conflicts between these standards, a consuming repository and a task instruction are resolved, and how a deviation is recorded.
---

# Precedence and deviation

This file governs which source wins when these standards, a consuming repository and a task instruction conflict, and how a repository records a deviation.

## Order of precedence

### PR-1

When sources conflict, the following order MUST apply, highest first:

1. An explicit instruction for the task at hand that the repository owner gave, directly or passed on unchanged and marked as the owner's.
2. A constraint imposed by an external system that cannot be changed: a platform requirement, a package manager convention, a language's mandatory layout.
3. A deviation recorded in the consuming repository under PR-5.
4. These standards.
5. Community defaults for the language or framework in use.

### PR-3

Where these standards are silent, the community default MUST be applied, and the silence MUST NOT be read as a prohibition.

## Conflicts between standards

### PR-9

Work that two conflicting rules of these standards govern MUST NOT proceed until the repository owner has given an instruction for the task that decides between them.

Such a conflict is a defect of the standards, raised as an issue on this repository under ISS-1; PR-1 makes the owner's instruction for the task the source that decides it.

## Deviation

### PR-5

A repository MUST record each deviation from a MUST or MUST NOT rule in `deviations.md` at its root, as one entry giving the rule id, the reason and the date recorded as YYYY-MM-DD.

```markdown
# Deviations

This file lists the rules of tiavelum/engineering-standards that this
repository deviates from, with the reason for each, for its maintainers and
for anyone who applies the standards to it.

## RL-3: no `.gitignore`

This repository holds two text files, and nothing that works on them writes
build output, caches or local settings into it.
Recorded 2026-09-01.
```

### PR-6

A deviation entry MUST give a reason specific to that repository.

> Correct: `This repository holds two text files, and nothing that works on them writes build output, caches or local settings into it.` as the reason for a deviation from RL-3
>
> Incorrect: `Not applicable.`, `The rule does not fit this repository.` as the reason for the same deviation

### PR-11

A rule that a repository setting enforces MUST NOT be deviated from.

### PR-8

A deviation that turns out to apply to several repositories SHOULD be raised as a change to the standard rather than repeated.
