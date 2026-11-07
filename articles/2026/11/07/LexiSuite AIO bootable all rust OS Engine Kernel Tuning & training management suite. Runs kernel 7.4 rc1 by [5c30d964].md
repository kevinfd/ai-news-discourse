---
id: "5c30d9649836a6d7"
title: "LexiSuite AIO bootable all rust OS/Engine/Kernel/Tuning & training management suite. Runs kernel 7.4 rc1 by default as the kernel needs work. Engine runs Qwen3.8 27b faster with lossless 5-25% lead over llama.cpp. 100% solo authored. Built on for 7900xtx vulcan, should work on other AMD cards."
url: "https://github.com/W61k3r/LexiSuite-Releases/releases/tag/LexiSuitet6"
link: "https://github.com/W61k3r/LexiSuite-Releases/releases/tag/LexiSuitet6"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T06:19:12Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["W61k3r"]
language: "en"
summary: "Use balena etcher or whatever to mount to USB stick, boot. Test. Report. Verified 5-25% faster than llama.cpp, system uses 90% of card bandwidth as opposed to 80% on my 7900xtx. I there is code for nvidia, intel, amd, and chinese hardware and supports 20 lanuages."
tags: ["r/LocalLLaMA"]
orgs: ["AMD", "Microsoft", "DeepSeek", "Alibaba", "Intel"]
topics: ["products & launches", "chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1884
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpzdy6/lexisuite_aio_bootable_all_rust/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# LexiSuite AIO bootable all rust OS/Engine/Kernel/Tuning & training management suite. Runs kernel 7.4 rc1 by default as the kernel needs work. Engine runs Qwen3.8 27b faster with lossless 5-25% lead over llama.cpp. 100% solo authored. Built on for 7900xtx vulcan, should work on other AMD cards.

GitHub · W61k3r · 2026-11-07

Repository navigation
LexiSuite Testing Image 6
Pre-release
LexiSuite
DOWNLOAD LINK
https://github.com/W61k3r/LexiSuite-Releases/releases/download/LexiSuitet6/LexiSuite-051033e-secureboot-dev.img.xz
OS / Kernel / Engine / Panel. All Rust.
A complete local inference stack, from the kernel that boots the machine to the browser
panel that runs it. Your hardware, your models, nothing in the cloud.
Overview •
Architecture •
Performance •
Models •
Quick start •
API •
Hardware •
Status •
License
Overview
LexiSuite is four products built to work as one system:
Why build the whole stack:
- It's fast on real cards. On the 7900 XTX with draft-head speculation, LexiEngine is level with or ahead of
llama.cpp on every 27B row measured on 11/03/2026, up to 30% faster, and processes prompts up to 22% faster.
See Performance.
- One Rust codebase. 1.77 million lines across 324 crates, from boot code to the browser UI.
- Local by design. Models, prompts and data stay on your machine.
- It boots from a stick. A development USB image carries Linux 7.3 and LexiKernel side by side, and LexiKernel
has booted real hardware and served the Panel from it.
Architecture
flowchart TB
    subgraph clients [Clients]
        B[Browser]
        A[API clients]
    end
    subgraph panel [LexiPanel]
        P[Auth, instances, models, storage, fleet]
    end
    subgraph engine [LexiEngine]
        H[HTTP APIs]
        S[Scheduler and sampling]
        M[Model graphs: Qwen, Gemma, DeepSeek]
        V[Vulkan]
        C[CUDA]
        U[CPU]
    end
    subgraph os [LexiOS]
        O[Init, network, firewall, storage, setup, updates]
    end
    subgraph kernels [Kernel, chosen at boot]
        L[Linux 7.3]
        K[LexiKernel]
    end
    subgraph hw [Hardware]
        G[GPUs]
        N[NVMe, USB, NICs]
    end
    B --> P
    A --> H
    P --> H
    H --> S --> M
    M --> V & C & U
    P --> O
    O --> L & K
    V & C --> G
    L & K --> N
Repository layout
.
├── lexipanel-rs/
│   ├── crates/
│   │   ├── lexi/            Panel server and CLI tools
│   │   ├── lexi-gui/        Browser UI, compiled to WebAssembly
│   │   ├── installer/       Panel installer
│   │   ├── lexi-debugkit/   Support and boot diagnostics
│   │   ├── lexi-guard/      Tool permission gate
│   │   ├── lexi-hwinfo/     Hardware inventory
│   │   ├── lexi-vm/         VM support
│   │   └── xtask/           Build and release tasks
│   ├── engine/              LexiEngine workspace, 159 crates
│   ├── deploy/              Install scripts and packaging
│   └── third-party-licenses/
├── lexios/
│   ├── lexikernel/          LexiKernel: 99 crates
│   │   ├── crates/          Kernel subsystems
│   │   └── drivers/         NVMe, AHCI, xHCI, USB, virtio, NICs, GPU blocks
│   ├── tools/               LexiOS userland, 52 crates
│   ├── .lexios/             Policies, configuration, fixtures
│   └── third-party-licenses/
├── docs/                    Binary test fixtures read by the test suites
├── experimental/            Research code, not shipped
└── tools/                   Build helpers
Performance
Qwen3.8 27B on a Radeon RX 7900 XTX against the newest llama.cpp release (b12180, Vulkan, flash attention), measured
on 11/06/2026 on the same machine with the same harness: Intel i7-9700, XTX capped at 291 W, Linux 7.3, Q4_1 KV cache,
131,072-token context, one slot, no cache reuse, a random prefix on every prompt, idle box. Generation is tokens per
second after the first token, the median of three runs (68k is one request). Greedy output text is identical across
LexiEngine builds.
Headline: generation without speculation, short prompt
Generation (tok/s) at short / 3.6k / 21k / 68k tokens of context
Measured with the previous engine build c5dd9d0e; the engine in this source is faster again at short prompts
(table above), and its full table follows in the next update.
Prompt processing (tok/s) at 3.6k / 21k / 68k tokens (LexiEngine c5dd9d0e vs llama.cpp b12177)
LexiEngine is ahead of llama.cpp in every measured case. The gains of 11/06 came from removing a per-allocation host
cost that left the GPU idle about 4.7 ms per token, half-subgroup and 64-lane Q4_K/Q6_K and eight-lane IQ4_XS decode
kernels, a long-context decode attention kernel (68k keys: 1029 to 321 us per layer), a recycled decode activation pool,
fused FFN gate/up/SwiGLU passes and a split DeltaNet step. Decode is GPU-bound; the next target is about 80% of the
card's 960 GB/s without speculation (about 47 tok/s on Q4_K_M and 53 on IQ4_XS for short prompts).
7900 XTX: Qwen3 1.7B Q4_K_M, LexiOS from the USB image (11/04, before the 11/06 engine work)
Measured on 11/04/2026 (UTC) on a second 7900 XTX (Ryzen 9 5900X), LexiOS on Linux 7.3 booted from the USB stick,
through the Panel over the network. Same model and settings on both engines: 8,192-token context, f16 KV cache,
one slot, 256 generated tokens, three runs each. llama.cpp b12090 (Vulkan) installed by the Panel's engine installer.
On small models llama.cpp is 25-30% faster: at this speed LexiEngine's fixed per-token cost dominates. This is the
next performance target.
Status, 11/07/2026
- Development USB image with Secure Boot (Linux entry on 7.4-rc1): signed with the LexiSuite development certificate.
After that certificate is appended to the PC's db (the Microsoft keys stay), both menu entries boot with Secure Boot
on. Verified in a VM from an unenrolled state: LexiKernel first and second start (it creates and then reuses its
rollback-protection variable) and with an AMD IOMMU, Linux 7.4 to a working Panel, and refusals of a stick without
enrollment, a tampered rollback file and a tampered kernel. Not yet started on a physical Secure Boot PC.
- Upstream llama.cpp runs on LexiOS without third-party libraries: LexiOS ships original Rust implementations of the
runtime interfaces it loads (libgomp, libcrypto, libssl). llama.cpp b12180 against them gives identical greedy text
on CPU and on Vulkan and the same speed (within 1%), and HTTPS model downloads work through its own HTTP client,
with certificate verification. TLS older than 1.2, TLS 1.2 without extended master secret, client certificates and
encrypted private keys are refused with a clear error.
- On first boot the LEXIDATA partition and filesystem grow to fill the stick under either kernel, verified on a
physical stick and in a VM.
- Panel, tested in a real headless browser on both kernels. Defects found this way are fixed (uploads into system
folders, storage status on a fresh install, start-at-boot without systemd, engine start errors that now name the
missing library, chat sends before the model list loads, the consoles' Secure Boot rows, LexiKernel's console page
on Secure Boot images). On LexiKernel, features it does not provide say so in the GUI. Open: storage usage
measurement and CPU usage on LexiKernel.
- The Panel keeps a log of failed requests, so a debug kit records GUI failures.
- LexiKernel GPU: a native Rust AMD Navi 31 (RDNA3) driver is integrated as offline software and passes its mock and
kernel test suites. It has not run on hardware; GPU work under LexiKernel still uses the Linux driver-domain guest.
- The image is development-signed, not production-signed.
Models
Architectures served per backend, as reported by lexi-engine --accelerator-capabilities-json:
Measured here: Q4_K_M, IQ4_XS, Q8_0 and F16. Speculative decoding uses
the draft head embedded in MTP models. Also in the tree, at earlier stages: embeddings and reranking,
vision, speech, image generation and native quantization tools.
Quick start
Requirements
- Rust 1.100.0-beta.5 (the pinned toolchain the tests and the installer use; rustup toolchain install 1.100.0-beta.5)
- For the first build, network access so Cargo can fetch the locked dependencies (cargo fetch --locked)
- A Vulkan driver for AMD or Intel GPUs, or the CUDA runtime for NVIDIA
- glslc from the Vulkan SDK, for building the shaders
LexiEngine
cd lexipanel-rs/engine
GLSLC=/path/to/glslc cargo build --release -p lexi-engine-server \
    --features cuda,vulkan --bin lexi-engine
./target/release/lexi-engine serve \
    --backend vulkan --devices 0 \
    -m /path/to/model.gguf --alias local \
    -c 32768 --memory-budget-mib 23500 \
    --host 127.0.0.1 --port 8080
LexiPanel
cd lexipanel-rs
cargo build --release -p lexi
./target/release/lexi serve
Run this way, the Panel listens on 127.0.0.1:8094 (set LEXI_LISTEN to change it). On LexiOS and the USB image the
Panel is on port 8090 on every network interface.
A Linux or WSL developer install is also available:
deploy/install-linux.sh and
deploy/windows/install-wsl.ps1. The Linux script builds its installer
offline with the pinned toolchain, so run cargo fetch --locked in lexipanel-rs first.
Tests
Run tests with a throwaway HOME so they can't touch a live install, and leave lexipanel-installer out: its tests act on the machine.
# Engine
cd lexipanel-rs/engine && cargo test --release --workspace --lib
# Panel
cd lexipanel-rs && HOME=$(mktemp -d) cargo test --release --workspace --exclude lexipanel-installer
# LexiKernel and drivers
cd lexios && cargo test -p lk-iommu -p lk-cpu -p lk-pci -p lk-boundary -p lk-init \
    -p intel-nic -p realtek-nic -p xhci -p usb-class --lib --tests
cargo test -p lk-kernel --lib --features development-untrusted-boot
API
LexiEngine speaks the APIs existing clients already use.
curl http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local","stream":true,"messages":[{"role":"user","content":"Hello"}]}'
A request larger than the context window gets an HTTP 400 stating the reason, and the server keeps serving.
Hardware
Tested GPUs
LexiKernel requirements
- x86-64 with an active IOMMU: Intel VT-d or AMD-Vi. There is no boot without one, by design.
- xHCI USB.
- A supported network device, plugged in before boot.
The 2.5G RTL8125B driver runs on the chip's built-in microcode, and refuses other RTL8125 revisions.
Security model
- IOMMU required. Network drivers refuse to bind without isolated DMA.
- Rust first. 308 of 374 crate roots forbid unsafe outright.
- Fail closed. Unknown hardware revisions and unsupported shapes are refused, not guessed at.
- Authenticated Panel. One-time setup code, CSRF and origin checks on mutating requests.
- Key-only SSH on development images. The build carries a public key only. Release images refuse the option.
- Build-neutral binaries. Release builds remap paths, and media builds are scanned for private strings.
Status
LexiSuite is in active development and is not a generally available release. This section is kept honest on purpose.
Last test runs
On commit a7df5635, 11/03/2026, all passing:
Proven
- Qwen3.8 27B on the 7900 XTX at or above llama.cpp speed with draft-head speculation (see Performance).
- LexiKernel boots on real hardware. On 11/03/2026 it booted a Lenovo ThinkPad P71 (i7-7700HQ) from USB, brought
up the network, served the Panel to another machine and showed the local console.
- On LexiKernel, the Panel's Start button runs the engine and a chat completes, in QEMU with the same CPU flags as
that laptop.
- Linux 7.3 and LexiKernel boot from one image.
Not yet proven
- GPU inference on LexiKernel on real hardware. LexiKernel drives GPUs only through a Linux guest in QEMU so far.
- The RTL8125B driver has never run on a real chip.
Known gaps
- Plain generation (no draft head) at long context trails llama.cpp by up to 11% on the 27B.
- LexiKernel runs all of a process's threads on one CPU, so CPU inference there is far slower than on Linux.
- Most of the Panel's System pages call Linux tools that LexiKernel doesn't provide yet, and one engines page stops
the Panel there until it restarts.
- A client disconnect doesn't yet cancel a non-streaming request.
License
Free for public, private, personal and educational use. Commercial use is US$100 per instance per year, which
includes support and priority fixes for problems specific to your hardware and setup. There are no licence keys or
usage checks: commercial users are trusted to buy what they use. The source code remains proprietary. See
LICENSE.
Copyright (c) 2026 LexiPanel.
Third-party components keep their own licences. See lexios/THIRD_PARTY_NOTICES.md,
lexipanel-rs/engine/THIRD_PARTY_NOTICES.md and the
third-party-licenses directories. Linux 7.3, included in LexiOS images, is licensed under GPL-2.0.
OS / Kernel / Engine / Panel. All Rust.
