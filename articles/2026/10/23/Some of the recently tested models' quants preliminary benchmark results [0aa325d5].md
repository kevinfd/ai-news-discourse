---
id: "0aa325d5e2d66f16"
title: "Some of the recently tested models' quants preliminary benchmark results"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdtbor/some_of_the_recently_tested_models_quants"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdtbor/some_of_the_recently_tested_models_quants"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T23:26:43Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["EmilPi"]
language: "en"
summary: "Delta score* Model Relevant llama.cpp / other flags 2.86 **DeepSeek-V4-Flash-Vision-Exp -hf ggml-org/DeepSeek-V4-Flash-Vision-Exp-GGUF:MXFP4 2.38 Qwen3.8-Flash-Next-Q4KXL-STRATA -hf unsloth/Qwen3.8-Flash-Next-GGUF:Q4_K_XL + strata flags: -kv int8 1.76 **Qwen3.8-27B-unsl -hf unsloth/Qwen3.8-27B-GGUF:Q8_0 -ctv q8_0 1.68 **Qwen3.8-Flash-Next-Q4KXL -hf unsloth/Qwen3.8-Flash-Next-GGUF:Q4_K_XL -ctv…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Nvidia", "Alibaba"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 289
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdtbor/some_of_the_recently_tested_models_quants/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Some of the recently tested models' quants preliminary benchmark results

Reddit · EmilPi · 2026-10-23

Delta score* Model Relevant llama.cpp / other flags 2.86 **DeepSeek-V4-Flash-Vision-Exp -hf ggml-org/DeepSeek-V4-Flash-Vision-Exp-GGUF:MXFP4 2.38 Qwen3.8-Flash-Next-Q4KXL-STRATA -hf unsloth/Qwen3.8-Flash-Next-GGUF:Q4_K_XL + strata flags: -kv int8 1.76 **Qwen3.8-27B-unsl -hf unsloth/Qwen3.8-27B-GGUF:Q8_0 -ctv q8_0 1.68 **Qwen3.8-Flash-Next-Q4KXL -hf unsloth/Qwen3.8-Flash-Next-GGUF:Q4_K_XL -ctv q8_0 1.67 **Qwen3.8-27B-unsl-UDQ3KXL-13.4G-T0.6 -hf unsloth/Qwen3.8-27B-GGUF:UD-Q3_K_XL -temp 0.6 0.17 **Gemma4-26B-A4B-Q8 -hf ggml-org/gemma-4-26B-A4B-it-GGUF:Q8_0 -1.10 Ling-3.0-Flash-Sante-IQ4XS -hf AtomicChat/Ling-3.0-flash-Sante-GGUF:IQ4_XS -ctv q8_0 -ctk q8_0 -1.11 Sage-A1.5-Q8 -hf InternScience/Sage-A1.5-Q8_0-GGUF:Q8_0 -1.18 K2-Horizon-7B-Q8 -hf bartowski/K2-Horizon-7B-GGUF:Q8_0 -1.25 Nemotron-3.5-Bolt-74B-A9B-IQ2_XXS -hf unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF:IQ2_XXS -1.35 Kolibri1-Q4 -hf bartowski/Kolibri-1-GGUF:IQ4_XS -ctv q8_0 -ctk q8_0 -2.15 Recursive-Flint-Q8 -hf bartowski/RecursiveSI_flint-GGUF:Q8_0 -ctv q8_0 -2.38 LFM2.5-24B-A2B-Q4_0-QAD -hf LiquidAI/LFM2.5-24B-A2B-GGUF -hf-file LFM2.5-24B-A2B-QAD-Q4_0.gguf \ Delta score is a measure of how much above average a model is. * \ *Those models were released and tested long before, given for reference * Results for me are that for 2xRTX3090+128GB RAM no new models reach the capabilities of DS/Qwen models aged few months. Hopefully this changes with Qwen4. The tasks include an agentic coding task (rather easy one which only top models did well anyway), reasoning, tricky, spatial reasoning, physics, adversarial, needle in the haystack questions. This is just the quants I used with the settings I used. Please share your impressions if they are different, so that I can improve the test/quants/params. Sometimes the stock parameters may have been inferior, sometimes I tried to squeeze models into VRAM+RAM too much (especially with ctv/ctk). Maybe I should try bigger quants, and drop ctk/ctv for smaller models, but I don't expect pivotal changes. Things I didn't expect 1) Qwen3.8-Flash-Next on Strata does not have quality degradation, and does actually speed things up; 2) Nemotron is disappointing at the claimed QAT quant 3) Ling Sante became much faster, but quality didn't improve. 4) K2-Horizon-7B isn't bad for its size. Maybe this saves someone from lots of GB downloaded and some disappointment. source: https://beta.locallm.top/home?question=9
