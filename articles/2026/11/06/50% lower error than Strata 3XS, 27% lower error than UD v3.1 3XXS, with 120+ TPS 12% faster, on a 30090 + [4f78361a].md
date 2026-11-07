---
id: "4f78361ad833c29b"
title: "50% lower error than Strata 3XS, 27% lower error than UD v3.1 3XXS, with 120+ TPS/ 12% faster, on a 30090 + 64GB"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpmzg7/50_lower_error_than_strata_3xs_27_lower_error"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpmzg7/50_lower_error_than_strata_3xs_27_lower_error"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T20:16:38Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Brief-Tap-6616"]
language: "en"
summary: "Hello everyone! Over the past few weeks since Strata came out, I had many requests to add Qwen Flash Next to LlamAmpere. It was some very impressive engineering, but the models originally shipped (3XS and 2XS) showed very poor quality (.17+ KLD for just the 3XS variant, which uses a far lighter compression formula than more common sources like Unsloth). My initial work had llamAmpere running 20%…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 273
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpmzg7/50_lower_error_than_strata_3xs_27_lower_error/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 50% lower error than Strata 3XS, 27% lower error than UD v3.1 3XXS, with 120+ TPS/ 12% faster, on a 30090 + 64GB

Reddit · Brief-Tap-6616 · 2026-11-06

Hello everyone! Over the past few weeks since Strata came out, I had many requests to add Qwen Flash Next to LlamAmpere. It was some very impressive engineering, but the models originally shipped (3XS and 2XS) showed very poor quality (.17+ KLD for just the 3XS variant, which uses a far lighter compression formula than more common sources like Unsloth). My initial work had llamAmpere running 20% faster and ~15% lower error, but testing was showing inferior results vs 4bpw Qwen 27b, so I did not find it worth releasing. I continued to make progress on the AmpereInteger+ quantization format (I will release an encoder soon), and Unsloth released their v3.1 which provided a great new base. Happily, LlamAmpere v0.6.3 is now available with a new model and quant updates that show significant speed and quality gains over other options. At a depth of 100K, QFN runs at ~120+ TPS, with prefill >3000/s through the first 100K. It is a 50% error reduction vs the version of QFN available for this card size a few days ago, and 27% vs UD's improved quant. https://preview.redd.it/wcumk817v10i1.png?width=1108&format=png&auto=webp&s=4c321fbbbf328cd95163ecc51a7d6587fa1308c7 I do have a 3XS class file that runs ~10% faster than the version above, but as it is only ~15% better quality than the original Strata 3bpw model, I don't recommend it. This will also work well for 12+64GB configs. As with Strata, your performance will depend on the speed of your CPU and RAM as well. I do not recommend any quant of QFN for configs under 54GB of total memory, but you can always try the coder pruned variants as well. Enjoy! Model: https://huggingface.co/jakeatx/qwen3.8-flash-next-Swift1.5-ATX-AI3 LlamAmpere: https://github.com/JakeATX/llamAmpere
