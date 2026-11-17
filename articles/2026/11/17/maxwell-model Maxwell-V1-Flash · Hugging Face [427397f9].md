---
id: "427397f9a75af9e1"
title: "maxwell-model/Maxwell-V1-Flash · Hugging Face"
url: "https://huggingface.co/maxwell-model/Maxwell-V1-Flash"
link: "https://huggingface.co/maxwell-model/Maxwell-V1-Flash"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-17T04:04:39Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["pmttyji"]
language: "en"
summary: "Model Introduction Maxwell-V1.0-Flash is a next-generation, high-performance Mixture-of-Experts (MoE) language model developed by the Maxwell Team, with 35B total parameters and 3B active parameters per token (both excluding embeddings) and support for context lengths up to 256K tokens. It is designed for strong reasoning, agentic, and long-context capabilities at a practical inference cost. Key…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face", "Anthropic", "Nvidia", "Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "jobs & society"]
content_source: "fulltext"
word_count: 846
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyamk6/maxwellmodelmaxwellv1flash_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# maxwell-model/Maxwell-V1-Flash · Hugging Face

Hugging Face · pmttyji · 2026-11-17

1. Model Introduction
Maxwell-V1.0-Flash is a next-generation, high-performance Mixture-of-Experts (MoE) language model developed by the Maxwell Team, with 35B total parameters and 3B active parameters per token (both excluding embeddings) and support for context lengths up to 256K tokens. It is designed for strong reasoning, agentic, and long-context capabilities at a practical inference cost.
Key Features
- Maxwell Block Sparse Attention (MBSA). Each KV group keeps fixed coverage of 8 prefix and 8 local 128-token blocks and adds up to 16 remote blocks chosen by a learned indexer, bounding main attention at 4,096 tokens per KV group while the full-history KV cache stays available. The MBSA kernel is 6.7x faster than dense GQA at 256K.
- Manifold-Constrained Hyper-Connections. Multiple residual streams with learned, input-dependent aggregation and constrained mixing, widening information flow without extra attention or feed-forward evaluations.
- Fine-Grained Mixture of Experts. A mostly-MoE backbone pairing fine-grained routed experts with always-active shared experts, using a dynamic routing correction bias alongside a lightweight sequence-wise load-balancing loss.
Pre-training. Approximately 26T tokens of multilingual data, with the Muon optimizer on most hidden weight matrices. Training starts dense; block-sparse attention enters at 128K mid-training, once the indexer is warmed up against dense full-history attention, then trains jointly with the backbone.
Tokenizer and Long Context. A script-aware multilingual tokenizer stays compact across languages, especially low-resource Southeast Asian ones such as Thai, Lao, Myanmar, Khmer, and Shan. Long-context training then extends the sequence length in stages from 4K to 256K.
Post-training. Two-stage all-domain SFT builds general, reasoning, and agentic capabilities, then targets harder reasoning problems and agent trajectories. Independent RL branches cover general tasks, verifiable reasoning (mathematics, science, logic, code), and agentic tasks (search, terminal use, function calling, software engineering). Multi-teacher on-policy distillation then merges them into one model by supervising student-generated responses.
The results below summarize Maxwell-V1.0-Flash's performance across reasoning, agentic search, and other capabilities alongside the evaluated comparison models.
2. Model Specifications
The block budget applies in sparse-attention mode. The MTP layer is auxiliary and is not included in the backbone layer count.
3. Evaluation Results
Base model. Maxwell-V1.0-Flash (Base) is compared with two Qwen base models of comparable scale under a unified internal evaluation framework. All scores are percentages; the best score in each row is shown in bold. GSM8K is evaluated using pass@8.
Base model, long context. Scores are on a 0–100 scale. All results use block-sparse attention in every layer.
Post-trained model. Maxwell-V1.0-Flash is compared with four models of comparable scale: Qwen3.6-35B-A3B, which has the same nominal 35B total / 3B active parameter scale, together with Gemma-4-26B-A4B-it, Nemotron-3.5-Lightning, and Muse-Glimmer-30B. All scores are percentages; the highest score for each metric is shown in bold. Multilingual results cover only market languages.
* Maxwell with context management enabled.
Post-training evaluations mostly use temperature 0.6, top-p 0.95, top-k 20, and a 32K-token context. AA-LCR, mathematical benchmarks, and HLE use 128K; scientific benchmarks use 80K; LiveCodeBench v6 uses 64K; multilingual evaluation uses a maximum generation length of 16K tokens. SWE-Bench Verified is evaluated with the Claude Code harness (version 2.1.212) in a network-isolated environment, with a 256K-token context window, at most 240 interaction turns, and a four-hour wall-clock limit per task. Terminal-Bench 2.1 is evaluated in the Harbor framework with the Terminus-2 harness, using a two-hour timeout per task, a 256K-token context window, 32K max tokens, temperature 1.0, top-p 0.95, top-k 20, and interleaved thinking.
The scientific average excludes HLE.
4. Deployment
Requires NVIDIA driver >= 580 (CUDA 13.0). On older drivers, add
-e VLLM_ENABLE_CUDA_COMPATIBILITY=1 to docker run.
Download the weights to a local directory first with the Hugging Face CLI
(install it with pip install -U huggingface_hub if hf is not available):
export MODEL_DIR=$PWD/Maxwell-V1-Flash
hf download maxwell-model/Maxwell-V1-Flash --local-dir "$MODEL_DIR"
Start the vLLM OpenAI-compatible server:
docker run --rm --init \
  --name vllm-maxwell \
  --gpus all \
  --shm-size 8g \
  --network host \
  -v "$MODEL_DIR":/models/Maxwell-V1-Flash:ro \
  --entrypoint vllm \
  maxwellmodel/vllm-openai:v0.30.0 \
  serve /models/Maxwell-V1-Flash \
  --trust-remote-code \
  --block-size 128 \
  --served-model-name Maxwell-V1.0-Flash \
  --port 8000 \
  --tensor-parallel-size 1 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
  You can also try Maxwell-V1.0-Flash at https://maxwell-llm.ai/playground.
5. Model Usage
Maxwell-V1.0-Flash uses the bundled chat template for system, user, assistant,
and tool messages, with thinking enabled by default. For multi-turn
conversations and tool calls, pass the complete assistant message back into
messages, including reasoning_content and tool_calls when present.
OpenAI-compatible tool definitions are accepted through the tools field.
import openai
def chat_completion(
    client: openai.OpenAI,
    model_name: str,
) -> str:
    messages = [
        {
            "role": "user",
            "content": (
                "Why is it harder to keep a room cool when the door is open "
                "on a hot day? Explain in 3-4 simple sentences."
            ),
        },
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        max_tokens=4096,
        temperature=0.6,
        top_p=0.95,
        extra_body={
            "top_k": 20,
            "chat_template_kwargs": {
                "enable_thinking": True,
            },
        },
    )
    return response.choices[0].message.content
For full guides and examples, see the Maxwell-V1.0-Flash Quickstart.
6. License
Maxwell-V1.0-Flash is released under the Apache License 2.0. See LICENSE for details.
7. Contact Us
If you have any questions or suggestions, feel free to reach out to our R&D and product teams via email: contact@maxwell-llm.ai
- Downloads last month
- 287
