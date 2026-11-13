---
id: "1085c77a784123d9"
title: "Will Claude Fable 5.2 and GPT-6 Astra make specialized robot models obsolete, or do robots still need their own VLAs, tactile encoders and world models?"
url: "https://reddit.com/r/artificial/comments/1xulg6i/will_claude_fable_52_and_gpt6_astra_make"
link: "https://reddit.com/r/artificial/comments/1xulg6i/will_claude_fable_52_and_gpt6_astra_make"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T19:01:30Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Ok-Possible-5566"]
language: "en"
summary: "A claim I keep running into: now that frontier multimodal models score competitively on robot control benchmarks, specialized embodied models (touch encoders, VLAs, world models) will soon be unnecessary. I think the opposite is more likely. Anthropic's internal RoboDojo Sim runs put Fable 5.2's score at 64.9%, with Astra at 29.8% (the benchmark gives the model camera images). An academic…"
tags: ["r/artificial"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "robotics & autonomy"]
content_source: "post"
word_count: 189
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xulg6i/will_claude_fable_52_and_gpt6_astra_make/"
score: null
comments: null
community: "r/artificial"
---

# Will Claude Fable 5.2 and GPT-6 Astra make specialized robot models obsolete, or do robots still need their own VLAs, tactile encoders and world models?

Reddit · Ok-Possible-5566 · 2026-11-12

A claim I keep running into: now that frontier multimodal models score competitively on robot control benchmarks, specialized embodied models (touch encoders, VLAs, world models) will soon be unnecessary. I think the opposite is more likely. Anthropic's internal RoboDojo Sim runs put Fable 5.2's score at 64.9%, with Astra at 29.8% (the benchmark gives the model camera images). An academic evaluation of Astra on a real robot had to be stopped after the model kept producing physically unsafe actions that broke hardware (arXiv 2609.24170). The authors concluded it handles semantic tasks effectively but struggles with contact-rich, precision-critical work. On the embodied side, LingBot-Touch, a recently released tactile encoder, matched or beat the no-touch baseline in 99 out of 104 tested policy combinations on real robot hands across 26 tasks. Raw tactile input actually made things worse in 22 of those pairs. The way I see it, the general model belongs as the reasoning layer and the robot still needs fast models trained on touch and motion for low-level control. So, for the scaling camp: how exactly do we get to reliable dexterous manipulation without specialized models in the loop?
