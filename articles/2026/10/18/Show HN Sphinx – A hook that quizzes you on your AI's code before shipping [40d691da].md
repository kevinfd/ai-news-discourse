---
id: "40d691da45f32f89"
title: "Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping"
url: "https://sphinx-six-theta.vercel.app"
link: "https://sphinx-six-theta.vercel.app"
source: "sphinx-six-theta.vercel.app"
domain: "sphinx-six-theta.vercel.app"
source_type: "community"
collector: "hackernews"
date: "2026-10-18T04:33:49Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["critiquebrowser"]
language: "en"
summary: "FOSS, Basically it plugs into your existing coding agent workflow and every time you push to prod it'll throw up a questionnaire that checks if you understand how the code you're pushing works."
tags: []
orgs: ["OpenAI", "Anthropic", "Cursor"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 283
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50137950"
score: 153
comments: 46
community: "Hacker News"
---

# Show HN: Sphinx – A hook that quizzes you on your AI's code before shipping

sphinx-six-theta.vercel.app · critiquebrowser · 2026-10-18

- Free
- FOSS
“Outsource your thinking,
not your understanding.”
— Sun Tzu
Sphinx is a Git hook for agent-assisted development. Before your agent’s code ships, it asks you a question about what that code actually does.
npm install -g sphinx-understand
Built to run on minimal tokens, from your existing coding agent, OpenRouter, or any OpenAI-compatible endpoint.
Sphinx
Your webhook handler now saves the event ID before calling charge(). Stripe times out and sends the same event again. What happens on the retry?
You
It runs twice, so the customer is charged twice.
Sphinx
Not quite. The retry finds the saved ID and returns 200 without charging. But that ID is stored before the charge succeeds. If charge() fails, what does the next retry do?
You
It skips the charge, so the customer is never billed.
- 01 You push. Or your agent does. Git pauses on the branches you protect.
- 02 Sphinx asks. A reviewer that never saw your chat reads the diff and asks what the change does when things go wrong.
- 03 You answer. Get it wrong and you learn why, then try a new scenario. Get it right and the push continues.
Works with Codex, Claude Code, Cursor, OpenCode, and Pi, or plain Git. Your answers never reach the coding agent, and .env files and keys are never opened. In a hurry? sphinx yolo lets pushes through, and every skip is logged.
Start in a minute.
# Node 22.19+ · macOS, Linux, or WSL
npm install -g sphinx-understand
sphinx install
# then push as usual
git push
sphinx install connects Git and your coding agents and asks which model should review. Read the docs for everything else.
