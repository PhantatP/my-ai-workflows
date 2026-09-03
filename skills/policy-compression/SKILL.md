---
name: policy-compression
description: Losslessly compress runtime policy, workflow, and procedure Markdown while preserving behavioral semantics. Use for machine-facing rules and prompts, not ordinary human notes unless explicitly requested.
---

# Policy compression

Reduce policy tokens without changing behavior. This is semantic compression,
not summarization or redesign.

## Scope

Use for frequently loaded workflow, instruction, procedure, adapter, or policy
Markdown. Do not apply to ordinary human notes, journals, knowledge notes, or
historical/experimental documents unless the user explicitly includes them.
Prioritize hot runtime policy; leave cold material alone unless it duplicates
active rules.

## Method

1. Identify the task's completion condition, policy files, canonical owner of
   each rule, and any local instructions. Measure baseline size and, when an
   available tokenizer permits, tokens.
2. Read dependent files enough to distinguish universal rules, domain behavior,
   platform capability, and history. Preserve canonical definitions; replace
   downstream repetition with the minimum accurate implication or reference.
3. Remove exact/near duplication first, then repeated explanations/examples,
   then simplify wording. Prefer compact lists and references over prose; do
   not add abstractions or redesign ownership.
4. Never remove or weaken behavioral invariants, exceptions, stop conditions,
   escalation/de-escalation, safety/approval boundaries, user control,
   correctness contracts, or routing-changing conditions. Keep a rule explicit
   when a reference would hide a required operational distinction.
5. For repository BUILD edits, follow applicable local workflow: inspect state,
   scan intended/actual changes, preserve mechanical floors, and verify the
   changed artifact. Do not claim unavailable enforcement or validation.
6. Inspect the final diff specifically for semantic drift: lost qualifiers,
   changed authority, altered defaults/overrides, missing preconditions, or
   weakened verification. Restore any rule whose shorter form is ambiguous.

## Report

State changed files, canonicalization and redundancies removed, deliberately
retained text whose compression could change behavior, before/after bytes and
tokens (or a clearly labeled proxy), validation evidence, diff-review result,
and unavailable checks or degraded assurance.
