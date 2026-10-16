---
id: "e9daccf40793d2a8"
title: "AtomicChat/Ling-3.1-flash-GGUF · Hugging Face"
url: "https://huggingface.co/AtomicChat/Ling-3.1-flash-GGUF"
link: "https://huggingface.co/AtomicChat/Ling-3.1-flash-GGUF"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-15T15:16:42Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["BerryBlush_Rogers691"]
language: "en"
summary: "Yesterday I said its hard to play 4 spark with ling-3.1-flash but today its coming!"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face", "Google"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1097
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6of05/atomicchatling31flashgguf_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# AtomicChat/Ling-3.1-flash-GGUF · Hugging Face

Hugging Face · BerryBlush_Rogers691 · 2026-10-15

Instructions to use AtomicChat/Ling-3.1-flash-GGUF with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  llama.cpp  How to use AtomicChat/Ling-3.1-flash-GGUF with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Use pre-built binary # Download pre-built binary from: # https://github.com/ggerganov/llama.cpp/releases # Start a local OpenAI-compatible server with a web UI: ./llama-server -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M # Run inference directly in the terminal: ./llama-cli -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Build from source code git clone https://github.com/ggerganov/llama.cpp.git cd llama.cpp cmake -B build cmake --build build -j --target llama-server llama-cli # Start a local OpenAI-compatible server with a web UI: ./build/bin/llama-server -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M # Run inference directly in the terminal: ./build/bin/llama-cli -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Use Docker docker model run hf.co/AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M
- LM Studio
- Jan
-  vLLM  How to use AtomicChat/Ling-3.1-flash-GGUF with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "AtomicChat/Ling-3.1-flash-GGUF"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "AtomicChat/Ling-3.1-flash-GGUF",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M
-  Ollama  How to use AtomicChat/Ling-3.1-flash-GGUF with Ollama: ollama run hf.co/AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M
- Unsloth Desktop
-  Pi  How to use AtomicChat/Ling-3.1-flash-GGUF with Pi: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Configure the model in Pi# Install Pi:
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
          "id": "AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M"
        }
      ]
    }
  }
} Run Pi # Start Pi in your project directory: pi
-  Docker Model Runner  How to use AtomicChat/Ling-3.1-flash-GGUF with Docker Model Runner: docker model run hf.co/AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M
-  Lemonade  How to use AtomicChat/Ling-3.1-flash-GGUF with Lemonade: Pull the model # Download Lemonade from https://lemonade-server.ai/ lemonade pull AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Run and chat with the model lemonade run user.Ling-3.1-flash-GGUF-Q4_K_M List all available models lemonade list
-  Hermes Agent  How to use AtomicChat/Ling-3.1-flash-GGUF with Hermes Agent: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Configure Hermes # Install Hermes: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup # Point Hermes at the local server: hermes config set model.provider custom hermes config set model.base_url http://127.0.0.1:8080/v1 hermes config set model.default AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Run Hermes hermes
- Atomic Chat
-  OpenClaw  How to use AtomicChat/Ling-3.1-flash-GGUF with OpenClaw: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M Configure OpenClaw # Install OpenClaw: npm install -g openclaw@latest # Register the local server and set it as the default model: openclaw onboard --non-interactive --mode local \ --auth-choice custom-api-key \ --custom-base-url http://127.0.0.1:8080/v1 \ --custom-model-id "AtomicChat/Ling-3.1-flash-GGUF:Q4_K_M" \ --custom-provider-id llama-cpp \ --custom-compatibility openai \ --custom-text-input \ --accept-risk \ --skip-health Run OpenClaw openclaw agent --local --agent main --message "Hello from Hugging Face"
How to Run Ling 3.1 flash Locally
GGUF builds of inclusionAI's Ling 3.1 flash with our own importance matrix. The calibration corpora behind our builds are public.
- Runs in llama.cpp build b11571 or newer.
Pick a file
KL divergence is how far the quantized model's predictions drift from the
BF16 model's. Lower is better, and zero means identical. top-1 is how often it
picks the same next token the BF16 model would have picked. Both are measured
on held-out text; how is at the bottom.
The two 1-bit files are experimental: they matched the BF16 model's token choice 86 to 88% of the time here, so check them on your own tasks first.
AD- marks an Atomic Dynamic layout: the routed experts (97% of the weights)
take the low-bit type, while attention, the shared expert, the router and the
dense layers stay at q8_0 or higher. The file name is the type of the experts'
gate and up projections; their down projections, and all experts of the last
five blocks, get a step more.
How much memory it needs
The file has to fit, plus a little for the context. Context is cheap on this model: 63 of its 72 layers use linear attention with a fixed-size state, and only 9 keep a compressed attention cache. That is about 0.5 GB per conversation plus about 10 KB per token.
On a Mac, raise the GPU memory limit first, for example
sudo sysctl iogpu.wired_limit_mb=240000 on a 256 GB machine.
Running it
llama-server -hf AtomicChat/Ling-3.1-flash-GGUF:AD-Q4_K_M -ngl 99 -c 32768 --jinja
Each file sits in a folder of its name, split into shards of up to 45 GB; point llama.cpp at the first shard and it loads the rest:
hf download AtomicChat/Ling-3.1-flash-GGUF --include "AD-Q4_K_M/*" --local-dir .
llama-server -m AD-Q4_K_M/Ling-3.1-flash-AD-Q4_K_M-00001-of-00009.gguf -ngl 99 -c 32768 --jinja
The chat template is inside every file. Thinking is on by default; put
detailed thinking off in the system prompt to turn it off.
How we measured
Reference: BF16 weights converted from inclusionAI's FP8 release and run unquantized (perplexity 2.3590 on the held-out set). Converting FP8 to BF16 rounds each weight once, far below what Q8_0 adds.
Held-out text: eval_neutral from our
calibration dataset,
never used for calibration, 144 chunks of 4096 tokens. Metric: per-token KL
divergence of each file's predictions against the reference, plus top-1
agreement. Hardware: 8x A100-SXM4-80GB, llama.cpp 097cf33d9 for every file.
The importance matrix is the one we computed on 5.5M tokens of the
ling3-moe corpus (thinking on and off, tool calls, 30 languages, code, long
documents up to 32k tokens), rendered through this model's own chat template.
Model details
Mixture of experts: 512 routed experts in each of 68 layers (the first 4 layers are dense), 8 routed plus 1 shared expert per token, about 24B parameters active of 564B. Hybrid attention: 63 Kimi Delta Attention (linear) layers and 9 multi-head latent attention layers. Hidden size 4096, vocabulary 157,184, context 262,144. The multi-token-prediction head of the release is not included.
Built from inclusionAI's FP8 release (revision b426279f), converted to BF16
and quantized with llama.cpp b11571 (097cf33d9); needs llama.cpp with
bailingmoe3 support.
License and credits
MIT, as the original. Base model Ling 3.1 flash by inclusionAI. Quantization and evaluation by AtomicChat.
- Downloads last month
- 1,144
