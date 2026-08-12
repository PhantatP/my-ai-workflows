---
name: post-mortem
description: Write a canonical engineering record after a bug fix lands. Use after debugging is complete and fix is validated — not during investigation.
---

# Post-Mortem

The canonical engineering record of a bug fix. Written after the fix lands, for other engineers — and future you.

## Pre-conditions

**Refuse to proceed if any of these are missing. Say which is missing and stop.**

- [ ] A reliable, reproducible test case exists
- [ ] Root cause is definitively identified
- [ ] Fix has been implemented
- [ ] Fix has been validated against the original failure

If the bug is still open, use `superpowers:systematic-debugging` instead.

## When NOT to Use

- Bug is unresolved
- Customer-facing incident requiring a separate incident report
- Trivial single-line fix where the PR description covers it

## Output Structure

Write the post-mortem to `docs/post-mortems/YYYY-MM-DD-<slug>.md` in the active project. If no `docs/` directory exists, write to the project root.

---

### Summary

One paragraph. What the bug did to the user or system. What the fix does. No jargon — readable without deep context.

### Root Cause

The mechanism, not the symptom. Code identifiers are first-class: cite `file:line` for every relevant location.

- What was the incorrect behavior at the code level?
- What assumption was wrong?
- What invariant was violated?

### Fix

What changed and why it resolves the root cause (not just the symptom). Cite the changed `file:line`.

### Validation

What was run to confirm the fix. Be honest about scope — "tested the happy path only" is better than implying full coverage.

- Test cases run
- Manual verification steps
- Edge cases exercised (or explicitly not covered)

### Prevention

What would have caught this earlier. Pick the most actionable layer:

- **Test gap** — a specific test that didn't exist and should
- **Missing validation** — a guard that should have fired
- **Silent failure** — an error that was swallowed
- **Type gap** — a type that allowed an invalid state to be represented
- **Review gap** — something that should have been caught in code review

### What Slipped Through

Which layer failed to surface this: review, tests, types, runtime, documentation. One sentence per layer that failed.

---

## Tone Rules

- Blameless. Describe the gap, not the person.
- Technical and direct. Engineer-to-engineer.
- No hedging ("might", "could potentially"). State what happened.
- No flattery. Get to the finding.
