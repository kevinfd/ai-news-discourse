---
id: "4cfd35e611cb82a2"
title: "I have put jev inside claude code's harness to reduce token maxing"
url: "https://reddit.com/r/ClaudeAI/comments/1x7zahd/i_have_put_jev_inside_claude_codes_harness_to"
link: "https://reddit.com/r/ClaudeAI/comments/1x7zahd/i_have_put_jev_inside_claude_codes_harness_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T02:51:45Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Fit-Fail-3369"]
language: "en"
summary: "I’ve been exploring Jev and looking at projects that built around claude code. It's always the question that whether it could help with some of the smaller decisions around coding work, especially if it was given the right context instead of the whole conversation. That led me to build optim-jev, a Claude Code plugin with three experimental tools: Context compaction: Jev checks older tool calls…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 280
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7zahd/i_have_put_jev_inside_claude_codes_harness_to/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I have put jev inside claude code's harness to reduce token maxing

Reddit · Fit-Fail-3369 · 2026-10-17

I’ve been exploring Jev and looking at projects that built around claude code. It's always the question that whether it could help with some of the smaller decisions around coding work, especially if it was given the right context instead of the whole conversation. That led me to build optim-jev, a Claude Code plugin with three experimental tools: Context compaction: Jev checks older tool calls and outputs, then keeps, truncates, or removes them while protecting recent messages. (This is a pre-step add-on to claude code's built-in compactor) Model + Effort routing: Jev helps choose between Haiku, Sonnet, and Opus using the task, relevant files, and project rules that can evolve over time. Skill selection: Jev picks a small set of relevant skills or none instead of sending the entire skill catalog with every request. Most of claude's work has gone into deciding what Jev should actually see as context. It also helped in strategizing how the context that goes into jev is capped to prevent decision quality degradation, with essential task information kept while lower-priority history is trimmed first. It was also able to set a caching mechanism where potential repeatable decisions are preserved. I also designed a performance comparison metrics using with claude's help to compare claude code's legacy workflow and optim-jev integrated claude code workflow. I’ve been brainstorming with opus to find an optimal experimental setup to benchmark these ideas properly: token usage, decision quality, cost, and how they behave alongside existing optimizations such as prompt caching. I do not have final conclusions yet, but the plugin is at a point where the experiments can be inspected and repeated. Repo is free to use with MIT Licsence: https://github.com/Oqura-ai/optim-jev
