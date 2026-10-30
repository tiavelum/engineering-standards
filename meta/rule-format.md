---
id: rule-format
title: Rule file format
version: 8.0.1
status: active
applies_to: [authoring]
summary: How a standard file is written and changed, how rules are identified and versioned, and the admission test for new rules.
---

# Rule file format

This file governs how every file in `standards/` and `meta/` is written and changed. It exists so that standards stay loadable in isolation, citable by id, and cheap to keep in sync.

## Admission test

**RF-1** A rule MUST be admitted only if at least one of the following holds:

- a tool can enforce it automatically,
- a reviewer can check it objectively in a pull request,
- an AI agent can apply it deterministically when producing a file.

Preferences that cannot be checked belong in conversation, not in this repository. What a formatter or linter sets is kept out of a standard by TL-2. A rule in inexact terms cannot be checked objectively either.

**RF-44** A rule MUST be admitted only if it holds whether a person or an AI agent does the work it governs.

These standards are followed by every repository, whoever does its work. A rule that binds an AI agent doing the work but not a person doing the same work, such as one about the AI agent's own instructions, belongs with those instructions.

Correct: `A pull request is merged only after a review by a party that neither wrote nor directed its changes.`\
Incorrect: `An AI agent names its model at the end of every commit message it writes.`

**RF-41** A rule MUST NOT exempt anything from another rule.

A rule that needs an exemption from another shows that the other is scoped wrongly, and rescoping it removes the need.

**RF-42** A rule MUST NOT state a requirement another rule already states.

Two statements of one requirement drift apart; a citation by identifier keeps one.

## File structure

**RF-4** Each file in `standards/` MUST cover exactly one topic.

**RF-5** Each file MUST begin with YAML front matter carrying: `id`, `title`, `version`, `status`, `applies_to`, `summary`.

**RF-6** `id` MUST be unique across the repository.

**RF-35** `id` MUST be lowercase and hyphen separated.

**RF-7** `status` MUST be one of `active`, `draft`, `deprecated`.

**RF-37** A `deprecated` file MUST name its replacement in the first paragraph.

**RF-8** `summary` MUST be a single sentence stating what the file governs.

**RF-9** A standard file SHOULD stay under 200 lines.

Beyond that, split it by topic rather than adding sections.

## Index entries

**RF-27** `index.yaml` MUST carry `schema_version` and the sections `meta` and `standards`.

**RF-28** An entry MUST carry `id`, `path`, `title`, `version`, `status`, `summary` and `applies_to`.

**RF-29** An entry MUST NOT carry a field other than those named in RF-28, `tags` and `requires`.

**RF-30** An entry's `id`, `title` and `version` MUST equal those in the front matter of the file at its `path`.

**RF-31** An entry's `path` MUST resolve to an existing file in `standards/` or `meta/`.

**RF-32** Every file in `standards/` and `meta/` MUST be listed in exactly one entry.

The entry is closed rather than open. CO-20 promises a consumer that `schema_version` tracks a breaking change to the index structure, and that promise is empty while a field can appear without anyone announcing it. The cost is that a new field needs a rule before it needs code, which is the order this repository wants anyway.

DOC-51 covers the links of a file listed in `index.yaml`.

## Dependencies between standards

**RF-24** A file MUST be applicable given only itself and the standards its `index.yaml` entry names in `requires`.

**RF-25** A file's `index.yaml` entry MUST name in `requires` every other standard the file references.

**RF-26** A reference to another standard MUST name it by a rule identifier or by its repository relative path.

A standard that defers to another is not a defect; hiding that it does is. RF-26 fixes the reference form so that RF-25 can be checked mechanically rather than by reading. Over-declaring costs a consumer one fetch, and under-declaring makes it apply a rule whose terms it has not loaded, so a reference in an example counts the same as one in a rule.

## Rule identifiers

**RF-10** Every rule MUST carry an identifier of the form `<PREFIX>-<n>`, where `<PREFIX>` is a two or three letter uppercase abbreviation of the file `id`.

**RF-40** A prefix MUST be unique across the repository.

**RF-11** An identifier MUST NOT be reused for any rule other than the one it was first assigned to, including after that rule is removed.

**RF-43** A term written as a prefix of two or three uppercase letters, a hyphen and a number, in `index.yaml` or in a file it lists, in an example as anywhere else, MUST be the identifier of a rule in a file `index.yaml` lists, or be listed in `NOT_RULE_IDS` in `scripts/validate-standards.py`.

A citation of a removed or mistyped identifier points its reader at nothing, and RF-11 keeps a removed identifier from naming a rule again. A term such as UTF-8 has the same shape but names something other than a rule; listing it is how a file says so.

**RF-23** A rule whose meaning changes MUST keep its identifier.

A rule is amended in place and the version carries the change. RF-18 makes every change to a requirement a major increment, so a consumer that pinned a version meets the break where it already looks for one, and an identifier it stored stays valid.

**RF-12** The identifier MUST be the first thing in the rule, in bold.

**RF-34** A rule under review MUST carry the marker `(draft: #<issue>)` directly after its identifier, naming the issue that decides it.

A draft rule stays in its place and keeps its identifier, so it can be cited while it is discussed, and removing the marker puts it back in force. CO-17 tells a consumer to skip it.

## Rule language

**RF-13** A rule MUST state its keyword, one of MUST, MUST NOT, SHOULD, SHOULD NOT and MAY, in uppercase with its meaning from [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), on the line that carries its identifier.

That line is where a reader looks to find out whether a rule binds them, and where a check finds the keyword without guessing how far a rule extends.

**RF-14** A rule MUST state the required outcome; reasoning, where needed, stands in a separate paragraph without an identifier.

**RF-15** A rule MUST NOT contain two independent requirements.

Two requirements are independent when one can be met while the other is broken. Two parts are still one requirement when the second forbids only the alternative the first replaces, or when together they define one form, such as the form of a name or of a line. A rule that holds two independent requirements is split, and its identifier stays with the first (RF-23).

One requirement: `MUST start from index.yaml and MUST NOT discover standards by listing directories`.\
Two: `MUST name the problem solved and MUST state the scope boundary`.

**RF-16** Examples MUST be concrete.

**RF-39** Examples MUST show both the correct and the incorrect form where the distinction is the point.

## Versioning

**RF-17** A file's `version` MUST be a [semantic version](https://semver.org/).

**RF-18** The version MUST be incremented as follows: major when the file's set of requirements loses or changes a requirement; minor when it gains a requirement and loses or changes none; patch when it stays the same.

A split, a merge, or removing a rule whose requirement another rule of the same file already states leaves the set the same. A SHOULD that becomes a MUST, or a rule whose scope changes, changes a requirement.

**RF-19** A change to a standard MUST update the file, its front matter `version`, and its `index.yaml` entry in the same commit.

**RF-45** A file that a pull request adds or changes MUST follow, for each file listed in `index.yaml` that the same pull request adds or changes, that file as the pull request leaves it.

The validator run on the pull request's branch reads each file listed in `index.yaml` as the pull request leaves it, and once the pull request is merged, that version of the file is in force.

**RF-46** Every text of a pull request that changes a file listed in `index.yaml`, other than the files it adds or changes, such as its title, its description, its commit messages and its branch name, MUST follow, for each such file it changes, that file on the default branch.

The file on the default branch is in force while the change is under review. A squash merge can [turn the title and description into the commit message](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests) on the default branch, so they are written to the rules that hold when they are written.

Correct: a pull request that raises a limit on title length from 65 to 72 characters gives its own title at most 65 characters, and the examples in the file it changes up to 72\
Incorrect: the same pull request with a title of 70 characters

## Prohibited content

**RF-22** A standard file MUST NOT reference private repositories, internal systems or credentials.
