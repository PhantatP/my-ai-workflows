# Information architecture

Markdown is portable, human-readable, vendor-independent persistent storage;
users may inspect, edit, move, or delete it without AI. Obsidian/sync may be
used but are not correctness dependencies.

Apply the [Artifact Lifecycle and Provenance policy](../experiments/v2.5-artifact-lifecycle.md): classify roles (`capture`, `working`, `source`, `reference`, `decision`, `knowledge`) and lifecycles (`ephemeral`, `living`, `snapshot`, `immutable`, `durable`); resolve strongest context; follow local conventions; preserve provenance/relationships; choose write mode. These dimensions neither replace domains nor map to domain folders.

Before persistent writes: inspect local rules; resolve project, area, reusable
resource, or uncertainty; for durable roles check canonical artifact; choose
`create`, `update`, `snapshot`, or `do not overwrite`; distinguish originals
from synthesis/transformations sharing source identity. Material future claims
must trace to evidence; polish alone never promotes Knowledge. Before rereading
large sources, check canonical representation and change state; retrieve
metadata/canonical state before detail/evidence under [context.md](context.md).

The user profile (`~/.ai/USER_PROFILE.md`, living `reference` outside any
repository, from the [template](../templates/user-profile.md)) records who the
user is and what they are doing: background, expertise, current work, goals,
stated working preferences, constraints, and closed decisions. Agents update it
without asking when a prompt reveals new durable, useful information, replace
superseded facts rather than accumulate them, and name the change in their
reply. Never record private identifiers or sensitive data (national, passport,
or student IDs; addresses; phone numbers; account, card, or financial details;
credentials; health), third parties' private information, or inferred
personality, psychology, or health.

Project state (`<project>/.ai/STATE.md`, living `working` artifact, from the
[template](../templates/project-state.md)) records objective, where work left
off, next actions, and open and closed decisions; update it after milestones,
decisions, and substantial sessions, holding only what code, docs, and history
do not show. Follow local rules on committing it. Platform-native memory keeps
only platform-specific behavior; facts about the user or project go in these
portable files.

Local placement wins: project, then Area, then reusable Resource, else Inbox.
Do not create projects, areas, taxonomy, metadata, or source records without
utility. Agents may place new artifacts, update an unambiguous canonical living
artifact, preserve sources, and deduplicate identical identities; ask/propose
before uncertain material move, merge, delete, archive, promote, or restructure
human information. Templates do not authorize populating or owning a user vault.
