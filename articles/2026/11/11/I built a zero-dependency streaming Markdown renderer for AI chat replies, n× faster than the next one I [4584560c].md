---
id: "4584560cf3effc34"
title: "I built a zero-dependency streaming Markdown renderer for AI chat replies, n× faster than the next one I benchmarked"
url: "https://reddit.com/r/LocalLLaMA/comments/1xt3hjd/i_built_a_zerodependency_streaming_markdown"
link: "https://reddit.com/r/LocalLLaMA/comments/1xt3hjd/i_built_a_zerodependency_streaming_markdown"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T00:27:43Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Awkward-Let-4628"]
language: "en"
summary: "I've been building chat UIs for agents and kept running into the same issues with react-markdown: it re-parses the whole reply on every token, so long answers get noticeably slower, and you see raw ** and half-typed [links](htt until the token that closes them arrives. So I wrote my own renderer. It parses incrementally and repairs unfinished syntax while the reply streams: <Markdown…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 237
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xt3hjd/i_built_a_zerodependency_streaming_markdown/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built a zero-dependency streaming Markdown renderer for AI chat replies, n× faster than the next one I benchmarked

Reddit · Awkward-Let-4628 · 2026-11-11

I've been building chat UIs for agents and kept running into the same issues with react-markdown: it re-parses the whole reply on every token, so long answers get noticeably slower, and you see raw ** and half-typed [links](htt until the token that closes them arrives. So I wrote my own renderer. It parses incrementally and repairs unfinished syntax while the reply streams: <Markdown streaming={!done}>{text}</Markdown> On a 100k-character reply it takes 0.25 s of main-thread time in total. markdown-to-jsx takes 2.4 s, Streamdown 6.3 s, and react-markdown didn't finish within the 30 s budget. The benchmark scripts are in the repo if you want to check them. The other part is the syntax. Agents often want to show steps, alternatives or pros and cons, and plain Markdown flattens all of that into bullet lists. So on top of GFM I added a few blocks in the same style as GitHub alerts: > [!STEPS] 1. **Back up the database** 2. **Run the migration** There are also tabs, stats, pros/cons, sources, file trees, and Mermaid and KaTeX support. The source still reads fine as plain Markdown when it isn't rendered. The package exports a system-prompt snippet that teaches the model this syntax. It has no dependencies and comes in at 30 KB gzipped. Its parser passes the CommonMark and GFM spec tests. It doesn't support remark/rehype plugins, so if you rely on those, react-markdown is still the better choice. https://github.com/rsaryev/llx-markdown
