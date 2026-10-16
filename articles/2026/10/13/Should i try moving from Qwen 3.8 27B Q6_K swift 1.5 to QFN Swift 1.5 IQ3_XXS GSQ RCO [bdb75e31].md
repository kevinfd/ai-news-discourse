---
id: "bdb75e31ee5cccad"
title: "Should i try moving from Qwen 3.8 27B Q6_K swift 1.5 to QFN Swift 1.5 IQ3_XXS GSQ RCO?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x50d7y/should_i_try_moving_from_qwen_38_27b_q6_k_swift"
link: "https://reddit.com/r/LocalLLaMA/comments/1x50d7y/should_i_try_moving_from_qwen_38_27b_q6_k_swift"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T15:53:16Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["milpster"]
language: "en"
summary: "I have my inference rig set up now for Qwen 3.8 27B Swift 1.5 Q6_K at 262144ctx with KV at Q8/Q8. My rig has 40gb of vram over two radeon VIIs (2x16gb) and my laptops Rtx3080 Max Q (8gb), using rocm and vulkan. Additionally there is 64gb of ddr 4 ram. The current setup runs at around 450tps PP16384 and 15-30tps output using dflash2. But i am unsure whether i should try moving to the new Qwen 3.8…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 234
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x50d7y/should_i_try_moving_from_qwen_38_27b_q6_k_swift/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Should i try moving from Qwen 3.8 27B Q6_K swift 1.5 to QFN Swift 1.5 IQ3_XXS GSQ RCO?

Reddit · milpster · 2026-10-13

I have my inference rig set up now for Qwen 3.8 27B Swift 1.5 Q6_K at 262144ctx with KV at Q8/Q8. My rig has 40gb of vram over two radeon VIIs (2x16gb) and my laptops Rtx3080 Max Q (8gb), using rocm and vulkan. Additionally there is 64gb of ddr 4 ram. The current setup runs at around 450tps PP16384 and 15-30tps output using dflash2. But i am unsure whether i should try moving to the new Qwen 3.8 Flash next Swift 1.5 at a quant of only iq3_xxs in terms of overall smartness - mostly for agentic development but also general agentic work in terms of design or "do task x for me". Asking an ai model of choice to research this topic has not yielded any conclusive evidence for me - so heres my question: Given my rock solid qwen 3.8 27b setup - do you think i should invest my time and tokens into getting a low Qwen 3.8 Flash next 1.5 GSQ RCO IQ3_XXS quant to run at possibly Q8/Q8 KV cache? Do you see a chance of it being smarter than my current setup at comparable speeds? I see quite some hurdles to be taken because with a mixed backend of vulkan and rocm i can forget the use of things like strata and will have to pursue my own fork of some sorts - probably llama.cpp with heavy modifications.
