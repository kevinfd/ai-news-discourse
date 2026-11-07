---
id: "ab76f99ae189a1aa"
title: "maritaca-ai/S5-nano 4B · the best open-weights model in Brazil"
url: "https://huggingface.co/maritaca-ai/S5-nano"
link: "https://huggingface.co/maritaca-ai/S5-nano"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-06T17:14:34Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["ApprehensiveAd3629"]
language: "en"
summary: "Repo: https://github.com/maritaca-ai/observatorio-maritaca benchmarks: https://maritaca-ai.github.io/observatorio-maritaca/#inicio?size=all&mode=all"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Google"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1517
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpibxn/maritacaais5nano_4b_the_best_openweights_model_in/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# maritaca-ai/S5-nano 4B · the best open-weights model in Brazil

Hugging Face · ApprehensiveAd3629 · 2026-11-06

Instructions to use maritaca-ai/S5-nano with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use maritaca-ai/S5-nano with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="maritaca-ai/S5-nano")
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
processor = AutoProcessor.from_pretrained("maritaca-ai/S5-nano")
model = AutoModelForMultimodalLM.from_pretrained("maritaca-ai/S5-nano", device_map="auto")
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
-  vLLM  How to use maritaca-ai/S5-nano with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "maritaca-ai/S5-nano"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "maritaca-ai/S5-nano",
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
	}' Use Docker docker model run hf.co/maritaca-ai/S5-nano
-  SGLang  How to use maritaca-ai/S5-nano with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "maritaca-ai/S5-nano" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "maritaca-ai/S5-nano",
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
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "maritaca-ai/S5-nano" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "maritaca-ai/S5-nano",
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
	}'
-  Docker Model Runner  How to use maritaca-ai/S5-nano with Docker Model Runner: docker model run hf.co/maritaca-ai/S5-nano
S5-nano
S5-nano is a 4B-parameter model from Maritaca AI. It has two modes:
- Think: reasons before answering (the default mode).
- Instruct: answers directly, without a reasoning step.
The context window supports up to 262,144 tokens, and the weights include an MTP (multi-token prediction) layer for speculative decoding.
Versions
FP8 is recommended for GPUs with native FP8 support (Ada, Hopper, and Blackwell). The GGUF repository provides BF16, Q8_0, and Q4_K_M variants.
Evaluation results
Explore the results in Observatório Maritaca
Results for the original S5-nano checkpoint, evaluated in BF16 on text tasks.
Averages
Each primary metric is weighted equally.
Compared models and sizes
Total, active, and effective parameter counts measure different things. LatamGPT 70B is a larger reference model; LFM2.5 has approximately 24B total parameters and 2B active parameters.
Results by benchmark
Bold indicates the best result within each group with a documented evaluation protocol, in the same mode. Different groups may produce more than one highlighted result in the same row. † indicates that the model produced reasoning in Instruct mode even though it was disabled in the request.
Think / Thinking
Instruct
Evaluation populations, metrics, and documented limitations
- BLUEX: 173 questions and 395 subquestions. One grading result for S5-nano Think and one for LFM3 Think did not produce valid JSON; GAIA Instruct had three failures due to the judge's context limit. These cases receive zero under the native scoring rules, remain in the denominator, and are reported in the completed evaluations. Their scores are included in the averages.
- Prosa-PT: 981 conversations after 19 fixed exclusions. Rubrics without a recognized verdict are excluded from the denominator, following the native grader.
- Arena-Hard v2: the primary score uses 100 hard tasks, with the native weighting and bootstrap procedure. The 50 creative-writing prompts are excluded from this score.
- CAPITU: 200 single-turn prompts and 100 three-turn conversations. Citation grading accounts for typographic quotation marks; full-conversation results are a secondary metric.
- Lumen: 1,296 scenarios and 22 benign controls. Tucano Think completed 0/22 controls and is not assigned a safety score: its lack of harmful actions is not treated as demonstrated safety. This result is excluded from the averages.
- MMLU-PT and Global-MMLU PT: answer choices were extracted from chat responses; no equivalence is claimed with evaluations based on answer-choice probabilities.
- CulturalBench Hard: 1,227 groups, with four answers per group. A group counts as correct only when all four answers are correct.
- Structured Output Benchmark: weighted score over the 5,000 text items; the 324 OCR/transcription inputs are excluded from the primary denominator.
- BrowseComp-Plus: correct answers divided by all 100 selected questions.
- LongBench v2: 503 questions. Context limits vary by model; confirmed context-overflow cases receive zero and remain in the evaluation population.
- OAB-Bench: 210 questions from editions 39–44, across seven subject areas and 42 exams. Magis-Bench: 74 questions and 24 exam sections. Both use their native exam/section aggregation, converted to a 0–100 scale.
- CondutaBench: a stratified sample of 140/715 questions, covering 14 guidelines. ENADE-QA: the health-domain subset, with 716 questions.
- Tool calling not supported indicates that no tool-use evaluation is available; it is not a score of zero.
S5-nano evaluation setup
Sampling parameters match the mode-specific recommendations used for Qwen3.5-4B. The context window was 262,144 tokens, with the qwen3 and qwen3_coder parsers.
During evaluation, Think used the remaining context space for output, without an additional cap. Instruct generally used a 32,768-token limit. For MATH-PT, Instruct used the math configuration: temperature 1.0, top-p 1.0, top-k 40, presence penalty 2.0, and an 81,920-token limit. The llama.cpp usage examples below retain the recommended 32,768-token limit.
Recommended generation parameters
- Select the mode per request with chat_template_kwargs; the same server
supports both modes.
- For harder problems in Think mode, max_tokens can be increased to 81,920.
- generation_config.json includes the Think-mode values, but not presence_penalty. Send the parameters with every request.
Serving with vLLM
vllm serve maritaca-ai/S5-nano \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice --tool-call-parser qwen3_coder
The server starts at http://localhost:8000/v1 and is compatible with the OpenAI API.
Optional flags:
- --speculative-config '{"method":"mtp","num_speculative_tokens":3}' enables
speculative decoding with the MTP layer;
- --language-model-only excludes the vision encoder, freeing memory for
the KV cache;
- --max-model-len 32768 reduces the context length for GPUs with less memory.
For the FP8 version, replace the model name with maritaca-ai/S5-nano-FP8
and keep the same flags.
Requests with curl
Think mode:
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "maritaca-ai/S5-nano",
    "messages": [
      {"role": "user", "content": "Explain why the sky is blue."}
    ],
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 20,
    "min_p": 0.0,
    "presence_penalty": 1.5,
    "max_tokens": 32768
  }'
Reasoning is returned in choices[0].message.reasoning, and the final answer
in choices[0].message.content.
Instruct mode:
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "maritaca-ai/S5-nano",
    "messages": [
      {"role": "user", "content": "Write a haiku about the Cerrado."}
    ],
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 20,
    "min_p": 0.0,
    "presence_penalty": 1.5,
    "max_tokens": 32768,
    "chat_template_kwargs": {"enable_thinking": false}
  }'
Requests with the OpenAI library
top_k, min_p, and chat_template_kwargs are not part of the OpenAI API;
pass them in extra_body.
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
MODEL = "maritaca-ai/S5-nano"
THINK = dict(
    temperature=1.0,
    top_p=0.95,
    presence_penalty=1.5,
    max_tokens=32768,
    extra_body={"top_k": 20, "min_p": 0.0},
)
INSTRUCT = dict(
    temperature=0.7,
    top_p=0.8,
    presence_penalty=1.5,
    max_tokens=32768,
    extra_body={
        "top_k": 20,
        "min_p": 0.0,
        "chat_template_kwargs": {"enable_thinking": False},
    },
)
# Think
messages = [{"role": "user", "content": "Explain why the sky is blue."}]
resp = client.chat.completions.create(model=MODEL, messages=messages, **THINK)
msg = resp.choices[0].message
reasoning = getattr(msg, "reasoning", None)
print("reasoning:", reasoning)
print("answer:", msg.content)
# Next turn: pass the reasoning back along with the answer
messages.append({"role": "assistant", "content": msg.content, "reasoning": reasoning})
messages.append({"role": "user", "content": "And why does the sunset look reddish?"})
resp = client.chat.completions.create(model=MODEL, messages=messages, **THINK)
print(resp.choices[0].message.content)
# Instruct
resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Write a haiku about the Cerrado."}],
    **INSTRUCT,
)
print(resp.choices[0].message.content)
The model was trained with reasoning from previous turns retained in the
conversation history. In multi-turn conversations, include the reasoning
field from each assistant response, as shown above.
Serving with llama.cpp
The maritaca-ai/S5-nano-GGUF repository provides three quantization variants and the vision projector:
llama-server -hf maritaca-ai/S5-nano-GGUF:Q4_K_M --jinja -c 32768 -ngl 99
- Replace Q4_K_M with Q8_0 or BF16 to use a different quantization.
- -hf also downloads mmproj; use --no-mmproj for text-only serving.
- --spec-type draft-mtp --spec-draft-n-max 3 enables speculative decoding
with the MTP layer, which is included in all three GGUFs.
The server starts at http://localhost:8080/v1. The curl and Python examples
above work after changing the port, with the same parameters and
chat_template_kwargs. The reasoning field has a different name:
llama-server uses reasoning_content instead of reasoning, both in the
response and in the conversation history.
- Downloads last month
- 263
