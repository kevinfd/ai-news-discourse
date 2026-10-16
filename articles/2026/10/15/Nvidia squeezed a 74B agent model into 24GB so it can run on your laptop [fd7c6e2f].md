---
id: "fd7c6e2ff025b00c"
title: "Nvidia squeezed a 74B agent model into 24GB so it can run on your laptop"
url: "https://thenewstack.io/nvidia-nemotron-bolt-laptop"
link: "https://thenewstack.io/nvidia-nemotron-bolt-laptop"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T16:00:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Nvidia on Thursday announced a few new additions to its  Nemotron family : Nemotron 3.5 Super VL, a 120B vision-language model for enterprise agents and two small Bolt models ( Nemotron 3.5 Bolt 74B-A9B 24GB and Nemotron 3.5 Bolt E4B 4GB) for running coding, research, and conversational workloads locally. \n\n The Bolt models, Nvidia says , are meant to run “everyday agentic tasks on laptops,…"
tags: ["AI", "AI Agents", "AI Models"]
orgs: ["Nvidia", "Alibaba", "DeepSeek", "Hugging Face", "Thinking Machines"]
topics: ["models & research", "chips & infrastructure", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 847
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia squeezed a 74B agent model into 24GB so it can run on your laptop

The New Stack · Frederic Lardinois · 2026-10-15

Nvidia squeezed a 74B agent model into 24GB so it can run on your laptop
Nvidia on Thursday announced a few new additions to its Nemotron family: Nemotron 3.5 Super VL, a 120B vision-language model for enterprise agents and two small Bolt models (Nemotron 3.5 Bolt 74B-A9B 24GB and Nemotron 3.5 Bolt E4B 4GB) for running coding, research, and conversational workloads locally.
The Bolt models, Nvidia says, are meant to run “everyday agentic tasks on laptops, balancing speed and intelligence needed to handle multistep reasoning, tool calling, and web browsing.”
And while they come in very different sizes and are meant for different use cases, the focus for all three is on speed and efficiency.
The two larger models are available today, while the smaller Bolt E4B 4G model will launch in the near future.
Nemotron 3.5 Super VL
The marquee release here is Nemotron 3.5 Super VL, a 120-billion-parameter model that combines reasoning and tool use with image and document understanding.
In the announcement, Kari Briski, Nvidia’s VP for open models and software, notes that the large model is meant to deliver “leading accuracy on multimodal agentic tasks — instruction following, tool use, multistep business workflows, and visual understanding — comparable with NVIDIA’s largest reasoning model at roughly one-fifth the parameter count.”
Super VL builds on Nemotron 3 Super, which launched in March. Both have 120 billion total parameters, with 12 billion active during inference, and context windows of up to 1 million tokens. But while the earlier model only accepted text, Super VL now adds support for image and video input (though not output).
Mixed results against Qwen
But when it comes to the benchmarks, though, especially when compared to other open models of comparable size, the results are mixed.
In Nvidia’s own evaluations, Super VL outperforms Alibaba’s Qwen3.5-122B-A10B on scientific reasoning and terminal tasks, while scoring slightly lower on SWE-bench Verified and document understanding.
The five tests are GPQA-Diamond, Terminal-Bench 2.1, SWE-bench Verified, IFBench, and MMLongBench-Doc. Super VL scores 66.7 on Terminal-Bench, compared with Qwen3.5’s 48.7, but trails it on SWE-bench Verified, 71.1 to 71.9.
Qwen has 122 billion total parameters and 10 billion active, compared with Super VL’s 120 billion and 12 billion. The newer Qwen3.8-Flash-Next scores higher on all five tests, though its additional embedding and prediction components bring its total parameter count to about 180 billion.
Thinking Machines’ Inkling-Small has 276 billion total parameters and 12 billion active. It also trails Super VL on terminal tasks but scores higher on instruction following.
Nvidia also reports Super VL ahead of Ultra on Hermes Bench and LangChain behavioral evaluations, scoring 63.44% versus 56.33% and 87.05% versus 84.3%, respectively.
Overall, though, the focus here was clearly on speed.
Nvidia reports fourfold faster completion of 10,000 SWE-bench Pro tasks on four B200 GPUs, though its chart shows lower accuracy than Qwen3.8-Flash-Next and DeepSeek V4 Flash.
Hybrid Mamba architecture, faster decoding
As for how Nvidia built the model, it’s worth noting that the Nemotron coalition is sticking to the 3.5 family’s hybrid architecture, which combines Mamba-2, attention, and mixture-of-experts layers — but with the addition of a vision encoder. Nvidia also continued training the language model using distillation from Nemotron 3 Ultra before further training for software engineering, vision, and agent tasks, according to its model card.
To speed up text generation, Nvidia also uses LiLiCorr, a technique for speculative decoding. With this, a smaller helper model drafts several tokens ahead, which Super VL checks together instead of generating each token individually. Nvidia says this speeds up token generation on DGX Spark by up to 2.3 times compared with decoding without speculation.
For document workflows, Nvidia says Super VL focuses on optical character recognition, tables, charts, and structured information.
On CharXiv, a chart-reasoning benchmark, Nvidia reports 80.8% accuracy, compared with Nano Omni’s 63%. Python code interpretation raises Super VL’s result to 84%.
Bolt runs 74B in 24GB
If you’re interested in running local models, the new Bolt models may be the most interesting release here — and their benchmarks tend to outperform most comparable models.
Nemotron 3.5 Bolt 74B-A9B 24GB is derived from Super VL. Its hybrid mixture-of-experts architecture activates 9 billion of its 74 billion parameters at a time.
In Nvidia’s tests, Bolt scores 51.0 on Terminal-Bench 2.1, versus 44.4 for Qwen3.6-35B-A3B and 37.2 for Gemma4 26B-A4B, both tested in BF16. Bolt uses mixed precision, including two-bit experts.
To get to this size, Nvidia used two-bit quantization to reduce the 74B model’s memory footprint to 24GB. The company says it is optimizing the model for RTX Spark and DGX Spark systems, with support for llama.cpp, Ollama, LM Studio, and vLLM.
A second, even smaller version of this model, Nemotron 3.5 Bolt E4B 4GB, is scheduled for later this month. With this one, Nvidia is targeting conversational and physical agents on GeForce RTX, Jetson, and Spark hardware, including device assistants and interactive characters that need multiturn tool use and awareness of application state.
Availability
The new models are now available for download on Hugging Face under the OpenMDW 1.1 license, which permits commercial use and modification.
