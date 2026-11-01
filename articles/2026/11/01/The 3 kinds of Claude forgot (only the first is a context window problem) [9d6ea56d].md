---
id: "9d6ea56d8150b369"
title: "The 3 kinds of \"Claude forgot\" (only the first is a context window problem)"
url: "https://reddit.com/r/ClaudeAI/comments/1xkv0oo/the_3_kinds_of_claude_forgot_only_the_first_is_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xkv0oo/the_3_kinds_of_claude_forgot_only_the_first_is_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T05:27:05Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["ombre-ai"]
language: "en"
summary: "When Claude goes sideways on a long piece of work, it usually gets filed under \"it forgot.\" A technical write-up from early October (opencraftai's blog) argues that label covers three separate problems: Mid-session. A rule or goal you set early in the conversation stops shaping the replies. The write-up's explanation is oldest-first trimming, where the opening frame is the first thing to go.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 231
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkv0oo/the_3_kinds_of_claude_forgot_only_the_first_is_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# The 3 kinds of "Claude forgot" (only the first is a context window problem)

Reddit · ombre-ai · 2026-11-01

When Claude goes sideways on a long piece of work, it usually gets filed under "it forgot." A technical write-up from early October (opencraftai's blog) argues that label covers three separate problems: Mid-session. A rule or goal you set early in the conversation stops shaping the replies. The write-up's explanation is oldest-first trimming, where the opening frame is the first thing to go. That's their account of one mechanism, and I'd be careful about applying it to any specific tool. Between sessions. You start a new chat and you're at zero. Between projects. What you taught it in one project doesn't follow you into the next. Their point is that only #1 is a window problem. #2 and #3 are continuity problems, so a bigger window doesn't touch them, and saved facts like preferences or your name don't obviously cover working state: decisions made, options you already rejected. A quick way to use this: next time it goes wrong, ask whether it happened inside one conversation, the next time you opened one, or in a new project. The answer tells you which problem you actually have. For people using Claude on long projects: Which of the three hits you most? What do you put in a notes file or project instructions to cover #2 and #3, and what do you still end up retyping? Is there a fourth scope this misses
