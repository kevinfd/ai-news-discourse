---
id: "7842a2237e2e614e"
title: "Found a weird issue with Claude Code's native eval grader over an invisible space"
url: "https://reddit.com/r/ClaudeAI/comments/1xhkfpl/found_a_weird_issue_with_claude_codes_native_eval"
link: "https://reddit.com/r/ClaudeAI/comments/1xhkfpl/found_a_weird_issue_with_claude_codes_native_eval"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T10:32:18Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["maverick_man1111"]
language: "en"
summary: "I have an open source Evaluation project. When I was testing my grader, I found that claude code marked the correct python code as wrong and vice versa for the incorrect. When I digged deeper it was caused due to a single invisible character. Then I checked other tools to see ,they had the same issue- Langchain OpenEvals Promptfoo Nvidia SkillEvaluator It was a small fix - I added a small,…"
tags: ["r/ClaudeAI"]
orgs: ["Nvidia", "Anthropic"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 139
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xhkfpl/found_a_weird_issue_with_claude_codes_native_eval/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Found a weird issue with Claude Code's native eval grader over an invisible space

Reddit · maverick_man1111 · 2026-10-28

I have an open source Evaluation project. When I was testing my grader, I found that claude code marked the correct python code as wrong and vice versa for the incorrect. When I digged deeper it was caused due to a single invisible character. Then I checked other tools to see ,they had the same issue- Langchain OpenEvals Promptfoo Nvidia SkillEvaluator It was a small fix - I added a small, automatically generated note listing the exact unicode character and their positions, without changing the original answer, which improved the judgements drastically. I was able to reproduce the same issue in Claude Code's native claude plugin eval grader. I submitted PRs to fix to Nvidia, OpenEvals and Promptfoo, Nvidia has already approved the fix. Full reports can be found here https://driftproofhq.com/invisible-space/ Have any one else encountered the same before?
