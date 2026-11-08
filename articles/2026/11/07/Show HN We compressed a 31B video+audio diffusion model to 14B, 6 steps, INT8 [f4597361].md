---
id: "f459736103541901"
title: "Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8"
url: "https://github.com/Video-Rebirth/hyperflow-h3-flash"
link: "https://github.com/Video-Rebirth/hyperflow-h3-flash"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-07T15:16:01Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["jiant"]
language: "en"
summary: "HyperFlow H3 Flash is Video Rebirth's compressed, few-step version of MiniMax-H3. It generates video and synchronized stereo audio together.\nShowcase · Weights (Hugging Face) · ComfyUI nodes · GGUF setup guide · 8-step LoRA for full-size MiniMax-H3\n- Output: 5.2–15 s of video at 24 fps (1344×768 by default) with a 32 kHz stereo soundtrack.\n- Sampling: 4, 6 (default), or 8 steps, without…"
tags: []
orgs: ["Nvidia", "Hugging Face"]
topics: ["chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1984
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50405263"
score: 69
comments: 14
community: "Hacker News"
---

# Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8

GitHub · jiant · 2026-11-07

HyperFlow H3 Flash is Video Rebirth's compressed, few-step version of MiniMax-H3. It generates video and synchronized stereo audio together.
Showcase · Weights (Hugging Face) · ComfyUI nodes · GGUF setup guide · 8-step LoRA for full-size MiniMax-H3
- Output: 5.2–15 s of video at 24 fps (1344×768 by default) with a 32 kHz stereo soundtrack.
- Sampling: 4, 6 (default), or 8 steps, without classifier-free guidance (CFG).
- Speed (5.2 s clip, 6 steps): 8.7 s on 4× B200, 36 s on 1× H200, 92 s on 1× RTX 5090.
- Real time on 4× Blackwell GPUs: NVIDIA SOL-H3 runs HyperFlow H3 Flash in real time on 4× B-series GPUs. SOL-H3 is our inference-acceleration partner and supports this model from day 0.
- Model size: 13.7B (fl2va) or 13.9B (ref2va) parameters, less than half of the ~31B MiniMax-H3 transformer.
- Minimum footprint: Q4_K_M is 9.1 GB (Q8_0 is 14.9 GB). It runs on 24 GB and 32 GB GPUs in PCs with 16 GB of system RAM. 16 GB GPUs are not measured yet.
Decision rule: Use GGUF on PCs with 64 GB of system RAM or less. Use INT8 convrot on data-center GPUs, or on 24 GB+ RTX GPUs with at least 69 GiB of system RAM.
All weights are in VideoRebirthAI/hyperflow-h3-flash.
Full setup guide: integrations/README.md. Quick start:
- ComfyUI (Video-Rebirth/ComfyUI-HyperFlow-Flash):
  - Clone ComfyUI-GGUF and ComfyUI-HyperFlow-Flash into ComfyUI/custom_nodes/.
  - Download the 15.7 GB qwen3vl_32b_minimax_h3_nvfp4_awq text encoder.
  - On 16 GB or 32 GB PCs, start ComfyUI with python main.py --fast-disk.
  - Open Workflow > Browse Templates > ComfyUI-HyperFlow-Flash and select hyperflow_t2v, hyperflow_i2v, hyperflow_flf2v, or hyperflow_ref2v.
- Unsloth Studio (setup guide):
  - Point SD_CLI_PATH at the patched sd-cli binary and run unsloth studio.
  - Load VideoRebirthAI/hyperflow-h3-flash (fl2va_gguf/ or ref2va_gguf/).
  - Studio downloads the companion text encoder and VAEs automatically. It runs the built-in 6-step schedule at CFG = 1.
- stable-diffusion.cpp (integrations/stable-diffusion.cpp/):
Apply hyperflow-two-time.patch to upstream commit 3be2378. The patch adds the two-time (t, r) embedder, low-rank linear layers, the default 6-step schedule from GGUF metadata, and 32-bit matmul token splitting for long clips.
pip install git+https://github.com/Video-Rebirth/hyperflow-h3-flash
pip install "hyperflow-h3-flash[hopper] @ git+https://github.com/Video-Rebirth/hyperflow-h3-flash"  # H100 / H200: FlashAttention-3
pip install "hyperflow-h3-flash[fp8] @ git+https://github.com/Video-Rebirth/hyperflow-h3-flash"     # --text-encoder-precision fp8
- Requirements: Python 3.10+, PyTorch 2.6+ with CUDA and Triton (pip install triton-windows on native Windows), an Ampere or newer NVIDIA GPU, and diffusers >= 0.40. Multi-GPU (--gpus > 1) requires Linux or WSL2 (raise memory= in %UserProfile%\.wslconfig on WSL2).
- First-run download: ~90 GB, or ~68 GB with --text-encoder-precision fp8. This includes the MiniMax-H3 text encoder, VAEs, and the 16 GB HyperFlow INT8 transformer for the selected task. The 62 GB base transformer is never downloaded.
- First-run compilation: Triton INT8 kernels compile on first use (~1 min).
Run hyperflow-h3-flash or python -m hyperflow_h3_flash:
# Text to video + audio (t2va)
hyperflow-h3-flash --prompt "A chef slides a steaming bowl of ramen across a wooden counter; rain taps on the window." \
    --output ramen.mp4
# First keyframe, or first + last keyframe (fl2va)
hyperflow-h3-flash --prompt "..." --image first.png --output clip.mp4
hyperflow-h3-flash --prompt "..." --image first.png --last-image last.png --output clip.mp4
# Reference images, videos (with soundtrack), and audio clips in prompt order (ref2va)
hyperflow-h3-flash --prompt "<Picture 1> walks through the scene of <Picture 2> ..." \
    --reference person.png --reference scene.png --output clip.mp4
# 15 s clip, context-parallel across 4 GPUs (or --gpus auto for up to 4 visible GPUs)
hyperflow-h3-flash --prompt "..." --num-frames 360 --gpus 4
# 4 steps (speed), 6 steps (default), or 8 steps (quality)
hyperflow-h3-flash --prompt "..." --steps 4
examples/benchmark.py times every pipeline stage and per-GPU peak memory under torchrun.
import torch
from diffusers.utils.export_utils import encode_video
from hyperflow_h3_flash import load_pipeline
pipe = load_pipeline("t2va")  # "fl2va": pass image=... (and last_image=...); "ref2va": pass references=[...]
out = pipe(
    prompt="A chef slides a steaming bowl of ramen across a wooden counter.",
    num_frames=124,
    num_inference_steps=6,  # 4, 6, or 8
    generator=torch.Generator().manual_seed(0),
    output=["videos", "audio", "sampling_rate"],
)
encode_video(
    out["videos"][0],
    fps=24,
    output_path="ramen.mp4",
    audio=out["audio"][0],
    audio_sample_rate=out["sampling_rate"],
)
- Multi-GPU under torchrun: Call torch.distributed.init_process_group("nccl") and pass device=f"cuda:{local_rank}" to load_pipeline. The pipeline shards execution across ranks and returns the full output on every rank.
- Standalone transformer (AutoModel): Each INT8 Hub folder ships self-contained model code. Load it without installing this package: from diffusers import AutoModel, then AutoModel.from_pretrained("VideoRebirthAI/hyperflow-h3-flash", subfolder="fl2va_int8_convrot", trust_remote_code=True, torch_dtype=torch.bfloat16).
--offload sets GPU memory placement. auto (default) selects a mode from per-GPU VRAM:
- stream is only ~2% slower than none on the same GPU.
- model and stream keep offloaded weights in one pinned host-memory allocation.
- The loader drops unused Qwen3-VL layers above the conditioning tap. This saves ~14 GB. --text-encoder-precision fp8 saves another ~22 GiB.
- In containers, read the memory limit from /sys/fs/cgroup/memory.max, not from free.
All runs are end-to-end at 1344×768 and 6 steps: text encoding, transformer, and video and audio VAE decode. Each a / b cell is total time for a 5.2 s / 15 s clip (124 / 362 frames).
- GGUF setup: ComfyUI, Q4_K_M, and the 15.7 GB nvfp4 text encoder. 32 GB and 16 GB PCs use --fast-disk with models on NVMe (Host RAM). Peak RSS is 34–37 GiB on ≥ 64 GB PCs. Anonymous RSS is ~8–16 GiB on 32 GB PCs and ~8 GiB on 16 GB PCs.
- INT8 setup: hyperflow-h3-flash --offload stream. It needs ≥ 91 GiB of system RAM with the bf16 text encoder, or ~69 GiB with fp8. The 15 s RTX 5090 run used fp8.
- The INT8 transformer is 10–20% faster. GGUF needs less than half the system RAM. The transformer takes over 80% of the time and is compute bound. ComfyUI dequantizes Q4_K_M weights at run time.
- Use --fast-disk on 16 GB and 32 GB PCs. It streams unresident weights from the OS file page cache. Without it, ComfyUI-GGUF copies the 9 GB transformer into pinned RAM when VRAM overflows. 16 GB PCs then run out of RAM on 15 s clips. On 32 GB PCs, the RTX 3090 and 5090 become 13% and 21% slower (text encoding takes 27–31 s instead of 7–9 s).
- 32 GB of VRAM holds both models. On the RTX 5090, the text encoder and transformer stay in VRAM together (0.8 s text encoding). On 24 GB GPUs, ComfyUI swaps them between stages (10–16 s text encoding).
- Keyframe tasks (i2v, flf2v): See GGUF guide: Performance.
- References: Two 768p stills generated with t2va (a person and a street market). Mixed is one still, one 5.2 s reference video with its soundtrack, and one audio clip.
- INT8 setup: 100–125 GB of system RAM (80–88 GiB process RSS). ¹ On 24 GB GPUs, 15 s mixed runs need --block-chunk 16384. Without it, they run out of VRAM.
- GGUF setup: ComfyUI on ≥ 64 GB RAM, with hyperflow_ref2v_api.json and the nvfp4 text encoder. ref_image_size match (default) downscales each reference to the output's pixel area and keeps its aspect ratio. max downscales only above a 2048 short edge. The max runs used the stills upscaled to 3584×2048, the size the INT8 pipeline uses. ² max at 15 s needs python main.py --disable-cuda-malloc. The default cudaMallocAsync allocator fails with CUDA error: invalid argument.
- Each reference adds tokens to every step. At a 2048 short edge, one image adds ~14,300 tokens (about seven 768p latent frames). The clip itself is 37,710 tokens at 5.2 s and 109,062 at 15 s. Attention cost grows with the square of the token count. So at 5.2 s, the INT8 transformer takes 2.6–2.9× its t2va time with two images and 5.2–5.8× with the mixed set.
- GGUF match is the fastest image-reference path. It adds 24–36% to t2v at 5.2 s and 7–15% at 15 s. At the same reference size (max), GGUF is 11–25% slower than INT8 at 5.2 s and 8–9% slower at 15 s.
- --fast-disk also works for ref2v. 32 GB and 16 GB PCs ran 5.2 s and 15 s clips on all three GPUs, within 4% of ≥ 64 GB RAM at 15 s. See GGUF guide: Host RAM.
- Real-time inference: The table measures this package. For real time on 4× B-series GPUs, use NVIDIA SOL-H3.
- INT8 GEMM backend: The 4× H200 row uses the default Triton kernel (12.6 s). int8_gemm="sgl" (CUTLASS INT8 via sgl-kernel) measured 12.3 s.
- 4-GPU stage times (5.2 s): Text encoder 0.11–0.16 s. 6-step transformer 7.8–7.9 s on 4× H200 and 5.0 s on 4× B200. Video VAE decode 3.3–4.0 s.
- 1088p (1920×1088, 362 frames): 743 s on 1× H200 (106 GiB VRAM). 220 s on 4× H200 (68 GiB VRAM/GPU).
HyperFlow H3 Flash changes the MiniMax-H3 transformer in three ways:
- Structural pruning and low-rank factorization:
- Rotated W8A8 INT8 quantization (convrot): 180 linear layers are quantized to W8A8 INT8 behind a block-diagonal Hadamard rotation.
- Two-time (t, r) conditioning: Every token receives the current noise level t and the step endpoint r. This enables 4-to-8-step sampling without CFG. Conditioning tokens stay at their anchor noise level (r = t).
- 
Sequence and VAE parallelism (--gpus N): Ulysses context parallelism splits the packed transformer sequence across$N$ GPUs. Ranks encode keyframes and references and decode spatial video VAE tiles in parallel. Then they all-gather and blend the tiles to match single-GPU output bitwise.
- 
Text encoder placement: With --offload none and the bf16 text encoder, FSDP2 shards the 50 GiB text encoder across GPUs. This cuts 4-GPU peak VRAM from 91 GiB to 59 GiB/GPU. When offloading or using fp8, rank 0 runs the text encoder and broadcasts the embeddings (~2 MB).
- INT8 GEMM dispatch:
- Reproducibility: The same seed, GPU architecture, GPU count, and attention backend produce bitwise-identical clips. text_encoder_fsdp and vae_parallel preserve bitwise output.
make install   # create .venv and install editable package with dev tools
make test      # run unit tests on tiny models (CUDA tests skip without a GPU)
make lint      # ruff check + format check.
├── src/hyperflow_h3_flash/        # Python package (INT8 runtime)
│   ├── cli.py                     # `hyperflow-h3-flash` CLI entry point
│   ├── __main__.py                # `python -m hyperflow_h3_flash` entry point
│   ├── hostmem.py                 # Host RAM estimate before loading
│   ├── pipeline.py                # `load_pipeline`: loads models, trims unused text-encoder layers, configures offload/multi-GPU
│   ├── blocks.py                  # Modular Pipeline blocks swapped into the official MiniMax-H3 workflows
│   ├── transformer.py             # `HyperFlowH3FlashTransformer3DModel`: dropped blocks, low-rank linears, two-time (t, r) conditioning
│   ├── int8.py                    # Hadamard-rotated W8A8 linear layers (Triton, cuBLASLt, CUTLASS, and B300 BF16 kernels)
│   ├── schedule.py                # 4-, 6-, and 8-step sigma grids and per-token (t, r) pairs
│   ├── offload.py                 # Single-GPU memory placement (`none`, `model`, `stream`)
│   └── distributed.py             # Multi-GPU execution (torchrun launch, Ulysses attention, FSDP2 / rank-0 text encoder, parallel VAE)
├── integrations/                  # GGUF runtimes for consumer GPUs
│   ├── README.md                  # Step-by-step setup guide for ComfyUI, Unsloth Studio, and stable-diffusion.cpp
│   ├── ComfyUI-HyperFlow-Flash/   # Custom nodes (`loader_nodes.py`, `model_patch.py`, `gguf_io.py`; GPL-3.0)
│   │   └── example_workflows/     # Four UI workflows (`hyperflow_t2v`, `hyperflow_i2v`, `hyperflow_flf2v`, `hyperflow_ref2v`) and API versions in `api/`
│   └── stable-diffusion.cpp/      # `hyperflow-two-time.patch` for upstream commit `3be2378` (MIT)
├── examples/                      # `benchmark.py` (per-stage timings and peak memory)
├── tests/                         # Unit tests on tiny models (CUDA tests skip without a GPU)
├── Makefile                       # `make install`, `make test`, and `make lint`
├── pyproject.toml                 # Package metadata and optional extras (`hopper`, `sgl`, `fp8`, `dev`)
├── LICENSE                        # Apache License 2.0
└── THIRD_PARTY_NOTICES.md         # Notices for components adapted from `diffusers`
- Repository code: Apache License 2.0, except integrations/ComfyUI-HyperFlow-Flash (GPL-3.0) and integrations/stable-diffusion.cpp (MIT).
- Third-party notices: Components adapted from diffusers retain their notices in THIRD_PARTY_NOTICES.md.
- Model weights: A Model Derivative of MiniMax-H3 distributed under the MiniMax H3 Community License Agreement. The CLI and load_pipeline download them on first run, and using them means accepting that Agreement. The Agreement does not cover use in the European Union, the United Kingdom, the Republic of Korea, or the United States without MiniMax's authorization, and it includes an Acceptable Use Policy. See the model card for license terms and notices.
