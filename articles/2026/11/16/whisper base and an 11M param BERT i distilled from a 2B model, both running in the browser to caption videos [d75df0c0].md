---
id: "d75df0c00521daa4"
title: "whisper base and an 11M param BERT i distilled from a 2B model, both running in the browser to caption videos"
url: "https://reddit.com/r/LocalLLaMA/comments/1xy25lw/whisper_base_and_an_11m_param_bert_i_distilled"
link: "https://reddit.com/r/LocalLLaMA/comments/1xy25lw/whisper_base_and_an_11m_param_bert_i_distilled"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T21:40:43Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Pantheon3D"]
language: "en"
summary: "i make Blender tutorials as shorts and got tired of uploading every render to a caption service, so i made a caption tool that runs the models in the browser instead transcription is onnx-community/whisper-base_timestamped through transformers.js. real GPUs get WebGPU in fp32, everything else gets WASM with the decoder in q8. software WebGPU adapters turned out to be slower than WASM so those…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 225
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xy25lw/whisper_base_and_an_11m_param_bert_i_distilled/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# whisper base and an 11M param BERT i distilled from a 2B model, both running in the browser to caption videos

Reddit · Pantheon3D · 2026-11-16

i make Blender tutorials as shorts and got tired of uploading every render to a caption service, so i made a caption tool that runs the models in the browser instead transcription is onnx-community/whisper-base_timestamped through transformers.js. real GPUs get WebGPU in fp32, everything else gets WASM with the decoder in q8. software WebGPU adapters turned out to be slower than WASM so those get WASM too the part i had the most fun with is the caption tagger: which words get emphasis, where lines break, and fixing missing punctuation and capitals. it started as hand written rules, now it’s a BERT-mini (about 11M params, 8 labels per token, ~12mb) running in q8 on WASM. the training data came from LFM3-Omni-2B on llama.cpp on my own pc, about 190 scripts a minute on a 4070 ti super with 128 parallel slots. it only got to replace the rules because it beat them on held out data whisper base isn’t as accurate as the bigger ones so there’s a cloud option for noisy audio, and the tagger is english only for now has anyone gotten whisper small or turbo running in the browser at a usable speed? that’s what i want to try next :) https://cuecaps.com/studio?ref=reddit if you want to see it run (i’m the creator) also thank you for reading, it means a lot to me
