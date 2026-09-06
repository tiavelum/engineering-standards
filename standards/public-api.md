---
id: public-api
title: Public API
version: 1.0.0
status: active
applies_to: [all]
summary: What a repository publishes as its public API, and which changes to it are breaking.
---

# Public API

Prefix: `PA`

Semantic versioning is meaningless without a declared public API, because every increment under `versioning.md` is a statement about that API. This file defines what the API is and which changes to it break it.

## Declaration

**PA-1** A repository that publishes releases MUST declare its public API.

**PA-2** The declaration MUST name each surface that is public and each surface that is deliberately excluded.

**PA-3** A surface that the declaration does not mention MUST be treated as public.

The default is deliberately expensive. A repository that declares nothing has promised everything, including behaviour it never intended to guarantee. The way out is to declare.

**PA-4** An excluded surface MUST be marked where a consumer would encounter it, in the path, the symbol name, or the generated documentation.

Correct: an `internal/` package, a symbol prefixed `_`, an endpoint documented as experimental
Incorrect: an exclusion that exists only in the declaration, invisible to someone reading the code

## Surfaces

**PA-5** The declaration MUST cover every surface listed for the repository's type:

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

**PA-6** Each of the following MUST be treated as breaking:

- removing or renaming a public surface
- narrowing what an input accepts
- widening what an output may return
- making an optional input required
- changing a default in a way that alters existing behaviour
- changing the type, unit or meaning of a field
- adding a failure mode to an operation that previously could not fail
- dropping support for a runtime, platform or protocol version documented as supported
- a schema change that a reader at the previous version cannot read

**PA-7** The following MUST NOT be treated as breaking:

- adding an optional input, an endpoint, a command, a symbol or an optional field
- widening what an input accepts
- changing performance without changing the contract
- changing a surface marked excluded under PA-4

**PA-8** Where it is unclear whether a change is breaking, it MUST be treated as breaking.

The cost of an unnecessary MAJOR release is an inconvenience to the publisher. The cost of a missed one is an outage in someone else's system.

## Compatibility during rollout

**PA-9** A service deployed without downtime MUST remain compatible with the immediately preceding version for as long as both are running.

**PA-10** A breaking change to a live wire contract MUST be delivered as three releases: add the new surface, migrate consumers, remove the old surface.

Two versions of a service are in production simultaneously during any rolling deployment. A contract change that assumes otherwise fails while the rollout is in progress, not afterwards.
