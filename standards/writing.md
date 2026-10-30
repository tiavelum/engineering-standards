---
id: writing
title: Writing
version: 6.0.0
status: active
applies_to: [all]
summary: "How the texts of a repository are written, from its documents to its issues, pull requests and commit messages: their language, the reader they are written for, how they name people, how long their titles are, how they reference issues and pull requests, and how they link external sources."
---

# Writing

This file governs how the texts of a repository are written, for everyone who writes one: its documents and other files, its issues, its pull requests and its commit messages. Each rule names the texts it applies to.

Prefix: `WR`

## Language

**WR-1** A repository's README, every other document about the repository, every instruction file that directs an AI agent, such as `CLAUDE.md`, every issue, the title and description of every pull request, and every commit message MUST be written in English. A document about the repository is any document of the repository, as WR-8 defines it, other than a document that is the repository's content, a license, and an instruction file that directs an AI agent.

Instruction files, issues, pull requests and commit messages have the readers of the repository's documents. A document that is the repository's content rather than about it, such as a German CV or a German handbook, keeps the language that is the point of it, and a license keeps the language its text is written in.

## The reader who was not there

**WR-2** An issue and the description of a pull request MUST state what the work is and why, in terms a reader who was not present when the text was written can act on.

The work of a pull request is the change it makes, and its reader acts on it by reviewing it; the reader of an issue acts on it by doing or deciding its work. A text that relies on what was said in a conversation or a call leaves such a reader to ask its author.

Correct: `Rename setup.sh to install.sh: the README and the CI workflow both call install.sh, and both fail because the file is not found.`
Incorrect: `Apply the rename we agreed on.`, `Fix as discussed.`

## Names of people

**WR-6** A name of a person, whether a real name or an account handle, MUST take the form given in the row of the following table that names the place where the name stands. A file that is the repository's content rather than about it is outside this rule.

| Where the name stands | Form |
|---|---|
| A field made to record a person as author or rights holder, such as the author of a commit, a `Co-authored-by` trailer of a commit message or the copyright line of a license | The real name the field requires |
| An identifier that a tool or a link resolves, other than an `@` mention in a document about the repository, such as a repository path like `octocat/tools`, a URL, an entry of [`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-syntax) or [an `@` mention](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams) in an issue | The account handle |
| A name in a file that is not a document about the repository, such as a license, source code, a configuration file or an instruction file that directs an AI agent, such as `CLAUDE.md`, outside the places of the first two rows | The account handle on the forge that hosts the repository; the real name for a person who has no account there |
| A name of the owner, or a name that says who does something, in a document about the repository, such as the README, whether written out, as an `@` mention or as the visible text of a link, outside the places of the first two rows | No name and no handle; a role such as the user or the maintainer, where the sentence needs a person |
| A name in the running text of an issue, a pull request, a comment on either, or a commit message, outside the places of the first two rows | The account handle on the forge that hosts the repository; the real name for a person who has no account there |

What a name does decides its form, not the file it is in: a field made for an author asks for the person, a path or [a mention](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#mentioning-people-and-teams) works only with the handle, and a document about the repository says what the repository does, not whose it is. A clone URL or a repository path that contains the owner's handle is a path, not a name, so it stays in the second row in a document about the repository too. A `Co-authored-by` trailer has the form and purpose of a commit's author field, so it takes the real name as that field does. In an issue, a pull request, a commit message and a file such as source code or an instruction file, a person is named by the handle that mentions and paths already work with, so one person has one name in all of them; a person without an account on that forge has no handle there, so the real name stands instead. An instruction file directs an AI agent rather than describing the repository, so it names the owner as source code does. A file that is the repository's content, such as a crew list in a sailing handbook or a CV, names people as its content requires.

Correct: `A sailing logbook built from the photos of each charter trip.` and `git clone https://github.com/octocat/sailing-logbook` in a README, `Copyright (c) 2026 Mona Lisa Octocat` in a LICENSE, `Co-authored-by: Mona Lisa Octocat <mona@example.com>` in a commit message, `# Mirrors octocat's backup drive` in a shell script, `Ask octocat before you publish a release.` in `CLAUDE.md`, `Reported by hubot, who also tested the fix.` in a pull request, `# Uses the formula from Jane Roe's thesis` in a Python file, where Jane Roe has no account
Incorrect: `A logbook of the charter trips octocat skippers.`, `Maintained by @octocat.` and `Maintained by [octocat](https://github.com/octocat).` in a README, `Copyright (c) 2026 octocat` in a LICENSE, `Co-authored-by: octocat <mona@example.com>` in a commit message, `# Mirrors Mona's backup drive` in a shell script, `Ask Mona before you publish a release.` in `CLAUDE.md`, `Reported by Hubot Jones, who also tested the fix.` in a pull request, where hubot has an account, `# Uses the formula from jroe's thesis` in a Python file, where Jane Roe has no account

## Titles

**WR-5** The title of an issue, the title of a pull request and the first line of a commit message MUST each be at most 105 characters, not counting a pull request number that a forge appends to that line on merge.

A squash merge can [take a pull request's title as the first line of its commit](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests), so one limit lets either be written as the other.

Correct: `feat: add a writing standard for the rules on every text, from a README to its issues and commit messages (#145)`, 105 characters before the appended number
Incorrect: `fix: stop the import at the first corrupt file instead of skipping it and reporting the import as complete`, 106 characters

## References to issues and pull requests

**WR-7** In the description of an issue or a pull request and in a comment on either, each reference to an issue or a pull request MUST be written as its number, preceded by its repository path where it is in another repository. For each issue or pull request, the first reference to it in that description or comment that stands outside a list item MUST be followed in parentheses by its full title, as the title reads when the reference is written, and any other reference to it MUST NOT.

As GitHub's [Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls) describes, GitHub renders a number, and a pasted URL of an issue or a pull request, as a short link that shows the number, and unfurls a reference to show its title only in a list, and there only on github.com and GitHub Enterprise Cloud. Outside a list item the text carries the title, so the reader sees what a reference names without opening it; it carries it once, at the first reference outside a list item, and later references outside one rely on it. Each description and each comment carries the title on its own, since each can be read without the others. In a list item GitHub [shows the title already](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls), and a title written after it would show twice. Where the text is read without GitHub's rendering, as when a squash merge [can make a pull request's description the body of its commit](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests), a reference in a list item shows its number alone. The number comes first, so that GitHub still [links it](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls) and a [closing keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) such as `Closes` still works. A title changed later does not make the reference wrong: the number stays authoritative.

Correct: `Lands with #132 (Settle when a file names a person, a role or an account handle).`, `Lands with #132 (Settle when a file names a person, a role or an account handle) and #135 (Decide where the one-time setup steps of a repository live).`, `Closes #131 (Decide how sound reference links found in research are kept open)`, `See octocat/tools#12 (Add a dry-run flag); octocat/tools#12 also adds a test.` in one comment, `- #135: the proposal as written.` as a list item, `- #135: the proposal.` followed in the same comment by `Lands with #135 (Decide where the one-time setup steps of a repository live).`
Incorrect: `Lands with #132.` as the first reference to #132 in a comment, `See octocat/tools#12 (Add a dry-run flag); octocat/tools#12 (Add a dry-run flag) also adds a test.` in one comment, `- #135 (Decide where the one-time setup steps of a repository live): the proposal as written.` as a list item, `Lands with Settle when a file names a person, a role or an account handle (#132).`, `Lands with [Settle when a file names a person, a role or an account handle](https://github.com/tiavelum/engineering-standards/issues/132).`, `Lands with https://github.com/tiavelum/engineering-standards/issues/132.`

## Links to sources

**WR-8** Where a document of the repository, any file of it written as prose for a person or an AI agent to read, states a fact taken from a source outside the repository that has a URL, the sentence, list item or table cell that states it MUST link to that source.

The link stands where a reader checks the fact and stays as long as the statement does, so a sound source found in research is kept without a list to maintain.

Correct: `Versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).`
Incorrect: `Versions follow Semantic Versioning 2.0.0.`, with the link only in a list of references at the end of the document

**WR-9** A link in a document of the repository, as WR-8 defines it, to a page outside the repository MUST stand in a sentence, list item or table cell that states a fact the document takes from that page.

A link that supports no statement has nothing that shows when it can go. A list or section of links apart from the statements they back grows without pruning and drifts from them.

Correct: `The form is that of [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), without a scope.`, `The default timeout is 30 seconds, as [the configuration reference](https://example.org/reference) lists.`
Incorrect: a section "Further reading" that lists links, `See also [Semantic Versioning](https://semver.org/).`, `Read [the Git book](https://git-scm.com/book/en/v2) for details.`
