---
id: "1fd6dd971a81f8a5"
title: "DeepSeek: DeepSeek v4.1 Flash 1017"
url: "https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017"
link: "https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017"
source: "OpenRouter"
domain: "openrouter.ai"
source_type: "community"
collector: "hackernews"
date: "2026-10-17T08:37:46Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["theanonymousone"]
language: "en"
summary: "deepseek/deepseek-v4.1-flash-1017\nModel weights\nDeepSeek V4.1 Flash 1017 is the October 17, 2026 snapshot of DeepSeek V4.1 Flash, served by DeepSeek under the deepseek-flash API model name. V4.1 Flash is a sparse mixture-of-experts model from DeepSeek, and the first built on the company's Causal Encoder-Decoder (CED) architecture. It activates 8B parameters on input and 16B on output from a…"
tags: []
orgs: ["DeepSeek", "Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 383
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50129121"
score: 242
comments: 75
community: "Hacker News"
---

# DeepSeek: DeepSeek v4.1 Flash 1017

OpenRouter · theanonymousone · 2026-10-17

deepseek/deepseek-v4.1-flash-1017
Model weights
DeepSeek V4.1 Flash 1017 is the October 17, 2026 snapshot of DeepSeek V4.1 Flash, served by DeepSeek under the deepseek-flash API model name. V4.1 Flash is a sparse mixture-of-experts model from DeepSeek, and the first built on the company's Causal Encoder-Decoder (CED) architecture. It activates 8B parameters on input and 16B on output from a 552B-parameter backbone, an asymmetric split that keeps per-token compute low relative to the model's total size. Image understanding is native to the architecture, with visual and text embeddings trained jointly from the start of pre-training rather than added afterward as in the earlier experimental V4 Flash Vision ExpOpens in new tab.
It is suited for coding, terminal, and computer-use agents, along with long-horizon tasks that must run to completion across many steps and long-context analysis. Compressed KV caching cuts cache memory to roughly a quarter of the previous Flash generation, significantly reducing costs on agentic workloads. DeepSeek positions it as the cost-efficient tier of the V4.1 family and reports that it exceeds V4 ProOpens in new tab on performance, speed, and task completion time.
Modalities
In / Out Price
$0.10 / $0.50per 1M
Context
1.0M
Released
Oct 17, 2026
DeepSeek: DeepSeek Flash versions
Not currently available through EU in-region routing. In-region routing docs
Throughput
153tok/s
P50, best across providers
Latency
0.53s
P50, best provider
Uptime (3d)The model was reachable. Request routed to a provider.
100.00%
Availability (3d)The model returned inference from any provider. Errors and empty responses count against it.
99.88%
3 Days Ago2 Days AgoYesterdayNow
OpenRouter Availability
99.89%
Without Routing
98.72%
When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the Endpoints API. Learn more about our load balancing and provider routing options.
1.
Claude Code Claude Code is Anthropic's agentic coding tool that reads your entire codebase, plans and executes changes across files, runs tests, and iterates on failures, all from natural language prompts.
1.28Btokens
4.
Hermes Agent Hermes Agent is an open-source, self-improving AI agent by Nous Research that runs persistently with memory across sessions, and builds reusable skills from experience. It comes with 40+ built-in tools, including web search, browser automation, and vision, plus scheduled automations and subagents.
696Mtokens
