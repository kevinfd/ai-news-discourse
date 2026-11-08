---
id: "def58f441869efd4"
title: "# One token at the beginning of a prompt changed 6 out of 15 LLM responses. Does it matter?"
url: "https://github.com/DarkZachi83/Bobr/tree/main/tests/experiments/bos"
link: "https://github.com/DarkZachi83/Bobr/tree/main/tests/experiments/bos"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T21:12:26Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Full-Travel857"]
language: "en"
summary: "I'm back with another experiment. After the last heated discussion about KV cache, temperature 0, and reproducibility — where I got quite a beating for both my post and my writing style (partly deserved, to be fair ;) ) — I decided to investigate how models behave in Ollama and llama.cpp. And, as usually happens with these experiments, I found something I wasn't even looking for. The…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "summary"
word_count: 102
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqh2jw/one_token_at_the_beginning_of_a_prompt_changed_6/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# # One token at the beginning of a prompt changed 6 out of 15 LLM responses. Does it matter?

GitHub · Full-Travel857 · 2026-11-07

I'm back with another experiment. After the last heated discussion about KV cache, temperature 0, and reproducibility — where I got quite a beating for both my post and my writing style (partly deserved, to be fair ;) ) — I decided to investigate how models behave in Ollama and llama.cpp. And, as usually happens with these experiments, I found something I wasn't even looking for. The Bielik-Minitron 7B chat template stored in the GGUF includes the beginning-of-sequence token <s> , but the template Ollama uses for this model doesn't add it. I thought to myself: come on, man, it's just one…
