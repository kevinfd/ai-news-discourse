---
id: "9e0bec6a87e626ed"
title: "Recursive Releases Flint, an Open-Weight 40B MoE Local Coding Model for Agents with 2.5B Active Params"
url: "https://marktechpost.com/2026/10/21/recursive-flint-local-coding-model"
link: "https://marktechpost.com/2026/10/21/recursive-flint-local-coding-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T22:39:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Recursive Superintelligence has released Flint , its first model. The Recursive Flint local coding model is a mixture-of-experts (MoE) model with 40B total and 2.5B active parameters. Recursive team states that its Eureka Machine, an automated research system, helped build nearly every part of the stack. The weights are on Hugging Face under Apache 2.0. \n\n TL;DR \n\n Size: 39.8B total, about 2.5B…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning"]
orgs: ["Alibaba", "Nvidia", "Apple", "Google", "Hugging Face", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "safety & ethics"]
content_source: "summary"
word_count: 1056
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Recursive Releases Flint, an Open-Weight 40B MoE Local Coding Model for Agents with 2.5B Active Params

MarkTechPost · Asif Razzaq · 2026-10-21

Recursive Superintelligence has released Flint , its first model. The Recursive Flint local coding model is a mixture-of-experts (MoE) model with 40B total and 2.5B active parameters. Recursive team states that its Eureka Machine, an automated research system, helped build nearly every part of the stack. The weights are on Hugging Face under Apache 2.0. 

 TL;DR 

 Size: 39.8B total, about 2.5B active per token. Context: 262,144 tokens documented on the model card; the blog cites up to 512k. 

 Runs on: 48 GB Apple Silicon Macs (M4 Pro, M5 Pro, M5 Max) or 48 GB NVIDIA GPUs. 4-bit weights take about 23 GB. 

 Performance: Tops Recursive’s chart among MoE models under 50B on agentic coding. Trails the strongest dense models. 

 Best: IFEval 95.1%. SWE-bench Verified 74.2%. 

 Worst: Terminal-Bench 2.1 at 54.9%, versus 73.0% for dense Qwen 3.8. 

 What is Recursive Flint? 

 Flint is a decoder-only MoE Transformer for coding agents. The model investigates codebases, fixes bugs, implements features and writes tests. It is text-only and supports reasoning and OpenAI-compatible tool calls. 

 Introducing Flint, @Recursive_SI ’s first model: a fast local coding model built with our automated research system, the Eureka Machine. • Best-in-class fast local coding • Up to 2x faster than comparable models: 125+ tokens/sec on a MacBook Pro, 150+ on RTX Spark • Built from… pic.twitter.com/ufg2xScSGw — Richard Socher (@RichardSocher) October 21, 2026 

 How does Flint’s architecture work? 

 Flint has 49 layers: 2 dense layers, then 47 MoE layers. Each MoE layer has 256 routed experts. A router selects 6 per token, plus 1 always-active shared expert. 

 Attention mixes 2 types. 35 layers use a 513-token sliding window. 14 layers use full attention with no positional encoding. There are 32 query heads and 4 key/value heads. 

 The 2.5B active figure includes the output head. The active body alone is about 2.2B parameters. 

 How did the Eureka Machine build Flint? 

 The Eureka Machine proposes ideas, implements them, tests them and picks what to try next. 

 Recursive highlights 3 contributions: 

 Architecture: It started from a 35B-total, 3B-active baseline. It searched expert configurations and widths, landing on 40B total and 2.5B active. 

 Quantization: It quantized the output layer (lm_head) to 4 bits, against common practice. An offline distillation stage, with the 16-bit model as teacher, recovered accuracy. This nearly halved training steps versus a quantization-aware training baseline. The NVFP4 model scores within 0.7 points of the 16-bit model. 

 Kernels: It wrote specialized kernels for low-bit projections, MoE operations, attention and prompt processing. On M4 and M5 chips, a Metal megakernel fuses the entire decode forward pass. 

 How does Flint perform on coding benchmarks? 

 All scores below are self-reported by Recursive. Sampling used temperature 1.0, top-p 0.95 and top-k 20. 

 Benchmark Flint BF16 Flint NVFP4 Terminal-Bench 2.1 54.9% 53.7% SWE-bench Pro v2 89.7% 88.5% SWE-bench Verified 74.2% 74.1% LiveCodeBench v6 80.3% 80.8% IFBench 89.2% 88.1% IFEval 95.1% 94.6% 

 Terminal-Bench used the Terminus 2 harness. Solutions found through web retrieval counted as failures. SWE-bench runs used mini-swe-agent with no internet access. Agentic scores average pass@1 over at least 5 attempts. 

 In Recursive’s chart, Qwen3.6 scores 73.4% on SWE-bench Verified. Dense Qwen 3.8 scores 73.0% on Terminal-Bench 2.1, well above Flint. 

 Recursive’s own comparison chart (scores in %, † measured by Recursive, others developer-reported): 

 Model Terminal-Bench 2.1 SWE-bench Pro v2† SWE-bench Verified LiveCodeBench v6 IFBench IFEval Flint BF16 54.9 89.7 74.2 80.3 89.2 95.1 Flint NVFP4 53.7 88.5 74.1 80.8 88.1 94.6 Qwen 3.5 (MoE) 38.7 68.6 69.2 74.6 70.2 91.9 Qwen 3.6 (MoE) 44.9 73.8 73.4 80.4 67.9 89.6 Laguna XS 2.1 (MoE) 24.7† 38.6 70.9 49.5† 34.4† 73.7† Qwen 3.8 (dense) 73.0 94.9 75.6† 90.3 79.5 94.6† Muse Glimmer (dense) 51.7 86.0 76.0 63.5† 77.0 94.7† Gemma 4 (dense) 43.4 61.7 66.6 80.0 76.0 94.6 

&&

 How does Flint compare with Qwen3.6, Laguna XS 2.1 and Gemma 4? 

 Competitor figures below come from each developer’s own model card, not Recursive’s chart. 

 Feature Recursive Flint Qwen3.6-35B-A3B Laguna XS 2.1 Gemma 4 31B Developer Recursive Qwen (Alibaba) Poolside Google DeepMind Total params 39.8B 35B 33B 30.7B Active params ~2.5B 3B 3B 30.7B (dense) Context 262,144 (blog: up to 512k) 262,144 native, up to 1,010,000 262,144 256K Modality Text Text + image Text Text + image License Apache 2.0 Apache 2.0 OpenMDW-1.1 Apache 2.0 Local hardware 48 GB Mac or GPU Not disclosed Mac with 36 GB RAM Consumer GPUs, workstations SWE-bench Verified 74.2% 73.4% 70.9% Not disclosed Terminal-Bench 54.9% (v2.1) 51.5% (v2.0) 37.5% (v2.0) Not disclosed LiveCodeBench v6 80.3% 80.4% Not disclosed 80.0% SWE-bench Pro 89.7% (v2) 49.5% (public) 47.6% (public) Not disclosed 

 How fast is Flint, and what hardware does it need? 

 Recursive reports more than 125 tokens per second on an M4 Pro MacBook Pro. It reports more than 150 tokens per second on a 64 GB NVIDIA RTX Spark. Both are short-context figures, up to 2x faster than comparable models. It also claims Flint runs more than 5x faster than dense 25-40B models with similar coding scores. 

 There are 3 local options: 

 Apple Silicon: Flint INT4 MLX weights take about 22.6 GB. The rec engine needs an M4 Pro, M5 Pro or M5 Max with 48 GB memory. It reports 1.4 to 2.6x the throughput of llama.cpp on an M4 Pro. 

 NVIDIA: The NVFP4 GGUF file is 22.9 GB. Recursive recommends at least 48 GB of GPU memory. 

 Server: The 80 GB BF16 checkpoint needs 1 B300 or H200 GPU per replica. 

 Flint also works with llama.cpp, Ollama, Unsloth, LM Studio, vLLM and SGLang. 

 Key Takeaways 

 Flint is a 40B MoE coding model with only 2.5B active parameters. 

 It scores 74.2% on SWE-bench Verified and 54.9% on Terminal-Bench 2.1. 

 4-bit weights run in about 23 GB on a 48 GB Mac or GPU. 

 Recursive’s Eureka Machine helped design the architecture, quantization and kernels. 

 SWE-bench Pro v2 scores are Recursive-measured and not comparable to public SWE-Bench Pro. 

 Check out the technical details , model weights and rec engine on GitHub . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Recursive Releases Flint, an Open-Weight 40B MoE Local Coding Model for Agents with 2.5B Active Params appeared first on MarkTechPost .
