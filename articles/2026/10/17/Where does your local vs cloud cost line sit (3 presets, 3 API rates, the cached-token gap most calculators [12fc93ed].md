---
id: "12fc93ed0bdc03b6"
title: "Where does your local vs cloud cost line sit? (3 presets, 3 API rates, the cached-token gap most calculators guess at) :)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x85758/where_does_your_local_vs_cloud_cost_line_sit_3"
link: "https://reddit.com/r/LocalLLaMA/comments/1x85758/where_does_your_local_vs_cloud_cost_line_sit_3"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T08:40:23Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["paq85"]
language: "en"
summary: "Is self-hosting even worth it on your electricity rate? The answer is 3 numbers you can plug in yourself :) I made a calculator for it (one of 153 free tools, runs in your browser, nothing is uploaded and there is no sign-up): https://appdoesit.com/apps/llm-cost-calculator It does 2 jobs. 1) local side: watts x hours x your kWh rate, with 3 GPU presets (RTX 4070 Ti Super 500 W at ~1k/50 tok/s,…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x85758/where_does_your_local_vs_cloud_cost_line_sit_3/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Where does your local vs cloud cost line sit? (3 presets, 3 API rates, the cached-token gap most calculators guess at) :)

Reddit · paq85 · 2026-10-17

Is self-hosting even worth it on your electricity rate? The answer is 3 numbers you can plug in yourself :) I made a calculator for it (one of 153 free tools, runs in your browser, nothing is uploaded and there is no sign-up): https://appdoesit.com/apps/llm-cost-calculator It does 2 jobs. 1) local side: watts x hours x your kWh rate, with 3 GPU presets (RTX 4070 Ti Super 500 W at ~1k/50 tok/s, RTX 5090 900 W at ~2.5k/120 tok/s, the same 5090 in eco-mode 650 W at ~2k/100). 2) cloud side: input, output and cached tokens at reference API rates ($0.25 / $1.20 / $0.02 per 1M). The line that moves my answer the most is the cached-input rate. Most calculators guess at it, and that is where the crossover hides: a cached prefix re-read costs almost nothing on some providers and real money on others, so your local-vs-cloud answer swings with your provider's cache bill, not just the sticker price. From my experience the crossover sits further out than most people expect once the prompt is long and repeated: on the fixed scenario (60k input / 50k cached / 2k output, 90% uptime), the electricity side is almost flat while the API side keeps climbing. I've had the thread running 8 days with 40 comments, and the most useful replies were the people with their own rig numbers in it. Run the scenario that matches your workload and tell me where your line landed :)
