---
id: "22aef1183288dacc"
title: "The 7.72TB Alleged Anthropic AI Model Is Fake — I Reconstructed Its Generated Weights"
url: "https://reddit.com/r/ClaudeAI/comments/1xls4cj/the_772tb_alleged_anthropic_ai_model_is_fake_i"
link: "https://reddit.com/r/ClaudeAI/comments/1xls4cj/the_772tb_alleged_anthropic_ai_model_is_fake_i"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T08:50:22Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Appropriate-Try-1998"]
language: "en"
summary: "I investigated burner22/numbat , a 7.72TB checkpoint claiming to be an internal Anthropic Mythos-class model. My forensic findings show that the tested weights are deterministically generated, not learned through training. The checkpoint's claim to be a genuine trained model is not supported by this evidence. Here's the proof: 633 tensors: 11,374,080 values reconstructed 100% bit-for-bit using…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 154
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xls4cj/the_772tb_alleged_anthropic_ai_model_is_fake_i/"
score: null
comments: null
community: "r/ClaudeAI"
---

# The 7.72TB Alleged Anthropic AI Model Is Fake — I Reconstructed Its Generated Weights

Reddit · Appropriate-Try-1998 · 2026-11-02

I investigated burner22/numbat , a 7.72TB checkpoint claiming to be an internal Anthropic Mythos-class model. My forensic findings show that the tested weights are deterministically generated, not learned through training. The checkpoint's claim to be a genuine trained model is not supported by this evidence. Here's the proof: 633 tensors: 11,374,080 values reconstructed 100% bit-for-bit using SHA-256 and NumPy PCG64. 373.6 million weight signs: 100% matched the predicted pseudorandom sequences. NVFP4 weights: 99.51% of 173 million held-out quantization codes reconstructed. 4.73B-parameter truncated model: Successfully assembled and executed, but generated repetitive punctuation rather than meaningful language. Embeddings: Some semantic structure exists, but that does not make the reconstructed weight families genuine trained weights. Conclusion: This is a fake model checkpoint containing demonstrably generated weights. The analysis does not establish who created it or whether it has any connection to Anthropic. Full forensic research, reconstruction scripts, and evidence: https://huggingface.co/adityawakharkar/numbat-forensics All findings are open for independent verification.
