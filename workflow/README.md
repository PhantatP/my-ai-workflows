# My AI Workflows V2.2.1

This directory is the platform-neutral workflow core. `CLAUDE.md` and
`AGENTS.md` are small adapters that load the same policy in Claude Code and
Codex.

## Current scope

Only the BUILD core is implemented and considered stable enough for use:

- mechanically executed trigger scanning and policy floors;
- fail-closed guarding for destructive and production-sensitive commands;
- adaptive routing across Levels 0–4;
- counterargument checkpoint;
- runtime re-evaluation;
- append-only human-readable operational logging.

RESEARCH and LEARN are intentionally not operationalized yet. They remain
experiments until real use provides evidence for a more specific design.

## Layout

```text
workflow/
├── bin/                  # scanner, actual-diff rescan, and pre-action guard
├── enforcement/          # shared standard-library implementation
├── adapters/             # platform capability/limitation documentation
├── principles.md          # constitution shared by all adapters
├── routing/
│   ├── build.md           # operational BUILD procedure
│   └── triggers.yaml      # deterministic, inspectable trigger policy
├── agents/
│   └── roles.md           # V2.2 active role contracts and independence rules
├── future/                # deferred designs, not runtime workflow
└── skills.md              # V1 audit inventory and lifecycle rules
```

## Adoption

Copy `AGENTS.md`, `CLAUDE.md`, and `workflow/` into a target repository. A
target repository may override `routing/triggers.yaml` with project-specific
path patterns, but must preserve the distinction between mechanical evidence
and judgment risk. Scan intended paths before edits and run `scan-change-set`
once changes exist. Enforcement events are appended to `.workflow/log.txt`,
which is ignored by default; see `adapters/README.md` for platform limitations.
