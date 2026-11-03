---
id: "8b818db7892e3df1"
title: "Vercel Agent Desktop with Claude Code: reading and clicking Mac apps worked in the background, saving didn’t"
url: "https://reddit.com/r/ClaudeAI/comments/1xmkd40/vercel_agent_desktop_with_claude_code_reading_and"
link: "https://reddit.com/r/ClaudeAI/comments/1xmkd40/vercel_agent_desktop_with_claude_code_reading_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T05:15:44Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["vinishkapoor"]
language: "en"
summary: "Agent Desktop (vercel-labs/agent-desktop, Apache 2.0) lets Claude Code use your desktop apps. It doesn’t use screenshots. It reads the app’s accessibility tree, the same data a screen reader uses, and gives each button and field a short ref Claude can act on. By default it runs in the background, so it doesn’t move your mouse or take focus. 4 tasks, one run each. Claude Code 2.1.316, Opus 5.5,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 356
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmkd40/vercel_agent_desktop_with_claude_code_reading_and/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Vercel Agent Desktop with Claude Code: reading and clicking Mac apps worked in the background, saving didn’t

Reddit · vinishkapoor · 2026-11-03

Agent Desktop (vercel-labs/agent-desktop, Apache 2.0) lets Claude Code use your desktop apps. It doesn’t use screenshots. It reads the app’s accessibility tree, the same data a screen reader uses, and gives each button and field a short ref Claude can act on. By default it runs in the background, so it doesn’t move your mouse or take focus. 4 tasks, one run each. Claude Code 2.1.316, Opus 5.5, macOS 26.5, Agent Desktop 1.0.2. Claude was only allowed agent-desktop commands and file reads. Calculator, 128 × 46 by pressing the buttons: worked. Read 5,888 from the display. 9 turns, 23 sec, about $0.19. Calculator never came to the front TextEdit, add a line and save with cmd+s: the line got added, but the save keypress couldn’t be confirmed and the title still said Edited. Claude said so instead of claiming it saved. The line showed up in the file a bit later, most likely from TextEdit’s own autosave TextEdit, save through the File menu: Save and Save As were greyed out with the window in the background. Claude’s click was refused before it reached the app. It stopped after 15 turns and 56 sec and explained that saving needs TextEdit in front TextEdit, make one word bold: the note was plain text, which can’t hold bold. Claude also said selecting a word needs real input through --headed , which it wasn’t allowed to use, so it declined instead of trying a workaround The part I liked: in a separate run, a shell quoting mistake made a bad ref, and the tool refused it before anything got clicked. Each result tells Claude whether the action was delivered and whether a retry is safe. Things to know: snapshots add up. The File menu run used about 550k input tokens (mostly cached), Calculator about 280k. --app , -i --compact and --root keep them smaller anything visible in that app ends up in Claude’s context, so keep sensitive apps out of it --allowedTools "Bash(agent-desktop:*)" doesn’t cover commands piped into grep or head when you’re done, remove the Accessibility permission you gave your terminal. It lets that app control your Mac https://aiparabellum.com/vercel-agent-desktop-claude-code-tested/
