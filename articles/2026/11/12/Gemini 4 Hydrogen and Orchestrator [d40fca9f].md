---
id: "d40fca9fd5e12c4b"
title: "Gemini 4 Hydrogen and Orchestrator"
url: "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity"
link: "https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity"
source: "Google Antigravity"
domain: "antigravity.google"
source_type: "community"
collector: "hackernews"
date: "2026-11-12T18:52:01Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["jonbaer"]
language: "en"
summary: "Explore our next generation products\nBuilt for developers and teams in the agent-first era\nEverything you need to stay up-to-date and get help\nGemini 4 Hydrogen and Orchestrator\nToday, we’re rolling out Gemini 4 Hydrogen inside Google Antigravity alongside a new model dropdown option called Orchestrator, which pairs Hydrogen with our strongest models for long-horizon tasks, including Gemini 4…"
tags: []
orgs: ["Google"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 586
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50472260"
score: 440
comments: 130
community: "Hacker News"
---

# Gemini 4 Hydrogen and Orchestrator

Google Antigravity · jonbaer · 2026-11-12

Explore our next generation products
Built for developers and teams in the agent-first era
Everything you need to stay up-to-date and get help
Gemini 4 Hydrogen and Orchestrator
Today, we’re rolling out Gemini 4 Hydrogen inside Google Antigravity alongside a new model dropdown option called Orchestrator, which pairs Hydrogen with our strongest models for long-horizon tasks, including Gemini 4 Carbon, in an optimized balance of quality, efficiency, and latency.
Put Gemini 4 Carbon and Gemini 4 Hydrogen to work with Orchestrator
Earlier this week, we introduced Gemini 4 Carbon alongside /swarm for tackling massive, multi-worktree engineering tasks with parallel agent teams. In just a couple of days, tens of thousands of swarms have been launched on Antigravity, pushing frontier intelligence on the hardest problems.
For everyday feature work and debugging inside a single session, running a frontier reasoning model with multiple parallel agents on every step of every routine task slows down your loop and burns frontier quota. A common industry approach is to use a static “model router” that guesses task difficulty from your first prompt and routes the entire task to the cheapest model that is good enough to complete the task. Unfortunately, these start breaking down as agents become longer running, requiring different levels of complexity at different stages, often discovered as the task evolves.
Orchestrator takes a dynamic, bidirectional approach between Carbon and Gemini 4 Hydrogen within the evolution of a single trajectory. For example, Carbon can start in a read-only phase to explore dependencies, resolve ambiguities, and build a concrete plan with explicit re-planning triggers. Hydrogen could then take over to write edits, update packages, and run tests. If Hydrogen hits friction, it would hand back to Carbon to inspect the state, repair the plan, and resume execution. This allows Orchestrator to reach near-Carbon task success while being faster and more quota-efficient. On Terminal-Bench 4.1, Orchestrator reached near-Carbon task success rates while, on average, consuming 24% less quota and completing 19% faster.
- Explicit multi-model pipelines with the Antigravity SDK: When you want programmatic control over which model handles each role, you can wire Hydrogen and Carbon together directly with the Antigravity SDK. In the demo below, an open-source issue triage system built with the Antigravity SDK pairs multiple agents together. The Hydrogen agents handle triaging and coding to keep up with incoming issue volume, searching the codebase, asking clarifying questions, and fast UI iteration from PR comments while the Carbon agent is assigned to larger refactors, new features, and security checks.
- Fast, dependable execution with Gemini 4 Hydrogen: Hydrogen also works as a standalone model for everyday coding and agentic work, scoring 51 on the Artificial Analysis Intelligence Index (surpassing Argon’s 50, and reaching 54 at its highest setting) and 57% on Terminal-Bench 4.1 (more than tripiling 3.8 Flash’s 18.2%). When selecting Hydrogen directly, you can dial reasoning depth across four thinking levels, low, medium, high (default), and a new xhigh tier.
Getting started
Gemini 4 Hydrogen brings cutting-edge intelligence for everyday coding and agentic workflows. When you want frontier planning paired with speed without managing model switches, Orchestrator puts both Gemini 4 Carbon and Gemini 4 Hydrogen behind one prompt. Starting today, Gemini 4 Hydrogen is rolling out across paid Google AI Pro and Ultra subscribers. Orchestrator is rolling out as Orchestrator (Carbon) and Orchestrator (Argon) for Google AI Ultra subscribers, and as Orchestrator (Argon) for paid Google AI Pro subscribers, with additional models and plans supported in the future. Enterprises can access both in Gemini for business.
