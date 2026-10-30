---
id: "6ebaa851c1e82228"
title: "TKintegers K5: 3.21× prefill and 3.10× decode throughput vs TorchAO FP8 on NVIDIA L4 [R] [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xir3oa/tkintegers_k5_321_prefill_and_310_decode"
link: "https://reddit.com/r/MachineLearning/comments/1xir3oa/tkintegers_k5_321_prefill_and_310_decode"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T17:53:52Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Code_MasterCody"]
language: "en"
summary: "I built TKintegers, a balanced-ternary weight representation, converter, and GPU inference implementation. The result that stood out to me: the NVIDIA L4 has native FP8 tensor-core support, but my K5 implementation achieved higher throughput than the TorchAO FP8 baseline—even though the GPU has no native K5 instructions. On Qwen2.5-0.5B-Instruct, using a fixed matched workload: - Prefill: K5…"
tags: ["r/MachineLearning"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 240
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xir3oa/tkintegers_k5_321_prefill_and_310_decode/"
score: null
comments: null
community: "r/MachineLearning"
---

# TKintegers K5: 3.21× prefill and 3.10× decode throughput vs TorchAO FP8 on NVIDIA L4 [R] [P]

Reddit · Code_MasterCody · 2026-10-29

I built TKintegers, a balanced-ternary weight representation, converter, and GPU inference implementation. The result that stood out to me: the NVIDIA L4 has native FP8 tensor-core support, but my K5 implementation achieved higher throughput than the TorchAO FP8 baseline—even though the GPU has no native K5 instructions. On Qwen2.5-0.5B-Instruct, using a fixed matched workload: - Prefill: K5 achieved 3,402.85 tokens/s versus FP8’s 1,061.58 — 3.21× throughput. - Decode: K5 achieved 26.75 tokens/s versus FP8’s 8.63 — 3.10× throughput. The baseline was standard TorchAO dynamic E4M3 FP8, running in eager PyTorch. Decode measured fixed-token model forwards with a carried KV cache. What is K5? TK stands for Ternary Kluster. K5 represents each weight code with five balanced ternary digits, giving 243 possible values. In this layout, each code occupies one byte. Five trits does not mean five binary bits. My kernels expand bounded tiles for computation and use FP16 tensor-core operands with FP32 accumulation. Some tensors remain in higher precision. For me, this is why the runtime matters alongside the representation: K5 can outperform this FP8 baseline on existing hardware without requiring a processor built specifically for K5. These measurements apply to this model, workload, and implementation; they don’t establish a win over every FP8 runtime. The FP16 control was faster than both. The repository includes the converter, native kernels, benchmark scripts, and recorded evidence: https://github.com/CodeMasterCody3D/tkintegers https://youtu.be/JFDBuwMoL0s?is=ucya9errGEh4xJ2L I’d welcome technical feedback on the kernel design and benchmark methodology, especially independent replication.
