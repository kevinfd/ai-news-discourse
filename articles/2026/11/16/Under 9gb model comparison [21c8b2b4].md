---
id: "21c8b2b44c9b90b8"
title: "Under 9gb model comparison"
url: "https://reddit.com/r/LocalLLaMA/comments/1xxvr5z/under_9gb_model_comparison"
link: "https://reddit.com/r/LocalLLaMA/comments/1xxvr5z/under_9gb_model_comparison"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T17:39:46Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["parepeg"]
language: "en"
summary: "Scores are lab-reported so take them with a grain of salt. Specs Model Org Params (total/active) Context Modality License K2-Horizon-7B IFM 7B dense 512K text Apache-2.0 Granite 4.2-8B IBM 8B dense (thinking) 128K (512K ext.) text Apache-2.0 Qwen3.5-9B Qwen 9B hybrid (delta-net, thinking) 262K (~1M ext.) text + vision + video Apache-2.0 MiMo-V2.6-Distill-Qwen-9B Xiaomi 9B (SFT of Qwen3.5-9B)…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Google", "IBM"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 442
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xxvr5z/under_9gb_model_comparison/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Under 9gb model comparison

Reddit · parepeg · 2026-11-16

Scores are lab-reported so take them with a grain of salt. Specs Model Org Params (total/active) Context Modality License K2-Horizon-7B IFM 7B dense 512K text Apache-2.0 Granite 4.2-8B IBM 8B dense (thinking) 128K (512K ext.) text Apache-2.0 Qwen3.5-9B Qwen 9B hybrid (delta-net, thinking) 262K (~1M ext.) text + vision + video Apache-2.0 MiMo-V2.6-Distill-Qwen-9B Xiaomi 9B (SFT of Qwen3.5-9B) ~262K (base) text + vision (visual coding) MIT LFM2.5-8B-A1B Liquid 8.3B / 1.5B active MoE 128K text LFM 1.0 Gemma 4 E4B Google 4.5B effective / 8B total (PLE) 128K text + image + audio Apache-2.0 LFM3-VL-2B Liquid 1.92B (1.73B backbone, thinking) 128K text + image + video LFM 1.0 Text benchmarks Superscripts: a = K2 card (IFM harness), b = Liquid harness, c = MiMo card (Xiaomi harness); no mark = own card; e = from LFM3-1.7B, the text backbone; d/† = MiMo avg@3 / internal set. Bold = best in row (cross-harness caveat applies). Benchmark K2-7B Granite 8B Qwen3.5-9B MiMo-D-9B LFM2.5-8B-A1B Gemma 4 E4B LFM3-VL-2B Math AIME 2026 90.2 92.5 50.0 42.5 AIME 2025 90.3 86.7 56.1ᵇ 42.5 34.3ᵇ HMMT Feb 2026 77.8 66.5ᵃ 65.7ᵃ MATH-500 88.8 65.0ᵇ Coding SWE-bench Verified 72.4 47.7 50.8ᵃ 61.1ᵈ 0.5ᵇ 43.4ᵉ SWE-bench Pro 19.1 44.6ᵈ SWE-bench Multilingual 30.8 35.0ᵇ 0.7ᵇ 23.0ᵉ Terminal-Bench 2.1 44.6 20.6 29.2ᵃ 37.1 0.0ᵇ 12.9ᵉ LiveCodeBench v6 73.2 65.6 52.0 73.5ᵉ SciCode 33.6 30.4ᵃ 27.5ᵃ 25.0ᵇ 28.5ᵉ Agentic AutomationBench 15.1ᵇ 30.3 1.9ᵇ 41.3ᵉ LiveClaw 35.8ᵇ 20.4ᵇ 45.6ᵉ tau/ϴ-bench Banking 25.8 7.6ᵃ 7.0ᵃ 4.1ᵇ tau2-Bench 79.1 88.1T / 39.8R 42.2 WebArena Verified 28.9ᵇ 17.1ᵇ 38.4ᵉ BrowseComp / BrowseComp-Plus 59.0 38.0ᵇ 21.0ᵇ 37.0ᵉ PinchBench 71.5ᵇ 55.1ᵇ Claw-Eval (EN avg) 66.5ᵇ 56.1ᵇ 68.6ᵉ Toolathlon-Verified 25.9ᶜ 35.2 OfficeQA 9.0ᶜ 19.5 JobBench 2.6ᶜ 18.3 BFCL v4 (tool use) 52.4 66.1 49.7 48.3ᵇ 71.4ᵉ ToolSandbox 76.4ᵇ 69.3ᵇ 80.4ᵉ MCP-Atlas 42.7ᵇ 6.2ᵇ 32.6ᵉ EnterpriseOps-Gym 29.0ᵇ 13.4ᵇ 28.2ᵉ MiMo Code (mini) † 19.5ᶜ 51.6 MiMo Cyber (mini) † 5.7ᶜ 31.3 MiMo General (mini) † 28.5ᶜ 62.2 Knowledge GPQA Diamond 75.6 64.1 81.7 58.6 63.4ᵉ HLE 19.5 9.7ᵃ 14.9ᵃ 4.8ᵇ 7.2ᵉ MMLU-Pro 74.0 82.5 69.4 AA-Omniscience Index -28.0ᵇ -24.7 -15.3ᵇ 0.5ᵉ Instruction following IFEval 91.5 91.8 90.0ᵇ 96.7ᵉ IFBench 79.3 64.5 56.5 44.6ᵇ 73.0ᵉ Multi-IF 79.9 81.0ᵇ 89.1ᵉ IFStruct 89.2ᵇ 78.5ᵇ 93.7ᵉ Long context LCR / AA-LCR 68.0 43.3ᵃ 63.0 39.3ᵇ 52.8ᵉ RULER 128K 71.4 87.1ᵇ 18.8ᵇ 65.6ᵉ Vision benchmarks Benchmark LFM3-VL-2B Gemma 4 E4B Qwen3.5-9B MiMo-D-9B MMMU (val) 55.7 78.4 MMMU-Pro 45.7 52.6 70.1 MathVista (mini) 84.2 85.7 MATH-Vision 51.6 59.5 78.9 OCRBench v1 86.3 89.2 RefCOCO (avg) 90.5 89.7 ScreenSpot-Pro 55.5 65.2 RealWorldQA 79.3 80.3 MMStar 74.4 79.7 HallusionBench 65.6 69.3 MVBench (video) 69.4 74.4 Video-MME (subtitles) 69.0 84.5 MedXpertQA-MM 28.7 49.9 MiMo Visual Coding (mini) † 61.7ᶜ 64.0
