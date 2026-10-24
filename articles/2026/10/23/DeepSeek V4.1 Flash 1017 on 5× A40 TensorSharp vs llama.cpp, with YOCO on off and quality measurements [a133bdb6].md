---
id: "a133bdb60972d8d9"
title: "DeepSeek V4.1 Flash 1017 on 5× A40: TensorSharp vs llama.cpp, with YOCO on/off and quality measurements"
url: "https://github.com/zhongkaifu/TensorSharp"
link: "https://github.com/zhongkaifu/TensorSharp"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T15:47:06Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["fuzhongkai"]
language: "en"
summary: "I’m the developer of TensorSharp , and I wanted to share some results from running DeepSeek-V4.1-Flash-1017 on five NVIDIA A40s . The largest gains are in prompt processing: TensorSharp reached 4.4–5.5× llama.cpp’s prefill throughput on the longer real-text server prompts with its default YOCO optimization enabled. With YOCO disabled, the gains were still 2.4–3.2× . There is a measurable quality…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "DeepSeek", "OpenAI", "Apple", "Alibaba", "Intel", "AMD"]
topics: ["models & research", "chips & infrastructure", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 1482
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdho58/deepseek_v41_flash_1017_on_5_a40_tensorsharp_vs/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# DeepSeek V4.1 Flash 1017 on 5× A40: TensorSharp vs llama.cpp, with YOCO on/off and quality measurements

GitHub · fuzhongkai · 2026-10-23

TensorSharp is a .NET 10 inference engine for local GGUF models. Run it on Windows, macOS or Linux through the CLI, browser chat, or Ollama/OpenAI-compatible APIs, or embed it in your own .NET application. Use managed C# CPU kernels or native CUDA, Metal and Vulkan backends, with support that varies by model.
Current source covers text and reasoning, multimodal input, embeddings, image generation/editing, video with audio, personal knowledge collections, and Agent Skills with code tools. TensorSharp also powers TensorAgent, the local app for iPhone, iPad, Mac and Windows. Start below, or check the project status for capabilities and validation limits.
- Local models, several interfaces. One engine for CLI use, browser chat and Ollama/OpenAI-compatible APIs, across managed CPU and native accelerator backends.
- Text and multimodal models. Dense and MoE GGUF models, reasoning, image/audio input and document questions. See Supported models for each family's capabilities.
- Embeddings and media generation. EmbeddingGemma 2 provides text/code embeddings and optional image, audio and video inputs. Generate and edit images with Qwen-Image-2.1 and Turbo, or generate video with stereo audio using LTX 2.5 Distilled (48 kHz) and MiniMax-H3 (32 kHz).
- Editable video projects. Video Studio in WebUX Chat and TensorAgent shares a persistent multitrack editor, native generation jobs, reviewed agent proposals, undo/redo and local FFmpeg export. Long videos are made as chains of takes, each starting on the previous segment's last frame; reference photos keep a character in new shots. See the validation matrix for tested models and platform limits.
- Efficient serving. Continuous batching and a paged, Radix prefix-shared KV cache are on by default. Speculative decoding and multi-GPU placement are available for supported models. See Features.
- Agent Skills and code tools. TensorSharp.AgentHost adds file, shell and document workflows. The 17 bundled skills include research, documents, TDD, design interviews and handoff; find-skills searches, inspects and installs additional skills when network access is enabled. Server and TensorAgent chats also support bounded sub-agent delegation with private workspaces and read-only defaults.
- Personal knowledge collections. Upload files or nested folders, and import saved chats with their attachments and artifacts. Select collections per chat, retrieve cited excerpts with page/row/time locations, preview originals, or let code agents open full datasets. Local BM25 works by default; optional GGUF embeddings add semantic search, and compatible media models index images, audio and sampled video. Extraction status and warnings show coverage limits.
- Steer an active response. Submit a new instruction while the CLI, server Web UI or TensorAgent is reasoning or answering. The next response uses the conversation, partial output and your guidance; Stop remains available.
- Latest recorded comparisons. DeepSeek V4.1 Flash 1017 on five A40 GPUs and Muse Spark on ten have workload-specific comparisons against llama.cpp. In the matched ~1.8K DeepSeek prompt, exact TP5 prefill was 3.23× the reference rate; default approximate YOCO was 5.50× with a measured quality trade-off. See Benchmarks for the exact settings, slower cells and limitations.
- TensorAgent apps. Local chat, attachments, skills and saved work on phones and desktops. See the Mac/Windows installation guide and app coverage notes.
Explore both books and their repository reading paths
TensorSharp/TensorAgent is free. If you like it, a coffee keeps the work on it going.
The Releases page provides self-contained CLI and Server archives for Windows x64 (CPU/CUDA), Linux x64 (CPU/CUDA), and macOS arm64.
To build from source you need the full .NET 10 SDK (how to install it), git, curl, CMake 3.20+, and the toolchain for your GPU. Then run the verified Gemma 4 E4B model (7.48 GiB). On Windows with an NVIDIA GPU (PowerShell):
git clone https://github.com/zhongkaifu/TensorSharp.git; Set-Location TensorSharp
New-Item -ItemType Directory -Force models | Out-Null
curl.exe -L --fail "https://huggingface.co/ggml-org/gemma-4-E4B-it-GGUF/resolve/main/gemma-4-E4B-it-Q8_0.gguf?download=true" -o models\gemma-4-E4B-it-Q8_0.gguf
'Answer in one short sentence: what is TensorSharp?' | Set-Content prompt.txt
$env:TENSORSHARP_GGML_NATIVE_ENABLE_CUDA = 'ON'
dotnet run --project TensorSharp.Cli -c Release -p:TensorSharpSkipMlxNative=true -- --model models\gemma-4-E4B-it-Q8_0.gguf --input prompt.txt --max-tokens 128 --backend ggml_cuda
On other machines, change the backend (see Pick a backend):
- macOS (Apple Silicon): drop the CUDA environment variable and use --backend ggml_metal.
- Linux + NVIDIA: prefix the dotnet run with TENSORSHARP_GGML_NATIVE_ENABLE_CUDA=ON and use --backend ggml_cuda.
- AMD / Intel / NVIDIA Vulkan: set TENSORSHARP_GGML_NATIVE_ENABLE_VULKAN=ON and use --backend ggml_vulkan.
Host the same model as a server: a browser chat at http://localhost:5000 plus Ollama- and OpenAI-compatible APIs.
dotnet run --project TensorSharp.Server.Host -c Release -p:TensorSharpSkipMlxNative=true -- --model models/gemma-4-E4B-it-Q8_0.gguf --backend ggml_cuda --max-tokens 512
The server listens on 0.0.0.0:5000 with no built-in authentication or TLS; keep it behind a firewall or an authenticated HTTPS reverse proxy.
The Getting started guide has the rest: installing the SDK on each platform, multi-GPU and multi-node runs, NVIDIA DGX Spark, multimodal input, embeddings, and making it fast. Every option is in the CLI and Server references, and both programs print them with --help.
dotnet build TensorSharp.slnx also builds TensorAgent's available desktop heads and the iOS simulator head on Apple Silicon when the selected SDK has the required MAUI workloads and staged native/Python files. Missing prerequisites skip the affected app head with a warning; see TensorAgent build instructions.
Download the latest release and expand Assets. Choose a file beginning with tensoragent-desktop-:
The app includes its .NET runtime and native engine. Windows needs WebView2 Evergreen Runtime if missing; Python/Node are optional tools for skills. The current built-in catalog needs at least 12 GB system RAM, and model weights download separately. Open ☰ → Models → Download → Use, then type a message. The Desktop user guide covers package verification, unsigned-app prompts, first-run setup, attachments, skills, updates and troubleshooting. Historical releases may have no Desktop assets until a release runs the updated workflow; iPhone/iPad remain source builds.
- Text, reasoning, and multimodal LLMs: DeepSeek V4 Flash / V4.1 Flash, GLM 5.x, Gemma 4, Qwen 3.5 / 3.6 / 3.8 27B, Qwen 3.8 Flash Next, Bonsai2 (Qwen family), GPT OSS, Nemotron-H, Mistral 3, Hunyuan Dense, Muse-Glimmer, and Muse Spark (816B MoE, multi-GPU).
- Text diffusion: DiffusionGemma, including Jev typed decision inference at /v1/systemone, over text, images, uploaded documents, sampled video frames and audio transcripts (configured ASR companion).
- Image generation/editing and video generation: Qwen-Image-2.1, LTX 2.5 Distilled (video + 48 kHz stereo audio), MiniMax-H3 (video + stereo audio), and Wan 2.1 / 2.2.
- Embeddings: EmbeddingGemma 2, including text/code and optional image, audio, and video inputs; BERT / XLM-R encoders including Snowflake Arctic Embed L v2.0 and all-MiniLM-L6-v2.
Backend, modality, feature support, and validation coverage vary by model. See the supported models tables, the model cards, and the embedding guide for details.
TensorAgent's current catalog has 38 entries, grouped into searchable model families with memory and download filters, including LTX 2.5 Distilled at an experimental 48 GB memory tier, Qwen-Image-2.1 Turbo at 4-bit and 8-bit quantizations, fourteen image LoRA plug-ins and two MiniMax-H3 Turbo speed plug-ins. The expanded catalog includes experimental entries whose memory tiers and app/device behavior have not all been measured. Qwen3.8 Flash Next uses SSD-backed weights; its Q2 package was measured on a 48 GB Mac, and IQ1_M has separate Windows catalog-host validation. Multi-GPU --layer-split and --tp are separate controls; support and performance depend on the architecture and quantization. See TensorAgent's coverage notes and the model cards. Desktop installers appear in releases built with the updated Release Binaries workflow, while older releases may lack them.
One engine, four ways to use it, each an unedited capture of a real run.
What each run shows, step by step: Screenshots.
Latest recorded comparisons, audited on 2026-10-23. DeepSeek V4.1 Flash 1017 was measured on five A40 46 GB GPUs on October 22–23; Muse Spark's ten-A40 report was refreshed October 22 (its exact measurement date is not recorded). These are different models and workloads, not a combined engine speedup.
DeepSeek: UD-IQ2_XXS, 32,768-token context, one request, 256 output tokens, greedy/thinking off; prefill uses internal server timers, not HTTP TTFT. TensorSharp TP5 is compared with the reference's supported layer split. Default YOCO is approximate: wikitext-2 perplexity was 2.4978, versus 2.4811 with exact prefill and 2.4697 for llama.cpp. 5.50× applies only to that approximate ~1.8K prefill cell, not decode or general engine performance. Model, method and provenance.
Muse Spark: UD-IQ3_XXS, 32,768-token context, F16 KV, greedy/thinking off; matching placement modes, 32 output tokens for long-prompt prefill and 256 for short decode / concurrent requests. Prefill is uncached prompt tokens divided by streamed TTFT. Layer-split decode was slightly slower: 16.69 vs 16.79 tok/s (0.99×). On this host P2P was broken and llama.cpp tensor split ran without NCCL, while TensorSharp used NCCL; that limits the TP comparison. Full report.
Methods, repetitions, quality trade-offs and build limitations: Benchmarks. No new benchmark runs are claimed; these results do not qualify every backend or the published release binaries.
New here? The sections above are all you need to get running. Everything else is detailed reference:
Actively developed, and the source tree runs ahead of the published packages.
Per-area detail (which architecture runs on which backend, which features each family supports, and the known limits) is in the status matrix.
Zhongkai Fu
See LICENSE for details.
