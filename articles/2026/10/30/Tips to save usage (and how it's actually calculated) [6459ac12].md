---
id: "6459ac123faeac9f"
title: "Tips to save usage (and how it's actually calculated)."
url: "https://reddit.com/r/ClaudeAI/comments/1xj6245/tips_to_save_usage_and_how_its_actually_calculated"
link: "https://reddit.com/r/ClaudeAI/comments/1xj6245/tips_to_save_usage_and_how_its_actually_calculated"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T04:35:29Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["aigisbot"]
language: "en"
summary: "**One month of Claude Pro: what worked for me** These are the results of my own testing. I don't run 100k line codebases, orchestration loops or subagents. My main model is Opus 5.5 medium. Sonnet feels too sloppy, and tbh it feels like it uses just as much usage. --- **1) Watch how many requests you make in a session** A request is a round trip between Claude Code and Anthropic's server. Each…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 356
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj6245/tips_to_save_usage_and_how_its_actually_calculated/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Tips to save usage (and how it's actually calculated).

Reddit · aigisbot · 2026-10-30

**One month of Claude Pro: what worked for me** These are the results of my own testing. I don't run 100k line codebases, orchestration loops or subagents. My main model is Opus 5.5 medium. Sonnet feels too sloppy, and tbh it feels like it uses just as much usage. --- **1) Watch how many requests you make in a session** A request is a round trip between Claude Code and Anthropic's server. Each round trip resends the entire conversation, and as context fills up the model gets worse and uses more tokens for the same work. My fix is a handover skill. It explains the model, our current state, what was approved, what was rejected, and what needs to be done now. I do the handover once a session passes 150k context. **2) Avoid compaction** It uses tokens, so I only do it when I really have to stay in that session. **3) Strip the context bloat** The plain Claude Code desktop app injects a lot of bloat. In my measurements it's around 54k for a simple "hi" on a fresh install. Claude wrote me a wrapper exe (some of it can't be turned off, so we had to force it) and now it's around 12.4k. That's still massive, but I get more work done within the same 150k context limit. **4) Small things that add up** - Bundle commands - Strip your CLAUDE.md - Strip bash noise - The expensive mistakes Claude makes for me are syntax errors in commands. So every time it makes one, I tell it to update the memory file so it doesn't repeat it. This saves a round trip. --- **The math on usage** Raw tokens are converted into weighted tokens, and that's what affects your usage. One output/thinking token on Opus 5.5 medium is as expensive as 50 cache read tokens. I ran a bunch of small tests against my own sessions. With all of the above I now get around 10 five-hour sessions per week. It would be 7 otherwise. You can ask Claude to analyze the transcripts of your own sessions. Thanks for reading, hope it helps.
