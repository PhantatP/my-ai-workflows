# My AI Workflows V2.2

This directory is the platform-neutral workflow core. `CLAUDE.md` and
`AGENTS.md` are small adapters that load the same policy in Claude Code and
Codex.

## Current scope

Only the BUILD core is implemented and considered stable enough for use:

- mechanical guardrails and policy floors;
- adaptive routing across Levels 0–4;
- counterargument checkpoint;
- runtime re-evaluation;
- auditable routing telemetry.

RESEARCH and LEARN are intentionally not operationalized yet. They remain
experiments until real use provides evidence for a more specific design.

## Layout

```text
workflow/
├── principles.md          # constitution shared by all adapters
├── routing/
│   ├── build.md           # operational BUILD procedure
│   └── triggers.yaml      # deterministic, inspectable trigger policy
├── telemetry/
│   ├── schema.yaml        # record contract and mandatory events
│   └── template.yaml      # copyable record for opted-in projects
├── agents/
│   └── roles.md           # V2.2 active role contracts and independence rules
└── skills.md              # V1 audit inventory and lifecycle rules
```

## Adoption

Copy `AGENTS.md`, `CLAUDE.md`, and `workflow/` into a target repository. A
target repository may override `routing/triggers.yaml` with project-specific
path patterns, but must preserve the distinction between mechanical evidence
and judgment risk. Telemetry is ephemeral by default; create
`.workflow/telemetry/` in the target project to opt into repository-local YAML
records.

