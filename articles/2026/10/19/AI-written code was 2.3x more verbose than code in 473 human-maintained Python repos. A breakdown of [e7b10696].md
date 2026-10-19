---
id: "e7b10696f0c67799"
title: "AI-written code was 2.3x more verbose than code in 473 human-maintained Python repos. A breakdown of SlopCodeBench and what it means for AI-assisted coding"
url: "https://reddit.com/r/ChatGPT/comments/1x9ly2k/aiwritten_code_was_23x_more_verbose_than_code_in"
link: "https://reddit.com/r/ChatGPT/comments/1x9ly2k/aiwritten_code_was_23x_more_verbose_than_code_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T03:08:09Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["aj_marshall"]
language: "en"
summary: "I made a video essay on SlopCodeBench (arXiv 2603.24755, out of UW–Madison). It looks at something most coding benchmarks skip: what happens to an agent's code when the requirements keep changing. Most benchmarks give a model one task and check whether the tests pass. SlopCodeBench gives agents problems that evolve over several checkpoints. At each checkpoint the agent has to extend its own…"
tags: ["r/ChatGPT"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 283
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x9ly2k/aiwritten_code_was_23x_more_verbose_than_code_in/"
score: null
comments: null
community: "r/ChatGPT"
---

# AI-written code was 2.3x more verbose than code in 473 human-maintained Python repos. A breakdown of SlopCodeBench and what it means for AI-assisted coding

Reddit · aj_marshall · 2026-10-19

I made a video essay on SlopCodeBench (arXiv 2603.24755, out of UW–Madison). It looks at something most coding benchmarks skip: what happens to an agent's code when the requirements keep changing. Most benchmarks give a model one task and check whether the tests pass. SlopCodeBench gives agents problems that evolve over several checkpoints. At each checkpoint the agent has to extend its own previous code, with no earlier chat history, just the codebase. That's much closer to how Claude Code actually gets used on a real project. Key findings: 15 models tested, including Opus 4.5, 4.6 and 4.7 and Sonnet 4.6. None fully solved any of the 36 problems. The best strict checkpoint solve rate was 14.8% (GPT 5.5). Opus 4.6 had the highest core test pass rate at 67.3%. Structural erosion increased in 77% of runs and verbosity in 75.5%. Erosion is roughly the share of the code's complexity sitting in overly complex functions. Verbosity is the share of lines that are flagged wasteful patterns or copy-paste clones. Agent code was 2.3x more verbose than code from 473 human-maintained Python repos. One example from the paper: on one problem, Opus 4.7's main() grew from cyclomatic complexity 13 to 92 over 8 checkpoints (38 → 240 lines), getting worse at every single step. "Anti-slop" and plan-first prompts helped at the start. They cut initial verbosity and erosion by up to about a third, but didn't stop the degradation over time. They also raised cost per checkpoint by about 12% on average. These prompts were only tested on GPT models. This is my first video essay, so I'd appreciate if you gave it a watch and left feedback! 🎥 Video: https://youtu.be/KnyQZwHolRQ 📄 Paper: https://arxiv.org/abs/2603.24755v2
