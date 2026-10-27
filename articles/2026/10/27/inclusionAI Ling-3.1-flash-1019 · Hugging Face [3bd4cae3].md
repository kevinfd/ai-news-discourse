---
id: "3bd4cae39db0a5b5"
title: "inclusionAI/Ling-3.1-flash-1019 · Hugging Face"
url: "https://huggingface.co/inclusionAI/Ling-3.1-flash-1019"
link: "https://huggingface.co/inclusionAI/Ling-3.1-flash-1019"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-27T11:12:14Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["jacek2023"]
language: "en"
summary: "from inclusionAI: We introduce Ling-3.1-flash-1019 , an upgraded version of Ling-3.1-flash , with 560B total parameters, 25B active parameters per token, and a 1M-token context window . With further post-training optimizations, Ling-3.1-flash-1019 demonstrates significant improvements in reasoning and real-world agentic capabilities. Its AA-Briefcase score rises from approximately 1400 to 1524…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 445
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgpo4q/inclusionailing31flash1019_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# inclusionAI/Ling-3.1-flash-1019 · Hugging Face

Hugging Face · jacek2023 · 2026-10-27

🤗 Hugging Face | 🤖 ModelScope | 🐙 OpenRouter
Introduction
We introduce Ling-3.1-flash-1019, an upgraded version of Ling-3.1-flash, with 560B total parameters, 25B active parameters per token, and a 1M-token context window. With further post-training optimizations, Ling-3.1-flash-1019 demonstrates significant improvements in reasoning and real-world agentic capabilities. Its AA-Briefcase score rises from approximately 1400 to 1524 Elo, while performance on AutomationBench-AA increases from 62% to 68%. The model also makes gains on scientific benchmarks, including CritPt (18% → 26%) and SciCode (54% → 57%). Overall, it scores 44 on the Artificial Analysis Intelligence Index v4.3.2, up from 41 for its predecessor. These gains highlight the model's improved capabilities in complex reasoning, multi-step task execution, and agentic workflows across diverse real-world scenarios.
Model Overview
The table and diagram below summarize the model’s specifications and architecture.
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
- -
