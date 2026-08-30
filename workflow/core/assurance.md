# Assurance levels

Levels represent required confidence and process. They do not represent model tier, agent count, or response length.

## L0 — Direct

Use for trivial, well-understood, low-risk work: understand, then answer or act. No explicit verification ceremony is required.

## L1 — Checked

Default for ordinary work: understand, perform, then sanity-check. Main normally works alone.

## L2 — Structured

Use when complexity or uncertainty warrants deliberate structure: plan or decompose, explore or gather targeted evidence, execute, then inspect.

## L3 — Verified

Use when correctness requires evidence meaningfully independent from the original reasoning path. Suitable mechanisms include an independent reviewer, an alternative hypothesis, adversarial source search, automated tests, primary-source verification, or an independent learner transfer exercise. Execute, independently verify, then reconcile.

The verifier must be capable of falsifying the result and must not merely repeat Main's account.

## L4 — Assured

Reserve for critical consequences, accumulated uncertainty, or dependency chains requiring explicit checkpoints and multiple assurance mechanisms. Scope, checkpoint, execute a stage, verify, checkpoint again, and complete only after final assurance. L4 may require staged execution, multiple evidence types, independent review, human approval, adversarial analysis, and rollback planning.

L4 should remain rare. Never create work merely to justify it.

## Assurance state

Adapters report one of:

- `NORMAL`: required mechanisms were available and used;
- `DEGRADED`: a required mechanism was unavailable and the strongest honest fallback was used;
- `BLOCKED`: required confidence cannot be obtained safely on the current surface.

`DEGRADED` is not equivalent to enforcement. High-assurance work may move to a more capable platform.
