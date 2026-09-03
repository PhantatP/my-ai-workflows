# My AI Workflows V2.5 (experimental)

This directory contains the platform-neutral adaptive workflow. BUILD,
RESEARCH, and LEARN share a domain-neutral Core while defining different
correctness evidence. Model routing, execution-platform adapters, and portable
Markdown information conventions remain separate concerns.

V2.5 adds an experimental Artifact Lifecycle and Provenance policy for any
information intended to persist beyond an interaction. It classifies artifacts
by role and lifecycle, resolves context before placement, respects local
conventions, protects canonical artifacts, and preserves source provenance.
The full bounded policy and deferred validation protocol are in
[`experiments/v2.5-artifact-lifecycle.md`](experiments/v2.5-artifact-lifecycle.md).

V2.4's experimental interaction behavior remains inside the LEARN profile while
retaining the V2.3 general architecture. It does not yet introduce a
cross-domain Interaction Layer or new interaction routing machinery; promotion
into Core depends on evidence from later cross-domain experiments.

Phase 2 adds thin PLAN and GRILL skills to test the same interaction vocabulary
across existing domains. They remain optional presets outside Core and do not
define domains, assurance levels, model tiers, agent roles, or fixed state
machines.

Phase 3 closed after controlled cross-domain validation established acceptable
interaction behavior; its [record](experiments/v2.4-phase3.md) preserves the
original criteria and the explicit phase-boundary decision. Phase 4 now
evaluates value, friction, attribution, and generalization through genuine use
in its active [protocol and evidence ledger](experiments/v2.4-phase4.md).
Synthetic regressions do not count as Phase 4 evidence or justify Core
promotion.

BUILD retains the V2.2.1 deterministic trigger scanner and fail-closed shared
guard. RESEARCH remains intentionally minimal, and LEARN now carries a bounded
interaction experiment to be refined through real sessions rather than
elaborate agent orchestration.

## Layout

```text
workflow/
├── core/                 # architecture, routing, assurance, models, information
├── profiles/             # BUILD, RESEARCH, and LEARN correctness policies
├── adapters/             # capability declarations and platform mappings
├── templates/            # portable Task Packet and working-state Markdown
├── bin/                  # scanner, actual-diff rescan, and pre-action guard
├── enforcement/          # shared standard-library BUILD implementation
├── routing/              # BUILD trigger policy and compatibility entry point
├── agents/               # optional delegation contracts
├── experiments/          # bounded experimental protocols and working evidence
├── future/               # deferred inventory, not runtime workflow
└── skills.md             # skill lifecycle audit
```

## Adoption

Copy the adapter entry point for the target platform together with `workflow/`
and any active skills. A repository may override `routing/triggers.yaml` with
project-specific BUILD patterns while preserving the distinction between
mechanical evidence and judgment. Scan intended paths before edits and run
`scan-change-set` once changes exist. Operational events are appended to the
ignored `.workflow/log.txt`; adapter limitations remain explicit in
`adapters/capabilities.yaml`.
