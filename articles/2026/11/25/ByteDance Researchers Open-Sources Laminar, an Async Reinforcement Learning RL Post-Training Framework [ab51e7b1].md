---
id: "ab51e7b113eeddd0"
title: "ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning RL Post-Training Framework"
url: "https://marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework"
link: "https://marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-25T05:42:05Z"
published_date: "2026-11-25"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Researchers from The University of Hong Kong and ByteDance Seed have open-sourced Laminar . Laminar is an reinforcement learning RL post-training framework for LLMs and long-horizon agents. The core idea is simple: stop forcing every trajectory and every GPU to wait for the slowest one. For teams training coding agents with long, skewed rollouts, that is where most GPU time goes. \n\n TL;DR \n\n…"
tags: ["AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "New Releases", "Open Source", "Reinforcement Learning", "Staff", "Tech News", "Technology"]
orgs: ["ByteDance", "Nvidia", "Hugging Face"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "summary"
word_count: 883
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning RL Post-Training Framework

MarkTechPost · Asif Razzaq · 2026-11-25

Researchers from The University of Hong Kong and ByteDance Seed have open-sourced Laminar . Laminar is an reinforcement learning RL post-training framework for LLMs and long-horizon agents. The core idea is simple: stop forcing every trajectory and every GPU to wait for the slowest one. For teams training coding agents with long, skewed rollouts, that is where most GPU time goes. 

 TL;DR 

 What: A framework. Tested on Qwen3-Coder-30B-A3B-Instruct (30.5B total, 3.3B active) and Qwen2.5 at 7B, 32B and 72B. 

 Runs on: Multi-node NVIDIA GPU clusters with Ray and CUDA. Tested on 64x H800 and up to 1024 H800 GPUs. vLLM for inference, Megatron-LM or FSDP2 for training. 

 Performance: Strong end-to-end gains on SWE agent RL and up to 5.48x throughput in the paper. 

 Best: 52.2% on SWE-bench Verified, up from 46.6% for the base model. 

 Worst: Early repo (1 commit at launch), vLLM is the only listed inference backend, and per-step async checkpointing is still in progress. 

 Bottom line: Best: fewer samples and GPU-hours to a higher SWE-bench score. Worst: the headline comparison mixes H800 and H100 hardware. 

 What is Laminar? 

 Laminar is an asynchronous RL post-training framework that decouples rollout, buffering, training and weight transfer into independent loops. It is built on verl and Uni-Agent and released under Apache-2.0. 

 The launch blog splits the stack into 3 layers. verl provides training and inference compute backends. Uni-Agent handles agent execution, tool calls and sandboxes. Laminar handles cluster-scale orchestration. 

 How does Laminar’s architecture work? 

 The design rests on 3 principles: full decoupling, fine-grained asynchrony and fault tolerance. 

 Rollout loop: Drives agent interactions and serves generation across inference replicas. 

 Experience buffer (data plane): Separates trajectory production from training and serves ready batches on demand. 

 Training loop: Samples batches, computes advantages and off-policy corrections, and publishes weights. 

 Weight Relay (weight plane): The trainer stages weights into per-node shared CPU memory and keeps going. Replicas pull updates on their own schedule. 

 In the research paper , relays are CPU processes, 1 per rollout machine. They broadcast weights along a pipelined RDMA chain. A 72B model reaches 127 other relays in under 1.6 seconds. 

 What is version-consistent rollout? 

 Most async systems use version-mixed partial rollout. They interrupt in-flight trajectories at each weight update and resume under the new policy. That forces repeated re-prefill. 

 Laminar also supports a version-consistent mode. Each trajectory finishes under 1 policy version. Replicas update independently, without a global weight-switch barrier. The blog states that this keeps the prefix KV cache intact. It argues re-prefill cost scales cubically with sequence length under frequent updates. 

 Repack handles the tail. Once new weights exist, leftover old-version trajectories are consolidated onto fewer replicas. Drained replicas then load the new version immediately. 

&&

 How does Laminar perform on SWE-bench Verified? 

 The research team trained Qwen3-Coder-30B-A3B-Instruct on SWE-rebench. They evaluated on all 500 SWE-bench Verified tasks with greedy decoding. 

 Base model: 46.6% (233/500). 

 Baseline peak (step 150, 64x H100): 51.4% with 76.4k samples and 5,085 GPU-hours. 

 Laminar match (step 320, 64x H800): 51.4% with 41.0k samples (46% fewer) and 1,450 GPU-hours (71% fewer). 

 Laminar peak (step 400, 64x H800): 52.2% with 51.2k samples (33% fewer) and 1,843 GPU-hours (64% fewer). 

 How does Laminar handle failures? 

 Faults stay local. If a rollout replica fails, the router fences only that replica. It restarts, reloads weights from the local relay and resumes from its generated token prefix. A replica that fails during weight loading recovers without blocking the trainer. Trainer checkpoints align model state, prompt cursors and published weight versions. 

 laminar.eval also evaluates several checkpoints at once across resident replicas, in batch or streaming mode during training. 

 Laminar vs verl vs AReaL vs slime 

 Feature Laminar verl AReaL slime Developer HKU + ByteDance Seed ByteDance Seed, verl community Tsinghua IIIS + Ant Group THUDM License Apache-2.0 Apache-2.0 Apache-2.0 Apache-2.0 Async mode Trajectory-level, no global barrier Sync default; fully async and 1-step off-policy (experimental) Fully asynchronous Async rollout, fully async example Version-consistent rollout Yes, plus version-mixed partial Not disclosed Not disclosed Not disclosed Inference backend vLLM vLLM, SGLang, HF vLLM, SGLang SGLang Training backend Megatron-LM, FSDP2 FSDP, FSDP2, Megatron-LM Megatron, FSDP, Archon Megatron Agentic RL Via Uni-Agent Multi-turn tool calling Yes (coding, search, Tau2) Yes (coding, search, multi-agent) Fault tolerance Replica, weight sync and trainer level Not disclosed Not disclosed Documented Key result 52.2% SWE-bench Verified Not disclosed Not disclosed Not disclosed 

 Key Takeaways 

 Laminar decouples rollout, training and weight sync into independent loops. 

 Version-consistent rollout avoids re-prefill by finishing each trajectory on 1 policy. 

 Qwen3-Coder-30B-A3B rose from 46.6% to 52.2% on SWE-bench Verified. 

 It used 33% fewer samples and 64% fewer GPU-hours, on different GPUs than the baseline. 

 The code is Apache-2.0 but early, with vLLM-only inference. 

 Check out the Paper , arXiv preprint , GitHub Repo and Technical Blog . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning RL Post-Training Framework appeared first on MarkTechPost .
