---
id: "eac3db6276eafad4"
title: "unsloth/DeepSeek-V4.1-Flash-1017-GGUF · Hugging Face"
url: "https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF"
link: "https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-18T14:51:58Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["MundanePercentage674"]
language: "en"
summary: "no document or announcement from unslot team yet"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "OpenAI", "Hugging Face", "Anthropic", "Google"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 852
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x95491/unslothdeepseekv41flash1017gguf_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# unsloth/DeepSeek-V4.1-Flash-1017-GGUF · Hugging Face

Hugging Face · MundanePercentage674 · 2026-10-18

Instructions to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  llama.cpp  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL # Run inference directly in the terminal: llama cli -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL # Run inference directly in the terminal: llama cli -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Use pre-built binary # Download pre-built binary from: # https://github.com/ggerganov/llama.cpp/releases # Start a local OpenAI-compatible server with a web UI: ./llama-server -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL # Run inference directly in the terminal: ./llama-cli -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Build from source code git clone https://github.com/ggerganov/llama.cpp.git cd llama.cpp cmake -B build cmake --build build -j --target llama-server llama-cli # Start a local OpenAI-compatible server with a web UI: ./build/bin/llama-server -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL # Run inference directly in the terminal: ./build/bin/llama-cli -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Use Docker docker model run hf.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL
- LM Studio
- Jan
-  vLLM  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "unsloth/DeepSeek-V4.1-Flash-1017-GGUF"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "unsloth/DeepSeek-V4.1-Flash-1017-GGUF",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}' Use Docker docker model run hf.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL
-  Ollama  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with Ollama: ollama run hf.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL
- Unsloth Desktop
-  Pi  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with Pi: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Configure the model in Pi# Install Pi:
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
          "id": "unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL"
        }
      ]
    }
  }
} Run Pi # Start Pi in your project directory: pi
-  Docker Model Runner  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with Docker Model Runner: docker model run hf.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL
-  Lemonade  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with Lemonade: Pull the model # Download Lemonade from https://lemonade-server.ai/ lemonade pull unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Run and chat with the model lemonade run user.DeepSeek-V4.1-Flash-1017-GGUF-UD-Q4_K_XL List all available models lemonade list
-  Hermes Agent  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with Hermes Agent: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Configure Hermes # Install Hermes: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup # Point Hermes at the local server: hermes config set model.provider custom hermes config set model.base_url http://127.0.0.1:8080/v1 hermes config set model.default unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Run Hermes hermes
- Atomic Chat
-  OpenClaw  How to use unsloth/DeepSeek-V4.1-Flash-1017-GGUF with OpenClaw: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL Configure OpenClaw # Install OpenClaw: npm install -g openclaw@latest # Register the local server and set it as the default model: openclaw onboard --non-interactive --mode local \ --auth-choice custom-api-key \ --custom-base-url http://127.0.0.1:8080/v1 \ --custom-model-id "unsloth/DeepSeek-V4.1-Flash-1017-GGUF:UD-Q4_K_XL" \ --custom-provider-id llama-cpp \ --custom-compatibility openai \ --custom-text-input \ --accept-risk \ --skip-health Run OpenClaw openclaw agent --local --agent main --message "Hello from Hugging Face"
WIP - quants and implementation will be posted soon
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
- 1,447
4-bit
8-bit
Model tree for unsloth/DeepSeek-V4.1-Flash-1017-GGUF
Base model
deepseek-ai/DeepSeek-V4.1-Flash-1017
