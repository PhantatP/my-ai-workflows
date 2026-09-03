# Execution-platform adapters

Adapters map Core, profiles, model classes, enforcement entry points, and Task
Packets to platform capabilities; platforms are not domains. Capabilities are
`ENFORCED` (guaranteed in scope), `SUPPORTED` (reliable when invoked),
`ADVISORY` (not guaranteed), or `UNAVAILABLE` (no validated mechanism).

When required capability is unavailable, state the limit, use the strongest
fallback, and report `DEGRADED` or `BLOCKED`; never call advisory enforcement.
Where possible adapters run `scan-triggers` before edits, `scan-change-set`
after, and `enforce-operation` before external sensitive commands. Deterministic
BUILD implementation is `workflow/enforcement/`.
