---
id: "987d7c178614d5bb"
title: "Qwen3.8FN vLLM vs. llama.cpp vs Ninfer6000"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6wtqd/qwen38fn_vllm_vs_llamacpp_vs_ninfer6000"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6wtqd/qwen38fn_vllm_vs_llamacpp_vs_ninfer6000"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T20:34:35Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["dboybaker"]
language: "en"
summary: "I saw u/lkarlslund 's post just over a week ago regarding Ninfer6000 (a fork of Ninfer specifically tuned for 6000 blackwell and Qwen3.8-Flash-Next) and figured \"Hey I'm an idiot & bought one of those and I primarily use that model, lets try it\". I have a full blog post about it on my little site , but to summarize: tl;dr: Decode is incredible Prefill trails vLLM but is close enough its an…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 643
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6wtqd/qwen38fn_vllm_vs_llamacpp_vs_ninfer6000/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8FN vLLM vs. llama.cpp vs Ninfer6000

Reddit · dboybaker · 2026-10-15

I saw u/lkarlslund 's post just over a week ago regarding Ninfer6000 (a fork of Ninfer specifically tuned for 6000 blackwell and Qwen3.8-Flash-Next) and figured "Hey I'm an idiot & bought one of those and I primarily use that model, lets try it". I have a full blog post about it on my little site , but to summarize: tl;dr: Decode is incredible Prefill trails vLLM but is close enough its an overall win I didn't match the almost 400tok/s from the post, but got close in small idealized conditions so I imagine my test just differed. Accuracy benchmarks basically equal I'm seeing some major tool calling formatting issues in real world use Models/engines: Engine Model vLLM nvidia/Qwen3.8-Flash-Next-NVFP4 Ninfer6000 swift_1_5_qwen3_8_flash_next_nvfp4_fp8ple_fp8proj.ninfer llama.cpp unsloth/Qwen3.8-Flash-Next-GGUF/UD-Q4_K_XL Hardware: Rtx Pro 6000 Blackwell @ 600w, 96gb ddr4 @ 3000mhz, Ryzen 5 5600x Decode tps: visual Prompt Ninfer6000 vLLM nvfp4 llama.cpp Q4_K_XL N vs vLLM N vs llama.cpp ~1k 232 159 138 1.46x 1.68x 7.2k 241 148 129 1.63x 1.87x 28.6k 227 150 112 1.51x 2.02x 57.1k 249 149 93 1.68x 2.67x 114.1k 240 144 65 1.66x 3.70x mean 238 150 108 1.59x 2.21x Prefill tps & TTFT: visual Prompt Ninfer6000 prefill vLLM prefill llama.cpp prefill Ninfer TTFT vLLM TTFT llama.cpp TTFT ~1k 4,315 6,944 1,823 0.23 s 0.17 s 0.56 s 7.2k 7,996 16,484 2,960 0.90 s 0.44 s 2.44 s 28.6k 9,521 16,798 3,320 3.00 s 1.70 s 8.61 s 57.1k 9,914 16,700 3,277 5.76 s 3.42 s 17.42 s 114.1k 10,037 16,229 3,108 11.37 s 7.03 s 36.70 s The speed gains are real. Substantial decode gain over vLLM, but a prefill loss. Colossal decode and prefill gain over llama.cpp. Benchmarks: visual Benchmark Samples Ninfer6000 vLLM nvfp4 llama.cpp Q4_K_XL Spread Tool calling (BFCL v4) 300 76.67 ± 5.21 74.56 ± 0.96 73.00 ± 2.96 3.7 Instruction following (IFEval, prompt-strict) 250 82.80 ± 1.06 84.93 ± 0.61 84.93 ± 0.61 2.1 Knowledge (MMLU-Pro) 420 84.13 ± 0.77 83.65 ± 0.73 84.92 ± 0.69 1.3 Code (HumanEval+) 164 93.29 ± 0.61 94.92 ± 0.35 93.90 ± 1.22 1.6 Code (MBPP+) 378 94.80 ± 0.31 95.15 ± 1.07 95.59 ± 0.76 0.8 Long-form (Arena-Hard) 75 81.48 76.07 77.42 5.41 Long context (RULER, 4k to 257k) 290 98.28 99.14 98.97 0.9 The benchmarks were extremely close, only a small gap in tool calling in favor of the Ninfer6000 setup was beyond noise. Needle in a haystack (RULER): visual Haystack Actual prompt tokens Ninfer6000 vLLM nvfp4 llama.cpp Q4_K_XL Spread Items 4,096 4,820 98.89 100.00 98.89 1.11 45 16,384 18,910 98.89 100.00 98.89 1.11 45 32,768 37,754 98.75 100.00 100.00 1.25 40 65,536 75,294 98.75 98.75 98.75 0.00 40 131,072 150,371 97.50 98.75 98.75 1.25 40 180,000 206,418 97.50 97.50 98.75 1.25 40 224,000 256,827 97.50 98.75 98.75 1.25 40 all 290 - 98.28 99.14 98.97 0.86 290 No issues with long context between the three. One big issue: Outside of the benchmarks I set all 3 against an in-harness test and found a crippling tool calling issue with Ninfer6000. It consistently malforms tool calls and ends up printing the text back instead of actually calling the tool. Example This wasn't isolated either. For the past week I have tried to use Ninfer6000 as my daily driver and it repeats this behavior constantly in both Open-WebUI and Cline where I've used it. I don't have this problem with llama.cpp or vLLM. I'm not sure if I and my configuration are at fault, or if there's an issue with the engine itself. Until I figure that out I'll have to keep using vLLM. I do think the reasoning efficiency gains with Swift1.5 tuning are fantastic though, worth alone if I can get it to fit nicely. Imo Ninfer6000 had the best pelican , despite failing the tool call initially and requiring me to tell it "bro you messed up another tool call, try again"
