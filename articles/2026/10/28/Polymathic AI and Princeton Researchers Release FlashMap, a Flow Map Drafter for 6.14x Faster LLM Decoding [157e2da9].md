---
id: "157e2da996ea8437"
title: "Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter for 6.14x Faster LLM Decoding"
url: "https://marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding"
link: "https://marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T08:18:03Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Researchers from Polymathic AI, Princeton University, USC ISI, NYU and the Flatiron Institute have released FlashMap . FlashMap speculative decoding replaces the discrete diffusion drafter with a continuous flow map. It drafts a full 16-token block in 1 forward pass. Tokens in that block stay consistent with each other. On Qwen3-8B, the research team reports up to 6.14x lossless speedup on…"
tags: ["AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Hugging Face", "Nvidia", "DeepSeek"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 977
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter for 6.14x Faster LLM Decoding

MarkTechPost · Asif Razzaq · 2026-10-28

Researchers from Polymathic AI, Princeton University, USC ISI, NYU and the Flatiron Institute have released FlashMap . FlashMap speculative decoding replaces the discrete diffusion drafter with a continuous flow map. It drafts a full 16-token block in 1 forward pass. Tokens in that block stay consistent with each other. On Qwen3-8B, the research team reports up to 6.14x lossless speedup on GSM8K. Drafter weights for Qwen3-8B and Qwen3-4B are on Hugging Face , with vLLM and SGLang plugins . 

 TL;DR 

 Size: 0.5B-parameter drafter (500M for Qwen3-8B, 475M for Qwen3-4B); drafts blocks of K = 16 tokens. 

 Runs on: the same GPU as the target model. Paper speedups use 1 NVIDIA H200 NVL at concurrency 1, in bf16. 

 Performance: fastest drafter tested on Qwen3-8B, about 7% above a retrained DFlash on average. 

 Best: 6.14x speedup on GSM8K at temperature 0 (acceptance length 7.69 tokens). 

 Worst: 2.28x speedup on Alpaca at temperature 1. On Qwen3-4B (temperature 0), it trails DFlash on 4 of 9 tasks. 

 What is FlashMap? 

 FlashMap is a speculative decoding drafter that maps Gaussian noise to a token block in 1 step. A small drafter proposes K tokens. The target model then checks all K in 1 parallel pass and keeps the longest matching prefix. Output stays exactly what the target would produce. 

 Speed depends on 2 things. How many drafted tokens get accepted, and how cheaply they were drafted. EAGLE-3 drafts autoregressively, so cost grows with block length. DFlash drafts the full block in 1 pass with block diffusion. 

 Why do diffusion drafters lose acceptance? 

 DFlash predicts each slot in the block independently. The research team calls this the factorized approximation. Picture a continuation that is “new york” or “san diego” with equal odds. An independent drafter proposes “new diego” or “san york” half the time. The target rejects those at slot 2. 

 FlashMap builds on Flow Map Language Models . Each noise sample maps to 1 full block. The noise picks the mode for every slot jointly. 

 How does FlashMap work? 

 The drafter is a 6-block diffusion transformer (DiT), with embedding dimension 2048 and 16 attention heads. It reads hidden states from target layers 1, 9, 17, 25 and 33. Embedding matrix and LM head are copied from the target and stay frozen. 

 Training runs in 2 stages: 

 Flow teacher: a continuous flow over one-hot token blocks, trained with cross-entropy. A time reparameterization handles Qwen3’s 151,936-token vocabulary. 

 Flow map student: semigroup distillation turns the flow into a 2-time denoiser. It jumps from noise to data in 1 step. 

 Both drafters train on 500K samples from Open-PerfectBlend . Total compute across all models and ablations was about 4,600 GPU hours on H200s. 

&&

 How does FlashMap compare on benchmarks? 

 The research team retrained EAGLE-3 and DFlash on the same data and settings. Tests cover 9 benchmarks across math, code and chat, at temperatures 0 and 1. 

 Speed: 1-step FlashMap is the fastest drafter on every Qwen3-8B task, at both temperatures. 

 Accuracy: 1-step FlashMap beats DFlash on acceptance length in 15 of 18 settings. It has about half the parameters. 

 Chat gains are largest: at temperature 0, gains over DFlash are 5.5% on math, 11.1% on chat. 

 2-step mode: acceptance length beats DFlash in 18 of 18 settings, by 10% on average. 

 EAGLE-3: at temperature 1, it has 9% higher acceptance length but runs 35% slower. 

 A shuffle test checks whether drafts use real inter-token structure. At 2 steps, FlashMap recovers most of the joint-structure gain of a 16-step teacher. At 1 step, it keeps only a small fraction. Drafting 4 noise samples as a tree raised speedup by 11% on average. 

 Comparison: FlashMap vs other speculative decoding drafters 

 Feature FlashMap DFlash EAGLE-3 DSpark Drafting style Continuous flow map, 1 or 2 passes Block diffusion, 1 pass Autoregressive, tree Semi-autoregressive Inter-token dependencies Yes, joint over block No, per-slot independent Yes, sequential Yes, lightweight sequential module Drafter size (Qwen3-8B) 500M 1B 302M (retrained, per FlashMap paper ) Not disclosed Headline claim (own source) Up to 6.1x Up to 6.17x on Qwen3-8B Up to 6.5x 60 to 85% faster per user vs MTP-1 Avg speedup, Qwen3-8B, T=0 (matched, FlashMap paper ) 4.36x 4.07x 2.55x Not tested GSM8K speedup, T=0 (matched) 6.14x 5.77x 3.20x Not tested Weights license Apache-2.0 MIT Apache-2.0 (code) Not disclosed Serving Transformers, vLLM, SGLang Transformers, vLLM, SGLang SGLang and others DeepSeek-V4 serving 

 Average speedups are computed by Marktechpost from Figure 1(c) of the FlashMap paper. Matched rows use the authors’ retrained baselines. 

 How do you deploy FlashMap? 

 The flashmap package needs only torch and transformers>=4.56 . Install it with uv pip install flashmap . A spec_generate call runs drafter and target together on 1 GPU. 

 For serving, the project page gives 2 paths: 

 vLLM 0.31: pass the drafter in --speculative-config with num_speculative_tokens set to 16. 

 SGLang 0.5.20: use --speculative-algorithm DSPARK with the FlashMap draft path. 

 Set num_steps=2 to trade some speed for higher acceptance. For sampling above temperature 0, vLLM needs "draft_sample_method": "probabilistic" . 

 Key Takeaways 

 FlashMap drafts 16 tokens jointly in 1 pass with a continuous flow map. 

 Up to 6.14x lossless speedup on Qwen3-8B, using a 0.5B drafter. 

 Faster than a retrained DFlash on all 9 Qwen3-8B benchmarks. 

 2-step mode keeps acceptance flat across the block. 

 Weights are Apache-2.0, code is MIT, with vLLM and SGLang plugins. 

 Check out the paper , project page , GitHub repo and model weights . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter for 6.14x Faster LLM Decoding appeared first on MarkTechPost .
