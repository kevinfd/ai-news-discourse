---
id: "c47a89a8410210d4"
title: "I made a Claude Code mod that lets you see what your agents and subagents are doing live without leaving Claude."
url: "https://reddit.com/r/ClaudeAI/comments/1xpesbb/i_made_a_claude_code_mod_that_lets_you_see_what"
link: "https://reddit.com/r/ClaudeAI/comments/1xpesbb/i_made_a_claude_code_mod_that_lets_you_see_what"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T14:55:26Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["kontrollable"]
language: "en"
summary: "I mainly use Claude Code via the desktop app and with Opus 5.5 and the newer models delegating lots of work to subagents behind the scenes. Claude doesn't exactly make it easy to tell which ones are still working, which have finished and which are stuck going in circles. So I built Apiarius, a Claude Code mod that adds a live agent deck that shows every agent and subagent, what each one is doing…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 301
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpesbb/i_made_a_claude_code_mod_that_lets_you_see_what/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Claude Code mod that lets you see what your agents and subagents are doing live without leaving Claude.

Reddit · kontrollable · 2026-11-06

I mainly use Claude Code via the desktop app and with Opus 5.5 and the newer models delegating lots of work to subagents behind the scenes. Claude doesn't exactly make it easy to tell which ones are still working, which have finished and which are stuck going in circles. So I built Apiarius, a Claude Code mod that adds a live agent deck that shows every agent and subagent, what each one is doing right now, who started it, what they tell each other and which files each one changed. Then I brought it to the terminal (for the purists) and a local web page too, so you can watch from wherever you work. Inspired a little by the latest agent apps like muse, grokbot and dots that give the agents a little personality and flair, so I gave them small vector avatars. The single major principle I had to build this was that it shouldn’t change how you work or what Claude does. It just reads Claude Code’s own events through hooks and just shows you what’s happening. It only steps in with action if you press a prompt or a send button on the deck. I built it with Claude Code itself, and watching the agents build their own deck via the deck within a couple hours which was trippy and made me realise how insane recursive self improvement will be. In the video demo, Claude spins up a team of agents to ship v2 of a small mock API, then on a local web view they take a break and play a game of mafia/imposter/werewolf. Free and open source (MIT): https://github.com/yusuflkq/apiarius Let me know what else you want it to show, and if you main the terminal, give the terminal version a go and help me improve it.
