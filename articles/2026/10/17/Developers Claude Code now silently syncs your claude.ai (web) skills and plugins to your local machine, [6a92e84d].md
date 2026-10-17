---
id: "6a92e84dbd1ad08e"
title: "Developers: Claude Code now silently syncs your claude.ai (web) skills and plugins to your local machine, enabled by default"
url: "https://reddit.com/r/ClaudeAI/comments/1x839jo/developers_claude_code_now_silently_syncs_your"
link: "https://reddit.com/r/ClaudeAI/comments/1x839jo/developers_claude_code_now_silently_syncs_your"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T06:41:54Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["phatstackzdevops"]
language: "en"
summary: "I'm a senior developer and I intentionally maintain separate configurations for Claude's web chat, which I use primarily for personal purposes, and my local CLI development environment. Today, I discovered that Claude Code had automatically synced nearly 700 skill and plugin files from my claude.ai account to my development server in two new directories, ~/.claude/skills/synced/ and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 275
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x839jo/developers_claude_code_now_silently_syncs_your/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Developers: Claude Code now silently syncs your claude.ai (web) skills and plugins to your local machine, enabled by default

Reddit · phatstackzdevops · 2026-10-17

I'm a senior developer and I intentionally maintain separate configurations for Claude's web chat, which I use primarily for personal purposes, and my local CLI development environment. Today, I discovered that Claude Code had automatically synced nearly 700 skill and plugin files from my claude.ai account to my development server in two new directories, ~/.claude/skills/synced/ and ~/.claude/plugins/synced/ , adding nearly 10,000 tokens to the start of every session. After investigating, I found that the feature is controlled by a server-side flag ( tengu_claudeai_skills_sync_enabled ). Although it was introduced in September, and (surprisingly) briefly mentioned in the changelog, Anthropic silently enabled it on my machine only a couple of days ago. The first obvious question is: Who at Anthropic thought it was a good idea to automatically mix consumer web chat settings with local development environments? Second, this follows an increasing pattern of questionable behavior. A few months ago, despite disabling auto-updates and pinning my binary, Anthropic hijacked my settings, updated the binary, and silently enrolled my installation in a server-side A/B experiment. The experiment assignment was cached in my local configuration mid-workflow and subsequently sent with every API request through an x-cc-atis header. The changes caused immediate errors, and it took hours of debugging to identify the cause. I understand that some server-side control comes with using Anthropic's services, and I'm fine with that. But there's a difference between remotely managing a service and silently modifying a developer's local environment, potentially wasting hours of their time. If server-side feature flags can modify local files, settings, or behavior, why not at least notify users when those changes occur, particularly when they're being enrolled in A/B experiments?
