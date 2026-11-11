---
id: "62101333d9a209a9"
title: "Strata vs Basalt more differences than speed."
url: "https://reddit.com/r/LocalLLaMA/comments/1xsp6ub/strata_vs_basalt_more_differences_than_speed"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsp6ub/strata_vs_basalt_more_differences_than_speed"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T15:05:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["x_MASE_x"]
language: "en"
summary: "So I've been using strata for a while now in windows using Qwen3.8-Flash-Next iq3s before the new gui thing and I think it's been fine compared to Qwen3.8-27B which was lacking in quality and polishing. So I upgraded my ram from 64 to 128. Got a new pc and made an Ai box only for Ai text models and comfyui. So I had to test the speed difference between strata and basalt since in windows basalt…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 502
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsp6ub/strata_vs_basalt_more_differences_than_speed/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata vs Basalt more differences than speed.

Reddit · x_MASE_x · 2026-11-10

So I've been using strata for a while now in windows using Qwen3.8-Flash-Next iq3s before the new gui thing and I think it's been fine compared to Qwen3.8-27B which was lacking in quality and polishing. So I upgraded my ram from 64 to 128. Got a new pc and made an Ai box only for Ai text models and comfyui. So I had to test the speed difference between strata and basalt since in windows basalt was not working good at all. So strata cli engine 0.1.59 Qwen3.8-Flash-Next iq3s with 256k context. Dflash 2 and 0 reserve vram and tuned run. Vision on. With basalt converted model .basalt file Version 0.3.2 same model. Same context. Same everything. Vision dynamic. The differences is. Strata: Avg tps 99.2 and avg prefill 839 with 11.1M tokens used. Vram 15.3 Ram 69.2gb The prompts felt sluggish moving from generating to reading to whatever. It felt wrong and slow and toke forever and that caused the huge stale in usage which dips down and up a lot. Like it's having problems moving from each phase to the next. Last and most importantly that it can't finish the work correctly. Doesn't compact correctly. The development is broken. And it feels like a cheap model you hosted in your cheap pc you poor man. Basalt: Avg from 100 to 118. Peaking to 145. Avg prefill not sure but peaking 4200. Vram 15.8 with reserve ram 128m Ram 52.7gb then after maybe a couple of hours 53.1 The generation been smooth without any dipping or staling and moving from phases like strata. Last and most important factor is it finished. It kept going. It compacted fine like deepseek and it felt more capable and more reliable than with strata. Way less errors. Way less mess up and when I told him to keep going till the project is finished it kept going. Granted it's not perfect but it's the model capabilities and we have to realize that. But at least it's now in a stage you can actually rely on it and say you have a "working" local Ai model. Cause since I tested maybe Qwen-3.6-35B nothing ever felt like a good model I can rely on. I know this is a small task but it paves the road for me to actually feel like I can do stuff locally and reliably. I will next test nvfp4 model for both and see if nvfp4 actually gains more speed or not. So basalt now more capable and can contuine working way longer than with strata. Can actually do a good job. And it uses way less ram too. This is also my first ever run so there is maybe more optimizations can be done but this is the default settings besides the vram change. I advice anyone using Qwen3.8-Flash-Next to try it. And I will test swift too but later and with this ram savings I might also test deepseek why not hahah. My rig: 12900k 128gb ddr4 5070ti Harness: opencode
