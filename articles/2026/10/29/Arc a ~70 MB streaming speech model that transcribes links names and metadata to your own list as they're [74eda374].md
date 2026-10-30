---
id: "74eda3744f1223ff"
title: "Arc: a ~70 MB streaming speech model that transcribes links names and metadata to your own list as they're spoken, with no second model [p]"
url: "https://reddit.com/r/MachineLearning/comments/1xiyuoj/arc_a_70_mb_streaming_speech_model_that"
link: "https://reddit.com/r/MachineLearning/comments/1xiyuoj/arc_a_70_mb_streaming_speech_model_that"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T22:51:57Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Working_Hat5120"]
language: "en"
summary: "I built Arc-Transcriber, which does ASR-NL in 1-step. Every 100 ms, one model returns the transcript plus: - Names linked to a list you give it (a roster, contacts, product names); new names are flagged \"not on the list\" - Numbers with their values (scores, clocks, money, dates) - Speakers and roles; - Sound and channel events (telephone audio, clipping, poor audio) - Whether the speech was…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 179
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xiyuoj/arc_a_70_mb_streaming_speech_model_that/"
score: null
comments: null
community: "r/MachineLearning"
---

# Arc: a ~70 MB streaming speech model that transcribes links names and metadata to your own list as they're spoken, with no second model [p]

Reddit · Working_Hat5120 · 2026-10-29

I built Arc-Transcriber, which does ASR-NL in 1-step. Every 100 ms, one model returns the transcript plus: - Names linked to a list you give it (a roster, contacts, product names); new names are flagged "not on the list" - Numbers with their values (scores, clocks, money, dates) - Speakers and roles; - Sound and channel events (telephone audio, clipping, poor audio) - Whether the speech was addressed to an assistant. - Inbuilt tags for dialog act, speaker segmentation and more. Total 200+ trained decision heads. The usual ASR, then NER, then entity-linking and then LLM chain is collapsed into the model's own heads, so live "fact-checking" against your list happens inside the stream, not in a second pass. Currently it has two variants Arc mini (which uses moonshot pretrained encoder) and second Arc-v1 (which uses parakeet pretrained encoder). Weights: huggingface.co/WhissleAI/arc-v1.1 Code and CLI: github.com/WhissleAI/arc_transcriber We use it on-device in our Mac app. Voice search over 61k books primes Arc with matching titles while you're still talking. Here is a video to give a glimpse on how it works.
