# Information architecture

Markdown is portable, human-readable, vendor-independent persistent storage;
users may inspect, edit, move, or delete it without AI. Obsidian/sync may be
used but are not correctness dependencies.

Apply the bounded [Artifact Lifecycle and Provenance experiment](../experiments/v2.5-artifact-lifecycle.md): classify roles (`capture`, `working`, `source`, `reference`, `decision`, `knowledge`) and lifecycles (`ephemeral`, `living`, `snapshot`, `immutable`, `durable`); resolve strongest context; follow local conventions; preserve provenance/relationships; choose write mode. These dimensions neither replace domains nor map to domain folders.

Before persistent writes: inspect local rules; resolve project, area, reusable
resource, or uncertainty; for durable roles check canonical artifact; choose
`create`, `update`, `snapshot`, or `do not overwrite`; distinguish originals
from synthesis/transformations sharing source identity. Material future claims
must trace to evidence; polish alone never promotes Knowledge. Before rereading
large sources, check canonical representation and change state; retrieve
metadata/canonical state before detail/evidence under [context.md](context.md).

Local placement wins: project, then Area, then reusable Resource, else Inbox.
Do not create projects, areas, taxonomy, metadata, or source records without
utility. Agents may place new artifacts, update an unambiguous canonical living
artifact, preserve sources, and deduplicate identical identities; ask/propose
before uncertain material move, merge, delete, archive, promote, or restructure
human information. Templates do not authorize populating or owning a user vault.
