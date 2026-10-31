---
id: module-layers
title: Module layers
version: 4.0.0
status: active
applies_to: [software]
summary: How the modules of a source directory are arranged in layers, which way they import, where files are read and written, and how the layers are described and checked.
---

# Module layers

This file governs how the modules of a repository's source are arranged in layers, which way they import, which of them read and write files, and how the layers are described and checked.

Prefix: `ML`

A module is a source file that other source files import.

### ML-1

This standard MUST be applied to every directory of a repository that holds more than one module of its source.

Layers make the direction of every import a rule that a reader can follow and a tool can check.

## Layers

### ML-2

Each module of a directory MUST belong to exactly one layer of that directory.

### ML-3

A module MUST import from the same directory only modules of the layers below its own.

### ML-11

The imports between the modules of a repository MUST NOT form a cycle, across directories as within one, whether or not ML-1 applies to their directories.

### ML-4

A module that another module of its directory imports MUST NOT read or write a file other than one that ships with it, such as a template or a data set.

It takes its input as data and returns its result as data, so it can be called and tested without files.

## Description

### ML-6

The README of the directory MUST name each layer, from the lowest to the highest, the modules it holds and what it does.

### ML-7

The README of the directory MUST name the modules that read or write files other than files that ship with them.

### ML-8

The README of the directory MUST show the imports between its modules as a diagram.

DOC-4 requires the diagram to be generated from the code.

## Checks

### ML-9

A check in CI MUST fail when a module breaks ML-2 or ML-3, taking the layers and their order from the README of the directory.

### ML-10

A check in CI MUST fail when the diagram of ML-8 no longer matches the imports.

## Example

A command-line tool with these layers in `src/`, as its README states them, lowest layer first:

| Layer | Modules | Does |
|---|---|---|
| Basics | `geo`, `tables` | Distances and bearings; parsing and formatting CSV tables |
| Domain | `route`, `report` | A route along days; the report as text |
| Steps | `compute` | Reads the input files, calls the layers below, writes the report |

The entry point `cli` parses the arguments and runs a step; nothing imports it, so it is no module and sits in no layer.

> Correct: `route` imports `geo`; `compute` imports `route`, `report` and `tables`; only `compute` reads and writes files, and it parses and formats their content with `tables`.
>
> Incorrect: `report` imports `compute` (ML-3); `route` opens the input file itself (ML-4).
