---
id: writing
title: Writing
version: 7.0.0
status: active
applies_to: [all]
summary: "How the texts of a repository are written, from its documents to its issues, pull requests, comments and commit messages: their language, how a description opens, how they name people, how long their titles are, and how they reference issues, pull requests and sources."
---

# Writing

This file governs how the texts of a repository are written: its documents, issues, pull requests, comments and commit messages.

Prefix: `WR`

## Language

### WR-1

A repository's documents, instruction files such as `CLAUDE.md`, issues, pull requests, comments on either and commit messages MUST be in English, other than a document that is the repository's content, such as a German CV, and a license.

## Descriptions

### WR-10

The description of an issue or a pull request MUST open with what and why in at most three sentences that need no earlier conversation; what follows, other than what another rule asks for, MUST stand in collapsed `<details>` sections.

> Correct: `Rename setup.sh to install.sh: the README and the CI workflow call install.sh and fail without it.`, then the failing log in a `<details>` section
>
> Incorrect: `Apply the rename we agreed on.`, or the right text after the failing log

## Names of people

### WR-6

A person's name, whether a real name or an account handle, MUST take the form the following table gives for where it stands; a document that is the repository's content names people as its content requires.

| Where the name stands | Form |
|---|---|
| A field that records an author or rights holder, such as a commit's author, a `Co-authored-by` trailer or a license's copyright line | The real name |
| A document about the repository, such as the README, other than an instruction file, and outside a path or URL | No name and no handle; a role such as the maintainer, where a sentence needs a person |
| Anywhere else, such as an issue, a pull request, a comment, a commit message, source code, an instruction file, a path or a URL | The account handle on the forge; the real name for a person without an account there |

> Correct: `Copyright (c) 2026 Mona Lisa Octocat` in a LICENSE, `Reported by hubot.` in a pull request, `Ask the maintainer before a release.` in a README
>
> Incorrect: `Copyright (c) 2026 octocat` in a LICENSE, `Reported by Hubot Jones.` in a pull request, where hubot has an account, `Maintained by @octocat.` in a README

## Titles

### WR-5

The title of an issue, the title of a pull request and the first line of a commit message MUST each be at most 105 characters, not counting a pull request number that a forge appends to that line on merge.

> Correct: `feat: add a writing standard for the rules on every text, from a README to its issues and commit messages (#145)`, 105 characters before the appended number
>
> Incorrect: `fix: stop the import at the first corrupt file instead of skipping it and reporting the import as complete`, 106 characters

## References to issues and pull requests

### WR-7

In an issue's or pull request's description and in a comment on either, a reference to an issue or pull request MUST be its number, after its repository path if in another one, with its title in parentheses at its first reference outside a list item.

GitHub shows the title next to a reference only in a list item, so elsewhere the text carries it, once.

> Correct: `Closes #131 (Decide how sound reference links are kept open)`, `- #135: the proposal as written.` as a list item
>
> Incorrect: `Lands with #132.` as the first reference to #132, `Lands with [Settle how a file names a person](https://github.com/o/r/issues/132).`

## Links to sources

### WR-8

Where a document of the repository, any file of it written as prose for a person or an AI agent to read, states a fact taken from an outside source that has a URL, the sentence, list item or table cell stating it MUST link to that source.

> Correct: `Versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).`
>
> Incorrect: `Versions follow Semantic Versioning 2.0.0.`, with the link only in a list of references at the end of the document

### WR-9

A link in a document of the repository to a page outside the repository MUST stand in a sentence, list item or table cell that states a fact the document takes from that page.

A link that backs no statement has nothing that shows when it can go, so a list of links grows without pruning.

> Correct: `The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope.`
>
> Incorrect: a section "Further reading" that lists links, `See also [Semantic Versioning](https://semver.org/).`
