---
id: "7ed07a436da8abfa"
title: "We counted AI-signed PRs in 450 popular GitHub repos. Claude Code signs the most in 279 of 383"
url: "https://reddit.com/r/ClaudeAI/comments/1xpdmtr/we_counted_aisigned_prs_in_450_popular_github"
link: "https://reddit.com/r/ClaudeAI/comments/1xpdmtr/we_counted_aisigned_prs_in_450_popular_github"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T14:05:48Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["coderot_ai"]
language: "en"
summary: "We measured 12 months of merged PRs (Oct 2025 to Sep 2026) in GitHub's most popular repos, across 9 languages, counting the PRs where an AI tool left a signature: co-author trailers, bot authors, agent branches and similar. What we found: Claude Code is the tool that signs the most PRs in 279 of the 383 repos with any AI-signed PRs. Copilot's coding agent leads in 41, Copilot CLI in 24, Cursor…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 271
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpdmtr/we_counted_aisigned_prs_in_450_popular_github/"
score: null
comments: null
community: "r/ClaudeAI"
---

# We counted AI-signed PRs in 450 popular GitHub repos. Claude Code signs the most in 279 of 383

Reddit · coderot_ai · 2026-11-06

We measured 12 months of merged PRs (Oct 2025 to Sep 2026) in GitHub's most popular repos, across 9 languages, counting the PRs where an AI tool left a signature: co-author trailers, bot authors, agent branches and similar. What we found: Claude Code is the tool that signs the most PRs in 279 of the 383 repos with any AI-signed PRs. Copilot's coding agent leads in 41, Copilot CLI in 24, Cursor in 13 and Codex in 12. Big caveat: that's a ranking of what tools record , not of what people use. Claude Code adds its co-author trailer unless you turn it off, and most other tools don't add one. Every number here is a floor. 264 of the 450 repos have committed agent instructions (AGENTS.md, CLAUDE.md and similar), yet half of those sign fewer than 5% of their PRs. Angular has an AGENTS.md, and none of its 4,037 merged PRs in the year carries a signal. The average repo went from 2.3% of PRs AI-signed to 10.3%. The median repo is still at 0.9%: a minority carries the average, and in 17 repos agents now write most merged PRs. A typical AI PR is 2.1× as big as the rest. In our 100 TypeScript and C# repos, AI-heavy repos got no more complex per line than the others, except where their code was also growing fast. Every repo is listed, and the data is a CSV you can download. The post explains the method and its limits: https://coderot.ai/blog/ai-code-rot-in-open-source?utm_source=reddit-claudeai Disclosure: we build coderot, a tool that measures this kind of thing in CI. Happy to answer questions about the method.
