---
id: "36198afd6b90f881"
title: "Upgrade X299, build a 4×3090 rig, or sell the extra GPUs? Looking for advice"
url: "https://reddit.com/r/LocalLLaMA/comments/1x69sit/upgrade_x299_build_a_43090_rig_or_sell_the_extra"
link: "https://reddit.com/r/LocalLLaMA/comments/1x69sit/upgrade_x299_build_a_43090_rig_or_sell_the_extra"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T02:15:07Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Leo_Kwkmi"]
language: "en"
summary: "Hey everyone, I’m trying to decide what to do with my local LLM setup before putting more money into it. A bit of background: I’m a final-year electrical engineering student, and I use local models for learning about LLMs, experimenting stuff and my thesis on financial analysis of solar plants with BESS. I also am going to work in strategic consulting after graduation, so I want a setup that is…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 503
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x69sit/upgrade_x299_build_a_43090_rig_or_sell_the_extra/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Upgrade X299, build a 4×3090 rig, or sell the extra GPUs? Looking for advice

Reddit · Leo_Kwkmi · 2026-10-15

Hey everyone, I’m trying to decide what to do with my local LLM setup before putting more money into it. A bit of background: I’m a final-year electrical engineering student, and I use local models for learning about LLMs, experimenting stuff and my thesis on financial analysis of solar plants with BESS. I also am going to work in strategic consulting after graduation, so I want a setup that is useful for data and market analysis and some coding. My current machine: i7-7800X MSI X299 Raider 128GB RAM — 8×16GB DDR4 2666MHz 2× RTX 3090 I’m currently running Strata IQ3_S at around 100 tokens/s, and I’m pretty happy with the speed. Quality seems okay, a bit better than 27B at Q8. I also have five more 3090s: one ASUS ROG Strix and four Zotacs. All five need repasting and new thermal pads. So seven cards total, with only two currently in use. I paid about $900 each for the four Zotacs. That’s part of why I’m torn: I could use them for a bigger setup, but I could also sell them for around $1,300 each pretty easily in my local used market. These are the options I’m considering: 1. Upgrade the existing X299 machine I found an i9-10940X on AliExpress for around $300. It would give me more cores for my other server workloads and more PCIe lanes, without replacing the motherboard and RAM. My understanding is that I could then run the GPUs at x16/x16, depending on the motherboard’s slot wiring. Please correct me if there’s a limitation I’m overlooking. Alternatively, I could use more widely spaced slots at x16/x8. I’ve tested that layout, and the top GPU runs about 10°C cooler, with the cards sitting around 65°C and 58°C. Would you spend $300 on this CPU upgrade, or avoid putting more money into X299? For inference, would you prioritize x16/x16 or the better cooling at x16/x8? 2. Build a separate machine for the four Zotacs This would give me a second machine with 96GB of VRAM. I’d need to buy a suitable CPU/motherboard setup and sort out cooling, power, and the rest of the build. For anyone who has gone from 48GB to 96GB: Was the improvement in model quality worth it? Im looking at maya for GLM 5.3 flash. Which models and quantizations made the upgrade worthwhile? What inference speeds are you getting, and with which backend? What reasonably priced platform would you recommend for four 3090s? Used hardware is fine. I’m happy with my current speed. The main reason to expand would be access to better models or higher-quality quantizations for engineering, financial modeling, document analysis, and coding. 3. Sell the Zotacs and keep the current setup Since I paid about $900 per card and could sell them for around $1,300 each, I could also sell them and avoid the cost and work of another build. Would you keep the cards because 96GB opens up enough useful possibilities, or sell them while the local resale price is still decent?
