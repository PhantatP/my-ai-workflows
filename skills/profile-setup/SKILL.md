---
name: profile-setup
description: Create or refresh the portable user profile (~/.myai/USER_PROFILE.md) through a short interview so every AI platform knows who the user is and what they are doing. Use when no profile exists and substantial work begins, or when the user asks to set up, review, or refresh their profile.
---

# Profile setup interview

The profile policy, location, and privacy exclusions are owned by
`workflow/core/information.md`; the structure by
`workflow/templates/user-profile.md`. This skill only runs the interview.

## Before asking

Draft from what is already known: the current conversation, global
instruction files, and platform-native memory. Ask the user to confirm or
correct a draft rather than answer from scratch. Never ask for private
identifiers or sensitive data.

## Rounds

Ask one round at a time, at most three short questions each, and stop for the
answer. Skip a round the draft already answers; stop early if the user wants.

1. Who you are: current role, study or work, fields of expertise, and what you
   are still learning.
2. What you are doing: active projects, near-term goals, and priorities.
3. How to work with you: language, tone, response format, how tasks should be
   handed to you, what to avoid, and constraints such as tools, platforms, or
   cost sensitivity.
4. Closed decisions: settled choices the AI should not reopen.

## Finish

Write `~/.myai/USER_PROFILE.md` from the template, leaving unanswered sections
empty and uncertain items under Unconfirmed. Show the Summary and ask for
corrections once. When refreshing, keep valid content and replace only what the
user changes.
