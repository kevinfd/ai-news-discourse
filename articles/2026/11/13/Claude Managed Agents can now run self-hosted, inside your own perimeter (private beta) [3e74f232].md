---
id: "3e74f232c47dc93d"
title: "Claude Managed Agents can now run self-hosted, inside your own perimeter (private beta)"
url: "https://reddit.com/r/ClaudeAI/comments/1xuw68g/claude_managed_agents_can_now_run_selfhosted"
link: "https://reddit.com/r/ClaudeAI/comments/1xuw68g/claude_managed_agents_can_now_run_selfhosted"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T02:35:19Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "Anthropic announced self-hosted Managed Agents yesterday. The harness, sandboxes, credentials and session history run in your cloud or on-prem, and model requests go where you point them: Anthropic directly, Amazon Bedrock, Google's Agent Platform, Microsoft Foundry, or your own gateway. Two boundaries are worth stating precisely. Session history and credentials are stored in your environment,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Amazon", "Google", "Microsoft"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 177
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuw68g/claude_managed_agents_can_now_run_selfhosted/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Managed Agents can now run self-hosted, inside your own perimeter (private beta)

Reddit · shoumikgoswami · 2026-11-13

Anthropic announced self-hosted Managed Agents yesterday. The harness, sandboxes, credentials and session history run in your cloud or on-prem, and model requests go where you point them: Anthropic directly, Amazon Bedrock, Google's Agent Platform, Microsoft Foundry, or your own gateway. Two boundaries are worth stating precisely. Session history and credentials are stored in your environment, but whatever an agent puts into a model request, including code and task context, still goes to the model provider you picked. And zero data retention only applies if your organization already has that agreement with Anthropic; then it covers these requests like any other Messages API call. The security design is the part worth reading. When an agent runs unattended there is nobody reviewing each step, so the limits sit in the architecture: the agent loop and session history live outside the sandbox, a proxy attaches credentials to requests so secrets never enter it, each environment gets a host allowlist, and every step exports over OpenTelemetry into your existing monitoring. Access for now is through an Anthropic account team. Source: https://claude.com/resources/articles/self-hosted-claude-managed-agents
