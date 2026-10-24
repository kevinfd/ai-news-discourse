---
id: "9f01b68498dc6795"
title: "agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF · Hugging Face"
url: "https://huggingface.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF"
link: "https://huggingface.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-23T16:16:38Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Dentuam"]
language: "en"
summary: "AgentionAI Gyro Coder Large is now live 🚢 This coding specific finetune of Qwen 3.8 Flash Next is the same size as Gyro-S, but with half the experts and more bits per expert. The model fits in 32GB VRAM. More details in the model card"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face", "Google", "Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 1377
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdihql/agentionaiqwen38flashnextgyrocodergguf_hugging/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF · Hugging Face

Hugging Face · Dentuam · 2026-10-23

Instructions to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  llama.cpp  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 # Run inference directly in the terminal: llama cli -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 # Run inference directly in the terminal: llama cli -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Use pre-built binary # Download pre-built binary from: # https://github.com/ggerganov/llama.cpp/releases # Start a local OpenAI-compatible server with a web UI: ./llama-server -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 # Run inference directly in the terminal: ./llama-cli -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Build from source code git clone https://github.com/ggerganov/llama.cpp.git cd llama.cpp cmake -B build cmake --build build -j --target llama-server llama-cli # Start a local OpenAI-compatible server with a web UI: ./build/bin/llama-server -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 # Run inference directly in the terminal: ./build/bin/llama-cli -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Use Docker docker model run hf.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0
- LM Studio
- Jan
-  vLLM  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0
-  Ollama  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with Ollama: ollama run hf.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0
- Unsloth Desktop
-  Pi  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with Pi: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Configure the model in Pi# Install Pi:
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
          "id": "agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0"
        }
      ]
    }
  }
} Run Pi # Start Pi in your project directory: pi
-  Docker Model Runner  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with Docker Model Runner: docker model run hf.co/agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0
-  Lemonade  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with Lemonade: Pull the model # Download Lemonade from https://lemonade-server.ai/ lemonade pull agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Run and chat with the model lemonade run user.Qwen3.8-Flash-Next-Gyro-Coder-GGUF-TQ2_0 List all available models lemonade list
-  Hermes Agent  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with Hermes Agent: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Configure Hermes # Install Hermes: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup # Point Hermes at the local server: hermes config set model.provider custom hermes config set model.base_url http://127.0.0.1:8080/v1 hermes config set model.default agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Run Hermes hermes
- Atomic Chat
-  OpenClaw  How to use agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF with OpenClaw: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0 Configure OpenClaw # Install OpenClaw: npm install -g openclaw@latest # Register the local server and set it as the default model: openclaw onboard --non-interactive --mode local \ --auth-choice custom-api-key \ --custom-base-url http://127.0.0.1:8080/v1 \ --custom-model-id "agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF:TQ2_0" \ --custom-provider-id llama-cpp \ --custom-compatibility openai \ --custom-text-input \ --accept-risk \ --skip-health Run OpenClaw openclaw agent --local --agent main --message "Hello from Hugging Face"
Qwen3.8-Flash-Next Gyro-Coder — GGUF
A 125B-parameter coding model on one 24 GB card.
Qwen3.8-Flash-Next is a 125B mixture-of-experts model, the kind that normally needs a workstation full of GPUs. Gyro-Coder brings it to a single RTX 3090, 4090 or 7900 XTX: 19.9 GiB of GPU memory.
New: Gyro-Coder-L for 32 GB cards. The same experts at about 3.2 bits per weight: 27.5 GiB of GPU memory, and closer to the full model than Gyro-Coder on every set we measure. On C++ it is closer than Gyro-M, which keeps all 512 experts.
Two things make that possible:
- Only the experts that code. Each layer keeps the 256 of its 512 experts that matter for programming, picked by an evolutionary search over a space of 10⁷³²⁸ possible combinations (see below). That leaves 65B parameters on the GPU.
- 2.125 bits per weight, without the usual damage. The experts are stored with our own trellis encoder, the same one that puts Gyro-M ahead of IQ3_XXS and UD-Q2_K_XL quants that need 20-25% more memory.
On held-out Python it picks the same next token as the full model 93% of the time. Give it clear instructions (implement this, fix that, refactor, explain) and it delivers. For open-ended work and general knowledge, Gyro-S or Gyro-M is the better pick.
Runs in our llama.cpp build (Docker, see Quick start). Strata support is coming.
Pick your file
The TQ2_0 / TQ3_0 in the names are only size classes for the Hub: stock llama.cpp cannot load this file.
A needle in a very large haystack
Each layer keeps 256 of its 512 experts. That is about 10¹⁵² possible choices for one layer, and about 10⁷³²⁸ for the whole model: written out, the number fills about four pages. If you had tested a billion candidate models every second since the Big Bang, you would have covered about 10⁻⁷³⁰¹ of them.
The layers don't act alone either: what one layer keeps changes what every later layer sees, and each candidate is a full model that has to be built and tested before you know whether it is any good.
We started by mapping which experts carry which domains. From there, an evolutionary search proposed and scored about 2,200 candidate expert sets across 14 runs. The best were built as full models and put through coding, loop and knowledge tests. This is the one that passed.
Quality
KL divergence and top-1 agreement against the full model (Q8_0, all 512 experts), -c 2048.
Half the experts are gone, so general text and knowledge lose the most (Gyro-M: held-out 0.291); code stays close to the full model.
Coding tests: 13 of 16 passed (8 auto-graded tasks: LRU cache, interval merging, bug fix from a trace, refactor, bash script, SQL, CSV parsing in JS, multi-file change; 2 seeds each, thinking on, 64k tokens). The same expert set at 8 bits passes 15 of 16. Gyro-Coder-L passes 15 of 16.
Speed
Strix Halo (Vulkan, MTP draft): 11–22 tok/s per stream with two streams running at once (measured while generating long answers).
Quick start
1. Download Gyro-Coder (70.6 GiB on disk; Gyro-Coder-L 78.2 GiB; put it on a fast NVMe drive):
pip install -U huggingface_hub
hf download agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF Qwen3.8-Flash-Next-Gyro-Coder-TQ2_0.gguf --local-dir ~/models
# 32 GB card: Qwen3.8-Flash-Next-Gyro-Coder-L-TQ3_0.gguf (and use that name below)
2. Run it with our llama.cpp build (Vulkan, in Docker):
# AMD (and Intel) GPUs
docker run --rm -it --device /dev/dri --group-add "$(getent group render | cut -d: -f3)" \
  -v ~/models:/models -p 8080:8080 agentionai/agention-llama:server \
  -m /models/Qwen3.8-Flash-Next-Gyro-Coder-TQ2_0.gguf -ngl 999 -fa on --jinja --ngram-on-disk \
  -c 65536 -ctk q8_0 -ctv q8_0 --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.05
NVIDIA: replace --device /dev/dri --group-add ... with --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all.
Web chat at http://127.0.0.1:8080, OpenAI-compatible API at http://127.0.0.1:8080/v1: point your coding agent or
editor plugin there.
Strata: support is coming. Strata 0.2.2 does not know this file yet (Gyro-S and Gyro-M already run there); we will update this card when it does.
Recommended settings
- Sampling: --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.05 (the settings all our tests used).
- Keep --ngram-on-disk, with the model on fast NVMe: the 50.7 GiB n-gram table stays on disk, which is why the file
(70.6 GiB) is much larger than its GPU footprint.
- Give it clear instructions; it does best on well-specified tasks.
Credits
Built and tested on AMD Ryzen AI Max (Strix Halo). Hardware supported by AMD
Tensor format: trellis-coded quantization with Hadamard rotation, in the family of QTIP (Tseng et al., 2024). Encoder, trellis types and kernels: AgentionAI. Base model: Qwen/Qwen3.8-Flash-Next. Runtimes: llama.cpp, Strata, strix-llama.cpp.
Support AgentionAI
These quants are released freely. If they save you VRAM or make Qwen more useful, you can buy me a coffee or some GPU time and sponsor continued quantization and benchmarking on Buy Me A Coffee. AgentionAI is a one-person team and can use your help.
- Downloads last month
- 9,332
2-bit
Model tree for agentionai/Qwen3.8-Flash-Next-Gyro-Coder-GGUF
Base model
Qwen/Qwen3.8-Flash-Next
