---
id: "4c06cda8dbe29277"
title: "Anthropic published a guide on building always-on agents (Nov 13). It breaks them into 5 parts: inbox, timers, memory, permissions, outbox"
url: "https://reddit.com/r/ClaudeAI/comments/1xxdzcf/anthropic_published_a_guide_on_building_alwayson"
link: "https://reddit.com/r/ClaudeAI/comments/1xxdzcf/anthropic_published_a_guide_on_building_alwayson"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T02:35:56Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["emarkosov"]
language: "en"
summary: "Anthropic published \"Building always-on agents\" on Nov 13 (by William Hu, about a 14 minute read). It's a design guide, not a feature launch. The main idea: an always-on agent is asleep most of the time. It wakes up for \"runs\" that work inside sessions. The guide names 5 building blocks: - Event inbox – a durable store where webhooks, schedules and background jobs send events, with one worker…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "jobs & society", "products & launches"]
content_source: "post"
word_count: 244
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xxdzcf/anthropic_published_a_guide_on_building_alwayson/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic published a guide on building always-on agents (Nov 13). It breaks them into 5 parts: inbox, timers, memory, permissions, outbox

Reddit · emarkosov · 2026-11-16

Anthropic published "Building always-on agents" on Nov 13 (by William Hu, about a 14 minute read). It's a design guide, not a feature launch. The main idea: an always-on agent is asleep most of the time. It wakes up for "runs" that work inside sessions. The guide names 5 building blocks: - Event inbox – a durable store where webhooks, schedules and background jobs send events, with one worker per inbox. So nothing is lost while the agent sleeps. - Timers – follow-ups the agent sets for itself, plus recurring schedules, fired by a scheduler. This is how it wakes up without you. - Memory – its own store, usually a directory of files, for instructions, notes, past messages and task progress. It points to Claude Code auto memory and the Messages API memory tool. - Permissions – a credential-injecting proxy, auto mode, and deferred tool calls, where a hook defers a call, the run ends and the session is saved. So it can wait for approval without burning a session. - Outbox – a table of outgoing messages with a dispatcher, or a simple "send" tool. Timing: published Nov 13, so a few days old. It did not get much attention because of the other launches last week. I run a daily scheduled Claude task, and memory is the part where mine is weakest. If you run a scheduled or always-on agent, which of the 5 gave you the most trouble? Source: https://claude.com/resources/articles/building-always-on-agents
