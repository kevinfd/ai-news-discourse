---
id: "57d6a5f9f9d07e53"
title: "I got tired of doing LLM cost math in spreadsheets, so I built a calculator."
url: "https://reddit.com/r/OpenAI/comments/1xb45s4/i_got_tired_of_doing_llm_cost_math_in"
link: "https://reddit.com/r/OpenAI/comments/1xb45s4/i_got_tired_of_doing_llm_cost_math_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T21:04:27Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["zackku"]
language: "en"
summary: "So I kept running into the same annoying thing. Someone asks “what would this cost us per month on Claude vs GPT vs DeepSeek?” and I’d end up in a spreadsheet, manually updating prices that were already stale by the time I finished. I ended up building a small tool for myself and figured I’d share it. It pulls live pricing and context windows from the OpenRouter API (250+ models), and you plug…"
tags: ["r/OpenAI"]
orgs: ["Anthropic", "DeepSeek"]
topics: ["policy & regulation", "agents & coding"]
content_source: "post"
word_count: 231
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xb45s4/i_got_tired_of_doing_llm_cost_math_in/"
score: null
comments: null
community: "r/OpenAI"
---

# I got tired of doing LLM cost math in spreadsheets, so I built a calculator.

Reddit · zackku · 2026-10-20

So I kept running into the same annoying thing. Someone asks “what would this cost us per month on Claude vs GPT vs DeepSeek?” and I’d end up in a spreadsheet, manually updating prices that were already stale by the time I finished. I ended up building a small tool for myself and figured I’d share it. It pulls live pricing and context windows from the OpenRouter API (250+ models), and you plug in your monthly input/output token volume to see the projected bill. It also has a prompt caching slider, since cache hit rate changes the math a lot for RAG and agent workloads. It also has a rough breakeven estimate for when self-hosting an open-weight model on a rented GPU starts to beat paying per token. It’s a ballpark with assumptions you can tweak, not gospel, because real throughput and utilization vary a lot. Caveats so nobody gets misled: the prices come from OpenRouter, which can differ from going direct to the provider, and I’m not modeling every provider’s cache write fees and TTL quirks perfectly yet. If you spot something wrong, tell me and I’ll fix it. It’s free, no signup: ModelAnalysis.si Genuinely curious what would make it more useful. What do you wish a tool like this showed that existing pricing pages don’t? I’m thinking price history charts next, but I’d rather build what people actually want.
