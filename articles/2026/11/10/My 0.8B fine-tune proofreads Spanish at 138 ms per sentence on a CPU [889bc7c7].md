---
id: "889bc7c7327344d5"
title: "My 0.8B fine-tune proofreads Spanish at 138 ms per sentence on a CPU"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsocrj/my_08b_finetune_proofreads_spanish_at_138_ms_per"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsocrj/my_08b_finetune_proofreads_spanish_at_138_ms_per"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T14:31:04Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["AlternativeEnough352"]
language: "en"
summary: "I have been building a Spanish proofreader that runs fully local, and it's finally released, so I wanted to share how it went. It only corrects Spanish, but I think the approach works for other languages and narrow tasks too. If the project has audience, I will release the English proofreader version as well :) App running Better thing is the app is 100% compatible with ANY app in Windows and…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 674
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsocrj/my_08b_finetune_proofreads_spanish_at_138_ms_per/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# My 0.8B fine-tune proofreads Spanish at 138 ms per sentence on a CPU

Reddit · AlternativeEnough352 · 2026-11-10

I have been building a Spanish proofreader that runs fully local, and it's finally released, so I wanted to share how it went. It only corrects Spanish, but I think the approach works for other languages and narrow tasks too. If the project has audience, I will release the English proofreader version as well :) App running Better thing is the app is 100% compatible with ANY app in Windows and Linux. You select text in any app, press Ctrl+Alt+Space, a small popup shows each change with a short explanation, and Enter replaces your selection. MIT, a C++ app on top of llama.cpp . The model is a full fine-tune (no LoRA) of Qwen3.5-0.8B on aprox. 40k pairs, 2 epochs, lr 1e-5. In Q4_K_M with imatrix it's 529 MB. Training took 22 minutes on one rented GPU, and the whole rental with all the evals cost about $2.50 . GPU was RTX 5090 rented (I'm just a mortal so I don't have this GPU at home). I tested it on a benchmark I built for this, 2,388 cases in three parts: real Wikipedia edits, Wikipedia talk pages, and synthetic work emails and chat. F0.5: Model Wiki edits Talk pages Emails/chat Mean revisa-0.8b (fine-tuned) 81.5 80.0 92.0 84.5 revisa-0.8b without the C++ filters 77.4 75.8 91.7 81.6 Qwen3.5-0.8B, untuned 70.4 67.9 71.2 69.9 Qwen3.5-2B, untuned 73.8 66.9 81.2 74.0 Gemma 4 E2B, untuned 65.5 65.5 94.1 75.0 Qwen3.5-4B, untuned 83.6 67.4 88.4 79.8 Gemma 4 E4B, untuned 74.4 79.0 95.1 82.8 Qwen3.5-9B, untuned 79.8 69.6 91.2 80.2 LanguageTool 6.6 24.1 52.8 74.1 50.4 Claude Sonnet, high reasoning (cloud, upper bound) 98.0 91.8 98.2 96.0 Gemini 3.8 Flash, high reasoning (cloud, upper bound) 98.7 92.3 98.4 96.5 https://preview.redd.it/fiec1c0uos0i1.png?width=1600&format=png&auto=webp&s=2dea5c522a63c7c5727af2e8fe94b0dbb9264a3b It changes less than 3% of the sentences that were already correct, on every part. LanguageTool changes 39% of the correct Wikipedia sentences, which is more or less why I started this. For those who may not know, LanguageTool is a benchmark when it comes to checking grammar and spelling errors. (More info: https://en.wikipedia.org/wiki/LanguageTool ) A few things I learned: Most of the training data isn't LLM generated. I take correct text from Wikipedia , Tatoeba and Common Voice and break it with a rule-based error injector, so the exact answer is known. Around a third of the examples are correct sentences that have to come back unchanged, and that's what keeps false alarms low. The model doesn't explain anything. It only returns the corrected sentence. Then plain C++ does a word diff, puts each edit in one of 31 error types with a fixed explanation, and drops anything it doesn't recognize or that rewrites too much. Small models invent grammar rules with a lot of confidence, so I didn't let it. For speed, the user's own sentence is the speculative draft, because a corrected sentence is almost the same text. I got 2.2x: 138 ms median against 305 ms greedy, 8 threads, same output as greedy on 99.4% of a 500-sentence sample. The annoying part was that the Gated DeltaNet layers keep a recurrent state you can't partially roll back, so I snapshot the state before each verification pass. But I'm happy the app run like a charm. https://preview.redd.it/r8lv0gpvos0i1.png?width=1600&format=png&auto=webp&s=30971b3aba5f6187ea18100d1d7585e5fb05fa72 Caveats: it's my benchmark. The gold corrections come from two LLMs of different families working blind, with a debate round when they disagreed, and it was frozen before scoring anything. The untuned models got the same instructions and the same filters. Bigger untuned models win some parts (Qwen3.5-4B on Wikipedia edits, Gemma 4 E4B on emails), and if you remove the borderline sentences they pass it on average, so a big part of the win is knowing when not to touch. Frontier cloud models with reasoning are still around 96, so there's room. All the process explained: https://manuelgs.com/en/blog/revisa-case-study/ App: https://manuelgs.com/en/revisa/ Model (GGUF): https://huggingface.co/manuelgscom/revisa-0.8b-GGUF Benchmark: https://huggingface.co/datasets/manuelgscom/revisa-bench-es Source: https://github.com/manuelgscom/revisa Has anyone tried the input-as-draft trick for other editing tasks? English isn't my first language, so sorry if something sounds weird. Happy to answer questions about the data or the training.
