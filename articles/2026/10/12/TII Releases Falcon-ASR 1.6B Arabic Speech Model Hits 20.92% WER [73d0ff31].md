---
id: "73d0ff31d60974a6"
title: "TII Releases Falcon-ASR: 1.6B Arabic Speech Model Hits 20.92% WER"
url: "https://marktechpost.com/2026/10/11/tii-falcon-asr-arabic-speech-recognition"
link: "https://marktechpost.com/2026/10/11/tii-falcon-asr-arabic-speech-recognition"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-12T03:16:09Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "The Technology Innovation Institute (TII) in Abu Dhabi has released Falcon-ASR , a 1.6B parameter Arabic speech recognition model. It focuses on the Emirati dialect and also transcribes English, French, Spanish and Portuguese. In TII’s evaluation, Falcon-ASR posts a 20.92% average word error rate (WER) across 6 Arabic test sets. That beats the best published entry in TII’s leaderboard snapshot…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Small Language Model"]
orgs: ["Cohere", "Alibaba", "Hugging Face", "China"]
topics: ["models & research", "chips & infrastructure", "business & funding", "agents & coding"]
content_source: "summary"
word_count: 981
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# TII Releases Falcon-ASR: 1.6B Arabic Speech Model Hits 20.92% WER

MarkTechPost · Asif Razzaq · 2026-10-12

The Technology Innovation Institute (TII) in Abu Dhabi has released Falcon-ASR , a 1.6B parameter Arabic speech recognition model. It focuses on the Emirati dialect and also transcribes English, French, Spanish and Portuguese. In TII’s evaluation, Falcon-ASR posts a 20.92% average word error rate (WER) across 6 Arabic test sets. That beats the best published entry in TII’s leaderboard snapshot by 2.25 points. For developers building Arabic voice products, the catch is access: today it runs only as a hosted demo. 

 TL;DR 

 Size: 1.6B parameters. Max audio context: Not disclosed (the demo accepts clips up to 60 seconds and 20 MB). 

 Runs on: Not disclosed. No weights or quantized variants are published. Access is a Hugging Face demo, with API and native apps planned. 

 Performance: Lowest Arabic and Emirati WER in TII’s own comparisons, with solid English results. 

 Best: 20.92% average Arabic WER, 2.25 points below Audar-ASR-V1-Turbo (23.17%). 

 Worst: 11.86% WER on Earnings-22, its weakest English test set. 

 Bottom line (best): a compact 1.6B model leading larger Arabic systems in TII’s tests. 

 Bottom line (worst): no weights, no license, no API yet, and all scores are self-reported. 

 What is Falcon-ASR? 

 Falcon-ASR is a speech-to-text model from TII that converts spoken Arabic and 4 other languages into text. All 5 languages share one set of weights. The model needs no language flag and outputs text in the language spoken. It also returns word-level timestamps , linking each word to its position in the audio. This is important for subtitling, searchable recordings and meeting notes. 

 How does Falcon-ASR handle Arabic dialects? 

 Dialectal Arabic has far fewer transcribed resources than Modern Standard Arabic (MSA). TII trained Falcon-ASR on Emirati, MSA, other Gulf and Arabic dialects, and English. The objective is everyday speech, including dialect forms and language switching. 

 Training audio was augmented with background noise, overlapping speech, music, room reverberation and telephony effects. Speed and pitch were varied too. The same treatment was applied to Emirati recordings. 

 The model builds on TII’s Falcon3-Audio work . That research describes audio-language models built on instruction-tuned LLMs and Whisper encoders, trained on under 30K hours of public audio. Our editorial and technical team at Marktechpost could not find any published Falcon-ASR’s exact architecture or training data size. 

 How does Falcon-ASR score on Arabic benchmarks? 

 TII followed the protocol of the Open Universal Arabic ASR Leaderboard , run by the ELM Research Center. It ranks systems by equal-weight average WER over 6 test sets. TII used the leaderboard’s pinned manifests. Competitor numbers are published leaderboard averages checked on 30 September 2026. 

 Model Params Avg WER (%) Avg CER (%) Falcon-ASR 1.6B 20.92 8.79 Audar-ASR-V1-Turbo 2.35B 23.17 9.23 Cohere Transcribe Arabic (07-2026) 2.0B 25.87 11.80 omniASR LLM 7B 7.0B 28.32 12.52 

 Lower is better. Note that Falcon-ASR’s figure is TII’s own run, not a leaderboard entry. The Audar model card lists its own average CER as 9.20%. 

 How does Falcon-ASR perform on Emirati speech? 

 TII built an internal Emirati and Gulf test set from held-out recordings with human-validated transcripts. It complements the UAE subset of the public Casablanca dataset. 

 Model Params WER (%) CER (%) Falcon-ASR 1.6B 22.73 10.19 Qwen3-Omni-30B-A3B-Instruct 30B (3B active) 26.80 12.72 Audar-ASR-V1-Turbo 2.35B 27.89 13.75 Cohere Transcribe Arabic 2.0B 31.05 18.07 Qwen3-ASR-1.7B 2.0B 31.52 13.35 Audar-ASR-V1-Flash 0.78B 32.87 15.36 

 Falcon-ASR leads by 4.07 WER points over Qwen3-Omni. This test set is private, so it cannot be reproduced. Audar reports 19.4% WER on a different Emirati set (Mixat), so the numbers are not directly comparable. 

 How good is Falcon-ASR at English? 

 On the 7 English test sets used by the Hugging Face Open ASR Leaderboard, TII reports a 5.74% mean WER. Per-set scores range from 1.75% on LibriSpeech clean to 11.86% on Earnings-22. For context, Qwen3-ASR-1.7B lists 5.76% mean WER on that leaderboard. French, Spanish and Portuguese are supported, but TII published no scores for them. 

 Comparison: Falcon-ASR vs closest Arabic ASR models 

 Feature Falcon-ASR Audar-ASR-V1-Turbo Cohere Transcribe Arabic Qwen3-ASR-1.7B Organization TII (UAE) AudarAI Cohere Alibaba Qwen Parameters 1.6B 2.35B 2B 1.7B (2B on HF card) Architecture Builds on Falcon3-Audio Audio encoder + LM decoder FastConformer encoder + Transformer decoder Built on Qwen3-Omni License Not disclosed AudarAI Community License v1.0 Apache 2.0 Apache 2.0 Open weights No Yes (BF16, GGUF, W4A16) Yes Yes Languages 5 (Arabic incl. Emirati, EN, FR, ES, PT) 30 (Arabic-first) Arabic, English 30 languages + 22 Chinese dialects Arabic avg WER (6 sets) 20.92 (TII eval) 23.17 25.87 33.36 ( leaderboard ) Arabic avg CER 8.79 (TII eval) 9.20 11.80 12.33 TII Emirati WER 22.73 27.89 31.05 31.52 English mean WER (Open ASR sets) 5.74 (TII eval) Not disclosed Not disclosed 5.76 Timestamps Word-level Not disclosed Not disclosed Via Qwen3-ForcedAligner-0.6B Runs on Not disclosed (hosted demo) CPU, GPU, edge via GGUF; W4A16 on 12 GB+ GPU Not disclosed GPU via Transformers or vLLM Access HF demo; API planned Weights + Audar API Weights + Cohere API Weights + DashScope API 

 Sources: Falcon-ASR figures from TII’s blog . Audar, Cohere and Qwen leaderboard figures from the ELM leaderboard as reproduced on the Audar card. Emirati WER for all models is from TII’s internal evaluation. 

&&&

 Key Takeaways 

 Falcon-ASR is a 1.6B Arabic-first speech model from TII with an Emirati focus. 

 It reports 20.92% average Arabic WER, 2.25 points ahead of Audar-ASR-V1-Turbo. 

 On TII’s Emirati set it beats a 30B Qwen3-Omni by 4.07 WER points. 

 1 set of weights covers 5 languages, with word-level timestamps. 

 No weights, license or API yet: test it via the 60-second demo. 

 Check out the Falcon-ASR blog , the Falcon3-Audio paper and try the demo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post TII Releases Falcon-ASR: 1.6B Arabic Speech Model Hits 20.92% WER appeared first on MarkTechPost .
