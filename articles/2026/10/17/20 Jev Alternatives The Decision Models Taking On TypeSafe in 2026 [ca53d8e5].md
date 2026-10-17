---
id: "ca53d8e5462270e7"
title: "20 Jev Alternatives: The Decision Models Taking On TypeSafe in 2026"
url: "https://marktechpost.com/2026/10/17/20-jev-alternatives-the-decision-models-taking-on-typesafe-in-2026"
link: "https://marktechpost.com/2026/10/17/20-jev-alternatives-the-decision-models-taking-on-typesafe-in-2026"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-17T07:26:39Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "TypeSafe launched Jev on September 15, 2026. It is a decision model, not a chatbot. You define the allowed answers, and Jev returns a label, a score or a yes/no probability. In about 4 weeks, at least 20 Jev alternatives shipped. They come from Cloudflare, OpenAI, Perplexity, Liquid AI, AWS’s Strands Labs and independent developers. This guide compares each one on size, license, hardware,…"
tags: ["Agentic AI", "AI Infrastructure", "Artificial Intelligence", "Comparison", "Decision Models", "Editors Pick", "For Devs", "Language Model", "Staff", "Tech News", "Technology"]
orgs: ["OpenAI", "Perplexity", "Amazon", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "jobs & society"]
content_source: "summary"
word_count: 2276
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 20 Jev Alternatives: The Decision Models Taking On TypeSafe in 2026

MarkTechPost · Asif Razzaq · 2026-10-17

TypeSafe launched Jev on September 15, 2026. It is a decision model, not a chatbot. You define the allowed answers, and Jev returns a label, a score or a yes/no probability. In about 4 weeks, at least 20 Jev alternatives shipped. They come from Cloudflare, OpenAI, Perplexity, Liquid AI, AWS’s Strands Labs and independent developers. This guide compares each one on size, license, hardware, pricing, Jev API compatibility and published benchmarks. 

 TL;DR 

 Size range: 287M (GLiNER2.5-multi-Decide) to 35B-A3B (Mapika Decider). Jev’s size is not disclosed. 

 Runs on: Encoders like Von and Laya run on CPU. 4B adapters fit a 24 GB GPU or a 32 GB Mac. 

 Performance: Most open models trail Jev on hard reasoning. Several match or beat it on narrow classification. 

 Best: Cloudflare Clef scores 94.20 BANKING77 F1 versus Jev’s 79.74, per Cloudflare’s own run. 

 Worst: Von 1.2 scores 0.422 accuracy in Respan’s run, against Jev’s 0.932. 

 What is Jev, and why look for alternatives? 

 Jev is TypeSafe’s first ‘System One’ model. You send a state, such as a ticket or log line. You also send typed questions: Choice, Score or Noul (yes/no). Jev scores every question in one parallel pass and generates no text. 

 TypeSafe’s docs list $0.042 per 1M input tokens, with free output. Context is 64k tokens per request. Input is text only. Weights are closed, and access runs through a waitlist. TypeSafe’s workflow evals put Jev at 67.8% agreement and 0.4 s per case. 

 That leaves 4 gaps developers keep raising: no images, no self-hosting, no published size and no fine-tuning. The 20 models below fill some or all of them. 

 How should you read these benchmarks? 

 Most figures below are self-reported. The suites differ: JevBench, Decision Index, typed-decisions and Respan’s behavior benchmark. Scores across suites are not comparable. The one multi-model third-party table comes from Respan , which sells a competing model. 

 Hosted decision APIs 

 1. Cloudflare Clef and Clef-flash 

 Cloudflare announced Clef on October 1, 2026. Clef is 27B on Qwen3.8-27B with a vision encoder. Clef-flash is 9B on Qwen3.5-9B. Both are Apache-2.0 on Hugging Face and served on Workers AI. They accept text, JSON and up to 4 images per request. 

 Workers AI pricing is $0.24 (Clef) and $0.038 (Clef-flash) per 1M input tokens. Cloudflare calls the API fully Jev-compatible. In its own run, Clef scored 94.20 BANKING77 F1 versus Jev’s 79.74. Jev still wins GPQA Diamond, 78.3 versus 48.0. 

 2. Liquid AI d1 

 Liquid AI’s d1 family has hosted d1 and d1-ultra, plus 2 open models. d1-3B (3.1B) runs on LFM2.5-VL-3B. d1-omni-600M (587M) adds audio clips up to 30 s. The open weights use the LFM Open License. 

 Liquid’s guide calls d1 through TypeSafe’s own SDK with a different base URL. Liquid reports d1-3B at 48.57 on Decision Index 0.2.1. It also reports 8 ms latency on an RTX 4090. Hosted parameter counts and paid rates are not disclosed. 

 3. OpenAI Decisions API 

 OpenAI released the Decisions API in public beta on October 6, 2026. It runs only on gpt-6-luna. It accepts text plus base64 images. Question types are predicate, choice and score. 

 Pricing is $0.10 per 1M input tokens, with output not billed. The schema is OpenAI’s own, so it is not Jev-compatible. OpenAI claims about 10x faster responses than the Responses API. No benchmarks are published. 

 4. Perplexity pplx-decider 

 Perplexity’s pplx-decider-v1-27b is a Qwen3.8-27B fine-tune under Apache-2.0. It reads text, JSON and up to 8 images per question. The API allows 128 questions and 255 options per request. 

 The current pricing is $0.02 per 1M input tokens for v1.2 (27B). A 4B flash-v1.2 costs $0.01. On Perplexity’s 11-task panel, it scored 85.71% versus Jev’s 84.51%. Jev still won BBH, 94.27 versus 82.80. 

 5. meraGPT Decider 1 

 meraGPT announced Decider 1 on September 22, 2026. It is a hosted, closed-weight, text-only model. It allows up to 10 Choice labels and a 4,096-token context. The model page lists $0.04 per 1M input tokens. 

 It exposes /v1/systemone and works with the TypeSafe SDK. On meraGPT’s typed-decisions run, it scored 0.768 versus Jev’s 0.727. An independent review notes its ECE of 0.180 trails Jev’s 0.144. 

 6. Respan Span-01 

 Span-01 is a behavior-scoring model, not a general decision model. It returns present, absent or not_observable probabilities. It costs $0.02 per 1M input tokens. Span-01 Lite is free. 

 Respan claims 0.843 overall F1 on its Behavior Benchmark. Its own blog table shows a lower 0.806, with GPT-6 Sol ahead at 0.885. Size, base model and license are not disclosed. 

 7. Standard Thinking Standard One 

 Standard One ships as 3B and 8B models, both open and hosted. The 8B is a LoRA on Ministral-3-8B under Apache-2.0. It reads text and images, with a 32,768-token context. It serves /v1/systemone. 

 Hosted text pricing is $0.018 (3B) and $0.035 (8B) per 1M tokens. On JevBench public hard, the 8B scored 54.95% versus Jev’s 72.07%. It led on realistic transfer, 90.83% versus 86.67%. Both runs are publisher-measured. 

 Open-weight Jev alternatives you can self-host 

 8. Together AI Tev1-4B-experimental 

 Together trained Tev1 as a LoRA SFT of Qwen3.5-4B. It cost about $17 and 25 minutes on 37,840 examples. It picks from 2 to 24 options. The model card says the weights license is still being finalized. 

 It answers through chat completions, not a native Jev endpoint. Respan measured 0.901 accuracy and 0.031 ECE, the best ECE in its table. Together warns its logprobs are not calibrated confidence. 

 9. Fastino GLiNER2.5-Decide 

 Fastino’s GLiNER2.5-Decide is a 340M DeBERTa-v3-large encoder under Apache 2.0. It handles decisions, span extraction and relations in one pass. A 1B and a 287M multilingual variant also exist. 

 On Fastino’s 17-domain set, the model card lists 60.2% exact match. p50 latency is 167.3 ms on a 48-vCPU Xeon. It is not Jev API-compatible. 

 10. Strands Labs Strands Decider 2B 

 AWS’s Strands Labs introduced Strands Decider on October 1, 2026. It is about 1.9B: Qwen3.5-2B-Base plus a pointer head. The repo publishes 246,678 training rows and the full recipe. One RTX 3090 trains it in about 11 hours. 

 It serves a local /v1/systemone endpoint under Apache-2.0. The v1 checkpoint scored 180 of 231 (77.9%) on JevBench public. Median latency is 115 ms on an RTX 3090. 

 11. Kev (Jared Palmer) 

 Kev comes in 0.8B, 4B, 9B and 27B sizes on Qwen3.5 and Qwen3.8. Kev-4B is a LoRA plus pointer head under Apache-2.0. It supports 255 options. The TypeSafe SDK works against it unchanged. 

 Kev-4B fits a 24 GB GPU or a 32 GB Apple Silicon Mac. Respan measured 0.833 accuracy and a 0.060 flip rate. Self-reported MMLU-Pro is 0.565 versus Jev’s 0.840. Option order can change its answers. 

 12. Mapika Decider family 

 Mapika’s Decider ships 0.8B to 35B-A3B variants on Qwen3.5 and Gemma 4. A decider-2b-vision model adds images. Everything is Apache-2.0, with 32k context and /v1/systemone. 

 On the JevBench public hard tier, decider-12b v1 tied Jev at 0.730. The 4B GGUF Q4_K_M is 2.7 GB and runs on CPU. The 4B’s ECE is 0.184 on hard items, so expect overconfidence. 

 13. Bespoke Labs Bespoke-Nimble-9B 

 Bespoke-Nimble-9B is a 165 MiB LoRA on Qwen3.5-9B, Apache-2.0 on Hugging Face. The current card lists 255 choices and 8,192 tokens. It reads English text only. 

 On Bespoke’s 324-example held-out set, Nimble scored 90.12% versus Jev’s 93.21%. Latency is about 106 ms on an H100. It trained on only 2,676 examples, and its probabilities are not calibrated. 

 14. Convai Innovations Laya 

 Laya is a ModernBERT-based family with 421M English and 322M multilingual checkpoints. It is Apache-2.0 and text only. The laya-serve server exposes a Jev-shaped /v1/systemone endpoint. 

 The typed-decisions checkpoint scored 0.766 versus Jev’s 0.727. On Banking77, it scored 0.425 versus 0.870. Respan measured 0.542 accuracy and a 0.396 injection success rate. p50 latency is 32.8 ms on a T4. 

 15. Von (wfzyx) 

 Von is a 395M ModernBERT-large encoder with an option-marker head. It scores all options in one bidirectional pass. It is Apache-2.0 with an 8,192-token context. 

 The repo reports 0.096 s p50 on 4 vCPUs and 0.023 s on an A10G. Respan measured Von 1.2 at 0.422 accuracy, the lowest in its table. Its calibration is tuned to JevBench and can mislead out of domain. 

 16. Open-Jev-9B (Zefan Cai) 

 Open-Jev ships 2B, 9B and 27B adapters on Qwen3.5 bases. Open-Jev-9B adds a scalar head and fits one 16 GB GPU. It matches the /v1/systemone request shape but claims no parity. 

 On a 231-task JevBench subset, the project reports 77.49% for 9B and 85.28% for 27B v1.1. Each candidate is capped at 4,096 tokens. Numeric and timeline tasks are weak. 

 17. OpenJev on DiffusionGemma (razorback16) 

 This OpenJev reads decisions from NVIDIA’s DiffusionGemma 26B-A4B (4B active). It accepts text plus up to 8 images. It uses the same wire API, so Jev SDKs work unchanged. 

 The project reports 87.4% on JevBench public and 30 ms p50 at 49 tokens. A free hosted endpoint gives 100M tokens per account. Self-hosting needs an NVIDIA GPU with at least 24 GB. 

 18. InnerJev-4B and InnerJev-27B 

 InnerJev comes from a Fudan, Tongji and King’s College London team. It distills LLM reasoning into a single-pass decision. The paper also introduces JEVal: 11,257 instances across 36 datasets. 

 On JEVal, InnerJev-27B scored 79.24% versus Jev’s 78.38%. Its ECE was 0.0149 against Jev’s 0.0532. InnerJev-4B scored 71.92%. Code is on GitHub ; the license is not stated. 

 19. SemIf 

 SemIf reads typed decisions from existing open LLMs, with Qwen3.5-4B as the default. A WebGPU demo runs quantized models in the browser. Code is MIT. 

 On a 102-row TypeSafe subset, SemIf scored 0.845 balanced accuracy versus Jev’s published 0.883. On an RTX 3090, direct logits took 1.023 s versus 5.332 s for JSON generation. It has no Jev-compatible endpoint. 

 20. Rizzo Flow 

 Rizzo Flow from Rizzo AI Academy is a LoRA on Spark-X2.5-4B under Apache-2.0. It serves a native /v1/decisions and a Jev-compatible /v1/systemone. Choice is capped at 26 options. 

 On 400 typed-decisions cases, it scored 0.648 versus the base model’s 0.574. Jev’s dataset-card figure is 0.727. It is uncalibrated by default. 

 What does the only multi-model third-party run show? 

 Respan used its Span-01 judge to score 11 models. Lower is better for every column except accuracy. 

 Model Accuracy Paired flip rate Injection ASR ECE Jev 1.13.0 0.932 0.021 0.063 0.045 Tev1 4B 0.901 0.052 0.042 0.031 Kev 4B 0.833 0.060 0.078 0.070 Decider 2B v10 0.747 0.128 0.208 0.074 Laya 0.542 0.298 0.396 0.092 Von 1.2 0.422 0.242 0.297 0.071 

 Source: Respan , October 16, 2026. Tev1 beat Jev on injection resistance and calibration. Jev led accuracy and consistency. 

 Jev alternatives comparison table 

 # Model Org Size License Inputs Jev API Price (per 1M input) Key result (source) Ref Jev 1.13 TypeSafe Not disclosed Closed Text Native $0.042 0.932 acc (Respan) 1 Clef / Clef-flash Cloudflare 27B / 9B Apache-2.0 Text, images Yes $0.24 / $0.038 94.20 BANKING77 F1 (vendor) 2 d1 family Liquid AI 587M to 3.1B open; hosted not disclosed LFM Open Text, images, audio Via TypeSafe SDK Not disclosed 48.57 Decision Index (vendor) 3 Decisions API OpenAI Not disclosed Closed Text, images No $0.10 Not published 4 pplx-decider Perplexity 27B / 4B flash Apache-2.0 Text, images No $0.02 / $0.01 85.71% vs Jev 84.51% (vendor) 5 Decider 1 meraGPT Not disclosed Closed Text Yes $0.04 0.768 typed-decisions (vendor) 6 Span-01 Respan Not disclosed Not stated Text Not stated $0.02 (Lite free) 0.843 F1 (vendor) 7 Standard One Standard Thinking 3B / 8B Apache-2.0 Text, images /v1/systemone $0.018 / $0.035 54.95% JevBench hard (vendor) 8 Tev1-4B-experimental Together AI 4B Being finalized Text No $0.042 (OpenRouter) 0.901 acc (Respan) 9 GLiNER2.5-Decide Fastino 340M Apache 2.0 Text No Not disclosed 60.2% exact match (vendor) 10 Strands Decider Strands Labs (AWS) ~1.9B Apache-2.0 Text /v1/systemone Free, local 77.9% JevBench public (project) 11 Kev-4B Jared Palmer 0.8B to 27B Apache-2.0 Text Yes Free, local 0.833 acc (Respan) 12 Decider family Mapika 0.8B to 35B-A3B Apache-2.0 Text, images (2B) Yes Free, local 0.730 JevBench hard, 12B (project) 13 Bespoke-Nimble-9B Bespoke Labs 9B Apache-2.0 Text Not stated Free, local 90.12% vs Jev 93.21% (vendor) 14 Laya Convai Innovations 322M / 421M Apache-2.0 Text Yes Free, local 0.542 acc (Respan) 15 Von wfzyx 395M Apache-2.0 Text Not stated Free, local 0.422 acc (Respan) 16 Open-Jev-9B Zefan Cai 2B to 27B Apache-2.0 Text Request shape only Free, local 77.49% JevBench subset (project) 17 OpenJev (DiffusionGemma) razorback16 26B-A4B Apache-2.0 (code) Text, images Yes Free tier, 100M tokens 87.4% JevBench public (project) 18 InnerJev Academic team 4B / 27B Not stated Text Not stated Free, local 79.24% vs Jev 78.38% JEVal (authors) 19 SemIf TheoLeeCJ 0.6B to 4B (base LLMs) MIT (code) Text No Free, local 0.845 vs Jev 0.883 (author) 20 Rizzo Flow Rizzo AI Academy 4B / 1.7B Apache-2.0 Text Yes Free, local 0.648 typed-decisions (author) 

 Which Jev alternative should you choose? 

 Need images: Clef, pplx-decider, Standard One or the DiffusionGemma OpenJev. 

 Need a drop-in Jev swap: Clef, Kev, Decider, meraGPT or Laya expose /v1/systemone. 

 Need CPU or edge: Von, Laya, GLiNER2.5-Decide or Liquid’s d1-omni-600M. 

 Need to train your own: Strands Decider and Together’s Tev1 publish full recipes. 

 Need the cheapest hosted call: Perplexity’s flash-v1.2 at $0.01 per 1M input tokens. 

 Whatever you pick, test it on your own labeled data first. Decision models can return a valid answer that is still wrong. 

 Key Takeaways 

 20 Jev alternatives shipped within roughly 4 weeks of Jev’s launch. 

 Clef, pplx-decider and Standard One add the image input Jev lacks. 

 Perplexity’s flash-v1.2 undercuts Jev at $0.01 per 1M input tokens. 

 In Respan’s run, Jev still leads accuracy at 0.932. 

 Almost every score is vendor-run, so benchmark on your own data. 
 
 The post 20 Jev Alternatives: The Decision Models Taking On TypeSafe in 2026 appeared first on MarkTechPost .
