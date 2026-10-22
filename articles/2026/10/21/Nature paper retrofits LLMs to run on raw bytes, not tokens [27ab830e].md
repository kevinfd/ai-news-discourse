---
id: "27ab830e50707db3"
title: "Nature paper retrofits LLMs to run on raw bytes, not tokens"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xbukow/nature_paper_retrofits_llms_to_run_on_raw_bytes"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xbukow/nature_paper_retrofits_llms_to_run_on_raw_bytes"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T18:04:46Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Justgototheeffinmoon"]
language: "en"
summary: "A [Nature paper published October 7, 2026]( https://nature.com/articles/s41586-026-11111-4?code=ef6759a7-4657-4854-a6e7-87a5ed6db042&error=cookies\\_not\\_supported ) describes a procedure the authors call 'byteification': converting existing subword language models into byte-level ones using less than 1% of a typical pretraining budget. The headline number is 49.1 billion tokens total, split…"
tags: ["r/ArtificialInteligence"]
orgs: ["Meta"]
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xbukow/nature_paper_retrofits_llms_to_run_on_raw_bytes/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Nature paper retrofits LLMs to run on raw bytes, not tokens

Reddit · Justgototheeffinmoon · 2026-10-21

A [Nature paper published October 7, 2026]( https://nature.com/articles/s41586-026-11111-4?code=ef6759a7-4657-4854-a6e7-87a5ed6db042&error=cookies\_not\_supported ) describes a procedure the authors call 'byteification': converting existing subword language models into byte-level ones using less than 1% of a typical pretraining budget. The headline number is 49.1 billion tokens total, split across a 9.8B-token first stage with the global model frozen and a 39.3B-token second stage. The team, led by Benjamin Minixhofer with co-authors including Luke Zettlemoyer, Noah A. Smith, Luca Soldaini and Valentin Hofmann, applied the method to four open models: Olmo 3 7B, OLMo 2 1B, Qwen3 8B Base and Llama 3 8B. The byteified versions are named Bolmo 7B, Bolmo 1B, Bwen 8B and Blama 8B. Parameter counts barely moved — +4.5% for Bolmo 7B, -0.7% for Bolmo 1B. The paper reports that Bolmo 7B delivered a '+16.5% absolute improvement in STEM tasks over BLT 7B', the prior byte-level baseline, while keeping general-benchmark performance close to the subword source. The authors frame the motivation plainly: most frontier models 'use subword tokenization, which obscures fine-grained information problematic for scientific data like code or biological sequences'. Byte-level models sidestep that, but 'have previously lagged in performance'. Two technical choices carry the method. Boundary prediction is non-causal, using one byte of future context. And the byte vocabulary is doubled from 256 to 512 by fusing boundary symbols directly with bytes. The claim is that the resulting models 'operate at practical inference speeds by efficiently processing byte-level information' while remaining compatible with existing serving stacks.
