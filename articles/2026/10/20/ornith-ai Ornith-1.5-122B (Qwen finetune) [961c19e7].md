---
id: "961c19e76e6ab3da"
title: "ornith-ai/Ornith-1.5-122B (Qwen finetune)"
url: "https://huggingface.co/ornith-ai/Ornith-1.5-122B"
link: "https://huggingface.co/ornith-ai/Ornith-1.5-122B"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-20T14:19:07Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["jacek2023"]
language: "en"
summary: "from Ornith: Ornith-1.5-122B Chirp Chirp! 🐦 We are introducing Ornith-1.5, a major step toward building foundation models through end-to-end self-improvement. Ornith-1.5 extends Ornith-1.0 (which was developed on top of Qwen3.5 and Gemma4 with additional continued pretraining, mid-training, and post-training) by expanding the self-improvement loop from scaffold and rollout optimization to…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "OpenAI", "Alibaba", "Google"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 1561
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xatebw/ornithaiornith15122b_qwen_finetune/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# ornith-ai/Ornith-1.5-122B (Qwen finetune)

Hugging Face · jacek2023 · 2026-10-20

Instructions to use ornith-ai/Ornith-1.5-122B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use ornith-ai/Ornith-1.5-122B with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="ornith-ai/Ornith-1.5-122B")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModelForMultimodalLM
processor = AutoProcessor.from_pretrained("ornith-ai/Ornith-1.5-122B")
model = AutoModelForMultimodalLM.from_pretrained("ornith-ai/Ornith-1.5-122B", device_map="auto")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
inputs = processor.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(processor.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use ornith-ai/Ornith-1.5-122B with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "ornith-ai/Ornith-1.5-122B"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "ornith-ai/Ornith-1.5-122B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/ornith-ai/Ornith-1.5-122B
-  SGLang  How to use ornith-ai/Ornith-1.5-122B with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "ornith-ai/Ornith-1.5-122B" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "ornith-ai/Ornith-1.5-122B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "ornith-ai/Ornith-1.5-122B" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "ornith-ai/Ornith-1.5-122B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use ornith-ai/Ornith-1.5-122B with Docker Model Runner: docker model run hf.co/ornith-ai/Ornith-1.5-122B
Ornith-1.5-122B
Chirp Chirp! 🐦 We are introducing Ornith-1.5, a major step toward building foundation models through end-to-end self-improvement.
Ornith-1.5 extends Ornith-1.0 (which was developed on top of Qwen3.5 and Gemma4 with additional continued pretraining, mid-training, and post-training) by expanding the self-improvement loop from scaffold and rollout optimization to jointly optimizing task generation, scaffold construction, and solution rollouts. Rather than relying on a fixed set of human-curated tasks and manually designed harnesses, Ornith-1.5 continuously generates new training tasks, discovers effective strategies for solving them, and improves the policy through reinforcement learning. For more details on the task, harness, and rollout reward design, please refer to our blog.
Ornith 1.5 122B
This model card documents Ornith-1.5-122B, the most capable and efficient.member of the Ornith-1.5 family — a 122B MOE model designed for efficient single-GPU deployment, and edge-deployable on mobile devices via its quantized Ornith-1.5-122B-Mobile variant.
Benchmarks
 * Terminal-Bench 2.1 (Claude Code): We evaluate Terminal-Bench 2.1 using Claude Code 2.1.126 with parser=json, temperature=1.0, top_p=1.0, max_new_tokens=131072. Results are averaged over 5 runs. Again, Qwen chat template needs to be modified.
* SWE-Bench Verified, Pro, and Multilingual: Evaluated using the OpenHands harness with temperature=1.0, top_p=0.95, and a 256K context window. Anti-hacking safeguards are applied throughout evaluation: models are explicitly informed of potential reward-hacking behaviors and instructed to avoid them. Any solution that still exhibits such behavior is marked incorrect.
* NL2Repo: with temperature=1.0, top_p=1.0, 400K context, 48K output. Access to specified GitHub repositories and pip packages is blocked to prevent reward hacking.
* HLE: Evaluated using Claude 4.6 Opus as the judge model.
* MCP-Atlas: All models were evaluated in thinking mode on the 500-task public subset, with a 10-minute timeout per task. We use Claude 4.8 Opus as the judge model.
* Toolathlon-Verified: We use the official evaluation service with the maximum token limit set to 128K.
* ClawEval: An agentic code benchmark over real-user task distributions; temp=0.6 and 256K context.
Quickstart
Ornith-1.5-122B is a reasoning model: by default the assistant turn opens with a <think> … </think> block before the final answer. The serving recipes below enable a reasoning parser so the chain-of-thought is returned in a separate reasoning_content field, and a tool-call parser so the model's <tool_call> blocks are surfaced as OpenAI-style tool_calls.
Serving Ornith-1.5-122B requires recent runtimes:
- Transformers ≥ 5.8.1
- vLLM ≥ 0.19.1
- SGLang ≥ 0.5.9
Recommended sampling parameters:
- For general tasks: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
- For precise coding tasks: temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
Serving Ornith-1.5-122B
Ornith-1.5-122B is a MOE 122B model, so it serves on a single 80GB GPU. The recipes below stand up an OpenAI-compatible server; add --tensor-parallel-size / --tp if you want to shard across more GPUs.
- vLLM
vllm serve ornith-ai/Ornith-1.5-122B --served-model-name Ornith-1.5-122B --host 0.0.0.0 --port 8000 --max-model-len 262144 --gpu-memory-utilization 0.90 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_xml --reasoning-parser qwen3 --trust-remote-code
- SGLang
python -m sglang.launch_server --model-path ornith-ai/Ornith-1.5-122B --served-model-name Ornith-1.5-122B --host 0.0.0.0 --port 8000 --context-length 262144 --mem-fraction-static 0.85 --tool-call-parser qwen3_coder --reasoning-parser qwen3
For Long-Context
Ornith-1.5-122B handles context windows of up to 262,144 tokens. When a task's combined input and output must go beyond this limit, we suggest extending the effective window with RoPE scaling — YaRN is the technique we validate against, and it is already built into both vLLM and SGLang. With a scaling factor of 4.0, the usable window grows to roughly 1M tokens.
You can turn YaRN on in either of two ways:
- Edit the checkpoint's config.json. Add a rope_scaling block to the model configuration:
{
    "rope_scaling": {
        "rope_type": "yarn",
        "factor": 4.0,
        "original_max_position_embeddings": 262144
    }
}
- Override at launch time. Leave the checkpoint untouched and extend the serve commands above with the equivalent flags. vLLM: VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve ornith-ai/Ornith-1.5-122B ... --hf-overrides '{"rope_scaling": {"rope_type": "yarn", "factor": 4.0, "original_max_position_embeddings": 262144}}' --max-model-len 1000000
SGLang: SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python -m sglang.launch_server ... --json-model-override-args '{"rope_scaling": {"rope_type": "yarn", "factor": 4.0, "original_max_position_embeddings": 262144}}' --context-length 1000000
Open-source runtimes implement YaRN statically: the same scaling factor is applied to every request regardless of its length, which can slightly hurt quality on ordinary-length inputs. Only enable rope_scaling when your workload genuinely needs the longer window, and size factor to match it — the target window is roughly factor × 262,144, so if your requests top out around 524,288 tokens, factor: 2.0 is the better setting.
Using Ornith-1.5-122B via the Chat Completions API
Once a vLLM or SGLang server is running, talk to it with any OpenAI-compatible client.
Basic Usage
from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",  # any non-empty string works for a local server
)
response = client.chat.completions.create(
    model="Ornith-1.5-122B",
    messages=[
        {"role": "user", "content": "Write a one-line Python lambda that squares a number."}
    ],
    temperature=0.6,
    top_p=0.95,
    max_tokens=1024,
)
message = response.choices[0].message
# reasoning_content holds the <think> trace; content holds the final answer.
print("reasoning:", getattr(message, "reasoning_content", None))
print("answer:", message.content)
You can also stream tokens, or hand the model tools — Ornith-1.5-122B emits well-formed function calls that the server parses into the standard tool_calls field:
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }
]
response = client.chat.completions.create(
    model="Ornith-1.5-122B",
    messages=[{"role": "user", "content": "What is the weather in Paris right now?"}],
    tools=tools,
    tool_choice="auto",
    temperature=0.6,
    max_tokens=2048,
)
tool_call = response.choices[0].message.tool_calls[0]
print(tool_call.function.name, tool_call.function.arguments)
# -> get_weather {"city": "Paris"}
You can point any OpenAI-compatible SDK (Python, Node.js, etc.) or curl at the same /v1/chat/completions endpoint.
Agentic Usage
Ornith-1.5-122B exposes an OpenAI-compatible endpoint with tool calling, it works out of the box with standard agent frameworks.
Examples of using Ornith with agents:
Ollama
ollama run ornith-1.5:122b
Atomic.chat
# Both runtimes load a GGUF build of Ornith (publish one at ornith-ai/Ornith-1.5-122B-GGUF).
# llama.cpp — serve an OpenAI-compatible API on port 8000.
llama-server -hf hf.co/ornith-ai/Ornith-1.5-122B-GGUF --port 8000 -c 262144
llama.cpp
# Both runtimes load a GGUF build of Ornith (publish one at ornith-ai/Ornith-1.5-122B-GGUF).
# llama.cpp — serve an OpenAI-compatible API on port 8000.
llama-server -hf hf.co/ornith-ai/Ornith-1.5-122B-GGUF --port 8000 -c 262144
Hermes Agent
# Hermes talks to any OpenAI-compatible endpoint — point it at your Ornith server.
export OPENAI_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="EMPTY"
export MODEL="ornith-ai/Ornith-1.5-122B"
OpenClaw
# OpenClaw talks to any OpenAI-compatible endpoint — point it at your Ornith server.
export OPENAI_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="EMPTY"
export OPENAI_MODEL="ornith-ai/Ornith-1.5-122B"
Unsloth Studio
pip install unsloth
# Load Ornith for fast local inference or fine-tuning (Python):
#   from unsloth import FastLanguageModel
#   model, tokenizer = FastLanguageModel.from_pretrained(
#       "unsloth/Ornith-1.5-122B-GGUF",
#       max_seq_length=262144,
#       load_in_4bit=True,
#   )
Coding CLIs
Ornith-1.5-122B is optimized for terminal-based coding agents. Point any OpenAI-compatible coding CLI at your Ornith-1.5-122B endpoint (set OPENAI_BASE_URL and OPENAI_API_KEY) to understand large codebases, automate tedious work, and ship faster.
OpenCode
# Register your local Ornith endpoint as a provider in ~/.config/opencode/opencode.json:
#
# {
#   "$schema": "https://opencode.ai/config.json",
#   "provider": {
#     "ornith": {
#       "npm": "@ai-sdk/openai-compatible",
#       "name": "Ornith (local)",
#       "options": { "baseURL": "http://localhost:8000/v1", "apiKey": "EMPTY" },
#       "models": { "ornith-ai/Ornith-1.5-122B": { "name": "Ornith-1.5-122B" } }
#     }
#   }
# }
opencode
Citation
If you find our work helpful, feel free to give us a cite.
@misc{ornith_1_5,
    title = {{Ornith-1.5}: From Self-Scaffolding to Self-Improvement},
    url = {https://ornith.ai/ornith_1_5.html},
    author = {{Ornith Team}},
    year = {2026}
}
- Downloads last month
- 742
