# Context retrieval and policy compression

Persistent storage is not active context. Start from task objective, constraints,
output, candidate artifacts, and result-changing facts; retrieve progressively:
metadata → smallest canonical state → relevant detail → original/large evidence.
Use original sources only for verification, freshness, conflict, missing
provenance/detail, or high-consequence decisions. Keep objective, constraints,
decisions, open questions, canonical artifacts, evidence, and next action;
reuse valid unchanged summaries and stop when more context cannot change the
result, confidence, or verification. Correctness, safety, comprehensive
requests, and required evidence override reduction. If missing context causes
rework, expand and record the gap. Follow links/citations only for a
task-specific reason.

At session start, read the Summary of the user profile
(`~/.myai/USER_PROFILE.md`) and the project's `<project>/.myai/STATE.md` when they
exist; open other profile sections only when the task needs them. Closed
decisions stay closed unless a new material fact appears. With no profile,
offer the `profile-setup` interview before substantial work; if declined,
create the file with an empty Summary so later sessions do not ask again.
During work, keep project state current without being asked: create it when
missing and update it after each meaningful change, under
[information.md](information.md).

Prefer deterministic tools to model perception when they give an equal or
better result: extract a PDF's text layer (`pdftotext`, PyMuPDF) rather than
reading rendered pages, parse structured data with a parser or query tool, and
compute rather than estimate. Extract only the needed scope and keep reusable
extractions with source, locator, and tool as derived representations under
[information.md](information.md), so later sessions reuse rather than re-read.
Without a usable text layer, tell the user before OCR; approved OCR tries
Tesseract before model-based reading. Use model perception when layout,
figures, or visual meaning matter or tool output is inadequate.

Before durable writing, find canonical state then update, link, snapshot, or
create under [information.md](information.md); discard irrelevant context.

Each invariant has one owner: Core universal rules, profiles domain correctness,
skills invocation, adapters capability, experiments deltas/evidence, and local
rules local. Compress prose and duplication, never safety, exceptions,
escalation, user control, verification, or stop conditions. Do not load
unrelated profiles, experiments, skills, or adapters in routine work.
