---
id: "5bf98f75d81aef0b"
title: "LightMIS: Ultra-lightweight medical image segmentation for edge devices [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image"
link: "https://reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T20:22:30Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["OkLion2068"]
language: "en"
summary: "Hi everyone, I am one of the authors of LightMIS, and I would like to share our work on 2D binary medical image segmentation. LightMIS has 131K parameters and aggregates multi-scale encoder features directly, without a learned stage-wise decoder. It achieves close observed modality-macro Dice and IoU averages to nnWNet, while using 98.14% fewer parameters and 94.58% fewer GFLOPs, with both…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "health & science", "chips & infrastructure"]
content_source: "post"
word_count: 216
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/"
score: null
comments: null
community: "r/MachineLearning"
---

# LightMIS: Ultra-lightweight medical image segmentation for edge devices [R]

Reddit · OkLion2068 · 2026-11-02

Hi everyone, I am one of the authors of LightMIS, and I would like to share our work on 2D binary medical image segmentation. LightMIS has 131K parameters and aggregates multi-scale encoder features directly, without a learned stage-wise decoder. It achieves close observed modality-macro Dice and IoU averages to nnWNet, while using 98.14% fewer parameters and 94.58% fewer GFLOPs, with both models trained and evaluated under the same nnU-Net protocol. Paper: https://arxiv.org/abs/2609.28327 Code: https://github.com/AndreiiArhire/LightMIS We also tested LightMIS and the reference models on a real edge device with an Arm Mali-G52 MC2 GPU, where the full LightMIS model ran around 10.5× faster than nnWNet. All LightMIS variants achieved 100% GPU operator coverage, without CPU fallback. We started by training several popular medical image segmentation architectures, both lightweight and heavyweight, from scratch in the same controlled environment using nnU-Net v2.3.1. The experiments covered six datasets and five imaging modalities. Our goal was to develop a lightweight architecture that performs well across these modalities, which led us to the current version of LightMIS. The source code, checkpoints, and details needed to reproduce the results are publicly available. Feel free to experiment with it and try it on your own segmentation tasks. I would be happy to hear how it works for you! Any suggestions or feedback are welcome!
