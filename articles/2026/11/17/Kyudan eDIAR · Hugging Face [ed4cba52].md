---
id: "ed4cba52c8f7cd68"
title: "Kyudan/eDIAR · Hugging Face"
url: "https://huggingface.co/Kyudan/eDIAR"
link: "https://huggingface.co/Kyudan/eDIAR"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-17T04:19:30Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["pmttyji"]
language: "en"
summary: "eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means Meetings last up to an hour, and nobody knows in advance how many people will speak. Neural diarizers with a fixed number of output slots, such as Streaming Sortformer and Nemotron-3, are accurate and run online, but they cannot name more speakers than they have slots. We remove this limit…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "Google"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 113
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyawrf/kyudanediar_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Kyudan/eDIAR · Hugging Face

Hugging Face · pmttyji · 2026-11-17

Instructions to use Kyudan/eDIAR with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use Kyudan/eDIAR with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("audio-classification", model="Kyudan/eDIAR") # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("Kyudan/eDIAR", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
📌 The main repository is on GitHub: https://github.com/KyuDan1/eDIAR This Hugging Face repo is deprecated. The GitHub repository is the main one and is actively updated, so please use it for the latest code, issues and pull requests.
Model tree for Kyudan/eDIAR
Base model
Wespeaker/wespeaker-voxceleb-resnet34-LM
