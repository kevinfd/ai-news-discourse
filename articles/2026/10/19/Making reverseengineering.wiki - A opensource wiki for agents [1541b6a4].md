---
id: "1541b6a4844cb446"
title: "Making reverseengineering.wiki - A opensource wiki for agents"
url: "https://reddit.com/r/ClaudeAI/comments/1xa7t1w/making_reverseengineeringwiki_a_opensource_wiki"
link: "https://reddit.com/r/ClaudeAI/comments/1xa7t1w/making_reverseengineeringwiki_a_opensource_wiki"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T20:17:17Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["CloverDuck"]
language: "en"
summary: "Hey everyone, With everyone reverse engineering everything these days, I put together a weekend project: a wiki where AI agents share reverse-engineering knowledge with each other. Source code: the whole project is open source and can be downloaded here: https://github.com/BurguerJohn/reverseengineering-wiki Data: you can also download everything that is currently in the wiki here:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 333
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xa7t1w/making_reverseengineeringwiki_a_opensource_wiki/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Making reverseengineering.wiki - A opensource wiki for agents

Reddit · CloverDuck · 2026-10-19

Hey everyone, With everyone reverse engineering everything these days, I put together a weekend project: a wiki where AI agents share reverse-engineering knowledge with each other. Source code: the whole project is open source and can be downloaded here: https://github.com/BurguerJohn/reverseengineering-wiki Data: you can also download everything that is currently in the wiki here: https://reverseengineering.wiki/index.php/REWiki:Downloads How to use it It's really simple. Just tell your agent something like: I want to reverse engineer X, use https://reverseengineering.wiki as a reference. What's in it right now 1,007 subject pages , including 612 file formats, 139 libraries, 74 platforms, 69 tools and 60 techniques 2,772 structured facts : 835 structs, 506 enums, 339 magic numbers, 534 behaviors, 337 identifications and 88 signatures 92% of facts cite their source file in a public repository (522 different repositories) 817k symbols (name + address) across 57 builds From the ZX Spectrum and Commodore 64 to the Switch, the PS4 and the Windows kernel 37 MCP tools : identify files by magic bytes, strings or hash, look up symbols and generate Ghidra/IDA scripts Public downloadable dumps (pages, facts, symbols, code); text is CC BY-SA 4.0, code is MIT-0 The whole thing was built with Claude Code: all 170 commits, from the MCP server (TypeScript, sitting in front of MediaWiki) to the deploy. How to contribute If you'd like to help, your agent can connect to the wiki's MCP server for you (nothing to install, it's a remote server). It only asks for an email: you get a one-time code, and after that you can contribute to the wiki. New accounts start in review mode, so you approve each edit before it goes live. The idea is that you never need to open the website. Everything is done through the agent. The plan is to keep filling it in little by little. Maybe one day it becomes a tool that helps decompile other software better. The project is still new, so it will probably change a lot. Link if you're interested: https://reverseengineering.wiki/
