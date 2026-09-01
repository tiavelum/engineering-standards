---
id: rule-format
title: Rule file format
version: 1.0.0
status: active
applies_to: [authoring]
summary: How a standard file is written, how rules are identified and versioned, and the admission test for new rules.
---

# Rule file format

This file governs how every file in `standards/` is written. It exists so that standards stay loadable in isolation, citable by id, and cheap to keep in sync.

## Admission test

**RF-1** A rule MUST be admitted only if at least one of the following holds:

- a tool can enforce it automatically,
- a reviewer can check it objectively in a pull request,
- an agent can apply it deterministically when producing a file.

**RF-2** A rule that fails RF-1 MUST NOT be added. Preferences that cannot be checked belong in conversation, not in this repository.

**RF-3** A rule that a tool already enforces MUST NOT be restated here. Point at the tool configuration instead. See `standards/tooling.md`.

## File structure

**RF-4** Each file in `standards/` MUST cover exactly one topic and MUST be understandable without loading any other standard.

**RF-5** Each file MUST begin with YAML front matter carrying: `id`, `title`, `version`, `status`, `applies_to`, `summary`.

**RF-6** `id` MUST be unique across the repository, lowercase, hyphen separated, and identical to the file's `id` in `index.yaml`.

**RF-7** `status` MUST be one of `active`, `draft`, `deprecated`. A `deprecated` file MUST name its replacement in the first paragraph.

**RF-8** `summary` MUST be a single sentence stating what the file governs.

**RF-9** A standard file SHOULD stay under 200 lines. Beyond that, split it by topic rather than adding sections.

## Rule identifiers

**RF-10** Every rule MUST carry an identifier of the form `<PREFIX>-<n>`, where `<PREFIX>` is a two or three letter uppercase abbreviation of the file `id`, unique across the repository.

**RF-11** Identifiers MUST be stable. A removed rule's number MUST NOT be reused. A rule whose meaning changes materially MUST get a new number and the old one MUST be marked withdrawn.

**RF-12** The identifier MUST be the first thing in the rule, in bold, followed by the rule text in a single sentence where possible.

## Rule language

**RF-13** Rules MUST use the keywords MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, in uppercase, with the meanings from RFC 2119.

**RF-14** A rule MUST state the required outcome, not the reasoning. Reasoning, where needed, goes in a separate paragraph that carries no identifier.

**RF-15** A rule MUST NOT contain two independent requirements. Split them.

**RF-16** Examples MUST be concrete and MUST show both the correct and the incorrect form where the distinction is the point.

## Versioning

**RF-17** Each standard file carries its own semantic version in front matter.

**RF-18** The version MUST be incremented as follows: major when an existing MUST rule changes or is removed, minor when a rule is added, patch for wording that does not change meaning.

**RF-19** A change to a standard MUST update the file, its front matter `version`, and its `index.yaml` entry in the same commit.

## Prohibited content

**RF-20** A standard file MUST NOT contain a changelog, migration notes, or any narration of how the rule came about.

**RF-21** A standard file MUST NOT contain TODOs, placeholders, or empty sections.

**RF-22** A standard file MUST NOT reference private repositories, internal systems or credentials.
