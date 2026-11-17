---
id: "03dd9463190fd7e5"
title: "Yomikae: translate raw manga in your browser, lettered into the bubbles like a real scanlation"
url: "https://reddit.com/r/ClaudeAI/comments/1xxubo7/yomikae_translate_raw_manga_in_your_browser"
link: "https://reddit.com/r/ClaudeAI/comments/1xxubo7/yomikae_translate_raw_manga_in_your_browser"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T16:47:34Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Narrow_Ad9226"]
language: "en"
summary: "I read a lot of untranslated manga/doujinshi on pixiv and X (you can also create an adapter for aggregator sites like tachiyomi), so I built Yomikae. You browse normally, and each page gets the Japanese erased and English lettered into the speech bubbles, like a scanlation. It runs on your Claude subscription through claude -p , with no API key. Only the text goes to Claude, and the page images…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 198
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xxubo7/yomikae_translate_raw_manga_in_your_browser/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Yomikae: translate raw manga in your browser, lettered into the bubbles like a real scanlation

Reddit · Narrow_Ad9226 · 2026-11-16

I read a lot of untranslated manga/doujinshi on pixiv and X (you can also create an adapter for aggregator sites like tachiyomi), so I built Yomikae. You browse normally, and each page gets the Japanese erased and English lettered into the speech bubbles, like a scanlation. It runs on your Claude subscription through claude -p , with no API key. Only the text goes to Claude, and the page images stay on your computer. A local LLM or a codex sub works too. GitHub (GPL-3.0): https://github.com/gravewhisper/yomikae Benchmarks: Benchmark Yomikae Koharu manga-image-translator BallonsTranslator Names spelled right (of 113) 86 70 45 65 OCR error rate 1.0% 1.3% 4.3% 5.6% Translation quality (COMET) 0.747 0.752 0.731 0.736 Lines translated (of 1586)¹ 1546 1583 1498 1530 Seconds per page (CPU) 3.9 22.9 7.5 2.9 Works in your browser as you read ✅ ❌ ❌ ❌ Remembers earlier pages and names ✅ ❌ ❌ ❌ ¹ 33 of Yomikae's 40 skipped lines are bubbles with only "?" or "……", which it leaves as they are. All four tools ran 214 OpenMantra pages with the same LLM (Gemma 4 12B), reasoning off, vision models on the CPU. Each ran once. Full method: docs/benchmarks.md
