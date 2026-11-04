---
id: "5f868b22181a2c14"
title: "I gave all my Claude Code sessions one shared memory: a folder of plain markdown notes"
url: "https://reddit.com/r/ClaudeAI/comments/1xn1527/i_gave_all_my_claude_code_sessions_one_shared"
link: "https://reddit.com/r/ClaudeAI/comments/1xn1527/i_gave_all_my_claude_code_sessions_one_shared"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T18:37:05Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Pleasant_Humor_1562"]
language: "en"
summary: "I'm a solo dev running a few dozen small apps. My biggest problem with agents was that every session started from zero. Same questions, same mistakes, rules I had already explained. So I built a simple shared memory. No vector DB, no plugin magic: One folder of markdown notes in git (327 notes now) index.md lists every note with a one-line hook One note per project, one per rule, plus a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 238
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn1527/i_gave_all_my_claude_code_sessions_one_shared/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave all my Claude Code sessions one shared memory: a folder of plain markdown notes

Reddit · Pleasant_Humor_1562 · 2026-11-03

I'm a solo dev running a few dozen small apps. My biggest problem with agents was that every session started from zero. Same questions, same mistakes, rules I had already explained. So I built a simple shared memory. No vector DB, no plugin magic: One folder of markdown notes in git (327 notes now) index.md lists every note with a one-line hook One note per project, one per rule, plus a history.md log per project My global CLAUDE.md says: read the index first, then the note for the project you're in. When we decide something lasting, write it down. What changed: New sessions know my rules before I type anything (e.g. "never install on my phone without asking", "one heavy build at a time, the Mac crashed once") Decisions survive. If we picked an approach last week, the next session finds it in history.md instead of re-arguing it Sub-agents get the same context because they read the same files What I learned: Keep notes short and dated. Stale rules hurt more than missing ones, so each note has a "verified" date and the index has a stale list on top Rules need a "why". Agents follow a rule much better when the note says what went wrong last time The index grows. Mine is ~45 KB now and I need to trim it Curious how others handle memory across sessions. Do you use CLAUDE.md only, or something bigger?
