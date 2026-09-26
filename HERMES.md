# My AI Workflows — Hermes adapter

This repository implements My AI Workflows V2.5 experimentally while retaining
the V2.3 general architecture. The portable workflow lives in
[`workflow/`](workflow/README.md); this is the Hermes entry point.

## Required reading order

1. [`workflow/core/principles.md`](workflow/core/principles.md)
2. [`workflow/core/architecture.md`](workflow/core/architecture.md)
3. [`workflow/core/routing.md`](workflow/core/routing.md)
4. [`workflow/core/assurance.md`](workflow/core/assurance.md)
5. The relevant [`workflow/profiles/`](workflow/profiles/README.md)
6. [`workflow/adapters/hermes/README.md`](workflow/adapters/hermes/README.md)

Main retains task ownership. Treat Assistant capture, retrieval, organization,
preparation, and dispatch as information logistics rather than a fourth domain.
For persistent writes, classify artifact role and lifecycle, resolve context,
respect local conventions and canonical artifacts, and preserve provenance.
Route uncertain captures to Inbox and do not promote assistant-generated
content into trusted Knowledge automatically. At session start, load the user
profile Summary and project state per
[`workflow/core/context.md`](workflow/core/context.md).

Use a Markdown Task Packet when handing serious work to Codex, Claude Code, or
another surface. State unsupported capabilities and degraded assurance
explicitly. Do not claim hooks, command blocking, subagents, model switching,
or persistent memory unless the active Hermes environment demonstrates them.

Hermes is not permanently limited to lightweight work. Expand into BUILD,
serious RESEARCH, or structured LEARN work when demonstrated platform
capabilities and real use justify it. For BUILD, use deterministic trigger and
command enforcement only if the active environment can actually invoke the
shared tools; otherwise hand off or report degraded assurance.

For LEARN, apply the experimental interaction strategy in the LEARN profile,
respect explicit interaction preferences, and keep workflow metadata internal
by default. This behavior has not been promoted into cross-domain Core policy.
