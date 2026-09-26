# Skill lifecycle and V1 audit

A skill is a reusable procedure plus reasoning discipline. It remains active
only when it produces a useful behavioral effect relative to its discovery and
maintenance cost.

## Initial audit ledger

These are hypotheses for measurement, not final removals.

| Existing skill | Provisional lifecycle | V2.5 rationale |
| --- | --- | --- |
| `my-ai-workflows` | KEEP — V2.5.2 entry point | portable domain, assurance, model, and artifact-lifecycle routing plus LEARN interaction |
| `plan` | KEEP — promoted 2026-09-26 | concise elicitation, structure, and assumption challenge for genuine planning work |
| `grill-me` | KEEP — promoted 2026-09-26 | adaptive one-question-at-a-time challenge for genuine work |
| `test-backend`, `test-frontend` | KEEP — migrated | reusable verification methodology |
| `scrutinize` | KEEP — migrated | useful falsification-oriented review method |
| `policy-compression` | KEEP — V2.5 | losslessly reduces hot policy context without changing behavioral semantics |
| `profile-setup` | EXPERIMENT — V2.5.2 | evaluate whether a short setup interview gives every platform enough user context to reduce repeated explanation |
| `lint-check` | ON-DEMAND | tool-specific verification, not global routing |
| `post-mortem` | ON-DEMAND | useful after meaningful incidents, not every bug |
| `graphify` | ON-DEMAND | expensive exploration aid for unfamiliar systems |
| `plan-as-html` | ON-DEMAND | presentation format, not planning policy |
| `git-commit-sync` | ON-DEMAND | narrow user-invoked operation |

No skill is automatically active solely because it exists. Future decisions
should use activation frequency, task category, behavioral effect, defects
found/prevented, context cost, and overlap.

PLAN and GRILL were promoted on 2026-09-26 by the user's judgment from real
use. They remain optional presets; their interaction vocabulary stays out of
Core. Phase 3's behavior record is in
[`experiments/v2.4-phase3.md`](experiments/v2.4-phase3.md) and the Phase 4
decision in [`experiments/v2.4-phase4.md`](experiments/v2.4-phase4.md).

## Active skill placement

The KEEP skills are in the repository-root `skills/` directory for Claude Code
discovery. Codex uses the same methodologies through the
shared routing policy and direct task instructions; its active skill mechanism
is platform-specific.
