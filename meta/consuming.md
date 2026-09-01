---
id: consuming
title: Consumer contract
version: 1.0.0
status: active
applies_to: [tooling, agents]
summary: What a tool, agent or script may rely on when loading these standards, and what it must not assume.
---

# Consumer contract

A consumer is anything that loads these standards to apply them: a skill, a plugin, a CI check, a script, or a person with a browser. This file is the interface those consumers code against.

## Loading

**CO-1** A consumer MUST start from `index.yaml` and MUST NOT discover standards by listing directories or guessing paths.

**CO-2** A consumer MUST load only the entries whose `applies_to` matches the task, and MUST NOT assume that loading every standard is necessary or affordable.

**CO-3** A consumer MUST treat each standard file as self-contained. It MUST NOT require another file to be loaded in order to apply the rules in one.

**CO-4** A consumer MUST ignore entries with `status: draft` unless explicitly asked to include them, and MUST warn when applying an entry with `status: deprecated`.

## Applying

**CO-5** A consumer MUST cite the rule identifier when reporting a violation or justifying a decision, for example `NAM-2`.

**CO-6** A consumer MUST apply the precedence order in `meta/precedence.md` rather than assuming these standards outrank a direct instruction.

**CO-7** A consumer MUST NOT invent rules. If the standards are silent on a point, the consumer applies the community default and says so.

**CO-8** A consumer that produces a file governed by a standard SHOULD state which standards it applied.

## Stability guarantees

**CO-9** `index.yaml` keeps its `schema_version`. A breaking change to the index structure increments it.

**CO-10** File paths listed in `index.yaml` are stable within a major version of the standard they point at.

**CO-11** Rule identifiers are stable and are never reused. A consumer MAY store a rule id as a durable reference.

**CO-12** Consumers MUST NOT rely on line numbers, heading order, or any structure not described in `meta/rule-format.md`.

## What a consumer must not assume

**CO-13** The repository is not guaranteed to be reachable at any given moment. A consumer that cannot fetch MUST say so rather than proceeding from memory of an earlier version.

**CO-14** These standards do not cover language specific style. A consumer MUST NOT infer formatting rules from silence here.

## Distribution mechanisms

This repository is deliberately mechanism neutral. The same content can be delivered by any of the following, and the choice is made per consuming context, not here.

| Mechanism | Currency | Offline | Cost |
|-----------|----------|---------|------|
| Fetch from this repo at use time | Always current | No | One network call per file |
| Bundled into a plugin or package | Pinned to the release | Yes | Requires a release and an update flow |
| Vendored or submoduled into a repo | Pinned to the commit | Yes | One copy per consuming repo to maintain |
| Pointer file in the consuming repo | Depends on what the pointer resolves to | No | Cheapest to add, weakest guarantee |

**CO-15** A mechanism MUST satisfy CO-1 through CO-14 regardless of how the files reach the consumer.
