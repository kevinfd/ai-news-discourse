---
id: "6d2d05a329e442ed"
title: "DeepSeek V4 Pro 0813"
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
link: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "hackernews"
date: "2026-11-14T00:50:33Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["nthypes"]
language: "en"
summary: "Instructions to use deepseek-ai/DeepSeek-V4-Pro-0813 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.\n- Libraries\n-  Transformers How to use deepseek-ai/DeepSeek-V4-Pro-0813 with Transformers: # Use a pipeline as a high-level helper\nfrom transformers import pipeline\npipe = pipeline(\"text-generation\", model=\"deepseek-ai/DeepSeek-V4-Pro-0813\") #…"
tags: []
orgs: ["DeepSeek", "OpenAI", "Google"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 851
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50492302"
score: 24
comments: 1
community: "Hacker News"
---

# DeepSeek V4 Pro 0813

Hugging Face · nthypes · 2026-11-14

Instructions to use deepseek-ai/DeepSeek-V4-Pro-0813 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use deepseek-ai/DeepSeek-V4-Pro-0813 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V4-Pro-0813") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V4-Pro-0813")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-V4-Pro-0813", device_map="auto")
- Inference
- HuggingChat
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use deepseek-ai/DeepSeek-V4-Pro-0813 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "deepseek-ai/DeepSeek-V4-Pro-0813"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro-0813",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker docker model run hf.co/deepseek-ai/DeepSeek-V4-Pro-0813
-  SGLang  How to use deepseek-ai/DeepSeek-V4-Pro-0813 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "deepseek-ai/DeepSeek-V4-Pro-0813" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro-0813",
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
        --model-path "deepseek-ai/DeepSeek-V4-Pro-0813" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro-0813",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
-  Docker Model Runner  How to use deepseek-ai/DeepSeek-V4-Pro-0813 with Docker Model Runner: docker model run hf.co/deepseek-ai/DeepSeek-V4-Pro-0813
DeepSeek-V4-Pro-0813
Introduction
DeepSeek-V4-Pro-0813 is the official release of DeepSeek-V4-Pro, superseding the preview version, with greatly enhanced agentic capabilities and performance improvements that are especially pronounced in production environments. It is built on the DeepSeek-V4-Pro (Preview) model structure, with a DSpark speculative decoding module attached.
DeepSeek-V4-Pro-0813 outperforms DeepSeek-V4-Pro (Preview) on the benchmarks listed below, and is broadly competitive with the strongest proprietary models available.
Notes:
- For the code-agent tasks among the public benchmarks above, DeepSeek-V4-Pro-0813 is evaluated with the minimal mode of DeepSeek Harness as the agent framework, using the max reasoning effort level with temperature = 1.0, top_p = 0.95.
- † DSBench-FullStack is an internal full-stack development test set; DSBench-Hard is an internal test set of difficult coding-agent problems.
Chat Template
This release does not include a Jinja-format chat template. Instead, we provide a dedicated encoding folder with Python scripts and test cases demonstrating how to encode messages in OpenAI-compatible format into input strings for the model, and how to parse the model's text output. Please refer to the encoding folder for full documentation.
The reasoning_effort parameter now supports three levels — low, high, and max — which control how much deliberation the model spends before answering.
A brief example:
from encoding_dsv4 import encode_messages, parse_message_from_completion_text
messages = [
    {"role": "user", "content": "hello"},
    {"role": "assistant", "content": "Hello! I am DeepSeek.", "reasoning_content": "thinking..."},
    {"role": "user", "content": "1+1=?"}
]
# messages -> string
prompt = encode_messages(messages, thinking_mode="thinking", reasoning_effort="max")
# string -> tokens
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V4-Pro-0813")
tokens = tokenizer.encode(prompt)
How to Run with vLLM
DSpark speculative decoding is enabled with a single flag — add --speculative-config with method: dspark to your vLLM launch command:
--speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"greedy"}'
For example, the command below serves the model with vLLM on a single 4×GB300 node. See the vLLM recipe for detailed instructions and other hardware configurations.
vllm serve deepseek-ai/DeepSeek-V4-Pro-0813 \
  --trust-remote-code --kv-cache-dtype fp8 --block-size 256 \
  --data-parallel-size 4 --enable-expert-parallel \
  --moe-backend deep_gemm_mega_moe \
  --attention-config '{"use_fp4_indexer_cache": true}' \
  --speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"greedy"}'
How to Run with SGLang
Enable DSpark with --speculative-algorithm DSPARK and do not set a separate --speculative-draft-model-path as the target and draft weights therefore come from the same checkpoint.
See the SGLang cookbook for detailed instructions, benchmarks and other hardwares configurations.
sglang serve \
  --trust-remote-code \
  --model-path deepseek-ai/DeepSeek-V4-Pro-0813 \
  --tp 4 \
  --moe-runner-backend flashinfer_mxfp4 \
  --speculative-algorithm DSPARK \
  --mem-fraction-static 0.90 \
  --chunked-prefill-size 4096 \
  --swa-full-tokens-ratio 0.1 \
How to Run Locally
Please refer to the inference folder for detailed instructions on running DeepSeek-V4 locally, including model weight conversion and interactive chat demos.
For local deployment, we recommend setting the sampling parameters to temperature = 1.0, with top_p = 0.95 for agentic scenarios and top_p = 1.0 otherwise. For the high and max reasoning effort levels, we recommend a maximum output length of 384K tokens.
License
This repository and the model weights are licensed under the MIT License.
Citation
@misc{deepseekai2026deepseekv4,
      title={DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence},
      author={DeepSeek-AI},
      year={2026},
}
Contact
If you have any questions, please raise an issue or contact us at service@deepseek.com.
- Downloads last month
- 53,977
Model tree for deepseek-ai/DeepSeek-V4-Pro-0813
Spaces using deepseek-ai/DeepSeek-V4-Pro-0813 18
Collection including deepseek-ai/DeepSeek-V4-Pro-0813
Paper for deepseek-ai/DeepSeek-V4-Pro-0813
Evaluation results
- harborframework/terminal-bench-2.1 · Terminalbench 2 1 View evaluation results    leaderboard   87.9 *
- datacurve/deep-swe · Deep Swe View evaluation results    leaderboard   62.7 *
- hkust-nlp/Toolathlon · Toolathlon Verified View evaluation results      74.1
