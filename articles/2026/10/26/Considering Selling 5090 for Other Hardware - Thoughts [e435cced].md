---
id: "e435cced3078bd4e"
title: "Considering Selling 5090 for Other Hardware - Thoughts?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xg4cj4/considering_selling_5090_for_other_hardware"
link: "https://reddit.com/r/LocalLLaMA/comments/1xg4cj4/considering_selling_5090_for_other_hardware"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T18:04:33Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Anarchaotic"]
language: "en"
summary: "Hey everyone, Here are the specs of my main workstation: 5090 FE 14700k 96GB DDR5 Ram (Two Sticks) Specs of my inference server: Strix Halo - 128GB (Framework Desktop) GUFO + Qwen3.8 Flash Next Embedding Models STT/TTS Models I also have some other non-AI servers for hosting containers + offsite cloud backup + NAS. When I upgraded my current PC prices were basically MSRP (that's what I paid for…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 617
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg4cj4/considering_selling_5090_for_other_hardware/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Considering Selling 5090 for Other Hardware - Thoughts?

Reddit · Anarchaotic · 2026-10-26

Hey everyone, Here are the specs of my main workstation: 5090 FE 14700k 96GB DDR5 Ram (Two Sticks) Specs of my inference server: Strix Halo - 128GB (Framework Desktop) GUFO + Qwen3.8 Flash Next Embedding Models STT/TTS Models I also have some other non-AI servers for hosting containers + offsite cloud backup + NAS. When I upgraded my current PC prices were basically MSRP (that's what I paid for the FE and RAM was $400). It was intended to be a very functional work machine for heavy usage + gaming on the side. Now that prices have skyrocketed, I'm seriously considering selling the 5090 and replacing it with a 5070ti + another dedicated machine. The Strix Halo is excellent, but I'm running a business and want my employees to be able to also make use of everything that I've built out infrastructure wise. A single machine is great for me, but you can't reasonably scale it. We do a lot of sensitive client work where we can't use cloud models, so local models are amazing for this. My goals are: Create a more easily "scalable" solution that can grow over time. Be able to serve at least three concurrent users with 2 or 3 parallel sessions for each (so tool calling works per-user). Be able to run Qwen3.8 FN equivalent @ 200k context windows. Sacrifices I'm aware of and willing to make: Speed - Obviously this won't come close to cloud infrastructure, but the Strix Halo in its current implementation has been good enough for my usage. 1400 prefill, 50 token average for generation. Intelligence - We can still use cloud models for internal work, these only replace customer-specific coding and scripting, which require far less complexity. Pooling hardware - I don't know how much this will impact us in the future, but as of now I'm not sure I require something like the DGX Spark interconnect. Current Options: Buy another Strix Halo. I don't actually need to pool the machines together so they can just run independently with custom user profiles. For the price of the 5090 I could actually buy two of these. Buy a 256GB Mac Studio. I might have to cover a cost difference, and this will now force me to upkeep two completely different stacks of infrastructure - but will allow for potentially easier scalability in the future + bigger models. Buy a 5070ti, and re-work my current machine as a server. I already have enough components on hand to build a new PC without a GPU, so I could use the 5090 with 96GB of RAM as a new machine. Buying 4 Radeon R9700s. This also increases my cost because now I have to get a new motherboard, PSU, and a bunch of other stuff. DGX Spark - When I first considered what machine to buy, the spark was about $1000 more than the Halo, which wasn't a justifiable cost for the performance benefit. At the moment it's so outrageously expensive for what it is there's no shot. Things I won't consider: Building used. This is for my business and so I want to have a warranty. A few things I don't know or need to speculate about: How good is the 5090 + 96GB RAM with newer software improvements today? It's been a while since I've seriously done any AI work on this. Is 128GB going to be a problem down the line, and so being able to pool hardware together to run bigger models is a key influence? Any advice is appreciated. My gut is telling me to just get another Strix Halo since I've been using it long enough + have all of the software components dialed in.
