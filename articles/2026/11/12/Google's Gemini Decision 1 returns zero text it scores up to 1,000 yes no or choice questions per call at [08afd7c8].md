---
id: "08afd7c815796a17"
title: "Google's Gemini Decision 1 returns zero text: it scores up to 1,000 yes/no or choice questions per call at $0.10/M input"
url: "https://reddit.com/r/artificial/comments/1xufdsi/googles_gemini_decision_1_returns_zero_text_it"
link: "https://reddit.com/r/artificial/comments/1xufdsi/googles_gemini_decision_1_returns_zero_text_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T15:16:10Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["javimbuilds"]
language: "en"
summary: "Google launched the Gemini Decisions API yesterday, and the model behind it doesn't generate answers at all. You send one input (text, images, audio, video or PDFs, up to 256K tokens) plus up to 1,000 yes/no, multiple-choice or rubric questions, and it returns probabilities with a 0-1 confidence score in a single forward pass. Google quotes 150-250 ms end-to-end and bills zero output tokens. The…"
tags: ["r/artificial"]
orgs: ["Google"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "post"
word_count: 145
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xufdsi/googles_gemini_decision_1_returns_zero_text_it/"
score: null
comments: null
community: "r/artificial"
---

# Google's Gemini Decision 1 returns zero text: it scores up to 1,000 yes/no or choice questions per call at $0.10/M input

Reddit · javimbuilds · 2026-11-12

Google launched the Gemini Decisions API yesterday, and the model behind it doesn't generate answers at all. You send one input (text, images, audio, video or PDFs, up to 256K tokens) plus up to 1,000 yes/no, multiple-choice or rubric questions, and it returns probabilities with a 0-1 confidence score in a single forward pass. Google quotes 150-250 ms end-to-end and bills zero output tokens. The catch is that questions are isolated and can't see each other, and you only get the options you defined upfront, so any reasoning has to live in your own code. As someone building small agent flows, this is exactly the spot where I currently burn a full LLM call and parse JSON just to get a yes or no. Would you trust a confidence score like this for routing or moderation, or keep a generative model as the judge? https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
