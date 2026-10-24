---
id: "47251ceef4154908"
title: "qwen3.8 27B on my 3090 basically tied Opus 5.5 on a Korean RAG benchmark, which I did not expect"
url: "https://reddit.com/r/LocalLLaMA/comments/1xe4v74/qwen38_27b_on_my_3090_basically_tied_opus_55_on_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1xe4v74/qwen38_27b_on_my_3090_basically_tied_opus_55_on_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T10:07:50Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Front-University4363"]
language: "en"
summary: "So I’ve been running local RAG over Korean PDFs for a while and my only evaluation was “yeah the answers look ok”. Finally sat down and used Allganize’s Korean RAG set since every question has a known answer and the page it’s on (300 questions, 64 PDFs, MIT). Fed every model the same top 5 pages and same prompt. I used qwen3.6 27B as a judge but figured it might go soft on its own family, so…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 415
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xe4v74/qwen38_27b_on_my_3090_basically_tied_opus_55_on_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# qwen3.8 27B on my 3090 basically tied Opus 5.5 on a Korean RAG benchmark, which I did not expect

Reddit · Front-University4363 · 2026-10-24

So I’ve been running local RAG over Korean PDFs for a while and my only evaluation was “yeah the answers look ok”. Finally sat down and used Allganize’s Korean RAG set since every question has a known answer and the page it’s on (300 questions, 64 PDFs, MIT). Fed every model the same top 5 pages and same prompt. I used qwen3.6 27B as a judge but figured it might go soft on its own family, so Opus 5.5 judged everything too. qwen3.8 27B with thinking on got 77.3%, Opus 5.5 got 76.6%. p=0.82 on McNemar so that’s a tie. Opus judging gave 80.6 vs 80.3, same story. Thinking off drops qwen about 6 points though, so don’t skip that. What surprised me more was looking at where Opus failed. 70 misses total, and 22 of those were pages that are just scanned images with no text layer, 23 the retriever never pulled the right page, and only 25 were actually the model screwing up. so honestly the model isn’t the bottleneck anymore for me, my PDF parsing is. There’s a 2024 commercial system (Alli + Claude 3.5 Sonnet) with results on this same set and it only beats my setup on those scanned pages, 19 to 1. I don’t do OCR. lol. Also BM25 with plain whitespace splitting got 56% hit@5 and with a proper Korean morphological tokenizer it got 80%. Kind of obvious in hindsight but I’d been running the whitespace one for months. gpt-oss 20B looked terrible at first (57.5%) until I noticed a bunch of empty answers. My 1024 token limit was cutting it off while it was still thinking. Bumped to 8192 and it went to 69.6%. That one was on me. Tried KRAFTON’s new Raon-1 mini preview after (30B MoE, ~4B active). Lands around 74-75% and does 96 tok/s on the 3090, which is nice. But at temp 0 with thinking on it got stuck in a loop on 16 out of 320 questions (the 320 includes 20 unanswerable ones I wrote). Couple of things I’m not confident about. Everything’s one run at temp 0, and when I ran the same model on different hardware 11 verdicts flipped, so a 1 point gap means nothing. And those 20 unanswerable questions were way too easy, every model refused every one of them, so I learned nothing there. Need to write harder ones. Scripts, per question verdicts and the full tables are here if anyone wants to poke at it: https://bric.pe.kr/blog/local-rag-27b-ties-opus-korean-documents-300-questions
