---
id: "f28552647362533e"
title: "Fabel 5.1 Can Write AI Model Weights Directly Without Training"
url: "https://reddit.com/r/ClaudeAI/comments/1xrmui5/fabel_51_can_write_ai_model_weights_directly"
link: "https://reddit.com/r/ClaudeAI/comments/1xrmui5/fabel_51_can_write_ai_model_weights_directly"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T08:59:29Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Hephaestite"]
language: "en"
summary: "I've been experimenting with having Fable 5.1 write every weight of a neural network straight from a written spec. Staring from zero, with no training data and no optimiser. I wanted to showed it could be done and I wanted to know whether it's actually useful, so I thought I would try it on two jobs with absolutely nothing in common. Spotting coding agents stuck in loops . A 2.1M-parameter…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["models & research", "agents & coding", "chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 339
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrmui5/fabel_51_can_write_ai_model_weights_directly/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Fabel 5.1 Can Write AI Model Weights Directly Without Training

Reddit · Hephaestite · 2026-11-09

I've been experimenting with having Fable 5.1 write every weight of a neural network straight from a written spec. Staring from zero, with no training data and no optimiser. I wanted to showed it could be done and I wanted to know whether it's actually useful, so I thought I would try it on two jobs with absolutely nothing in common. Spotting coding agents stuck in loops . A 2.1M-parameter transformer labels each tool call as productive, recovering, stalled or oscillating. It scored 0.957 on a hidden test set and 0.908 on logs from an independently written generator. On those off-distribution logs it raised false alarms on 6.8% of healthy windows. The same architecture trained conventionally on 223,930 labels raised them on 34.5%. Total cost was US$64.62 of model usage at API rates but I did this on a normal subscription. Lighting a cloud . A 3,057-parameter network tells a ray marcher how much light reaches each point inside a cumulus cloud. Against path-traced references it gets within 13.8% on luminance (15.5% on held-back views), versus 82.4% for a single-scattering baseline. Almost every weight is zero or a physics formula, so it compiled down to 116 terms of shader code. It runs at 60 fps in the browser, and you can drag the sun around in the post. It cost US$75.77. The thing that I found interesting about the results wasn't the experiements themselves (although I have to say the cloud illumination model is quite pretty ), it's the follow on question of how this can be ultilised going forward. I've worked in a lot of different domains and my mind is racing with all the highly domain specific things I could have used a model for that would have out performed a rules engine or whatever. It feels like a use case thats massively under utilised at the moment, what could we do in the world when we can just spin up custom models for our own niche tasks, and tune them with natural language as we go?
