# Skill lifecycle and V1 audit

A skill is a reusable procedure plus reasoning discipline. It remains active
only when it produces a useful behavioral effect relative to its discovery and
maintenance cost.

## Initial audit ledger

These are hypotheses for measurement, not final removals.

| Existing skill | Provisional lifecycle | V2.2 rationale |
| --- | --- | --- |
| `my-ai-workflows` | KEEP — V2.2 core | portable BUILD routing methodology |
| `test-backend`, `test-frontend` | KEEP — migrated | reusable verification methodology |
| `scrutinize` | KEEP — migrated | useful falsification-oriented review method |
| `lint-check` | ON-DEMAND | tool-specific verification, not global routing |
| `post-mortem` | ON-DEMAND | useful after meaningful incidents, not every bug |
| `graphify` | ON-DEMAND | expensive exploration aid for unfamiliar systems |
| `plan-as-html` | ON-DEMAND | presentation format, not planning policy |
| `git-commit-sync` | ON-DEMAND | narrow user-invoked operation |

No skill is automatically active solely because it exists. Future decisions
should use activation frequency, task category, behavioral effect, defects
found/prevented, context cost, and overlap.

## Active skill placement

The KEEP skills are in the repository-root `skills/` directory for Claude Code
discovery. The rest remain in `archive/v1/skills/` until evidence justifies a
different lifecycle decision. Codex uses the same methodologies through the
shared routing policy and direct task instructions; its active skill mechanism
is platform-specific.
