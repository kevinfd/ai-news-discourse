---
id: "61ebe50c8af5bcbd"
title: "Marimba: a System One model for speech [R]"
url: "https://huggingface.co/charcot-ai/marimba/resolve/main/assets/marimba-demo-60s.mp4"
link: "https://huggingface.co/charcot-ai/marimba/resolve/main/assets/marimba-demo-60s.mp4"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-15T16:30:09Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["solanotodesch"]
language: "en"
summary: "Marimba is like Jev, but for audio. I built it to be fast and lightweight, and to return typed decisions about speech: yes/no, a choice, or a score. It runs on a frozen Qwen3-ASR-0.6B. Word and language questions use zero-shot scores from the ASR decoder's hypotheses, followed by calibration. Small readouts on the frozen encoder handle voice activity, turn endings, speaker changes and speaker…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "summary"
word_count: 91
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xwzsm4/marimba_a_system_one_model_for_speech_r/"
score: null
comments: null
community: "r/MachineLearning"
---

# Marimba: a System One model for speech [R]

Hugging Face · solanotodesch · 2026-11-15

Marimba is like Jev, but for audio. I built it to be fast and lightweight, and to return typed decisions about speech: yes/no, a choice, or a score. It runs on a frozen Qwen3-ASR-0.6B. Word and language questions use zero-shot scores from the ASR decoder's hypotheses, followed by calibration. Small readouts on the frozen encoder handle voice activity, turn endings, speaker changes and speaker count. Watch the 60 s demo · Try it live Open weights (Apache-2.0), pip install marimba-audio . Paper on arXiv this week. Code · Model · Benchmark
