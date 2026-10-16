---
id: module-layers
title: Module layers
version: 1.0.0
status: active
applies_to: [software]
summary: How the modules of a source directory are arranged in layers, which way they import, where files are read and written, and how the layers are described and checked.
---

# Module layers

Prefix: `ML`

A module is a source file that other source files import.

**ML-1** This standard MUST be applied to every directory of a repository that holds more than one module of its source.

Splitting code into files pays off only when the files do not all depend on each other. Layers make the direction of every dependency a rule that a reader can follow and a tool can check.

## Layers

**ML-2** Each module of a directory MUST belong to exactly one layer of that directory.

**ML-3** A module MUST import from the same directory only modules of the layers below its own.

A module that imports only downwards cannot be part of a cycle, and a layer can be changed without touching the layers below it.

**ML-4** A module that computes or renders MUST take its input as data and return its result as data, not as a file it reads or writes.

**ML-5** A module MAY read a file that ships with it, such as a template or a data set.

## Description

**ML-6** The README of the directory MUST name each layer, the modules it holds and what it does.

**ML-7** The README of the directory MUST name the modules that read or write files other than those of ML-5.

**ML-8** The README of the directory MUST show the imports between its modules as a diagram generated from the code.

A diagram written by hand goes stale with the first changed import; one generated from the code is the reference DOC-4 requires to be generated. DOC-45 makes the README the home of these rules.

## Checks

**ML-9** A test MUST fail when a module breaks ML-2 or ML-3.

**ML-10** A check in CI MUST fail when the diagram of ML-8 no longer matches the imports.

Both run where every merge is gated, as TL-10 requires.

## Example

A command-line tool with these layers in `src/`, as its README states them, lowest layer first:

| Layer | Modules | Does |
|---|---|---|
| Basics | `geo`, `tables` | Distances and bearings; reading and writing CSV tables |
| Domain | `route`, `report` | A route along days; the report as text |
| Steps | `compute` | Reads the input files, calls the layers above, writes the report |
| Command line | `cli` | Parses the arguments and runs a step |

Correct: `route` imports `geo`; `compute` imports `route`, `report` and `tables`; only `compute` reads and writes files, through `tables`.
Incorrect: `report` imports `compute` (ML-3); `route` opens the input file itself (ML-4).
