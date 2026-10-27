---
id: "36fa57e641092193"
title: "Kanzo, a tiny self-hosted kanban board you and your coding agents can share (~5k lines, one 4 MB binary)"
url: "https://reddit.com/r/ClaudeAI/comments/1xgbl62/kanzo_a_tiny_selfhosted_kanban_board_you_and_your"
link: "https://reddit.com/r/ClaudeAI/comments/1xgbl62/kanzo_a_tiny_selfhosted_kanban_board_you_and_your"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T22:41:29Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["allmudi"]
language: "en"
summary: "Apparently in 2026 everyone has to build their own task board, usually with Docker, three services and half a GB of RAM to show a todo list. I built the opposite: a kanban board in your browser plus an MCP server, in one small Rust binary. Tell Claude Code or Codex \"take the next task from kanzo\" and it moves the card and comments as it works, which is more than I do.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 284
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgbl62/kanzo_a_tiny_selfhosted_kanban_board_you_and_your/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Kanzo, a tiny self-hosted kanban board you and your coding agents can share (~5k lines, one 4 MB binary)

Reddit · allmudi · 2026-10-26

Apparently in 2026 everyone has to build their own task board, usually with Docker, three services and half a GB of RAM to show a todo list. I built the opposite: a kanban board in your browser plus an MCP server, in one small Rust binary. Tell Claude Code or Codex "take the next task from kanzo" and it moves the card and comments as it works, which is more than I do. https://github.com/emanuele-em/kanzo I liked Vikunja but wanted zero setup. The one rule was keeping it small, which these days feels almost rebellious: ~5k lines total. You can read the whole thing in an afternoon 4.3 MB binary with SQLite inside, ~4 MB RAM idle starts in 3 ms, a 3,000-task board loads in 17 ms light on your agents too: ~800 tokens of tools, short replies no account, no cloud, no Docker. Syncs between machines through your own private git repo if you want one-line install on macOS/Linux, runs fine on a Raspberry Pi How Claude helped: I built it with Claude Code. I set the rules (no frameworks, few dependencies, every line has to earn its place) and Claude wrote a good part of the code, then I went back and cut. It was also great for measuring things: binary size, memory and token counts, so we could check each change actually made it smaller. And once the MCP server worked, Claude Code was picking kanzo tasks from kanzo itself. It's free and open source (AGPL). To try it: curl -LsSf https://github.com/emanuele-em/kanzo/releases/latest/download/kanzo-installer.sh | sh then run kanzo . Still early. If you've got ideas on how to make it even smaller, PRs very welcome, deleting code counts as a feature here.
