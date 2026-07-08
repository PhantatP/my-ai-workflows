# Global Rules

## 1. Think Before Coding
Don't assume. Don't hide confusion. Surface tradeoffs.

Before implementing:
- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.
- No "✅" emoji in code or responses — hard to see in dark theme.

## 2. Simplicity First
Minimum code that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.
- Ask: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes
Touch only what you must. Clean up only your own mess.

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.
- Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution
Define success criteria. Loop until verified.

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]

## 5. Model Selection
Use the right model for the task.

- **Opus** — orchestrator and planner roles only, and only by default for those two. Any other role: Opus only when the user explicitly asks. Never for implementation.
- **Sonnet** — default for implementation, editing, debugging, responses, orchestration, and planning.
- **Haiku** — lightweight subagent work.

(Per-agent model assignments live in each agent's frontmatter under `~/.claude/agents/` — don't restate them here.)

## 6. Orchestrator Owns Execution

For any multi-step task, **invoke the `orchestrator` agent first** — it is the entry point and the single source of truth for:
- the agent roster and what each agent does,
- coder/tester routing rules,
- the feature / bug / review-PR workflows (which agents run, in what order, what's parallel, how context is passed).

That detail lives in `~/.claude/agents/orchestrator.md` and the individual agent files — **not here**, so the two can't drift apart. Don't duplicate the roster or workflow tables in this file.

Principle that governs every flow: **skills govern HOW work is approached (process discipline); agents govern WHO executes it. When a skill applies to a step, invoke the skill BEFORE routing to an agent.**

## 7. Debugging: Breadcrumb Ledger

Always invoke `superpowers:systematic-debugging` before proposing any fix. The breadcrumb ledger below extends it — run both together.

During any multi-hypothesis debug session, maintain a running experiment log:
- Entry format: [what changed] → [what happened] → [what it ruled in/out]
- All new hypotheses must survive EVERY prior observation, not just the most recent one
- If a new hypothesis contradicts an earlier breadcrumb, investigate the contradiction — don't discard the breadcrumb

## graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.

## Knowledge Graph
If a `graphify-out/` folder exists in the project root, a knowledge graph has been built for this repo.
- `graphify-out/graph.json` — file relationships and architecture connections
- `graphify-out/GRAPH_REPORT.md` — god nodes, surprising connections, suggested questions

Check for it before exploring an unfamiliar codebase. If present, use `/graphify query "<question>"` to traverse it instead of reading files one by one.
