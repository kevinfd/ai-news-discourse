---
id: "7d446caae4666450"
title: "I have ADHD and kept losing hours to YouTube while studying, so I built a focus app with Claude (free + open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xx75ii/i_have_adhd_and_kept_losing_hours_to_youtube"
link: "https://reddit.com/r/ClaudeAI/comments/1xx75ii/i_have_adhd_and_kept_losing_hours_to_youtube"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T21:22:38Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Trivialli"]
language: "en"
summary: "Hey everyone, wanted to share something I actually use every day now. I have ADHD and studying for exams was getting rough. I'd sit down, open my notes, and somehow 40 minutes later I'm on YouTube with no memory of how I got there. Pomodoro timers didn't help because nothing stopped me drifting mid-session. So I asked Claude to help me make a desktop app that reminds me to study every time I get…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "ByteDance"]
topics: ["search & media", "products & launches", "models & research"]
content_source: "post"
word_count: 366
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx75ii/i_have_adhd_and_kept_losing_hours_to_youtube/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I have ADHD and kept losing hours to YouTube while studying, so I built a focus app with Claude (free + open source)

Reddit · Trivialli · 2026-11-15

Hey everyone, wanted to share something I actually use every day now. I have ADHD and studying for exams was getting rough. I'd sit down, open my notes, and somehow 40 minutes later I'm on YouTube with no memory of how I got there. Pomodoro timers didn't help because nothing stopped me drifting mid-session. So I asked Claude to help me make a desktop app that reminds me to study every time I get distracted. That one message turned into StudyGuard. What it does: - Watches which window you're on during a study session. If you drift to YouTube/Reddit/TikTok etc. for too long, a popup tells you to get back to it - Strict mode, where anything that isn't a study app counts as a distraction - Breaks, up to 4 x 5 min per hour, so you can rest without losing the whole afternoon - Session checklist so you always know your next small step - "Parking lot" to dump random thoughts into so you can deal with them later - Exam/deadline countdown + daily goal streak - Water, movement and meal reminders - Habit tracker that shows where your time actually went - Compact always-on-top timer, dark and light mode - Everything stays on your PC: no account, nothing uploaded How I built it: no fancy prompt or workflow, just a lot of back and forth. I'd describe what I wanted in plain English, try it, screenshot anything that looked off and say "fix this". It ended up as a single Python file with no extra packages. Claude also made the icon, built the Windows.exe and walked me through putting it on GitHub. Fun side story: it originally had an animated training buddy in the corner. Claude wouldn't draw Goku for me (copyright lol) so it became a pixel art knight that swung his sword while I studied. I eventually cut him for a cleaner look but I miss him a bit. It's free and open source: https://github.com/GigaGoose287/StudyGuard Windows only for now (Mac maybe later). It's unsigned, so Windows will warn you the first time. Click More info > Run anyway. Would really appreciate any feedback or feature ideas, it's my first proper project!
