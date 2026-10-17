---
id: "d9cd0593d3d88610"
title: "Gen-Verse/DiscoveryRSI-27B (finetune)"
url: "https://huggingface.co/Gen-Verse/DiscoveryRSI-27B"
link: "https://huggingface.co/Gen-Verse/DiscoveryRSI-27B"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-17T10:11:01Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["jacek2023"]
language: "en"
summary: "🎯 About This Repository This repository contains the DiscoveryRSI-27B model release for DiscoveryRSI , a research system that recursively develops, evaluates, revises, and attributes scientific hypotheses. DiscoveryRSI-27B is an instruction-finetuned 27B language model intended for research ideation and evidence-grounded planning. It helps turn a research question and available evidence into an…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Google"]
topics: ["models & research", "products & launches", "health & science"]
content_source: "fulltext"
word_count: 852
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x86mh7/genversediscoveryrsi27b_finetune/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Gen-Verse/DiscoveryRSI-27B (finetune)

Hugging Face · jacek2023 · 2026-10-17

Instructions to use Gen-Verse/DiscoveryRSI-27B with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use Gen-Verse/DiscoveryRSI-27B with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="Gen-Verse/DiscoveryRSI-27B") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("Gen-Verse/DiscoveryRSI-27B", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use Gen-Verse/DiscoveryRSI-27B with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "Gen-Verse/DiscoveryRSI-27B"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Gen-Verse/DiscoveryRSI-27B",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}' Use Docker docker model run hf.co/Gen-Verse/DiscoveryRSI-27B
-  SGLang  How to use Gen-Verse/DiscoveryRSI-27B with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "Gen-Verse/DiscoveryRSI-27B" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Gen-Verse/DiscoveryRSI-27B",
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
        --model-path "Gen-Verse/DiscoveryRSI-27B" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "Gen-Verse/DiscoveryRSI-27B",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
-  Docker Model Runner  How to use Gen-Verse/DiscoveryRSI-27B with Docker Model Runner: docker model run hf.co/Gen-Verse/DiscoveryRSI-27B
🎯 About This Repository
This repository contains the DiscoveryRSI-27B model release for DiscoveryRSI, a research system that recursively develops, evaluates, revises, and attributes scientific hypotheses.
DiscoveryRSI-27B is an instruction-finetuned 27B language model intended for research ideation and evidence-grounded planning. It helps turn a research question and available evidence into an explicit hypothesis, investigation plan, alternatives, decision criteria, and falsification conditions.
🌟 Introduction
DiscoveryRSI treats a hypothesis as a versioned research object rather than a finished answer. The model is designed to support a loop of:
- 🔎 Explore: identify valuable questions and candidate explanations
- 🧪 Evaluate: propose tests, comparators, evidence, and decision criteria
- 🛠️ Revise: repair weak designs and incorporate criticism
- 🧬 Attribute: record which research behaviors improved a hypothesis
- 🔁 Learn: use replay and attribution to improve future research paths
The model works with the public DiscoveryRSI harness, role prompts, tool registry, replay store, and domain adapters. The public system supports life-science research workflows including GEO-derived pathway analysis and therapeutic-target prioritization.
📦 Resources
📋 Model Details
The exact base model, training-data manifest, preprocessing format, evaluation configuration, and final checkpoint metadata should be read from the files published in this repository. Private campaign traces, credentials, patient rows, restricted datasets, and laboratory infrastructure are not included.
🚀 Intended Use
DiscoveryRSI-27B is intended for:
- research ideation and hypothesis generation;
- critique and revision of proposed experiments;
- evidence-grounded research planning;
- explicit alternatives, comparators, and falsification criteria; and
- use through the DiscoveryRSI agentic harness.
The model is not a medical device. Do not use it to make clinical, diagnostic, treatment, or other high-stakes decisions. Generated hypotheses require expert review and independent verification.
💻 Usage
After the checkpoint files are published, the model can be loaded with the
standard Transformers interfaces. Use the exact transformers version,
checkpoint revision, and generation settings listed in this repository:
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "Gen-Verse/DiscoveryRSI-27B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
prompt = "Develop a testable research hypothesis about a disease pathway."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
For multi-step research workflows, follow the DiscoveryRSI quick start and configure a provider adapter for the checkpoint.
🧪 Training and Evaluation
DiscoveryRSI uses hypothesis development, criticism, revision, contribution attribution, harness replay, and DFM-Bench-style process evaluation. Release documentation should report the base-model identity, training-data provenance, instruction format, evaluation configuration, and known limitations. Results should be interpreted as research-process evidence rather than proof that a generated hypothesis is correct or clinically useful.
⚠️ Limitations and Responsible Use
The model can produce plausible but unsupported claims, omit relevant evidence, misread sources, or propose infeasible experiments. It may reflect biases and errors in its base model and instruction-tuning data. Users should preserve source provenance, check citations, inspect alternatives and falsification criteria, and have a qualified researcher review outputs before acting on them.
📝 Citation
If you use DiscoveryRSI-27B or the accompanying harness, cite the technical report and link to the released model:
@software{discoveryrsi,
  title  = {DiscoveryRSI},
  url    = {https://github.com/Gen-Verse/DiscoveryRSI},
  note   = {Recursive scientific hypothesis discovery and DiscoveryRSI-27B}
}
See the repository citation section for the maintained technical-report and model links.
📄 License
The model license, base-model terms, and dataset attribution requirements must be stated in this card with the checkpoint release. The DiscoveryRSI code repository is licensed under Apache-2.0; that code license does not by itself determine the model or training-data license.
