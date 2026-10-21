---
id: "2e829f1f359a9f86"
title: "KRAFTON/Raon-1-mini-preview · Hugging Face"
url: "https://huggingface.co/KRAFTON/Raon-1-mini-preview"
link: "https://huggingface.co/KRAFTON/Raon-1-mini-preview"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-21T07:54:08Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["jacek2023"]
language: "en"
summary: "Raon-1 mini is a 30B-A4B Mixture-of-Experts (MoE) language model, designed and trained from scratch by KRAFTON AI . It demonstrates strong capabilities in Korean conversation and agentic tasks . As part of the Raon open model family, it is released under the Apache 2.0 license . https://huggingface.co/KRAFTON/Raon-1-mini-preview-gguf Highlights Reasoning : Built-in thinking, with leading results…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Nvidia", "Google", "DeepSeek", "Hugging Face", "China"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "search & media"]
content_source: "fulltext"
word_count: 2457
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbh0ev/kraftonraon1minipreview_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# KRAFTON/Raon-1-mini-preview · Hugging Face

Hugging Face · jacek2023 · 2026-10-21

Instructions to use KRAFTON/Raon-1-mini-preview with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use KRAFTON/Raon-1-mini-preview with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="KRAFTON/Raon-1-mini-preview", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("KRAFTON/Raon-1-mini-preview", trust_remote_code=True, device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use KRAFTON/Raon-1-mini-preview with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "KRAFTON/Raon-1-mini-preview"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "KRAFTON/Raon-1-mini-preview",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/KRAFTON/Raon-1-mini-preview
-  SGLang  How to use KRAFTON/Raon-1-mini-preview with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "KRAFTON/Raon-1-mini-preview" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "KRAFTON/Raon-1-mini-preview",
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
        --model-path "KRAFTON/Raon-1-mini-preview" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "KRAFTON/Raon-1-mini-preview",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use KRAFTON/Raon-1-mini-preview with Docker Model Runner: docker model run hf.co/KRAFTON/Raon-1-mini-preview
Raon-1 mini
Raon-1 mini is a 30B-A4B Mixture-of-Experts (MoE) language model, designed and trained from scratch by KRAFTON AI. It demonstrates strong capabilities in Korean conversation and agentic tasks. As part of the Raon open model family, it is released under the Apache 2.0 license.
Want to try Raon-1 mini without setting anything up?
Chat with it for free, for a limited time, in the Raon-1 mini playground.
This is a preview release, not a final model. Specs and results may change before the final version.
Highlights
- Reasoning: Built-in thinking, with leading results on the math and science benchmarks shown below.
- Instruction following and search: Leads the comparison models on the instruction-following and search benchmarks shown below.
- Multilingual capabilities: Trained on Korean, English, Japanese, Chinese, Spanish, French, and Thai. Demonstrates strong Korean performance and solid English capabilities.
- Agent execution: Tool calling for agentic workflows, with support for Hermes Agent, Pi and OpenCode.
- Speculative decoding support: A DFlash2 draft model is provided for accelerated speculative decoding.
- Quantization options: Available in MXFP8 and NVFP4 formats, with NVFP4 enabling inference on a single NVIDIA RTX 5090 gpu (32 GB VRAM).
Model Overview
Raon-1 mini uses a hybrid Mixture-of-Experts (MoE) architecture, consisting of 18 linear attention layers and 7 full attention layers.
- Raon Delta Attention (RDA): Raon Delta Attention decouples the erase and write gates of Kimi Delta Attention, which improves long-context performance over KDA.
- Raon-mHC: Raon-mHC reduces the computational cost of DeepSeek’s manifold-constrained hyper-connections (mHC), which speeds up training.
- Hybrid layout: 18 of the 25 layers are Raon Delta Attention layers with a fixed-size state. Only the 7 MLA layers keep a KV cache, about 8 KiB per token in BF16.
- Long context: Natively supports up to 262,144 tokens of context.
- Sparse MoE: 6 of 128 routed experts plus 1 shared expert are active per token, so each token uses 4.3B of the 28.8B total parameters.
Benchmark Results
- Red indicates the best performance of Raon-1 mini preview among MoE baselines.
Judge and user simulator: gpt-5.6-luna for all evaluations.
Red = Raon-1 mini preview is best within the MoE group (Raon-1 mini preview, Qwen3.6-35B-A3B, Gemma 4 26B-A4B). Dense models (Qwen3.8-27B, Muse Glimmer 30B) are shown for reference only.
¹ SWE-Verified: evaluated with the mini-SWE-agent harness.
² GDPVal (dataset): metric is a judge score, not Elo.
³ AutomationBench: public split, not the official evaluation set.
⁴ GDP.pdf: official Artificial Analysis (artificialanalysis.ai) text-only version. PDFs are OCR-ed in advance; no image input.
⁵ Chatbot Korean (internal): an internal benchmark measuring Korean colloquial ability in chatbot conversations across diverse situations. Not publicly released.
Sampling parameters
Raon-1 mini is designed for thinking mode; disabling it is not recommended.
Settings shared by all tasks:
Settings that depend on the task:
Speculative Decoding
We release a DFlash2 draft model alongside Raon-1 mini preview to accelerate inference through speculative decoding. In our benchmarks on a single NVIDIA B300, it delivers up to 2.18× higher output throughput than autoregressive decoding. Speedups vary by hardware and workload.
Throughput is measured in output tok/s, with speedup over autoregressive decoding in parentheses. Acceptance length (AL) is the mean number of tokens per verification step, averaged across requests at concurrency 1.
Evaluated with vLLM 0.28.0 and an MXFP8 target model; block size 8 (7 draft tokens), probabilistic draft sampling, temperature 1.0, top-p 0.95, top-k 20, thinking enabled, up to 4,096 new tokens, and 128 prompts per benchmark (80 for MT-Bench).
Quickstart
Raon-1 mini supports inference with Transformers, vLLM, llama.cpp, and MLX. The examples below show how to run the model locally or launch an OpenAI-compatible server, using thinking mode and the recommended sampling settings above.
The model repositories are gated. Request access once on this page (approval is automatic; it covers every Raon-1 mini preview repository), then log in so the examples below can download them:
pip install -U huggingface_hub
hf auth login
Use Hugging Face Transformers to load Raon-1 mini and generate responses directly in Python.
Install the dependencies:
uv venv --python 3.12 --seed
source .venv/bin/activate
pip install \
    "transformers==5.16.1" \
    "accelerate==1.15.0"
Then run the model:
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "KRAFTON/Raon-1-mini-preview"
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
messages = [
    {"role": "user", "content": "Tell me about KRAFTON AI."}
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    enable_thinking=True,
    truncate_history_thinking=False,
).to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=32768,
    do_sample=True,
    temperature=1.0,
    top_p=0.95,
    top_k=20,
    min_p=0.0,
    repetition_penalty=1.0,
    presence_penalty=1.5,
)
# The reasoning ends at </think>; the answer follows it.
response = outputs[0][inputs["input_ids"].shape[-1]:].tolist()
think_end = tokenizer.convert_tokens_to_ids("</think>")
split = response.index(think_end) + 1 if think_end in response else 0
reasoning = tokenizer.decode(response[:split], skip_special_tokens=True).strip()
answer = tokenizer.decode(response[split:], skip_special_tokens=True).strip()
print("Reasoning:\n" + reasoning)
print("\nAnswer:\n" + answer)
presence_penalty is applied by the model's remote code, since
Transformers has no built-in presence penalty.
For coding and math, set presence_penalty to 0.0.
vLLM (beta)
Use vLLM to serve Raon-1 mini through an OpenAI-compatible API with tool calling and DFlash2 speculative decoding. Tested on NVIDIA B300.
Install from our fork and start the server:
VLLM_REF="raon-1-mini-preview"
uv venv --python 3.12
source .venv/bin/activate
VLLM_USE_PRECOMPILED=1 uv pip install \
    "vllm @ git+https://github.com/krafton-ai/vllm.git@${VLLM_REF}"
vllm serve KRAFTON/Raon-1-mini-preview \
    --host 127.0.0.1 \
    --port 8000 \
    --served-model-name Raon-1-mini-preview \
    --max-model-len 262144 \
    --max-num-batched-tokens 16384 \
    --max-num-seqs 128 \
    --gpu-memory-utilization 0.85 \
    --kv-cache-dtype fp8_e4m3 \
    --enable-prefix-caching \
    --spec-method dflash \
    --spec-model KRAFTON/Raon-1-mini-preview-dflash2 \
    --spec-tokens 7 \
    --reasoning-parser raon_1 \
    --enable-auto-tool-choice \
    --tool-call-parser raon_1 \
    --default-chat-template-kwargs '{
      "enable_thinking": true,
      "truncate_history_thinking": false
    }'
The first start compiles the model's kernels and takes about 10 minutes;
later starts reuse them.
To serve the NVFP4 checkpoint, replace the model with
KRAFTON/Raon-1-mini-preview-nvfp4 in the same command.
It runs on a single GPU (tensor parallel size 1).
Send a request from another terminal:
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Raon-1-mini-preview",
      "messages": [
        {
          "role": "user",
          "content": "Tell me about KRAFTON AI."
        }
      ],
      "max_tokens": 32768,
      "temperature": 1.0,
      "top_p": 0.95,
      "top_k": 20,
      "min_p": 0.0,
      "repetition_penalty": 1.0,
      "frequency_penalty": 0.0,
      "presence_penalty": 1.5,
      "chat_template_kwargs": {
        "enable_thinking": true,
        "truncate_history_thinking": false
      }
    }'
Reasoning is returned in message.reasoning;
the answer is in message.content.
For coding and math, set presence_penalty to 0.
llama.cpp
Use llama.cpp to run the GGUF checkpoint locally in a terminal or through an OpenAI-compatible API, with optional DFlash2 speculative decoding.
Checkpoint: KRAFTON/Raon-1-mini-preview-gguf
Build from our branch; upstream support is pending. On Windows, see the build guide.
git clone -b raon-1-mini-preview \
    https://github.com/krafton-ai/llama.cpp
cd llama.cpp
# Omit -DGGML_CUDA=ON on Apple silicon.
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j
Start a terminal chat. The model downloads automatically.
./build/bin/llama-cli \
    -hf KRAFTON/Raon-1-mini-preview-gguf:Q4_K_M \
    --ctx-size 262144 \
    --n-predict 32768 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0 \
    --repeat-penalty 1.0 \
    --frequency-penalty 0.0 \
    --presence-penalty 1.5 \
    --reasoning on \
    --chat-template-kwargs '{
      "enable_thinking": true,
      "truncate_history_thinking": false
    }'
Or start an OpenAI-compatible server:
./build/bin/llama-server \
    -hf KRAFTON/Raon-1-mini-preview-gguf:Q4_K_M \
    --host 127.0.0.1 \
    --port 8000 \
    --alias Raon-1-mini-preview \
    --ctx-size 262144 \
    --parallel 1 \
    --n-predict 32768 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0 \
    --repeat-penalty 1.0 \
    --frequency-penalty 0.0 \
    --presence-penalty 1.5 \
    --reasoning on \
    --chat-template-kwargs '{
      "enable_thinking": true,
      "truncate_history_thinking": false
    }'
For coding and math, use --presence-penalty 0.
For DFlash2 speculative decoding, append these options to either
command with a trailing \ on the preceding line.
The draft model downloads automatically.
    --spec-type draft-dflash \
    --spec-draft-n-max 7 \
    --spec-draft-sampling probabilistic
Send a request from another terminal:
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model": "Raon-1-mini-preview",
      "messages": [
        {
          "role": "user",
          "content": "Tell me about KRAFTON AI."
        }
      ],
      "max_tokens": 32768,
      "temperature": 1.0,
      "top_p": 0.95,
      "top_k": 20,
      "min_p": 0.0,
      "repeat_penalty": 1.0,
      "frequency_penalty": 0.0,
      "presence_penalty": 1.5,
      "chat_template_kwargs": {
        "enable_thinking": true,
        "truncate_history_thinking": false
      }
    }'
Reasoning is returned in message.reasoning_content;
the answer is in message.content.
For coding and math, set presence_penalty to 0.
MLX (Apple silicon)
Use MLX to run Raon-1 mini locally on Apple silicon, either directly in Python or through an OpenAI-compatible API.
Checkpoint: KRAFTON/Raon-1-mini-preview-mlx
Install the dependencies with Python 3.11+:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install \
    "mlx==0.32.4" \
    "mlx-lm==0.32.2" \
    "transformers==5.20.1"
Run in Python:
from mlx_lm import load, generate
from mlx_lm.sample_utils import (
    make_logits_processors,
    make_sampler,
)
model, tokenizer = load(
    "KRAFTON/Raon-1-mini-preview-mlx",
    trust_remote_code=True,
)
messages = [
    {"role": "user", "content": "Tell me about KRAFTON AI."}
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True,
    truncate_history_thinking=False,
)
response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=32768,
    sampler=make_sampler(
        temp=1.0,
        top_p=0.95,
        top_k=20,
        min_p=0.0,
    ),
    logits_processors=make_logits_processors(
        repetition_penalty=1.0,
        frequency_penalty=0.0,
        presence_penalty=1.5,
    ),
)
print(response)
Or start an OpenAI-compatible server:
python -m mlx_lm server \
    --model KRAFTON/Raon-1-mini-preview-mlx \
    --trust-remote-code \
    --host 127.0.0.1 \
    --port 8000 \
    --max-tokens 32768 \
    --chat-template-args '{
      "enable_thinking": true,
      "truncate_history_thinking": false
    }' \
    --decode-concurrency 2 \
    --prompt-concurrency 2
Send a request from another terminal:
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model": "default_model",
      "messages": [
        {
          "role": "user",
          "content": "Tell me about KRAFTON AI."
        }
      ],
      "max_tokens": 32768,
      "temperature": 1.0,
      "top_p": 0.95,
      "top_k": 20,
      "min_p": 0.0,
      "repetition_penalty": 1.0,
      "frequency_penalty": 0.0,
      "presence_penalty": 1.5,
      "chat_template_kwargs": {
        "enable_thinking": true,
        "truncate_history_thinking": false
      }
    }'
Use http://localhost:8000/v1 as the base URL
and default_model as the model name.
For coding and math, set presence_penalty to 0.
Agentic Use
Raon-1 mini preview can be used with agent harnesses such as Hermes Agent, Pi, and OpenCode through an OpenAI-compatible API. The examples below assume an endpoint at http://localhost:8000/v1 with the model ID Raon-1-mini-preview. Adjust these settings to match your server, ensuring that tool calling and reasoning are properly supported.
With MLX, use KRAFTON/Raon-1-mini-preview-mlx as the model ID instead of Raon-1-mini-preview; mlx_lm server loads the model named in each request.
Hermes Agent
Register Raon-1 mini preview as a custom OpenAI-compatible model in ~/.hermes/config.yaml:
model:
  provider: custom
  default: Raon-1-mini-preview
  base_url: http://localhost:8000/v1
  api_key: dummy
Hermes automatically detects the context window from the server when supported. If detection fails, add context_length: 262144 under model:. Replace dummy with your API key if the endpoint requires authentication.
Pi
Register Raon-1 mini preview as a custom provider in ~/.pi/agent/models.json:
{
  "providers": {
    "raon": {
      "baseUrl": "http://localhost:8000/v1",
      "api": "openai-completions",
      "apiKey": "dummy",
      "models": [
        {
          "id": "Raon-1-mini-preview",
          "name": "Raon-1 mini preview",
          "reasoning": true,
          "contextWindow": 262144,
          "maxTokens": 32768
        }
      ]
    }
  }
}
Select the model using /model inside a session, or launch Pi with --model raon/Raon-1-mini-preview. Replace dummy with your API key if the endpoint requires authentication.
OpenCode
Register Raon-1 mini preview as a custom OpenAI-compatible provider in ~/.config/opencode/opencode.json (or opencode.json in your project root):
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "raon": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Raon",
      "options": {
        "baseURL": "http://localhost:8000/v1"
      },
      "models": {
        "Raon-1-mini-preview": {
          "name": "Raon-1 mini preview",
          "limit": {
            "context": 262144,
            "output": 32768
          }
        }
      }
    }
  },
  "model": "raon/Raon-1-mini-preview"
}
The model field sets Raon-1 mini preview as the default model. You can also select it interactively using /models. If the endpoint requires authentication, configure an API key under options or use OpenCode's authentication settings.
For all three agent harnesses, the configured context window and maximum output tokens should not exceed the limits supported by the serving backend.
Access
Raon-1 mini preview is an open-weight model. Access is granted on request.
You can also try it in the Raon-1 mini playground, free for a limited time.
License
Hugging Face model card / README notice License - Apache 2.0
The Raon model, including its model weights, configuration files, and other model components made available for download through this repository, is licensed under the Apache License, Version 2.0. Subject to that license, you may download, use, modify, and redistribute the model and its weights, including for commercial purposes.
Krafton and its licensors retain ownership of their respective intellectual property. The Apache License grants the rights stated in that license and does not transfer ownership. Rights in third-party materials remain subject to their applicable terms.
The Apache License does not extend to Krafton’s proprietary training datasets, training methodologies, undistributed software, hosted API, playground, or other proprietary materials not included in this repository.
Hosted API and Playground Have Separate License Terms
Krafton also makes Raon available through its hosted API and playground service (“RAON Service”). The Raon Service is not licensed under Apache 2.0. Access to and use of the Raon Service is governed by separate Hosted Access Terms and Conditions that are provided before access to the service is granted. The Hosted Access Terms and Conditions govern, among other things, permitted service use, suspension, termination, and Krafton’s right to charge fees in the future.
Beta Access
To request free, limited private-beta access to the hosted API or playground, email raon.krafton.ai@krafton.com Krafton will send a link to the applicable Hosted Access Terms and Conditions by email. You must accept those terms before Krafton issues a key for the hosted API or enables playground access. Krafton may modify, suspend, or discontinue the Raon Service and may offer future access on paid or different terms. No charges will apply unless you first agree to them.
- Downloads last month
- 25
