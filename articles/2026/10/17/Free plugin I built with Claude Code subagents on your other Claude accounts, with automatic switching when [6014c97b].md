---
id: "6014c97bead53d05"
title: "Free plugin I built with Claude Code: subagents on your other Claude accounts, with automatic switching when one hits its limit"
url: "https://reddit.com/r/ClaudeAI/comments/1x7y05b/free_plugin_i_built_with_claude_code_subagents_on"
link: "https://reddit.com/r/ClaudeAI/comments/1x7y05b/free_plugin_i_built_with_claude_code_subagents_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T01:43:42Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Kynori20"]
language: "en"
summary: "I have more than one Claude account and got tired of setting up MCP servers and skills in every config folder, and of switching accounts by hand when one ran out. This links every account to one setup and lets your main session start subagents on the others. New work goes to the account with the most room in its 5-hour and weekly windows. A job that hits a limit continues on the next account…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["jobs & society", "models & research", "agents & coding"]
content_source: "post"
word_count: 185
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7y05b/free_plugin_i_built_with_claude_code_subagents_on/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Free plugin I built with Claude Code: subagents on your other Claude accounts, with automatic switching when one hits its limit

Reddit · Kynori20 · 2026-10-17

I have more than one Claude account and got tired of setting up MCP servers and skills in every config folder, and of switching accounts by hand when one ran out. This links every account to one setup and lets your main session start subagents on the others. New work goes to the account with the most room in its 5-hour and weekly windows. A job that hits a limit continues on the next account with its conversation intact. You can also send work to Codex or Gemini. Proxy tools do that by running Claude inside other harnesses and holding your Claude.ai token, which Anthropic's terms don't allow. Here each model runs in its own CLI and your login stays in the official claude binary. How Claude helped: I built it with Claude Code over a lot of sessions. Claude wrote most of the production code with me and ran all the tests. For live testing I used Gemini through Antigravity since it's cheap and fast: send a request, then check the job shows up inside Claude through the relay. Free and open source. https://github.com/lunati228/CLI-Subagents
