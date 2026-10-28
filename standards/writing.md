---
id: writing
title: Writing
version: 1.0.0
status: active
applies_to: [all]
summary: "How the texts of a repository are written, from its documents to its issues, pull requests and commit messages: their language, the reader they are written for, and how they name people."
---

# Writing

This file governs how the texts of a repository are written, for everyone who writes one: its documents and other files, its issues, its pull requests and its commit messages. Each rule names the texts it applies to.

Prefix: `WR`

## Language

**WR-1** A repository's README, every other document about the repository, every issue and every commit message MUST be written in English.

Issues and commit messages have the readers of the repository's documents. A document that is the repository's content rather than about it, such as a German CV or a German handbook, keeps the language that is the point of it.

## The reader who was not there

**WR-2** An issue and the description of a pull request MUST state what the work is and why, in terms a reader who was not present when the text was written can act on.

The work of a pull request is the change it makes, and its reader acts on it by reviewing it; the reader of an issue acts on it by doing or deciding its work. A text that relies on what was said in a conversation or a call leaves such a reader to ask its author.

Correct: `Rename setup.sh to install.sh: the README and the CI workflow both call install.sh, and both fail because the file is not found.`
Incorrect: `Apply the rename we agreed on.`, `Fix as discussed.`

## Names of people

**WR-3** A document about the repository MUST NOT name the repository's owner.

A document says what the repository does, not whose it is. Where a sentence needs a person, a role such as the user or the developer names them. A file that has to name the owner, such as a license, is not a document about the repository.

Correct: `A sailing logbook built from the photos of each charter trip.`
Incorrect: `A logbook of the charter trips octocat skippers.`

**WR-4** A file that is not a document about the repository MUST refer to the repository's owner by the owner's account handle, if at all.

Correct: `octocat's repositories`
Incorrect: `Mona's repositories`
