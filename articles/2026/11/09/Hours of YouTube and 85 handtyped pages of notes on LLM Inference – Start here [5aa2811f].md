---
id: "5aa2811f45ceef64"
title: "Hours of YouTube and 85 handtyped pages of notes on LLM Inference – Start here"
url: "https://github.com/samir-sarwar/samir-vllm"
link: "https://github.com/samir-sarwar/samir-vllm"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T11:36:55Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["samirswr"]
language: "en"
summary: "Teaching LLM inference from first principles by building a small engine in C++ and CUDA.\nThe series follows what happens between a prompt and a generated token, from loading model weights to running each part of the transformer on the GPU.\nRead Inference from Scratch (PDF) for 80+ pages of my handwritten notes and diagrams. I developed all of the writing in this PDF myself, with NO AI…"
tags: []
orgs: ["Meta", "Nvidia"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1210
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50424199"
score: 11
comments: 0
community: "Hacker News"
---

# Hours of YouTube and 85 handtyped pages of notes on LLM Inference – Start here

GitHub · samirswr · 2026-11-09

Teaching LLM inference from first principles by building a small engine in C++ and CUDA.
The series follows what happens between a prompt and a generated token, from loading model weights to running each part of the transformer on the GPU.
Read Inference from Scratch (PDF) for 80+ pages of my handwritten notes and diagrams. I developed all of the writing in this PDF myself, with NO AI writing.
Companion notes for every video are in the study-notes index, with separate Markdown and PDF folders. You can also read the complete PDF collection.
- A C++17 / CUDA project, built with CMake and linked with ICU for Unicode-aware tokenization.
- Direct model.safetensors loading: parse metadata, validate tensor offsets, and copy the raw BF16 weights to GPU memory. There is also a memory-mapped loader implementation to avoid an extra CPU-side copy.
- A fixed Llama 3.2 1B Instruct weight layout, with direct pointers to the embedding, normalization, attention, and MLP tensors across all 16 layers.
- A local BPE tokenizer that supports Unicode, special tokens, encode/decode, and the Instruct chat prompt format; its expected output is covered by a dedicated test executable.
- A CUDA embedding-gather kernel and prefill path that copies prompt token IDs to the GPU and allocates activations.
- A CUDA RMSNorm kernel for the 2,048-wide hidden state: it reduces in FP32 and applies the learned BF16 weights throughout the forward pass.
- Dense causal prefill now runs all 16 layers: Q/K/V projection, RoPE, grouped-query attention, output projection, the attention residual, post-attention RMSNorm, SwiGLU MLP, and the MLP residual.
- The final RMSNorm and tied embedding/LM-head projection produce FP32 logits; GPU argmax selects each next token.
- A shared BF16 KV page pool with a block table per sequence and layer. Each physical page holds 16 tokens of K and V; prefill fills prompt pages and decode appends one new token at its absolute RoPE position.
- Greedy response generation with Instruct chat formatting, end-of-turn/end-of-text stopping, and configurable output length within the 2,048-token context.
- Persistent scratch buffers and one cuBLAS handle shared by prefill and decode. Q storage is reused for output/MLP projections, and normalization storage is reused for attention output.
- Batched decode with runtime-sized buffers, packed projections, and separate KV page mappings and attention lengths per sequence. Request count does not enlarge the KV pool.
- Static batching and a continuous scheduler that admit queued prompts according to available page budgets, then return their pages and budgets on completion.
- Direct paged decode attention with FP32 online softmax. Each query head streams its sequence's cached pages and accumulates weighted values without gathering a contiguous prefix or storing attention scores.
Part 8 explains Prefill, Decode, and the KV Cache. Part 9 follows with Static and Continuous Batching, including the current paged cache and online-softmax decode attention.
The Llama 3.2 1B inference path includes dense causal prefill, paged decode attention, and static or continuous batching. Model dimensions and the 2,048-token context remain fixed for this learning engine. The KV pool defaults to 128 MiB and can be set with --kv-cache-mib N; active request capacity follows the workload's page budgets rather than a fixed two-request limit.
Admission guarantees room for each request's maximum processed prefix: prompt_tokens + allowed_new_tokens - 1, rounded up to 16-token pages in each of the 16 layers. The allowed output budget is clamped to the context limit, and the final predicted token is returned without being processed again. These admission credits are separate from physical pages, which are assigned lazily. Early completion releases both the assigned pages and the remaining credits.
Requests wait in FIFO order when their budgets cannot fit alongside active requests. Active requests have room to finish, so future page-boundary growth cannot exhaust the pool or deadlock generation. A request whose budget exceeds the entire pool is rejected with a clear error. This conservative policy avoids preemption and recomputation; a large requested output budget can limit concurrency even if the model eventually stops early.
--stats reports the pool size, peak active requests, largest decode batch, peak assigned pages, admission waits, and final free-page count. Prefill still processes one prompt at a time between decode iterations.
BF16 computations can round differently at different batch sizes. When vocabulary logits are nearly tied, greedy output tokens can therefore differ between individual and batched runs. Bitwise output equality across batch sizes is not guaranteed.
- A CUDA-capable NVIDIA GPU and CUDA Toolkit
- CMake 3.24+
- A C++17 compiler
- ICU development libraries
- The nlohmann/json header
- Model weights at models/llama-3.2-1b-instruct/model.safetensors
- The matching tokenizer at models/llama-3.2-1b-instruct/tokenizer.model (copy it from models/Llama-3.2-1B-Instruct/original/tokenizer.model)
mkdir -p models/llama-3.2-1b-instruct
cp models/Llama-3.2-1B-Instruct/original/tokenizer.model models/llama-3.2-1b-instruct/
cmake -S . -B build
cmake --build build -j
./build/samir-vllm "Explain the KV cache in two sentences." 128
# Continuous batching (default): admit requests whose page budgets fit.
./build/samir-vllm "Say hello." 64 "Explain the KV cache." "What is RoPE?"
# Static batching: wait for the current group before admitting more.
./build/samir-vllm --static "Say hello." 64 "Explain the KV cache." "What is RoPE?"
# More than two requests share the same default 128 MiB pool.
./build/samir-vllm --stats "Explain paging." 64 "Explain GQA." "Explain RoPE." "Explain softmax."
# A smaller pool queues requests when their declared budgets cannot fit together.
./build/samir-vllm --kv-cache-mib 8 --stats "Explain paging." 64 "Explain GQA." "Explain RoPE."
./build/tokenizer-test models/llama-3.2-1b-instruct/tokenizer.model
After optional --static, --continuous, --kv-cache-mib N, and --stats flags, the first argument is a prompt and the second is max_new_tokens (default: 128). Any remaining arguments are additional prompts; the token budget applies to each request. Every prompt is formatted as an Instruct user message. Generation stops independently at EOS, EOT, or EOM, or the output/context limit, and each completed response is printed with its token IDs and request number.
Prompts are prefilled one at a time, pausing decode. Each decode step packs one token from every active sequence into the shared buffers. Attention reads only that sequence's cache; requests can have different prompt and output lengths. Continuous batching admits waiting requests when page credits become available, while static batching admits the next group after the current group finishes.
src/           Engine entry point, CUDA kernels, and tokenizer implementation
include/       Public kernel and tokenizer headers
tests/         Tokenizer tests
python/        Tokenizer reference script
proper_notes/  Study-notes index, markdown/ sources, and pdf/ reading editions
scripts/       Rebuild the study-note PDFs
notes.md       Working notes from the build
The engine source code in src/, include/, tests/, and python/, along with CMakeLists.txt, .gitignore, and this README, is licensed under the MIT License.
The notes in proper_notes/, notes.md, and podLibraryInstall.md, along with handwritten notes, scans, illustrations, photographs of notes, and PDFs provided with this project, are all rights reserved and excluded from MIT. Personal reading and study are permitted. Redistribution, republication, rehosting, resale, or distribution of adapted versions requires prior written permission, whether offered for free or for payment. See LICENSE-NOTES for the full terms and exceptions.
Public repositories can still be viewed and forked within GitHub under GitHub's Terms of Service.
Built with Llama. The bundled Llama 3.2 tokenizer and any separately downloaded Llama 3.2 weights retain Meta's Llama 3.2 Community License and Acceptable Use Policy. They are excluded from MIT. Keep the agreement, policy, and attribution notice with any redistributed Llama materials.
Third-party dependencies, including CUDA, cuBLAS, ICU, and nlohmann/json, retain their respective licenses.
