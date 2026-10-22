---
id: "25a07f553bdf3c3e"
title: "Made a quant: Swift 1.5 Qwen 3.8 Flash Next - Heretic - Unsloth Dynamic IQ4_XS"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbweuw/made_a_quant_swift_15_qwen_38_flash_next_heretic"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbweuw/made_a_quant_swift_15_qwen_38_flash_next_heretic"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T19:11:31Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["jjusko20"]
language: "en"
summary: "Really couldn't find any good existing quantization for this, only uncensored editions for the GSQ-RCO versions, so I made one. Strata is pre configured for the unsloth dynamic iq4_xs build. Sorry the model card is so cornbally This is the full precision swift 1.5 with the heretic method applied quantized down to iq4_xs. The tensor profile has been extracted from the regular UD-IQ4_XS gguf from…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 122
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbweuw/made_a_quant_swift_15_qwen_38_flash_next_heretic/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Made a quant: Swift 1.5 Qwen 3.8 Flash Next - Heretic - Unsloth Dynamic IQ4_XS

Reddit · jjusko20 · 2026-10-21

Really couldn't find any good existing quantization for this, only uncensored editions for the GSQ-RCO versions, so I made one. Strata is pre configured for the unsloth dynamic iq4_xs build. Sorry the model card is so cornbally This is the full precision swift 1.5 with the heretic method applied quantized down to iq4_xs. The tensor profile has been extracted from the regular UD-IQ4_XS gguf from qwen 3.8 flash next, and applied to this quant. The model was quantized with an imatrix covering math, code, english language, general instruct, and tools, generated for this model against a small custom dataset. Just IQ4_XS right now because that's what I needed but feel free to request new formats. Copying unsloth quants is pretty easy. https://huggingface.co/trubisky/Swift-1.5-Qwen-3.8-Flash-Next-Heretic-UD-IQ4_XS
