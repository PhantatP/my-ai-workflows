# My AI Workflows

Portable adaptive workflow configuration for Codex, Claude Code, Hermes,
Antigravity, and future execution surfaces. V2.5 adds a cross-domain artifact
lifecycle and provenance policy while retaining V2.4's LEARN interaction and
the V2.3 general architecture, separation of assurance from
model routing, portable Markdown information conventions, and deterministic
BUILD enforcement.

V2.5.1 adds experimental progressive context retrieval and policy compression;
see [`workflow/core/context.md`](workflow/core/context.md).

V2.5.2 adds an experimental portable user profile, project state, and
code-tools-first reading; see
[`workflow/core/information.md`](workflow/core/information.md). V2.4 and V2.5
were promoted from experimental on 2026-09-26.

## Contents

- `workflow/` — domain-neutral Core, three domain profiles, executable BUILD
  enforcement, platform adapters, information templates, roles, and skill audit.
- `CLAUDE.md` — thin Claude Code adapter for the shared policy.
- `AGENTS.md` — thin Codex adapter for the shared policy; Antigravity loads it
  with overrides in `.agents/rules/antigravity.md`.
- `HERMES.md` — thin Hermes adapter emphasizing information trust and honest
  capability degradation.
- `skills/` — active methodologies: adaptive routing, testing, independent
  falsification review, PLAN/GRILL interaction presets, and profile setup.

See [`workflow/README.md`](workflow/README.md) for adoption and current scope.

## Credits

- **CLAUDE.md** base structure inspired by [Andrej Karpathy](https://github.com/karpathy)'s public writing on working with coding agents.
- **post-mortem** and **scrutinize** skills — credit to [9arm](https://github.com/thananon).
- **[graphify](https://github.com/Graphify-Labs/graphify)** skill — knowledge graph generation for codebases/docs.
- **[superpowers](https://github.com/obra/superpowers)** — the skills framework (`using-superpowers`, brainstorming, systematic-debugging, TDD, etc.) this setup builds on top of.

Everything here has been adapted/customized for personal use.
