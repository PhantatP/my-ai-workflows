# BUILD profile

## Correctness

Deliver a correct artifact or system change: artifact correctness, runtime/test
evidence, actual-change inspection, and risk controls. Relevant evidence
includes inspection, tests, runtime behavior, environment validation,
independent review, and approval for irreversible actions.

## Procedure

Inspect relevant state and execution path; scan intended paths; change; inspect
and scan actual changes; verify behavior; re-evaluate risk. Apply [Core
context](../../core/context.md) progressively. For bugs, reproduce failure and
test the root-cause hypothesis before patching. Stay in scope and claim only
what verification exercised.

## Mechanical policy

[`../../routing/triggers.yaml`](../../routing/triggers.yaml), implemented by
`workflow/enforcement/` and `workflow/bin/`, is canonical.

1. Scan intended paths before edits and actual changes after; record triggers, detector, evidence reference, and floor.
2. A path trigger applies only when its path enters intended/actual changes; a command trigger applies when proposed. Exploration alone is not a path trigger. A new match raises the minimum level.
3. Remove a floor only with an append-only trigger-disproof event containing trigger, detector, evidence reference and summary, and `disproved: true`.
4. Run `enforce-operation` before external sensitive commands. Denial is fail-closed and Main cannot self-approve it.

Authentication/authorization, secrets, schemas/migrations, dependencies, public
interfaces, infrastructure, destructive operations, unexpected scope, and
failed assumptions escalate. Levels add: L0 negligible non-behavioral/direct;
L1 inspect/implement/verify; L2 explore or plan/implement/verify; L3 L2 plus
independent read-only falsification review and relevant evidence; L4 staged
checkpoints and multiple mechanisms. L4 parallel work is only for separable,
independent questions. Before L0–L2 work and de-escalation, use the Core
counterargument checkpoint; complexity de-escalation needs inspectable evidence
and an audit event and never lowers a mechanical floor.

Report levels, floors/triggers, escalation/de-escalation/disproof, required and
completed review, verification, changed files, risks/findings, assurance, and
uncertainty.
