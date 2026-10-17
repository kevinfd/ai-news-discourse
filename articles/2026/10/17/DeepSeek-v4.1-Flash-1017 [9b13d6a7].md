---
id: "9b13d6a721a0c270"
title: "DeepSeek-v4.1-Flash-1017"
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
link: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "hackernews"
date: "2026-10-17T08:21:25Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["theykk"]
language: "en"
summary: "Instructions to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.\n- Libraries\n-  Transformers How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with Transformers: # Use a pipeline as a high-level helper\nfrom transformers import pipeline\npipe = pipeline(\"image-text-to-text\",…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "OpenAI", "Anthropic", "Google"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 554
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50129045"
score: 223
comments: 86
community: "Hacker News"
---

# DeepSeek-v4.1-Flash-1017

Hugging Face · theykk · 2026-10-17

Instructions to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="deepseek-ai/DeepSeek-V4.1-Flash-1017") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-V4.1-Flash-1017", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "deepseek-ai/DeepSeek-V4.1-Flash-1017"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker docker model run hf.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
-  SGLang  How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "deepseek-ai/DeepSeek-V4.1-Flash-1017" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "deepseek-ai/DeepSeek-V4.1-Flash-1017" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4.1-Flash-1017",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
-  Docker Model Runner  How to use deepseek-ai/DeepSeek-V4.1-Flash-1017 with Docker Model Runner: docker model run hf.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
DeepSeek-V4.1-Flash-1017
Introduction
DeepSeek-V4.1-Flash-1017 is a minor update to DeepSeek-V4.1-Flash, delivering substantial improvements across reasoning, coding, agentic tasks, and visual benchmarks. Alongside these gains, the model reduces task execution time and output length, enabling users to complete tasks faster and at lower cost and advancing the performance–cost Pareto frontier across multiple agent harnesses.
† denotes the text-only subset of HLE. We use the Claude Code harness for Terminal-Bench 4.0 and the Mini-SWE-V2 harness for DeepSWE v1.1.
Prompt Encoding
This release does not include a Jinja-format chat template. The encoding folder contains a self-contained Python reference implementation (encoding.py) with test cases for multi-turn conversations, tool calling, thinking mode, numeric reasoning effort, mid-conversation system messages, and interleaved image content.
For production use, we additionally release deepseek-recipe, a set of Rust libraries with Python bindings that provides the same prompt format as a maintained, protocol-aware toolkit. It converts Messages, Chat Completions, and Responses API requests into the Conversation format, encodes them into DeepSeek V4 and V4.1 prompts or token IDs, and parses model output back into complete or streamed responses — covering thinking, tool calls, images, and generation settings. Model inference, tool execution, and HTTP transport are left to the caller.
Minimal Inference
Please refer to the inference folder for instructions on weight conversion and running inference locally.
Recommended sampling parameters:
License
This repository and the model weights are licensed under the MIT License.
Citation
@misc{deepseekai2026deepseekv41flash,
      title={DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression},
      author={DeepSeek-AI},
      year={2026},
}
Contact
If you have any questions, please raise an issue or contact us at service@deepseek.com.
- Downloads last month
- -
