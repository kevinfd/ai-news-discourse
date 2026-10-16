---
id: "21319273819e7a0f"
title: "Fish Audio Releases Drama 3, a 35B Open-Weight MoE Text-to-Speech Model"
url: "https://marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model"
link: "https://marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T22:52:17Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "This week, Fish Audio released Fish Audio Drama 3 . Drama 3 is a text-to-speech model from Fish Audio that takes plain-language acting direction. It is a 35B mixture-of-experts model with about 3B parameters active per token. The weights are on Hugging Face , and the model is also live in the Fish Audio API . For developers, it is a self-hostable option for scripted dialogue, audiobooks and…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "New Releases", "Staff"]
orgs: ["Nvidia", "Hugging Face", "Apple", "AMD", "Alibaba"]
topics: ["models & research", "chips & infrastructure", "products & launches", "business & funding"]
content_source: "summary"
word_count: 993
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Fish Audio Releases Drama 3, a 35B Open-Weight MoE Text-to-Speech Model

MarkTechPost · Asif Razzaq · 2026-10-14

This week, Fish Audio released Fish Audio Drama 3 . Drama 3 is a text-to-speech model from Fish Audio that takes plain-language acting direction. It is a 35B mixture-of-experts model with about 3B parameters active per token. The weights are on Hugging Face , and the model is also live in the Fish Audio API . For developers, it is a self-hostable option for scripted dialogue, audiobooks and dubbing. 

 TL;DR 

 Size: 35B total parameters, about 3B active per token (8 of 256 experts plus 1 shared). Context length: Not disclosed. 

 Runs on: 1 NVIDIA GPU with at least 48 GB in FP8. No CPU, Apple MPS or AMD ROCm. Official benchmarks use 1 H200. 

 Performance: Fish Audio’s highest-scoring model on Artificial Analysis, but still behind several closed APIs on quality Elo. 

 Best: 95.9% on brands, places and technical terms in Artificial Analysis Pronunciation Robustness. 

 Worst: 86.3% on exact sequences (codes, paths, emails), its weakest pronunciation category. 

 Bottom line: 
 
 Best: directable, multi-speaker speech with open weights. 

 Worst: 48 GB GPU floor and a revenue-capped license. 

 What is Fish Audio Drama 3? 

 Drama 3 turns a script along with bracketed directions into acted speech. Writers place cues like [barely holding it together] before a line. Paired tags such as <whisper> change only the enclosed words, per the Drama 3 docs . Directions can be written in any language, independent of the spoken line. 

 The model supports 83 languages . Speaker tags <|speaker:0|> to <|speaker:15|> allow up to 16 characters in 1 request. The API takes 1 voice ID per speaker, so a full scene renders in a single call. 

 How does the Drama 3 architecture work? 

 According to the launch post , the backbone starts from the Qwen3.5-35B-A3B language model. It has 40 layers, grouped as 3 Gated DeltaNet layers per 1 gated full-attention layer. Only 1 layer in 4 keeps a KV cache. DeltaNet layers store history in a constant-size state instead. 

 A new Codebook-MTP decoder replaces the per-frame Fast AR decoder used in S2 . It has 4 shared layers feeding 9 layers, 1 per acoustic codebook. Only codebooks 0 and 1 feed back into the backbone; S2 fed back all 10. 

 The audio tokenizer is unchanged from S2. It is built on the Descript Audio Codec and outputs 44.1 kHz audio. It runs at about 21.5 frames per second. 

 Training ran 3 pre-training stages, then instruction tuning, then reinforcement learning. RL used GRPO without a KL penalty and a single learned human-preference reward model. 

 &&

 How does Drama 3 perform on benchmarks? 

 Fish Audio reports Drama 3 at 93.2% overall on Artificial Analysis Pronunciation Robustness , ranked #1. Its predecessor S2.1 Pro scored 88.1%. Human listeners judge hard English words across 4 categories: 

 Brands, places, technical terms: 95.9% (S2.1 Pro: 87.3%) 

 Context-dependent readings: 95.3% (86.1%) 

 Shorthand such as numbers, dates and units: 93.6% (92.7%) 

 Exact sequences such as codes, paths and emails: 86.3% (79.4%) 

 This benchmark tests pronunciation, not emotional delivery. Fish Audio describes emotive quality only qualitatively. On the Artificial Analysis quality leaderboard , ‘Drama 3 Preview’ holds an Elo of 1242. That beats S2.1 Pro at 1190 but trails Eleven v4 Turbo at 1328. 

 What hardware does Drama 3 need? 

 The Fish Speech install guide lists at least 48 GB of NVIDIA GPU memory in FP8. CPU, Apple MPS and AMD ROCm are not supported. MoE experts ship in FP8, with the remaining weights in bf16. 

 The model card reports streaming results on 1 H200. At 1 stream, median time to first audio is 88.9 ms with a real-time factor of 0.131. At 16 streams, throughput reaches 927.6 frames per second. Serving runs through SGLang-Omni , whose fused kernels are validated only on Hopper GPUs. 

 How do you access Drama 3, and what does it cost? 

 In the hosted API, set the model header to drama-3 on POST /v1/tts . The docs warn that a missing or misspelled header silently falls back to s2.1-pro . List price is $50 per 1M characters. A $10 launch price runs until November 12, 2026, per the launch post . 

 The weights use the Fish Audio Community License v1.0 . Research and non-commercial use are free. Commercial use is free under USD 500,000 in annual revenue. Hosting Drama 3 as a third-party API needs a separate license. Products must display ‘Built with Fish Audio.’ Cloning a real voice without consent is prohibited. 

 Drama 3 vs closest competitors 

 Feature Fish Audio Drama 3 Fish Audio S2 Pro ElevenLabs Eleven v4 Turbo Qwen-Audio-3.0-TTS-Plus Total size 35B (MoE) 5B (4B Slow AR + 400M Fast AR) Not disclosed Not disclosed Active parameters ~3B Not MoE Not disclosed Not disclosed Weights Open, Community License v1.0 Open, Research License API and apps API (Model Studio) Languages 83 80+ 90+ 8 listed, plus dialects Self-host hardware 48 GB+ NVIDIA, FP8 24 GB+ NVIDIA, or CPU Hosted only Hosted only Latency 88.9 ms TTFA p50, H200 ~100 ms TTFA, H200 ~150 ms median time to first speech Not disclosed AA quality Elo ( source ) 1242 (Preview) 1116 1328 1266 API price per 1M chars $50 list, $10 to Nov 12 $15 $40 $20, Singapore 

 Key Takeaways 

 Drama 3 is a 35B MoE TTS model with ~3B active parameters. 

 Plain-language direction and 16 speakers per request target scripted audio. 

 93.2% on AA Pronunciation Robustness; exact sequences lag at 86.3%. 

 Self-hosting needs 48 GB+ of NVIDIA memory in FP8. 

 Free commercial use stops at USD 500,000 in annual revenue. 

 Check out the weights on Hugging Face , the technical report , the GitHub repo and the launch post . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Fish Audio Releases Drama 3, a 35B Open-Weight MoE Text-to-Speech Model appeared first on MarkTechPost .
