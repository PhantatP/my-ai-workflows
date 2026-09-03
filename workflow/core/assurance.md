# Assurance levels

Levels set confidence and process, not model tier, agent count, or response length.

- **L0 — Direct:** trivial, understood, low-risk work; act or answer.
- **L1 — Checked:** ordinary work; perform and sanity-check.
- **L2 — Structured:** plan/decompose, gather targeted evidence, execute, inspect.
- **L3 — Verified:** independently falsifiable evidence, then reconcile. The verifier must not merely repeat Main's account; mechanisms include independent review, alternative hypotheses, adversarial source search, tests, primary evidence, or learner transfer.
- **L4 — Assured:** rare critical or dependency-chain work; scope, checkpoint, stage, verify, checkpoint, then complete. May require multiple evidence types, review, approval, adversarial analysis, and rollback planning. Never create work to justify L4.

Adapters report `NORMAL` when required mechanisms were used, `DEGRADED` when the strongest fallback replaced an unavailable mechanism, or `BLOCKED` when required confidence cannot safely be obtained. `DEGRADED` is not enforcement; high-assurance work may require another platform.
