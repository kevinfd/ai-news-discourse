---
id: "b7da720a6faff934"
title: "Training Memorilla on Strix Halo for Gemma4"
url: "https://reddit.com/r/LocalLLaMA/comments/1xtfle1/training_memorilla_on_strix_halo_for_gemma4"
link: "https://reddit.com/r/LocalLLaMA/comments/1xtfle1/training_memorilla_on_strix_halo_for_gemma4"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T11:39:55Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["DataPhreak"]
language: "en"
summary: "Spent the past couple of days converting https://github.com/snap-stanford/memorilla (paper: https://arxiv.org/abs/2610.21375 ) to train Gemma4 26b a4b on the strix. Not only was it originally written for CUDA, but Gemma4 has a unique architecture and the encoder has different dimensions. There's a lot of crazy math here to make it fit that I don't even understand, but apparently, we can leverage…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 164
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xtfle1/training_memorilla_on_strix_halo_for_gemma4/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Training Memorilla on Strix Halo for Gemma4

Reddit · DataPhreak · 2026-11-11

Spent the past couple of days converting https://github.com/snap-stanford/memorilla (paper: https://arxiv.org/abs/2610.21375 ) to train Gemma4 26b a4b on the strix. Not only was it originally written for CUDA, but Gemma4 has a unique architecture and the encoder has different dimensions. There's a lot of crazy math here to make it fit that I don't even understand, but apparently, we can leverage the existing weights published by standford and only have to train on ~10% of the original dataset. It's going to take a couple of weeks to run, but seems to be cooking along. Code: https://github.com/DataBassGit/MemoryLLM-Gemma4-StrixHalo Memorilla is an AI memory framework developed by researchers from Stanford, MIT, UPenn, and the Vector Institute that compresses huge collections of documents or chat histories into just 16 dynamic memory tokens for a Large Language Model. Think of it as treating long-term memory like a new modality (similar to how vision-language models process an image as a fixed set of embeddings) rather than relying on massive text copy-pasting.
