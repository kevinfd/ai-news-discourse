---
id: "d8a0ee75b94bc0e4"
title: "peekme: select any text in your agent’s terminal and get an explanation right under it"
url: "https://reddit.com/r/ClaudeAI/comments/1x7ko15/peekme_select_any_text_in_your_agents_terminal"
link: "https://reddit.com/r/ClaudeAI/comments/1x7ko15/peekme_select_any_text_in_your_agents_terminal"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T16:21:37Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Key_Recognition_8112"]
language: "en"
summary: "peekme is a small, free and open-source tool you install once. It lets you select any text in your coding agent's terminal, press Alt+P, and read a short explanation right under it. Esc closes it and the screen is back as it was. It works the same way in Claude Code , Codex CLI , GitHub Copilot CLI and Kiro CLI , and more agents are coming. Next I want it to work in any terminal, with no agent…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 379
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7ko15/peekme_select_any_text_in_your_agents_terminal/"
score: null
comments: null
community: "r/ClaudeAI"
---

# peekme: select any text in your agent’s terminal and get an explanation right under it

Reddit · Key_Recognition_8112 · 2026-10-16

peekme is a small, free and open-source tool you install once. It lets you select any text in your coding agent's terminal, press Alt+P, and read a short explanation right under it. Esc closes it and the screen is back as it was. It works the same way in Claude Code , Codex CLI , GitHub Copilot CLI and Kiro CLI , and more agents are coming. Next I want it to work in any terminal, with no agent running at all. Select a line in a man page or a build log and ask what it means. That should help anyone who is learning their way around the terminal. One answer often leads to the next question, so: - Alt+Q lets you type your own question about the selection. The model your chat runs on answers it, with the whole conversation. - Select words inside an answer to open another box inside it, as many levels deep as you need. - What you asked about stays underlined, also after you resume the chat. A click opens the answer again. If you use /btw or side chats for quick questions, try this for the ones about words already on your screen. Maybe you'll like it more. It runs on your agent's own login, no API key. I test every release on Linux and macOS , also inside tmux , over SSH , with the mouse on and off. Windows isn't supported yet. It's only 0.5.0, so I'd love to hear about your setup, whether it breaks or works. The colors can be customized. npm i -g peekme peekme install https://github.com/GregoryBolshakov/peekme How Claude helped: I built peekme in Rust, with Claude Code helping me along the way. The hard part was learning how each agent draws its screen, so that a box can open inside the chat and move with it when you scroll. Claude helped me read raw recordings of each agent's terminal output and work out where the chat, the selection and the scroll position are. It also helped me write the end-to-end tests that start the real agents, directly and through tmux and SSH, and check every frame while you scroll with a box open. And it helped me make the website https://peekme.dev and the demo GIFs.
