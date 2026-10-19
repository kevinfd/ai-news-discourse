---
id: "4e94f4024cd8f966"
title: "Strata - Windows - working dual AMD GPU setup with VISION !"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9qe2h/strata_windows_working_dual_amd_gpu_setup_with"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9qe2h/strata_windows_working_dual_amd_gpu_setup_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T07:29:30Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Ok-Importance-3529"]
language: "en"
summary: "Hi, just want to say that i ran strata on Windows 11 with layer split on dual AMD GPUs 9070XT and 9060XT, 14900KF processor and 64GB RAM. Only problem i encountered was that without \"STRATA_RESIDENT_PIN\": \"0\" it crashed, but with this env on it was running fine, though it was having a little overhead and slowdown. Finally i settled on single card setup 9070XT with ~1350pp and around ~50-100 tgs…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: ["chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 237
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9qe2h/strata_windows_working_dual_amd_gpu_setup_with/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata - Windows - working dual AMD GPU setup with VISION !

Reddit · Ok-Importance-3529 · 2026-10-19

Hi, just want to say that i ran strata on Windows 11 with layer split on dual AMD GPUs 9070XT and 9060XT, 14900KF processor and 64GB RAM. Only problem i encountered was that without "STRATA_RESIDENT_PIN": "0" it crashed, but with this env on it was running fine, though it was having a little overhead and slowdown. Finally i settled on single card setup 9070XT with ~1350pp and around ~50-100 tgs (depending on task) at full ctx , qwen sampling and IQ3_XXS quant. Also i compiled vulkan vision and run vision mmproj on my second card all on Windows without any problems. Config is here: { "exe": "E:\\Strata\\engine\\strata.exe", "args": [ "--pack", "C:\\Strata-data\\packs\\iq3_xxs", "--native", "C:\\Strata-data\\models\\IQ3_XXS\\Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00001-of-00002.gguf", "--ple-gguf", "C:\\Strata-data\\models\\IQ3_XXS\\Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00002-of-00002.gguf", "--expert-profile", "E:\\Strata\\data\\expert-profile.bin", "--expert-cache", "auto", "--prefill", "auto", "--spec", "4", "--spec-min-p", "0.5", "--mtp", "C:\\Strata-data\\mtp\\rt", "--max-context", "262144", "--kv", "int8", "--resident-experts", "--pool-workers", "15", "--vram-reserve-mib", "2300", "--kv-resident", "32768" ], "cwd": "E:\\Strata", "tokenizer": "C:\\Strata-data\\packs\\iq3_xxs\\tokenizer", "model_name": "qwen3.8-flash-next-iq3_xxs", "log": "E:\\Strata\\strata-iq3_xxs.log", "lib_dirs": [ "E:\\Strata\\engine\\rocm\\bin" ], "port": 8080, "backend": "hip", "env": { "GGML_VK_VISIBLE_DEVICES": "1", "STRATA_PREFILL_CPU_SHARE" : "auto", "STRATA_STAGER_THREADS": "8", "STRATA_PF_FUSED": "1", "STRATA_PF_GEMM" : "1", "STRATA_HIP_WMMA": "1", "STRATA_HIPBLASLT_TUNING": "E:\\Strata\\tools\\hip\\gfx1201-hipblaslt-100500.txt", "STRATA_IQ256_GATHER": "1" }, "sampling": { "temperature": 1.0, "top_p": 0.95, "top_k": 20, "min_p": 0.0 }, "vision": { "exe": "E:\\Strata\\build-vision-vk\\bin\\strata-vision.exe", "mmproj": "C:\\Strata-data\\models\\IQ3_XXS\\mmproj-Qwen3.8-Flash-Next-BF16.gguf", "model": "C:\\Strata-data\\models\\IQ3_XXS\\Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00001-of-00002.gguf", "gpu": true, "max_tokens": 1024 }, "gpu": "1", "gpu_order": "as_given", "gpus_asked": true } Officially windows isnt supported for dual amd gpus, vision on windows also not supported, both run fine on my setup without any modifications to the strata code. Good job team.
