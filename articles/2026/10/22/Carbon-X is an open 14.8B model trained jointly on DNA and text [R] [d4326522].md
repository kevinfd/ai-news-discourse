---
id: "d432652212050f6c"
title: "Carbon-X is an open 14.8B model trained jointly on DNA and text [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on"
link: "https://reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T12:32:56Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["jatingargiitk"]
language: "en"
summary: "Carbon-X is a 14.8B parameter decoder-only model that takes raw DNA in a normal chat and answers in English. It shares one token stream for text and DNA, using 6-mer tokens, and was mid-trained on 302B tokens. Hugging Face reports a 66.7% average across five DNA benchmarks with thinking disabled, versus 67.5% for GPT-6.1 Sol. The weights fit on one 80 GB GPU in bfloat16 and are Apache 2.0. It…"
tags: ["r/MachineLearning"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "business & funding", "chips & infrastructure"]
content_source: "post"
word_count: 115
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on/"
score: null
comments: null
community: "r/MachineLearning"
---

# Carbon-X is an open 14.8B model trained jointly on DNA and text [R]

Reddit · jatingargiitk · 2026-10-22

Carbon-X is a 14.8B parameter decoder-only model that takes raw DNA in a normal chat and answers in English. It shares one token stream for text and DNA, using 6-mer tokens, and was mid-trained on 302B tokens. Hugging Face reports a 66.7% average across five DNA benchmarks with thinking disabled, versus 67.5% for GPT-6.1 Sol. The weights fit on one 80 GB GPU in bfloat16 and are Apache 2.0. It has not been clinically validated, and the model card says exact sequence operations should still be handled by code. the useful part is making sequence analysis local enough for sensitive datasets. has anyone tested whether the benchmark gains hold on private variant datasets? source: https://huggingface.co/HuggingFaceBio/Carbon-X
