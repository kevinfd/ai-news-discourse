---
id: "f6812e32974f7a62"
title: "LiquidAI/LFM2.5-24B-A2B"
url: "https://huggingface.co/LiquidAI/LFM2.5-24B-A2B"
link: "https://huggingface.co/LiquidAI/LFM2.5-24B-A2B"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-13T17:14:08Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Skyline34rGt"]
language: "en"
summary: "Gguf's: https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF Free Demo: https://playground.liquid.ai \"LFM2.5-24B-A2B is a 24B-parameter reasoning model with only 2B active parameters, built for fast, private agents on-device . It is the largest and final model in the LFM2.5 family, which now spans two orders of magnitude: from LFM2.5-230M to LFM2.5-24B-A2B. Best-in-class agent : Competitive with…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Google", "Nvidia", "Apple", "China"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1642
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x52kco/liquidailfm2524ba2b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# LiquidAI/LFM2.5-24B-A2B

Hugging Face · Skyline34rGt · 2026-10-13

Instructions to use LiquidAI/LFM2.5-24B-A2B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use LiquidAI/LFM2.5-24B-A2B with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="LiquidAI/LFM2.5-24B-A2B")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("LiquidAI/LFM2.5-24B-A2B")
model = AutoModelForCausalLM.from_pretrained("LiquidAI/LFM2.5-24B-A2B", device_map="auto")
messages = [
    {"role": "user", "content": "Who are you?"},
]
inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use LiquidAI/LFM2.5-24B-A2B with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "LiquidAI/LFM2.5-24B-A2B"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "LiquidAI/LFM2.5-24B-A2B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/LiquidAI/LFM2.5-24B-A2B
-  SGLang  How to use LiquidAI/LFM2.5-24B-A2B with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "LiquidAI/LFM2.5-24B-A2B" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "LiquidAI/LFM2.5-24B-A2B",
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
        --model-path "LiquidAI/LFM2.5-24B-A2B" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "LiquidAI/LFM2.5-24B-A2B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use LiquidAI/LFM2.5-24B-A2B with Docker Model Runner: docker model run hf.co/LiquidAI/LFM2.5-24B-A2B
LFM2.5-24B-A2B
LFM2.5-24B-A2B is a 24B-parameter reasoning model with only 2B active parameters, built for fast, private agents on-device. It is the largest and final model in the LFM2.5 family, which now spans two orders of magnitude: from LFM2.5-230M to LFM2.5-24B-A2B.
- Best-in-class agent: Competitive with Qwen3.6-35B-A3B, a model with ~50% more total and active parameters, on agentic and tool-use tasks, scoring 48.09 on LiveClaw versus 38.19.
- Reasoning at MoE speed: Always thinks before it answers. With only 2B active parameters per token, each reasoning token is cheap.
- Efficient inference: Runs up to 1.7× faster than comparable MoEs on-device, with 184 tok/s on an Apple M5 Max and up to 21K output tok/s on a single NVIDIA B300 GPU.
Find more information about LFM2.5-24B-A2B in our blog post.
🗒️ Model Details
LFM2.5-24B-A2B is a general-purpose text-only reasoning model with the following features:
- Total parameters: 24.0B
- Active parameters: 2.45B
- Number of layers: 40 (30 double-gated short convolution blocks + 10 GQA)
- Experts: 64 per MoE block, top-4 routing
- Training budget: 36 trillion tokens
- Vocabulary size: 128,000
- Context length: 131,072 tokens
- Languages: English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish
- Generation parameters:
  - temperature: 0.1
  - top_k: 50
  - repetition_penalty: 1.05
We recommend using it for agents that need to reason, call tools, and run reliably on your device. It is not recommended for knowledge-heavy tasks on its own: pair it with retrieval or web search, which plays to its tool-calling strength.
Chat Template
LFM2.5 uses a ChatML-like format. See the Chat Template documentation for details. Example:
<|startoftext|><|im_start|>system
You are a helpful assistant trained by Liquid AI.<|im_end|>
<|im_start|>user
What is C. elegans?<|im_end|>
<|im_start|>assistant
<think>
You can use tokenizer.apply_chat_template() to format your messages automatically.
💡 Note: Unlike LFM2-24B-A2B, LFM2.5-24B-A2B is a pure reasoning model that always thinks before it answers. It adds a <think> tag directly in the chat template when starting an assistant answer.
Tool Use
LFM2.5 supports function calling in four steps:
- Function definition: Provide the list of tools as a JSON object in the system prompt, or use tokenizer.apply_chat_template() with tools=....
- Function call: By default, LFM2.5 writes Pythonic function calls (a Python list between <|tool_call_start|> and <|tool_call_end|> special tokens), as the assistant answer. You can override this behavior by asking the model to output JSON function calls in the system prompt.
- Function execution: Execute the call and return the result with the tool role.
- Final answer: LFM2.5 interprets the tool output and returns a plain-text answer addressing the original prompt.
See the Tool Use documentation for the full guide. Example:
<|startoftext|><|im_start|>system
List of tools: [{"name": "get_candidate_status", "description": "Retrieves the current status of a candidate in the recruitment process", "parameters": {"type": "object", "properties": {"candidate_id": {"type": "string", "description": "Unique identifier for the candidate"}}, "required": ["candidate_id"]}}]<|im_end|>
<|im_start|>user
What is the current status of candidate ID 12345?<|im_end|>
<|im_start|>assistant
<|tool_call_start|>[get_candidate_status(candidate_id="12345")]<|tool_call_end|>Checking the current status of candidate ID 12345.<|im_end|>
<|im_start|>tool
[{"candidate_id": "12345", "status": "Interview Scheduled", "position": "Clinical Research Associate", "date": "2023-11-20"}]<|im_end|>
<|im_start|>assistant
The candidate with ID 12345 is currently in the "Interview Scheduled" stage for the position of Clinical Research Associate, with an interview date set for 2023-11-20.<|im_end|>
Training
LFM2.5-24B-A2B keeps the LFM2-24B-A2B architecture with two changes: the context window grows from 32K to 131K tokens, and the vocabulary doubles from 65K to 128K tokens through an in-place tokenizer expansion for better non-Latin tokenization.
- Pre-training: ~33T tokens, up from ~17T.
- Mid-training: 2T tokens at 32K context on curated, higher-quality data weighted toward reasoning, math, code, instruction following, and multilingual text, then 300B tokens of long-context data at 131K context. Tool calls and multi-turn trajectories appear in both phases.
- Post-training: supervised fine-tuning, teacher specialization, two multi-domain on-policy distillation stages (one non-agentic, one agentic), and agentic reinforcement learning inside popular agent harnesses (OpenClaw, Hermes Agent, Pi, OpenCode), so the model learns their tools, system prompts, and interaction patterns.
🏃 Inference
LFM2.5 is supported by many inference frameworks. See the Inference documentation for the full list.
Quick start
Get started with Transformers (compatible with transformers>=5.0.0):
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
model_id = "LiquidAI/LFM2.5-24B-A2B"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16",
#   attn_implementation="flash_attention_2" <- uncomment on compatible GPU
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
prompt = "What is C. elegans?"
input_ids = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
)["input_ids"].to(model.device)
output = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.1,
    top_k=50,
    repetition_penalty=1.05,
    max_new_tokens=4096,
    streamer=streamer,
)
Agentic Harnesses
LFM2.5-24B-A2B supports tool calling for agentic workflows. Serve it locally with any OpenAI-compatible backend from the table above, then configure your agent harness to connect to it. For full setup instructions including installation and additional options, see our Agent Harnesses guide.
Hermes
Either use the interactive wizard or set it directly:
hermes config set model.provider custom
hermes config set model.base_url http://localhost:8080/v1
hermes config set model.default LFM2.5-24B-A2B
hermes config set model.context_length 131072
hermes config set model.api_mode chat_completions
hermes config set agent.tool_use_enforcement true
OpenClaw
Add to your config in models.providers:
local: {
  baseUrl: "http://localhost:8080/v1",
  apiKey: "sk-local",
  api: "openai-completions",
  models: [{
    id: "LFM2.5-24B-A2B",
    name: "LFM2.5-24B-A2B",
    contextWindow: 131072,
    maxTokens: 8192,
    cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }
  }]
}
Pi
Add to your config to ~/.pi/agent/models.json:
{
  "providers": {
    "local": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "local",
      "models": [{ "id": "LFM2.5-24B-A2B" }]
    }
  }
}
🔧 Fine-Tuning
We recommend fine-tuning LFM2.5 for your specific use case to achieve the best results.
📊 Performance
Benchmarks
We compared LFM2.5-24B-A2B with relevant MoE models on 16 benchmarks covering knowledge, instruction following, math, code, tool use, and agentic workflows.
Evaluation settings
All the models were evaluated with vLLM and the following generation parameters:
- AutomationBench: temperature = 0.6, top_p = 0.95, max_turns = 50, no max output tokens (bounded by the model's context window).
- BFCLv4: temperature = 0.001, max output tokens = 4096.
- ToolSandbox: temperature = 0, max output tokens = 1024; user simulator: GPT-4o-2024-08-06, temperature = 0, max output tokens = 1024.
- LiveClaw: temperature = 1.0 (vLLM default; the agent sets no temperature), max output tokens = 8192.
- τ³-Bench Banking: official user model (GPT-5.2, low reasoning effort) with default BM25 retrieval, temperature = 0, max output tokens = 16384 per turn.
- WebArena Verified: temperature = 0.6, top_p = 0.95, max_turns = 40 (number of browser actions allowed), no max output tokens (bounded by the model's context window).
- Other evals: temperature = 0.6, max output tokens = 32768.
Edge Inference
LFM2.5-24B-A2B is the fastest of the compared MoEs at reading in prompts and generating answers. It decodes 184 tokens/s on an Apple M5 Max and 114 tokens/s on an AMD Ryzen AI Max+ 395, up to 1.7x faster than the next-best model, while using the least memory.
Evaluation settings
Collected on Pipette, Liquid AI's device benchmarking infrastructure, with llama.cpp, Q4_K_M quantization, and a 4K-token input context.
GPU Inference
LFM2.5-24B-A2B is the fastest model in its size class, reaching over 21K output tokens per second at high concurrency.
Evaluation settings
We measure GPU throughput (total output tokens / wall time) on a single NVIDIA B300 GPU with SGLang 0.5.22, using 1,024 input tokens, up to 256 output tokens, and BF16 weights. At each concurrency level, we continuously maintain the target number of in-flight requests, replacing each completed request immediately.
📬 Contact
- Got questions or want to connect? Join our Discord community
- If you are interested in custom solutions with edge deployment, please contact our sales team.
Citation
@article{liquidAI202624BA2B,
  author  = {Liquid AI},
  title   = {LFM2.5-24B-A2B: Built for Fast On-Device Agents},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-24b-a2b},
}
@article{liquidai2025lfm2,
  title   = {LFM2 Technical Report},
  author  = {Liquid AI},
  journal = {arXiv preprint arXiv:2511.23404},
  year    = {2025}
}
- Downloads last month
- 4,067
Model tree for LiquidAI/LFM2.5-24B-A2B
Base model
LiquidAI/LFM2.5-24B-A2B-Base
