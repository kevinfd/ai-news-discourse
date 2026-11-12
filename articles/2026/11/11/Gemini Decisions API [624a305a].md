---
id: "624a305adfa41ec6"
title: "Gemini Decisions API"
url: "https://simonwillison.net/2026/Nov/11/gemini-decisions-api"
link: "https://simonwillison.net/2026/Nov/11/gemini-decisions-api"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-11T22:03:25Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Simon Willison"]
language: "en"
summary: "Gemini Decisions API \nGoogle join Jev and OpenAI in the decision model category with \"Gemini Decision 1\". This new model API is almost identical to Jev: it supports the same three types of questions (yes/no, choice, and rubric-scoring) and even reuses Jev's term \"Noul\" for a yes/no question. \n It's priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is…"
tags: ["ai", "generative-ai", "gemini", "llm-release", "jev", "decision-models"]
orgs: ["Google", "OpenAI", "Anthropic", "Alibaba"]
topics: ["models & research", "business & funding", "robotics & autonomy"]
content_source: "fulltext"
word_count: 273
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Gemini Decisions API

Simon Willison · Simon Willison · 2026-11-11

11th November 2026 - Link Blog
Gemini Decisions API (via) Google join Jev and OpenAI in the decision model category with "Gemini Decision 1". This new model API is almost identical to Jev: it supports the same three types of questions (yes/no, choice, and rubric-scoring) and even reuses Jev's term "Noul" for a yes/no question.
It's priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is free. Jev remains the cheapest of the three, at 4.2 cents per million.
Jev is text (and JSON) only. OpenAI can handle text and images. Gemini Decision 1 is fully multi-model: it covers text, images, audio, video, and PDFs.
I tested it against video by passing these questions to it along with my Yonkers stomping robot video file:
dragon: Does this video have a dragon in it?
robot: Does this video have a robot in it?
france: Is this video set in France?
usa: Is this video set in the USA?
Jev and OpenAI both return 1.0 or 0.0 for yes/no questions, but Gemini insists on being a little less confident than that:
{
  "dragon": {
    "type": "yes_no",
    "probability": 0.04976021841520312
  },
  "robot": {
    "type": "yes_no",
    "probability": 0.9234055387792485
  },
  "france": {
    "type": "yes_no",
    "probability": 0.08329171353166241
  },
  "usa": {
    "type": "yes_no",
    "probability": 0.9230459995157706
  }
}
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
