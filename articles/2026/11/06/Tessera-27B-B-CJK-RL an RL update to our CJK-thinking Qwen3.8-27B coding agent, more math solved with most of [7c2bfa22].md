---
id: "7c2bfa2269dd7867"
title: "Tessera-27B-B-CJK-RL: an RL update to our CJK-thinking Qwen3.8-27B coding agent, more math solved with most of the token saving kept"
url: "https://reddit.com/r/LocalLLaMA/comments/1xprcv6/tessera27bbcjkrl_an_rl_update_to_our_cjkthinking"
link: "https://reddit.com/r/LocalLLaMA/comments/1xprcv6/tessera27bbcjkrl_an_rl_update_to_our_cjkthinking"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T23:23:20Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["ghgi_"]
language: "en"
summary: "A few weeks ago we posted Tessera-27B-B-CJK here, a Qwen3.8-27B coding agent that thinks in compressed CJK and uses fewer thinking tokens per agent turn. Thanks for all the feedback on that one. Today we're releasing the RL version, Tessera-27B-B-CJK-RL. Open weights, Apache-2.0. - Hugging Face: https://huggingface.co/ZelligeAI/Tessera-27B-B-CJK-RL - Release post:…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "China"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 515
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xprcv6/tessera27bbcjkrl_an_rl_update_to_our_cjkthinking/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tessera-27B-B-CJK-RL: an RL update to our CJK-thinking Qwen3.8-27B coding agent, more math solved with most of the token saving kept

Reddit · ghgi_ · 2026-11-06

A few weeks ago we posted Tessera-27B-B-CJK here, a Qwen3.8-27B coding agent that thinks in compressed CJK and uses fewer thinking tokens per agent turn. Thanks for all the feedback on that one. Today we're releasing the RL version, Tessera-27B-B-CJK-RL. Open weights, Apache-2.0. - Hugging Face: https://huggingface.co/ZelligeAI/Tessera-27B-B-CJK-RL - Release post: https://zellige.ai/research/tessera-27b-b-cjk-rl-release - RL method write-up: https://zellige.ai/research/tessera-27b-b-cjk-rl What changed: A lot of the questions last time were about quality. Tessera-27B-B-CJK was weaker than the base on hard math and code, so this version adds 8 RL updates on math and code on top of it. Numbers: (xhigh effort, both Tessera models sampled the same day with the same seeds): - AIME + HMMT 2026, 63 new problems, 2 attempts each: 108 of 126 right vs 97 for Tessera-27B-B-CJK, and 11 vs 23 attempts cut off at the 64K window. We didn't run the base on these. - Our main hard set (118 problems from AIME 2022-2024, LiveCodeBench and MATH level 5): 100 vs 89. The base got 98 in an earlier run, so it's now roughly level with the base qwen there instead of behind. - Agent turns, 64 new states from 16 coding tasks held out from training: 0.67x the base model's thinking tokens on a typical turn (90% CI 0.53-0.85), with 256 of 256 valid tool calls. - That's 1.11x Tessera-27B-B-CJK's typical turn (CI 0.98-1.26), so the first version still keeps a bit more of the saving (0.60x the base on the same tasks). Example turn from a held-out task: 测试套件：基线同(既有5失败不变+11新通过). 无回归. Typecheck: 仅既有version.ts错(因predev生成). 现跑lint于改文件. The base qwen spent 158 tokens at the same step. That's a bigger cut than usual: the typical turn is about two thirds of the base. How we trained it: 8 RL updates on Tinker, starting from Tessera-27B-B-CJK, using the per-rollout weighting from our ablation write-up. Each rollout's advantage is spread over its own tokens, so long failed rollouts don't dominate the update. Later updates thought longer per agent turn, since the reward only sees math and code, so we picked update 8 and confirmed it on held-out tasks before release. A few things people asked last time: - Does CJK pack more meaning per token? A little, at the phrase level, where one word can stand in for a whole English phrase. Most of the saving comes from training the model to think less, and the CJK is a smaller extra on top, We do plan to expand this further as the limiter here is tokenizer and going past just CJK and using other methods are being researched. - Quants: the GGUF repo has BF16 plus UL-Q3_K_XL through Q8_K_XL (Q3 is 13.15 GB, no XXS yet). The BF16 GGUF, the five quants and the NVFP4 checkpoint all passed a quick breakage check (valid tool call, no Chinese in the answer, no loops). We haven't benchmarked them or tried the vision projector, so results are very welcome. - Effort: use xhigh, same as before. Also, if you grabbed the original Tessera-27B-B-CJK-NVFP4 before Nov 5: its config.json didn't load in vLLM. We fixed it so a config.json redownload is needed.
