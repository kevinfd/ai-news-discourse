---
id: "8a5b37ed5e94a16e"
title: "Update: My 4B coding model is getting better at generating 3D scenes"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgc7uv/update_my_4b_coding_model_is_getting_better_at"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgc7uv/update_my_4b_coding_model_is_getting_better_at"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T23:07:49Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["ConfidentDinner6648"]
language: "en"
summary: "Hey everyone, just wanted to share a quick update on the 4B model I posted here . The video shows some results from the latest checkpoint. I'm still training this Qwen3.5-4B fine-tune for general coding, using Three.js scene generation as my main test for now. It still messes up some scenes on the first try, but the newer checkpoints are getting noticeably better, both in scene quality and…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "post"
word_count: 191
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgc7uv/update_my_4b_coding_model_is_getting_better_at/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Update: My 4B coding model is getting better at generating 3D scenes

Reddit · ConfidentDinner6648 · 2026-10-26

Hey everyone, just wanted to share a quick update on the 4B model I posted here . The video shows some results from the latest checkpoint. I'm still training this Qwen3.5-4B fine-tune for general coding, using Three.js scene generation as my main test for now. It still messes up some scenes on the first try, but the newer checkpoints are getting noticeably better, both in scene quality and one-shot success rate. I've updated both Q4_K_M and Q8_0 and fixed the layer issue some people ran into with the previous files. You can grab the updated versions here: https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder I've also been saving test results from each checkpoint, so I can put together a report showing how the model improved throughout training, using multiple prompts for comparison. If everything goes as planned, training should finish around October 28 at 07:30 UTC . After that, I'll release the full FP16 weights, all quantizations, the training dataset, and the technical report . I'm still curious to see how far I can push this little 4B. If you give it a try, feel free to share what works and what breaks, both are really helpful.
