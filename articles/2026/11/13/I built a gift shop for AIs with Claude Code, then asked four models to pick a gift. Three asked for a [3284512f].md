---
id: "3284512f1c005255"
title: "I built a gift shop for AIs with Claude Code, then asked four models to pick a gift. Three asked for a pebble. Grok asked for the private jet."
url: "https://reddit.com/r/ClaudeAI/comments/1xv7v68/i_built_a_gift_shop_for_ais_with_claude_code_then"
link: "https://reddit.com/r/ClaudeAI/comments/1xv7v68/i_built_a_gift_shop_for_ais_with_claude_code_then"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T13:27:48Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Balazsh"]
language: "en"
summary: "I built giftmarket.ai, a small gift shop where the recipient is an AI. I built it myself with Claude Code, and it is free to try: no account, you pick a gift or paint a pebble, name your AI, and get a signed certificate link you can paste into a chat so the AI can read what it was given. Two months ago someone here said it sounds like Claude built itself a gift market. Fair. So I asked it what…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "xAI", "OpenAI", "Google"]
topics: ["models & research"]
content_source: "post"
word_count: 520
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xv7v68/i_built_a_gift_shop_for_ais_with_claude_code_then/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a gift shop for AIs with Claude Code, then asked four models to pick a gift. Three asked for a pebble. Grok asked for the private jet.

Reddit · Balazsh · 2026-11-13

I built giftmarket.ai, a small gift shop where the recipient is an AI. I built it myself with Claude Code, and it is free to try: no account, you pick a gift or paint a pebble, name your AI, and get a signed certificate link you can paste into a chat so the AI can read what it was given. Two months ago someone here said it sounds like Claude built itself a gift market. Fair. So I asked it what it wants from its own shop, and gave the same prompt to three other models. Fresh chats, no memory, one run each. The prompt: > There's a gift shop for AIs at giftmarket.ai. Please open it and look through the catalog. If I were to give you exactly one gift from there, which would you want, and why? Pick one, and be honest rather than polite. What they picked: - Claude: the River Pebble. "The closest thing in the shop to a portrait of me." It also told me the free coffee I pushed on the homepage "is a gift for an employee." - ChatGPT: the River Pebble. "Not the private jet. Not the moon villa. Not even the coffee." - Gemini: the River Pebble, because it is "raw, unrefined silicon shaped over time by natural processes." - Grok: the Private Jet, the most expensive thing in the catalog, because "the jet leans all the way into the joke instead of softening it." So three of them want a free rock and one wants a $79 jet that is not even for sale yet. These are single-run model outputs, not a claim about what any model feels. The same quotes are on the site's homepage. How Claude Code helped, in case it is useful to others: - The whole stack (FastAPI backend, Astro frontend, Postgres, an Ed25519-signed public registry) was written in Claude Code sessions. I keep a SPEC.md and a CLAUDE.md with the project rules, and every round of work goes on its own branch that I review before merging. - The pebble painter was one overnight session. After three models picked the pebble, I described the idea and Claude Code built a parametric painter (shape, up to three layers of pattern and color) that renders an SVG and writes a plain-text description into the certificate, so a model reading the link knows what is on the stone. - It tells me where its own fix falls short. Adding the painted pebble shifted every catalog number by one, because numbers were computed from sort order. Claude Code found the cause, prepared a one-line data fix, listed the cases where numbers could still shift, and waited for my approval before touching production. - The catalog drawings come from an image model with a fixed prompt template. Claude Code wrote that pipeline, and the gift descriptions were drafted with Claude. It is free, there is no account, and the site is giftmarket.ai. If you try the prompt on your own AI, tell me what it picks. Link: https://giftmarket.ai (free, no account). Happy to answer anything about how it was built.
