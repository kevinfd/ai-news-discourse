---
id: "9dc848007d998ce8"
title: "I spent two days making a free version of Adobe Acrobat to test the current Spite-Coding Trend"
url: "https://reddit.com/r/ClaudeAI/comments/1x6uzj1/i_spent_two_days_making_a_free_version_of_adobe"
link: "https://reddit.com/r/ClaudeAI/comments/1x6uzj1/i_spent_two_days_making_a_free_version_of_adobe"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T19:23:40Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Jolly_General_7227"]
language: "en"
summary: "I started this as a personal project to get rid of Acrobat on my laptop, and it ended up going further than I expected. It’s now on the Microsoft Store and also runs in the browser. How I used Claude (Opus 5.5, Claude Code): I started by brainstorming the feature list and the tech in a Project. Claude suggested building on PDFium (the PDF engine Chrome uses) through EmbedPDF instead of writing a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft"]
topics: ["products & launches"]
content_source: "post"
word_count: 292
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6uzj1/i_spent_two_days_making_a_free_version_of_adobe/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I spent two days making a free version of Adobe Acrobat to test the current Spite-Coding Trend

Reddit · Jolly_General_7227 · 2026-10-15

I started this as a personal project to get rid of Acrobat on my laptop, and it ended up going further than I expected. It’s now on the Microsoft Store and also runs in the browser. How I used Claude (Opus 5.5, Claude Code): I started by brainstorming the feature list and the tech in a Project. Claude suggested building on PDFium (the PDF engine Chrome uses) through EmbedPDF instead of writing a renderer from scratch. Claude wrote the app itself: a TypeScript/Vite web app, plus a Tauri wrapper so it also runs as a desktop app with no network permission. It set up the GitHub Actions workflows that build the Windows, Mac and Linux installers and the Store package, and wrote Playwright tests that run the app in a headless browser. When I hit problems (empty releases, a broken publish step, a signature that showed up too early in the trailer), I pasted the error or a screenshot and it fixed them. I then set-up the product for Microsoft Store. Claude made the Store screenshots and the trailer by scripting the real app. What it does: Fill forms (even ones without form fields), sign, highlight, comment, merge, compress and redact. Nothing is locked behind a paid tier. Study mode: your PDF on one side, a notebook on the other. Notes are saved inside the app and don’t touch the original PDF unless you export them together. No network access. The app never connects to anything; on Windows the Store handles updates. Free to try: Browser: https://krithickdesign.github.io/Nib-E/ (click Open Nib-E, nothing to install) Windows: https://apps.microsoft.com/detail/9PPKF7HC76Q3 Mac/Linux installers are on the same page This is mostly an experiment for me before I build something original. Honest feedback is very welcome, especially bugs :D
