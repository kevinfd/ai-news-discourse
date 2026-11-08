---
id: "5e7dca67d4988a34"
title: "Released an open-source EOU detection model covering English + 8 Indic languages voice agents stop cutting callers off mid-sentence"
url: "https://reddit.com/r/LocalLLaMA/comments/1xq9yjf/released_an_opensource_eou_detection_model"
link: "https://reddit.com/r/LocalLLaMA/comments/1xq9yjf/released_an_opensource_eou_detection_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T16:08:45Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["martian7r"]
language: "en"
summary: "Voice agents serving Indic-language users cut callers off constantly Indic languages put the verb last, so \"aapko kal phone…\" pauses sound finished to a VAD, and the bot jumps in before \"kar dunga\" lands. VAD hears silence, not meaning Released an end-of-turn (EOU) detector fine-tuned from Qwen2.5-0.5B scores the live transcript and predicts whether the caller has finished • Languages: English,…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 145
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xq9yjf/released_an_opensource_eou_detection_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Released an open-source EOU detection model covering English + 8 Indic languages voice agents stop cutting callers off mid-sentence

Reddit · martian7r · 2026-11-07

Voice agents serving Indic-language users cut callers off constantly Indic languages put the verb last, so "aapko kal phone…" pauses sound finished to a VAD, and the bot jumps in before "kar dunga" lands. VAD hears silence, not meaning Released an end-of-turn (EOU) detector fine-tuned from Qwen2.5-0.5B scores the live transcript and predicts whether the caller has finished • Languages: English, Hinglish, Hindi, Telugu, Tamil, Marathi, Bengali, Gujarati, Punjabi • CPU-only ONNX Runtime (~2GB, fp32) fully local, no cloud inference • Text-only needs your STT; drop-in for LiveKit Agents, same interface as their text turn detector • Proven live on LiveKit Cloud: held mid-request pauses and committed complete requests 91.3% TPR on our held-out validation set, calibrated to ~10% false cuts on incomplete turns AUC 0.967. On LiveKit's official real-speech harness (Hindi): 85.3% detection at the same budget. Model + plugin: https://huggingface.co/tarun7r/indic-turn-detector Apache-2.0. Feedback welcome!
