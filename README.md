# My AI Workflows

Portable workflow configuration for [Claude Code](https://claude.com/claude-code)
and Codex. V2.2 implements the smallest BUILD core first: evidence-gated
mechanical guardrails, adaptive routing, counterargument, runtime escalation,
and auditable telemetry.

## Contents

- `workflow/` — platform-neutral V2.2 principles, BUILD routing, trigger policy,
  telemetry contract, roles, and skill audit.
- `CLAUDE.md` — thin Claude Code adapter for the shared policy.
- `AGENTS.md` — thin Codex adapter for the shared policy.
- `skills/` — active V2.2 methodologies: BUILD routing, testing, and
  independent falsification review.
- `archive/v1/` — remaining V1 inventory, clearly separate from the active
  workflow and pending audit.

See [`workflow/README.md`](workflow/README.md) for adoption and current scope.

## Credits

- **CLAUDE.md** base structure inspired by [Andrej Karpathy](https://github.com/karpathy)'s public writing on working with coding agents.
- **post-mortem** and **scrutinize** skills — credit to [9arm](https://github.com/thananon).
- **[graphify](https://github.com/Graphify-Labs/graphify)** skill — knowledge graph generation for codebases/docs.
- **[superpowers](https://github.com/obra/superpowers)** — the skills framework (`using-superpowers`, brainstorming, systematic-debugging, TDD, etc.) this setup builds on top of.

Everything here has been adapted/customized for personal use.
