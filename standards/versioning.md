---
id: versioning
title: Versioning and public API
version: 4.0.0
status: active
applies_to: [software]
summary: What a repository publishes as its public API, which changes to it are breaking, when each component of its version is incremented, and how a release version is formed and recorded.
---

# Versioning and public API

Prefix: `VER`

## The scheme

A repository publishes a release by pushing a release tag in the form VER-28 sets.

**VER-1** A repository that publishes releases MUST version them according to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

The specification is incorporated by reference. The rules below narrow it for these repositories; none of them contradicts it. Where this file is silent, the specification governs.

**VER-2** A repository that publishes no release MUST NOT carry a version.

## The public API

Semantic versioning is meaningless without a declared public API, because every increment is a statement about that API.

**VER-34** A repository that publishes releases MUST declare its public API.

**VER-35** The declaration MUST name each surface that is public and each surface that is deliberately excluded.

**VER-36** A surface that the declaration does not mention MUST be treated as public.

The default is deliberately expensive. A repository that declares nothing has promised everything, including behaviour it never intended to guarantee. The way out is to declare.

**VER-37** An excluded surface MUST be marked where a consumer would encounter it, in the path, the symbol name, or the generated documentation.

Correct: an `internal/` package, a symbol prefixed `_`, an endpoint documented as experimental
Incorrect: an exclusion that exists only in the declaration, invisible to someone reading the code

## Public surfaces

**VER-38** The declaration MUST cover every surface the following table lists for each type in the table that describes the repository:

| Type | Public surface |
|---|---|
| Library | Exported symbols and their signatures, documented behaviour, error types returned or raised, supported runtime range |
| HTTP service | Paths, methods, request and response schemas, status and error codes, authentication scheme |
| CLI | Command names, flags, arguments, exit codes, and any output documented as machine readable |
| Container image | Entrypoint contract, required environment variables, mounted paths, exposed ports, configuration schema |
| Event producer or consumer | Topic names, message schemas, key semantics, delivery guarantees |
| Infrastructure module | Input variables and types, outputs, and resources whose replacement destroys state |
| Schema or configuration repository | The schema, and defaults consumers rely on |

Log text is not a public surface unless the repository documents a machine readable log format.

## Breaking changes

**VER-39** Each of the following MUST be treated as breaking:

- removing or renaming a public surface
- narrowing what an input accepts
- widening the values an existing output field may take
- making an optional input required
- changing a default in a way that alters existing behaviour
- changing the type, unit or meaning of a field
- adding a failure mode to an operation that previously could not fail
- dropping support for a runtime, platform or protocol version documented as supported
- a schema change that a reader at the previous version cannot read

**VER-40** The following MUST NOT be treated as breaking:

- adding an optional input, an optional output field, an endpoint, a command or a symbol
- widening what an input accepts
- changing performance without changing the contract

**VER-41** Where it is unclear whether a change is breaking, it MUST be treated as breaking.

The cost of an unnecessary MAJOR release is an inconvenience to the publisher. The cost of a missed one is an outage in someone else's system.

## Incrementing

**VER-6** From a version of `1.0.0` or higher, MAJOR MUST be incremented when a change is breaking under VER-39 to VER-41.

**VER-7** From a version of `1.0.0` or higher, MINOR MUST be incremented when the public API gains functionality and nothing breaks.

**VER-8** From a version of `1.0.0` or higher, MINOR MUST be incremented when any part of the public API is marked deprecated.

**VER-9** From a version of `1.0.0` or higher, PATCH MUST be incremented when shipped behaviour changes and the public API does not.

**VER-10** When more than one of VER-6 to VER-9 applies to a release, the highest MUST be taken.

**VER-11** A change that alters no shipped artifact and marks no part of the public API deprecated MUST NOT produce a release.

A shipped artifact is what a release publishes: the package, image or files a user installs. A deprecation produces a release even where it is marked only in documentation that ships with none of them, so that the MINOR release VER-22 counts on exists.

**VER-12** A dependency update MUST be classified by its effect on this repository's public API, not by the increment the dependency itself took.

A dependency going from 3.x to 4.x is not by itself a MAJOR here. It is MAJOR here only if this repository's own contract changes as a result.

**VER-31** A repository that publishes releases MUST state in each pull request which increment the change requires under VER-6 to VER-9 or VER-16.

This makes the pull request the record of the versioning decision. Without it the increment is chosen at release time, by whoever cuts the release, from a history they did not write.

| Change | Increment | From 2.4.7 |
|---|---|---|
| Breaking change to the public API | MAJOR | 3.0.0 |
| Backward compatible addition | MINOR | 2.5.0 |
| Deprecation marked | MINOR | 2.5.0 |
| Bug fix, no API change | PATCH | 2.4.8 |
| Internal refactor, observable behaviour unchanged | PATCH | 2.4.8 |
| Documentation, tests or CI only, marking nothing deprecated | none | 2.4.7 |

## Initial development

**VER-14** A repository MUST give its first release the version `0.1.0` while its public API is not stable.

**VER-15** A repository that runs in production, or that has any consumer outside its own repository, MUST publish releases at `1.0.0` or higher.

Under [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), `0.y.z` states that the public API is not stable, which software others already depend on cannot claim.

**VER-16** A release that stays below `1.0.0` MUST increment MINOR when it contains a breaking change, and PATCH when it contains none.

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) scopes its items on the increments to versions of `1.0.0` or higher. VER-6 to VER-9 narrow those items and keep their scope, so they and this rule never govern the same release.

## Pre-release and build metadata

**VER-17** A pre-release identifier MUST be `alpha`, `beta` or `rc`, followed by a dot and an integer counting from 1.

Correct: `2.0.0-rc.1`, `2.0.0-beta.3`
Incorrect: `2.0.0-rc1`, `2.0.0-test`, `2.0.0-final`

**VER-18** A released repository MUST NOT depend on a pre-release version of anything.

**VER-19** Build metadata MUST NOT be the only difference between two published artifacts.

Build metadata is ignored when versions are compared, as [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) specifies, so two artifacts that differ only there are indistinguishable to a consumer. If the content differs, the version differs.

## The version of record

**VER-3** A repository that publishes releases MUST hold the version of each unit it publishes in exactly one place.

**VER-4** The version of record MUST be the location its ecosystem defines:

| Ecosystem | Version of record |
|---|---|
| Node | `package.json`, [`version`](https://docs.npmjs.com/cli/v12/configuring-npm/package-json#version) |
| Python | `pyproject.toml`, [`[project] version`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#version) |
| Rust | `Cargo.toml`, [`[package] version`](https://doc.rust-lang.org/cargo/reference/manifest.html#the-version-field) |
| Go | the git tag, since Go has no manifest version and [maps each module version to a tag](https://go.dev/ref/mod#vcs-version) |
| Container image | the git tag, mirrored into the image tag |
| Anything else | the location its ecosystem defines, or a `VERSION` file at the repository root where it defines none |

Where a unit is built into a container image, the row of the ecosystem of its source applies; the Container image row applies to an image built from no such ecosystem.

**VER-5** Every other occurrence of the version MUST be derived from the version of record when the artifact is built.

A version written by hand in a second place is a version that will disagree with the first. Documentation, build arguments, generated headers and image tags all read from the one location.

**VER-32** A repository that publishes releases MUST gate merges on a check that fails when the version of record does not take the form of VER-28 or is not higher than the latest release tag of its unit.

**VER-44** Publication of a release MUST fail when its tag and the version of record disagree, or when a tag that is the version of record does not take the form of VER-28.

A release's tag exists only once its pull request is merged, so the merge gate checks what the pull request can already show, the form of the version and that it rises, where VER-31 records the increment; like every merge gate, it runs in CI (TL-10). Agreement between tag and version of record can be checked only once the tag exists, so it is checked where the release is published.

## Tags

**VER-28** A release tag MUST take the form `[<unit>/]v<major>.<minor>.<patch>[-<pre-release>]`: `<unit>/` only in a repository that publishes more than one unit, and `<pre-release>` as VER-17 requires.

Correct: `v2.1.0`, `v2.0.0-rc.1`, `billing-api/v2.1.0` in a repository publishing three services
Incorrect: `v2.0.0rc1`, `v2.0.0-RC1`, `v2.1.0` in a repository publishing three services

## Deprecation and removal

**VER-22** Public API MUST NOT be removed until it has been published as deprecated in at least one MINOR release of the current MAJOR line.

**VER-23** A deprecation MUST name the version in which removal is planned.

## Compatibility during rollout

**VER-42** A service deployed without downtime MUST, while it and its immediately preceding version both run, handle every request, message and stored record that the preceding version handles on each surface a client still uses.

**VER-43** A breaking change to the HTTP or event surface of a service MUST be delivered as a release that adds the new surface and marks the old one deprecated, then, once no client uses the old one, a release that removes it.

Two versions of a service are in production simultaneously during any rolling deployment. A contract change that assumes otherwise fails while the rollout is in progress, not afterwards.

## Supported lines

**VER-24** A repository MUST state which MAJOR lines it supports and until when.

Where a repository says nothing, only the current MAJOR line is supported.

**VER-27** A consumer MUST express a dependency as a range bounded above by the next MAJOR, or by the next MINOR where the range starts below `1.0.0`; an exact version is such a range.

Below `1.0.0` a MINOR release may break (VER-16), so the bound moves down one place there. An exact version admits no other release at all, so it is the narrowest range the rule allows.

Correct: `>=3.1.0 <4.0.0`, `>=0.3.1 <0.4.0`, `==0.16.6`
Incorrect: `>=3.1.0`, `*`, a bare `latest`, `>=0.3.1 <1.0.0`
