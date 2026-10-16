---
id: "090c46eee4c1f94a"
title: "Stop making your Claude Code sessions message each other: use git notes as a shared timeline"
url: "https://reddit.com/r/ClaudeAI/comments/1x7bbxb/stop_making_your_claude_code_sessions_message"
link: "https://reddit.com/r/ClaudeAI/comments/1x7bbxb/stop_making_your_claude_code_sessions_message"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T09:08:50Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Commercial_Base488"]
language: "en"
summary: "I run several Claude Code sessions in parallel, one per project plus a couple of \"reviewer\" sessions. They kept sending each other status messages like \"done X, your turn\". Every message cost tokens on both ends, some arrived late, and some were duplicates. The fix: every session writes what it did as a git note and reads everyone else's notes when it starts. Notes go on a separate ref, so they…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["business & funding"]
content_source: "post"
word_count: 406
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7bbxb/stop_making_your_claude_code_sessions_message/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Stop making your Claude Code sessions message each other: use git notes as a shared timeline

Reddit · Commercial_Base488 · 2026-10-16

I run several Claude Code sessions in parallel, one per project plus a couple of "reviewer" sessions. They kept sending each other status messages like "done X, your turn". Every message cost tokens on both ends, some arrived late, and some were duplicates. The fix: every session writes what it did as a git note and reads everyone else's notes when it starts. Notes go on a separate ref, so they never create commits, never touch your history, and never get squashed away. 1. Write (any session, after finishing something others should know): git notes --ref=timeline append -m "2026-10-16 15:30 [docs-room] finished chapter 3 fixes; build room is next" HEAD 2. Make notes show up in git log (once per repo): git config notes.displayRef refs/notes/timeline 3. Read on startup. A SessionStart hook in ~/.claude/settings.json runs a small script. It walks all my repos, merges commits and notes into one time-sorted list for the last day, and prints the last 20 lines. Hook output is injected into context, so every new or compacted session starts already knowing what the others did: "hooks": { "SessionStart": [{ "hooks": [{ "type": "command", "command": "python ~/.claude/hooks/session_timeline.py" }] }] } The script is about 40 lines. It runs git log --branches --tags --format=... plus git notes --ref=timeline list per repo and sorts the results by time. Use --branches --tags , not --all , or the notes ref's own "Notes added by…" commits show up as noise. 4. A rule in CLAUDE.md: Before starting work, check the timeline for overlap. Leave a note when you finish or hand off. Send a direct message only when the other session must act now (a review request or a handoff), and keep it to one line pointing at the commit or note. What changed for me Status pings between sessions mostly disappeared. The only messages left are real requests. A reviewer session can check for duplicate work by reading commits and notes, with no message history needed. It survives compaction and restarts, because the timeline lives in git, not in any session's context. Zero extra infrastructure: no server, no database, no MCP. Caveats Notes don't push by default. Add git push origin refs/notes/* if you sync through a remote. Mine sync by folder, so I skip that step. Keep the startup output short (I use 20 lines). Otherwise you pay tokens on every session start. Curious whether anyone has a better way to coordinate parallel sessions.
