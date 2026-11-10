---
id: "83de1ce33235c06a"
title: "Google claims its new AI software cuts inference latency by over 90% — but there’s a catch"
url: "https://thenewstack.io/google-tpu-sync-inference"
link: "https://thenewstack.io/google-tpu-sync-inference"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T18:40:01Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google’s eighth-generation TPU announcement on Monday included more than new chips, introducing TPU Sync , an open-source system designed to speed up AI inference by tackling a problem that worsens as context windows grow: moving data between different types of memory. \n\n The software is made for developers running large models, particularly ones handling million-token contexts and…"
tags: ["AI", "AI Infrastructure", "Hardware", "Open Source"]
orgs: ["Google", "Nvidia"]
topics: ["chips & infrastructure", "agents & coding", "models & research", "business & funding"]
content_source: "summary"
word_count: 587
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google claims its new AI software cuts inference latency by over 90% — but there’s a catch

The New Stack · Amanda Caswell · 2026-11-09

Google’s eighth-generation TPU announcement on Monday included more than new chips, introducing TPU Sync , an open-source system designed to speed up AI inference by tackling a problem that worsens as context windows grow: moving data between different types of memory. 

 The software is made for developers running large models, particularly ones handling million-token contexts and reinforcement-learning workloads. The company claims it can cut KV-cache transfer latency and time to first token by more than 90% in some tests. 

 The company claims it can cut KV-cache transfer latency and time to first token by more than 90% in some tests. 

 Inside the memory hierarchy 

 Written in C++, the framework moves data between accelerator memory, host DRAM, storage, and the network. It uses zero-copy transfers and native PjRtBuffer hardware descriptors to avoid unnecessary copies. 

 Combined host-to-device and device-to-host throughput reached 223 GB/s per Ironwood TPU host, approaching the theoretical 256 GB/s PCIe Gen5 limit. 

 Google’s numbers, with caveats 

 In Google’s benchmarks , moving KV caches for the 235-billion-parameter Qwen3 model went from taking several seconds to about 230 milliseconds. That cut the average time to first token (TTFT) by 60% when relatively few requests were running at once. With a larger 480-billion-parameter model, the reduction reached 90%. 

 Google saw similar gains when testing prefix caching with 64,000-token contexts. TTFT dropped by as much as 90%, throughput increased by more than 50%, and P99 inter-token latency fell 30%. Developers may see different results depending on what they’re running, how much cached data they can reuse, and how much network bandwidth they have available. 

 SemiAnalysis , offers some context for the gains. Its analysis suggests that external TPU serving previously lacked the infrastructure needed to separate prefill and decode workloads effectively. 

 Where Nvidia still leads 

 Nvidia may still have an advantage in some workloads. SemiAnalysis’s InferenceX data shows its GB200 and GB300 NVL72 systems ahead in parts of the disaggregated-serving performance curve, although a direct comparison with a fully tuned TPU v7 setup has yet to be published. 

 Chipping away at the CUDA moat 

 Developers can use the new software with the inference tools they already have since the company released the project alongside TorchTPU , with support for vLLM and SGLang , two widely used open-source inference engines. Developers already using those frameworks can run disaggregated workloads on TPUs without rebuilding their serving stack from scratch. 

 Developers already using those frameworks can run disaggregated workloads on TPUs without rebuilding their serving stack from scratch. 

 This also fits with Google’s broader effort to make its custom chips more competitive. The company has emphasized reducing inference costs through hardware changes, including reportedly designing chips around Gemini’s architecture . 

 Now it’s addressing the software problems that can leave those chips waiting for data. Making TPU infrastructure easier to use with familiar frameworks could give developers another reason to consider Google’s hardware instead of defaulting to Nvidia and CUDA; whether it can match Nvidia’s inference performance remains an open question. 

 Not production-ready yet 

 The software isn’t production-ready for everyone just yet. Google warns in its GitHub repository that the APIs are still changing and recommends sticking to a verified commit or tagged release. Support is also limited to Cloud TPU v7x and v6e, with specific JAX and PyTorch version requirements. 

 Support is also limited to Cloud TPU v7x and v6e, with specific JAX and PyTorch version requirements. 
 
 The post Google claims its new AI software cuts inference latency by over 90% — but there’s a catch appeared first on The New Stack .
