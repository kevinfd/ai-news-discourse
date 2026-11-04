---
id: "562ecff496b6a0a2"
title: "Anthropic Releases FlashProve: Cryptographic Proofs That a Reply Came From Committed Weights"
url: "https://marktechpost.com/2026/11/03/anthropic-flashprove-provable-inference-zksnark"
link: "https://marktechpost.com/2026/11/03/anthropic-flashprove-provable-inference-zksnark"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T22:08:22Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Anthropic’s Frontier Red Team has released FlashProve , an open-source research prototype for provable inference . FlashProve is a zkSNARK system from Anthropic that proves a reply came from a committed model. The proof reveals nothing about the model weights. On Llama 4 Maverick , a 400B mixture-of-experts model, it proves about 110 tokens/second on 1 H100. For developers, this targets a real…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "New Releases", "Open Source"]
orgs: ["Anthropic", "Meta", "OpenAI", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 848
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic Releases FlashProve: Cryptographic Proofs That a Reply Came From Committed Weights

MarkTechPost · Asif Razzaq · 2026-11-03

Anthropic’s Frontier Red Team has released FlashProve , an open-source research prototype for provable inference . FlashProve is a zkSNARK system from Anthropic that proves a reply came from a committed model. The proof reveals nothing about the model weights. On Llama 4 Maverick , a 400B mixture-of-experts model, it proves about 110 tokens/second on 1 H100. For developers, this targets a real gap: today you cannot check which model actually answered your API call. 

 TL;DR 

 Size: Proves a 400B MoE model (~17B active per token); context capped at 1,024 tokens per request. 

 Runs on: Prover needs 1 H100 80 GB, 24 CPU cores and ~290 GB host RAM. Verifier runs on a CPU, no GPU. 

 Performance: Orders of magnitude faster than prior open-source zkML systems on the same 400B model. 

 Best: 110 tokens/second proving on 1 H100, with 18.78 MB proofs checked in 17 seconds. 

 Worst: Proving costs ~70 to 95x the GPU time of plain vLLM inference. 

 What problem does provable inference solve? 

 A user querying a model cannot verify which model produced the response. A routing service could swap in a cheaper model . An attacker could tamper with the token stream. Judging from output quality alone is unreliable. 

 Anthropic lists 4 use cases: 

 Regulators could confirm hardware serves inference, supporting AI pacing rules. 

 Labs could detect tampered inference servers. 

 Users could verify text provenance. 

 Regulators could enforce serving of approved models only. 

 How does FlashProve work? 

 FlashProve has a prover (the model provider) and a verifier (the user). It runs in 2 phases: 

 Offline: The provider publishes a commitment, a short fingerprint binding one exact set of weights. This takes about 39 minutes and covers about 16 million requests. 

 Online: For each request, the GPU produces a proof that the committed model produced those tokens. 

 The proof system compiles an interactive oracle proof into a cryptographic proof using hash functions. Anthropic says this offers post-quantum security. It is the same family used by validity-proof L2 networks such as Starknet. 

 Three engineering choices drive the speed. Prover work scales with the ~17B active parameters, not all 400B. Requests are proved in batches after the fact, like prefill. Weights stream from host memory, so a single 80 GB GPU suffices. 

 How fast is it? Benchmarks 

 Anthropic measured the public 4-bit Maverick weights on 1 H100 with 24 CPU cores. Per the repo performance guide : 

 Batch of 24: 111.23 tokens/second, ~221 to 226 seconds per batch. 

 Batch of 1: 17.41 tokens/second. Batch of 64: 123.31 tokens/second, flagged as unreliable on 80 GB cards. 

 Proof size: 18.78 MB. Client downloads ~6.5 MB once per commitment. 

 Verification: 17 seconds on 24 threads, 21 seconds on 1 thread. 

 Against vLLM running FP8 Maverick on 8 H100s, proving costs about 72x the GPU time per batch. At vLLM’s highest tested load, the gap is about 94x. 

&

 How does FlashProve compare with other zkML systems? 

 Metrics FlashProve Attestable VerInf DeepProve zkLLM Model proven Llama 4 Maverick (400B MoE) Gemma 4 31B (dense) Llama 4 Maverick (400B MoE) GPT-2, Gemma 3 LLaMA-2-13B Throughput ~110 tok/s 53 to 77 tok/s ~0.02 tok/s (1,000 tokens in 14.3 h) ~2.9 tok/s (GPT-2), ~1.4 tok/s (Gemma 3) Full inference in under 15 min Hardware 1 H100 + 24 CPU cores 1 H100 1 DGX Spark 1 machine; 31 tok/s distributed GPU (CUDA) Proof size 18.78 MB 4.35 to 7.92 MiB 93.6 GB Not disclosed Under 200 kB Verify time 17 s (24 threads) 157 to 648 ms 17.7 h (20 cores) 1 to 3.7 s Not disclosed Context 1,024 tokens Up to 16K tokens 1,000 tokens Not disclosed Not disclosed Code / license Open, Apache 2.0 Not open source Open, MIT Open source per Lagrange Paper (CCS 2024) 

 How is the security checked? 

 Cryptographic code is brittle, so Anthropic formalized the protocol in Lean. It proves completeness, soundness and zero knowledge. The README states a cheating provider is caught except with probability about q/2^124 + 2^-101. 

 FlashProve ships 2 verifiers. A fast C++ verifier is for daily use but carries no formal guarantee. A slower Lean verifier is proven to accept only what the soundness theorem accepts. Anthropic team notes Claude helped optimize the system. 

 Key Takeaways 

 FlashProve proves a 400B MoE model at ~110 tokens/second on 1 H100. 

 Proofs are 18.78 MB and verify on a CPU in 17 seconds. 

 Proving costs ~70 to 95x the GPU time of vLLM inference. 

 Security properties are formalized in Lean; weights stay hidden. 

 Limited to 1,024 tokens, greedy decoding, and MoE models for now. 

 Check out the research post , technical report , protocol specification and GitHub repo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Anthropic Releases FlashProve: Cryptographic Proofs That a Reply Came From Committed Weights appeared first on MarkTechPost .
