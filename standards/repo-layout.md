---
id: repo-layout
title: Repository layout
version: 1.0.0
status: active
applies_to: [all]
summary: Required top-level files, directory roles, and what must not live in a repository.
---

# Repository layout

Prefix: `RL`

## Required at the root

**RL-1** Every repository MUST contain a `README.md` conforming to `standards/readme.md`.

**RL-2** Every public repository MUST contain a `LICENSE` file.

**RL-3** Every repository MUST contain a `.gitignore` appropriate to its stack.

**RL-4** A repository with documentation beyond the README MUST place it in `docs/`, not at the root.

**RL-5** A repository MUST contain an `.editorconfig` when it holds files edited by more than one tool or person.

## Root discipline

**RL-6** The root MUST contain only: the required files above, configuration files that their tool requires to sit at the root, and the top-level directories.

**RL-7** Source files MUST NOT sit at the root when the repository has more than one of them.

**RL-8** The root MUST NOT contain scratch files, exports, notes, or anything named per the prohibitions in `NAM-4` and `NAM-8`.

## Directory roles

**RL-9** Each top-level directory MUST have exactly one role, stated in the README's structure section.

**RL-10** A repository SHOULD use these names where the role applies, rather than inventing synonyms:

| Directory | Role |
|-----------|------|
| `src/` | Source that is built or executed |
| `docs/` | Documentation for readers |
| `tests/` | Automated tests, when not colocated with source |
| `scripts/` | Operational and development scripts |
| `templates/` | Files intended to be copied and filled in |
| `examples/` | Runnable examples, not fragments |
| `.github/` | Repository automation and templates |

**RL-11** A directory MUST NOT be created for a single file unless more files of that kind are expected.

## What must not be committed

**RL-12** Secrets, credentials, tokens and private keys MUST NOT be committed, in any form, including in history, examples and test fixtures.

**RL-13** Build output, dependency directories and local environment files MUST NOT be committed. They belong in `.gitignore`.

**RL-14** Large binaries MUST NOT be committed. Reference them or use a purpose built store.

**RL-15** Personal notes, session logs and working files MUST NOT be committed unless the repository exists for them.

## Discoverability

**RL-16** A reader MUST be able to determine from the README's structure section which directory holds what, without opening files.

**RL-17** A directory whose purpose is not obvious from its name SHOULD carry a short `README.md` of its own.
