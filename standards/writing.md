---
id: writing
title: Writing
version: 3.0.0
status: active
applies_to: [all]
summary: "How the texts of a repository are written, from its documents to its issues, pull requests and commit messages: their language, the reader they are written for, how they name people, how long their titles are, how they reference issues and pull requests, and how they link external sources."
---

# Writing

This file governs how the texts of a repository are written, for everyone who writes one: its documents and other files, its issues, its pull requests and its commit messages. Each rule names the texts it applies to.

Prefix: `WR`

## Language

**WR-1** A repository's README, every other document about the repository, every issue, the title and description of every pull request, and every commit message MUST be written in English.

Issues, pull requests and commit messages have the readers of the repository's documents. A document that is the repository's content rather than about it, such as a German CV or a German handbook, keeps the language that is the point of it.

## The reader who was not there

**WR-2** An issue and the description of a pull request MUST state what the work is and why, in terms a reader who was not present when the text was written can act on.

The work of a pull request is the change it makes, and its reader acts on it by reviewing it; the reader of an issue acts on it by doing or deciding its work. A text that relies on what was said in a conversation or a call leaves such a reader to ask its author.

Correct: `Rename setup.sh to install.sh: the README and the CI workflow both call install.sh, and both fail because the file is not found.`
Incorrect: `Apply the rename we agreed on.`, `Fix as discussed.`

## Names of people

**WR-6** A name of a person, whether a real name or an account handle, MUST take the form given in the row of the following table that names the place where the name stands. A file that is the repository's content rather than about it is outside this rule.

| Where the name stands | Form |
|---|---|
| A field made to record a person as author or rights holder, such as the author of a commit or the copyright line of a license | The real name the field requires |
| An identifier that a tool or a link resolves, other than an `@` mention in a document about the repository, such as a repository path like `octocat/tools`, a URL, an entry of `CODEOWNERS` or an `@` mention in an issue | The account handle |
| A name of the owner in a file that is not a document about the repository, such as a license, source code or a configuration file, outside the places of the first two rows | The account handle |
| A name of the owner, or a name that says who does something, in a document about the repository, such as the README, whether written out, as an `@` mention or as the visible text of a link, outside the places of the first two rows | No name and no handle; a role such as the user or the maintainer, where the sentence needs a person |

What a name does decides its form, not the file it is in: a field made for an author asks for the person, a path or a mention works only with the handle, and a document about the repository says what the repository does, not whose it is. A clone URL or a repository path that contains the owner's handle is a path, not a name, so it stays in the second row in a document about the repository too. A file that is the repository's content, such as a crew list in a sailing handbook or a CV, names people as its content requires.

Correct: `A sailing logbook built from the photos of each charter trip.` and `git clone https://github.com/octocat/sailing-logbook` in a README, `Copyright (c) 2026 Mona Lisa Octocat` in a LICENSE, `# Mirrors octocat's backup drive` in a shell script
Incorrect: `A logbook of the charter trips octocat skippers.`, `Maintained by @octocat.` and `Maintained by [octocat](https://github.com/octocat).` in a README, `Copyright (c) 2026 octocat` in a LICENSE, `# Mirrors Mona's backup drive` in a shell script

## Titles

**WR-5** The title of an issue, the title of a pull request and the first line of a commit message MUST each be at most 65 characters, not counting a pull request number that a forge appends to that line on merge.

A pull request's title becomes the first line of the commit a squash merge makes, so one limit lets either be written as the other. With a number such as ` (#145)` appended, the line still reads without wrapping.

Correct: `feat: add a writing standard for the rules on every text (#145)`, 56 characters before the appended number
Incorrect: `fix: stop the import at the first corrupt file instead of skipping it silently`, 78 characters

## References to issues and pull requests

**WR-7** In the description of an issue or a pull request and in a comment on either, each reference to an issue or a pull request MUST be written as its number, preceded by its repository path where it is in another repository, and followed in parentheses by its full title as the title reads when the reference is written.

As GitHub's [Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls) describes, GitHub renders a number, and a pasted URL of an issue or a pull request, as a short link that shows the number, and unfurls a reference to show its title only in a list, and there only on github.com and GitHub Enterprise Cloud. In such a list the title shows twice. The text carries it all the same: a squash merge makes a pull request's description the body of a commit, where nothing unfurls, and one form in every place needs no exception. The number comes first, so that GitHub still links it and a closing keyword such as `Closes` still works. A title changed later does not make the reference wrong: the number stays authoritative.

Correct: `Lands with #132 (Settle when a file names a person, a role or an account handle).`, `Closes #131 (Decide how sound reference links found in research are kept)`, `See octocat/tools#12 (Add a dry-run flag).`
Incorrect: `Lands with #132.`, `Lands with Settle when a file names a person, a role or an account handle (#132).`, `Lands with [Settle when a file names a person, a role or an account handle](https://github.com/octocat/tools/issues/132).`, `Lands with https://github.com/octocat/tools/issues/132.`

## Links to sources

**WR-8** A fact that a document of the repository takes from a source outside the repository that has a URL MUST be linked to that source in the sentence, list item or table cell that states it.

The link stands where a reader checks the fact and stays as long as the statement does, so a sound source found in research is kept without a list to maintain.

Correct: `Versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).`
Incorrect: `Versions follow Semantic Versioning 2.0.0.`, with the link only in a list of references at the end of the document

**WR-9** A link in a document of the repository to a page outside the repository MUST stand in a sentence, list item or table cell that states a fact the document takes from that page.

A link that supports no statement has nothing that shows when it can go. A list or section of links apart from the statements they back grows without pruning and drifts from them.

Correct: `The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope.`, `Every option is listed in [the configuration reference](https://example.org/reference), which this README does not copy.`
Incorrect: a section "Further reading" that lists links, `See also [Semantic Versioning](https://semver.org/).`, `Read [the Git book](https://git-scm.com/book/en/v2) for details.`
