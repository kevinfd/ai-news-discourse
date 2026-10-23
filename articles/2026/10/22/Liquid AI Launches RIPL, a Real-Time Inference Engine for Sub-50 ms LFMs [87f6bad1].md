---
id: "87f6bad16b7b7d6b"
title: "Liquid AI Launches RIPL, a Real-Time Inference Engine for Sub-50 ms LFMs"
url: "https://marktechpost.com/2026/10/22/liquid-ai-ripl-real-time-inference-engine"
link: "https://marktechpost.com/2026/10/22/liquid-ai-ripl-real-time-inference-engine"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T17:33:25Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Liquid AI just announced Liquid RIPL , short for Real-time Inference Pipeline. RIPL is a low-latency engine that serves Liquid Foundation Models (LFMs) inside a live request path. It returns complete generated responses end-to-end in under 50 ms. It also claims that latency holds while traffic arrives continuously at peak load. For developers, the message is simple. Swap gradient-boosted trees…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Language Model", "New Releases", "Staff"]
orgs: ["Nvidia", "Hugging Face"]
topics: ["models & research", "search & media", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 781
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Liquid AI Launches RIPL, a Real-Time Inference Engine for Sub-50 ms LFMs

MarkTechPost · Asif Razzaq · 2026-10-22

Liquid AI just announced Liquid RIPL , short for Real-time Inference Pipeline. RIPL is a low-latency engine that serves Liquid Foundation Models (LFMs) inside a live request path. It returns complete generated responses end-to-end in under 50 ms. It also claims that latency holds while traffic arrives continuously at peak load. For developers, the message is simple. Swap gradient-boosted trees for a generative model, and keep the latency budget. 

 TL;DR 

 Engine : Serves LFM2.5 models from 230M to 2.6B parameters 

 Runs on: Enterprise deployments on NVIDIA H100, H200, B200 and RTX PRO 6000 GPUs. Benchmarks used a single B200. 

 Performance: 5.6 to 28.4x lower p95 latency than Qwen3.5 on vLLM, per Liquid’s own tests. 

 Best: LFM2.5-1.2B hit 155.8 ms p95 vs 4,431 ms for Qwen3.5-0.8B, a 28.4x gap (256 in, 128 out). 

 Worst: LFM2.5-2.6B gained only 5.6x (449.1 ms vs 2,499 ms). Sub-50 ms fails on longer requests. 

 What problem does Liquid RIPL solve? 

 Most serving stacks target large batches and long agentic jobs. A few seconds per request is acceptable there. Search ranking, fraud checks and payment authorization need answers in milliseconds. Liquid AI argues teams default to classical models for these paths because LLM serving is too slow. RIPL is built to remove that trade-off. 

 How does RIPL work? 

 Liquid AI describes RIPL as optimizing the full path, from request arrival to completed response. In several workloads, Liquid AI plots the same model, LFM2.5-350M, on vLLM and on RIPL. RIPL’s p95 line sits well below the vLLM line in each case. That isolates part of the gain to the engine, not just the model architecture. 

 The LFM2.5 models themselves are hybrids. LFM2.5-1.2B-Instruct has 16 layers: 10 double-gated convolution blocks and 6 GQA blocks. LFM2.5-2.6B has 30 layers: 22 convolution blocks and 8 GQA blocks. 

 RIPL benchmarks: how fast is it vs vLLM? 

 Liquid measured p95 end-to-end latency under open-loop Poisson arrivals on one B200. LFMs ran on RIPL. Baselines, including MiniCPM5 and Granite 4.2, ran on vLLM. 

 Workload Load LFM2.5 on RIPL (p95) Qwen3.5 on vLLM (p95) Gap 1B class, 32 in → 32 out 1,000 req/s 34.6 ms (1.2B) 498 ms (0.8B) 14.4x 1B class, 256 in → 128 out 400 req/s 155.8 ms (1.2B) 4,431 ms (0.8B) 28.4x 2B class, 32 in → 32 out 1,000 req/s 76.4 ms (2.6B) 586.8 ms (2B) 7.7x 2B class, 256 in → 128 out 300 req/s 449.1 ms (2.6B) 2,499 ms (2B) 5.6x 

 Source: Liquid AI blog, Figure 2 . Sealf-reported. 

 Liquid AI also mapped 6 real-time workloads against fixed budgets: 

 Adtech query rewriting: 32 in, 32 out, 50 ms budget, LFM2.5-350M. 

 Search intent classification: 128 in, 1 out, 20 ms budget. 

 Search reranking: 1k in, 1 out, 30 ms budget. 

 Payments risk scoring: 512 in, 16 out, 50 ms budget, LFM2.5-1.2B. 

 Credit decisioning: 8k in, 64 out, 150 ms budget. 

 Image alt text: 512×512 image and 64 tokens in, 16 out, 100 ms budget, LFM2.5-VL-450M . 

&&
 -->

 Competitor Comparison 

 Feature LFM2.5-1.2B on RIPL Qwen3.5-0.8B on vLLM LFM2.5-2.6B on RIPL Qwen3.5-2B on vLLM Parameters 1.17B 0.8B 2.69B 2B Context 32,768 262,144 131,072 262,144 License (weights) LFM Open License v1.0 Apache 2.0 LFM Open License v1.0 Apache 2.0 Modality Text Text, image, video Text Text, image, video Default mode Instruct Non-thinking Always reasons Non-thinking Serving engine RIPL (enterprise) vLLM (open source) RIPL (enterprise) vLLM (open source) p95, 32→32 34.6 ms 498 ms 76.4 ms 586.8 ms p95, 256→128 155.8 ms 4,431 ms 449.1 ms 2,499 ms 

 Is RIPL used in production? 

 Yes, according to Liquid AI. Shopify is deploying LFMs across latency-sensitive commerce workloads. In search enhancement, LFMs run with sub-20 ms inference on production traffic. According to Liquid AI’s blog, they use about 50% fewer parameters than alternatives and deliver 2 to 10x faster inference. 

 Key Takeaways 

 RIPL is Liquid AI’s engine for LLMs inside live request paths. 

 Liquid claims 5.6 to 28.4x lower p95 latency than Qwen3.5 on vLLM. 

 Same-model tests (LFM2.5-350M) show RIPL itself beats vLLM. 

 Shopify runs LFMs at sub-20 ms in production search. 

 Enterprise-only, closed, and all figures are self-reported. 

 Check out the RIPL announcement , try the latency calculator , and see the LFM2.5 model cards .. All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Liquid AI Launches RIPL, a Real-Time Inference Engine for Sub-50 ms LFMs appeared first on MarkTechPost .
