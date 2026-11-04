---
id: "518390d9da8bf070"
title: "A new, open-weights 278M PII detection model and reference benchmark [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xn2lro/a_new_openweights_278m_pii_detection_model_and"
link: "https://reddit.com/r/MachineLearning/comments/1xn2lro/a_new_openweights_278m_pii_detection_model_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T19:29:54Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["shanekj"]
language: "en"
summary: "Hi everyone, I wanted to share a new open-weights PII detection model, benchmark and research paper. It's a fine-tune of RoBERTa using 1.2B samples of synthetically generated text that contain a variety of PII. The benchmark, PII-SCOPE (Synthetic Context and Ontology for PII Extraction), was built to address common issues in public LLM-generated datasets and is on Hugging Face too. The model and…"
tags: ["r/MachineLearning"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 102
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xn2lro/a_new_openweights_278m_pii_detection_model_and/"
score: null
comments: null
community: "r/MachineLearning"
---

# A new, open-weights 278M PII detection model and reference benchmark [R]

Reddit · shanekj · 2026-11-03

Hi everyone, I wanted to share a new open-weights PII detection model, benchmark and research paper. It's a fine-tune of RoBERTa using 1.2B samples of synthetically generated text that contain a variety of PII. The benchmark, PII-SCOPE (Synthetic Context and Ontology for PII Extraction), was built to address common issues in public LLM-generated datasets and is on Hugging Face too. The model and script identify instances of PII based on surrounding context, and then return the index and type of each instance. Alternatively, it can return the input with all PII redacted. Technical report (research paper) https://arxiv.org/html/2610.30518v2 Hugging Face model card https://huggingface.co/Protegrity/protegrity-pii
