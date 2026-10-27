---
id: "c5f7c50d4d1a0a71"
title: "How to use Q8 ngram with lower quant Qwen 3.8 Flash Next in Strata and avoid errors"
url: "https://reddit.com/r/LocalLLaMA/comments/1xglhtx/how_to_use_q8_ngram_with_lower_quant_qwen_38"
link: "https://reddit.com/r/LocalLLaMA/comments/1xglhtx/how_to_use_q8_ngram_with_lower_quant_qwen_38"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T06:54:21Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["citrusalex"]
language: "en"
summary: "Supposedly, you can increase output quality/\"intelligence\" of Qwen Flash Next quants somewhat (using Strata) without increase in VRAM, system memory usage or sacrificing prefill/decode speed (when using ple-io=direct) by side-loading a higher quality ngram, in this case Q8 . You do this with the following option: --ple-gguf=/path/to/ngram.gguf or, if running Strata in Docker, by adding this…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: []
content_source: "post"
word_count: 233
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xglhtx/how_to_use_q8_ngram_with_lower_quant_qwen_38/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# How to use Q8 ngram with lower quant Qwen 3.8 Flash Next in Strata and avoid errors

Reddit · citrusalex · 2026-10-27

Supposedly, you can increase output quality/"intelligence" of Qwen Flash Next quants somewhat (using Strata) without increase in VRAM, system memory usage or sacrificing prefill/decode speed (when using ple-io=direct) by side-loading a higher quality ngram, in this case Q8 . You do this with the following option: --ple-gguf=/path/to/ngram.gguf or, if running Strata in Docker, by adding this envar to the compose file: STRATA_SET: "ple-gguf=/path/to/ngram.gguf" However, if you just feed Strata the original ngram gguf straight from hugging face (in my case unsloth's Q8 ngram while using their IQ4_XS quant), it will error out complaining about architecture mismatch. To fix this, you need to make a simple metadata change just to the ngram gguf file. Either download a pre-edited gguf: https://ciscai-gguf-editor.hf.space/download/unsloth/Qwen3.8-Flash-Next-GGUF/Q8_0/Qwen3.8-Flash-Next-Q8_0-00003-of-00006.gguf?add=%5B%22general.architecture%22,8,%22strata-ple%22%5D or, using gguf-editor-gui from gguf python package, add general.architecture key with STRING type and a value of strata-ple . It will bypass Strata's (unnecessary IMO) checks and successfully load the ngram. I must make a disclaimer that I have not verified whether this actually makes the model smarter myself nor were my speed/resource usage impact checks thorough, but the logic behind using a higher precision ngram seems reasonable, and if you can spare the storage space it seems like a no-brainer decision. You can do the same with an even larger BF16 ngram , but from what I've heard the difference is basically not perceivable and it's not worth wasting 50GBs more of storage.
