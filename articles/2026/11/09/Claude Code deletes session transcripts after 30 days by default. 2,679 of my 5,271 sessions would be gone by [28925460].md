---
id: "289254603b0bac08"
title: "Claude Code deletes session transcripts after 30 days by default. 2,679 of my 5,271 sessions would be gone by now, so I built a dashboard that keeps them"
url: "https://reddit.com/r/ClaudeAI/comments/1xrt75c/claude_code_deletes_session_transcripts_after_30"
link: "https://reddit.com/r/ClaudeAI/comments/1xrt75c/claude_code_deletes_session_transcripts_after_30"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T14:33:54Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Nitjsefnie"]
language: "en"
summary: "the setting is cleanupPeriodDays in ~/.claude/settings.json, default 30, and old session JSONLs get deleted at startup. you can raise it, but I also wanted the numbers out of them, so I built claudit. free and open source (MIT), you host it yourself what it does: you sync your session JSONLs into a bucket (R2, or any local dir you keep as a file:// mirror) and claudit ingests from there, so a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "post"
word_count: 290
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrt75c/claude_code_deletes_session_transcripts_after_30/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code deletes session transcripts after 30 days by default. 2,679 of my 5,271 sessions would be gone by now, so I built a dashboard that keeps them

Reddit · Nitjsefnie · 2026-11-09

the setting is cleanupPeriodDays in ~/.claude/settings.json, default 30, and old session JSONLs get deleted at startup. you can raise it, but I also wanted the numbers out of them, so I built claudit. free and open source (MIT), you host it yourself what it does: you sync your session JSONLs into a bucket (R2, or any local dir you keep as a file:// mirror) and claudit ingests from there, so a prune never shrinks your history. then one page of numbers: cost by model, token breakdown, the 5m vs 1h cache write split, context growth per session, reply latency, tool error rate, an activity heatmap. it doesn't grade your sessions, reading them is on you one thing it showed me: 64.9% of my cache write tokens were the 1h kind, which bills at 2x input instead of 1.25x. price all cache writes at 1.25x and those come out 37.5% low how Claude helped: built with AI coding agents, mostly in Claude Code (Claude Opus, plus GLM-5.3-Flash and other models routed through it), some in Codex CLI. it goes issue by issue, one agent session per issue, review agents before anything merges, and every agent commit names its model in a co-author trailer. the parser's tricky parts came from reading Claude Code's own transcripts: one streamed reply gets logged several times under the same requestId, so it keeps the biggest one, and subagent files repeat records from the parent, so it dedups by uuid across files panels are ported from nhz-io/ccusage-plot , the heatmap, lines added/deleted and cost by context size are new here. FastAPI, Postgres, React with in-browser Babel, docker compose up boots it on sample data with no config live one to try, guest login is read-only: https://all.nitjsefni.eu https://github.com/Nitjsefnie/claudit
