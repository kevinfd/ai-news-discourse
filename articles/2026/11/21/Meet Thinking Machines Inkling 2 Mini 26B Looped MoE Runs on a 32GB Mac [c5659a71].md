---
id: "c5659a71aeab19ae"
title: "Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac"
url: "https://marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer"
link: "https://marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-21T12:13:50Z"
published_date: "2026-11-21"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Thinking Machines Lab has released Inkling 2 Mini , an open-weight looped transformer with 26.4B total parameters. The model reuses its middle layers 3 times per token instead of adding more weights. That keeps the checkpoint near 20GB, small enough for a 32GB Mac or 1 NVIDIA DGX Spark. For developers, Inkling 2 Mini is a local option for agentic coding, tool use and document work. It ships…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Machine Learning", "New Releases", "Open Source"]
orgs: ["Thinking Machines", "Nvidia", "Alibaba", "Apple", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 1052
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac

MarkTechPost · Asif Razzaq · 2026-11-21

Thinking Machines Lab has released Inkling 2 Mini , an open-weight looped transformer with 26.4B total parameters. The model reuses its middle layers 3 times per token instead of adding more weights. That keeps the checkpoint near 20GB, small enough for a 32GB Mac or 1 NVIDIA DGX Spark. For developers, Inkling 2 Mini is a local option for agentic coding, tool use and document work. It ships under Apache 2.0 on Hugging Face , with hosted inference and fine-tuning on Tinker . 

 TL;DR 

 Size: 26.4B total, 3.4B active (5.4B effective per token with looping), up to 1M-token context. 

 Runs on: Apple silicon with 32GB+ memory, 1 NVIDIA DGX Spark, or GPUs with 32GB+ VRAM. GGUF builds via Unsloth and llama.cpp. 

 Performance: 20.1 on the Artificial Analysis Index, tied with Qwen3.8-27B (self-reported). 

 Best: 79.2% on SWE-bench Verified (bash only). 

 Worst: 15.2% on HLE-Diamond and 50.0% on MultiChallenge. 

 Bottom line: Best: strong agentic coding from a 20GB checkpoint. Worst: weaker knowledge recall and multi-turn instruction following. 

 What is Inkling 2 Mini? 

 Inkling 2 Mini is a sparse Mixture-of-Experts model from Thinking Machines that loops its middle layers. It accepts text and images and returns text only. 

 It follows Inkling 2 Small, a 594B-parameter model released on November 5. 

 How does the looped transformer work? 

 The model stores 24 layers, grouped into 4 blocks of 6. The first and last blocks run once. The 2 middle blocks run 3 times with shared weights. That gives 48 layer applications per token from 24 layers of weights. 

 Each pass after the first receives a “message” from the previous pass. Thinking Machines carries it with Attention Residuals and a learned gate. Feed-forward layers use 128 experts, with 8 routed per token. 

 Looping the middle layers gave a 1.51x to 1.91x compute-equivalent gain. Looping the last layers gave only 1.24x to 1.36x. The middle-loop variant won 27 of 28 evaluations. 

 Looping costs training compute but saves inference. An unlooped baseline used 7.5% less training compute. It needed 140% more inference compute to match the looped model’s loss on 512k-token agentic traces. 

 How was Inkling 2 Mini trained? 

 Training began with 384 experts per layer, with 8 active per token. At midtraining, the team pruned two-thirds of them and kept the 128 most-used experts. A 1T-token distillation run from a larger internal Inkling model then healed the pruned model. Post-training used SFT, then RL over 2.2T tokens and 2,000 steps, plus on-policy distillation. 

 Expert layers are trained and deployed in NVFP4. The last 4 layers use MXFP8. Thinking Machines says this removes quantization conversion loss. A research variant, TML-d24-varloop-research , trains with 1 to 5 passes. 

 How does Inkling 2 Mini perform on benchmarks? 

 All Inkling scores below are self-reported by Thinking Machines. Coding is the strongest area. Inkling 2 Mini scores 79.2% on SWE-bench Verified (bash only) and 77.9% on SWE-bench Pro v2 (Hard). It reaches 48.2% on DeepSWE v1.1, where Qwen’s own card lists Qwen3.8-27B at 42.2%. On Terminal Bench v2.1 it scores 71.6%, behind Qwen3.8-27B at 73.0%. 

 Agentic search also holds up: 79.0% on BrowseComp with compaction and 82.7% on MCP Atlas. For documents and vision, it posts 92.8% on OmniDocBench v1.6 and 74.9% on MMMU Pro. On reasoning, it scores 86.6% on GPQA Diamond and 49.3% on ARC-AGI-2. 

 Efficiency is the headline claim. On Stanford’s Intelligence per Watt metric, Thinking Machines reports 0.703 on a DGX Spark. It lists Qwen3.6-35B-A3B at 0.430 and Gemma-4-26B-A4B at 0.159. 

&&

 How does Inkling 2 Mini compare with Qwen and Gemma? 

 Feature Inkling 2 Mini ( card ) Qwen3.8-27B ( card ) Qwen3.6-35B-A3B ( card ) Gemma 4 26B A4B ( card ) Architecture Looped MoE Dense MoE MoE Total params 26.4B 27B 35B 25.2B Active params 3.4B (5.4B effective) 27B (dense) 3B 3.8B Context Up to 1M 262,144 native, up to 1M 262,144 native, up to 1,010,000 256K License Apache 2.0 Apache 2.0 Apache 2.0 Apache 2.0 Input Text, image Text, image, video Text, image Text, image Hardware listed ~20GB; 32GB Mac or DGX Spark Not disclosed Not disclosed Not disclosed GPQA Diamond 86.6% 89.2 86.0 82.3% Terminal Bench 2.1 71.6% 73.0 Not reported Not reported SWE-bench Verified 79.2% (bash only) Not reported 73.4 Not reported DeepSWE 1.1 48.2% 42.2 Not reported Not reported Hosted access Tinker Qwen Cloud Not disclosed Not disclosed 

 Each column uses the vendor’s own model card. Harnesses and settings differ, so treat cross-vendor gaps as directional. 

 What hardware do you need to run Inkling 2 Mini? 

 The checkpoint is about 20GB in Safetensors. Thinking Machines lists 3 supported setups: 1 NVIDIA DGX Spark, Apple silicon with 32GB+ memory, and other GPUs with 32GB+ VRAM. Quantized GGUF builds are available through Unsloth and llama.cpp. 

 Serving support covers Transformers, vLLM, SGLang, Ollama, NVIDIA Dynamo and TokenSpeed. Tinker pricing for Mini is not disclosed in the launch materials. 

 A vLLM quick start takes 1 command: vllm serve "thinkingmachines/Inkling-2-Mini" . 

 Where does Inkling 2 Mini fall short? 

 Knowledge depends mostly on total parameters, and looping did not help knowledge benchmarks. Inkling 2 Mini scores -8.6 on AA-Omniscience, with a 63.4% non-hallucination rate. 

 It is not the best small model for multi-turn chat or constraint-heavy prompts. It scores 50.0% on MultiChallenge and 33.4% on ComplexConstraints v1.1. It also trails larger models on HLE-Diamond (15.2%) and CritPt v2. 

 Key Takeaways 

 Inkling 2 Mini loops 24 stored layers into 48 layer passes per token. 

 26.4B total, 3.4B active, ~20GB, Apache 2.0, up to 1M context. 

 Runs on a 32GB Mac or 1 DGX Spark via Ollama, vLLM or llama.cpp. 

 Scores 79.2% on SWE-bench Verified and ties Qwen3.8-27B at 20.1 AA Index. 

 Weak spots: knowledge recall, multi-turn chat and constraint-heavy prompts. 

 Check out the technical blog , model card , model weights and Tinker Playground . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac appeared first on MarkTechPost .
