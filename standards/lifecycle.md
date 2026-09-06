---
id: lifecycle
title: Product lifecycle
version: 1.0.1
status: draft
applies_to: [all]
summary: The phases a product passes through from idea to operation, the artifact each produces, and the gate that must be passed to leave it.
---

# Product lifecycle

Prefix: `LC`

This standard governs a repository that produces a product. It does not govern a repository whose content is itself the deliverable, such as a document set or this one.

## Levels

**LC-1** A repository that produces a product MUST declare a lifecycle level of `0`, `1` or `2` in `docs/lifecycle.md`.

**LC-2** A repository at level 0 MUST satisfy only LC-1 and LC-3 of this standard.

**LC-3** A repository at level 1 or 2 MUST NOT depend on a repository at level 0.

**LC-4** A repository at level 2 MUST satisfy LC-38 through LC-41 in addition to every other rule here.

Level 0 is exploratory, which is why it is exempt from everything but the two rules that keep it from being depended on. Level 1 is the default. Level 2 applies where a failure costs more than the record keeping, or where someone outside the project must be able to check that something was done rather than take it on trust.

## Phases

**LC-5** A product MUST pass the gates below in the order given.

| Phase | Artifact | Gate rules |
|-------|----------|------------|
| Idea | `docs/idea.md` | LC-7, LC-8, LC-9 |
| Needs | `docs/needs.md` | LC-10, LC-11, LC-12 |
| Requirements | `docs/requirements.md` | LC-13 to LC-18 |
| Architecture | `docs/architecture.md` | LC-19 to LC-22 |
| Design | `docs/design.md` | LC-23, LC-24, LC-25 |
| Build | source, tests, changelog | governed by `standards/git-workflow.md` |
| Verification | `docs/verification.md` | LC-26, LC-27 |
| Validation | `docs/verification.md` | LC-28, LC-29, LC-30 |
| Release | `docs/operations.md` | LC-31, LC-32 |

**LC-6** A gate MUST be recorded as passed, with its date, at the foot of the artifact that the table names for it.

The build phase has no gate record of its own. Its evidence is a merged pull request, which `GW-1` and `GW-14` already govern.

## Idea

**LC-7** `docs/idea.md` MUST state the problem without naming a solution, a technology or a feature.

**LC-8** `docs/idea.md` MUST state success as an outcome an observer outside the project could notice.

**LC-9** `docs/idea.md` MUST state at least two non-goals.

## Needs

A need is what a person must be able to do. It is not what the system does; that is a requirement.

**LC-10** Each need MUST carry a unique identifier of the form `NEED-<n>`, and MUST NOT reuse a withdrawn identifier.

**LC-11** Each need MUST state who has it, what they must be able to do, and a priority of `must`, `should` or `could`.

**LC-12** A need MUST NOT name a technology or a user interface element.

## Requirements

**LC-13** Each requirement MUST carry a unique identifier of the form `REQ-<n>`, and MUST NOT reuse a withdrawn identifier.

**LC-14** Each requirement MUST state an acceptance criterion that a reader who did not write it can evaluate.

**LC-15** Each requirement MUST name the need it serves.

**LC-16** Each need of priority `must` MUST be served by at least one requirement.

**LC-17** A requirement MUST NOT describe how it is built.

**LC-18** `docs/requirements.md` MUST record, for each quality characteristic in ISO/IEC 25010, either a requirement or the reason that none applies.

The characteristics are functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility and safety. Most will not apply to a given product. LC-18 requires that each was considered, not that each produces a requirement.

## Architecture

**LC-19** `docs/architecture.md` MUST name the chosen approach and at least one rejected alternative with the reason for rejecting it.

**LC-20** `docs/architecture.md` MUST state what lies inside the product's boundary and what it depends on outside it.

**LC-21** Each component MUST carry a stated responsibility of one sentence.

**LC-22** Each requirement recorded under LC-18 as a quality requirement MUST name the mechanism that satisfies it.

## Design

**LC-23** Each requirement MUST be covered by at least one design element.

**LC-24** Each interface MUST state its inputs, its outputs and its errors.

**LC-25** Each external dependency named under LC-20 MUST have stated behaviour for when it is unavailable.

## Verification and validation

Verification asks whether the product was built to its requirements. Validation asks whether the requirements were the right ones. A product can satisfy every requirement and still fail to solve the problem, and only validation detects that.

**LC-26** Each requirement MUST have a recorded verification method of `test`, `analysis`, `inspection` or `demonstration`, together with the result.

**LC-27** A verification failure MUST be resolved by changing the design or the source, and MUST NOT be resolved by relaxing the requirement.

**LC-28** Each need of priority `must` MUST be recorded as confirmed against use of the product rather than against its tests.

**LC-29** `docs/verification.md` MUST record an evaluation of the success outcome stated under LC-8.

**LC-30** A validation failure MUST be resolved by changing the needs or the requirements, and MUST NOT be resolved by changing only the source.

## Release

**LC-31** `docs/operations.md` MUST enable a reader who did not build the product to install it, run it and roll it back.

**LC-32** `docs/operations.md` MUST state what becomes of the product's data when the product is retired.

Known limitations at release are covered by `RM-18` and are not restated here.

## Deferred work

**LC-33** Work consciously left undone at a gate MUST be recorded as an issue per `DOC-21` before that gate is recorded as passed.

**LC-34** An issue recording deferred work MUST state the condition under which the work becomes due, and MUST NOT use a date as that condition.

**LC-35** A gate record MUST name every issue raised under LC-33 for that gate.

A condition is checkable and a date is not: a date passes whether or not the work has become necessary. `DOC-14` already requires the same of a comment marking a known compromise.

## Re-entry

**LC-36** A change that invalidates an artifact named in LC-5 MUST update that artifact, and every artifact below it in that table, in the same pull request.

**LC-37** A change that invalidates no artifact named in LC-5 MUST NOT create one.

LC-36 specialises `DOC-19` for the artifacts of this standard. It is what decides how much process a given change attracts: the phase re-entered is the one whose artifact has stopped being true, and a change that makes nothing untrue re-enters nothing.

## Level 2

**LC-38** Each requirement MUST name the design elements and the verification entries that satisfy it.

**LC-39** `docs/requirements.md`, `docs/architecture.md` and `docs/design.md` MUST each carry a version in front matter, incremented whenever the file changes.

**LC-40** Each decision that fixes a component boundary or a technology MUST be recorded per `DOC-10`.

**LC-41** A gate record MUST name the person who reviewed it, and that person MUST NOT be the author of the artifact.
