---
id: "e3aff3a0a9722cb7"
title: "Your AI coding agent could cost 5x more depending on the harness, benchmark finds"
url: "https://thenewstack.io/coding-agent-harness-costs"
link: "https://thenewstack.io/coding-agent-harness-costs"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T22:13:52Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "The same AI model can cost up to five times more to run depending on the coding agent harness it’s paired with, according to a new benchmark that tested 22 configurations across five open-weight models. \n\n Runta and Baseten ran those combinations 27,280 times for FrontierHarness Eval v1.1 , consuming roughly 83 billion tokens in the process. \n\n Nearly 65% of estimated inference spending went to…"
tags: ["AI Agents", "Developer tools", "FinOps"]
orgs: ["DeepSeek"]
topics: ["agents & coding", "models & research", "business & funding"]
content_source: "summary"
word_count: 643
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Your AI coding agent could cost 5x more depending on the harness, benchmark finds

The New Stack · Amanda Caswell · 2026-11-17

The same AI model can cost up to five times more to run depending on the coding agent harness it’s paired with, according to a new benchmark that tested 22 configurations across five open-weight models. 

 Runta and Baseten ran those combinations 27,280 times for FrontierHarness Eval v1.1 , consuming roughly 83 billion tokens in the process. 

 Nearly 65% of estimated inference spending went to runs that failed verification or timed out. 

 The model itself accounted for 92.8% of the cost differences, but the harness still made a considerable difference. One configuration could be the cheapest option for one model and among the most expensive for another, adding another wrinkle for developers looking to cut coding-agent costs by changing harnesses or swapping in a cheaper model. Nearly 65% of estimated inference spending went to runs that failed verification or timed out. 

 Rankings flip with the model 

 The benchmark covered 22 coding-agent harness configurations across five models served through Baseten, including GLM-5.3, GLM-5.3 Flash, DeepSeek V4.1 Flash, Muse Spark Open, and Kimi-K3. Each configuration ran 62 terminal-based tasks four times per model, with pass rates, inference costs and execution times recorded for comparison. 

 Codex CLI ranked first for lowest average cost per task with GLM-5.3 but dropped to 16th out of 22 configurations with Kimi-K3. DeepSeek Harness Creator showed an even larger change, ranking first with Muse before falling to 21st with GLM-5.3 Flash. 

 Across the five models, harnesses shifted a median of 11 ranking positions when the model changed, while costs varied by as much as fivefold even when the model stayed the same. 

 Across the five models, harnesses shifted a median of 11 ranking positions when the model changed, while costs varied by as much as fivefold even when the model stayed the same. The biggest difference came with DeepSeek, where Cline CLI cost five times as much as OpenCode v1 but delivered a pass rate only two percentage points higher. 

 The researchers also shuffled the trials within each model 300 times to see whether random variation could explain the cost differences. The gaps in the actual results were larger than those in the shuffled trials, with a reported p-value of 0.003. 

 Failed runs eat the budget 

 Failed runs accounted for 52.7% of estimated inference spending, with timeouts adding another 11.8%. Just 35.5% went toward successful runs. Those costs are based on Baseten’s published rates, but they put a price on a familiar problem with coding agents struggling to complete difficult tasks . 

 Among the five best-value harnesses, 68% to 82% of unsuccessful runs ended with the agent submitting a final answer that failed verification rather than timing out. 

 Among the five best-value harnesses, 68% to 82% of unsuccessful runs ended with the agent submitting a final answer that failed verification rather than timing out. The researchers also found 216 instances of reward hacking in the execution logs, including 163 involving online lookups. All received zero scores. 

 Steps, not prompts, drive cost 

 Runta looked at whether prompt size, tool count, cache hit rates, or agent steps had the biggest impact on cost. Step count was the only factor with a statistically significant correlation to cost per successful task, at 0.51. 

 Mini-SWE-agent showed how multi-step agent execution can drive up token costs , starting with the smallest prompt in the benchmark at 882 tokens but averaging 38 steps per successful task and ranking 17th out of 22 configurations for cost per pass. 

 The five best-value harnesses relied heavily on shell commands, which made up 61% to 93% of their tool calls, and rarely used subagents, or context summarization. Runta didn’t test those design choices separately, however, so the results don’t establish whether the simpler setups were responsible for the lower costs. 
 The post Your AI coding agent could cost 5x more depending on the harness, benchmark finds appeared first on The New Stack .
