---
id: "5e9d3fd0e59ccb77"
title: "Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU"
url: "https://github.com/synchopate/llama-modchip"
link: "https://github.com/synchopate/llama-modchip"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-08T10:22:04Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["joshcsimmons"]
language: "en"
summary: "Break the 64 GB RAM Wall: Run 284B DeepSeek-V4-Flash (< 59 GiB RAM) & 30B MoEs (up to 111 tok/s) at 256K Context on Pure CPU — Zero GPUs Required.\n⚡ Quickstart · 🧩 Supported Models · 🖥️ Supported Chips & Platforms · 🏆 Leaderboard · 📄 Preprint PDF (paper/) · 📐 Architecture · ❓ FAQ\nReal-time Frontier & Agentic MoE inference on the CPU workstation you already own — 100% in RAM, zero NVMe…"
tags: []
orgs: ["DeepSeek", "Nvidia", "Anthropic", "AMD", "Meta", "Apple", "Amazon", "Hugging Face"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 921
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50411961"
score: 31
comments: 13
community: "Hacker News"
---

# Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

GitHub · joshcsimmons · 2026-11-08

Break the 64 GB RAM Wall: Run 284B DeepSeek-V4-Flash (< 59 GiB RAM) & 30B MoEs (up to 111 tok/s) at 256K Context on Pure CPU — Zero GPUs Required.
⚡ Quickstart · 🧩 Supported Models · 🖥️ Supported Chips & Platforms · 🏆 Leaderboard · 📄 Preprint PDF (paper/) · 📐 Architecture · ❓ FAQ
Real-time Frontier & Agentic MoE inference on the CPU workstation you already own — 100% in RAM, zero NVMe swap:
TL;DR — The 3 Paradigm-Breaking Pillars of llama-modchip:
- 🐋 284.33B Frontier MoE in a 64 GB CPU Box: Shrinks DeepSeek-V4-Flash from 76.87 GiB (which crashes in OOM on 64 GB Linux) down to 56.56 GiB on disk / 57.61–58.9 GiB VmRSS at full 256K context (44.36 tok/s prefill, 9.06–10.74 tok/s pure CPU decode, 11.5–14.7 tok/s with PVS) using closed-form Analytical SwiGLU-H2 Second-Order Hessian Compression + Fractal-64 (Q2_0, 3.75 bpw) MLA transcoding + 4-Level Register (ZMM AVX-512BW) + L1D (32 KB) + L2 (1 MB) + L3 (64 MB) Whole-Model Tiling +$L_2$ -Quadrature MoE Pruning.
- ⚡ 30B MoE at GPU Speeds on Pure CPU: Runs NVIDIA-Nemotron-3.5-30B-A3B in 14.35 GiB at 25.0–60.4 tok/s on 16-core Zen 5 (111.6 tok/s on Threadripper, 80.8 tok/s on AMD Vulkan Hybrid, 44.97 tok/s on AWS Graviton3 ARM64) via a 1.64 MB Stockfish-PVS v2 + RouteCrack L2/L3 Drafter (96.4% acceptance) and _MM_HINT_NTA L3 cache isolation (HARPCache).
- 🤖 Zero-API Claude Code (./modchip claude): Eliminates the 45-second CPU agent prompt re-evaluation bottleneck via /dev/shm Slot-0 KV Warm Restore (18.9 ms on Nemotron-30B / 13.1–32.6 ms on DeepSeek-284B) with all 40 Claude Code tools active.
git clone https://github.com/synchopate/llama-modchip.git
cd llama-modchip
./modchip chat
⚠️ Important Compatibility Note (GGML_TYPE_Q2_0 = 40): Our Fractal-64 models use custom block-64 BF16-scale Gray-coded tensors (GGML_TYPE_Q2_0, type ID 40) and custom deepseek4 / Stockfish-PVS kernels. Opening them in unpatched llama.cpp, Ollama, or LM Studio will fail with unknown tensor type 40. Use either ./modchip above or our standalone single-file pre-compiled binary (llama-server-modchip-linux-x86_64, zero .so dependencies) bundled directly inside the Hugging Face repositories and GitHub Release v2.4.0:
# 1. For 30B Nemotron-3.5-A3B (14.35 GiB — runs in 16–32 GB RAM at 25–60.4 tok/s):
hf download Synchopate/NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64-CPU-GGUF \
  llama-server-modchip-linux-x86_64 NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf --local-dir .
chmod +x llama-server-modchip-linux-x86_64
./llama-server-modchip-linux-x86_64 -m NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf -c 262144 -t 16 --port 8080
# 2. For 284B DeepSeek-V4-Flash (56.56 GiB — fits in 64 GB RAM at 9.1–14.7 tok/s):
hf download Synchopate/DeepSeek-V4-Flash-0731-Fractal-64GB-CPU-GGUF --local-dir ./dsv4
chmod +x ./dsv4/llama-server-modchip-linux-x86_64
./dsv4/llama-server-modchip-linux-x86_64 -m ./dsv4/DeepSeek-V4-Flash-0731-Fractal-00001-of-00003.gguf -c 32768 -t 16 -fa on --port 8080
Open windows/ and double-click windows/AVVIA_MODCHIP.bat (or run ./modchip start in Git Bash). It automatically detects your CPU cores, free RAM, and GPU VRAM (nvidia-smi), downloads official llama.cpp CUDA 12.4 / Vulkan binaries, computes the optimal --n-cpu-moe split, and opens the Web Chat UI (http://127.0.0.1:8080).
curl -sL https://raw.githubusercontent.com/synchopate/llama-modchip/main/scripts/check_cpu_readiness.py | python3
👉 Paste your terminal scorecard in a 📊 1-Click GitHub Benchmark Issue or GitHub Discussions to be added to the Official Community CPU Leaderboard!
Each model family has a dedicated deep-dive optimization guide with exact mathematical proofs, operator-level latency breakdowns, and quality gate benchmarks:
Full microarchitectural details and tuning flags for every supported processor and GPU hybrid are documented in docs/HARDWARE_OPTIMIZATIONS.md:
Full operator-level profiling and mathematical proofs in docs/DEEPSEEK_V4_OPTIMIZATIONS.md:
Full ablation tables and 100/100 Quality Gate report in docs/NEMOTRON_OPTIMIZATIONS.md:
Run ./modchip bench (or windows\BENCHMARK_PC.bat on Windows) and ➕ Submit Your Scorecard (1-Click GitHub Issue)!
🛠️ Click to expand: Repository Structure & Manual CMake Build Instructions
llama-modchip/
├── modchip                                    # Unified CLI (setup | start | chat | bench | eval | quantize | web | claude | stop)
├── install.sh                                 # 1-Command Automated Installer (Linux)
├── README.md / ARCHITECTURE.md / FAQ.md       # Clean Overview, Full Mathematical Paper & Engineering FAQ
├── RELEASE_NOTES.md                           # v2.4.0 Release Notes
├── docs/
│   ├── NEMOTRON_OPTIMIZATIONS.md              # Deep-dive on Nemotron-3.5-30B-A3B & Nemotron-H-8B optimizations
│   ├── DEEPSEEK_V4_OPTIMIZATIONS.md           # Deep-dive on DeepSeek-V4-Flash 284B profiling, SVD & L2-quadrature MoE
│   └── HARDWARE_OPTIMIZATIONS.md              # Chip-by-chip optimizations (Zen 5, Threadripper, Vulkan, CUDA, Metal, ARM64)
├── patches/
│   ├── deepseek-v4-flash-fractal-256k.patch   # Unified v2.4.0 patch (DeepSeek-V4-Flash 284B + Nemotron-3.5 30B, Linux/macOS/Windows)
│   └── zen5-nemotron-256k-optimizations.patch # Standalone ggml/llama core patch for Nemotron-3.5
├── windows/                                   # 1-Click Windows 10/11 Hybrid GPU+CPU MoE Pack (AVVIA_MODCHIP.bat, modchip_win.ps1)
├── apple-silicon/                             # Apple M4 Pro (24 GB) Metal setup & 128K benchmarks
├── fedora/                                    # Fedora 44 / AMD Ryzen 7 8745HS (GEEKOM A8) all-in-one script
├── speculative/                               # RouteCrack + Stockfish-PVS v2 (rc_stockfish.h, ngram-map.cpp, 96+ techniques)
├── benchmarks/                                # eval_quality_and_tools.py (100-pt Quality Gate) & results/*.json
├── gateway/sse_gateway.py                     # Agentic SSE Proxy + Compact Tool Table + Dark-Mode Web Chat HUD (:8787)
└── scripts/                                   # build_fractal_moe_gguf.sh, transcode_dsv4.{c,py}, chat.py, llama_modchip.py
llama-modchip demonstrates that modern multi-core CPUs and compact Mini-PCs with 64–128 GB of DDR5 RAM can run 284B Frontier MoEs (DeepSeek-V4-Flash) and 30B Hybrid MoEs (Nemotron-3.5-30B-A3B) locally at full 256K context—eliminating $30,000+ multi-GPU hardware requirements for air-gapped enterprise code intelligence, security auditing, and autonomous agent fleets.
We actively partner with hardware manufacturers, cloud silicon teams, and AI research labs to build and validate architecture-specific kernel patches:
- 🖥️ CPU & Workstation OEMs (AMD Ryzen AI / Threadripper / EPYC, Minisforum, Framework, System76, Apple, Intel): Sponsor a physical test unit or workstation to receive dedicated L1D/L2/L3 cache-tiling & SIMD kernels and permanent verification on the Official README CPU Leaderboard.
- ☁️ Cloud & ARM64 Silicon Teams (AWS Graviton4, AmpereOne, Google Axion, Azure Cobalt): Sponsor cloud compute credits to validate SVE2 / SME / multi-socket NUMA kernels.
- 🤝 Enterprise Support & Custom Model Transcoding: Reach out via GitHub Issues or GitHub Sponsors to sponsor custom SwiGLU-H2 + Fractal-64 model transcoding and on-premise deployment.
