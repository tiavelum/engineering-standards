---
id: repo-layout
title: Repository layout
version: 9.0.0
status: active
applies_to: [all]
summary: Required top-level files, directory roles, where each file is placed, and what must not live in a repository.
---

# Repository layout

This file governs the files every repository holds at its root, the roles of its directories, where each file lives and what is never committed.

Prefix: `RL`

## Required at the root

A repository without commits has no default branch yet, so its first commit brings these files.

### RL-1

The default branch of every repository MUST contain at its root a `README.md` that follows `standards/readme-contract.md`.

### RL-2

The default branch of every public repository MUST contain a `LICENSE` file at its root.

### RL-3

The default branch of every repository MUST contain at its root a `.gitignore` that lists each file or directory a tool used on the repository writes into it and that is not committed, such as build output, caches and local environment files.

## Directory roles

A repository creates the directories it needs, under names of its choosing; the rules below give each file one place.

### RL-9

Every directory below the root MUST have exactly one role.

A role is what the statement that RM-11 or RL-18 requires says the directory holds, and it may name several kinds of file, such as a module's code and its tests.

### RL-18

The role of a directory that lies inside a top-level directory and whose role no tool fixes MUST be stated in the README at the root or in the README of a directory that contains it.

A tool fixes a directory's role where it gives that directory its meaning, as GitHub Actions does for `.github/workflows/`.

### RL-19

The roles of directories that share a parent directory MUST NOT overlap.

Two roles overlap when one file can have both.

> Correct: `scripts/` for scripts that build, test or run the repository, next to `tools/` for prebuilt executables from outside the repository that those scripts run
>
> Incorrect: `scripts/` for development scripts next to `tools/` for development utilities

## Placement

### RL-20

A file whose path no other rule fixes MUST live in the deepest directory whose role covers it, among those where the tool that reads it finds it on its own, or else in the shallowest of those.

A file that only people read, or that a tool reads only from a path given to it, is found in every directory.

> Correct: `CONTRIBUTING.md` in `docs/`, where GitHub also finds it, when `docs/` holds the repository's documentation
>
> Incorrect: `CONTRIBUTING.md` at the root of the same repository

## What must not be committed

### RL-12

Secrets, credentials, tokens and private keys MUST NOT be committed, in any form, including in examples and test fixtures.

A secret that was committed is rotated under GW-19.

### RL-13

Build output, directories a package manager restores from the repository's manifest or lock file, and local environment files MUST NOT be committed.

They belong in the `.gitignore` of RL-3.

### RL-14

A file that Git treats as binary and that is larger than 1 MiB MUST NOT be committed.

Reference it or keep it in a store made for large files.

### RL-15

Personal notes, session logs and files made only to write or check a change, which nothing reads or runs once it is merged, MUST NOT be committed unless the repository exists for them.
