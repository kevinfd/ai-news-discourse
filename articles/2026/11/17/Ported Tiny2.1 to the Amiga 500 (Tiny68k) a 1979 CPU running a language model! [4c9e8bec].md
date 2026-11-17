---
id: "4c9e8becbcfff466"
title: "Ported Tiny2.1 to the Amiga 500 (Tiny68k): a 1979 CPU running a language model!"
url: "https://reddit.com/r/ClaudeAI/comments/1xyi1th/ported_tiny21_to_the_amiga_500_tiny68k_a_1979_cpu"
link: "https://reddit.com/r/ClaudeAI/comments/1xyi1th/ported_tiny21_to_the_amiga_500_tiny68k_a_1979_cpu"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:27:10Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["azhadron"]
language: "en"
summary: "I ported TINY 2.1 (a tiny LLM by u/WollyMonjac ) to a stock Amiga 500: Motorola 68000 at 7 MHz, no FPU, 512KB + 512KB A501. I built it mostly with Claude Code and Opus 5.5, reusing the workflow from my earlier TinyStories port to the Amiga . It runs the original model and weights, but all in integer math because the 68000 has no floating point. Claude wrote the C inference engine, the 68000…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "business & funding", "agents & coding"]
content_source: "post"
word_count: 194
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xyi1th/ported_tiny21_to_the_amiga_500_tiny68k_a_1979_cpu/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Ported Tiny2.1 to the Amiga 500 (Tiny68k): a 1979 CPU running a language model!

Reddit · azhadron · 2026-11-17

I ported TINY 2.1 (a tiny LLM by u/WollyMonjac ) to a stock Amiga 500: Motorola 68000 at 7 MHz, no FPU, 512KB + 512KB A501. I built it mostly with Claude Code and Opus 5.5, reusing the workflow from my earlier TinyStories port to the Amiga . It runs the original model and weights, but all in integer math because the 68000 has no floating point. Claude wrote the C inference engine, the 68000 assembly, and the GUI. Every change was verified bit-for-bit against an integer spec in Python, in an emulated 68000, and in WinUAE before I put it on the real machine. In exact mode, the answers are identical to the original on all 44 test questions. Blazing fast at 0.2 to 0.4 letters/s. Cheated a bit with a KV cache and a few optimizations, but it’s the original model nonetheless. The video is sped up so it ain't that boring (the sped-up parts are marked). As a bonus, I ported the Amiga CD32 intro for the demo, because why the hell not? Free and open source, as all software should be: https://github.com/azha2005/tiny68k You'll need TINY.BIN from the original repo: https://github.com/WollyMonjac/Tiny-2.1
