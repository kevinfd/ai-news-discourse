---
id: "a40405858299f9af"
title: "Steering a pretrained music transformer at sampling time into a real-time jazz partner (no fine-tuning) [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at"
link: "https://reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T09:19:43Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["GGAllin43"]
language: "en"
summary: "I've been working on duetto, a real-time jazz partner for a MIDI keyboard: it plays a standard with you as a small band (solo, comping, walking bass), comps while you play and takes a solo when you stop. Demo (Autumn Leaves, 160 bpm): https://youtu.be/8zIAzVY8O6w Code (free for noncommercial use): https://github.com/RiccardoCataldi/duetto Approach. Instead of fine-tuning, it uses the pretrained…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 336
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at/"
score: null
comments: null
community: "r/MachineLearning"
---

# Steering a pretrained music transformer at sampling time into a real-time jazz partner (no fine-tuning) [P]

Reddit · GGAllin43 · 2026-11-16

I've been working on duetto, a real-time jazz partner for a MIDI keyboard: it plays a standard with you as a small band (solo, comping, walking bass), comps while you play and takes a solo when you stop. Demo (Autumn Leaves, 160 bpm): https://youtu.be/8zIAzVY8O6w Code (free for noncommercial use): https://github.com/RiccardoCataldi/duetto Approach. Instead of fine-tuning, it uses the pretrained Anticipatory Music Transformer (Thickstun et al., 2023) as-is and does all the control at sampling time: The player's notes and the model's are one event sequence the model continues, one note (onset, duration, pitch) at a time. Before each sample, a rule layer edits the logits: it masks what is not allowed (a hand that must wait, a pitch out of register, a bass note off the beat) and biases what should be likely (the current chord's tones, a guide tone on the downbeat, the next note of a phrase being quoted). Phrases come from the Weimar Jazz Database (transcribed solos), segmented where the soloists actually breathed, transposed to the tune's chords and developed over a chorus. In the demo, about 61% of solo notes come from quoted phrases or the theme; the rest is the model. The server keeps ~1 s of music sampled ahead and resamples the unplayed part whenever the player plays, which keeps latency low while the model "plans". Speed. About 12 ms/note (medium) and 18 ms/note (large) on a 3080 Ti; the large model runs at ~90 ms/note on a Jetson Orin Nano, which is still enough to play live. What doesn't work well yet. It can drift away from the player, its responses are hard to predict, and the balance between the model's own ideas and the rules is fragile: too much bias and it sounds like a phrase book, too little and it stops sounding like jazz. I'd love feedback on the approach, especially from anyone who has tried constrained or guided decoding for symbolic music: is sampling-time steering a reasonable alternative to fine-tuning here, or does it hit a ceiling?
