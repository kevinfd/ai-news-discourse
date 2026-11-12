---
id: "5bcbda3aecedfb00"
title: "Opus 5.5 on the API: same prompts, same settings, ~60% more output tokens per call since mid-October (charts from my Console export)"
url: "https://reddit.com/r/ClaudeAI/comments/1xtlbqt/opus_55_on_the_api_same_prompts_same_settings_60"
link: "https://reddit.com/r/ClaudeAI/comments/1xtlbqt/opus_55_on_the_api_same_prompts_same_settings_60"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T15:54:38Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["FlynancialAnalyst"]
language: "en"
summary: "I run a small production app that sends the same analysis prompts to the API every day. Nothing changed on my side: same model ID ( claude-opus-5-5 ), same effort settings (last touched Sept 26), same prompts. My Console cost export says the model got much wordier anyway. Output tokens per input token (standard calls): ~0.69 in Opus 5.5's first three weeks (Sep 21–Oct 11), ~1.09 since Oct 12.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 261
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtlbqt/opus_55_on_the_api_same_prompts_same_settings_60/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Opus 5.5 on the API: same prompts, same settings, ~60% more output tokens per call since mid-October (charts from my Console export)

Reddit · FlynancialAnalyst · 2026-11-11

I run a small production app that sends the same analysis prompts to the API every day. Nothing changed on my side: same model ID ( claude-opus-5-5 ), same effort settings (last touched Sept 26), same prompts. My Console cost export says the model got much wordier anyway. Output tokens per input token (standard calls): ~0.69 in Opus 5.5's first three weeks (Sep 21–Oct 11), ~1.09 since Oct 12. That's about +60%. Input spend (my actual workload) stayed flat. All of the extra cost is output. Weekly spend went from about $86 to $119. Compared with the model's own first three weeks, that's about $120–140 of extra output since Oct 12. Ruled out: price changes, caching, batch, and refusal retries (9 in two months). Method: Opus prices output at 5× input, so output $ ÷ input $ ÷ 5 = output tokens per input token. Claude Code on Ultra shows the same thing. From my local transcripts, output per turn went from ~170 tokens on Opus 5 to ~1,300 at Opus 5.5's launch, and ~1,600–1,700 lately. Thinking is billed as output but hidden by default, so there's no way to see what you're paying for. Anthropic's reset announcement says they "fixed a few small issues that used more limits than intended" and reset subscription limits. If the same issues touched the API, API customers paid for them per token, and nothing covers that. Is anyone else seeing output per call jump on Opus 5.5 since mid-October? And Anthropic: did these issues affect the API too, and will API users be credited?
