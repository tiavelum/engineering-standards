# engineering-standards

The normative engineering standards used across tiavelum's repositories. Naming, repository layout, git workflow, README and documentation rules, written so that a person can read them and a tool or agent can load them.

## What it is for

This repo is the single source of truth for how work is structured across repositories: what files are called, how a repo is laid out, what a commit message says, what a README must contain. It exists so those decisions are made once, in one place, and applied everywhere, including when the files are not written by hand.

It covers conventions that a linter cannot check. Formatting, import order and line length belong in tool configuration, not here. See [standards/tooling.md](standards/tooling.md) for that boundary.

It is not a tutorial, not a style guide for any single language, and not a record of past decisions.

## Getting started

### As a reader

1. Read [meta/rule-format.md](meta/rule-format.md) to understand how a standard is written and how rules are identified.
2. Open the standard you need from [`standards/`](standards/).
3. Apply the MUST rules. Deviations need a written reason in the consuming repo.

### As a consumer (tool, agent, or script)

1. Fetch [`index.yaml`](index.yaml). It is the authoritative catalogue of every standard, with its id, path, scope, summary and dependencies.
2. Select the entries whose `applies_to` matches the task at hand.
3. Fetch those files and everything their `requires` lists name, resolved transitively. Nothing else.
4. Apply the rules by id. Cite the id when reporting a violation, for example `NAM-3`.

A standard that defers to another says so in its `requires`, so the closure is what makes the rules applicable. The consumer contract, including versioning and what a consumer must not assume, is in [meta/consuming.md](meta/consuming.md).

### As a contributor

Every change is validated against the rules in [meta/rule-format.md](meta/rule-format.md). Run the checks CI runs locally before opening a pull request.

Prerequisites: Python 3.10 or later. The tool versions are pinned in [requirements.txt](requirements.txt).

```bash
pip install -r requirements.txt
ruff format --check .
ruff check .
python3 scripts/validate-standards.py
```

Each command exits with status 0 when the change passes. The last one prints:

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
Load:     index.yaml -> entry `naming` -> standards/naming.md
Rules:    NAM-2  file names use lowercase words separated by single hyphens
          NAM-19 a name must not refer to when work was done
Result:   two violations. Lowercasing gives `session-notes-august.md`, which
          NAM-19 still rejects: August records when the sessions happened,
          not what they are about. Name the file for its subject.
```

## Content and structure

| Path | Contains |
|------|----------|
| `index.yaml` | The authoritative catalogue of standards. Every consumer starts here. |
| `standards/` | The standards themselves. One topic per file. |
| `meta/` | Rules about the rules: file format, precedence, consumer contract. |
| `scripts/` | The validator that enforces the rules this repo can check itself. |
| `.github/` | The workflow that runs the formatter check, the linter and the validator on every push and pull request. |

Start here: [`index.yaml`](index.yaml), then [meta/rule-format.md](meta/rule-format.md).

## Mental model

Three layers, each with one job.

**Index.** A catalogue that lets any consumer discover what exists and load only what it needs, without parsing prose. Each entry declares what must be loaded with it, so "what it needs" is a fact in the index rather than something read out of the prose.

**Standards.** The rules. Each file covers one topic, carries front matter describing its scope, and gives every rule a stable id so it can be cited, tested and reported against.

**Meta.** How the standards are written, how conflicts between them and a local repo are resolved, and what a consumer may rely on.

The distribution mechanism sits outside this repo on purpose. Nothing here assumes it is loaded by a skill, a plugin, a submodule or a person with a browser. See [meta/consuming.md](meta/consuming.md).

## Contributing

Changes are proposed as pull requests. Whether a new rule belongs here is decided by the admission test RF-1, and what a changed standard must carry with it by RF-17 to RF-19, both in [meta/rule-format.md](meta/rule-format.md).

CI runs the checks under "As a contributor" on every push and pull request and fails the build on a violation. Each check in [scripts/validate-standards.py](scripts/validate-standards.py) names the rule it enforces; the rules it cannot check are enforced in review.

## License

MIT. See [LICENSE](LICENSE).
