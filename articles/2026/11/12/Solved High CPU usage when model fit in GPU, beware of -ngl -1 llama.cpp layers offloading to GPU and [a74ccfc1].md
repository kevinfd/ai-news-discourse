---
id: "a74ccfc1cdbd7d4a"
title: "Solved High CPU usage when model fit in GPU, beware of -ngl -1 llama.cpp layers offloading to GPU and llama-fit-param"
url: "https://reddit.com/r/LocalLLaMA/comments/1xun196/solved_high_cpu_usage_when_model_fit_in_gpu"
link: "https://reddit.com/r/LocalLLaMA/comments/1xun196/solved_high_cpu_usage_when_model_fit_in_gpu"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T20:00:08Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["randomjapaneselearn"]
language: "en"
summary: "I'm trying to figure out how much context i can use on my 3090 (full compute, monitor is on mobo). If i launch: llama-bin-win-cuda-13.4-x64\\llama-fit-params.exe --model modelli\\Swift-1.5-Qwen3.8-27B-Q4_K_M.gguf -ctk q8_0 -ctv q8_0 -ngl -1 -fa on -np 1 -b 4096 -ub 1024 I get: -c 150272 -ngl -1 but if i launch real llama.cpp with lower context: llama-bin-win-cuda-13.4-x64\\llama-server.exe…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "models & research", "products & launches"]
content_source: "post"
word_count: 395
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xun196/solved_high_cpu_usage_when_model_fit_in_gpu/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Solved High CPU usage when model fit in GPU, beware of -ngl -1 llama.cpp layers offloading to GPU and llama-fit-param

Reddit · randomjapaneselearn · 2026-11-12

I'm trying to figure out how much context i can use on my 3090 (full compute, monitor is on mobo). If i launch: llama-bin-win-cuda-13.4-x64\llama-fit-params.exe --model modelli\Swift-1.5-Qwen3.8-27B-Q4_K_M.gguf -ctk q8_0 -ctv q8_0 -ngl -1 -fa on -np 1 -b 4096 -ub 1024 I get: -c 150272 -ngl -1 but if i launch real llama.cpp with lower context: llama-bin-win-cuda-13.4-x64\llama-server.exe --verbose --log-file log.txt --host 0.0.0.0 --port 9931 --model modelli\Swift-1.5-Qwen3.8-27B-Q4_K_M.gguf --ctx-size 131072 -ctk q8_0 -ctv q8_0 -ngl -1 -fa on --spec-type draft-mtp --spec-draft-n-max 2 -np 1 -b 4096 -ub 1024 --jinja From the log, matches for "offloaded" with "-ngl -1": Line 2200: load_tensors: offloaded 66/66 layers to GPU Line 5935: load_tensors: offloaded 66/66 layers to GPU Line 8273: load_tensors: offloaded 0/66 layers to GPU Line 12009: load_tensors: offloaded 66/66 layers to GPU Line 15746: load_tensors: offloaded 64/66 layers to GPU Line 19484: load_tensors: offloaded 65/66 layers to GPU Line 23226: load_tensors: offloaded 64/66 layers to GPU <-- (actual used vlaue, slow loading because copying data) So even if i use 131k context wich is less than the 150k suggested it doesn't offload all layers and i have high cpu usage for any prompt. IF I CHANGE -NGL FROM -1 TO "ALL" I GET THIS: matches for "offloaded" with "-ngl all" Line 2200: load_tensors: offloaded 66/66 layers to GPU Line 5935: load_tensors: offloaded 66/66 layers to GPU Line 8276: load_tensors: offloaded 66/66 layers to GPU <-- AND NO MORE CPU USAGE!! (same if i write 99 or 999 but it's ugly) It gets more confusing: if i write in llama fit -ngl all instead of -1 it gives a "-2" in output. there is an entry in the log when i used "all": common_fit_params: failed to fit params to free device memory: n_gpu_layers already set by user to -2, abort Conclusion: Seems that -ngl -1 means "auto" while -2 means "all", but if you have high cpu usage in a model that theorically fit in the GPU use "all". This alone changed t/s generation from 60 to 76 for completeness here is the --help from llama.cpp for "ngl" parameter: -ngl, --gpu-layers, --n-gpu-layers N max. number of layers to store in VRAM, either an exact number, 'auto', or 'all' (default: auto) And here it gets even more confusing because the help talks about "MAX" number of layers to offload so according to this help it's an upper limit not a lower limit...
