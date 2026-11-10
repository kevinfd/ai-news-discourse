---
id: "322f3a51d05589f1"
title: "Latent prediction beats reconstruction for tactile pretraining on dexterous manipulation tasks[R]"
url: "https://reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for"
link: "https://reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T18:52:05Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Zealousideal-War7154"]
language: "en"
summary: "New paper from Robbyant, with inference code and checkpoints already public. LingBot-Touch is a self-supervised tactile encoder trained JEPA-style: it predicts latent representations of masked contact instead of reconstructing raw sensor signals. The paper tests it against same-size MAE and VAE reconstruction models on the same data. Tactile-to-video top-5 recall at 1K hours: 32.1% (JEPA) vs…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 218
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/"
score: null
comments: null
community: "r/MachineLearning"
---

# Latent prediction beats reconstruction for tactile pretraining on dexterous manipulation tasks[R]

Reddit · Zealousideal-War7154 · 2026-11-09

New paper from Robbyant, with inference code and checkpoints already public. LingBot-Touch is a self-supervised tactile encoder trained JEPA-style: it predicts latent representations of masked contact instead of reconstructing raw sensor signals. The paper tests it against same-size MAE and VAE reconstruction models on the same data. Tactile-to-video top-5 recall at 1K hours: 32.1% (JEPA) vs 5.6% (MAE) vs 4.4% (VAE). At 4K hours JEPA reaches 49.3% and MAE stays under 9%, while the VAE actually gets worse, down to 3.1%. Their explanation: most of a tactile clip is near-zero background, so reconstruction loss can shrink without learning anything about actual contact. Two design choices stood out. The masking ratio warms up from 40% to 80% over 300 steps, because starting at high masking hid every contacting taxel in sparse signals and caused gradient explosions. Three sensor types (magnetic, piezoresistive, visuotactile) feed one shared Transformer through canonical fingertip coordinates with 5D RoPE (time, finger, 3D position). On 26 real robot tasks with 4 policies, frozen encoder features scored highest in 89 of the 104 policy and task combinations. On a magnetic hand never seen in pretraining, LingBot-VLA went from 57.21 to 75.04. The Tiny model levels off around 4K hours while Small keeps improving, so a bigger version trained on more data looks like the natural next step.
