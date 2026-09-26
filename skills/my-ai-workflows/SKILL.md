---
name: my-ai-workflows
description: Route BUILD, RESEARCH, LEARN, and mixed tasks through My AI Workflows V2.5.2, including artifact lifecycle, adaptive LEARN interaction, and portable user context while preserving deterministic BUILD safeguards.
---

# My AI Workflows V2.5.2

Main owns intent, routing, integration, completion, and communication. Use the
least process, evidence, model capability, context, and coordination that can
achieve the required confidence.

## Route the task

1. Read `workflow/core/principles.md`, `workflow/core/routing.md`, and
   `workflow/core/assurance.md`.
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

For LEARN, read `workflow/profiles/learn/routing.md` and use its
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

For persistent information, read `workflow/core/information.md`. Classify the
artifact's role and lifecycle, resolve its strongest context, follow existing
local conventions, check for a canonical artifact, choose create, update,
snapshot, or no-overwrite behavior, and preserve source provenance. Do not
promote polished assistant output to knowledge automatically. Use Markdown Task
Packets for portable handoff. At session start, load the user profile Summary
and project state per `workflow/core/context.md`.

## Report

Include domains, initial and final levels, material model transitions,
mechanical floors and triggers, assurance degradation, evidence, verification,
independent review, changed artifacts, findings, and remaining uncertainty.
Do not log secrets or unnecessary raw user content.

