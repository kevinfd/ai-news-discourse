---
id: "df5c400b60dd90df"
title: "I built a Mac app with Claude Code that coaches you to use Claude Code better"
url: "https://reddit.com/r/ClaudeAI/comments/1xqjb21/i_built_a_mac_app_with_claude_code_that_coaches"
link: "https://reddit.com/r/ClaudeAI/comments/1xqjb21/i_built_a_mac_app_with_claude_code_that_coaches"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T22:55:31Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["iLrama"]
language: "en"
summary: "I kept hitting my 5-hour limit without knowing why, so I built Nudge, a free Mac menu bar app that reads your Claude Code chats on your Mac and tells you what’s worth changing. What I learned about where tokens go (useful even if you never install it) Every message re-reads the whole chat. In a 400K chat, each message costs about 7 times more than in a fresh one. Ask for a handoff summary and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 419
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqjb21/i_built_a_mac_app_with_claude_code_that_coaches/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Mac app with Claude Code that coaches you to use Claude Code better

Reddit · iLrama · 2026-11-07

I kept hitting my 5-hour limit without knowing why, so I built Nudge, a free Mac menu bar app that reads your Claude Code chats on your Mac and tells you what’s worth changing. What I learned about where tokens go (useful even if you never install it) Every message re-reads the whole chat. In a 400K chat, each message costs about 7 times more than in a fresh one. Ask for a handoff summary and start a new chat from it. Idle chats cost more. After a chat sits idle long enough, Claude’s cache expires and your next message pays full price to re-read everything. Helper agents inherit your model. If your main model is Opus, every subagent runs on Opus too. Setting CLAUDE_CODE_SUBAGENT_MODEL in the env block of ~/.claude/settings.json moves them all to a cheaper model. On my week, Nudge estimated that moving them to Haiku would cut that cost from $129 to about $22. Late compaction is expensive. Chats that grow past 300K before compacting pay for every message at that size. CLAUDE_CODE_AUTO_COMPACT_WINDOW sets when compaction happens. Stop retyping instructions. If you paste the same instructions into every chat, put them in CLAUDE.local.md at the project root. Claude Code reads it like CLAUDE.md, but it’s meant to stay out of git. What Nudge does with that Warns you once before a costly message, like waking an idle chat or sending a huge paste. Start fresh: one click summarizes a long chat and opens a new one from it. Offers to make the fixes above for you. It shows the exact line and file first, changes nothing until you click, and every change has Undo. A few days later, it checks whether the fix helped. How Claude helped The whole app: Claude Code wrote all of it in SwiftUI. I described what I wanted and how it should look and feel, then reviewed every screen. Seeing without a screen: Claude Code can’t see the app, so it built a mode that draws each screen to an image. It checks its own layouts that way, and I review the real thing. Self-testing: a built-in self-test checks the panel’s interactions and the file edits before each release. Performance: the first animated version used about 30% of a CPU core while idle. Claude profiled it and cut it to about 0%. Free to try. macOS 26+, also supports Codex, and chats never leave your Mac. https://nudgeformac.com Happy to answer questions about building a native app this way without reading code.
