# my-ai-workflows

Custom [Claude Code](https://claude.com/claude-code) configuration: subagents, skills, and global instructions.

## Contents

- `CLAUDE.md` — global instructions Claude Code loads in every project (model routing rules, coding philosophy, orchestrator entry point).
- `agents/` — custom subagent definitions (orchestrator, planners, coders, testers, reviewers, debuggers, data agents).
- `skills/` — custom skills invoked via `/skill-name` or auto-triggered by task context.

## Credits

- **CLAUDE.md** base structure inspired by [Andrej Karpathy](https://github.com/karpathy)'s public writing on working with coding agents.
- **post-mortem** and **scrutinize** skills — credit to [9arm](https://github.com/thananon).
- **[graphify](https://github.com/Graphify-Labs/graphify)** skill — knowledge graph generation for codebases/docs.
- **[superpowers](https://github.com/obra/superpowers)** — the skills framework (`using-superpowers`, brainstorming, systematic-debugging, TDD, etc.) this setup builds on top of.

Everything here has been adapted/customized for personal use.
