---
id: rule-format
title: Rule file format
version: 11.0.0
status: active
applies_to: [authoring]
summary: How a standard file is written and changed, how rules are identified and versioned, and the admission test for new rules.
---

# Rule file format

This file governs how a standard file, any file of `standards/` or `meta/` not named `README.md`, is written, indexed, identified and versioned.

## Admission test

### RF-1

A rule MUST be admitted only if a tool can enforce it, a person can check it objectively in a pull request, or an AI agent can apply it deterministically.

### RF-44

A rule MUST be admitted only if it holds whether a person or an AI agent does the work it governs.

A rule that binds only an AI agent, such as one on its own instructions, belongs with those instructions.

> Correct: `A merged branch MUST be deleted.`
>
> Incorrect: `An AI agent names its model at the end of every commit message it writes.`

### RF-41

A rule MUST NOT exempt anything from another rule, other than through the order of precedence that PR-1 sets.

A rule that needs an exemption from another shows that the other is scoped wrongly, and rescoping it removes the need.

### RF-42

A rule MUST NOT state a requirement another rule already states; it cites that rule by its identifier instead.

## File structure

### RF-4

Each standard file MUST cover one topic: what the summary of its `index.yaml` entry states.

A file is split by topic, not by length.

### RF-5

Each standard file MUST begin with YAML front matter carrying `id`, `title`, `version`, `status`, `applies_to` and `summary`.

### RF-6

`id` MUST be unique across the repository.

### RF-35

`id` MUST be lowercase and hyphen separated.

### RF-7

`status` MUST be one of `active`, `draft`, `deprecated`.

### RF-37

A `deprecated` file MUST name its replacement in the first paragraph.

### RF-8

`summary` MUST be a single sentence stating what the file governs.

## Index entries

### RF-27

`index.yaml` MUST carry `schema_version` and the sections `meta` and `standards`, and MUST NOT carry another top-level key.

### RF-28

An entry MUST carry `id`, `path`, `title`, `version`, `status`, `summary` and `applies_to`.

### RF-29

An entry MUST NOT carry a field other than those named in RF-28, `tags` and `requires`.

### RF-30

An entry's `id`, `title`, `version`, `status`, `summary` and `applies_to` MUST equal those in the front matter of the file at its `path`.

### RF-31

An entry's `path` MUST resolve to an existing standard file, with the entry under `meta` for a file in `meta/` and under `standards` for a file in `standards/`.

### RF-32

Every standard file MUST be listed in exactly one entry.

### RF-50

An entry with `status: active` MUST NOT name in `requires` an entry with `status: draft`.

A consumer ignores a draft (CO-4), so an active standard that rests on one cannot be applied whole.

## Dependencies between standards

### RF-24

A standard file MUST be applicable without any standard other than itself and those its `index.yaml` entry names in `requires`.

### RF-25

A file's `index.yaml` entry MUST name in `requires` every other standard the file references, in an example as anywhere else.

### RF-26

A reference to another standard MUST name it by a rule identifier or by its repository relative path.

## Rule identifiers

### RF-10

Every rule MUST carry an identifier of the form `<PREFIX>-<n>`, where `<PREFIX>` is a two or three letter uppercase abbreviation of the file `id`.

### RF-40

A prefix MUST NOT be used by more than one file, including a file that was removed.

### RF-11

An identifier MUST NOT be reused for any rule other than the one it was first assigned to, including after that rule is removed.

### RF-23

A rule whose meaning changes MUST keep its identifier.

### RF-12

Each rule MUST stand under a heading of its own, `### <identifier>`, with its text in the paragraph below the heading.

The heading makes the identifier stand out, gives the rule a link anchor and lists it in GitHub's outline of the file.

### RF-34

A rule under review MUST carry the marker `(draft: #<issue>)` in its heading, after its identifier, naming the issue that decides it.

### RF-43

A term of the form of RF-10 in `index.yaml` or a file it lists MUST be the identifier of a rule in a file `index.yaml` lists, unless it names something other than a rule, such as `UTF-8`.

### RF-49

A citation MUST name each rule identifier on its own, never a range such as `RF-27 to RF-32`.

A range hides the identifiers inside it, so a removed one goes unnoticed (RF-43).

## Rule language

### RF-13

A rule MUST state its keyword, one of MUST, MUST NOT, SHOULD, SHOULD NOT and MAY, in uppercase with its meaning from [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), in the first line of its text.

### RF-14

A rule MUST state only the required outcome; a reason, where its purpose is not self-evident, follows it as one paragraph, at most 250 characters.

### RF-47

The paragraph under a rule's heading MUST be at most 250 characters.

### RF-15

A rule MUST NOT hold two requirements of which one can be met while the other is broken, unless one only forbids the alternative to the other, or together they define one form or list one set.

> One requirement: `MUST start from index.yaml and MUST NOT discover standards by listing directories`
>
> Two: `MUST name the problem solved and MUST state the scope boundary`

### RF-16

Examples MUST be concrete.

### RF-39

Examples MUST show both the correct and the incorrect form where the distinction is the point.

### RF-51

Each example of a rule MUST stand in a blockquote below the rule, as a paragraph of its own; a sample of a whole file MAY stand in a fenced code block instead.

### RF-48

Each line of an example MUST be at most 200 characters.

## Versioning

### RF-17

A file's `version` MUST be a [semantic version](https://semver.org/).

### RF-18

A pull request that changes a standard file MUST raise its version from the one on the default branch by the first row of this table that fits the change.

| Increment | Change |
|---|---|
| Major | A requirement the file applies, its own or one from a standard it requires, stops applying to the file or is changed; an existing rule gains the marker of RF-34; the entry's `id` or `applies_to` changes; or the file moves (CO-10) |
| Minor | A requirement is added, or a rule loses the marker of RF-34 |
| Patch | Anything else, such as splitting or merging rules, or removing a rule whose requirement still applies through the file or a standard it requires |

### RF-19

A commit that changes a standard file MUST carry the version RF-18 gives the change in its front matter and its `index.yaml` entry.

### RF-45

A file that a pull request adds or changes MUST follow each standard file as the same pull request leaves it.

## Prohibited content

### RF-22

A standard file MUST NOT reference private repositories or internal systems.
