---
id: "f50addd24ad0d09b"
title: "Dream come true: I trained 48 in-browser 24 kHz TTS voices for Classical Sanskrit, English & 10 Indic languages (21.7 MB mobile iSTFTNet / 27.9 MB HiFi-GAN)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xomom1/dream_come_true_i_trained_48_inbrowser_24_khz_tts"
link: "https://reddit.com/r/LocalLLaMA/comments/1xomom1/dream_come_true_i_trained_48_inbrowser_24_khz_tts"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T16:13:12Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["init0"]
language: "en"
summary: "It is a dream come true for me to build an in-browser TTS model for Indic languages, including Classical Sanskrit. Today I'm open-sourcing Ninada (code MIT, 48 ONNX checkpoints CC-BY-4.0). Live in-browser studio (zero sign-up, 100% on-device): https://h3manth.com/ai/ninada/ Getting studio 24 kHz audio onto real phones was trickier than expected. Meta's 16 kHz MMS models take 1.5 GB, and on my…"
tags: ["r/LocalLLaMA"]
orgs: ["Meta", "Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 221
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xomom1/dream_come_true_i_trained_48_inbrowser_24_khz_tts/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Dream come true: I trained 48 in-browser 24 kHz TTS voices for Classical Sanskrit, English & 10 Indic languages (21.7 MB mobile iSTFTNet / 27.9 MB HiFi-GAN)

Reddit · init0 · 2026-11-05

It is a dream come true for me to build an in-browser TTS model for Indic languages, including Classical Sanskrit. Today I'm open-sourcing Ninada (code MIT, 48 ONNX checkpoints CC-BY-4.0). Live in-browser studio (zero sign-up, 100% on-device): https://h3manth.com/ai/ninada/ Getting studio 24 kHz audio onto real phones was trickier than expected. Meta's 16 kHz MMS models take 1.5 GB, and on my Pixel 10 Pro XL, mobile WebGPU froze for 6 to 14s compiling shaders while 2-thread WASM actually ran slower than 1 thread on mobile CPU cores. So I trained 48 native-script 24 kHz VITS specialists across 12 languages (sa, en, hi, kn, mr, bn, ta, te, ml, gu, pa, or; male and female): • Device-aware voices: Desktops run 27.9 MB HiFi-GAN (89 ms on WebGPU), while phones auto-switch to a 21.7 MB distilled iSTFTNet (2.64x lighter, zero custom ONNX ops). • Sub-second streaming: Splits the VITS ONNX model in <15 ms in browser memory (cutting browser RAM 72% to 162 MB) to stream speech in 538 ms on phones with 0 audio dropouts. • Studio quality, offline-ready: 3.09 to 3.22 dB MCD across 480 test clips, cached locally after first load, with a 0 MB Klatt fallback. GitHub (npm i ninada / pip install ninada): https://github.com/hemanth/ninada Hugging Face (48 ONNX checkpoints): https://huggingface.co/gnumanth/ninada Would love feedback on how your language sounds!
