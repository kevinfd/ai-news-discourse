---
id: "6a131d09282fa503"
title: "Anthropic’s new guide (Oct 22) argues most agents should have fewer subagents: one main loop, skills and tool search instead. Includes “we cut Claude Code’s system prompt by over 80%”"
url: "https://reddit.com/r/ClaudeAI/comments/1xdwquj/anthropics_new_guide_oct_22_argues_most_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xdwquj/anthropics_new_guide_oct_22_argues_most_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T02:15:23Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["emarkosov"]
language: "en"
summary: "Anthropic published an 18-minute guide on Oct 22 called \"When to fold subagents into your main agent loop.\" It is aimed at enterprise agent builders, but the lessons apply to anyone who set up a pile of subagents in Claude Code. Main points: - Default to one model, one context window, one open-ended tool loop. Put domain procedures into skills and hard limits and lookups into tools. Let the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "post"
word_count: 295
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdwquj/anthropics_new_guide_oct_22_argues_most_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic’s new guide (Oct 22) argues most agents should have fewer subagents: one main loop, skills and tool search instead. Includes “we cut Claude Code’s system prompt by over 80%”

Reddit · emarkosov · 2026-10-24

Anthropic published an 18-minute guide on Oct 22 called "When to fold subagents into your main agent loop." It is aimed at enterprise agent builders, but the lessons apply to anyone who set up a pile of subagents in Claude Code. Main points: - Default to one model, one context window, one open-ended tool loop. Put domain procedures into skills and hard limits and lookups into tools. Let the model write and revise its own plan. - Keep subagents only when you measure degradation from context bloat, need parallel work with disposable context, or the agent struggles with too many tools or conflicting instructions. - One customer's single loop ran roughly 2x faster than its multi-agent harness. Several deployments saw better quality, lower cost and lower latency. - Tool choice tends to degrade past 30-50 tool definitions in the system prompt. Group tools by user intent and use tool search with deferred loading. - Anthropic cut Claude Code's own system prompt for newer models by over 80%. - Start with evals before you refactor. 10 golden examples are enough to begin. Run each task more than once, because one regression only showed in one of two runs. - Failure modes they list for big orgs: lost context between agents, subagent sprawl, the "Frankenprompt" where every team adds rules, overly local evals, latency. - New /claude-api skills for the migration: build-eval, prompt-audit, hillclimb, cost-optimize, plus /skill-creator and /skill-doctor. There is a kit on GitHub (anthropics/single-agent-loop-kit). I had about six subagents at one point and ended up using two. This article matches what I saw: most of them were just skills with a separate context window. Where do subagents still earn their place for you, and how many do you actually use day to day? Source: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
