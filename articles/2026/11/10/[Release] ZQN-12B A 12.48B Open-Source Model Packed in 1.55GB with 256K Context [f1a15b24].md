---
id: "f1a15b2458822a8d"
title: "[Release] ZQN-12B: A 12.48B Open-Source Model Packed in 1.55GB with 256K Context"
url: "https://reddit.com/r/artificial/comments/1xstm27/release_zqn12b_a_1248b_opensource_model_packed_in"
link: "https://reddit.com/r/artificial/comments/1xstm27/release_zqn12b_a_1248b_opensource_model_packed_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T17:52:28Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["ZAQERIS_Ai"]
language: "en"
summary: "Hi everyone, We wanted to share ZQN-12B , an open-source foundation model developed by the ZAQERIS AI Research Group. Our main goal was to achieve deep reasoning and long context capabilities while drastically reducing memory requirements so it can run smoothly on consumer hardware. 🔍 Quick Overview & Specs: - Parameter Count: 12.48 Billion physical parameters ($d=5120$, 40 layers, GQA 32:8). -…"
tags: ["r/artificial"]
orgs: ["Hugging Face"]
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 270
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xstm27/release_zqn12b_a_1248b_opensource_model_packed_in/"
score: null
comments: null
community: "r/artificial"
---

# [Release] ZQN-12B: A 12.48B Open-Source Model Packed in 1.55GB with 256K Context

Reddit · ZAQERIS_Ai · 2026-11-10

Hi everyone, We wanted to share ZQN-12B , an open-source foundation model developed by the ZAQERIS AI Research Group. Our main goal was to achieve deep reasoning and long context capabilities while drastically reducing memory requirements so it can run smoothly on consumer hardware. 🔍 Quick Overview & Specs: - Parameter Count: 12.48 Billion physical parameters ($d=5120$, 40 layers, GQA 32:8). - Extreme Compression (1.55 GB): Uses a 16D Barnes-Wall lattice quantization format (M4-Gold), storing the entire model in just 1.55 GB across 2 Safetensors shards, running in ~3.34 GB VRAM. - Dynamic Expansion (DVMU): Automatically activates ephemeral reasoning pathways (+3.0B for math / +8.0B for software engineering) based on contextual complexity. - 256K Extended Context: 131,072 native tokens scalable up to 262,144 tokens via full progressive YaRN RoPE. - Latent Tri-Agent Deliberation: Internal consensus between Thesis, Critic, and Arbiter in under 250ms directly inside latent space. - Typo Invariance (ASSC-TIDD): Recovers intent from keyboard slips and morpho-phonetic errors with 99.6% accuracy. - Languages: Native Arabic and English support. 💻 How to Run It: You can test it directly with Hugging Face Transformers: ```python import torch from transformers import AutoModelForCausalLM, AutoTokenizer model_id = "ZAQERIS/ZAQION-12B" tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained( model_id, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True ) prompt = "Hello! What are your core capabilities?" inputs = tokenizer(prompt, return_tensors="pt").to(model.device) outputs = model.generate(**inputs, max_new_tokens=150) print(tokenizer.decode(outputs[0], skip_special_tokens=True)) ``` 📂 Hugging Face Repository: https://huggingface.co/ZAQERIS/ZAQION-12B The repo includes the full architecture code, complete technical papers, and executable verification scripts for parameter counting, KV cache, and YaRN context scaling. Released under the Apache 2.0 license. We would love to hear your feedback, thoughts, or test results!
