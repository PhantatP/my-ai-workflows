# Information architecture

Markdown is the canonical portable representation for persistent workflow information. Storage remains human-readable, editable, vendor-independent, and usable without an AI system. The user retains ownership and can inspect, edit, move, or delete it without an AI system. Obsidian or a synchronized filesystem may be used, but correctness must not depend on Obsidian-specific behavior.

## V2.5 experimental lifecycle

Persistent information follows the bounded
[V2.5 Artifact Lifecycle and Provenance experiment](../experiments/v2.5-artifact-lifecycle.md).
Classify by artifact role and lifecycle, resolve its strongest context, follow
existing local conventions, preserve provenance and relationships, then choose
the appropriate write mode.

Artifact roles are `capture`, `working`, `source`, `reference`, `decision`, and
`knowledge`. Lifecycle classes are `ephemeral`, `living`, `snapshot`,
`immutable`, and `durable`. These dimensions do not replace BUILD, RESEARCH, or
LEARN correctness and do not map directly to domain folders.

Before writing persistent information:

1. Inspect library- and context-local rules.
2. Resolve project, area, reusable-resource, or uncertain ownership.
3. Check for an existing canonical artifact when the role is durable.
4. Choose `create`, `update`, `snapshot`, or `do not overwrite`.
5. Keep original sources distinguishable from synthesis and transformed
   representations linked to the same source identity.

Material claims intended to affect future reasoning, decisions, or durable
knowledge remain traceable to evidence. Assistant polish alone does not justify
promotion to knowledge.

Before rereading a large source, check whether a valid canonical representation
already answers the task and whether the source has changed. Apply the
[V2.5.1 context policy](context.md): retrieve metadata and canonical state
before relevant detail or original evidence.

## Placement and autonomy

Local conventions override generic placement. Prefer active project context,
then an ongoing Area, then a reusable Resource location; use Inbox when the
destination is genuinely unclear. Do not create new Projects, Areas, folder
taxonomies, metadata, or source records without demonstrated utility.

An Obsidian/PARA layout is one compatible implementation, not a Core contract:

```text
01 Inbox / 02 Projects / 03 Areas / 04 Resources / 05 Archive / 90 Assets
```

Agents may classify and place new artifacts, update an unambiguous canonical
living artifact, preserve sources, and deduplicate identical source identities.
They should ask or propose before materially moving, merging, deleting,
archiving, promoting, or restructuring existing human information when intent
is uncertain.

The repository supplies templates only; it must not create, populate, or claim
ownership of a user's vault without an explicit request.
