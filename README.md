# My AI Workflows

Portable adaptive workflow configuration for Codex, Claude Code, Hermes,
Antigravity, and future execution surfaces. V2.5 adds an experimental cross-domain artifact
lifecycle and provenance policy while retaining V2.4's LEARN interaction and
the V2.3 general architecture, separation of assurance from
model routing, portable Markdown information conventions, and deterministic
BUILD enforcement.

V2.5.1 adds experimental progressive context retrieval and policy compression;
see [`workflow/core/context.md`](workflow/core/context.md).

## Contents

- `workflow/` — domain-neutral Core, three domain profiles, executable BUILD
  enforcement, platform adapters, information templates, roles, and skill audit.
- `CLAUDE.md` — thin Claude Code adapter for the shared policy.
- `AGENTS.md` — thin Codex adapter for the shared policy; Antigravity loads it
  with overrides in `.agents/rules/antigravity.md`.
- `HERMES.md` — thin Hermes adapter emphasizing information trust and honest
  capability degradation.
- `skills/` — active V2.5 methodologies: adaptive routing, testing,
  independent falsification review, and experimental PLAN/GRILL interaction
  presets.

See [`workflow/README.md`](workflow/README.md) for adoption and current scope.

## Credits

- **CLAUDE.md** base structure inspired by [Andrej Karpathy](https://github.com/karpathy)'s public writing on working with coding agents.
- **post-mortem** and **scrutinize** skills — credit to [9arm](https://github.com/thananon).
- **[graphify](https://github.com/Graphify-Labs/graphify)** skill — knowledge graph generation for codebases/docs.
- **[superpowers](https://github.com/obra/superpowers)** — the skills framework (`using-superpowers`, brainstorming, systematic-debugging, TDD, etc.) this setup builds on top of.

Everything here has been adapted/customized for personal use.
