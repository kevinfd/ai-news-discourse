---
id: "3da203190003ff2e"
title: "tencent/Hy-Memory-30B-A3B · Hugging Face"
url: "https://huggingface.co/tencent/Hy-Memory-30B-A3B"
link: "https://huggingface.co/tencent/Hy-Memory-30B-A3B"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-16T10:10:59Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["paf1138"]
language: "en"
summary: "interesting focus: \"A 3B active model beats Opus 5 at memory\" (whatever that means :D)"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "DeepSeek", "Google", "Hugging Face"]
topics: ["models & research", "jobs & society", "chips & infrastructure"]
content_source: "fulltext"
word_count: 950
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7cc2z/tencenthymemory30ba3b_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# tencent/Hy-Memory-30B-A3B · Hugging Face

Hugging Face · paf1138 · 2026-10-16

Instructions to use tencent/Hy-Memory-30B-A3B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use tencent/Hy-Memory-30B-A3B with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="tencent/Hy-Memory-30B-A3B")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("tencent/Hy-Memory-30B-A3B")
model = AutoModelForCausalLM.from_pretrained("tencent/Hy-Memory-30B-A3B", device_map="auto")
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
-  vLLM  How to use tencent/Hy-Memory-30B-A3B with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "tencent/Hy-Memory-30B-A3B"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "tencent/Hy-Memory-30B-A3B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/tencent/Hy-Memory-30B-A3B
-  SGLang  How to use tencent/Hy-Memory-30B-A3B with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "tencent/Hy-Memory-30B-A3B" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "tencent/Hy-Memory-30B-A3B",
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
        --model-path "tencent/Hy-Memory-30B-A3B" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "tencent/Hy-Memory-30B-A3B",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use tencent/Hy-Memory-30B-A3B with Docker Model Runner: docker model run hf.co/tencent/Hy-Memory-30B-A3B
Model Introduction
Hy-Memory-30B-A3B is a compact long-term-memory writer model (~3B active parameters) developed by Tencent Hunyuan to execute the write path inside external memory frameworks. It directly replaces the general-purpose LLM inside Mem0, MemOS, and Hy-Memory (covering Chat, Working, and Coding scenarios), deciding what information to retain, how precisely to represent it, and how new evidence should update the persistent memory bank. The model is trained in two stages—Memory On-Policy Distillation (OPD) followed by Attributed Memory Reinforcement Learning—and transfers directly to unseen memory frameworks such as EverMemOS.
Cross-harness macro-average scores on the fixed 20% benchmark matrix. Each harness score averages six metrics equally; Overall averages the four harnesses equally. EverMemOS is held out from training.
Two-Stage Training
Figure 1: Hy-Memory-30B-A3B is trained inside the same deployed harness configurations in both stages. OPD supplies dense teacher supervision on student-written state chains; RL examines the resulting banks, assigns chunk-level credit, and carries the selected bank across windows. In the rollout grid, each cell is the bank after chunk t of rollout i, shaded by its chunk score s_i[t]. Advantages are normalized within each column (dashed: one chunk-level group), so the best rollout can differ from chunk to chunk. The outlined cell is the final bank with the highest sum_t s_i[t], which becomes the parent of the next window.
Experiments
Evaluation Principles
The evaluation changes only the memory writer. For each comparison, the harness version and prompts are fixed, retrieval configuration is fixed, and the answer model, judge, and other framework-side components are held fixed. Throughout this report, every reference to a DeepSeek Flash endpoint denotes DeepSeek V4.1 Flash. Decoding settings are matched where APIs permit, each writer builds its own bank from an empty state, and test examples and scoring rules are identical.
For computational efficiency, every benchmark in the main four-harness matrix is evaluated on a fixed 20% subsample. Each harness score is the equal-weight average of six metrics: LoCoMo Judge, LongMemEval (LME), PersonaMem-v2 (PM-v2), Travel SPS, Shopping PS, and Code Memory Bench (CMB). CMB is itself the equal-weight average of two repository QA evaluations. The overall score is the equal-weight average of the four harness scores.
Final Cross-Harness Results
Table 1: Six-metric means on fixed 20% benchmark subsamples. The macro average weights the four harnesses equally.
Detailed Benchmark Results
Tables 2–5 report the six benchmark scores used to compute each harness mean in Table 1 on the same fixed 20% benchmark subsamples.
Table 2: Detailed results on the Mem0 harness
Table 3: Detailed results on the Hy-Memory harness
Table 4: Detailed results on the MemOS harness
Table 5: Detailed results on the held-out EverMemOS harness
Quickstart
Deploy the model with vLLM (tested with v0.31.0) using --served-model-name hy-memory, then call the OpenAI-compatible API. The example below extracts user facts and preferences with no-think mode enabled.
from openai import OpenAI
client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="EMPTY",
)
response = client.chat.completions.create(
    model="hy-memory",
    messages=[
        {
            "role": "system",
            "content": (
                "Extract explicit user facts and preferences from the conversation. "
                "Write each memory as a concise, self-contained statement. "
                "Do not infer or invent information. "
                'Return only a JSON object with a "memories" list of strings.'
            ),
        },
        {
            "role": "user",
            "content": (
                "My name is Alex. I live in Seattle and work as a software engineer. "
                "I mainly use Python and prefer concise answers with code examples. "
                "I'm vegetarian, so please keep that in mind when suggesting meals."
            ),
        },
    ],
    temperature=0.0,
    max_tokens=512,
    extra_body={
        "chat_template_kwargs": {
            "reasoning_effort": "no_think",
        },
    },
)
Resource Availability
- Framework Code & Evaluation Utilities: https://github.com/Tencent-Hunyuan/Hy-Memory
- Model Weights, Configuration, and Model Card: https://huggingface.co/tencent/Hy-Memory-30B-A3B
- Technical Report: https://arxiv.org/pdf/2610.22196
- Downloads last month
- -
