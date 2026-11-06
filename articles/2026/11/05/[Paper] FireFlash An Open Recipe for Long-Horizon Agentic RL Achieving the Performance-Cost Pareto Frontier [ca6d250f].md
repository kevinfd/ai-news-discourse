---
id: "ca6d250f780b67b3"
title: "[Paper] FireFlash : An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier"
url: "https://reddit.com/r/LocalLLaMA/comments/1xomst7/paper_fireflash_an_open_recipe_for_longhorizon"
link: "https://reddit.com/r/LocalLLaMA/comments/1xomst7/paper_fireflash_an_open_recipe_for_longhorizon"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T16:17:42Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["pmttyji"]
language: "en"
summary: "We introduce FireFlash , a 300B-scale model tailored for long-horizon agentic tasks. FireFlash excels as a terminal and coding agent, achieving 46.2% on Terminal-Bench 4.0 1 , putting it on par with Fable 5 and GPT-6 Sol, while costing over 30× less per task than Fable 5 at maximum effort (Figure 1). These gains also transfer to software engineering benchmarks, including DeepSWE v1.1 2 and…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Nvidia"]
topics: ["agents & coding", "chips & infrastructure", "models & research"]
content_source: "post"
word_count: 175
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xomst7/paper_fireflash_an_open_recipe_for_longhorizon/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] FireFlash : An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier

Reddit · pmttyji · 2026-11-05

We introduce FireFlash , a 300B-scale model tailored for long-horizon agentic tasks. FireFlash excels as a terminal and coding agent, achieving 46.2% on Terminal-Bench 4.0 1 , putting it on par with Fable 5 and GPT-6 Sol, while costing over 30× less per task than Fable 5 at maximum effort (Figure 1). These gains also transfer to software engineering benchmarks, including DeepSWE v1.1 2 and SWE-Bench Pro Verified 3 (Table 1). While frontier labs scale reinforcement learning across thousands of GPUs, we reach the performance-cost Pareto frontier under 5 days using 64 NVIDIA B300 GPUs . Three key factors make this possible: (1) careful curation of agentic RL environments so that every task provides a reliable signal at the right difficulty; (2) an RL recipe built for long, stale, and low-precision rollouts; and (3) an optimized coding harness tailored to the model for both training and evaluation. Together, these components bring frontier efficiency to a hundred-GPU-scale cluster, and we are releasing the full recipe. Blog Post : https://agenteconomics.org/posts/agentic-rl-recipe Tweet : https://x.com/kaiwei_chang/status/2117378474654781780 Open weights : Soon
