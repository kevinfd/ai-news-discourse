---
id: "d315c45ab355135e"
title: "Qwen Flash Next potential SOTA Q2 nobody talks about"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7bboy/qwen_flash_next_potential_sota_q2_nobody_talks"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7bboy/qwen_flash_next_potential_sota_q2_nobody_talks"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T09:08:25Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["PlasticRevenue4601"]
language: "en"
summary: "Whenever it comes to Strata and low bit QFN discussion, everyone is talking about Unsloth, ISTA-lab and nobody mentions Agantai with his GYRO series of quants - https://huggingface.co/agentionai/Qwen3.8-Flash-Next-Gyro-GGUF The quants allegedly have simultaniously better KLD, top 1 and lesser size than the ones from ISTA. Also enhanced loop resitance is advertised. Bold claims and signle…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["jobs & society", "agents & coding", "search & media"]
content_source: "post"
word_count: 334
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7bboy/qwen_flash_next_potential_sota_q2_nobody_talks/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen Flash Next potential SOTA Q2 nobody talks about

Reddit · PlasticRevenue4601 · 2026-10-16

Whenever it comes to Strata and low bit QFN discussion, everyone is talking about Unsloth, ISTA-lab and nobody mentions Agantai with his GYRO series of quants - https://huggingface.co/agentionai/Qwen3.8-Flash-Next-Gyro-GGUF The quants allegedly have simultaniously better KLD, top 1 and lesser size than the ones from ISTA. Also enhanced loop resitance is advertised. Bold claims and signle contributor were the things why I was initially reluctunt to check the claims myselfm hovewer that potential space savings were impossible to resist so I downloaded GYRO-M and played around with it for a little while. My expersience with it: Before moving further, I'd like to share my serttings: Inference engine: GYRO fork of the Strata Quant used: GYRO-M Vision: yes, took it from ISTA lab IQ3_XXS quant Context: 200k KV cache quantisation: k8v4 Agent: Pi agent Samplings: temperature: 1.0, top_p: 0.95, top_k: 20, min_p: 0.05 Thinking: always xhigh Looping It never looped once during my 3 days of testing, longest autonomous cycle - 2-3 hours, author's claims seems to hold up Tool calls Generally stable, however it sometimes meeses up edits on Cyryllic texts(Russian, Ukrainian languages). Subjective impression - more stable than ISTA q2 quants, less stable than ISTA q3 because of Cyrillics problem Context retention No signs of braindeadness recorded, it never loses initial goal, almost always remembers all the nuances, instruction following is stable Performance As fast as ISTA 2 bit quants Example Prompt: "create an animated voxel 3d world of a pelican riding a bike as good as you can" First photo is ISTA lab IQ3XXS Second one is ISTA lab IQ2XS Third one is GYRO-M https://preview.redd.it/slx0eci7osvh1.png?width=1911&format=png&auto=webp&s=6fd3042b5770850c00bcf4f9450401d418ae51e7 https://preview.redd.it/nwkbc5ahosvh1.png?width=1917&format=png&auto=webp&s=cb5965017ef49df6003427179769cd6cabde8964 https://preview.redd.it/o2lgfothosvh1.png?width=1916&format=png&auto=webp&s=880bab363dc169fc76de8b2ea79a899e361b0778 Conclusion This quant is 100% alive and well and there are strong signals that it's indeed at ISTA lab q3 level while being much smaller, huge thanks for the author for his incredible job, he's a monster because this impeccable job was done by a !single man. It looks like sometimes a solo with skill, perseverance and purpose can go against the dedicated team and win
