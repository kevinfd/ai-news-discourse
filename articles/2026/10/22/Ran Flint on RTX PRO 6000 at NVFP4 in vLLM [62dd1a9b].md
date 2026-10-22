---
id: "62dd1a9b1d38c59d"
title: "Ran Flint on RTX PRO 6000 at NVFP4 in vLLM"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc6j8t/ran_flint_on_rtx_pro_6000_at_nvfp4_in_vllm"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc6j8t/ran_flint_on_rtx_pro_6000_at_nvfp4_in_vllm"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T02:24:05Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["DataCraftsman"]
language: "en"
summary: "Manged to get Flint running in vLLM (with the flint PR) on my RTX 6000 Pro. The model was using my harness well, using OKF knowledge base, doing webscraping, spoke in the character I gave it, etc. I ran a couple of their benchmarks (45 of the 454 LiveCodeBench v6 problems and 50 of the 500 SWE-bench Verified tasks) because I wanted to see if it could actually code, these were my results:…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 352
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc6j8t/ran_flint_on_rtx_pro_6000_at_nvfp4_in_vllm/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ran Flint on RTX PRO 6000 at NVFP4 in vLLM

Reddit · DataCraftsman · 2026-10-22

Manged to get Flint running in vLLM (with the flint PR) on my RTX 6000 Pro. The model was using my harness well, using OKF knowledge base, doing webscraping, spoke in the character I gave it, etc. I ran a couple of their benchmarks (45 of the 454 LiveCodeBench v6 problems and 50 of the 500 SWE-bench Verified tasks) because I wanted to see if it could actually code, these were my results: LiveCodeBench v6: 82.2, they said 80.8 SWE-bench Verified: 80, they said 74.1 Does about 110-180 tok/s single stream, I saw peaks of like 2,500 tok/s with 64 reqs. Seems like a good daily model, I am going to see if the speed gain is worth dropping qwen3.8 27b over. There are some issues with the chat_template.yml atm but I included a fix below. Just hoping someone finds a hacky way to give it vision. This was my docker compose for vllm: vllm: image: vllm/vllm-openai:flint-8e2beaa3-pr62938 restart: unless-stopped cap_drop: - ALL cap_add: - SETUID - SETGID ipc: host ulimits: memlock: -1 ports: - "localhost:8000" entrypoint: ["/bin/bash", "-c"] command: - | set -e rm -rf /usr/local/cuda-*/compat/ && ldconfig vllm serve /models/flint \ --hf-config-path /models/flint \ --tokenizer /models/flint \ --generation-config /models/flint \ --chat-template /app/flint_chat_template.jinja \ --served-model-name vllm \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 262144 \ --reasoning-parser glm47 \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --exclude-tools-when-tool-choice-none \ --max-num-seqs 64 \ --max-num-batched-tokens 8192 \ --gpu-memory-utilization 0.65 \ --enable-prefix-caching \ --enable-prompt-tokens-details \ --enable-force-include-usage \ --uvicorn-log-level warning runtime: nvidia deploy: resources: reservations: devices: - capabilities: [gpu] device_ids: ['1'] driver: nvidia healthcheck: test: ["CMD", "curl", "-f", "http://localhost:8000/health"] interval: 15s timeout: 30s retries: 60 start_period: 900s start_interval: 10s volumes: - ./models/Flint/NVFP4-GGUF:/models/flint:ro - ./flint/chat_template.jinja:/app/flint_chat_template.jinja:ro - huggingface:/root/.cache/huggingface - vllm_cache:/root/.cache/vllm - flashinfer_cache:/root/.flashinfer environment: - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN} - HF_HUB_OFFLINE=1 - VLLM_USE_RUST_FRONTEND=0 - OMP_NUM_THREADS=1 - TORCHINDUCTOR_CACHE_DIR=/root/.cache/vllm/inductor - TRITON_CACHE_DIR=/root/.cache/vllm/triton logging: driver: "json-file" options: max-size: "50m" max-file: "5" and chat_template.jinja change: {%- if add_generation_prompt -%} <|assistant|> {%- if enable_thinking is defined and enable_thinking is false -%} {%- if tools -%} <think>We need respond, using a tool if the request needs one.</think> {%- else -%} <think>We need answer.</think> {%- endif -%} {%- endif -%} {%- endif -%}
