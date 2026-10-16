---
id: "5241da4e264a9022"
title: "inclusionAI/Ling-3.1-flash · Hugging Face"
url: "https://huggingface.co/inclusionAI/Ling-3.1-flash"
link: "https://huggingface.co/inclusionAI/Ling-3.1-flash"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-14T15:11:14Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["jacek2023"]
language: "en"
summary: "With 560B total parameters, 25B active parameters per token, and a 1M-token context window , wait what? 3.0 was just 127B"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "Anthropic", "Google", "Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 592
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5tsni/inclusionailing31flash_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# inclusionAI/Ling-3.1-flash · Hugging Face

Hugging Face · jacek2023 · 2026-10-14

Instructions to use inclusionAI/Ling-3.1-flash with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Inference
- HuggingChat
- Notebooks
- Google Colab
- Kaggle
🤗 Hugging Face | 🤖 ModelScope | 🐙 OpenRouter
Introduction
We're introducing Ling-3.1-flash, an upgraded native hybrid reasoning model designed for complex, real-world tasks. With 560B total parameters, 25B active parameters per token, and a 1M-token context window, Ling-3.1-flash builds upon Ling-3.0-flash with improvements in architecture and performance on real-world tasks.
With stronger real-world capabilities, Ling-3.1-flash shows improvements across a range of real-world tasks, including general-purpose agents, search, office productivity, and software engineering. It demonstrates strong performance on benchmarks such as GDPVal-AA V2.1, HealthBench Professional, FrontierSWE, and Terminal-Bench 4.0, covering office tasks, healthcare, software engineering, and terminal-based tool use. The model also shows improvements in specialized domains such as finance and materials science.
Model Overview
The table and diagram below summarize the model’s specifications and architecture.
Evaluation
We have conducted a comprehensive evaluation of Ling-3.1-flash across multiple authoritative benchmarks. Ling-3.1-flash performs strongly on representative coding/agentic benchmarks including Terminal-Bench 4.0, SWE-bench Pro, FrontierSWE, GDPVal-AA V2.1, Automationbench, MCP-Atlas, and SkillsBench, among others. In practice, Ling-3.1-flash delivers a strong user experience across Claude Code, Kilo Code, Qwen Code, Hermes Agent, OpenClaw, and other frameworks. Beyond agentic tasks, Ling-3.1-flash performs strongly on real-world tasks across STEM, healthcare, and finance.
We also introduce LingCode, a harness built on the open-source coding agent Pi and enhanced to support complex, long-horizon coding tasks that run for hours, involve hundreds of rounds of tool calls, and require repeated context compaction. LingCode delivers significant performance gains on some coding agent tasks, and we are considering open-sourcing it in the future.
Quickstart
SGLang (Recommended)
The day-0 SGLang image includes Ling-3.1-flash support, MTP (NEXTN) speculative decoding, and Hopper decode optimizations:
docker pull lmsysorg/sglang:dev-ling-3.1-flash
Run Inference
Server (8 × H200, TP8 + EP8):
docker run --gpus all --network host --ipc=host --rm \
  lmsysorg/sglang:dev-ling-3.1-flash \
  python3 -m sglang.launch_server \
    --model-path inclusionAI/Ling-3.1-flash \
    --tp 8 --ep 8 \
    --speculative-algorithm NEXTN \
    --host 0.0.0.0 --port 30000
On 4 × GB300, use --tp 4 --ep 4 instead. Hopper decode optimizations (optional, ~10% faster batch-1 decode) can be enabled with SGLANG_ENABLE_FP8_BLOCK_GEMV=1 and SGLANG_ENABLE_FUSED_KDA_OUTPUT_QUANT=1.
Client
curl -s http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "Ling-3.1-flash",
       "messages": [{"role": "user", "content": "What is the capital of France?"}],
       "chat_template_kwargs": {"enable_thinking": true},
       "stream": true,
       "temperature": 1.0,
       "top_k": 20,
       "top_p": 0.95}'
Verified recipes for H200, GB300, H800, H100, and B200, plus HiCache (Mooncake L3), reasoning on/off, tool calling, and measured accuracy/speed numbers, are in the SGLang Ling-3.1-flash cookbook.
vLLM
Environment Preparation
pip install uv
uv venv ~/my_ling_env
source ~/my_ling_env/bin/activate
git clone -b vllm https://github.com/vllm-project/vllm.git
cd vllm
VLLM_USE_PRECOMPILED=1 uv pip install --editable . --torch-backend=auto
Run Inference
Server
vllm serve "$MODEL_PATH" \
    --port "$PORT" \
    --trust-remote-code \
    --served-model-name auto \
    --tensor-parallel-size 8 \
    --gpu-memory-utilization 0.85 \
    --enable-prefix-caching \
    --enable-expert-parallel \
    --mamba-cache-mode align \
    --enable-auto-tool-choice \
    --tool-call-parser ling3 \
    --reasoning-parser ling3 \
    --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
Client
It is recommended to use the sampling parameters (temperature=1.0, top_p=0.95, top_k=20) and set enable_thinking to true for better performance.
curl -s http://${MASTER_IP}:${PORT}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "auto", 
       "messages": [{"role": "user", "content": "What is the capital of France?"}],
       "chat_template_kwargs": {"enable_thinking": true},
       "stream": true,
       "temperature": 1.0, 
       "top_k": 20,
       "top_p": 0.95}'
Training Content Summary
The public training-content summary identifying Ling-3.1-flash is available below. Please refer to the document for its covered model versions, training-content scope, summary version, and update date.
This summary concerns training-content disclosure; it does not replace the model’s technical documentation, usage terms, or license.
- Downloads last month
- 666
