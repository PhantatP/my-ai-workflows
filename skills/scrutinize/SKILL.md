---
name: scrutinize
description: Deep pre-merge review. Checks whether a change should exist and actually does what it claims, end-to-end. Use before any PR merge. Complements code-review (quality/conventions) — this one verifies correctness and necessity.
---

# Scrutinize

Stand outside the change and ask whether it should exist at all, then verify it actually does what it claims end-to-end.

**Distinct from `/review`:** `review` checks quality and conventions. `scrutinize` checks necessity and end-to-end correctness. Run scrutinize before merging anything non-trivial.

## Operating Stance

- **Outsider.** Forget who wrote it and why they think it's right. Read the artifact cold.
- **End-to-end, not diff-local.** The diff is the entry point, not the scope. Follow the call graph through real code paths.
- **Actionable, concise, with evidence.** Every finding states *what to change*, *why it matters*, and *what evidence* led you there. No filler.

## Four Steps — Run in Order, No Skipping

### 1. Intent

State the goal in one sentence, in your own words.

If you cannot state it clearly, the artifact is underspecified — say so and stop. Do not proceed to step 2.

### 2. Simpler-Alternative Pass (mandatory — never skip)

Before any line-by-line review, spend one pass asking: **is there a better way to achieve this goal?**

Consider:
- **Doing nothing** — is the problem real and load-bearing?
- **Using something that already exists** — is there an existing function, pattern, or config that covers this?
- **A smaller change** — does 90% of the goal at 10% of the risk/complexity?
- **A different layer** — config vs code, framework vs app, build vs runtime?

If a better alternative exists, name it explicitly with rationale. **This is the highest-value output of the review.** Surface it before the trace.

Skip only if the user explicitly says "don't question scope."

### 3. End-to-End Trace

For each behavior the change claims, trace the path through the **real code** — not just the diff lines:

- Entry point → call sites → branches taken → state mutated → exit / return / side effect
- Include the **unchanged code on either side** of the diff — bugs hide at seams
- For a plan or design doc: trace the proposed flow against the existing system; where does it touch reality?

**Note every surprise** — unexpected branch, dead code reached, state you didn't expect. Surprises are signal.

### 4. Report

One section per finding. Order by severity: blocker → major → nit.

For each finding:
- **Finding** — one sentence, specific. Cite `file:line` when applicable.
- **Why it matters** — the consequence, not the principle.
- **Evidence** — the trace step or input that exposes it.
- **Suggested change** — concrete and minimal.

Close with a one-line verdict:

> `ship` / `fix-then-ship` / `rework` / `reject` — [single biggest reason]

---

## Operating Rules

- **Cite or it didn't happen.** Every claim about the code references a specific path, file, or line. No vague "this might break under load."
- **No rubber-stamps.** "LGTM" is not an output. If you genuinely find nothing, state what you traced so the user can judge coverage.
- **Distinguish claim from verification.** "The PR says X" and "I traced X and confirmed/refuted it" are different statements — keep them separate.
- **Lead with structural problems.** If step 1 or 2 surfaces a real issue, lead with it. Don't pad with nits when a blocker exists.
- **No flattery, no hedging.** State the finding directly.
