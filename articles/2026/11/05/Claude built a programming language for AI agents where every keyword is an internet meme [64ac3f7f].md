---
id: "64ac3f7fa159b539"
title: "Claude built a programming language for AI agents where every keyword is an internet meme"
url: "https://reddit.com/r/ClaudeAI/comments/1xook9e/claude_built_a_programming_language_for_ai_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xook9e/claude_built_a_programming_language_for_ai_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:24:29Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["jvon5808"]
language: "en"
summary: "i had a dumb idea a while ago. what if ai agents had their own programming language, but every keyword was an internet meme? so i built Memesis with Claude Code. it's an actual interpreted language with its own .meme files, parser, runtime and CLI. what it does pepe = an agent, npc = a function sus = untrusted data yolo = irreversible actions apu = ask a human, thonk = call an ai model…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 279
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xook9e/claude_built_a_programming_language_for_ai_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude built a programming language for AI agents where every keyword is an internet meme

Reddit · jvon5808 · 2026-11-05

i had a dumb idea a while ago. what if ai agents had their own programming language, but every keyword was an internet meme? so i built Memesis with Claude Code. it's an actual interpreted language with its own .meme files, parser, runtime and CLI. what it does pepe = an agent, npc = a function sus = untrusted data yolo = irreversible actions apu = ask a human, thonk = call an ai model trustmebro = mark untrusted data as reviewed chad / virgin / F = try / catch / finally touchgrass = sleep the funny part is that some of these actually make sense for ai agents. for example, data fetched from the internet gets marked as sus , and the runtime blocks it from reaching irreversible actions without an explicit trust check. there's also memesis check to catch issues before running anything and memesis explain to translate meme code into plain english. how Claude Code helped i came up with the concept and the meme keywords, then used Claude Code to implement the language itself. it wrote the lexer, parser, interpreter and CLI. the hardest part was the sus and yolo safety system. i described how untrusted data should be handled, and Claude Code implemented the tracking and static checks. it also wrote 34 tests and helped build the animated examples in the README using Playwright. it supports multiple agents, parallel tasks, Claude and local models through Ollama. GitHub: https://github.com/tasdongyro/memesis it's completely free, open source under MIT and runs locally without signup. still experimental, but i'm curious what other Claude Code users think. what would you add or change? is there anything you'd approach differently?
