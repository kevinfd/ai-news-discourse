---
id: "6f8f79a2c5d9be8f"
title: "I made a Claude Code mod that draws a live map of what the agent is doing"
url: "https://reddit.com/r/ClaudeAI/comments/1xst2qe/i_made_a_claude_code_mod_that_draws_a_live_map_of"
link: "https://reddit.com/r/ClaudeAI/comments/1xst2qe/i_made_a_claude_code_mod_that_draws_a_live_map_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T17:31:57Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["alexeyw"]
language: "en"
summary: "I got tired of reading a scrolling list of tool calls, so I had Claude Code build a mod that shows the work as a map in a pane beside the chat. The agent sits in the centre, with ten stations around it: you, the model, memory, files, shell, network, browser, subagents, skills and hooks. Every model request, tool call and hook sends a pulse from the centre to its station and back, and errors turn…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 145
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xst2qe/i_made_a_claude_code_mod_that_draws_a_live_map_of/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Claude Code mod that draws a live map of what the agent is doing

Reddit · alexeyw · 2026-11-10

I got tired of reading a scrolling list of tool calls, so I had Claude Code build a mod that shows the work as a map in a pane beside the chat. The agent sits in the centre, with ten stations around it: you, the model, memory, files, shell, network, browser, subagents, skills and hooks. Every model request, tool call and hook sends a pulse from the centre to its station and back, and errors turn red. Spokes get thicker with use, a ring around the centre fills with the context window, and subagents circle their station while they run. It makes no network requests and shows names only, never content. Opus 5.5 wrote the first version, and Fable 5.2 reworked it the next day. Free, MIT: https://github.com/alexeyw/lot-map /plugin install lot-map --marketplace alexeyw/lot-map Tested on macOS only, so reports from Windows and Linux are welcome.
