# My AI Workflows

Portable adaptive workflow configuration for Codex, Claude Code, Hermes, and
future execution surfaces. V2.3 makes BUILD, RESEARCH, and LEARN first-class,
separates assurance from model routing, and defines portable Markdown
information and handoff conventions while preserving deterministic BUILD
enforcement.

## Contents

- `workflow/` — domain-neutral Core, three domain profiles, executable BUILD
  enforcement, platform adapters, information templates, roles, and skill audit.
- `CLAUDE.md` — thin Claude Code adapter for the shared policy.
- `AGENTS.md` — thin Codex adapter for the shared policy.
- `HERMES.md` — thin Hermes adapter emphasizing information trust and honest
  capability degradation.
- `skills/` — active V2.3 methodologies: adaptive routing, testing, and
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
