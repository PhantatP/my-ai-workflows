---
name: my-ai-workflows
description: Route BUILD, RESEARCH, LEARN, and mixed tasks through My AI Workflows V2.4, including experimental adaptive LEARN interaction while preserving deterministic BUILD safeguards.
---

# My AI Workflows V2.4 (experimental)

Main owns intent, routing, integration, completion, and communication. Use the
least process, evidence, model capability, context, and coordination that can
achieve the required confidence.

## Route the task

1. Read `workflow/core/principles.md`, `routing.md`, and `assurance.md`.
2. Segment the task into BUILD, RESEARCH, and LEARN; treat Assistant capture,
   retrieval, organization, and handoff as information logistics.
3. Assess complexity, risk, uncertainty, evidence requirement, and
   reversibility independently. Apply any mechanical floor.
4. Choose L0–L4, then choose execution strategy and model capability. Assurance,
   model tier, and agent count are separate decisions.
5. Before L0–L2 work, state a possible miss and observable escalation evidence.
6. Read and apply only the relevant profile under `workflow/profiles/`.
7. Re-evaluate routing whenever evidence changes. Report degraded platform
   assurance honestly.
8. Verify each domain by its own contract: artifact behavior for BUILD,
   evidence and conclusion for RESEARCH, and independent use for LEARN.

For LEARN, read `workflow/profiles/learn/routing.md` and use its experimental
interaction strategy. Keep simple questions direct; elicit, structure,
challenge, and adapt only when they improve learning. Keep workflow metadata
internal unless the user asks to inspect or debug it. The LEARN profile is the
policy source; do not duplicate it here or generalize it into BUILD or RESEARCH.

For BUILD, scan intended and actual paths with the executable trigger policy,
use the fail-closed guard before external sensitive commands, and never lower a
mechanical floor without an inspectable trigger-disproof event. L3+ BUILD uses
an independent read-only falsification reviewer.

For model routing, prefer the cheapest sufficiently capable model, account for
handoff cost, escalate capability before agent count when reasoning is the
constraint, and use an independent instance when independence is the need.

For persistent information, keep Capture, Evidence, Working State, and
Knowledge distinct. Assistant-generated material is not trusted Knowledge by
default. Use Markdown Task Packets for portable handoff.

During V2.4 Phase 4, record a concise entry in
`workflow/experiments/v2.4-phase4.md` when a genuine session naturally reaches
a meaningful outcome and the ledger is available. PLAN, GRILL, and `neither`
routes may qualify. Do not manufacture tasks, force presets, extend an
interaction, or interrupt the user's work merely to collect evidence. Preserve
only the minimum concrete excerpt or reference needed for attribution; if
recording would require unrelated permissions or add material friction, provide
the concise record for later capture instead.

## Report

Include domains, initial and final levels, material model transitions,
mechanical floors and triggers, assurance degradation, evidence, verification,
independent review, changed artifacts, findings, and remaining uncertainty.
Do not log secrets or unnecessary raw user content.

