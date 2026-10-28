---
id: "930db33f0a3507f3"
title: "Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models"
url: "https://marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models"
link: "https://marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T21:08:02Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Liquid AI has released LFM3 , its new generation of Liquid Foundation Models. Liquid AI LFM3 is a family of 6 open-weight, 2B-class models built on one shared backbone. The family covers text, vision, audio, omni and decision tasks. Every model can be fine-tuned on a single GPU. Developers can then deploy on phones, laptops, private servers or the cloud. \n\n TL;DR \n\n Size: LFM3-1.7B has 1.73B…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "New Releases", "Staff", "Tech News", "Technology", "Uncategorized"]
orgs: ["Hugging Face", "Meta", "Nvidia"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 928
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models

MarkTechPost · Asif Razzaq · 2026-10-27

Liquid AI has released LFM3 , its new generation of Liquid Foundation Models. Liquid AI LFM3 is a family of 6 open-weight, 2B-class models built on one shared backbone. The family covers text, vision, audio, omni and decision tasks. Every model can be fine-tuned on a single GPU. Developers can then deploy on phones, laptops, private servers or the cloud. 

 TL;DR 

 Size: LFM3-1.7B has 1.73B parameters and a 256K context window . LFM3-VL-2B has 1.92B and 128K. LFM3-Omni-2B has 2.2B. 

 Runs on: about 1 GB of memory at 4-bit, so phones and laptops. GGUF, MLX, ONNX, FP8 and NVFP4 checkpoints ship. 

 Performance: LFM3-1.7B averages 49.37 across 29 benchmarks, above Qwen3.5-9B at 47.24 (Liquid’s own eval). 

 Best: IFEval 96.66, and AutomationBench 41.29 vs 15.10 for Qwen3.5-9B. 

 Worst: Humanity’s Last Exam (no tools) 7.17, and RULER 128K 65.56 vs 87.11 for Qwen3.5-9B. 

 What is Liquid AI LFM3? 

 LFM3 is a multimodal model family from Liquid AI that branches 6 models from 1 base. All of them start from LFM3-1.7B-Base . 

 The release includes: 

 LFM3-1.7B: a text model for local agents, post-trained for harnesses like Hermes Agent, Pi and OpenClaw. 

 LFM3-VL-2B: the first LFM vision model with video input, sampled at 2 fps. 

 LFM3-Audio-2B: speech in and out across 18 languages, with tool calling. 

 LFM3-Omni-2B: vision, audio and language in one model, answering in text or speech. 

 d1-2B and d1-Omni-2B: decision models that answer many questions in 1 forward pass. 

 How does the tri-hybrid architecture work? 

 The backbone mixes 3 operators across 24 layers . There are 13 gated short convolutions, 5 sliding-window attention layers and 6 global attention layers. The SWA window is 256 tokens. Convolution kernels grew from 3 to 7. 

 Liquid AI team found this mix with its hardware-in-the-loop architecture search. LFM2 was tuned on 1 phone and 1 laptop. LFM3 was tuned across 14 device and backend combinations. These include a Raspberry Pi 5 and the Qualcomm Hexagon NPU. 

 Other changes include head-wise sigmoid gates on attention, partial RoPE on global layers and sandwich norm. The base model saw 22T tokens. The last 3.5T tokens were agent-heavy mid-training, which also extended context to 256K. 

 Post-training ran in 4 stages. SFT on 1.75T tokens came first, then mixed RL. Next, 6 specialist teachers were distilled into 1 model, followed by agentic RL. 

 How does LFM3-1.7B perform on benchmarks? 

 Liquid AI reports that LFM3-1.7B beats LFM2.5-2.6B with 35% fewer parameters. The bigger story is the agent results. On WebArena-Verified it scores 38.42, against 28.94 for Qwen3.5-9B. On BFCL V4 it scores 71.39, against 62.83. 

 Size still wins on knowledge and agentic coding. GPQA Diamond is 63.37, versus 80.40 for Qwen3.5-9B. SWE-bench Verified is 43.40, versus 51.20. Search narrows the gap: Humanity’s Last Exam rises from 7.17 to 13.90 with tools. 

 &

 How do LFM3-1.7B and its rivals compare? 

 Feature LFM3-1.7B MiniCPM5-2B Qwen3.5-4B Gemma 4 E4B Parameters 1.73B 2.52B 4B LM (5B on Hub with vision) 4.5B effective (8B with embeddings) Architecture Conv + SWA + global attention Standard Llama transformer Gated DeltaNet + gated attention Sliding window + global attention Context 256K 131,072 262,144 128K Input modalities Text Text Text, image, video Text, image, audio License LFM Open License v1.0 ($10M revenue threshold) Apache 2.0 Apache 2.0 Apache 2.0 BFCL V4 (Liquid eval) 71.39 62.65 55.12 48.25 WebArena-Verified (Liquid eval) 38.42 9.11 21.92 17.06 SWE-bench Verified (Liquid eval) 43.40 34.80 41.20 0.50 GPQA Diamond (Liquid eval) 63.37 65.15 75.76 57.88 GPQA Diamond (vendor-reported) 63.37 70.2 76.2 58.6 RULER 128K (Liquid eval) 65.56 37.96 84.63 18.82 Liquid 29-benchmark average 49.37 39.19 39.27 31.74 

 Sources: Liquid LFM3 model card , MiniCPM5-2B card , Qwen3.5-4B card , Gemma 4 E4B card , LFM license . 

 What about vision, audio, omni and decision models? 

 LFM3-VL-2B averages 71.4 across 62 vision benchmarks. Gemma 4 12B scores 71.7 on the same suite. It leads that comparison on visual grounding (77.3) and GUI understanding (83.1). Video (61.2) and agentic tasks (42.5) still trail larger API models. 

 LFM3-Audio-2B reaches 6.2 English WER and a 3.8 UTMOSv2 TTS score. LFM3-Omni-2B scores 70.1 on Daily-Omni, against 61.3 for Qwen2.5-Omni-7B. 

 d1-2B replaces d1-3B with a third fewer parameters. It improves Decision Bench from 83.6 to 85.2. 

 How can developers deploy LFM3? 

 Weights are on Hugging Face , the Liquid AI Playground and the Liquid API. The docs list GGUF, MLX and ONNX for the text and vision models. Runtimes include llama.cpp, MLX, vLLM, SGLang, Ollama and Transformers. 

 On-device, Liquid AI measured llama.cpp at Q4_0 with 32K context. A full 128K context needs 1.6 GB of KV cache. Qwen3.5-4B needs 4.3 GB. On 1 NVIDIA B300 with SGLang, LFM3-1.7B produces 3.6B tokens per day at 1,024 concurrent requests. 

 Liquid AI also showed specialization. A few hours of SFT and GRPO on 1 A100 lifted wind-turbine defect classification to 67%. 

 Key Takeaways 

 6 open-weight 2B-class models share 1 tri-hybrid backbone. 

 LFM3-1.7B fits in about 1 GB at 4-bit with 256K context. 

 It beats Qwen3.5-9B on BFCL V4, WebArena-Verified and AutomationBench. 

 Knowledge and agentic coding remain clear weak spots. 

 Free commercial use stops at $10M annual revenue. 

 Check out the technical details , model weights and docs . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models appeared first on MarkTechPost .
