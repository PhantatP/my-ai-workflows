# BUILD profile

## Objective and correctness contract

Produce a correct artifact or system change.

```text
artifact correctness
+ runtime or test evidence
+ actual-change inspection
+ risk controls
```

Useful evidence includes static inspection, tests, runtime behavior, change-set review, environment validation, independent review, and user approval for irreversible actions.

## Flow

```text
Understand
→ inspect relevant state and execution path
→ scan intended paths
→ change
→ inspect and scan the actual result
→ verify behavior
→ re-evaluate risk
→ complete
```

For bugs, reproduce the failure and test the root-cause hypothesis before patching. Keep changes within requested scope and do not claim more than the verification exercised.

## Mechanical BUILD policy

The canonical policy remains [`../../routing/triggers.yaml`](../../routing/triggers.yaml), implemented by `workflow/enforcement/` and `workflow/bin/`.

1. Scan intended paths before editing and the actual change set after editing.
2. Record every trigger, detector, evidence reference, and resulting mechanical floor.
3. A trigger applies only when a path enters the intended or actual change set, or when a matching command is proposed. Exploration alone is not a path trigger.
4. A new match automatically raises the minimum assurance level.
5. Removing a mechanical floor requires an append-only trigger-disproof event containing the trigger, detector, evidence reference, evidence summary, and `disproved: true`.
6. Use `workflow/bin/enforce-operation` before external sensitive commands. A deny decision is fail-closed and cannot be self-approved by Main.

Authentication, authorization, secrets, schemas, migrations, dependencies, public interfaces, infrastructure, destructive operations, unexpected scope, and failed assumptions are escalation signals.

## BUILD levels

- L0: direct answer or negligible non-behavioral change.
- L1: inspect, implement, verify.
- L2: explore or plan, implement, verify.
- L3: L2 discipline plus independent falsification review and relevant tests or other evidence.
- L4: staged high-consequence work with checkpoints and multiple assurance mechanisms; parallel investigation only for independent, separable questions.

Before L0–L2 execution and before de-escalation, apply the Core counterargument checkpoint. Complexity-driven de-escalation needs inspectable evidence and an audit event. It cannot lower a mechanical floor.

## Report

Report initial and final level, mechanical floor and triggers, escalation/de-escalation or disproof events, independent-review requirement and completion, verification evidence, files changed, judgment risks, findings, assurance state, and remaining uncertainty.
