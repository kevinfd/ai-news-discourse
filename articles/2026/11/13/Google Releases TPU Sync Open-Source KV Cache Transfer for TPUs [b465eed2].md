---
id: "b465eed2f9de498a"
title: "Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs"
url: "https://marktechpost.com/2026/11/13/google-tpu-sync-kv-cache-transfer-library"
link: "https://marktechpost.com/2026/11/13/google-tpu-sync-kv-cache-transfer-library"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-13T10:32:26Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google Cloud has released TPU Sync , an open-source C++ library for moving KV caches and model weights on Cloud TPUs. The Google TPU Sync KV cache transfer library treats TPU HBM, host DRAM, shared storage and the data center network as one memory hierarchy. It targets a growing bottleneck: moving model state, not computing it. Google reports over 90% lower KV transfer latency on 235B to 480B…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Machine Learning", "Open Source", "Software Engineering"]
orgs: ["Google", "Nvidia", "Meta"]
topics: ["chips & infrastructure", "models & research", "products & launches"]
content_source: "summary"
word_count: 988
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs

MarkTechPost · Michal Sutter · 2026-11-13

Google Cloud has released TPU Sync , an open-source C++ library for moving KV caches and model weights on Cloud TPUs. The Google TPU Sync KV cache transfer library treats TPU HBM, host DRAM, shared storage and the data center network as one memory hierarchy. It targets a growing bottleneck: moving model state, not computing it. Google reports over 90% lower KV transfer latency on 235B to 480B parameter MoE models. 

 TL;DR 

 Library: Native C++ core with Python wheels for PyTorch and JAX. Tested on 235B to 480B MoE models. 

 Runs on: Cloud TPU v7x (Ironwood) and v6e per the README . Benchmarks used TPU v7x (2x2x1), PCIe Gen5 and 200 Gbps NICs. 

 Performance: Large cuts to KV transfer latency and time to first token (TTFT) in Google’s internal lab tests. 

 Best: Up to 90% lower average TTFT (480B P/D serving at low concurrency, and 64K-context prefix caching). 

 Worst: No RL numbers published. The README says it is not yet recommended for general use. 

 Bottom line: Best: Qwen3 235B KV transfer drops from several seconds to ~230 ms. Worst: every number is self-reported and early-stage. 

 What is TPU Sync? 

 TPU Sync is an open-source C++ library from Google that moves TPU-tiled tensors across memory tiers with asynchronous DMA. It handles 2 jobs: KV cache state during inference, and trainer-to-sampler weight broadcast in reinforcement learning (RL). The repository is licensed Apache-2.0. 

 How does TPU Sync work? 

 The library spans TPU HBM, pinned host DRAM, shared storage and multi-host DCN. Storage uses experimental POSIX backends, including local SSDs and Google Cloud Managed Lustre. Google lists 4 design choices: 

 Layout-preserving direct DMA: It reads JAX PJRT buffers or PyTorch tensors in place. Data keeps its native TPU tile layout, with no Python serialization or bounce buffers. 

 Compute-overlapped transfers: Raw PJRT buffer aliases let transfers run during computation. Built-in DMA pacing stops large copies from delaying kernel launches. 

 No XLA compilation in the data path: Transfers and resharding run in native C++ outside the XLA graph. 

 High-bandwidth PCIe and DCN: It reaches up to 223 GB/s per Ironwood host, against a 256 GB/s PCIe Gen5 ceiling. DCN streaming hits ~192 Gbps on 1 NIC, or ~350 Gbps across 2. 

 Above this sit a global KV store for prefix lookups, a transfer controller and a KV cache manager. 

 How does disaggregated prefill/decode serving use it? 

 The prefill node offloads KV blocks to pinned host RAM through async DMA. The controller streams them host-to-host to the assigned decode node. Arriving blocks move into decode-node HBM while decoding continues. 

&

 What do the TPU Sync benchmarks show? 

 Google ran internal tests in July 2026 on TPU v7x (2x2x1). The stack was tpu-inference v0.24.0, JAX 0.10.2 and libtpu 0.0.42.1. Google team states that real-world results will vary. 

 For P/D disaggregated serving: 

 KV transfer overhead fell by over 90%. Qwen3 235B median KV transfer latency dropped from several seconds to ~230 ms. 

 Average TTFT fell 60% for 235B and 90% for 480B at low concurrency. 

 Token output throughput rose 30% to 70% for 235B during traffic spikes. 

 For prefix caching: 

 Effective cache capacity grew by an order of magnitude when MoE weights fill most of HBM. 

 Average TTFT fell by up to 90% on 64K-context workloads. 

 Throughput rose over 50%, and P99 inter-token latency fell 30%. 

 Which frameworks does TPU Sync support? 

 TPU Sync integrates with PyTorch through TorchTPU and with JAX natively. In vLLM-TorchTPU , it is the TPU KV connector behind vLLM’s KVConnector interface. In SGLang-TorchTPU , it is the P/D transfer backend and hierarchical cache I/O backend. On GKE, llm-d 1.0 uses it for prefix-cache-affinity routing and experimental spill to Managed Lustre. Inferact and RadixArk co-engineered the vLLM and SGLang integrations. Google says Meta and Wayfair are evaluating the architecture. 

 How does TPU Sync compare with GPU-side alternatives? 

 Feature Google TPU Sync NVIDIA Dynamo KVBM + NIXL LMCache Mooncake Target hardware Cloud TPU v7x, v6e ( README ) NVIDIA CUDA GPUs; partial ROCm in NIXL ( NIXL ) CUDA and ROCm ( repo ) CUDA, HIP, Ascend, MUSA and more ( repo ) Memory tiers HBM, pinned host DRAM, POSIX storage (experimental), DCN GPU, CPU, local SSD, remote storage ( KVBM docs ) GPU, CPU DRAM, local disk, remote backends DRAM and SSD/NVMe (Mooncake Store) Network transport DCN, multi-NIC striping UCX, LIBFABRIC, GDS plugins NVLink, RDMA, TCP TCP, RDMA, EFA, NVMe-oF, NVLink, CXL Engine integrations vLLM-TorchTPU, SGLang-TorchTPU, llm-d, JAX vLLM, TensorRT-LLM, SGLang ( KVBM ) vLLM, NVIDIA Dynamo vLLM, SGLang License Apache-2.0 Apache 2.0 (some wheel modules NVIDIA proprietary) Apache 2.0 Apache-2.0 Core language C++ with Python bindings C++ with Python and Rust bindings Python package with C/C++ and Rust code Not disclosed Headline bandwidth Up to 223 GB/s per v7x host (PCIe D2H/H2D) Not disclosed Not disclosed Up to 190 GB/s on 8×400 Gbps RoCE (network) RL weight transfer Yes (experimental) Not disclosed Not disclosed Yes, via SGLang (RDMA) 

 The bandwidth figures measure different paths. TPU Sync’s number is host PCIe DMA. Mooncake’s number is network transfer over RoCE. 

 Key Takeaways 

 TPU Sync is Google’s Apache-2.0 C++ library for KV cache and weight movement on TPUs. 

 It reaches up to 223 GB/s per Ironwood host through direct, layout-preserving DMA. 

 Qwen3 235B KV transfer fell from several seconds to ~230 ms in Google’s tests. 

 It plugs into vLLM-TorchTPU, SGLang-TorchTPU and llm-d on GKE. 

 RL and storage tiering are experimental, and every number is self-reported. 

 Check out the technical blog , the GitHub repo , vLLM-TorchTPU and SGLang-TorchTPU . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs appeared first on MarkTechPost .
