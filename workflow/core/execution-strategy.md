# Execution strategy

Choose mechanisms only after classifying the task and selecting assurance.
Available strategies include direct execution, a structured plan, targeted
exploration, evidence gathering, staged work, automated checks, independent
verification, rollback planning, and human approval.

Delegation is justified only by identifiable value:

- genuinely independent verification;
- context isolation;
- specialist capability;
- useful parallel exploration of separable questions;
- bounded execution suitable for a cheaper model.

Length, available agents, or a named role are not reasons by themselves.
Parallel execution is reserved for independent, non-overlapping work where its
coordination cost is lower than its benefit.

Irreversible or externally consequential actions require action-specific human
approval where supported. Approval must be external to the proposing model,
short-lived where appropriate, and logged without secrets. If the platform
cannot provide the required control, report `DEGRADED` or `BLOCKED` assurance.
