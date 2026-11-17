---
id: "2f70d719d6bb479e"
title: "Intel Shares First Benchmarks of Its Next-Gen Crescent Island \"D270\" GPU, Claiming a 5.9x Throughput Over RTX PRO 6000 As Xe3P Goes Big On FP64"
url: "https://wccftech.com/intel-first-benchmarks-crescent-island-d270-xe3p-gpu-a-5-9x-faster-rtx-pro-6000-fp64"
link: "https://wccftech.com/intel-first-benchmarks-crescent-island-d270-xe3p-gpu-a-5-9x-faster-rtx-pro-6000-fp64"
source: "Wccftech"
domain: "wccftech.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T12:02:09Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["pulse77"]
language: "en"
summary: "The title talks about FP64. For local inference this info from the content is relevant: \"In AI benchmarks, Intel's D270 GPU offered 29% lower latency and 1.12x throughput versus the RTX PRO 6000 Blackwell.\" Maybe we are getting a good RTX PRO 6000 alternative..."
tags: ["r/LocalLLaMA"]
orgs: ["Intel", "Nvidia", "Google", "Alibaba"]
topics: ["chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 630
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyioi8/intel_shares_first_benchmarks_of_its_nextgen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Intel Shares First Benchmarks of Its Next-Gen Crescent Island "D270" GPU, Claiming a 5.9x Throughput Over RTX PRO 6000 As Xe3P Goes Big On FP64

Wccftech · pulse77 · 2026-11-17

Intel's D270 "Crescent Island" GPUs gets its first performance benchmarks, claiming big HPC & AI uplifts with its native FP64 compute.
Intel Crescent Island "D270" GPU With Xe3P Architecture Offers Up To Full-Rate FP64 "Double Precision" Compute, Primed for HPC Workloads
As we approach the launch of Intel's D270 GPU, codenamed Crescent Island, the Xe3P-powered solution is gearing up as an impressive competitor to existing HPC and AI options, as it has a few tricks up its sleeve to give it an edge.
Previously, Intel has disclosed the full specs of the D270 "Crescent Island" GPU, which packs 32 Xe3P cores, up to 480 GB of memory, an LPDDR5X subsystem for cost-effective AI/HPC options, and availability in a diverse range of solutions that range from air-cooled 350W parts to liquid-cooled and dual-GPU options.
Scientific, engineering, and financial simulations depend on double-precision arithmetic to preserve numerical fidelity and avoid compounding rounding errors. Built on Intel’s Xe 3P architecture, the Intel GPU D270 features 32 Xe cores and 256 Xe Matrix Extensions (XMX) engines, delivering 64 FP64 fused multiply-add (FMA) operations per core. This architecture offers developers precision optionality: lower precision (FP4 to FP8) for inference throughput alongside full-rate, native FP64 compute where mathematical accuracy is non-negotiable.
Today at SC26, Intel is sharing the performance results of its D270 GPU in HPC workloads that require native FP64 compute capabilities and lots of memory. With Crescent Island, Intel brings native FP64 compute or double-precision compute in addition to FP4-FP8 lower precision ops.
This means that Intel will have an edge over NVIDIA's recent Blackwell RTX PRO parts, which do not have as much FP64 compute in hand. So, keeping that in mind, Intel is comparing the D270 "Crescent Island" GPU against NVIDIA's flagship RTX PRO 6000 Blackwell Server Edition card, and the results are quite impressive. For starters, Intel's solution is a 350W part, while NVIDIA's RTX PRO operates at 600W.
In test results across four different Financial Services workloads, the D270 GPU secured up to a 5.9x lead over the RTX PRO 6000 Blackwell, and an average of 4.5x. In addition to the FP64 tests, Intel is also showcasing a Seismic modeling demo at SC26 that makes use of FP32 compute, showcasing strong gains here too.
Seismic modeling is one of the Oil and Gas industry’s most demanding workloads, requiring repeated acoustic wave-propagation calculations across massive 3D datasets utilizing FP32 compute. The combination of high memory capacity coupled this time with the FP32 compute in D270 shows strong capabilities for this workload. Cache-aware stencil optimizations maximize data reuse across local caches, keeping large wavefield arrays resident directly on the card. Intel is demonstrating Seismic modeling capabilities via a live demo at Supercomputing ‘26 in our booth.
In AI benchmarks, Intel's D270 GPU offered 29% lower latency and 1.12x throughput versus the RTX PRO 6000 Blackwell.
In the emerging, decision-making class of models, where the models make decisions rather than just generating answers, Intel GPU D270 delivers up to 29% lower latency than the NVIDIA RTX PRO 6000 Blackwell server edition running Drex 2.0. When it comes to LLM throughput also, D270 delivers 1.12x the throughput performance on Qwen 3 30B – A3B when compared to the same competitor GPU but at only 350W of power. These two results, achieved on pre-production silicon, already demonstrate strong agentic readiness for Intel GPU D270.
Now the main question remains: when is the GPU launching, and at what price range?
Considering Intel used LPDDR5X, they may have an advantage over standard GDDR & premium HBM options in terms of value, efficiency, and scalability. So overall, it looks like Crescent Island may turn out to be a strong AI, HPC, and Workstation offering.
Follow Wccftech on Google to get more of our news coverage in your feeds.
