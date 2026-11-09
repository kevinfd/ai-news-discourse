---
id: "223292349511df4b"
title: "My MCP server said \"typed, verified\" and the text never arrived. 20 rounds of Claude and Gemini reviewing each other's code missed it; a real-device run caught it"
url: "https://reddit.com/r/ClaudeAI/comments/1xqz95g/my_mcp_server_said_typed_verified_and_the_text"
link: "https://reddit.com/r/ClaudeAI/comments/1xqz95g/my_mcp_server_said_typed_verified_and_the_text"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T14:08:38Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["feng_sg"]
language: "en"
summary: "I'm the author of noracu, a free, open-source (MIT) local MCP server (noracu on npm) that lets Claude operate macOS apps and Playwright by element_index, with an experimental iPhone layer through Apple's iPhone Mirroring. The bug: on release day Claude was driving my iPhone through noracu's own phone tools, and phone_type reported \"typed, verified\" for text that never reached the field. The…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Apple", "EU"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 435
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqz95g/my_mcp_server_said_typed_verified_and_the_text/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My MCP server said "typed, verified" and the text never arrived. 20 rounds of Claude and Gemini reviewing each other's code missed it; a real-device run caught it

Reddit · feng_sg · 2026-11-08

I'm the author of noracu, a free, open-source (MIT) local MCP server (noracu on npm) that lets Claude operate macOS apps and Playwright by element_index, with an experimental iPhone layer through Apple's iPhone Mirroring. The bug: on release day Claude was driving my iPhone through noracu's own phone tools, and phone_type reported "typed, verified" for text that never reached the field. The picture had changed (most likely a selection highlight), and that change was taken as the paste. It now needs an OCR sighting before reporting "typed, verified" (the device run passed 24/24 checks after the fix). The clipboard rule held: the user's clipboard was not restored on that weak evidence. How 0.2.0 was built with Claude: Claude and Gemini 4 (through Google's agy CLI) ran ten rounds of cross-analysis of the code and docs, then ten rounds arguing against each other's conclusions. The top 10 fixes were split: each model implemented half and reviewed the other half. Claude also ran the real-Mac and iPhone tests through noracu itself. The last round had to produce three lists: agreed, still disputed, and what observation would prove a decision wrong. What each caught: - Gemini: an "expect" parameter starting with "-" (say "-h") made the Python driver's argument parser fail before anything was sent, yet the server reported delivery "unknown" (retry unsafe). It's now passed as one --expect=... token. - Claude, on a real Mac (macOS 27.2): Gemini's "is Notification Center already open?" check counted desktop widget windows as an open Notification Center. It now needs positive evidence. Still disputed at release: Gemini wanted physical clicks moved into the accessibility engine now; Claude wanted that in 0.2.1. 0.2.1 has since moved the keyboard half into the engine; clicks still go through cliclick. It happened again this week. 0.2.7 (out today) puts the pointer back after a physical click so the agent doesn't fight you for the mouse. The first version asked cliclick to move the pointer back; on a real Mac, starting cold, the pointer came back 3 times out of 5. It now moves the pointer back directly and checks where it ended up: 8 of 8 in the same cold-start test. Limits: the iPhone layer is experimental (macOS 15+, python3 with pyobjc, a locked iPhone near the Mac, not available in the EU); the browser has one active tab. Repo: https://github.com/sgInnora/noracu If an agent of yours has reported success that wasn't, I'd like to hear how you caught it. And if you run noracu, bug reports beat stars. (Drafted with Claude Code; I checked every claim against the repo, the CHANGELOG and the test logs.)
