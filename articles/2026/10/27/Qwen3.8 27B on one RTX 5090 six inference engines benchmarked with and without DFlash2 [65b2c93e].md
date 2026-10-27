---
id: "65b2c93e78522d4c"
title: "Qwen3.8 27B on one RTX 5090: six inference engines benchmarked with and without DFlash2"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgkzb9/qwen38_27b_on_one_rtx_5090_six_inference_engines"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgkzb9/qwen38_27b_on_one_rtx_5090_six_inference_engines"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T06:20:34Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["fuzhongkai"]
language: "en"
summary: "Disclosure: I’m the author of TensorSharp. This English summary was adapted and edited with LLM assistance from the full benchmark report . The comparison covers llama.cpp, vLLM, SGLang, NInfer, velox-inferer, and TensorSharp on the same RTX 5090 32 GB, including decode throughput, long prompts, concurrent requests, image input, and a small tool loop. Setup: Ubuntu 24.04, EPYC 9354, one engine…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 622
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgkzb9/qwen38_27b_on_one_rtx_5090_six_inference_engines/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8 27B on one RTX 5090: six inference engines benchmarked with and without DFlash2

Reddit · fuzhongkai · 2026-10-27

Disclosure: I’m the author of TensorSharp. This English summary was adapted and edited with LLM assistance from the full benchmark report . The comparison covers llama.cpp, vLLM, SGLang, NInfer, velox-inferer, and TensorSharp on the same RTX 5090 32 GB, including decode throughput, long prompts, concurrent requests, image input, and a small tool loop. Setup: Ubuntu 24.04, EPYC 9354, one engine running at a time. All requests used greedy decoding with thinking off. Context was configured at 40,960 tokens per sequence, with tested prompts up to approximately 32K. TensorSharp used its direct-CUDA backend, --backend cuda . Before the numbers, the main qualification: the engines used different quantized checkpoints, drafters, and KV formats. TensorSharp / llama.cpp: the same NVFP4 GGUF target and Q4_K_M DFlash2 drafter. vLLM / SGLang: NVIDIA’s NVFP4/FP8 safetensors target and an FP8 drafter. NInfer / velox: a mixed NVFP4/FP8 .ninfer target and Q8 drafter. The results describe those complete configurations. They don’t isolate the performance of the runtime code alone. Throughput All figures below are tokens per second. Engine Single request, plain Single request, DFlash2 Four requests, DFlash2 — total NInfer 77.0 280.5 488 vLLM 69.4 247.8 304 velox-inferer 68.8 234.9 303 SGLang 78.5 234.5 251* TensorSharp 80.0 234.4 445 llama.cpp 84.2 212.9 259 The single-request figures average the code, prose, and passage-copy scenario medians. The last column comes from a separate concurrent-request workload and reports aggregate throughput , not throughput per request. For SGLang with DFlash2, only two active request lanes fit in 32 GB, so some of the four submitted requests queued. vLLM’s speculative configuration required GPU-memory utilization to be set to 0.97. NInfer led speculative decoding and concurrent throughput. llama.cpp had the highest measured plain decode rate. TensorSharp, SGLang, and velox were effectively tied at 234–235 tok/s with DFlash2. For TensorSharp, the most encouraging throughput result was 445 total tok/s across four requests . NInfer still led that workload at 488. Latency results 32K prompts: NInfer measured 3.02 s TTFT without speculation and 3.07 s with DFlash2 . TensorSharp measured 3.96 → 4.07 s . llama.cpp measured 5.01 → 8.16 s , showing a larger initial-latency cost from enabling speculation in this configuration. Screenshot input: On a 1344×768 screenshot without speculation, TensorSharp measured 125 ms TTFT and vLLM 127 ms . Those are effectively tied. With DFlash2, TensorSharp measured 142 ms , followed by NInfer at 163 ms . Four-turn tool loop: With DFlash2, end-to-end times were: TensorSharp: 0.748 s SGLang: 0.791 s llama.cpp and NInfer: 0.817 s velox-inferer: 1.42 s vLLM: 1.45 s This was a controlled loop with locally answered file-listing, file-reading, and calculator calls. It establishes a result for that workload; browser automation and longer agent tasks would need separate tests. Method and limitations Each scenario had three measured repetitions after warm-up. Timing was measured from the client over localhost HTTP streaming, so TTFT includes request handling, templating, tokenization, and prefill. Unique prompt nonces prevented reuse across independent requests; multi-turn and tool-loop tests intentionally reused prefixes. The report observed up to about 4% decode variation between runs. I’d treat differences below roughly 5% as inconclusive here. The harness also checked responses. velox failed the JSON-schema case in all three repetitions in both modes. NInfer with DFlash2 produced an empty JSON key in one of three JSON-object replies. The other checks passed, but these were limited functional checks, and quality equivalence across the quantizations was not evaluated . Thinking mode, non-greedy sampling, concurrency above four, and prompts beyond 32K remain untested. Exact engine revisions, model files, and launch settings are documented in the report. If you use one of these engines on a 5090 and spot a configuration that materially disadvantages it, I’d appreciate the specific setting and why you would change it . TensorSharp source
