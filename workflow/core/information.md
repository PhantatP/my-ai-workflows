# Information architecture

Markdown is the canonical portable representation for persistent workflow information. Storage remains human-readable, editable, vendor-independent, and usable without an AI system. The user retains ownership and can inspect, edit, move, or delete it without an AI system. Obsidian or a synchronized filesystem may be used, but correctness must not depend on Obsidian-specific behavior.

## Information classes

| Class | Purpose | Trust posture |
| --- | --- | --- |
| Capture | Raw notes, links, clips, transcripts, and assistant discoveries | Cheap and unreviewed |
| Evidence | Sources, quotes, experiments, test output, and provenance | Supports or challenges conclusions |
| Working State | Active questions, decisions, mastery estimates, task packets, and handoffs | Mutable and human-readable |
| Knowledge | Durable explanations, verified conclusions, and reusable procedures | Curated for reuse |

Evidence remains distinguishable from conclusions. Assistant-generated material enters Capture or Working State unless a human or domain-appropriate verification process deliberately curates it into Knowledge.

## Lifecycle

`Capture → Evaluate → discard | preserve as Evidence | attach to Working State | curate into Knowledge`

Folder placement should primarily represent lifecycle or use. Metadata and links may express topics and domains. Keep metadata minimal; useful fields include `type`, `status`, `topics`, `domains`, `confidence`, `created`, and `updated`.

BUILD, RESEARCH, and LEARN reuse the same Knowledge layer. Do not duplicate a concept into separate domain knowledge stores.

## Initial vault convention

An adapter may use this initial convention:

```text
Vault/
├── 00 Inbox/Assistant, Web, Quick
├── 10 Knowledge/
├── 20 Learning/
├── 30 Research/
├── 40 Projects/
├── 50 Assistant/Task Packets, Handoffs, Learner State, Research State
└── 90 Archive/
```

Assistant flow is `capture or retrieve → optionally enrich → stage → organize
→ persist`. RESEARCH promotes supported stable conclusions through Evidence and
Working State into Knowledge. LEARN retrieves shared Knowledge, records learner
evidence in Working State, and updates mastery estimates only from demonstrated
performance.

The repository supplies templates only; it must not create, populate, or claim
ownership of a user's vault without an explicit request.
