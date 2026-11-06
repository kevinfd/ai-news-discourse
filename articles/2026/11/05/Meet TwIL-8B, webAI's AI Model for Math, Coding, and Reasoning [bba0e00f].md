---
id: "bba0e00fe87987e2"
title: "Meet TwIL-8B, webAI's AI Model for Math, Coding, and Reasoning"
url: "https://hackernoon.com/meet-twil-8b-webais-ai-model-for-math-coding-and-reasoning"
link: "https://hackernoon.com/meet-twil-8b-webais-ai-model-for-math-coding-and-reasoning"
source: "HackerNoon"
domain: "hackernoon.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-05T16:00:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: []
language: "en"
summary: "TwIL-8B is an AI model designed for math, coding, and reasoning. Explore its balanced and verbose variants, benchmark results, and limitations."
tags: []
orgs: ["IBM"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 791
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet TwIL-8B, webAI's AI Model for Math, Coding, and Reasoning

HackerNoon · 2026-11-05

Overview
TwIL-8B is an 8.79B-parameter English text-generation model from webAI-Official, post-trained from IBM Granite 4.2 8B for contest mathematics, code, and instruction following. It has balanced (default) and verbose variants. The supplied benchmark results show strengths in math, code, and instruction following, with weaker results on knowledge-heavy benchmarks.
Best use cases
Use it for text-based contest math, code generation or problem solving, and instruction-following tasks. The balanced variant is intended for general use with shorter reasoning traces; the verbose variant is intended for difficult contest-style problems where longer reasoning is acceptable.
Limitations
Knowledge-heavy results are a documented weakness: GPQA Diamond is 70.2, and the supplied comparisons show lower scores than Qwen3.5-9B and Gemma 4 31B on GPQA Diamond, MMLU-Pro, and HLE. The model can produce long reasoning traces; benchmark token counts are directional because harnesses and tokenizers differ. There is no safety or preference tuning beyond what the Granite 4.2 base carries. Several reported results, including LiveCodeBench, IFBench, and knowledge benchmarks, were measured on verbose and have not yet been run on balanced; competitor figures were published results and were not rerun.
How it compares
Against Qwen3.5-9B, the supplied results show TwIL-8B ahead on MATH-500, LiveCodeBench, IFBench, and two of four shared contest sets, while behind on GPQA Diamond, MMLU-Pro, AIME 2026, and HMMT Feb 2026. Against Gemma 4 31B, it leads on MATH-500, AIME 2025, and LiveCodeBench, but trails on several knowledge, instruction-following, and contest benchmarks. These are source-reported comparisons, not controlled reruns. Other supplied internal model pages include TwIL-LM3-Pro and TwIL-LM3; their descriptions focus on formal logic and do not establish direct benchmark comparability with TwIL-8B.
Technical specifications
Granite decoder-only dense transformer using GraniteForCausalLM; 40 layers, hidden size 4096, 32 attention heads and 8 KV heads. It has 8,791,592,960 parameters, a tokenizer vocabulary of 100,352, and a 131,072-token context window inherited from the base model. The model is post-trained with full-parameter supervised fine-tuning and GRPO/DAPO reinforcement learning; balanced additionally uses length-aware RL. Both variants share architecture, tokenizer, chat template, and generation configuration. Checkpoints are bfloat16 (16.38 GiB per variant), with GGUF builds; the supplied description lists a 4.98 GiB Q4_K_M build for balanced. License: webAI Non-Commercial License version 1.0; the base model is identified as Apache License 2.0. Evaluation is described as high-effort pass@1 with thinking enabled; no hardware or latency measurements are supplied.
Model inputs and outputs
Inputs
Text input in English, formatted with the model's chat template. The supplied example uses a user message and apply_chat_template; the model card describes text input and text output. The default chat format emits a ... reasoning block before the answer.
Outputs
Generated text, typically with a reasoning block followed by an answer. Balanced is described as producing shorter reasoning traces; verbose produces longer traces. The supplied example sets max_new_tokens to 32768, but this is an example setting rather than a stated model limit.
Getting started
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "webAI-Official/TwIL-8B"
variant = None  # balanced by default; use "verbose" for the verbose variant
tok = AutoTokenizer.from_pretrained(model_id, subfolder=variant or "")
model = AutoModelForCausalLM.from_pretrained(
    model_id, subfolder=variant or "", dtype=torch.bfloat16, device_map="auto"
)
messages = [{"role": "user", "content": "How many positive integers n < 1000 are divisible by 3 but not by 5? Reason step by step, then give the final integer."}]
inputs = tok.apply_chat_template(
    messages, add_generation_prompt=True,
    return_tensors="pt", return_dict=True,
).to(model.device)
out = model.generate(**inputs, max_new_tokens=32768)
print(tok.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
Frequently asked questions
Q: Which variant loads by default?
A: Loading webAI-Official/TwIL-8B without a subfolder selects balanced. Use the verbose subfolder to load the verbose variant.
Q: How do the variants differ?
A: They share architecture, tokenizer, chat template, and generation configuration. Balanced is intended for general use with shorter reasoning traces; verbose is intended for hard contest-style problems with longer traces.
Q: What tasks is TwIL-8B designed for?
A: Its stated specializations are contest mathematics, code, and instruction following. It is an English text-in/text-out model.
Q: What context window is specified?
A: The supplied model details specify 131,072 tokens, inherited from the Granite 4.2 base model.
Q: Does the model provide strong general knowledge performance?
A: The supplied comparisons identify knowledge-heavy benchmarks as a weakness. GPQA Diamond is 70.2, and the reported MMLU-Pro and HLE results also trail several compared models.
Q: Are all benchmark results for the balanced variant?
A: No. The source marks several results, including LiveCodeBench, IFBench, MMLU-Pro, and HLE, as measured on verbose and not yet run on balanced.
Q: What license applies?
A: The model is listed under the webAI Non-Commercial License version 1.0. The supplied details separately identify the Granite 4.2 base model's license as Apache License 2.0.
This is a simplified guide to an AI model called TwIL-8B maintained by webAI-Official. If you like these kinds of analysis, join AIModels.fyi or follow us on Twitter.
