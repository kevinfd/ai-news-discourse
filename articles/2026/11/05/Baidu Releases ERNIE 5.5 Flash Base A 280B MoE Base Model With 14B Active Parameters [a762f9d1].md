---
id: "a762f9d149436c92"
title: "Baidu Releases ERNIE 5.5 Flash Base: A 280B MoE Base Model With 14B Active Parameters"
url: "https://marktechpost.com/2026/11/05/baidu-ernie-5-5-flash-base-280b-moe"
link: "https://marktechpost.com/2026/11/05/baidu-ernie-5-5-flash-base-280b-moe"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T21:33:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Baidu has released ERNIE 5.5 Flash Base , the raw pre-training checkpoint of its new sparse Mixture-of-Experts language model. ERNIE 5.5 Flash Base is a 280B-parameter text model from Baidu that activates 14B parameters per token. The weights stop at the end of pre-training, with no mid- or post-training applied. This as a clean starting point for teams that want to compare fine-tuning,…"
tags: ["AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source", "Staff"]
orgs: ["Baidu", "DeepSeek", "Hugging Face", "UK"]
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 899
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Baidu Releases ERNIE 5.5 Flash Base: A 280B MoE Base Model With 14B Active Parameters

MarkTechPost · Michal Sutter · 2026-11-05

Baidu has released ERNIE 5.5 Flash Base , the raw pre-training checkpoint of its new sparse Mixture-of-Experts language model. ERNIE 5.5 Flash Base is a 280B-parameter text model from Baidu that activates 14B parameters per token. The weights stop at the end of pre-training, with no mid- or post-training applied. This as a clean starting point for teams that want to compare fine-tuning, instruction tuning or RL methods from one checkpoint. 

 TL;DR 

 Size: 280B total, 14B active per token; 128K training context, 1M for fine-tuning and inference. 

 Runs on: Multi-GPU servers. Baidu’s reference configs use 4-way parallelism in SGLang and vLLM. GPU model and VRAM not disclosed. FP8 and BF16 weights. 

 Performance: Best score on 24 of 30 base-model benchmarks in Baidu’s unified pipeline (self-reported). 

 Best: MMLU-Pro 78.4, ahead of DeepSeek-V4-Flash-Base at 69.2. 

 Worst: HELMET-Rerank 56.2, behind DeepSeek-V4-Flash-Base at 60.0. 

 What is ERNIE 5.5 Flash Base? 

 It is a text-only MoE base model with 43 layers and a 4096 hidden size . It was pre-trained from scratch on 33.5T tokens with the Muon optimizer. The tokenizer has 201,216 entries and groups numbers right-to-left in chunks of up to 3 digits. 

 Activated compute, KV cache and long-context cost were treated as one budget. Pre-training data leaned on repository-scale code and long-context material, since those are hard to add later. 

 How does the ERNIE 5.5 Flash architecture work? 

 Hybrid attention : 37 layers use Heavily Compressed Attention (HCA), which caches 1 entry per 128 tokens. The other 6 layers use Multi-head Latent Attention with sparse attention (MLA + DSA). That means 1 in 7 layers keeps full-context access. HCA layers use 512-dim heads; MLA layers use 256-dim heads. 

 Gated and mixed heads : The attention output gate comes from the low-rank query latent, cutting gate-projection parameters by 75%. Virtual Head Attention adds a lightweight low-rank mix across heads. 

 Multi-Router Latent MoE. Each MoE layer has 512 routed experts (top-10) plus 1 shared expert. Several independent sigmoid routers replace a single router, per Baidu’s Multi-Router paper . Expert FLOPs and communication volume stay unchanged. Experts run in a 2048-d latent space, half the hidden width. 

 ECHO instead of MTP. : ECHO reuses the backbone’s final layer to predict future tokens. The same layer doubles as a built-in draft model for speculative decoding. ECHO adds 0.36B parameters, excluded from the headline counts. 

 Other pieces : The model uses Manifold-constrained Hyper-Connections with expansion rate 4 and a MultiMax output head. 

&&

 How does ERNIE 5.5 Flash Base perform on benchmarks? 

 Baidu team evaluated all 4 models with the same pipeline, prompts and few-shot settings. All figures below are self-reported by Baidu. 

 Exams: MMLU 93.3, MMLU-Redux 94.1, MMLU-Pro 78.4. 

 Knowledge: SimpleQA 34.1, versus 29.1 for DeepSeek-V4-Flash-Base. 

 STEM and reasoning: GPQA 60.2, MGSM 87.0, BBH direct 77.1. 

 Code: HumanEval+ 82.3, MBPP+ 81.5, LiveCodeBench 40.1. 

 Long context: RepoQA 91.7, LongBench-v2 48.7, HELMET-ICL 85.9. 

 It loses on 6 tasks. DeepSeek-V4-Flash-Base leads on ChineseSimpleQA, INCLUDE-lite, HELMET-Rerank and InfiniteBench. Hy3-preview-Base leads on BBH CoT and FullStackBench. 

 Competitor numbers in Baidu’s pipeline differ slightly from each vendor’s own report. DeepSeek lists MMLU-Pro 68.3; Baidu measures 69.2. Tencent lists Hy3 MMLU-Pro at 65.76; Baidu AI measures 66.9. 

 How does it compare with DeepSeek, Tencent and Xiaomi base models? 

 Feature ERNIE 5.5 Flash Base DeepSeek-V4-Flash-Base Hy3-preview-Base MiMo-V2.5-Base Developer Baidu DeepSeek Tencent Xiaomi Total params 280B 284B 295B (+3.8B MTP) 310B Active params 14B 13B 21B 15B Context 128K train / 1M inference 1M 256K 256K Attention HCA + MLA-DSA hybrid CSA + HCA hybrid GQA SWA + global, 5:1 Experts 512 routed, top-10 + 1 shared Not disclosed on card 192, top-8 256, top-8 Released weights FP8, BF16 FP8 Mixed BF16 FP8 License ERNIE 5.5 Flash Base License v1.0 MIT Tencent Hy Community License MIT MMLU-Pro* 78.4 69.2 66.9 65.7 HumanEval+* 82.3 69.5 78.0 74.4 LongBench-v2* 48.7 44.5 39.8 44.6 HELMET-Rerank* 56.2 60.0 55.7 56.6 

 *Scores from Baidu’s unified evaluation , self-reported. 

 How do you deploy ERNIE 5.5 Flash Base? 

 Weights are on Hugging Face and ModelScope, in FP8 and BF16 . Baidu documents serving with SGLang and vLLM. The SGLang example uses --tp 4 . The vLLM path needs version 0.32.0 plus the vLLM-ERNIE plugin . Both servers accept up to 1,048,576 tokens. As a base model, it runs through the completions endpoint, not chat. 

 Training ran on FlashMask-4 , a kernel for SM90 and SM100 GPUs. On SM100, Baidu team reports up to 175% faster forward and 74% faster backward than FlashAttention-4 MaskMod. 

 Key Takeaways 

 280B total, 14B active: a sparse MoE base checkpoint, not a chat model. 

 MMLU-Pro 78.4 leads DeepSeek-V4-Flash-Base by 9.2 points. 

 HCA caches 1 entry per 128 tokens in 37 of 43 layers. 

 ECHO turns the final layer into a built-in speculative draft model. 

 License is free under US$50M revenue but excludes EU, UK and South Korea. 

 Check out the Model Weights , Technical Blog , and papers on VHA , Multi-Router MoE and ECHO . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Baidu Releases ERNIE 5.5 Flash Base: A 280B MoE Base Model With 14B Active Parameters appeared first on MarkTechPost .
