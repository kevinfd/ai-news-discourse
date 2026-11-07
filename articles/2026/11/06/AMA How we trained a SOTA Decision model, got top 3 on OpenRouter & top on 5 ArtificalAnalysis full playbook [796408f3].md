---
id: "796408f3ea79e645"
title: "AMA: How we trained a SOTA Decision model, got top 3 on OpenRouter & top on 5 ArtificalAnalysis: full playbook - arch, datasets, training, evals, inference"
url: "https://reddit.com/r/LocalLLaMA/comments/1xphq4u/ama_how_we_trained_a_sota_decision_model_got_top"
link: "https://reddit.com/r/LocalLLaMA/comments/1xphq4u/ama_how_we_trained_a_sota_decision_model_got_top"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T16:51:38Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["m4rkGS"]
language: "en"
summary: "hey llamas! My name is Alt, and I'm on the technical staff at Nace AI . We're doing a quick AMA here, so ask us anything and we'll answer. we just published a full technical report on how we build, train, and evaluate Drex , our family of four open decision models. A decision model takes a state (a document, record, or agent context, optionally with images) plus questions with options, and…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 536
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xphq4u/ama_how_we_trained_a_sota_decision_model_got_top/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# AMA: How we trained a SOTA Decision model, got top 3 on OpenRouter & top on 5 ArtificalAnalysis: full playbook - arch, datasets, training, evals, inference

Reddit · m4rkGS · 2026-11-06

hey llamas! My name is Alt, and I'm on the technical staff at Nace AI . We're doing a quick AMA here, so ask us anything and we'll answer. we just published a full technical report on how we build, train, and evaluate Drex , our family of four open decision models. A decision model takes a state (a document, record, or agent context, optionally with images) plus questions with options, and returns a probability distribution over the options in a single pass, with no autoregressive decoding and no output parsing. Top 3 on OpenRouter Top 5 on Artificial Analysis 1. Models - Drex DLM (8B): diffusion LM backbone with bidirectional attention over the context - Drex v1.5 (9B): Gated DeltaNet hybrid backbone - Drex v2.0 (35B, 3B active): sparse MoE backbone - Drex Max (27B): dense, with an image encoder for vision inputs Pointer models (DLM / v1.5 / v2.0) encode the state once and cache it, so every question attends to the state but never to another question. A pointer head scores each option. Drex Max reads each question in full and answers with a linear readout head over option codes. Some technical details from the report: 1. Models - A family of four specialized decision models: Drex DLM (8B), Drex v1.5 (9B), Drex v2.0 (35B MoE, 3B active), and Drex Max (27B dense, with vision) - We built them on different architectures: a diffusion LM, a Gated DeltaNet hybrid, a sparse mixture of experts, and a dense transformer - We experimented with bidirectional vs. causal attention over the state, a pointer decision head that shares one cached state across questions, and a readout head for Max 2. Training - Full-parameter SFT on 1.15M verified decision records (2.9M questions) - Consistency training: we penalize the model when its output changes after the options are reordered or the state is shuffled - RLAF (Reinforcement Learning from Adjusted Feedback), using verified outcomes and judge feedback - Ablations to see which methods actually contributed On top of SFT, RLAF gave us +2.0 on the Decision Index, +1.5 pp accuracy, and 0.9 pp lower calibration error. The consistency terms cut the option-order flip rate from 6.3% to 4.2%. 3. Evaluation - Drex Max scores 67.52 on Decision Index 0.4.1 (public suite), vs. 60.70 for Jev 1.14.0 - Drex v2.0 has 1.37% calibration ECE on ~115K held-out decisions - Drex Max answers a typical request in 183 ms, vs. ~2.0 s for GPT-6 Sol and ~3.5 s for Claude Opus 5.5 - Context up to 131K tokens for v1.5/v2.0 and 262K for Max We also cover our limitations: our models trail frontier chat models on closed-book knowledge, and we don't yet have same-backbone architecture ablations. 5. Running locally The models are available in safetensors and GGUF formats, with llama.cpp and Ollama support. Their report includes details on quantization, caching, inference, and reproducibility. Links - Paper (arXiv): https://arxiv.org/pdf/2611.07854 - Blog: https://www.nace.ai/research/towards-foundation-decision-models - Weights: https://huggingface.co/collections/nace-ai/drex - GitHub: https://github.com/nace-ai/drex-decision-models - API: https://console.nace.ai we wanted to share the full methodology, not just benchmark numbers. hopefully it's useful if you're building agent routers, doing tool selection, or training your own decision models. ask us anything about architecture, data, training, evals, or running it locally
