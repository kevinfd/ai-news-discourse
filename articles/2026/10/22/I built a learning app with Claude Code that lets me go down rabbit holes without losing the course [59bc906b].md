---
id: "59bc906b2297115d"
title: "I built a learning app with Claude Code that lets me go down rabbit holes without losing the course"
url: "https://reddit.com/r/ClaudeAI/comments/1xc4r3y/i_built_a_learning_app_with_claude_code_that_lets"
link: "https://reddit.com/r/ClaudeAI/comments/1xc4r3y/i_built_a_learning_app_with_claude_code_that_lets"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T00:58:30Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["graywolf724"]
language: "en"
summary: "I learn by depth first searching a topic until it makes sense in my head. When I tried to learn genomics last year, Claude was great for that. But after a week I had a pile of long chats and no idea what I'd actually covered or what came next. Online courses either started at high school biology or jumped straight to advanced RNA. So I built Pomelo, with Claude Code, on top of Claude. You tell…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches", "jobs & society", "health & science"]
content_source: "post"
word_count: 411
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xc4r3y/i_built_a_learning_app_with_claude_code_that_lets/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a learning app with Claude Code that lets me go down rabbit holes without losing the course

Reddit · graywolf724 · 2026-10-22

I learn by depth first searching a topic until it makes sense in my head. When I tried to learn genomics last year, Claude was great for that. But after a week I had a pile of long chats and no idea what I'd actually covered or what came next. Online courses either started at high school biology or jumped straight to advanced RNA. So I built Pomelo, with Claude Code, on top of Claude. You tell it what you want to learn, Claude asks a few questions to figure out what you already know, and it builds a short course around the gap. One chapter a day. Each chapter has real sources on them with quick quizzes I like to highlight something on a slide and ask about it. I go down the rabbit hole in a side chat, and then I can back to the chapter where I left it. This makes learning with Claude feel like it adds up for me instead of scattering The first slides take about 90 seconds to show up (sped up in the video), and I'm working on that. It's free to try with an account. https://learnpomelo.com ---- How Claude Code helped : Claude Code wrote most of the code. That includes the web app (Next.js + Supabase) and the iPhone app (Expo). I made a Claude Code skill that takes one Linear ticket and does the whole loop: new worktree, a design mockup for me to approve, a plan review, the code, a demo video, then a PR. I review and merge. I also had it write small eval scripts to measure things before I changed them. One measured how fast slides stream back from the API. How Claude runs inside it : Claude writes the placement questions, the course plan, and each chapter. A chapter is one tool call that returns the whole slide deck. At first that meant a ~2.5 min spinner. With eager input streaming, the first slide's text comes back in 4 to 5 s, so the chapter now opens on its first slides while the rest are still being written. The course plan acts like a contract, which keeps chapter 6 from forgetting what chapter 2 said (mostly). Free to try : go to learnpomelo.com , sign up with Google or email, and type any topic. Chapter 1 of every course is free. Later chapters need approval from a waitlist for now while I watch API costs.
