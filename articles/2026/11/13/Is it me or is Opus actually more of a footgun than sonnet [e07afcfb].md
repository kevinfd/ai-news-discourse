---
id: "e07afcfb432cbea7"
title: "Is it me or is Opus actually more of a footgun than sonnet"
url: "https://reddit.com/r/ClaudeAI/comments/1xvj61w/is_it_me_or_is_opus_actually_more_of_a_footgun"
link: "https://reddit.com/r/ClaudeAI/comments/1xvj61w/is_it_me_or_is_opus_actually_more_of_a_footgun"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T20:43:55Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["YourVillainArc"]
language: "en"
summary: "Has anyone else found Claude harder to work with lately, despite how capable it is? I use my own provider-agnostic orchestration layer, so I regularly switch between coding agents. For most of the last year, Claude was my preference. Sonnet handled my open-ended instructions more intuitively than alternatives like Codex or Cursor. In my experience, making instructions too restrictive often makes…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 441
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvj61w/is_it_me_or_is_opus_actually_more_of_a_footgun/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Is it me or is Opus actually more of a footgun than sonnet

Reddit · YourVillainArc · 2026-11-13

Has anyone else found Claude harder to work with lately, despite how capable it is? I use my own provider-agnostic orchestration layer, so I regularly switch between coding agents. For most of the last year, Claude was my preference. Sonnet handled my open-ended instructions more intuitively than alternatives like Codex or Cursor. In my experience, making instructions too restrictive often makes agents struggle rather than perform better. Over the last two months, though, Sonnet has felt noticeably worse for my workflow. My setup and instructions haven’t changed, but the responses have become longer, harder to follow, and full of tangents. I tried Opus hoping it would handle things more intuitively, but it amplified the same problems. I still plan interactively before handing over implementation stories. The issue is that planning now involves reading an essay about everything the agent notices, including things that aren’t actually problems. I spend more time deciding whether its concerns are relevant than making progress on the task. For example, I might ask for a feature with a simple API endpoint. Claude identifies a supposed “gap” and spends a paragraph explaining it. After unpacking the explanation, I realize the gap doesn’t matter for what we’re building, or isn’t a gap at all. If I’m unsure and ask it to elaborate, that can make things worse. It seems to treat my request for clarification as validation of its concern. Instead of checking whether the issue is real, it becomes more committed to explaining why we need to solve it. This past week, I put Cursor’s agent in the lead, and it’s felt much closer to the old Sonnet: clear, concise, and focused. It doesn’t catch everything Claude catches, but it also doesn’t turn a straightforward task into four separate discussions. That’s the tradeoff I’m struggling with. Claude may identify four genuine issues among ten concerns, but evaluating all ten can cost me hours. Cursor gets the implementation moving, and we can catch missed issues during review or testing. The best way I can describe it is that the output feels like my own ADHD thought process, amplified tenfold: every possibility opens another tangent, and everything feels important enough to explain. I’m not asking it to stop thinking critically. I need it to filter those thoughts and distinguish actual blockers from passing observations. Instead, I feel like I’m managing its attention as well as my own. Has anyone else noticed this shift, or found a way to get back to the more focused behavior? My preference is to fail fast, test, and iterate. I’d rather fix a concrete problem than spend three hours debating one that might not exist.
