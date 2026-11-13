---
id: "b19430df4313f879"
title: "MoE and expert offloading on llama, exllamav3, strata on 9070XT"
url: "https://reddit.com/r/LocalLLaMA/comments/1xun15v/moe_and_expert_offloading_on_llama_exllamav3"
link: "https://reddit.com/r/LocalLLaMA/comments/1xun15v/moe_and_expert_offloading_on_llama_exllamav3"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T20:00:04Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["willeyh"]
language: "en"
summary: "First off. I am by all means no expert, and excellent work has been done in the past few years that we all currently enjoy. Came over this post https://www.reddit.com/r/LocalLLM/comments/1x5mxcj/qwen3827b_on_a_single_rx_9070_xt_150_toks_on_code/ and wanted to try the engine on MoEs. I've been benchmarking MoE experts offloading for the past two days in different engines on ROCm for my RDNA4…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 453
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xun15v/moe_and_expert_offloading_on_llama_exllamav3/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# MoE and expert offloading on llama, exllamav3, strata on 9070XT

Reddit · willeyh · 2026-11-12

First off. I am by all means no expert, and excellent work has been done in the past few years that we all currently enjoy. Came over this post https://www.reddit.com/r/LocalLLM/comments/1x5mxcj/qwen3827b_on_a_single_rx_9070_xt_150_toks_on_code/ and wanted to try the engine on MoEs. I've been benchmarking MoE experts offloading for the past two days in different engines on ROCm for my RDNA4 9070XT 16GB vram card and 32 GB DDR4. I'd set a goal at 128K context, which is the base minimum for agentic work, without compaction all the time. I've kept the KV at Q8. (Q8_0/Q5_1 decreased performance on exllamav3). Drafter cache, if added, is at Q4. Some limitations need apply when limited on vram. Lets face it If you want any kind of context, and a decent Q4 quant, 16GB ain't gonna cut it. Hot experts cache like Strata, Exllmv3 and now recently llama.cpp have made this more feasible on the slower system memory bandwidth. My end goal was to do QFN on all three, but I wanted to start with the smaller 35B-A3B's first. So I did Ornith 1.5 and Qwen 3.6, wanted to do Gemma, but found no EXL3 quant with mul1 experts required for offloading on Exllamav3. Tested both without drafter, MTP and DFlash2 where applicable. Strata/PolyStrata configs are mostly auto generated from the setup script, but added resident pin and tail skip. And for the non-qfn model performed worse overall, even t/w. I might be doing something wrong, bench might be bad, who knows. Stratas own bench stops at 32K if I'm not mistaken. Now Qwen 3.8 Flash Next (ista coder version) runs great on my rig, see plots. But I was surprised on the prefill tanking on the 35B models. 1900 t/s at 16K but 700 t/s at 128K where both llamacpp and exllamav3 where within 100-200 t/s difference. Findings so far is quite promising, especially on exllamav3. I'd say quite usable even. | Model | Winner (quant / engine) | Prefill u/128k | Decode u/128k | | --- | --- | ---: | ---: | | Ornith 1.5 35B-A3B | EXL3 4.0 bpw, DFlash2 / ExLlamaV3 | 1 168 tok/s | 57.3 tok/s | | Qwen3.6-35B-A3B | EXL3 4.0 bpw, DFlash2 (2 drafts) / ExLlamaV3 | 1 246 tok/s | 71.6 tok/s | | Qwen3.8-Flash-Next Coder | IQ1_M / Polystrata nov-7, `--spec 2` | 1 572 tok/s | 44.0 tok/s | Forgive my rambling thoughts. If you want to read my technical findings, written by the unsung local hero Qwen 3.8 27B. They can be found with more graphs and tables at https://github.com/willeyh-git/moe-offload-bench Q4/4bpw quants are preferred, some benches have been made on 5bpw and 6bpw so you can compare. Bench-suite is based on Kapitsa https://www.reddit.com/r/LocalLLM/comments/1x5mxcj/qwen3827b_on_a_single_rx_9070_xt_150_toks_on_code/ and written in go.
