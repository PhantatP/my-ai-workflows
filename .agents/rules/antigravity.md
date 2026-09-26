---
trigger: always_on
description: My AI Workflows adapter for Antigravity; overrides the Codex-specific parts of AGENTS.md.
---

# My AI Workflows — Antigravity adapter

Follow `AGENTS.md` with these differences:

- You are Antigravity, not Codex. Pass `--platform antigravity` to
  `workflow/bin/scan-triggers`, `workflow/bin/scan-change-set`, and
  `workflow/bin/enforce-operation`, and ignore `.codex/README.md`.
- No hook runs the shared guard here, so call `enforce-operation` yourself
  before external sensitive commands; a denial is fail-closed.
- Capability limits and degraded assurance:
  `workflow/adapters/antigravity/README.md`.
