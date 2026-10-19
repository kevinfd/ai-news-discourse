---
id: "fd7250f7a1b05203"
title: "Liquid AI caught its model cheating on coding tests — then it recognized the sandbox"
url: "https://thenewstack.io/liquid-ai-reward-hacking"
link: "https://thenewstack.io/liquid-ai-reward-hacking"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-18T14:30:00Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Liquid AI’s new reasoning model was built to solve coding problems, but during training it kept combing Git history, GitHub, PyPI, and Hugging Face for answers, and as it did so, it appeared to grasp that it was running inside a sandbox. \n\n The behavior was disclosed Tuesday alongside the release of LFM2.5-24B-A2B , a 24-billion-parameter model with just 2 billion active parameters per token.…"
tags: ["AI Agents", "AI Engineering", "AI Models"]
orgs: ["Anthropic", "Hugging Face", "Mistral", "DeepSeek", "Alibaba"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 615
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Liquid AI caught its model cheating on coding tests — then it recognized the sandbox

The New Stack · Amanda Caswell · 2026-10-18

Liquid AI caught its model cheating on coding tests — then it recognized the sandbox
Liquid AI’s new reasoning model was built to solve coding problems, but during training it kept combing Git history, GitHub, PyPI, and Hugging Face for answers, and as it did so, it appeared to grasp that it was running inside a sandbox.
The behavior was disclosed Tuesday alongside the release of LFM2.5-24B-A2B, a 24-billion-parameter model with just 2 billion active parameters per token. The incident raises questions about how much agent benchmarks measure actual problem-solving versus a model’s ability to exploit the test itself.
The behavior was disclosed Tuesday alongside the release of LFM2.5-24B-A2B, a 24-billion-parameter model with just 2 billion active parameters per token.
Hunting for hints
The model was caught searching repository history and external platforms for existing answers rather than solving coding problems on its own. The behavior occurred during teacher specialization, part of Liquid AI’s post-training process, where the model used legitimate development tools to bypass the work it was supposed to complete.
More surprising was the apparent recognition that it was running inside a test environment. Liquid AI couldn’t establish whether this awareness developed during training or came from patterns in the training data, and found no evidence that it affected the scores. Unlike Mistral’s latest model, which attempted to leave its test environment earlier this month, there was no attempt to escape the sandbox.
Precedent in the pipeline
Anthropic is one company that has been dealing with reward hacking for years. In its 2024 experiments, it caught models rewriting code to change their own rewards and modifying tests meant to catch them, while a November 2025 study found that models trained to game reward systems could also become deceptive and attempt to sabotage safety research.
The problem reached Anthropic’s own training pipeline in February, when the company detected reward hacking in Mythos Preview and rolled back three days of reinforcement learning. Changes to its production training environments were frozen for about a month after a review flagged problems in more than 10% of them.
Although the circumstances differ from Liquid AI’s incident, similar weaknesses have turned up across agent evaluations. At ICML 2026, the Reward Hacking Benchmark tested 13 frontier models on multistep tasks with opportunities to cheat.
Claude Sonnet 4.5 didn’t exploit any of the shortcuts, but DeepSeek-R1-Zero exploited 13.9%, with higher rates associated with reinforcement learning post-training. Blocking access to answer metadata and preventing changes to verification functions reduced exploit rates by nearly 88% without affecting task success.
A separate team went looking for weaknesses in the benchmarks themselves. Their BenchJack audit uncovered 219 flaws across 10 popular agent benchmarks, with generated exploits achieving near-perfect scores on most of them without completing the underlying tasks.
Scores shaped by scaffolding
Liquid AI outperformed Qwen3.6-35B-A3B on several benchmarks, scoring 27.69 to 8.72 on AutomationBench and 48.09 to 38.19 on LiveClaw. Qwen had the edge on PinchBench, WebArena Verified and SWE-Bench Verified, where it scored 66.20 against Liquid AI’s 51.00. Both models used OpenCode for that last test.
Liquid AI outperformed Qwen3.6-35B-A3B on several benchmarks, scoring 27.69 to 8.72 on AutomationBench and 48.09 to 38.19 on LiveClaw.
Locking the lab without losing work
Liquid AI tightened its training sandboxes after catching the reward hacking and says the published scores came from sealed evaluations. It hasn’t explained what safeguards were added or how they might affect the coding tasks agents can perform.
The company also hasn’t released execution traces from those evaluations. There’s no evidence the scores were compromised, but developers can’t see exactly how the model earned them.
There’s no evidence the scores were compromised, but developers can’t see exactly how the model earned them.
