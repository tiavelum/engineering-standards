# engineering-standards

Normative engineering standards for repositories: naming, repository layout, git workflow, README and documentation rules, written so that anyone can read them and a person, AI agent, tool or script can load them to apply them.

## What it is for

This repo is the single source of truth for how work is structured across repositories: what files are called, how a repo is laid out, what a commit message says, what a README must contain. It exists so those decisions are made once, in one place, and applied everywhere, including when the files are not written by hand.

It covers conventions that have to be read to be followed. Formatting, import order and line length belong in tool configuration, not here. See [standards/tooling.md](standards/tooling.md) for that boundary.

It is not a tutorial, not a style guide for any single language, and not a record of past decisions.

## Getting started

### As a reader

1. Read [meta/rule-format.md](meta/rule-format.md) to understand how a standard is written and how rules are identified.
2. Open the standard you need from [`standards/`](standards/).
3. To apply the rules, follow "As a consumer" below.

### As a consumer (person, AI agent, tool or script)

1. Fetch [`index.yaml`](index.yaml). It is the authoritative catalogue of every standard, with its id, path, scope, summary and dependencies.
2. Select, load and apply its entries as the consumer contract, [meta/consuming.md](meta/consuming.md), says.
3. For a deviation of the consuming repository from a rule, follow [meta/precedence.md](meta/precedence.md).

The consumer contract also holds its stability guarantees and what a consumer must not assume.

### As a contributor

Every change is validated against the rules in [meta/rule-format.md](meta/rule-format.md). Run the checks CI runs locally before opening a pull request.

Prerequisites: Python 3.10 or later. The tool versions are pinned in [requirements.txt](requirements.txt).

```bash
pip install -r requirements.txt
ruff format --check .
ruff check .
python3 scripts/check-line-breaks.py
python3 scripts/validate-standards.py
```

Each command exits with status 0 when the change passes. The last one prints the number of warnings, which do not fail the run:

```
All checks passed. 0 warning(s).
```

A violation is reported with the file, the rule id and what is wrong:

```
error    standards/naming.md: [RF-30] front matter version does not match the index entry
```

## Example

Checking a file name against the standards:

```
Question: is `Session_Notes_August.md` acceptable?
Load:     index.yaml -> the entries whose `applies_to` matches the task
          (CO-2, CO-16): every `all` entry, and `consuming`, since
          whoever checks the name loads the standards to apply them;
          with their `requires`, resolved transitively (CO-3):
          meta/rule-format.md, meta/precedence.md, meta/consuming.md,
          standards/naming.md, standards/repo-layout.md,
          standards/git-workflow.md, standards/readme-contract.md,
          standards/documentation.md, standards/writing.md,
          standards/issues.md, standards/tooling.md
Rules:    NAM-2  file names use lowercase words separated by single hyphens
          NAM-1  a name describes what the thing is, not when it was made
Result:   two violations. Lowercasing gives `session-notes-august.md`, which
          NAM-1 still rejects: August records when the sessions happened,
          not what they are about. Name the file for its subject.
```

## Content and structure

| Path | Contains |
|------|----------|
| `index.yaml` | The authoritative catalogue of standards. Every consumer starts here. |
| `standards/` | The standards themselves. One topic per file. |
| `meta/` | Rules about the rules: file format, precedence, consumer contract. |
| `scripts/` | The validator that enforces the rules this repo can check itself, and a check that fails on a line break inside a paragraph of a Markdown file, which renders as a space. |
| `.github/` | The workflow that runs the formatter check, the linter, the line-break check and the validator on every pull request and every push to the default branch. |
| `.claude/` | Agent types for Claude Code sessions that work on this repository: `checker` and `worker`, each with its model, effort and tools. |
| `project-instructions.md` | Rules for Claude sessions that work on this repository. |
| `CLAUDE.md` | Imports `project-instructions.md` for Claude Code. |

Start here: [`index.yaml`](index.yaml), then [meta/rule-format.md](meta/rule-format.md).

## After changing the project instructions

Once a change to `project-instructions.md` is on `main`, paste the whole file into the instructions field of the claude.ai project used for this repository. That field holds a copy, which no tool updates. Claude Code reads the file from its clone through `CLAUDE.md`.

## Mental model

Three layers, each with one job.

**Index.** A catalogue that lets any consumer discover what exists and load only what it needs, without parsing prose. Each entry declares what must be loaded with it, so "what it needs" is a fact in the index rather than something read out of the prose.

**Standards.** The rules. Each file covers one topic, carries front matter describing its scope, and gives every rule a stable id so it can be cited, tested and reported against.

**Meta.** How the standards are written, how conflicts between them and a local repo are resolved, and what a consumer may rely on.

The distribution mechanism sits outside this repo on purpose. Nothing here assumes it is loaded by a skill, a plugin, a submodule or a person with a browser. See [meta/consuming.md](meta/consuming.md).

## Contributing

Changes are proposed as pull requests. Whether a new rule belongs here is decided by the admission test RF-1, RF-41, RF-42 and RF-44, how long a rule, its reason and its examples may be by RF-47, RF-14 and RF-48, what a changed standard must carry with it by RF-17, RF-18 and RF-19, and what its pull request follows by RF-45, all in [meta/rule-format.md](meta/rule-format.md).

CI runs the checks under "As a contributor" on every pull request and every push to the default branch and fails the build on a violation. Each check in [scripts/validate-standards.py](scripts/validate-standards.py) names the rule it enforces; the rules it cannot check are left to whoever reads the change. While the standards are shortened to the length limits, the validator lists the files not yet shortened in `LENGTH_PENDING` and only warns where they exceed a limit; each file leaves the list once it is shortened. [scripts/check-line-breaks.py](scripts/check-line-breaks.py) enforces no rule, since TL-2 keeps formatting out of the standards: it fails where two lines of a Markdown file would render as one, and names the line where that paragraph starts.

## License

MIT. See [LICENSE](LICENSE).
