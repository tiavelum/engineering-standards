---
id: versioning
title: Versioning
version: 1.0.1
status: active
applies_to: [all]
summary: How a release version is formed, where it is recorded, and when each component is incremented.
---

# Versioning

Prefix: `VER`

## The scheme

**VER-1** A repository that publishes releases MUST version them according to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

The specification is incorporated by reference. The rules below narrow it for these repositories; none of them contradicts it. Where this file is silent, the specification governs.

**VER-2** A repository that publishes no release MUST NOT carry a version.

## The version of record

**VER-3** A repository MUST hold its version in exactly one place.

**VER-4** The version of record MUST be the location its ecosystem defines:

| Ecosystem | Version of record |
|---|---|
| Node | `package.json`, `version` |
| Python | `pyproject.toml`, `[project] version` |
| Rust | `Cargo.toml`, `[package] version` |
| Go | the git tag, since Go has no manifest version |
| Container image | the git tag, mirrored into the image tag |
| Anything else | a `VERSION` file at the repository root |

**VER-5** Every other occurrence of the version MUST be derived from the version of record when the artifact is built.

A version written by hand in a second place is a version that will disagree with the first. Documentation, build arguments, generated headers and image tags all read from the one location.

## Incrementing

**VER-6** MAJOR MUST be incremented when a change is breaking under `standards/public-api.md`.

**VER-7** MINOR MUST be incremented when the public API gains functionality and nothing breaks.

**VER-8** MINOR MUST be incremented when any part of the public API is marked deprecated.

**VER-9** PATCH MUST be incremented when shipped behaviour changes and the public API does not.

**VER-10** When more than one of VER-6 to VER-9 applies to a release, the highest MUST be taken.

**VER-11** A change that alters no shipped artifact MUST NOT produce a release.

**VER-12** A dependency update MUST be classified by its effect on this repository's public API, not by the increment the dependency itself took.

A dependency going from 3.x to 4.x is not by itself a MAJOR here. It is MAJOR here only if this repository's own contract changes as a result.

**VER-13** Urgency MUST NOT lower the increment a change requires.

A security fix that breaks the public API is a MAJOR release. Reaching affected consumers sooner is handled by backporting under VER-25, not by mislabelling the change.

| Change | Increment | From 2.4.7 |
|---|---|---|
| Breaking change to the public API | MAJOR | 3.0.0 |
| Backward compatible addition | MINOR | 2.5.0 |
| Deprecation marked | MINOR | 2.5.0 |
| Bug fix, no API change | PATCH | 2.4.8 |
| Internal refactor, observable behaviour unchanged | PATCH | 2.4.8 |
| Documentation, tests or CI only | none | 2.4.7 |

## Initial development

**VER-14** Initial development MUST start at `0.1.0`.

**VER-15** A repository that runs in production, or that has any consumer outside its own repository, MUST be at `1.0.0` or higher.

`0.y.z` states that the public API is not stable. It MUST NOT be used to avoid the discipline of MAJOR increments on software that others already depend on.

**VER-16** Below `1.0.0`, a breaking change MUST increment MINOR and every other change MUST increment PATCH.

## Pre-release and build metadata

**VER-17** A pre-release identifier MUST be `alpha`, `beta` or `rc`, followed by a dot and an integer counting from 1.

Correct: `2.0.0-rc.1`, `2.0.0-beta.3`
Incorrect: `2.0.0-rc1`, `2.0.0-andi-test`, `2.0.0-final`

**VER-18** A released repository MUST NOT depend on a pre-release version of anything.

**VER-19** Build metadata MUST NOT be the only difference between two published artifacts.

Build metadata is ignored when versions are compared, so two artifacts that differ only there are indistinguishable to a consumer. If the content differs, the version differs.

## Immutability

**VER-20** A published version MUST NOT be altered after publication.

**VER-21** A version that turns out to be wrong MUST be superseded by a higher version, never reissued under the same number.

## Deprecation and removal

**VER-22** Public API MUST NOT be removed until it has been published as deprecated in at least one MINOR release of the current MAJOR line.

**VER-23** A deprecation MUST name the version in which removal is planned.

## Supported lines

**VER-24** A repository MUST state which MAJOR lines it supports and until when.

Where a repository says nothing, only the current MAJOR line is supported.

**VER-25** A fix MUST be committed to `main` before it is backported to a supported line.

Fixing a release branch first is how a fix gets lost in the next MAJOR.

**VER-26** Versions MUST be ordered by the comparison rules of the specification, never by sorting the version string.

`1.10.0` sorts below `1.9.0` as text and above it as a version.

**VER-27** A consumer MUST express a dependency as a range bounded above by the next MAJOR.

Correct: `>=3.1.0 <4.0.0`
Incorrect: `>=3.1.0`, `*`, a bare `latest`
