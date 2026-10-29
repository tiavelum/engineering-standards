---
id: repo-layout
title: Repository layout
version: 8.0.0
status: active
applies_to: [all]
summary: Required top-level files, directory roles, where each file is placed, and what must not live in a repository.
---

# Repository layout

Prefix: `RL`

## Required at the root

**RL-1** The default branch of every repository MUST contain a `README.md` conforming to `standards/readme-contract.md`.

**RL-2** The default branch of every public repository MUST contain a `LICENSE` file.

**RL-3** The default branch of every repository MUST contain a `.gitignore` appropriate to its stack.

A repository without commits has no default branch yet, so its first commit brings these files.

## Directory roles

A repository creates the directories it needs, under names of its choosing. The rules below make the purpose of each directory explicit, so that every file has exactly one place.

**RL-9** Every directory below the root MUST have exactly one role.

**RL-18** The role of a directory that lies inside a top-level directory, and whose role no tool fixes, MUST be stated in the README at the root or in the README of the directory that contains it.

RM-11 requires the README at the root to describe each top-level directory. A tool fixes the role of a directory when it gives that directory, or every directory at that place, its meaning, as GitHub Actions does for `.github/workflows/` and Claude Code for each directory in `.claude/skills/`. A role stated in the README at the root keeps `.github/` free of a README, which GitHub would show in place of the repository's own.

**RL-19** The roles of directories that share a parent directory MUST NOT overlap.

Two roles overlap when one file can have both.

Correct: `scripts/` for scripts that build, test or run the repository, kept as source, next to `tools/` for prebuilt executables from outside the repository that those scripts run
Incorrect: `scripts/` for development scripts next to `tools/` for development utilities

## Placement

**RL-20** A file whose path no other rule of these standards fixes MUST live, of the directories in which the tool that reads it accepts it, in the deepest whose role the file has, or in the shallowest where none of them has a role that covers it.

A tool accepts a file in a directory where it finds the file on its own, by default or by searching. A file that a tool reads only from a path its author gives, such as an import, a script call or a path in a configuration file, is accepted in every directory, so it lives in the deepest directory whose role it has, or at the root.

PR-5, for example, fixes `deviations.md` at the root, and DOC-2 and DOC-10 set where documentation and decision records live.

Correct: `project-instructions.md` at the root, which `CLAUDE.md` imports and no directory's role covers; `CONTRIBUTING.md` in `docs/`, where GitHub also finds it, when `docs/` holds the repository's documentation
Incorrect: `CONTRIBUTING.md` at the root of the same repository

## What must not be committed

**RL-12** Secrets, credentials, tokens and private keys MUST NOT be committed, in any form, including in history, examples and test fixtures.

**RL-13** Build output, dependency directories and local environment files MUST NOT be committed.

They belong in `.gitignore`.

**RL-14** Large binaries MUST NOT be committed.

Reference them or use a purpose built store.

**RL-15** Personal notes, session logs and working files MUST NOT be committed unless the repository exists for them.
