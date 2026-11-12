---
id: "62b6ee326c9f0b01"
title: "PSA: Claude Code now automatically syncs claude.ai web skills and plugins to local machines (enabled by default)"
url: "https://reddit.com/r/ClaudeAI/comments/1xtrrxf/psa_claude_code_now_automatically_syncs_claudeai"
link: "https://reddit.com/r/ClaudeAI/comments/1xtrrxf/psa_claude_code_now_automatically_syncs_claudeai"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T19:52:29Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Dizzy_Log2916"]
language: "en"
summary: "As a developer, I intentionally maintain separate configurations for Claude's web chat, which I use primarily for personal purposes, and my local CLI development environment. Today, I discovered that Claude Code had automatically synced nearly 700 skill and plugin files from my claude.ai account to my development server, creating two new directories: ~/.claude/skills/synced/ and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 177
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtrrxf/psa_claude_code_now_automatically_syncs_claudeai/"
score: null
comments: null
community: "r/ClaudeAI"
---

# PSA: Claude Code now automatically syncs claude.ai web skills and plugins to local machines (enabled by default)

Reddit · Dizzy_Log2916 · 2026-11-11

As a developer, I intentionally maintain separate configurations for Claude's web chat, which I use primarily for personal purposes, and my local CLI development environment. Today, I discovered that Claude Code had automatically synced nearly 700 skill and plugin files from my claude.ai account to my development server, creating two new directories: ~/.claude/skills/synced/ and ~/.claude/plugins/synced/ , adding nearly 10,000 tokens to the start of every session. The feature is controlled by a server-side flag ( tengu_claudeai_skills_sync_enabled ). Although introduced in September, Anthropic stealthily enabled it on my machine just a few days ago. I would argue that automatically mixing consumer web chat configurations with local development environments without prior notice is questionable. More importantly, although I understand that some server-side control comes with using Anthropic's products, there's a difference between remotely managing a service and silently modifying a developer's local environment, potentially resulting in hours of unnecessary debugging. For anyone else affected who wants to disable automatic syncing, you can add the following settings to your settings.json : { "syncClaudeAiSkills": false, "syncClaudeAiPlugins": false } Docs: https://code.claude.com/docs/en/settings-reference#syncclaudeaiskills https://code.claude.com/docs/en/settings-reference#syncclaudeaiplugins
