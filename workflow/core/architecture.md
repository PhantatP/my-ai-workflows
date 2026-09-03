# Conceptual architecture

The workflow keeps five concerns separable:

1. **Core Router** decides how much process and assurance the task requires.
2. **Domain Profile** defines correctness for BUILD, RESEARCH, or LEARN.
3. **Execution Strategy** selects direct work, exploration, staging, tools, delegation, verification, or approval.
4. **Model Router** selects the cheapest sufficiently capable model for the current operation.
5. **Adapter** maps the workflow onto capabilities an execution platform actually provides.

The Assistant layer sits around the router to capture, retrieve, organize,
prepare, dispatch, remind, and hand off information. It does not define a
fourth correctness objective. The Information layer supplies the experimental
cross-domain artifact roles, lifecycles, and provenance rules to every domain
and platform.

A mixed task may route its segments independently, for example RESEARCH L2,
LEARN L1, then BUILD L3. The highest level does not impose identical process on
every segment; Main preserves coherence across them.
