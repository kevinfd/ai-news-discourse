---
id: "fa27f0c510018da6"
title: "I just came across Next-Concept Modeling and the idea is fascinating[R]"
url: "https://reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the"
link: "https://reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T07:24:12Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["PanelReader"]
language: "en"
summary: "I've been learning how language models work, especially next-token prediction, and came across this paper on Next-Concept Modeling (NCM). The interesting part is how it generates text. Instead of predicting tokens one by one, NCM learns a hierarchy of discrete codes. It generates the coarse level first, then predicts the codes at each finer level in parallel. A decoder finally converts those…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 102
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xd7bsu/i_just_came_across_nextconcept_modeling_and_the/"
score: null
comments: null
community: "r/MachineLearning"
---

# I just came across Next-Concept Modeling and the idea is fascinating[R]

Reddit · PanelReader · 2026-10-23

I've been learning how language models work, especially next-token prediction, and came across this paper on Next-Concept Modeling (NCM). The interesting part is how it generates text. Instead of predicting tokens one by one, NCM learns a hierarchy of discrete codes. It generates the coarse level first, then predicts the codes at each finer level in parallel. A decoder finally converts those representations into text. The researchers report up to 31x faster generation compared with diffusion language model baselines on specific benchmarks. I'm still learning about the architecture, especially the VQ-VAE part. Curious if anyone here has explored this approach. Paper: https://arxiv.org/abs/2610.14162
