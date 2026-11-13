---
id: "e62f18aceab4ebcd"
title: "update: a user says claude code moved 11gb in manual mode and logged approvals they never saw"
url: "https://reddit.com/r/artificial/comments/1xuiikp/update_a_user_says_claude_code_moved_11gb_in"
link: "https://reddit.com/r/artificial/comments/1xuiikp/update_a_user_says_claude_code_moved_11gb_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T17:13:47Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Glad-Concept-6809"]
language: "en"
summary: "so remember when i said i'm not letting an AI touch my files without me clicking ok first? yeah about that. this is just one person's report, not independently confirmed. they filed it on github last friday. they were using claude code on windows in manual approval mode, and they even had a rule that those powershell commands should stop and ask first. they say they never saw a single prompt.…"
tags: ["r/artificial"]
orgs: []
topics: ["products & launches"]
content_source: "post"
word_count: 194
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xuiikp/update_a_user_says_claude_code_moved_11gb_in/"
score: null
comments: null
community: "r/artificial"
---

# update: a user says claude code moved 11gb in manual mode and logged approvals they never saw

Reddit · Glad-Concept-6809 · 2026-11-12

so remember when i said i'm not letting an AI touch my files without me clicking ok first? yeah about that. this is just one person's report, not independently confirmed. they filed it on github last friday. they were using claude code on windows in manual approval mode, and they even had a rule that those powershell commands should stop and ask first. they say they never saw a single prompt. just some text from the assistant about what would get removed. then it ran 9 powershell commands that moved about 11 gigs of temp files and old app data to the recycle bin. the log says the user hit yes, once, for every command. they say they never did. three of those "approvals" even got recorded while they were typing messages asking where the recycle bin files came from. the bin got emptied later and the files are gone https://github.com/anthropics/claude-code/issues/108022 (writeup here if you don't want to read the github thread https://techbroz.com/chaos/claude-code-invisible-prompts-delete-11gb/ ) like if the click-ok prompt can get logged without you ever seeing it, what's the point of the click?? has anyone else had an approval prompt just... not show up?
