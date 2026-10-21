---
id: "967a44fdf4a05000"
title: "Show HN: Penmentor – Claude marks up your handwritten math like a teacher"
url: "https://github.com/AbdullahAlhariri/penmentor"
link: "https://github.com/AbdullahAlhariri/penmentor"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-20T15:10:54Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["abdullahalharir"]
language: "en"
summary: "You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert\nA maths mentor at the tip of your pen. Press a key while you work by hand: Claude, Gemini or GPT marks your work on the\nscreen like a teacher with coloured…"
tags: []
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "fulltext"
word_count: 412
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50167604"
score: 62
comments: 7
community: "Hacker News"
---

# Show HN: Penmentor – Claude marks up your handwritten math like a teacher

GitHub · abdullahalharir · 2026-10-20

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert
A maths mentor at the tip of your pen. Press a key while you work by hand: Claude, Gemini or GPT marks your work on the
screen like a teacher with coloured pens, gives you hints instead of answers, and shows the idea as a 3Blue1Brown-style animation.
Handwriting in xournal++ → one key → the slip is marked on the page → box the integral → an interactive manim animation.
(video; for a repeatable recording the pen is scripted and the model's answer is a fixed example.)
Why I use it
I study calculus with a pen tablet in xournal++. I kept screenshotting my work into Claude and reading long answers
back, when what I wanted was a teacher looking over my shoulder: circle the mistake, tick what's right, nudge me toward
the next step, and show me why. penmentor is that, one key away, on my own Claude subscription.
How it helps you learn
Hints, not answers. A ladder from a nudge to naming the technique to a faint ghost of the next line: you do
the thinking, which is what makes it stick.
Feedback on your own work. The first real mistake circled where you made it, correct lines ticked, later lines
that inherit the mistake underlined. The marks stay while you keep writing; Esc clears them.
Practice that makes you recall. Questions on your key steps (answer by typing or by writing), find-the-error
drills, "which technique fits?".
See it. Box what you want to understand and get an interactive animation made with 3Blue1Brown's own
manim: drag the bounds, retype a value, watch Riemann sums close in.
Whole page aware. A small xournal++ plugin shares the page you are on, not just what fits on screen.
Works with Claude Code, Codex and Antigravity
penmentor runs on the AI command-line agent you already use, on that subscription. Pick the model in Settings; its
prefix says which agent answers:
Settings lists the agents you have installed. How each one is run and what it sees: the guide.
Linux on X11 (best with i3), with one of those agents logged in (claude, codex or agy), plus rofi, slop,
xdotool and PyQt6. Bind bin/penmentor to a key (example). Setup, keys and how it works: the guide.
