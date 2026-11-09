---
id: "983d9f665ef983ae"
title: "I merged attention and MLP processing into a single gated Transformer block. GAP [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xr47tw/i_merged_attention_and_mlp_processing_into_a"
link: "https://reddit.com/r/MachineLearning/comments/1xr47tw/i_merged_attention_and_mlp_processing_into_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T17:43:26Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["WAMFT"]
language: "en"
summary: "Hi everyone! I've been experimenting with an alternative Transformer architecture called GAP (Gated Attention Projection) . The main idea is to combine attention and MLP-style processing into a single gated block, instead of using the standard separate attention and feed-forward sublayers. I tested it against a standard Transformer using 100 million scored training tokens per model from…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 197
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xr47tw/i_merged_attention_and_mlp_processing_into_a/"
score: null
comments: null
community: "r/MachineLearning"
---

# I merged attention and MLP processing into a single gated Transformer block. GAP [R]

Reddit · WAMFT · 2026-11-08

Hi everyone! I've been experimenting with an alternative Transformer architecture called GAP (Gated Attention Projection) . The main idea is to combine attention and MLP-style processing into a single gated block, instead of using the standard separate attention and feed-forward sublayers. I tested it against a standard Transformer using 100 million scored training tokens per model from WikiText-103. Some results: GAP20 used 19.91% fewer parameters than the standard Transformer. A smaller configuration can reduce parameters by 34.31% , although that version did not fair as well as the current model against the regular transformer, so i ended up giving 14% of my perameters savings to the GAP model for extra width, leaving the model at about 20% fewer perameters, which is why i called it in testing GAP20 The standard Transformer performed better on final language-model accuracy. Compiling GAP20 with torch.compile improved training throughput by approximately 19.9% in one CPU benchmark compared with running GAP20 without compilation. I've included the architecture code, configurable model sizes, speed benchmark and research paper. This is an experimental architecture, not a claim that it outperforms Transformers overall. I'd be interested in feedback on the design, mathematics and possible improvements. GitHub: https://github.com/rickey1990/Gated-Attention-Projection
