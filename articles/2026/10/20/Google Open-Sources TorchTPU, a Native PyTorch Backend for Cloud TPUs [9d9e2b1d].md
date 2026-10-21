---
id: "9d9e2b1d0a9197f3"
title: "Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs"
url: "https://marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu"
link: "https://marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T15:22:03Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google has open-sourced TorchTPU , a native PyTorch backend for Cloud TPUs. It was co-developed with the PyTorch team at Meta and announced at PyTorch Conference 2026 on October 20, 2026. Existing PyTorch code targets a TPU through a standard torch.device(\"tpu\") . TPUs now sit beside GPUs and CPUs as a native PyTorch device. Google team states that TorchTPU replaces PyTorch/XLA and recommends it…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Machine Learning", "New Releases", "Open Source", "Staff", "Tech News"]
orgs: ["Google", "Meta", "Alibaba", "Hugging Face", "Amazon"]
topics: ["chips & infrastructure", "models & research"]
content_source: "summary"
word_count: 889
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs

MarkTechPost · Asif Razzaq · 2026-10-20

Google has open-sourced TorchTPU , a native PyTorch backend for Cloud TPUs. It was co-developed with the PyTorch team at Meta and announced at PyTorch Conference 2026 on October 20, 2026. Existing PyTorch code targets a TPU through a standard torch.device("tpu") . TPUs now sit beside GPUs and CPUs as a native PyTorch device. Google team states that TorchTPU replaces PyTorch/XLA and recommends it for all new workloads. 

 TL;DR 

 Size: A software stack, not a model. 4 open repos: TorchTPU, vLLM-TorchTPU, SGLang-TorchTPU, TorchTitan. TorchTPU is v0.2.0 on PyPI , Python 3.11+, Apache 2.0. 

 Runs on: Google Cloud TPUs. Tested on generations from v5e , scaled to 8,192 Ironwood (TPU7x) chips. Serving supports FP8, MXFP4 and NVFP4 checkpoints. 

 Performance: Eager mode for debugging, torch.compile for production-level throughput. 

 Best: 52% MFU training Qwen 3 8B with TorchTitan on Ironwood (self-reported). 

 Worst: Out-of-box eager took 11.49s per step in a fine-tuning case, versus 2.78s fully tuned. 

 What is TorchTPU? 

 TorchTPU is an open-source PyTorch backend from Google and Meta that runs PyTorch models natively on TPUs. It plugs in through PyTorch’s PrivateUse1 interface . Tensors are ordinary PyTorch tensors, with no subclasses or wrappers. It runs one process per device and preserves tensor views and in-place mutations. 

 The predecessor, PyTorch/XLA, recorded lazy-tensor graphs. Developers often added code to mark compilable regions. PyTorch/XLA also only supported pure SPMD code . TorchTPU also handles divergent MPMD execution. 

 How does TorchTPU execute PyTorch code? 

 TorchTPU ships 3 eager modes : 

 Strict (default): dispatches each operator asynchronously with standard PyTorch semantics. 

 Debug: runs synchronously with tensor bounds checking. 

 DeferAndFuse: fuses runs of eager operators to cut HBM traffic. The TorchTPU paper says it can be 50% or more faster than Strict. 

 For peak speed, torch.compile(backend="tpu") captures the graph with TorchDynamo. It lowers through StableHLO to OpenXLA, which emits TPU machine code. Compiled executables are cached across processes, hosts and job restarts. 

 Custom Pallas kernels are callable as standard PyTorch functions. Prebuilt Tokamax kernels and Helion tile kernels also work. 

 Distribution uses the tpu_dist process group. It supports DDP, FSDP2 and DTensor, along with a topology-aware mesh for TPU interconnects. 

 How fast is TorchTPU? 

 All figures below are self-reported by Google and partners. 

 Training scale: TorchTitan reached up to 52% MFU on Qwen 3 8B . Google reports near-linear scaling up to 8,192 Ironwood TPUs. 

 Tuning ladder: In a TorchTitan fine-tuning case, step time fell from 11.49s to 2.78s. DeferAndFuse alone gave 1.15x. Full torch.compile gave 3.80x . 

 Model coverage: Google continuously tests about 5,000 Hugging Face models in eager and compiled modes. 

 Fleet serving: Zenteiq grew daily output from 1.47B to 5.97B tokens per 1,000 TPU v6e chips. That gain came from llm-d routing on GKE, not TorchTPU alone. 

&&

 What integrations ship with TorchTPU? 

 Hugging Face: Transformers v5 deploys to TPU with device_map="tpu" . Diffusers supports eager, torch.compile and tensor parallelism. 

 vLLM-TorchTPU : built with Inferact. Keeps upstream schedulers and API servers, with custom Pallas kernels. 

 SGLang-TorchTPU : built with RadixArk. Keeps RadixAttention prefix reuse. 

 Serving features: FP8 KV caches, FP8, MXFP4 and NVFP4 checkpoints. Speculative decoding includes MTP and EAGLE-3. 

 TorchTitan : recipes for Llama 3 70B/405B, Qwen 3 8B/32B, Qwen 3 235B MoE and FLUX.1 12B. 

 Also: llm-d 1.0, Ray, TorchRec, VeRL (preview) and LiteRT-Torch for on-device export. 

 How does TorchTPU compare with PyTorch/XLA, TorchNeuron and JAX? 

 Feature TorchTPU ( repo ) PyTorch/XLA ( repo ) TorchNeuron ( AWS docs ) JAX on TPU ( Google docs ) Vendor Google + Meta Google / PyTorch AWS Google Hardware Cloud TPU (v5e and later tested) Cloud TPU Trainium 2, Trainium 3 Cloud TPU PyTorch device tpu xla neuron Not PyTorch Backend mechanism PrivateUse1 Lazy-tensor graph recording PrivateUse1 Not applicable Default execution Eager (Strict, Debug, DeferAndFuse) Lazy tensors Eager plus torch.compile Not disclosed Compile path TorchDynamo to StableHLO to XLA XLA Neuron Compiler XLA Distributed APIs DDP, FSDP2, DTensor, SPMD and MPMD Pure SPMD only FSDP, DTensor, DDP, TP Not disclosed Custom kernels Pallas, Tokamax, Helion Not disclosed NKI Pallas vLLM / SGLang serving vLLM-TorchTPU, SGLang-TorchTPU Not disclosed vLLM Neuron vLLM-JAX, SGLang-JAX Status Open source, v0.2.0 Being replaced by TorchTPU Public beta (Neuron 2.33) Maintained License Apache 2.0 Not disclosed Not disclosed Not disclosed 

 How do you install TorchTPU? 

 Install the package on a TPU VM, then pick the tpu device: 

 Copy Code Copied Use a different Browser # pip install torch_tpu
import torch
device = torch.device("tpu")
x = torch.randn((4, 4), device=device) 

 The repo’s README pins torch_tpu==0.2.0 with the CPU PyTorch wheel index. Without it, pip pulls the CUDA build of torch . Full guides live at torchtpu.readthedocs.io . 

 Key Takeaways 

 TorchTPU is open source under Apache 2.0, co-built with Meta. 

 It replaces PyTorch/XLA with eager-first, PrivateUse1-based execution. 

 torch.compile(backend="tpu") lowers through StableHLO and XLA. 

 TorchTitan hit 52% MFU on Qwen 3 8B, scaling to 8,192 Ironwood chips. 

 vLLM, SGLang and Hugging Face now run on TPU through standard PyTorch. 

 Check out the GitHub repo , paper , docs and Google Cloud announcement . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs appeared first on MarkTechPost .
