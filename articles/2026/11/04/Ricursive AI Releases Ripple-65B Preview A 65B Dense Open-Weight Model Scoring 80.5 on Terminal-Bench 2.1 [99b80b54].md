---
id: "99b80b54a9e89fc4"
title: "Ricursive AI Releases Ripple-65B Preview: A 65B Dense Open-Weight Model Scoring 80.5 on Terminal-Bench 2.1"
url: "https://marktechpost.com/2026/11/04/ricursive-ripple-65b-preview-open-weight-model"
link: "https://marktechpost.com/2026/11/04/ricursive-ripple-65b-preview-open-weight-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-04T21:01:06Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Ricursive Intelligence just released Ripple-65B Preview . Ripple-65B Preview is a 65B dense open-weight model from Ricursive, pretrained from scratch for agentic coding. It is a general-purpose variant of the proprietary model behind Ricursive’s AI chip design platform. The main claim: 80.52 on Terminal-Bench 2.1 , the top self-reported score among US open-weight models. Every MoE rival it beats…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Meta", "Nvidia", "Hugging Face", "Thinking Machines"]
topics: ["models & research", "chips & infrastructure", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 912
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Ricursive AI Releases Ripple-65B Preview: A 65B Dense Open-Weight Model Scoring 80.5 on Terminal-Bench 2.1

MarkTechPost · Asif Razzaq · 2026-11-04

Ricursive Intelligence just released Ripple-65B Preview . Ripple-65B Preview is a 65B dense open-weight model from Ricursive, pretrained from scratch for agentic coding. It is a general-purpose variant of the proprietary model behind Ricursive’s AI chip design platform. The main claim: 80.52 on Terminal-Bench 2.1 , the top self-reported score among US open-weight models. Every MoE rival it beats on that test carries 501B to 975B total parameters. 

 TL;DR 

 Size: 65B dense (65B active), pretrained on 12T tokens, up to 1M context. 

 Runs on: BF16 on datacenter GPUs (250 tok/s on 2x B200). Experimental NVFP4 build targets NVIDIA DGX Spark. 

 Performance: Frontier-level agentic coding for its size; trails larger MoE models on knowledge and science coding. 

 Best: Terminal-Bench 2.1, 80.5 (self-reported). 

 Worst: SciCode, 39.4, lowest of the 5 models in Ricursive’s own table. 

 What is Ripple-65B Preview? 

 The release includes 3 checkpoints : an instruction-tuned BF16 model, an NVFP4 version , and a BF16 base model . All ship under Apache 2.0. Pretraining used a text-only corpus, mostly English and code, at 8K sequence length. 

 Ricursive team states that the full R&D cost was $32M . That figure covers ladder experiments, data mixing, evals, synthetic data and the final runs. Ricursive team estimates that it is one-tenth the cost of the prior open-weight agentic coding leader. 

 How does the architecture work? 

 Ricursive chose a dense Transformer over Mixture-of-Experts to reduce infrastructure complexity. Training held 40% MFU with simple sharding, no custom kernels and no quantization. 

 The model is thin and deep: a d_model of 5120 across 80 layers. It moves from Olmo 3’s Llama-like layout to a Gemma 3N-like design for stability. Key choices: 

 Overprovisioned attention heads for reasoning, offset by more sliding-window layers and smaller windows. 

 Gated attention , global NoPE and value residuals . 

 FFN activation clipping , a technique also used in gpt-oss . 

 Ricursive team built the recipe through laddering experiments starting from Olmo 3’s ladder . It rejected changes that failed to hold at 4B scale, such as 2-stream mHC. The technical post reports a 16x code compute-efficiency gain at 4B scale. 

 How was it post-trained? 

 Post-training ran midtraining, long context, SFT, long-context SFT and mixed RL. Long-context stages trained at 2M sequence length. Ricursive bought no post-training data and built its own synthetic pipelines. 

 The RL recipe combines truncated importance sampling , score centering and a linear length penalty . Ripple hit 80.5 on Terminal-Bench 2.1 with 1.4M rollouts. Ricursive puts that at roughly 70x fewer than Beam, which reported over 100M rollouts . 

 How does Ripple-65B compare on benchmarks? 

 Ricursive team ran missing evals in-house using OpenCode, and Terminus 2 for SWE-bench Pro v2.0 Hard and DeepSWE 1.1. Scores below are Ricursive’s presented data. 

 Terminal-Bench 2.1: 80.5, vs Beam 80.1 , Muse Spark Open 76.4 , Inkling 63.8 , Nemotron 3 Ultra 56.4 . 

 SWE-bench Pro v2.0 Hard: 79.1, the top score in Ricursive’s table. 

 SWE-bench Verified: 76.5, below Beam and Inkling. 

 Math: 98.3 on AIME 2025 and 90.5 on HMMT Feb 2026. 

 Weak spots: SciCode 39.4, DeepSWE 1.1 44.3, MCP Atlas 71.67, GPQA Diamond 85.2. 

 Ricursive team also reran Terminal-Bench 2.1 with the official Terminus 2 harness at 128K. Most rivals dropped there; Beam fell to 70.8. Muse Spark Open rose to 78.7, still below Ripple’s 80.5. 

&&&

 Comparison table 

 Feature Ripple-65B Preview Reflection Beam Meta Muse Spark Open Thinking Machines Inkling NVIDIA Nemotron 3 Ultra Architecture Dense MoE MoE MoE Hybrid Mamba-2 LatentMoE Total params 65B 501B 816B 975B 550B Active params 65B 23B 42B 41B 55B Pretraining tokens 12T 23.8T Not disclosed 45T (per Ricursive table) ~20T Context Up to 1M 1M (midtraining) 1M 1M Up to 1M License Apache 2.0 Apache 2.0 Muse Model License Apache 2.0 OpenMDW-1.1 Input modality Text Text Text, image, video, audio Text, image, audio Text Self-hosting floor DGX Spark class (NVFP4) Not disclosed 700GB VRAM (NVFP4) 600GB VRAM (NVFP4) 8x B200 or 16x H100 Terminal-Bench 2.1 80.5 80.1 76.4 63.8 56.4 SWE-bench Verified 76.5 80.9 Not disclosed by Meta 77.6 70.7 GPQA Diamond 85.2 Not disclosed in blog 89.0 87.2 87.0 

 Ripple scores from the Ricursive model card . Competitor scores from each vendor’s own source. All self-reported. 

 Where can developers run it? 

 Weights are on Hugging Face . Ricursive lists Together AI , GMI Cloud and OpenRouter at launch, with Fireworks later. Together AI’s page currently marks the model as coming soon. 

 On datacenter GPUs, the model reaches 250 tok/s on 2x B200 at batch 8, before quantization. The experimental NVFP4 checkpoint quantizes MLP layers and keeps attention in BF16. Ricursive team positions it for local devices like NVIDIA DGX Spark. A DFlash2 variant is also listed. 

 Key Takeaways 

 65B dense, 12T tokens, 1M context, Apache 2.0. 

 80.5 on Terminal-Bench 2.1, top among US open weights. 

 $32M full R&D, 1.4M RL rollouts. 

 NVFP4 build targets DGX Spark-class local hardware. 

 Trails larger MoE rivals on SciCode, DeepSWE and MCP Atlas. 

 Check out the the launch blog , the model card and the NVFP4 checkpoint . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Ricursive AI Releases Ripple-65B Preview: A 65B Dense Open-Weight Model Scoring 80.5 on Terminal-Bench 2.1 appeared first on MarkTechPost .
