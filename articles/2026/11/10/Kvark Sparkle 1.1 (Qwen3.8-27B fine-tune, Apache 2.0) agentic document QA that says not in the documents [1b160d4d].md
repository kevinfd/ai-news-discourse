---
id: "1b160d4d85dccbe7"
title: "Kvark Sparkle 1.1 (Qwen3.8-27B fine-tune, Apache 2.0): agentic document QA that says \"not in the documents\" 91.5% of the time, with 7-48% fewer reasoning tokens than the base"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsp2tv/kvark_sparkle_11_qwen3827b_finetune_apache_20"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsp2tv/kvark_sparkle_11_qwen3827b_finetune_apache_20"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T15:00:45Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Ill_Contribution_717"]
language: "en"
summary: "We released Kvark Sparkle 1.1, the second model in our Qwen3.8-27B line. Open weights, Apache 2.0, MTP head intact, BF16 / FP8 / GGUF. **What it is for:** document work. You give it `search` and `read_page` tools over a document base. It searches, reads the page, answers from the passage, and when three searches in a row miss the fact it stops and says NOT IN DOCUMENTS instead of making…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "agents & coding", "search & media"]
content_source: "post"
word_count: 586
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsp2tv/kvark_sparkle_11_qwen3827b_finetune_apache_20/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Kvark Sparkle 1.1 (Qwen3.8-27B fine-tune, Apache 2.0): agentic document QA that says "not in the documents" 91.5% of the time, with 7-48% fewer reasoning tokens than the base

Reddit · Ill_Contribution_717 · 2026-11-10

We released Kvark Sparkle 1.1, the second model in our Qwen3.8-27B line. Open weights, Apache 2.0, MTP head intact, BF16 / FP8 / GGUF. **What it is for:** document work. You give it `search` and `read_page` tools over a document base. It searches, reads the page, answers from the passage, and when three searches in a row miss the fact it stops and says NOT IN DOCUMENTS instead of making something up. **How:** LoRA SFT on top of Sparkle 1.0 (agent trajectories over a public legal corpus, MuSiQue multi-hop doc QA, retention data), plus a short stop rule that ships in the system prompt. **Document work (GroundedWork, our agentic RAG eval: public Serbian documents, thinking on, LLM judge vs gold answers, 3 runs per question):** | | Qwen3.8-27B | Sparkle 1.0 | Sparkle 1.0 + stop rule | **Sparkle 1.1 + stop rule** | |---|---|---|---|---| | Document Q&A (70 questions × 3) | 85.7 | 86.2 | 89.5 | **91.0** | | Answer not in the documents, correctly declined (98 × 3) | not yet run | 36% | 74% | **91.5%** | Note that the stop rule alone does a lot of the work for 1.0 (36% to 74%). Training adds the rest: +17.5 points on declining against 1.0 with the same rule. The base Qwen on the decline set is not measured yet; I will add it here when it is. **General ability vs Qwen3.8-27B (same harness, paired):** | | Qwen3.8-27B | Sparkle 1.1 | median reasoning tokens (base → 1.1) | |---|---|---|---| | GPQA Diamond | 88.8 | 88.3 | 7,670 → 4,471 (−42%) | | AIME 2026 | 95.8 | 92.5 | 14,822 → 8,732 | | HMMT | 86.1 | 88.1 | 21,182 → 13,540 | | LiveCodeBench | 82.0 | 86.0 | 15,276 → 8,607 | | IFEval | 90.8 | 91.1 | 695 → 646 (−7%) | | MMLU-Pro | 83.6 | 84.0 | 708 → 518 | | FRAMES | 70.6 | 69.8 | 1,228 → 644 (−48%) | None of the accuracy differences is significant (95% intervals arer answer: 32.9 s vs 40.8 s on the same hardware. **Public agentic / long-context sets (FP8, vLLM, thinking on):** | | Qwen3.8-27B | Sparkle 1.1 | |---|---|---| | BrowseComp-Plus (830 queries, BM25, official judge prompt) | 22. median output tokens | | LongBench v2 (503) | 58.6 | 57.7 | | SWE-bench Verified (500, mini-swe-agent) | **81.8** | 73.0 | **Where it is weak, so you don't have to find out yourself:** - SWE-bench is significantly below the base. Shorter thinking costs accuracy in agentic coding. For coding, use the base model. - Questions that need links across several documents are its weakness - English questions over Serbian documents are weaker than Serbian ones. - Nothing measured past 64k; no separate safety eval. **Run it:** ``` vllm serve Egzakta/Kvark-Sparkle-1.1-27B-FP8 \ --max-model-len 131072 --kv-cache-dtype fp8 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice --tool-call-parser qwen3_coder \ --speculative-config '{"method":"mtp","num_speculative_tokens":3}' ``` For document agents, put the stop rule from the card into the systline rate drops a lot. - BF16: https://huggingface.co/Egzakta/Kvark-Sparkle-1.1-27B - FP8: https://huggingface.co/Egzakta/Kvark-Sparkle-1.1-27B-FP8 - GGUF: https://huggingface.co/Egzakta/Kvark-Sparkle-1.1-27B-GGUF Built by Egzakta's AI Lab in Belgrade. We run these on-prem for organisations that cannot send their documents to an API, which is why "I don't know" matters more to us than another point on a leaderboard. Happy to answer questions on the training data, the stop rule or the eval harness. If you test it on your own document set, I'd like to see where it breaks.
