---
id: "76f42ca9be6710ca"
title: "Claude Managed Agents can now be self-hosted (private beta): harness, sandboxes, credentials and session history all run in your own cloud"
url: "https://reddit.com/r/ClaudeAI/comments/1xuwdfs/claude_managed_agents_can_now_be_selfhosted"
link: "https://reddit.com/r/ClaudeAI/comments/1xuwdfs/claude_managed_agents_can_now_be_selfhosted"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T02:45:06Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["emarkosov"]
language: "en"
summary: "Anthropic published this on Nov 12. Self-hosted Claude Managed Agents is now in private beta. What's in it: - The whole service runs in your own cloud or on-prem: the agent harness, sandboxes, credentials and session history. Nothing about your agent's state leaves your environment. - You run the server, its database and the workers yourself. More work, but full control. - Model requests can go…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Amazon", "Google", "Microsoft"]
topics: ["agents & coding", "chips & infrastructure", "models & research", "jobs & society"]
content_source: "post"
word_count: 193
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuwdfs/claude_managed_agents_can_now_be_selfhosted/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Managed Agents can now be self-hosted (private beta): harness, sandboxes, credentials and session history all run in your own cloud

Reddit · emarkosov · 2026-11-13

Anthropic published this on Nov 12. Self-hosted Claude Managed Agents is now in private beta. What's in it: - The whole service runs in your own cloud or on-prem: the agent harness, sandboxes, credentials and session history. Nothing about your agent's state leaves your environment. - You run the server, its database and the workers yourself. More work, but full control. - Model requests can go to Anthropic directly, Amazon Bedrock, Google's Agent Platform, Microsoft Foundry, or your own gateway. Useful if you already have a cloud contract. - Session history stays in your database. Zero data retention, if your org has it, applies to the requests to Claude like any other Messages API call. - Access is through your Anthropic account team. No public sign-up form yet. Docs: https://platform.claude.com/docs/en/managed-agents/self-hosted For context, Managed Agents is Anthropic's set of APIs for building and running autonomous agents. Until now the harness and sandboxes ran on Anthropic's side. This is the one I'd want to try at a company with strict security reviews. For those of you who got blocked by security review on agent tools: was it data residency, credentials, or something else? Source: https://claude.com/resources/articles/self-hosted-claude-managed-agents
