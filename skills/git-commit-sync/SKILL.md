---
name: git-commit-sync
description: Commit and push (sync) code changes using the project's convention — title only, no body, no co-authored line. Use this skill whenever the user says "commit", "push", "sync", "commit for me", "commit and push", or any variation. Never add bullet points, descriptions, or co-authored lines unless the user explicitly asks.
---

## Commit convention

- **Title only** — no body, no bullet list, no description paragraph
- **No co-authored line** — never append `Co-Authored-By`
- **Format**: `Tag: Short description`
- Keep the title under 72 characters

## Commit tags

| Tag | When to use |
|-----|-------------|
| `Feat:` | New feature or capability |
| `Fix:` | Bug fix |
| `Refactor:` | Code restructure, no behavior change |
| `Chore:` | Config, deps, tooling, cleanup |
| `Docs:` | Documentation only |

---

## Steps

### 1. Understand the changes

Run in parallel:
```bash
git status
git diff --stat
```

Infer the right tag and title from the diff — do not ask the user to describe it.

### 2. Group changes by concern

Before staging, check whether the modified files span more than one unrelated concern (e.g. a bug fix mixed with pre-existing unrelated feature work, or backend logic mixed with unrelated UI polish). Read the actual diffs, not just filenames — two files touched for the same reason belong together even if in different layers (backend + its test), while two changes in the same file for different reasons should be split.

- If everything traces to one concern, skip grouping — go straight to step 3 with one commit.
- If a single file mixes hunks from two different concerns, split it with a hand-crafted patch (`git diff <file> > /tmp/x.patch`, edit to keep only the relevant hunk, `git apply --cached /tmp/x.patch`) rather than committing it whole into one group.
- Don't over-split: group by "what it affects," not by individual file. A fix that touches 5 files for one reason is still one commit.
- If grouping is ambiguous, ask the user with one question showing the proposed groups rather than guessing.

### 3. Stage files

Stage only files relevant to this change/group. Prefer naming files explicitly over `git add .` to avoid accidentally including env files, generated outputs, etc.

If the user specified which files to include, use exactly those. Otherwise stage all modified tracked files shown in `git status` (per group, if grouped).

### 4. Commit — title only

```bash
git commit -m "Tag: Short description"
```

Single `-m` with the title. That's it.

**Never** append:
```
Co-Authored-By: ...
```

**Never** use a multiline message unless the user explicitly asks for detail.

Repeat steps 3-4 for each remaining group until `git status` is clean.

### 5. Push

```bash
git push
```

Report the branch and remote from the push output. If multiple commits were made, list each one.

---

## What NOT to do

- No commit body unless the user asks
- No `Co-Authored-By` lines, ever
- No `git add -A` or `git add .` without checking for sensitive files first
- No force-push unless explicitly requested
- No amending existing commits — always create a new one
