# My AI Workflows — Codex adapter

This repository implements My AI Workflows V2.5 experimentally while retaining
the V2.3 general architecture. The platform-neutral policy lives in
[`workflow/`](workflow/README.md); this is the Codex entry point.

## Required reading order

1. [`workflow/core/principles.md`](workflow/core/principles.md)
2. [`workflow/core/architecture.md`](workflow/core/architecture.md)
3. [`workflow/core/routing.md`](workflow/core/routing.md)
4. [`workflow/core/assurance.md`](workflow/core/assurance.md)
5. The relevant profile under [`workflow/profiles/`](workflow/profiles/)
6. For BUILD, [`workflow/routing/triggers.yaml`](workflow/routing/triggers.yaml)
7. [`workflow/agents/roles.md`](workflow/agents/roles.md) before delegating.

## Main owns the task

The active agent is Main. It owns intent, domain segmentation, routing,
strategy, execution, integration, completion, and communication. Planning is a
phase, testing an activity, and debugging a methodology. Delegate only when
independence, context isolation, specialist capability, or separable work adds
identifiable value.

Classify complexity, risk, uncertainty, evidence requirement, and reversibility
independently. Assurance level, model capability, and agent count are separate.
Escalate model capability before agent count when the problem is reasoning
capacity; use an independent instance when independence itself is required.
Re-evaluate routing on new evidence and state degraded platform assurance
honestly.

Apply domain correctness: verify the artifact for BUILD, the evidence and
conclusion for RESEARCH, and the learner's independent use for LEARN. Assistant
operations move information and must not promote unreviewed material to trusted
Knowledge.

For persistent writes, apply the V2.5 Artifact Lifecycle policy in
[`workflow/core/information.md`](workflow/core/information.md): classify role
and lifecycle, resolve context, follow local conventions, check canonical
artifacts, choose create/update/snapshot behavior, and preserve provenance.

For LEARN, apply the experimental interaction strategy in the LEARN profile.
Keep simple questions direct, prefer one meaningful cognitive task per learner
turn when interaction helps, and keep workflow metadata internal unless the
user requests inspection or debugging. Do not generalize this experiment into
BUILD or RESEARCH interaction policy yet.

## Codex-specific execution

- Use a reviewer subagent for Level 3+ BUILD; give it intent, changed files or
  diff, relevant evidence, and a falsification-oriented assignment. It must not
  edit. Other domains require genuinely independent verification but do not
  automatically require an agent when another independent mechanism suffices.
- Follow [`.codex/README.md`](.codex/README.md) for Codex's session-level model
  and permission controls; role-level restrictions are delegation contracts.
- Use parallel workers only at Level 4 and only for independent, separable
  questions.
- `archive/v1/` contains Claude Code V1 inventory, retained for audit. It is
  not Codex configuration and does not create mandatory workflow stages.
- Use `workflow/bin/scan-triggers --platform codex` for intended BUILD paths
  and `workflow/bin/scan-change-set --platform codex` for the actual change
  set. Use `workflow/bin/enforce-operation --platform codex` before external
  sensitive commands;
  its deny decision is fail-closed. Report enforcement evidence in the final
  response; `.workflow/log.txt` is the minimal local operational log.

## Core coding constraints

- Inspect the relevant state and execution path before editing.
- Reproduce bugs and test the root-cause hypothesis before applying a fix.
- Keep changes within the requested scope and verify requested behavior with
  proportionate evidence.
