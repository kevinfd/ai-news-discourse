---
id: "b8e67806b41988c5"
title: "Bring Agentic Coding On-Device with Foundry Local"
url: "https://devblogs.microsoft.com/foundry/foundry-local-agentic-coding-qwen3-8-27b"
link: "https://devblogs.microsoft.com/foundry/foundry-local-agentic-coding-qwen3-8-27b"
source: "Microsoft"
domain: "devblogs.microsoft.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T05:14:39Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["pmttyji"]
language: "en"
summary: "35-135% improvements(decode/tg) on 5090 & DGX Spark. Is it possible to add this to llama.cpp?"
tags: ["r/LocalLLaMA"]
orgs: ["Microsoft", "Nvidia", "AMD"]
topics: ["agents & coding", "chips & infrastructure", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 964
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xp4lv5/bring_agentic_coding_ondevice_with_foundry_local/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Bring Agentic Coding On-Device with Foundry Local

Microsoft · pmttyji · 2026-11-06

Coding agents can dramatically accelerate development—but cloud-only AI assistants can rack up costs, send sensitive context over the wire, and stall the moment your connection drops. Local inference flips that trade-off: your code and your context never leave the machine in front of you.
Foundry Local brings agentic coding directly to developer hardware. Run Qwen3.8-27B locally, connect it to GitHub Copilot, and get a responsive coding experience with predictable inference costs, greater privacy, and the freedom to keep working offline.
Foundry Local with Qwen3.8-27B for local coding
Qwen3.8-27B is our primary optimization target because it pairs strong coding capabilities with a size suited to high-performance local deployment. Published benchmarks show broad capability across agentic terminal tasks, software engineering, and repository-level code generation.
Optimized end to end for developer flow
Powered by ONNX Runtime, Foundry Local optimizes the full Qwen3.8-27B inference pipeline on Nvidia GPUs—from prefill and decoding to memory management, long-context processing, and concurrent requests—so local coding feels fast and responsive.
The hardware-aware optimization stack combines a comprehensive set of inference techniques to reduce compute and memory bottlenecks, maximizing performance across diverse hardware configurations:
- Faster inference speed: It leverages DFlash2 speculative decoding—a technique that uses a lightweight “drafter” model to predict multiple tokens at once, breaking through the memory-bandwidth ceiling and dramatically increasing decode throughput. It also applies CUDA graph fusions and kernel optimizations tuned specifically for the latest NVIDIA SM121 GPU architecture.
- Lower memory pressure: To fit within the memory limits of consumer GPUs, the solution combines efficient INT4 weight handling, KV-cache quantization, embedding memory sharing and CPU offloading. It also supports configurable, memory-aware inference to balance memory usage and performance across different hardware configurations. With 4-bit quantization, the model size is reduced to approximately 18 GB, making it runnable on consumer GPUs with 24 GB of VRAM, supporting context windows of up to 64K tokens. GPUs with 32 GB or more of VRAM can support longer context windows of up to the model’s maximum supported length of 262K tokens.
- Long context and parallel work: Modern coding workflows require processing large, repository-wide contexts across multiple simultaneous requests. The serving infrastructure uses prefix caching—reusing previously computed context so repeated prompts don’t start from scratch—and continuous batching to process concurrent workloads efficiently.
Together, these optimizations keep your assistant responsive as you explore a codebase, generate changes, run tools, and iterate across tasks. For model optimization instruction, see the Qwen3.8-27B optimization recipe.
Performance for coding workloads
We compared Foundry Local with llama.cpp using the 4-bit Qwen3.8-27B model on two systems: an NVIDIA GeForce RTX 5090 with 32 GB of VRAM and an NVIDIA DGX Spark with 128 GB of unified memory. The evaluation used a dataset of real GitHub issues. Foundry Local delivered higher generation speed at every tested prompt length, with the advantage widening beyond 131K tokens—exactly where repository-scale coding workflows need sustained performance.
On an NVIDIA GeForce RTX 5090 (32 GB VRAM)
On NVIDIA DGX Spark (128 GB unified memory)
Start coding locally with Foundry Local in GitHub Copilot
Have an NVIDIA GPU with at least 24 GB of VRAM? Follow the steps below to connect Foundry Local to GitHub Copilot using Bring Your Own Key (BYOK) and start coding locally. The example below uses BYOK in the GitHub Copilot app. Instructions for using GitHub Copilot BYOK with other clients are available here.
This experience requires Foundry Local CLI 0.13.0 or later, which includes the optimizations and capabilities described above. For NVIDIA GPU execution, install the required CUDA and compatible cuDNN runtimes separately, as Foundry Local does not download these dependencies. Ensure the runtime library paths are configured correctly (add the DLL directories to PATH on Windows). Refer to the release notes for platform-specific runtime requirements and setup instructions.
- Install the latest Foundry Local CLI with WinGet, then check the installed version.
winget install Microsoft.FoundryLocal
foundry --version The version command should report a version of 0.13.0 or higher. If Foundry Local was already running when you updated PATH, run foundry server restart from the new terminal before continuing.
- Load Qwen3.8-27B in Foundry Local and retrieve the API endpoint. foundry model load will trigger a model download if the model hasn’t been downloaded yet. foundry model load qwen3.8-27b
foundry server status Use the API endpoint returned by foundry server status on your machine, rather than copying the port shown in the screenshot.
- Connect GitHub Copilot to Foundry Local model.
- Switch the model provider to Foundry Local and select Qwen3.8-27B in the GitHub Copilot model picker. You’re now ready to start coding locally on your device.
It’s worth noting that local models may have limited reasoning capabilities compared with advanced cloud models due to their smaller size. For complex, high-reasoning tasks, cloud models remain a strong choice, while local models can efficiently handle everyday coding and targeted subtasks—enabling a flexible hybrid workflow.
What’s next for local coding
Next, we plan to expand Qwen3.8-27B support to more devices, including Macs and AMD GPUs, grow our lineup of coding-optimized local models, and deepen Foundry Local integration with GitHub Copilot for a more seamless local coding experience.
Ready to try local coding? Install Foundry Local, connect your endpoint to GitHub Copilot, and put Qwen3.8-27B to work on your own hardware. You get a private, cost-conscious, and responsive option for the everyday developer loop—right alongside the cloud models you already use.
Resources
- Foundry Local documentation — full reference documentation and samples for SDK and CLI usage
- Install Foundry Local CLI — set up the CLI and run your first model in minutes
- GitHub Copilot BYOK setup guide — step-by-step instructions for connecting a local endpoint in GitHub Copilot
- Qwen3.8-27B model card — model details, benchmarks, and licensing
- Share feedback — report issues, request features, and connect with developers
