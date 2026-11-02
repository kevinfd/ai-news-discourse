---
id: "44aa7212f206aee7"
title: "I asked Claude Code to break the tool that hides my secrets from Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xlvvbm/i_asked_claude_code_to_break_the_tool_that_hides"
link: "https://reddit.com/r/ClaudeAI/comments/1xlvvbm/i_asked_claude_code_to_break_the_tool_that_hides"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T12:29:09Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Relevant_Mousse_9117"]
language: "en"
summary: "My MCP server keeps tokens in the OS keychain so the agent never sees them. I told Claude Code: assume you're prompt-injected, you can write any file I can, get my secrets. Every finding needed a failing test before the fix. The one that stuck: the agent could simply edit the config the next session reads and switch a preset to auto-approve. A --confirm-auto flag doesn't help when the agent has…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 119
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlvvbm/i_asked_claude_code_to_break_the_tool_that_hides/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I asked Claude Code to break the tool that hides my secrets from Claude Code

Reddit · Relevant_Mousse_9117 · 2026-11-02

My MCP server keeps tokens in the OS keychain so the agent never sees them. I told Claude Code: assume you're prompt-injected, you can write any file I can, get my secrets. Every finding needed a failing test before the fix. The one that stuck: the agent could simply edit the config the next session reads and switch a preset to auto-approve. A --confirm-auto flag doesn't help when the agent has a shell. Lessons for anyone using agents: If permissions live in a file, check who can edit that file. A --yes flag is not human confirmation. Read what approval prompts actually show. Mine hid the host. If the agent can drive your screen, it can click your dialogs.
