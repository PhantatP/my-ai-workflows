# Skill lifecycle and V1 audit

A skill is a reusable procedure plus reasoning discipline. It remains active
only when it produces a useful behavioral effect relative to its discovery and
maintenance cost.

## Initial audit ledger

These are hypotheses for measurement, not final removals.

| Existing skill | Provisional lifecycle | V2.5 rationale |
| --- | --- | --- |
| `my-ai-workflows` | KEEP — V2.5 entry point | portable domain, assurance, model, and experimental artifact-lifecycle routing plus experimental LEARN interaction |
| `plan` | EXPERIMENT — Phase 4 validation | evaluate whether concise elicitation, structure, and assumption challenge materially improve genuine work |
| `grill-me` | EXPERIMENT — Phase 4 validation | evaluate whether adaptive one-question-at-a-time challenge materially improves genuine work |
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

PLAN and GRILL remain experimental until genuine evidence shows useful behavior
beyond LEARN at acceptable interaction cost. Promote their interaction
vocabulary into Core only when Phase 4 supports value, attribution, and
generalization without disproportionate overhead; otherwise keep the presets
local, change them, or remove them. Phase 3's closed behavior record is in
[`experiments/v2.4-phase3.md`](experiments/v2.4-phase3.md); active real-use
evidence belongs in
[`experiments/v2.4-phase4.md`](experiments/v2.4-phase4.md).

## Active skill placement

The KEEP skills are in the repository-root `skills/` directory for Claude Code
discovery. The rest remain in `archive/v1/skills/` until evidence justifies a
different lifecycle decision. Codex uses the same methodologies through the
shared routing policy and direct task instructions; its active skill mechanism
is platform-specific.
