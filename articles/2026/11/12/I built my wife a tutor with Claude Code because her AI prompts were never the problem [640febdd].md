---
id: "640febdd04ab6bc3"
title: "I built my wife a tutor with Claude Code because her AI prompts were never the problem"
url: "https://reddit.com/r/ClaudeAI/comments/1xu015l/i_built_my_wife_a_tutor_with_claude_code_because"
link: "https://reddit.com/r/ClaudeAI/comments/1xu015l/i_built_my_wife_a_tutor_with_claude_code_because"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T01:41:59Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["astrolafi"]
language: "en"
summary: "My wife spent a semester being handed AI prompts by her teachers. She would paste them, get a wall of text, and still not understand the topic. The prompts were never the problem: nothing in that loop checked whether she had actually learned anything. So I built her a tutor. It is called Aula: a desktop app for macOS, Windows and Linux, with a companion for iPad and iPhone. What it does You give…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 327
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xu015l/i_built_my_wife_a_tutor_with_claude_code_because/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built my wife a tutor with Claude Code because her AI prompts were never the problem

Reddit · astrolafi · 2026-11-12

My wife spent a semester being handed AI prompts by her teachers. She would paste them, get a wall of text, and still not understand the topic. The prompts were never the problem: nothing in that loop checked whether she had actually learned anything. So I built her a tutor. It is called Aula: a desktop app for macOS, Windows and Linux, with a companion for iPad and iPhone. What it does You give it your material (PDFs, slides, photos of the whiteboard, recordings of a class, links) or just a sentence like "Statistics for psychology, final in May". It turns that into a course: short lessons with figures and a worked example before the first exercise, exercises that are checked as you answer them, a notebook of your mistakes, flashcards with spaced repetition, and a mock exam shaped like the real one. It plans the work a little each day until the exam, and it is not tied to one subject. It uses the AI subscription you already pay for (Claude or ChatGPT, or an API key) or a free model that runs on your own machine. No account, no tracking, everything stored on your computer. How Claude Code helped The app is built with Claude Code. I drove it: I described what I wanted, then went module by module, the lesson generator, the exercise checker, the spaced repetition, the desktop shell and its self-updates, the iPad companion, the docs. Claude Code wrote the code, I reviewed and steered it, and when something broke I could paste the error and keep going instead of losing an evening to it. The short film in the links below was painted by code as well. Free to try Repo (AGPL-3.0): https://github.com/luumlabs/aula Downloads for macOS, Windows and Linux: https://github.com/luumlabs/aula/releases/latest The 1:50 film: https://github.com/luumlabs/aula/releases/download/v0.1.0/Aula-film-web.mp4 Everything is free, there is no paid tier yet, and it is early access, so expect rough edges. Happy to answer anything about how it is built.
