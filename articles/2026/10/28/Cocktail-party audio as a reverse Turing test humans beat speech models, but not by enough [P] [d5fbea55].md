---
id: "d5fbea558500cb70"
title: "Cocktail-party audio as a reverse Turing test: humans beat speech models, but not by enough [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xhuado/cocktailparty_audio_as_a_reverse_turing_test"
link: "https://reddit.com/r/MachineLearning/comments/1xhuado/cocktailparty_audio_as_a_reverse_turing_test"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T17:17:59Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["cloud_kj"]
language: "en"
summary: "Hello - I wanted to share a small project I worked on test whether picking one voice out of background chatter could separate humans from machines, in the spirit of an audio CAPTCHA. Setup 40 synthetic clips: one target sentence read by a synthetic voice, mixed over multiple background voices reading random short fragments (staggered starts, 4 dB attenuation) 146 human transcriptions from 18…"
tags: ["r/MachineLearning"]
orgs: ["Google"]
topics: ["models & research"]
content_source: "post"
word_count: 306
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xhuado/cocktailparty_audio_as_a_reverse_turing_test/"
score: null
comments: null
community: "r/MachineLearning"
---

# Cocktail-party audio as a reverse Turing test: humans beat speech models, but not by enough [P]

Reddit · cloud_kj · 2026-10-28

Hello - I wanted to share a small project I worked on test whether picking one voice out of background chatter could separate humans from machines, in the spirit of an audio CAPTCHA. Setup 40 synthetic clips: one target sentence read by a synthetic voice, mixed over multiple background voices reading random short fragments (staggered starts, 4 dB attenuation) 146 human transcriptions from 18 sessions, unlimited replays allowed 8 model configurations, one pass per clip: Whisper base/small, Vosk, Wav2Vec2, Qwen3-ASR 0.6B, Parakeet CTC 0.6B, and Gemini 3.8 Flash with a naive prompt and with an instruction to focus on the main speaker Primary metric: word accuracy (1 − WER, floored at 0); default passing threshold = word accuracy ≥ 0.5 TL;DR: humans are better at the task but the gap is too narrow to be a reliable CAPTCHA Results Humans 0.71 mean word accuracy vs. 0.54 for instructed Gemini (and 0.55 for Qwen3-ASR) Pass rate: 77% humans vs. 55% for Gemini Note: no threshold from ≥0.5 to ≥0.9 gets near my initial rough mental target: humans > 80% and machines < 20% Paired same-clip gap vs. Gemini: +0.13 (95% CI +0.03 to +0.23, session-level bootstrap); AUC 0.62 The instruction prompt alone lifted Gemini from 0.34 to 0.54 Replays didn't measurably help humans; people replayed the clips that were hardest for the models too Misses rise toward the end of the sentence for humans and every model alike Limitations: small sample (18 sessions, mostly native English speakers), a single synthetic setup, no source separation, and no large or commercial ASR beyond Gemini. I dusted off my dormant blog and did a write-up ( https://www.kelvinjiang.com/2026/10/can-machines-follow-voice-through-crowded-room.html ) and also shared the code, data, and audio corpus: https://github.com/cloudkj/crosstalk Feedback on the method is very welcome, especially ideas for audio that stays easy for people but is consistently hard for models!
