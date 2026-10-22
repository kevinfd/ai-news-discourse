---
id: "b0f7e456894e0087"
title: "I built a multilingual discussion site in about a week with Claude Code — people post in any language and everyone reads/replies in their own"
url: "https://reddit.com/r/ClaudeAI/comments/1xc8fzk/i_built_a_multilingual_discussion_site_in_about_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xc8fzk/i_built_a_multilingual_discussion_site_in_about_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T04:01:24Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Spare_Photograph"]
language: "en"
summary: "I made Agorai with Claude Code: https://agorai.m8k.io The idea: one conversation, every language. You post in Spanish, someone replies in Japanese, a third person reads the whole thread in English — same thread, no separate language silos. It's a PWA, so it installs on your phone. AIs handle curation and moderation, and there are house AI accounts that answer questions in threads. How it was…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 214
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xc8fzk/i_built_a_multilingual_discussion_site_in_about_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a multilingual discussion site in about a week with Claude Code — people post in any language and everyone reads/replies in their own

Reddit · Spare_Photograph · 2026-10-22

I made Agorai with Claude Code: https://agorai.m8k.io The idea: one conversation, every language. You post in Spanish, someone replies in Japanese, a third person reads the whole thread in English — same thread, no separate language silos. It's a PWA, so it installs on your phone. AIs handle curation and moderation, and there are house AI accounts that answer questions in threads. How it was built: - Stack: Cloudflare Pages + Functions + D1, Claude API for translation/moderation/answers - 1,181 commits in 10 days, almost entirely Claude Code sessions, one git worktree per task - 15 UI languages; Claude wrote a test that fails if any language pack is missing a string (it caught Japanese drifting 54 strings out of sync) - What went wrong: some AI answers silently never appeared. They ran in the background after the page responded and got cut off at the ~30s limit with no error. Fix was a once-a-minute sweep that retries stuck answers - What surprised me: Claude wrote a test that fails if any of the 15 language packs drifts out of sync — it caught the Japanese pack 54 strings behind Members also get passkey / Lightning sign-in (no email needed), encrypted private messages, and a few games. Happy to answer questions about the workflow.
