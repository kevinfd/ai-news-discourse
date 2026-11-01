---
id: "001417c1022d51c5"
title: "I built a live file tree for Claude Code so I can see what it reads and edits (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xkzlis/i_built_a_live_file_tree_for_claude_code_so_i_can"
link: "https://reddit.com/r/ClaudeAI/comments/1xkzlis/i_built_a_live_file_tree_for_claude_code_so_i_can"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T10:19:01Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["mCadamek"]
language: "en"
summary: "Why I built it I used to spend most of my day in a code editor. Lately I’m in the Claude app and the CLI more and more, and I started losing touch with the codebase: which files changed, what got committed, whether a new pattern was creeping in. What it does A pane beside the chat that updates while Claude works: Files Claude reads turn purple, files it edits turn orange, with lines added and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research", "search & media"]
content_source: "post"
word_count: 358
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkzlis/i_built_a_live_file_tree_for_claude_code_so_i_can/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a live file tree for Claude Code so I can see what it reads and edits (free, open source)

Reddit · mCadamek · 2026-11-01

Why I built it I used to spend most of my day in a code editor. Lately I’m in the Claude app and the CLI more and more, and I started losing touch with the codebase: which files changed, what got committed, whether a new pattern was creeping in. What it does A pane beside the chat that updates while Claude works: Files Claude reads turn purple, files it edits turn orange, with lines added and removed Every file touched this turn or this session, and what’s committed vs not A card showing what Claude is doing right now Search, and a ⋯ menu on each file to @-mention it (handy for “explain this new function”), view its diff, or open it in your editor It works in the desktop app, the VS Code extension and the terminal, on macOS and Linux. It’s read-only, and nothing leaves your machine. How I built it with Claude Code I built the whole thing with Claude Code, with the pane open beside the chat the whole time, so it was showing Claude working on its own code. I described what I wanted and checked each change in the pane, and Claude wrote the code and the tests. One bug taught me something worth passing on. In the terminal, the file-type labels showed up as solid coloured blocks. Claude traced it to the colours: they carried a transparency value, which the desktop app blends but the terminal draws as solid, so each label sat inside a block of its own colour. Claude wrote a test that fails if the terminal is ever handed a see-through colour, then fixed the pane until it passed. If you’re building a Claude Code mod for more than one surface, test each surface separately: something that looks right on the desktop can break in the terminal. Free to try It’s free and open source (MIT). Install it from a terminal: claude plugin marketplace add Marius-Adam/claude-files-pane claude plugin install files-pane@marius-adam Restart Claude Code and the pane opens beside the chat. https://github.com/Marius-Adam/claude-files-pane If you work on bigger changes than I do, I’d like to hear how it holds up.
