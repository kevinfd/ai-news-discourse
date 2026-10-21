---
id: "7a63cba0df798fe2"
title: "Agnes-AI/Agnes-3.0-Qwen (QFN finetune)"
url: "https://huggingface.co/Agnes-AI/Agnes-3.0-Qwen"
link: "https://huggingface.co/Agnes-AI/Agnes-3.0-Qwen"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-20T17:11:43Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["jacek2023"]
language: "en"
summary: "https://huggingface.co/bartowski/Agnes-AI_Agnes-3.0-Qwen-GGUF Strong agentic performance: agnes-3.0-qwen scores highest in its comparison set on τ³-Banking, and is within about one point of the best model on Terminal-Bench 2.1, while being a much smaller model than most of the flagship systems it is compared against. Reliable instruction following: on IFBench, agnes-3.0-qwen outperforms GPT-5.6…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Alibaba", "Anthropic", "Google", "DeepSeek"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 890
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xaxz80/agnesaiagnes30qwen_qfn_finetune/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Agnes-AI/Agnes-3.0-Qwen (QFN finetune)

Hugging Face · jacek2023 · 2026-10-20

agnes-3.0-qwen
Hello! 👋 Today we are introducing agnes-3.0-qwen, our most capable reasoning model for agentic coding, tool use, scientific problem solving, long-context analysis, and multimodal understanding.
Highlights:
- Strong agentic performance: agnes-3.0-qwen scores highest in its comparison set on τ³-Banking, and is within about one point of the best model on Terminal-Bench 2.1, while being a much smaller model than most of the flagship systems it is compared against.
- Reliable instruction following: on IFBench, agnes-3.0-qwen outperforms GPT-5.6 Sol (Max) and Claude Opus 4.8 (Max).
- Built for demanding work: a 1M-token context window, extended reasoning with selectable reasoning effort (xhigh, medium, low), tool calling, and text, image, and video understanding.
agnes-3.0-qwen
A multimodal reasoning model available as open weights. The model is a hybrid linear-attention / full-attention Mixture-of-Experts architecture (512 experts, 10 active per token) with a multi-token-prediction head, combining long-context understanding with strong coding, agentic, and scientific reasoning at the throughput and cost needed for production workloads.
Benchmarks
agnes-3.0-qwen is compared against GPT-5.6 Sol (Max), Gemini 3.8 Flash, DeepSeek V4 Flash (Max), MiniMax-M3, Claude Opus 4.8 (Max), and Qwen3.8 Max (0902). Results for agnes-3.0-qwen are self-reported on publicly available benchmarks; comparison figures are taken from public reports.
Higher is better for every benchmark. agnes-3.0-qwen figures are self-reported; comparison model figures are taken from publicly available reports and may change as evaluations are updated. "—" indicates no published result. Snapshot checked October 10, 2026.
Model Information
License
agnes-3.0-qwen is a post-trained derivative of Qwen/Qwen3.8-Flash-Next. Additional post-training was performed by Agnes AI. The model weights and inherited upstream artifacts are distributed under the Qwen Community License 1.0.
All use and redistribution must comply with the full terms in LICENSE. The original Qwen copyright and permission notices must be retained in all copies or substantial portions of the upstream software. See NOTICE for attribution and Agnes AI's post-training contribution.
Commercial use conditions (summary; the full license controls):
- If the licensee or any of its affiliates conducts a Model as a Service (MaaS) or AI Work Assistant business, a separate license from Qwen is required before using the model or its derivative works for any commercial purpose. The internal-use exception applies only when the software, its outputs, and its underlying model capabilities are not made available to any third party. See LICENSE for the definitions and exclusions for these businesses.
- If a commercial product or service using the model or its derivative works has more than 100,000,000 monthly active users or more than US$20,000,000 in monthly revenue (or the equivalent in other currencies), the respective model name must be prominently displayed on its user interface. This display condition is separate from the commercial licensing requirement above.
The API examples in this README do not grant additional commercial rights under the upstream license. Any separate commercial authorization must be obtained from Qwen; the contact listed in LICENSE is model-business@notice.qwencloud.com.
Hardware Requirements
The Quickstart launch command uses 8-GPU tensor parallelism. The checkpoint is a 119-shard BF16 package of about 360 GB; a single GPU is not sufficient.
Quickstart
agnes-3.0-qwen uses extended reasoning for complex tasks and is available through OpenAI-compatible Chat Completions and Responses APIs. Keep API keys in environment variables and use publicly accessible URLs for image inputs.
SGLang
python -m sglang.launch_server \
    --model-path Agnes-AI/agnes-3.0-qwen \
    --served-model-name agnes-3.0-qwen \
    --tp 8 \
    --host 0.0.0.0 --port 8000 \
    --context-length 1024000 \
    --mem-fraction-static 0.85 \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3
Chat Completions
export AGNES_API_KEY="your-api-key"
curl https://apihub.agnes-ai.com/v1/chat/completions \
  -H "Authorization: Bearer ${AGNES_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-3.0-qwen",
    "messages": [
      {
        "role": "user",
        "content": "Review this API handler for security issues and provide a corrected version."
      }
    ],
    "temperature": 1.0,
    "max_tokens": 4000
  }'
Python
pip install openai
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["AGNES_API_KEY"],
    base_url="https://apihub.agnes-ai.com/v1",
)
response = client.chat.completions.create(
    model="agnes-3.0-qwen",
    messages=[
        {
            "role": "user",
            "content": "Design a fault-tolerant event processing architecture.",
        }
    ],
    temperature=1.0,
    max_tokens=4000,
)
print(response.choices[0].message.content)
Reasoning Effort
The chat template accepts a reasoning_effort argument (xhigh by default, or medium / low) and an enable_thinking switch. With an OpenAI-compatible server these are passed through extra_body:
response = client.chat.completions.create(
    model="agnes-3.0-qwen",
    messages=[{"role": "user", "content": "Summarize the trade-offs of event sourcing in three bullets."}],
    extra_body={"chat_template_kwargs": {"reasoning_effort": "low"}},
)
Set {"enable_thinking": False} to disable extended reasoning entirely for latency-sensitive calls.
Image Understanding
response = client.chat.completions.create(
    model="agnes-3.0-qwen",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Explain this chart and call out anomalies."},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/chart.png"},
                },
            ],
        }
    ],
)
Responses API
curl https://apihub.agnes-ai.com/v1/responses \
  -H "Authorization: Bearer ${AGNES_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-3.0-qwen",
    "input": "Create a step-by-step migration plan from a monolith to services.",
    "max_output_tokens": 4000
  }'
Recommended Inference Settings
Use sampling rather than greedy decoding. Leave enough max_tokens / max_output_tokens for extended reasoning.
Raise max_tokens if a response stops early.
Model Capabilities
agnes-3.0-qwen is especially well suited to terminal and repository-level coding agents, tool-enabled customer workflows, technical research, document synthesis, and visual analysis that need to reason across long and complex contexts.
Responsible Use
Model outputs can contain errors. Validate high-impact decisions and tool actions in the application layer, and review the applicable Agnes AI service terms before sending sensitive or regulated data.
Citation
@misc{agnes30qwen2026,
  title        = {agnes-3.0-qwen},
  author       = {{Agnes AI}},
  year         = {2026},
  month        = oct,
  howpublished = {Open-weight model},
  url          = {https://huggingface.co/Agnes-AI/agnes-3.0-qwen}
}
- Downloads last month
- 235
