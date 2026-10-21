---
id: "66aafeba3e783ec1"
title: "InternScience/Sage-A1.5 [Finetune of Qwen 3.6 35b-a3b]"
url: "https://huggingface.co/InternScience/Sage-A1.5"
link: "https://huggingface.co/InternScience/Sage-A1.5"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-21T08:59:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Skyline34rGt"]
language: "en"
summary: "Gguf's: https://huggingface.co/InternScience/Sage-A1.5-Q4_K_M-GGUF https://huggingface.co/InternScience/Sage-A1.5-Q8_0-GGUF \" Sage‑A1.5 is a 35B Mixture‑of‑Experts agentic model based on Qwen3.6-35B-A3B from Shanghai AI Laboratory, built to advance long-horizon scientific problem solving through adaptive capability composition. Building upon A1 , Sage‑A1.5 learns not only to solve individual…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face", "Google", "Alibaba"]
topics: ["models & research", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 2188
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbi1hj/internsciencesagea15_finetune_of_qwen_36_35ba3b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# InternScience/Sage-A1.5 [Finetune of Qwen 3.6 35b-a3b]

Hugging Face · Skyline34rGt · 2026-10-21

Instructions to use InternScience/Sage-A1.5 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use InternScience/Sage-A1.5 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="InternScience/Sage-A1.5")
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
processor = AutoProcessor.from_pretrained("InternScience/Sage-A1.5")
model = AutoModelForMultimodalLM.from_pretrained("InternScience/Sage-A1.5", device_map="auto")
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
-  vLLM  How to use InternScience/Sage-A1.5 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "InternScience/Sage-A1.5"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "InternScience/Sage-A1.5",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/InternScience/Sage-A1.5
-  SGLang  How to use InternScience/Sage-A1.5 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "InternScience/Sage-A1.5" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "InternScience/Sage-A1.5",
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
        --model-path "InternScience/Sage-A1.5" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "InternScience/Sage-A1.5",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use InternScience/Sage-A1.5 with Docker Model Runner: docker model run hf.co/InternScience/Sage-A1.5
Sage-A1.5
This repository contains model weights and configuration files for Sage-A1.5 in the Hugging Face Transformers format.
These artifacts are compatible with Hugging Face Transformers, vLLM, SGLang, etc.
Sage‑A1.5 is a 35B Mixture‑of‑Experts agentic model based on Qwen3.6-35B-A3B from Shanghai AI Laboratory, built to advance long-horizon scientific problem solving through adaptive capability composition. Building upon A1, Sage‑A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution, highlighting three key capabilities: Agentic Orchestration, Verification, and Open Scientific Discovery.
First, agentic orchestration extends single-agent execution through task delegation and parallel collaboration among subagents with isolated contexts, enabling complex tasks to be decomposed and addressed concurrently while reducing interference across concurrent subagents. Second, agentic verification strengthens long-horizon reliability through progress checking, evidence validation, and reflective strategy revision, allowing Sage‑A1.5 to recognize unproductive search paths and pursue alternative approaches. Third, open scientific discovery extends agentic capabilities beyond answering predefined questions to conducting exploratory research, connecting scientific inquiry with interactive analysis and inspectable research artifacts. We hope Sage‑A1.5 provides the community with an accessible foundation for open scientific discovery, offering a practical path from long-horizon task execution to collaborative, verifiable, and inspectable scientific exploration.
Highlights
- Agentic Orchestration: Orchestrates parallel investigations across subagents with independent contexts, enabling them to challenge assumptions, refine conclusions through evidence, and synthesize their findings into comprehensive results.
- Verification Mode: An opt-in self-review capability that lives inside the model's own chain of thought — the model pauses mid-trajectory to review what it has established and what has failed, then acts on a revised direction in the same turn, with no external critic.
- Agentic Reasoning: Sage-A1.5 excels at decomposing complex tasks into executable sub-steps, planning ahead, and adapting its strategy based on intermediate results.
- Tool Use: Natively supports function calling and tool integration, enabling seamless interaction with APIs, code interpreters, search engines, and other external tools.
- Scientific and Professional Reasoning: Handles tool-integrated scientific reasoning and professional knowledge question answering.
- Instruction Following: Precisely follows detailed, multi-constraint instructions across diverse domains.
We welcome developers and enterprises to integrate and try Sage-A1.5 and share their feedback.
Performance
We evaluate Sage-A1.5 in real-world agentic and research-oriented workflows across six directions — long-horizon search, engineering tasks, instruction following, scientific research, general agentic tasks, and scientific agentic tasks. Despite operating in the ~35B model class, Sage-A1.5 delivers highly competitive performance against frontier-scale systems such as Kimi-K3, GLM-5.3, and GPT-5.6-sol. It achieves overall SOTA on XBench-DS-2510 (92.0), IFBench (81.6), PinchBench (90.0), FrontierScience-Olympiad (81.0), FrontierScience-Research (48.3), CMT (80.0), and OmniDocBench (91.5), and reaches 95.1 on GAIA — higher than every larger-scale model we compare against. Among comparable ~35B models it ranks first on a broad range of tasks, including BrowseComp (81.7), SWE-bench Pro (61.2), MLE-Lite (65.2), SciCode (44.3, tied with Agents-A1), AA-LCR (81.0), HLE w/ tools (55.1), VitaBench (45.4), and ChemCOTBench (66.5). Compared with A1, it improves substantially on engineering and agentic workloads (SWE-bench Pro +17.6, SWE-bench Multilingual +14.0, PinchBench +13.1, MLE-Lite +21.3). These results show that Sage-A1.5 combines strong long-horizon search ability, robust scientific reasoning, and reliable instruction following, establishing it as a highly capable and efficient agentic model that narrows the gap with much larger frontier models.
🥇 Overall SOTA 🟢 Best Among Comparable Models (~35B)
SWE-Bench Series: We use the mini-SWE-agent harness with a temperature of 1.0, top-p of 0.95, a 200K-token context window, and automatic context compaction enabled. All evaluations are conducted in a fully offline environment without internet access.
GLM-5.3 on OmniDocBench: GLM-5.3 is a text-only (unimodal) model without multimodal input support, so its results on OmniDocBench, a multimodal benchmark, are not reported.
Usage
SGLang
SGLang is a fast serving framework for large language models and vision language models.
Install SGLang with uv:
uv venv --python 3.12 --seed --managed-python
source .venv/bin/activate
uv pip install sglang
See its documentation for more details.
The following commands create API endpoints at http://localhost:8000/v1:
- Standard Version: python -m sglang.launch_server \
  --model-path InternScience/Sage-A1.5 \
  --port 8000 \
  --mem-fraction-static 0.8 \
  --context-length 262144 \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_coder
- Multi-Token Prediction (MTP): python -m sglang.launch_server \
  --model-path InternScience/Sage-A1.5 \
  --port 8000 \
  --mem-fraction-static 0.8 \
  --context-length 262144 \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_coder \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4
vLLM
vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.
Install vLLM from the main branch via uv:
uv venv --python 3.12 --seed --managed-python
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
See its documentation for more details.
The following commands create API endpoints at http://localhost:8000/v1:
- Standard Version (1 GPUs, 262K context): vllm serve InternScience/Sage-A1.5 \
  --port 8000 \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
- Text-Only (skips vision encoder to free KV cache memory): vllm serve InternScience/Sage-A1.5 \
  --port 8000 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --language-model-only
- Multi-Token Prediction (MTP): vllm serve InternScience/Sage-A1.5 \
  --port 8000 \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"}'
Advanced Modes
Sage-A1.5 ships two opt-in modes that build on the standard serving setup above. Both are off by default: Agentic Orchestration Mode is turned on by registering a tool, Verification Mode by a chat-template flag.
Agentic Orchestration
Agentic Orchestration Mode (see Highlights) lets the model fan out independent sub-questions to
sub-agents that run in parallel, each with its own context window and its own tool access. It is
enabled by exposing a spawn_subagent tool to the model: the model calls it whenever a task
decomposes into independent investigations, and your harness runs each sub-task and returns the
structured results.
Sub-agents are not restricted to any fixed tool set — they can be given whatever tools your
deployment registers (search, page reading, code execution, retrieval, internal APIs, …). By default
they inherit the main agent's tools; set subagent_tools if you want them to have a different, for
instance narrower, set.
Register the following tool schema alongside your other tools:
SPAWN_SUBAGENT_SCHEMA = {
    "type": "function",
    "function": {
        "name": "spawn_subagent",
        "description": (
            "Dispatch one or more sub-agents IN PARALLEL to investigate independent "
            "sub-questions. Each sub-agent has access to google_search and read_page "
            "but CANNOT see your conversation. You MUST give each sub-agent everything "
            "it needs via the `task`, `context`, and `expected_output` fields. Sub-agents "
            "return structured JSON: {answer, status, evidence, unresolved_issues}."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "tasks": {
                    "type": "array",
                    "minItems": 1,
                    "description": "List of independent sub-tasks to dispatch in parallel.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "task": {
                                "type": "string",
                                "description": "Self-contained sub-question. The sub-agent has no other context.",
                            },
                            "context": {
                                "type": "string",
                                "description": "Background facts and constraints the sub-agent needs.",
                            },
                            "expected_output": {
                                "type": "string",
                                "description": "Form of the desired answer (e.g. 'a year YYYY', 'a person name').",
                            },
                        },
                        "required": ["task", "context", "expected_output"],
                    },
                },
            },
            "required": ["tasks"],
        },
    },
}
Because a sub-agent cannot see the main conversation, every task must be self-contained — task,
context, and expected_output are all required. Each sub-agent returns one compact JSON object
{answer, status, evidence, unresolved_issues}, and the batch is handed back to the main model in
input order.
Notes:
- Keep each sub-task independent. Tasks in one batch run concurrently and cannot see each
other's results, so anything sequential belongs in separate spawn_subagent calls.
- expected_output acts as a format constraint on the sub-agent's answer (e.g. 'a year YYYY', 'a person name'), which keeps results short and easy to merge.
- A sub-agent that cannot resolve its task returns "UNKNOWN" with a status of unknown or insufficient_evidence rather than guessing — check status before using an answer.
- Batch size and per-sub-agent turn budget are harness-side settings
(max_tasks_per_spawn, default 5; subagent_max_turns, default 20). Oversized batches are
rejected with an error message instead of being truncated.
- The schema's description above names google_search and read_page because that is the
reference setup. If you give sub-agents a different tool set, update that sentence to match —
it is what tells the main model what its sub-agents can actually do.
Verification Mode
Verification Mode (see Highlights) is opt-in and off by default. Enable it per request by
passing verification through chat_template_kwargs; the chat template then appends the verification
protocol trigger to the end of your system message.
- OpenAI Python client (via extra_body):
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="InternScience/Sage-A1.5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Find the population of Beijing and cross-check it."},
    ],
    tools=TOOLS,
    extra_body={"chat_template_kwargs": {"verification": True}},
)
message = response.choices[0].message
print(message.reasoning_content)  # self-review happens inside the chain of thought
print(message.content)
- curl: curl http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "InternScience/Sage-A1.5",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Find the population of Shanghai and cross-check it."}
    ],
    "chat_template_kwargs": {"verification": true}
  }'
Notes:
- A non-empty system message is required. Because the trigger is appended to the end of the system
content, a request with verification: true and no system message (or a whitespace-only one) is
rejected with HTTP 400.
- Pass a JSON boolean, not a string: {"verification": true}, not {"verification": "true"}.
- Omitting chat_template_kwargs is equivalent to {"verification": false}, which renders the prompt
unchanged.
- Verification Mode is independent of tool use — it works with or without tools.
- The self-review is emitted as reasoning content, so read reasoning_content in addition to content.
Recommended Sampling Parameters
For the best generation quality, we recommend the following sampling parameters:
- temperature: 1.0
- top_p: 0.95
- top_k: 20
- min_p: 0.0
- presence_penalty: 1.5
- repetition_penalty: 1.0
Agent Capability Evaluation
To provide the community with a unified agent evaluation codebase for fair comparison, we have also open-sourced an evaluation framework for assessing agentic models across core capabilities, including tool use and multi-step reasoning. The evaluation code is included in the Sage-A1/evaluation of this repository.
We use this framework to evaluate the released model under a standardized and reproducible setting. Specifically, the model is tested on a set of agent-oriented tasks that require it to understand user goals, decompose complex instructions, interact with tools or environments when necessary, and produce final results. The evaluation results reported in Model Card are generated using the open-source framework above, so that users can reproduce the experiments, compare other models under the same protocol, and further extend the benchmark for new agent scenarios. (Note that: To ensure a fair comparison, we report the benchmark results from their original technical reports. If a model does not report the corresponding benchmark results, we evaluate it using the same evaluation protocol as our model.)
For detailed evaluation scripts, task definitions, metrics, and reproduction instructions, please refer to the evaluation codebase.
Citation
If you find our work helpful, feel free to give us a cite.
@misc{lou2026sagea15longhorizonexecutionscientific,
      title={Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition}, 
      author={Sage-A1.5 Team},
      year={2026},
      eprint={2610.28578},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2610.28578}, 
}
- Downloads last month
- 58
