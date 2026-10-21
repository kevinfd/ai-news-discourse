---
id: "b0ff76934a76a39a"
title: "I built an RK3588 NPU runtime without any proprietary inference libraries: Qwen3.5-4B at ~10 tok/s, ~2x faster than vendor SDK."
url: "https://reddit.com/r/LocalLLaMA/comments/1xb45bq/i_built_an_rk3588_npu_runtime_without_any"
link: "https://reddit.com/r/LocalLLaMA/comments/1xb45bq/i_built_an_rk3588_npu_runtime_without_any"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T21:03:58Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Flashy_Squirrel4745"]
language: "en"
summary: "If you have an RK3588 board, here’s another way to put its NPU to work. I made open_rknpu2_lm_infer, a local LLM inference engine for the Rockchip RK3588 NPU. It runs without Rockchip’s proprietary userspace inference libraries. The upper part is written in Rust and the NPU operators are coded with C++. No black-box, you can actually read, modify, and hack the host inference code and NPU…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: []
content_source: "post"
word_count: 219
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xb45bq/i_built_an_rk3588_npu_runtime_without_any/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built an RK3588 NPU runtime without any proprietary inference libraries: Qwen3.5-4B at ~10 tok/s, ~2x faster than vendor SDK.

Reddit · Flashy_Squirrel4745 · 2026-10-20

If you have an RK3588 board, here’s another way to put its NPU to work. I made open_rknpu2_lm_infer, a local LLM inference engine for the Rockchip RK3588 NPU. It runs without Rockchip’s proprietary userspace inference libraries. The upper part is written in Rust and the NPU operators are coded with C++. No black-box, you can actually read, modify, and hack the host inference code and NPU operator execution. And now supports Qwen3.5-4B with image input and optional MTP speculative decoding. And it's fast! Github: https://github.com/happyme531/open_rknpu2_lm_infer Quick comparison against RKLLM 1.3.1 Qwen3.5-4B test RKLLM 1.3.1 open_rknpu2_lm_infer MTP1 Prefill, 512-token prompt 58.35 tok/s 147.83 tok/s Prefill, 3,800-token prompt 54.03 tok/s 139.92 tok/s Decode after 512 tokens 5.54 tok/s 10.61 tok/s Decode after 3,800 tokens 4.57 tok/s 9.90 tok/s Current features: Terminal chat or an OpenAI-compatible API, with streaming, tool calling, and prefix caching. Qwen3.5-4B image input, alongside text inference. Validated checkpoints for Qwen3-4B, Qwen3.5-4B, Granite-4.2-3B, and MiniCPM5-2B. Prebuilt ARM64 Linux binaries and links to quantized models. Incoming features: DFlash and DSpark speculation MiniCPM-V 4.7 35a3 with expert prefetching If you have an RK3588 board, I’d love to compare results across boards and RAM configurations. Share your board, driver version, model, and speeds—or open an issue if something breaks. If you try it and find it useful, I’d appreciate a GitHub star!
