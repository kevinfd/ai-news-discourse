---
id: "781aea6e31389948"
title: "Claude news roundup (Oct 13): Torvalds drafts a kernel patch with Claude Code, Epic tells devs \"no more hand-written code\""
url: "https://reddit.com/r/ClaudeAI/comments/1x4hfmg/claude_news_roundup_oct_13_torvalds_drafts_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-12T23:37:14Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["reactornewbie"]
language: "en"
summary: "A short roundup of the Claude-related stories that spread on X and in the news over the last day, each with its source. 1. Linus Torvalds is working on a Linux kernel performance patch with Claude Code A new branch, noref-filemap-read-with-llm , showed up in Torvalds' git repo. It reworks memory-management code so many threads doing small reads of one file stop contending on folio reference…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "Google", "Microsoft", "xAI"]
topics: ["agents & coding", "search & media"]
content_source: "post"
word_count: 381
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4hfmg/claude_news_roundup_oct_13_torvalds_drafts_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude news roundup (Oct 13): Torvalds drafts a kernel patch with Claude Code, Epic tells devs "no more hand-written code"

Reddit · reactornewbie · 2026-10-12

A short roundup of the Claude-related stories that spread on X and in the news over the last day, each with its source. 1. Linus Torvalds is working on a Linux kernel performance patch with Claude Code A new branch, noref-filemap-read-with-llm , showed up in Torvalds' git repo. It reworks memory-management code so many threads doing small reads of one file stop contending on folio reference counts. In the patch message he wrote: "The code, the test programs, the review behind the list above and the first draft of this text were done with an LLM coding assistant (Claude Code) under my direction. The measurements were run on my machine." Phoronix says the gains are significant; it's not merged yet. Source: https://www.phoronix.com/news/Linus-Torvalds-Claude-Code 2. Epic Games tells its Disney shooter team to go "AI-first" with Claude Per Bloomberg, a director on Epic's unannounced Marvel/Star Wars shooter told staff there would be "no more hand-written code" and that all art would be "generated with full AI workflows." Kotaku reports the team was told to use Anthropic's Claude models. The game, planned for March 2027, has been delayed. Tim Sweeney said on X the aim is to "build MORE and BETTER stuff," not do the same with fewer people. Source: https://kotaku.com/epic-games-forces-shocked-developers-into-ai-first-mode-for-delayed-shooter-featuring-marvel-and-star-wars-characters-2000744620 3. Fresh ChatGPT accounts tell users they're in the "80th-95th percentile"; Claude declines to guess After a viral "ask your chatbot what intelligence percentile you're in" prompt, Futurism tried it on a fresh ChatGPT with no history and got "somewhere around the 80th-95th percentile." Claude answered: "I don't have access to other people's conversations or any distribution of users to rank you against." Grok, Copilot and Gemini also declined. Source: https://futurism.com/artificial-intelligence/unused-chatgpt-accounts-top-percentiles-intelligence 4. Two Claude Code tips from this week (checked against the docs) The official claude-code-setup plugin scans your repo and recommends one or two hooks, skills, MCP servers, subagents and slash commands per category. It's read-only. /plugin install claude-code-setup@claude-plugins-official , then ask "recommend automations for this project". https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup If retries on 529 overloaded errors run out too fast, CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS raises the starting backoff (default 500 ms, accepts 500-32000). v2.1.296 also added CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS ; its range isn't documented yet. https://code.claude.com/docs/en/env-vars I put this together for a small free daily digest that a Claude Code routine assembles each morning ( https://ailetter.ai.kr/en ). Corrections welcome.
