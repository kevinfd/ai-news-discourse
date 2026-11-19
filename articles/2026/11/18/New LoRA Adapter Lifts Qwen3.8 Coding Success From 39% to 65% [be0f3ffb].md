---
id: "be0f3ffb9c3f4e85"
title: "New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%"
url: "https://marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora"
link: "https://marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T16:07:50Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Hugging Face’s harness-hub team has released Qwen3.8-27B-pi-adapted , a LoRA adapter for Qwen3.8-27B . It was trained with reinforcement learning to work inside the pi coding agent . The Qwen3.8-27B-pi-adapted LoRA adapter targets one harness instead of general chat. For developers running local coding agents, that is the point. You keep the open base model and swap in a small, harness-specific…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Hugging Face", "Meta", "Nvidia", "Alibaba"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 889
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%

MarkTechPost · Asif Razzaq · 2026-11-18

Hugging Face’s harness-hub team has released Qwen3.8-27B-pi-adapted , a LoRA adapter for Qwen3.8-27B . It was trained with reinforcement learning to work inside the pi coding agent . The Qwen3.8-27B-pi-adapted LoRA adapter targets one harness instead of general chat. For developers running local coding agents, that is the point. You keep the open base model and swap in a small, harness-specific adapter. 

 TL;DR 

 Size: LoRA rank 32 (alpha 64) on Qwen3.8-27B, a 27B dense hybrid with 262,144 native context. Merged BF16 checkpoint is about 54 GB. 

 Runs on: vLLM with LoRA enabled, or llama.cpp with a GGUF adapter on a Q8_0 base. Inference VRAM is not disclosed. Training used 2x NVIDIA B200. 

 Performance: Large pass@1 gains inside pi with thinking off, plus far shorter sessions. 

 Best: 64.7% on SWE-bench Pro (hard 51), up from 39.2%. 

 Worst: 55.8% on Terminal-Bench 2.1. The base model with thinking already reaches 64.7% on SWE-bench Pro. 

 Bottom line: Best: thinking-level accuracy at about 4.5x fewer tokens. Worst: small eval sets, self-reported, pi only. 

 What is Qwen3.8-27B-pi-adapted? 

 Qwen3.8-27B-pi-adapted is a PEFT LoRA adapter that turns Qwen3.8-27B into a model tuned for pi. pi is an MIT-licensed agent toolkit with a coding agent CLI. The adapter is released under Apache-2.0 . It applies to the q, k, v, o, gate, up and down projections. It only works on Qwen3.8-27B. 

 The base model is a dense hybrid . It alternates Gated DeltaNet linear-attention blocks with Gated Attention blocks across 64 layers. 

 How does the harness adapter training work? 

 The method comes from Hugging Face’s harness adapters post from November 6. The idea is 1 LoRA adapter per model and harness. Training runs inside the unmodified harness on verifiable tasks. 

 For this checkpoint, the model card lists these details: 

 Algorithm: AsyncGRPO from TRL , 8 rollouts per task at temperature 0.8. 

 Tasks: 750 scale800 tasks interleaved with 300 TermGrade tasks. 

 Reward: verifier correctness plus a tool-efficiency bonus with weight 0.1. 

 Budget: up to 50 agent steps and 1,800 seconds per rollout, thinking off. 

 Checkpoint: step 160. The run stopped at step 191 of 1,000 planned. 

 Every tool call passes through safeagents , a rule-based proxy. It blocks calls such as fetching benchmark answers from the Hub. Blocked rollouts score 0, so RL pushes the model away from reward hacking. 

 Benchmarks: how much does the LoRA adapter help? 

 All numbers below are self-reported. They use the pi harness, 1 attempt per task. 

 Benchmark (pi, thinking off) Base Qwen3.8-27B pi-adapted Change SWE-bench Pro (hard 51) 39.2% 64.7% +25.5 ± 14.2 pts (p = 0.0023) Terminal-Bench 2.1 (86 tasks) 39.5% 55.8% +16.3 ± 9.1 pts (p = 0.0013) 

 The adapter solved 15 new SWE-bench Pro tasks and lost 2. On Terminal-Bench 2.1, it gained 16 and lost 2. 

 Efficiency is the larger story. On tasks both models solved, median turns fell from 59 to 23 on SWE-bench Pro. On Terminal-Bench 2.1, they fell from 18 to 8. The adapter also generates about 4.5x fewer tokens than the base model with thinking. 

&&

 How does it compare with thinking mode and other adapters? 

 With thinking on, the base model already scores 64.7% on SWE-bench Pro and 54.2% on Terminal-Bench 2.1. So the adapter matches thinking-level accuracy without paying for long reasoning traces. With thinking on, the adapter reaches 66.7% and 56.6%. 

 Feature Qwen3.8-27B-pi-adapted Qwen3.8-27B base, thinking on Qwen3.8-27B-opencode-adapted bytkim/Qwen3.8-27B-pi Type LoRA r=32 Base model LoRA r=32 Full fine-tune, 28B Method AsyncGRPO RL None AsyncGRPO RL SFT then GRPO Harness pi pi OpenCode pi License Apache-2.0 Apache-2.0 Apache-2.0 Apache-2.0 SWE-bench Pro (hard 51) 64.7% 64.7% 51.0% (OpenCode) Not disclosed Terminal-Bench 2.1 55.8% 54.2% 53.0% (OpenCode) Not disclosed Token use ~4.5x fewer than base + thinking Baseline ~6x to 8x fewer than base + thinking ~41% fewer output tokens (Terminal-Bench) Training hardware 2x B200 Not disclosed 2x B200 Not disclosed 

 OpenCode adapter numbers use a different harness and are not directly comparable. 

 How do you deploy it? 

 The model card gives 4 routes: 

 vLLM: serve Qwen/Qwen3.8-27B with --enable-lora --max-lora-rank 32 , thinking disabled. Point pi at http://localhost:8000/v1 . 

 llama.cpp: load the GGUF adapter on a Q8_0 base GGUF. 

 Llama.app on macOS: register the adapter with a 32,768-token context. 

 Merge: merge with PEFT on CPU, then serve the 54 GB BF16 result without LoRA flags. 

 Because adapters share 1 base model, a single server can host pi and OpenCode adapters side by side. 

 Key Takeaways 

 Qwen3.8-27B-pi-adapted is an Apache-2.0, rank-32 RL LoRA for the pi agent. 

 SWE-bench Pro hard-51 rises from 39.2% to 64.7%, thinking off. 

 Median turns drop from 59 to 23 on SWE-bench Pro. 

 It matches base-with-thinking accuracy at about 4.5x fewer tokens. 

 Results are self-reported on small sets; the tweet’s 29.4% baseline was corrected. 

 Check out the model card , GGUF adapter , methodology post and TRL training script . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65% appeared first on MarkTechPost .
