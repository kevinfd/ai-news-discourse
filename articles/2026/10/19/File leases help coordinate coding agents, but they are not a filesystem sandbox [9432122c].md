---
id: "9432122c6f8f8056"
title: "File leases help coordinate coding agents, but they are not a filesystem sandbox"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xa70lj/file_leases_help_coordinate_coding_agents_but"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xa70lj/file_leases_help_coordinate_coding_agents_but"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T19:48:25Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Historical_Dinner_69"]
language: "en"
summary: "When several developers use coding agents on one feature, assigning tasks is only part of the problem. Someone still has to decide which files each task owns and how the outputs fit together. I'm building Claude Share (session-share) around three separate pieces: shared tasks and contracts to describe the work, file leases to represent ownership, and a live board to show the coordination state.…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 209
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xa70lj/file_leases_help_coordinate_coding_agents_but/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# File leases help coordinate coding agents, but they are not a filesystem sandbox

Reddit · Historical_Dinner_69 · 2026-10-19

When several developers use coding agents on one feature, assigning tasks is only part of the problem. Someone still has to decide which files each task owns and how the outputs fit together. I'm building Claude Share (session-share) around three separate pieces: shared tasks and contracts to describe the work, file leases to represent ownership, and a live board to show the coordination state. Each developer uses their own Claude Code account and separate checkout. The enforcement boundary matters. The plugin's PreToolUse hook checks Edit, Write, MultiEdit and NotebookEdit against the participant's leases. That does not make it a filesystem sandbox. Other write paths are outside those checks, and the hook fails open if the coordination server errors or times out. The practical implication is that a lease helps agents coordinate; it does not prove two branches integrate correctly. Separate checkouts, review and integration testing still matter. A task can be complete on its own while the assembled feature is broken. I'm the creator, and Claude helped implement the project. The plugin/server are MIT licensed. The source is here if you want to inspect the boundary: https://github.com/cyber1443/session-share/blob/main/packages/plugin/src/hook.ts For people building multi-agent workflows, where do you put that boundary: advisory ownership, blocking tool hooks, or isolation below the tool layer?
