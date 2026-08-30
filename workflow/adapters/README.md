# Execution-platform adapters

Adapters map the portable Core, domain profiles, model classes, enforcement entry points, and Task Packets onto capabilities a platform actually provides. Platforms are execution surfaces, not workflow domains.

Capability values are:

- `ENFORCED`: the platform can mechanically guarantee the declared behavior in the stated scope;
- `SUPPORTED`: the platform exposes a reliable mechanism when invoked;
- `ADVISORY`: policy or a manual convention exists, but the platform cannot guarantee it;
- `UNAVAILABLE`: no validated mechanism is available.

See [`capabilities.yaml`](capabilities.yaml) for the current declaration and the platform notes for scope and limitations:

- [Codex](codex/README.md)
- [Claude Code](claude/README.md)
- [Hermes](hermes/README.md)

When a required capability is unavailable, state the limitation, use the strongest available fallback, and report assurance as `DEGRADED` or `BLOCKED`. Never describe an advisory fallback as enforcement.

The deterministic BUILD implementation remains in `workflow/enforcement/`.
Adapters invoke `workflow/bin/scan-triggers --platform <adapter>` before edits,
`workflow/bin/scan-change-set --platform <adapter>` after edits, and
`workflow/bin/enforce-operation --platform <adapter>` before an external
sensitive command where interception is possible.
