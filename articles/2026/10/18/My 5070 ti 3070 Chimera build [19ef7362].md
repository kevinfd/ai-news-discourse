---
id: "19ef7362b1ee367b"
title: "My 5070 ti/3070 Chimera build."
url: "https://reddit.com/r/LocalLLaMA/comments/1x8u6eg/my_5070_ti3070_chimera_build"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8u6eg/my_5070_ti3070_chimera_build"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T04:37:04Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["hereforcheesee"]
language: "en"
summary: "Got lucky with a 5070 Ti for $750 AFTER TAX (might be the best decision I've ever made tbh) back in November 2025. If only I had known I'd be getting into local llms at the time...anyways. I recently decided to start messing with local AI. I began getting comfortable in Powershell and having local models help me write random automation scripts. Naturally, that spiraled into wanting bigger…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 219
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8u6eg/my_5070_ti3070_chimera_build/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# My 5070 ti/3070 Chimera build.

Reddit · hereforcheesee · 2026-10-18

Got lucky with a 5070 Ti for $750 AFTER TAX (might be the best decision I've ever made tbh) back in November 2025. If only I had known I'd be getting into local llms at the time...anyways. I recently decided to start messing with local AI. I began getting comfortable in Powershell and having local models help me write random automation scripts. Naturally, that spiraled into wanting bigger models, which meant hunting for more VRAM. I had my old 3070 sitting around, so I mounted it outside the case on a PCIe riser (it’s only running at x1, which works because layer splitting passes very little data between cards). Ollama/llama.cpp split the model across the two mismatched GPUs with almost no fuss. Current result: Qwen 3.6 35B-A3B (a MoE with about 3B active parameters, so it’s quicker than a dense 35B would be) at around 82 tok/s with a 16k context. Still not perfect: about 23% of the layers are spilling into system RAM, and I haven’t tuned the split ratio between the cards yet. The 3070 has about 4GB sitting unused. If I keep it like this, I'll probably buy or make a cheap enclosure and put the 3070 in it. Anyone else running a mismatched GPU pair? What split ratios worked for you? https://preview.redd.it/ry5rngmkn5wh1.jpg?width=1555&format=pjpg&auto=webp&s=e15443f2271b5ebc0e9c9c3000c238eb5fa49d43 https://preview.redd.it/vkgqigmkn5wh1.jpg?width=1468&format=pjpg&auto=webp&s=a2e6c907e01b5281e96d65f8e9a4ed7cec5d1760 https://preview.redd.it/hxhquejmn5wh1.png?width=336&format=png&auto=webp&s=fca55d41607f65495a437bc8a67afcf2820296ab https://preview.redd.it/k7r06ejmn5wh1.png?width=962&format=png&auto=webp&s=3ec4ac990aef2d781e2128a2715f82ba2f2f2d0f
