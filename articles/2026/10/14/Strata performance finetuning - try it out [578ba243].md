---
id: "578ba2434e96ba36"
title: "Strata performance finetuning - try it out"
url: "https://reddit.com/r/LocalLLaMA/comments/1x65hq9/strata_performance_finetuning_try_it_out"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T22:47:26Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Dreeew84"]
language: "en"
summary: "As strata is somewhat new, I assume that some people din't yet learn how to finetune it for best performance on their machine. I find documentation a bit hard to navigate (use your agents for this!), which doesn't help. After some serious testing, I've tweaked pretty much every parameter available. Some are obvious and I'm not going to waste your time on explaining mtp tweaking. Some I beleive…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["chips & infrastructure", "agents & coding", "models & research"]
content_source: "post"
word_count: 477
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x65hq9/strata_performance_finetuning_try_it_out/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata performance finetuning - try it out

Reddit · Dreeew84 · 2026-10-14

As strata is somewhat new, I assume that some people din't yet learn how to finetune it for best performance on their machine. I find documentation a bit hard to navigate (use your agents for this!), which doesn't help. After some serious testing, I've tweaked pretty much every parameter available. Some are obvious and I'm not going to waste your time on explaining mtp tweaking. Some I beleive are more obscure and those are the ones worth mentioning: Strata setup is supposedly picking the best --pcie-frac value for you. I find that it often doesn't. It's worth investing your time and testing it. Counterintutively, my best performing value is a low 0.2. By testing different --pool-workers values, I was able to find an easy +10% in decode. I'm not smart enough to explain what it does (and how it's different from point 4), but it's worth investing your time in running some benchmarks on your machine. --trim-stage-weights . Boom, extra +8%, try it. Doc is quite explicit on what it does if you're curious. I do beleive that this one can impact performance later in the session and increase swaps but it's still worth it. --pipeline-windows . All I know is that higher values make my CPU work extra. Going from nothing/default to 6 gave an almost 15% increase. Last but not least multi-GPU owners be mindful of GPU priority, if one of your GPUs is on a slower pcie lane. I have two RTX3060's. GPU 0 and GPU 1. At some point I noticed that one of the two GPUs basically acts as a memory pool and doesn't do any compute. I guess it's makes sense for a MOE model. But now I wanted to understand which ones eactly does the work. So I quickly figured out that my default GPU 0 is the one on the slowest pcie lane! If your have two identical GPUs on different speed lanes, bear in mind that their 0/1 order is basically random. You need to figure out exactly which one is which and force the quick one to do the inference. Ask your agent for command lines to figure out whether the 0 or 1 is on your pci_e1 lane. In my case it was GPU 1, the only way to set it as the main GPU is a not very user-friendly two liner :) "gpu": [1,0], "gpu_order": "as_given" This was like another +15%, ridiculous. With all of those cumulated, I'm seeing speeds that I should not be having on my machine. I went from something like 35 decode peak on Qwen Flash Next IQ3_S, to 60 tps average code generation on empty context and 60-70 tps peaks. Performance does degrade with full context but still easily a solid +15%-20% versus the previous baseline tests. This includes huge sessions on full context and compaction. So, try it out.
