# My AI Workflows V2.3

This directory contains the platform-neutral adaptive workflow. BUILD,
RESEARCH, and LEARN share a domain-neutral Core while defining different
correctness evidence. Model routing, execution-platform adapters, and portable
Markdown information conventions remain separate concerns.

BUILD retains the V2.2.1 deterministic trigger scanner and fail-closed shared
guard. RESEARCH and LEARN are intentionally minimal profiles to be refined from
real use rather than elaborate agent orchestration.

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
