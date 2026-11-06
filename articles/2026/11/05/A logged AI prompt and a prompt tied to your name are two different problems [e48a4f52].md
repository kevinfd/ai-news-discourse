---
id: "e48a4f523cd8ea8e"
title: "A logged AI prompt and a prompt tied to your name are two different problems"
url: "https://reddit.com/r/artificial/comments/1xoj0n6/a_logged_ai_prompt_and_a_prompt_tied_to_your_name"
link: "https://reddit.com/r/artificial/comments/1xoj0n6/a_logged_ai_prompt_and_a_prompt_tied_to_your_name"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T13:45:38Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["tres_pares"]
language: "en"
summary: "Most AI privacy talk is about whether your prompt gets logged. OpenAI's API, for example, keeps abuse monitoring logs for up to 30 days unless it approves a customer for zero data retention, and those logs can include prompts. The other question is whether a log can be tied to you. With your own API key, every prompt sits under your account, and a VPN only hides your IP. A router puts its own…"
tags: ["r/artificial"]
orgs: ["OpenAI"]
topics: ["policy & regulation"]
content_source: "post"
word_count: 235
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xoj0n6/a_logged_ai_prompt_and_a_prompt_tied_to_your_name/"
score: null
comments: null
community: "r/artificial"
---

# A logged AI prompt and a prompt tied to your name are two different problems

Reddit · tres_pares · 2026-11-05

Most AI privacy talk is about whether your prompt gets logged. OpenAI's API, for example, keeps abuse monitoring logs for up to 30 days unless it approves a customer for zero data retention, and those logs can include prompts. The other question is whether a log can be tied to you. With your own API key, every prompt sits under your account, and a VPN only hides your IP. A router puts its own account between you and the provider, but it still sees your account and your prompt together, so you're trusting its policy. Some setups split those two things instead. A relay knows who you are but only gets encrypted data, and a secure enclave reads the prompt without seeing who sent it. Your client can also verify what code the enclave is running. The model provider still gets the prompt, but nothing sent with it identifies you. It only holds if the relay and enclave don't collude, though, and anything you type into the prompt can still give you away. OpenAI's policy if you want to check: https://developers.openai.com/api/docs/guides/your-data If you could only have one, which would you pick: a provider that keeps nothing, or a log that can't be tied to you? What would change your answer? Disclosure: I work at Dreamfort AI, private AI for chat, image, and video which uses the relay and enclave approach, so I'm biased toward it.
