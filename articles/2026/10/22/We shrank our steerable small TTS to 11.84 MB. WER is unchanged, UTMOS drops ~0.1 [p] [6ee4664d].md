---
id: "6ee4664dfe128402"
title: "We shrank our steerable small TTS to 11.84 MB. WER is unchanged, UTMOS drops ~0.1 [p]"
url: "https://reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer"
link: "https://reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T20:57:42Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Working_Hat5120"]
language: "en"
summary: "A while back I posted SteerTTS v1, a small English TTS you steer with numbers ( https://huggingface.co/WhissleAI/steer-tts ). Today I am releasing the edge variant: https://huggingface.co/WhissleAI/steer-tts-edge Size: everything an app has to ship (weights, voices, text front end and Python runtime) totals 11.84 MB . How: Acoustic model (9.25M params, attention + bidirectional Mamba-3) is…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 292
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer/"
score: null
comments: null
community: "r/MachineLearning"
---

# We shrank our steerable small TTS to 11.84 MB. WER is unchanged, UTMOS drops ~0.1 [p]

Reddit · Working_Hat5120 · 2026-10-22

A while back I posted SteerTTS v1, a small English TTS you steer with numbers ( https://huggingface.co/WhissleAI/steer-tts ). Today I am releasing the edge variant: https://huggingface.co/WhissleAI/steer-tts-edge Size: everything an app has to ship (weights, voices, text front end and Python runtime) totals 11.84 MB . How: Acoustic model (9.25M params, attention + bidirectional Mamba-3) is quantization-aware trained to int4 6.2M-param Vocos-style vocoder is distilled from charactr/vocos-mel-24khz , also int4 QAT Text front end is pure numpy, with no NLTK, g2p_en, torchaudio or num2words at runtime Quality (Open TTS Leaderboard protocol, run locally, not an official submission): Seed-TTS WER / UTMOS CV3-Eval WER / UTMOS v1 fp32 (no refiner) 0.96% / 4.20 edge 0.96% / 4.11 Intelligibility is essentially unchanged. UTMOS drops about 0.1, almost all of it from the small int4 vocoder. Steering survives quantization. Every one of the 12 controls (rate, loudness, pitch, pitch range, final rise, pauses, tilt, breathiness, and more) keeps at least 95% of its fp32 effect. You also get 50 style tags and inline markup: Well, *that* was fast. [pause 400ms] <slow>Let me think.</slow> <whisper>Don't tell anyone.</whisper> Speed (CPU only, a 2018 Threadripper under load): RTF 0.053 with 4 threads (~19x realtime), ~120 ms to first audio, with sentence-level streaming. Limitations: English only, and 200 voices (a subset of the full model’s 2,825) No voice cloning, free-text prompts or flow refiner on device. Those stay in the full model. Weights are dequantized to fp32 at load, so the win is size, not speed. Unless we write new kernels for edge devices. Emotion tags are mostly style switches, and fast / anger are weak I need feedback, especially on the vocoder quality gap and any edge targets you’d like to see (ONNX, mobile, WASM). Some examples here: https://whissleai.github.io/steer-tts/
