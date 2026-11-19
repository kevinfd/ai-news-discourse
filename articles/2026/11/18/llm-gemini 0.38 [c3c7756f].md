---
id: "c3c7756f62d48d7a"
title: "llm-gemini 0.38"
url: "https://simonwillison.net/2026/Nov/18/llm-gemini"
link: "https://simonwillison.net/2026/Nov/18/llm-gemini"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-18T23:59:20Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm-gemini 0.38 \n Today Google introduced Gemini 4 Neon . I wrote recently about how confusing the pricing for the Gemini 4 series was - Neon has somehow made this even worse. \n Previously the Gemini 4 lineup was Hydrogen, Argon, and Carbon - where Argon and Carbon were the same price , and Hydrogen was 3/4 of that price now but will be 1/4 of that price when the other two double an 1st…"
tags: ["yonkers-rising", "gemini", "llm", "pelican-riding-a-bicycle", "ai", "llms", "llm-release", "google", "generative-ai"]
orgs: ["Google", "Anthropic", "Alibaba"]
topics: ["models & research", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 312
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm-gemini 0.38

Simon Willison · Simon Willison · 2026-11-18

18th November 2026
Today Google introduced Gemini 4 Neon. I wrote recently about how confusing the pricing for the Gemini 4 series was - Neon has somehow made this even worse.
Previously the Gemini 4 lineup was Hydrogen, Argon, and Carbon - where Argon and Carbon were the same price, and Hydrogen was 3/4 of that price now but will be 1/4 of that price when the other two double an 1st December once their initial discount pricing expires.
The Neon announcement pretends that Argon doesn't exist. Here's their new image explaining the model line-up:
So the lineup now, from most to least expensive, is Carbon, Neon, Hydrogen.
Except Carbon is currently half price, so right now Neon ($3/million input, $15/million output) is the most expensive of the three - then Carbon ($2/$10), then Hydrogen ($1.50/$7.50). I guess this will make more sense when Carbon doubles to $4/$20 on December 1st.
I ran some pelicans through the three reasoning levels for Neon - low, medium, high.
I dropped Argon from my Gemini 4 comparison grid - here's the new Gemini 4 lineup, where the Neon pelicans do look better than Hydrogen and worse than Carbon:
As I've done with several recent models, I also fired the following prompt against Gemini 4 Neon on "extra" effort level in Google Antigravity:
Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
