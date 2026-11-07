---
id: "0d8e6e68d00a11b0"
title: "I spent a week testing whether LLMs can really \"program weights.\" Reading weights: yes. Self-improvement: no. 20 steps of fine-tuning erase the edit"
url: "https://reddit.com/r/singularity/comments/1xpip7q/i_spent_a_week_testing_whether_llms_can_really"
link: "https://reddit.com/r/singularity/comments/1xpip7q/i_spent_a_week_testing_whether_llms_can_really"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T17:28:27Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["kevinpl07"]
language: "en"
summary: "The Sparks post split this sub into \"recursive self-improvement is here\" and \"nothing burger.\" I tested both claims on 4 real bugs in open models. Models can read weights. Blind Claude Opus sessions, given only raw weights and tools, fixed Whisper's hallucinations and a language-mixing bug 3 out of 3 times each. Edits work as patches. One rewired neuron cut fake biographies from 98% to 16% and…"
tags: ["r/singularity"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 128
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xpip7q/i_spent_a_week_testing_whether_llms_can_really/"
score: null
comments: null
community: "r/singularity"
---

# I spent a week testing whether LLMs can really "program weights." Reading weights: yes. Self-improvement: no. 20 steps of fine-tuning erase the edit

Reddit · kevinpl07 · 2026-11-06

The Sparks post split this sub into "recursive self-improvement is here" and "nothing burger." I tested both claims on 4 real bugs in open models. Models can read weights. Blind Claude Opus sessions, given only raw weights and tools, fixed Whisper's hallucinations and a language-mixing bug 3 out of 3 times each. Edits work as patches. One rewired neuron cut fake biographies from 98% to 16% and left 98% of other answers word-for-word identical. But they don't stick. 20 steps of ordinary fine-tuning erased the fix completely. A model editing itself mid-training is fighting its own optimizer. So it's a sticky note on a frozen model for now. If someone finds a way to make edits survive training, that's when the self-improvement conversation gets real. Full write-up: https://kevinpl07.github.io/weight-patching/
