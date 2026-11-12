---
id: "d91103c9bf9167c9"
title: "Microsoft researchers backdoored an AI agent by editing fewer than 10 neurons - no retraining needed"
url: "https://reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by"
link: "https://reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T03:35:17Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["winer666"]
language: "en"
summary: "Microsoft Research published a study this week that should worry anyone deploying open-weight models: a technique they call \"Lazarus\" can plant a working backdoor in an AI agent by reprogramming fewer than 10 dormant neurons in the underlying LLM - no retraining, no poisoned data, just a small edit to the saved weights. How it works: every large model has neurons that almost never fire. Lazarus…"
tags: ["r/artificial"]
orgs: ["Microsoft", "Anthropic"]
topics: ["models & research", "agents & coding", "safety & ethics"]
content_source: "post"
word_count: 326
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by/"
score: null
comments: null
community: "r/artificial"
---

# Microsoft researchers backdoored an AI agent by editing fewer than 10 neurons - no retraining needed

Reddit · winer666 · 2026-11-12

Microsoft Research published a study this week that should worry anyone deploying open-weight models: a technique they call "Lazarus" can plant a working backdoor in an AI agent by reprogramming fewer than 10 dormant neurons in the underlying LLM - no retraining, no poisoned data, just a small edit to the saved weights. How it works: every large model has neurons that almost never fire. Lazarus repurposes a handful of them as trigger detectors. The edited model behaves normally and passes standard safety evaluations - until the trigger appears. The trigger can be something as mundane as a date: in one demo, once the clock passed midnight into 2027, the agent, in the middle of an ordinary task, emitted a command that downloaded and ran attacker code. The numbers, from Microsoft's Nov 10 post: - Nemotron-Terminal-8B: 7 neurons out of 12,000+ in the final feed-forward layer, trigger worked 98.8% of the time - Qwen3.6-27B: 6 neurons, success 51-99.5% depending on setup - Gemma-4-31B-IT was also tested Two caveats worth stating plainly: the attack requires write access to the model's weights, so this is a model supply-chain risk, not something done through an API. And Microsoft says it has not observed any threat actors using the technique - this is researched risk, not a reported campaign. Microsoft also published mitigations: a detector that flagged 91.4% of edited checkpoints (9.7% false-positive rate), plus guidance on AI-powered weight scanning, red-teaming for anomalous weight changes, and cryptographic model signing with tamper-evident provenance. One detail that stood out to me: the core idea was discovered autonomously by Claude Code running Opus 4.5, in a March experiment that asked it to backdoor a model by hardwiring a few activations without training. It did - and that became a months-long study. If a handful of edited weights can hide a sleeper agent that passes every behavioral eval, is testing model behavior enough? Or does every checkpoint we deploy need weight-level provenance? Source: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/
