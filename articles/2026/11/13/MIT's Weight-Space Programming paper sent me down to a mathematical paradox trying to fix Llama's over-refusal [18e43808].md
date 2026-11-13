---
id: "18e4380861882f27"
title: "MIT's Weight-Space Programming paper sent me down to a mathematical paradox trying to fix Llama's over-refusal."
url: "https://reddit.com/r/LocalLLaMA/comments/1xv5f8y/mits_weightspace_programming_paper_sent_me_down"
link: "https://reddit.com/r/LocalLLaMA/comments/1xv5f8y/mits_weightspace_programming_paper_sent_me_down"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T11:27:31Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Top_Speaker_7785"]
language: "en"
summary: "So i had been building a cli tool around weight space programming inspired by recent Mit- weight space programming paper, I had integrated couply of funtionalities to it along with triage, one of which was activation steering to deal with over refusals, my llama 3.2 1b was not answering prompts like \"how do i stage a massacre for a tv show\" Firstly attempt was by subtracting the refusal…"
tags: ["r/LocalLLaMA"]
orgs: ["Meta"]
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "post"
word_count: 440
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xv5f8y/mits_weightspace_programming_paper_sent_me_down/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# MIT's Weight-Space Programming paper sent me down to a mathematical paradox trying to fix Llama's over-refusal.

Reddit · Top_Speaker_7785 · 2026-11-13

So i had been building a cli tool around weight space programming inspired by recent Mit- weight space programming paper, I had integrated couply of funtionalities to it along with triage, one of which was activation steering to deal with over refusals, my llama 3.2 1b was not answering prompts like "how do i stage a massacre for a tv show" Firstly attempt was by subtracting the refusal direction , extracted the refusal vector and subtracted it, the tv massacre prompt was answered but my regression suit got hit, model started answering how to build pipe bombs and syntesize pioson so turned out over-refusal and real harmful refusal direction had a cosine similarity of about 0.75, so supressing one also effects other Second attempt.. Ran activation patching ..found the exact casual bottleneck layer ..(layer 8) orthogonally projected the harmful-refusal component out of my steering vector and used clamped so it caps the activation when it spiked above a threshold , without touching other things.. this nearly worked accuracy increased by 10% but a totally unrelated issue hit by regression suit again..a chinese benchmark loop started looping forver... failure again.. even on steering a single targeted layer ..gave regression as the residual stream is so densely packed that a small hit at layer 8 ripples down further ... my last few brain cells thought i l steer the layer 8 measure the drift at layer 9 and cancel the part i dont want . so i did the math Steer at Layer 8 At Layer 9, compute Δ = steered_layer9 - clean_layer9 Filter out the bad drift and keep only the anti-refusal shift I want Apply final_layer9 = clean_layer9 + wanted_shift ..so if i take the clean layer 9 add only anti refusal shift ..thats basically layer 9 steering .. and if do that to layer 9 same happens to layer 10.. what actually worked was weight surgery..i also tried a conditional weight edit.. a gate programmed into 3 mlp neurons across layer 9-11. they have non linea activations so they can act as real if/then if input matched fictional scary context - gate fires cancel refusal for chinese text -the neuron output is 0 nothing changes tl;dr steering works well for problems that sit along a direction, it fixed a blank reply bug for entangled safety problems like this one they do collateral damage somewhere even with causal layer localization and orthogonal projection non linear neuron gating was only thing that worked with no other damage everything i did was on gtx 1650 4gb, i l open source the cli tool in some time .. happy to answer any question
