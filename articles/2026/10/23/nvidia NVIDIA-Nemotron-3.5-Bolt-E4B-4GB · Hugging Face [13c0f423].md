---
id: "13c0f423c09dd3f2"
title: "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB · Hugging Face"
url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB"
link: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-23T16:13:05Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["jacek2023"]
language: "en"
summary: "NVIDIA-Nemotron-3.5-Bolt-E4B-4GB is a small language model (SLM) further post-trained from Gemma-4-E4B-it by NVIDIA. Nemotron-3.5-Bolt-E4B carries forward Gemma’s strong conversational capabilities and further improves multi-turn tool use, instruction following, and input grounding for fast local voice/device assistants, interactive personas, and embedded/edge interfaces. Designed for…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "OpenAI", "Google", "Hugging Face"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 3730
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdiecx/nvidianvidianemotron35bolte4b4gb_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB · Hugging Face

Hugging Face · jacek2023 · 2026-10-23

Instructions to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  llama.cpp  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M # Run inference directly in the terminal: llama cli -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M # Run inference directly in the terminal: llama cli -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Use pre-built binary # Download pre-built binary from: # https://github.com/ggerganov/llama.cpp/releases # Start a local OpenAI-compatible server with a web UI: ./llama-server -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M # Run inference directly in the terminal: ./llama-cli -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Build from source code git clone https://github.com/ggerganov/llama.cpp.git cd llama.cpp cmake -B build cmake --build build -j --target llama-server llama-cli # Start a local OpenAI-compatible server with a web UI: ./build/bin/llama-server -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M # Run inference directly in the terminal: ./build/bin/llama-cli -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Use Docker docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M
- LM Studio
- Jan
-  vLLM  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M
-  SGLang  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB",
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
        --model-path "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Ollama  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Ollama: ollama run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M
- Unsloth Desktop
-  Pi  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Pi: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Configure the model in Pi# Install Pi:
npm install -g @earendil-works/pi-coding-agent
# Add to ~/.pi/agent/models.json:
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "none",
      "models": [
        {
          "id": "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M"
        }
      ]
    }
  }
} Run Pi # Start Pi in your project directory: pi
-  Docker Model Runner  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Docker Model Runner: docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M
-  Lemonade  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Lemonade: Pull the model # Download Lemonade from https://lemonade-server.ai/ lemonade pull nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Run and chat with the model lemonade run user.NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Q4_K_M List all available models lemonade list
-  Hermes Agent  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with Hermes Agent: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Configure Hermes # Install Hermes: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup # Point Hermes at the local server: hermes config set model.provider custom hermes config set model.base_url http://127.0.0.1:8080/v1 hermes config set model.default nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Run Hermes hermes
- Atomic Chat
-  OpenClaw  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB with OpenClaw: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M Configure OpenClaw # Install OpenClaw: npm install -g openclaw@latest # Register the local server and set it as the default model: openclaw onboard --non-interactive --mode local \ --auth-choice custom-api-key \ --custom-base-url http://127.0.0.1:8080/v1 \ --custom-model-id "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M" \ --custom-provider-id llama-cpp \ --custom-compatibility openai \ --custom-text-input \ --accept-risk \ --skip-health Run OpenClaw openclaw agent --local --agent main --message "Hello from Hugging Face"
NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
Description
NVIDIA-Nemotron-3.5-Bolt-E4B-4GB is a small language model (SLM) further post-trained from Gemma-4-E4B-it by NVIDIA. Nemotron-3.5-Bolt-E4B carries forward Gemma’s strong conversational capabilities and further improves multi-turn tool use, instruction following, and input grounding for fast local voice/device assistants, interactive personas, and embedded/edge interfaces. Designed for low-memory, low-TTFT operation, the model allows agents to respond quickly while preserving headroom for applications or adjacent model pipelines.
For speculative decoding, use the companion DFlash drafter. For the full-precision (BF16) version, see NVIDIA-Nemotron-3.5-Bolt-E4B-BF16.
This model is ready for commercial or non‑commercial use.
Model Summary
Model Overview
Model Developer: NVIDIA Corporation
Model Dates: December 2025 - May 2026
Data Freshness:
- The post-training data has a cutoff date of May 2026.
What is Nemotron?
NVIDIA Nemotron™ is a family of open models with open weights, training data, and recipes, delivering leading efficiency and accuracy for building specialized AI agents.
Quick Start
export MODEL_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
export MODEL_FILE=Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf
export DRAFTER_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-DFlash
export DRAFTER_FILE=Nemotron-3.5-Bolt-E4B-DFlash-BF16.gguf
export MODEL_DIR="$PWD/bolt-models"
hf download "$MODEL_REPO" "$MODEL_FILE" \
  --local-dir "$MODEL_DIR"
hf download "$DRAFTER_REPO" "$DRAFTER_FILE" \
  --local-dir "$MODEL_DIR"
Without drafter
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
With DFlash drafter
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --spec-draft-model "/models/$DRAFTER_FILE" \
  --spec-type draft-dflash \
  --spec-draft-n-max 7 \
  --spec-draft-ngl 999 \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
curl --fail-with-body -sS \
  http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "nemotron-bolt",
    "messages": [
      {"role": "user", "content": "What is 17 multiplied by 23?"}
    ],
    "temperature": 0.0,
    "max_tokens": 512,
    "chat_template_kwargs": {
      "enable_thinking": true
    }
  }'
For more details on how to deploy and use the model — see the Quick Start Guide below!
License/Terms of Use
Governing Terms: Use of this model is governed by the OpenMDW License Agreement, version 1.1. This model has been post-trained on the Google Gemma 4 model, and use of the Google Gemma 4 model is governed by Apache License, Version 2.0
Benchmarks
Reasoning Benchmark Evaluations
Benchmarks
We evaluated our model on the following benchmarks:
Note:
- Evaluations are conducted in reasoning mode except for RoleBench, EQ-Bench v3, and RULER.
- Bold indicates the highest score within each precision group (BF16 and Q4_K_M) for each row. All tied highest scores are bold.
- Accuracy numbers are measured by NVIDIA under a consistent harness (NeMo Gym); they may differ from vendors' self-reported numbers.
Deployment Geography: Global
Use Case
NVIDIA-Nemotron-3.5-Bolt-E4B-4GB is designed for fast local voice and device assistants, interactive personas, and embedded interfaces, with an emphasis on multi-turn tool use, instruction following, and input grounding.
Release Date
- Hugging Face 10/23/2026 via https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
- Build.NVIDIA.com 10/23/2026 via https://build.nvidia.com/nvidia/nemotron-3.5-bolt-e4b
Reference(s)
- NVIDIA Nemotron 3 model family on Hugging Face
- NVIDIA Nemotron 3.5 Bolt E4B 4GB Technical Report
- NVIDIA Nemotron 3.5 Bolt E4B 4GB Technical Blog
Model Architecture
- Architecture Type: Gemma 4
- Network Architecture: Gemma-4-E4B
- Number of model parameters: 8B (4B effective parameters)
Model Design
The model was further post-trained from Gemma-4-E4B-it.
Training Methodology
Reinforcement Learning
- The model underwent multi-environment reinforcement learning using GRPO (Group Relative Policy Optimization) across instruction following, multi-step tool use, multi-turn conversations, and structured output environments. It utilized an asynchronous RL architecture that decouples training from inference.
- Software used for reinforcement learning: NeMo RL, NeMo Gym
NVIDIA-Nemotron-3.5-Bolt-E4B-4GB is a result of the above work.
Input
- Input Type(s): Text
- Input Format(s): String
- Input Parameters: One-Dimensional (1D): Sequences
- Other Properties Related to Input: Maximum context length up to 64K tokens. Supported languages include English, Spanish, French, German, Italian, and Japanese, among others.
Output
- Output Type(s): Text
- Output Format: String
- Output Parameters: One-Dimensional (1D): Sequences
- Other Properties Related to Output: Maximum context length up to 64K tokens
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.
Software Integration
- Runtime Engine(s): PyTorch
- Supported Hardware Microarchitecture Compatibility: NVIDIA Ampere - A100; NVIDIA Blackwell; NVIDIA Hopper - H100-80GB
- Supported Operating System(s): Linux
The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.
Model Version(s)
- GA (10/23/2026)
Quick Start Guide
export MODEL_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
export MODEL_FILE=Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf
export DRAFTER_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-DFlash
export DRAFTER_FILE=Nemotron-3.5-Bolt-E4B-DFlash-BF16.gguf
export MODEL_DIR="$PWD/bolt-models"
hf download "$MODEL_REPO" "$MODEL_FILE" \
  --local-dir "$MODEL_DIR"
hf download "$DRAFTER_REPO" "$DRAFTER_FILE" \
  --local-dir "$MODEL_DIR"
Without drafter
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
With DFlash drafter
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --spec-draft-model "/models/$DRAFTER_FILE" \
  --spec-type draft-dflash \
  --spec-draft-n-max 7 \
  --spec-draft-ngl 999 \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
curl --fail-with-body -sS \
  http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "nemotron-bolt",
    "messages": [
      {"role": "user", "content": "What is 17 multiplied by 23?"}
    ],
    "temperature": 0.0,
    "max_tokens": 512,
    "chat_template_kwargs": {
      "enable_thinking": true
    }
  }'
API Client
The examples below use the OpenAI-compatible client and work with the serving backend above. Recommended sampling settings are Temperature 1.0 and Top_P 0.95 in both thinking enabled and disabled modes.
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
MODEL = "nemotron-bolt"
Bolt-E4B exposes reasoning control through chat-template kwargs: thinking enabled (the default), thinking disabled for direct answers, and a runtime thinking budget.
Reasoning On
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Write a haiku about GPUs"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": True},
    }
)
print(response.choices[0].message.content)
Reasoning Off
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }
)
print(response.choices[0].message.content)
Streaming
stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain speculative decoding in two sentences"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    stream=True,
    extra_body={"skip_special_tokens": False},
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
Tool Calling
For vLLM, add the following to any serve command above:
--enable-auto-tool-choice \
--tool-call-parser gemma4 \
--reasoning-parser gemma4 \
Sample request with tool-calling enabled:
tools = [{
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
}]
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What's the weather in Santa Clara?"}],
    tools=tools,
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": True},
    },
)
print(response.choices[0].message.tool_calls)
Conversational Mode
Bolt-E4B supports a conversational mode. If enabled, Bolt-E4B responds concisely and without as much textual formatting. This mode is suitable for conversational and spoken interaction-based applications. Conversational mode can be toggled as follows:
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"conversational_mode": True},
    }
)
print(response.choices[0].message.content)
Conversational mode can be combined with thinking enabled and disabled mode, as well as tool-calling.
Runtime Thinking Budget Control
With llama-server you can control thinking budget by specifying the --reasoning-budget argument:
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja \
  --reasoning on \
  --reasoning-budget <reasoning budget in tokens>
Limits and Recommendations for Runtime Budget Control
- Restricted token allocations may truncate thought processes mid-sentence. While output clarity is typically maintained, task-specific output evaluation remains necessary.
- The client halts execution immediately upon reaching the pre-configured initial generation ceiling, ignoring subsequent line boundaries.
- Conduct systematic allocation sweeps using standard evaluation prompts prior to establishing deployment parameters.
- Illustration: To maintain a strict 500-token overall threshold, evaluate unconstrained model generation metrics (e.g., averaging 200 tokens). Assigning a dedicated 300-token reasoning parameter alongside a 500-token global ceiling forces thought termination at 300 tokens, reserving 200 tokens for output synthesis.
- To encourage brief output (excluding internal reasoning steps), incorporate explicit word- or sentence-count constraints within system prompts.
Asynchronous Tool Calling
Bolt-E4B's chat template currently does not allow stray tool responses (messages with tool role that do not immediately follow a message with assistant role and tool_calls). However, this model can support asynchronous tool-calling with in the following manner:
Asynchronous tool-calling usage
If the model invokes a tool in message.tool_calls that has a later arriving result, respond with a tool message in the immediate next turn that acknowledges the tool-call and shows the tool result as pending.
Example:
Assistant tool-call
{
  "role": "assistant",
  "tool_calls": [{
    "id": "call_1",
    "type": "function",
    "function": {
      "name": "build_report",
      "arguments": "{\"_task_id\":\"task_1\",\"scope\":\"weekly\"}"
    }
  }]
}
Immediate acknowledgement with pending result
{
  "role": "tool",
  "tool_call_id": "call_1",
  "content": "{\"status\":\"pending\",\"task_id\":\"task_1\",\"function\":\"build_report\"}"
}
The model can continue the conversation with the user after this acknowledgement tool result message.
Once the tool result is available, respond with a user message that provides the tool result in a structured format, prefixed with something like "TOOL RESULT:"
Example:
Later tool result completion result
{
  "role": "user",
  "content": "TOOL UPDATE: {\"status\":\"completed\",\"task_id\":\"task_1\",\"function\":\"build_report\",\"response\":\"Report is ready.\"}"
}
The model processes the finalized payload to resume the conversation.
Prompting Guidelines
General guidelines for using Bolt-E4B in conversational and interactive agent applications.
Prompt Structure and Content
- Put persistent role definitions, behavioral constraints, and operating rules in the system prompt.
- Use consistent headings which clearly identify the purpose of a section of the prompt, Example: ROLE, IDENTITY, INPUT FORMAT, TASK RULES, PERSONALITY, SPEECH EXAMPLES, etc.
- State the primary objective clearly. Define what counts as completion for multi-step workflows.
- Write instructions as conditions and actions: “After crafting succeeds, call the delivery tool.”
- Remove redundant instructions rather than repeatedly adding stronger versions.
- Use response-length limits that fit the application. A one- or two-sentence limit can suit spoken replies; it will not restrict tool arguments or reasoning.
- Use explicit constraints (e.g., "limit responses to 1-2 sentences") instead of vague requests (e.g., "be brief").
- Preserve genuine conversation history. Do not insert fabricated assistant actions, promises, or tool calls as if they occurred.
- If using few-shot examples, identify them as examples. Test whether the model copies their wording or themes and adjust instructions accordingly.
- Strictly adhere to standard system/user/assistant/tool turn sequences.
Identity, Ownership, and Perspective
- Define the agent and user as separate entities with separate actions, locations, possessions, and knowledge.
- Explain pronouns when both entities appear in state: “In the state update following a user turn, ‘my’ refers to the user; but in a state update after an assistant turn, ‘my’ refers to you.”
- Use explicit labels such as YOUR INVENTORY, PLAYER VIEW, and SHARED CHEST to reinforce ownership.
- Distinguish unavailable information from empty state. An inaccessible user inventory is unknown, not empty.
- Distinguish visible resources from possessed resources. A nearby item or chest does not mean the agent owns its contents.
- Make character lore consistent with available information and tools. Explain any restrictions on what the character can perceive or use.
Conveying Environment State
- Mark state blocks clearly, for example with # CURRENT STATE.
- Explain that state is operational context, not a new request or text to repeat aloud.
- Share state updates via new user or system messages. The model supports consecutive user and system messages. It is important to maintain correct chronology when conveying state information/updates and continuing the conversation.
For example, for a user message that is conditioned upon a state update,  the state update user or system message must come before the user response:
# CURRENT STATE
...
----------------
<actual user message>
OR in two user/system messages:
[..., {"role": "user/system", "content": "# CURRENT STATE..."}, {"role": "user", "content": "<actual user message>"}, ...]
But, for conveying an updated state that occurs after a tool is executed, the state update user or system message must come after the tool execution response:
[..., {"role": "tool", "content": "<tool execution result that updates a state>"}, {"role": "user/system", "content": "# CURRENT STATE... <state that got changed with tool execution>"}, {"role": "user", "content": "<next user message>"}, ...]
Tool Definitions and Calling
- Send tools through the native tools array and read actions from message.tool_calls.
- Use stable function names and parameter schemas. Describe prerequisites, argument meanings, units, defaults, effects, and failure conditions.
- Make tool descriptions match actual behavior. “Drops an item toward the player” must not be described as guaranteed placement in the player’s inventory.
Training, Testing, and Evaluation Datasets
Training
Dataset Overview
Data Modality: Text
Training Data Size: More than 20 Trillion Tokens
Dataset partition: Training [100%], testing [0%], validation [0%]
Time period for training data collection: 2013 to December 2025
Time period for testing data collection: 2013 to December 2025
Time period for validation data collection: 2013 to December 2025
Data Collection Method by dataset: Hybrid: Automated, Manually-Collected, Synthetic
Labeling Method by dataset: Hybrid: Automated, Manually-Labeled, Synthetic
The post-training corpus for NVIDIA-Nemotron-3.5-Bolt-E4B-4GB consists of high-quality curated and synthetically-generated data. Primary languages used for post-training include English, French, German, Italian, Japanese, Spanish, and Chinese.
These datasets, such as FinePDFs, EssentialWeb, HotpotQA, SQuAD, and HelpSteer3, do not collectively or exhaustively represent all demographic groups (and proportionally therein). For instance, these datasets do not contain explicit mentions of demographic classes such as age, gender, or ethnicity in 64-99% of samples, depending on the source. In the subset where such terms are present, document-based datasets (FinePDFs and EssentialWeb) contain representational skews, such as references to "male" outnumbering those to "female", and mentions of "White" as the most frequent among ethnic identifiers (comprising 43-44% of ethnicity mentions). To mitigate these imbalances, we recommend considering evaluation techniques such as bias audits, fine-tuning with demographically balanced datasets, and mitigation strategies like counterfactual data augmentation to align with the desired model behavior. This evaluation used a 3,000-sample subset per dataset, identified as the optimal threshold for maximizing embedder accuracy.
During post-training, we generate synthetic data by distilling trajectories, solutions, and translations from strong teacher models and agent systems, often grounded in real tasks or documents and aggressively filtered for quality. For math, code, and science, we start from curated problem sets and use open source permissive models such as GPT-OSS-120B to produce step-by-step reasoning traces, candidate solutions, best-of-n selection traces, and verified CUDA kernels. For long-context and science, we build synthetic QA and reasoning data by retrieving passages from long documents, generating MCQ/OpenQA questions and answers, and paraphrasing them into multiple prompt/response formats to ensure diversity. Across all pipelines we stack automated verification—compilers, numerical checks, language identification—to ensure our data is high quality.
For all domains, we apply a unified data filtering pipeline to ensure that only high-quality, license-compliant, and verifiable samples are used for post-training. We first discard malformed examples using structural checks (e.g., missing tool definitions when tool calls are present). We then aggressively filter reasoning traces exhibiting pathological repetition, such as repeated n-grams within a sliding window or across the entire trajectory, which we found to be a strong indicator of malformed or low-quality reasoning. Finally, based on internal audits of synthetically generated datasets, we observed that some teacher models occasionally produce reasoning traces and final responses that implicitly align with specific political entities or promote nationalistic narratives. To mitigate this, we apply targeted keyword- and regex-based filters and remove all trajectories matching such behavior.
Alongside the model, we release our final pre-training and post-training data, as outlined in this section. For ease of analysis, there is a sample set that is ungated. For all remaining code, math and multilingual data, gating and approval is required, and the dataset is permissively licensed for model training purposes.
Detailed dataset information
Public Datasets
Private Non-publicly Accessible Datasets of Third Parties
Private Non-publicly Accessible Datasets by NVIDIA
NVIDIA-Sourced Synthetic Datasets (Post-Training)
Language Distribution in Post-Training
For our post-training recipe, we focused on the following languages in addition to English: French, German, Italian, Japanese, Spanish, and Chinese. Those languages were represented in the form of multilingual reasoning and translation tasks.
Testing Datasets
Data Collection Method by dataset 
- Hybrid: Automated, Manually-Collected, Synthetic
Labeling Method by dataset 
- Hybrid: Automated, Manually-Labeled, Synthetic
Properties: This corpus comprises a mix of high-quality standard benchmarks and test suites for modern agentic AI. These benchmarks test model capabilities on tasks such as tool-calling and instruction following.
Evaluation Datasets
Data Collection Method by dataset 
- Hybrid: Automated, Manually-Collected, Synthetic
Labeling Method by dataset 
- Hybrid: Automated, Manually-Labeled, Synthetic
Properties: This corpus comprises a mix of high-quality standard benchmarks and test suites for modern agentic AI. These benchmarks test model capabilities on tasks such as tool-calling and instruction following.
Inference
- Acceleration Engine: PyTorch
- Test Hardware:
  - NVIDIA Hopper
    - 1-8x H100
    - 1-8x H200
  - NVIDIA Blackwell
    - GB200
    - GeForce RTX 5090
    - DGX Spark
    - RTX Spark
  - NVIDIA Jetson
    - Jetson Orin
    - Jetson Thor
Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
We advise against circumvention of any provided safety guardrails contained in the Model without a substantially similar guardrail appropriate for your use case. For more details: Safety and Explainability Subcards.
For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here.
- Downloads last month
- 5,906
4-bit
Model tree for nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
Base model
google/gemma-4-E4B
