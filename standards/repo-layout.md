---
id: repo-layout
title: Repository layout
version: 7.0.0
status: active
applies_to: [all]
summary: Required top-level files, directory roles, and what must not live in a repository.
---

# Repository layout

Prefix: `RL`

## Required at the root

**RL-1** The default branch of every repository MUST contain a `README.md` conforming to `standards/readme-contract.md`.

**RL-2** The default branch of every public repository MUST contain a `LICENSE` file.

**RL-3** The default branch of every repository MUST contain a `.gitignore` appropriate to its stack.

A repository without commits has no default branch yet, so its first commit brings these files.

## Root discipline

**RL-6** The root SHOULD contain only: the required files above, files whose location at the root is fixed by another rule in these standards or by the tool that reads them, and the top-level directories.

The clause is general on purpose. PR-5 fixes `deviations.md` at the root. Enumerating the files here would go stale each time a rule is added.

## Directory roles

**RL-9** Each top-level directory MUST have exactly one role.

RM-11 requires the README's structure section to say which directory holds what.

**RL-10** A repository SHOULD use these names where the role applies, rather than inventing synonyms:

| Directory | Role |
|-----------|------|
| `src/` | Source that is built or executed |
| `tests/` | Automated tests, when not colocated with source |
| `scripts/` | Operational and development scripts |
| `templates/` | Files intended to be copied and filled in |
| `examples/` | Runnable examples, not fragments |
| `.github/` | Repository automation and templates |

Documentation's directory is set by DOC-2.

## What must not be committed

**RL-12** Secrets, credentials, tokens and private keys MUST NOT be committed, in any form, including in history, examples and test fixtures.

**RL-13** Build output, dependency directories and local environment files MUST NOT be committed.

They belong in `.gitignore`.

**RL-14** Large binaries MUST NOT be committed.

Reference them or use a purpose built store.

**RL-15** Personal notes, session logs and working files MUST NOT be committed unless the repository exists for them.
