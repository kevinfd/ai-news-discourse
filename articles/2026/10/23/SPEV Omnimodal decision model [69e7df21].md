---
id: "69e7df219b4a85f3"
title: "SPEV: Omnimodal decision model"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdkub4/spev_omnimodal_decision_model"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdkub4/spev_omnimodal_decision_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T17:45:05Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["ProfessionalHorse707"]
language: "en"
summary: "When Jev / OpenAI decisions came out I got somewhat annoyed that there weren’t any audio native options I could use to act on raw audio inputs instead of having to round trip through an ASR model. The problem I hit running decisions through ASR was some combination of: For speech tasks the transcription step adds latency / cost ASR doesn’t work for non speech tasks (e.g. is this a bird call) In…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 125
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdkub4/spev_omnimodal_decision_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# SPEV: Omnimodal decision model

Reddit · ProfessionalHorse707 · 2026-10-23

When Jev / OpenAI decisions came out I got somewhat annoyed that there weren’t any audio native options I could use to act on raw audio inputs instead of having to round trip through an ASR model. The problem I hit running decisions through ASR was some combination of: For speech tasks the transcription step adds latency / cost ASR doesn’t work for non speech tasks (e.g. is this a bird call) In order to address these issues I built SPEV ( https://huggingface.co/SpragAI/SPEV ) an multimodal decision model based on Qwen3-Omni. It uses the underlying Omni audio/video/image decoders combined with a trained decision head to return probabilities. It supports choices, true/false questions and ordinal scores, with multiple questions handled in a single multimodal forward pass.
