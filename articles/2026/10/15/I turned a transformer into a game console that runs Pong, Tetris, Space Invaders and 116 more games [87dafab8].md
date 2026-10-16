---
id: "87dafab8fa4731d9"
title: "I turned a transformer into a game console that runs Pong, Tetris, Space Invaders and 116 more games."
url: "https://reddit.com/r/LocalLLaMA/comments/1x6uaav/i_turned_a_transformer_into_a_game_console_that"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6uaav/i_turned_a_transformer_into_a_game_console_that"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T18:57:13Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["RevealIndividual7567"]
language: "en"
summary: "I turned a CHIP-8 game console into a decoder-only transformer. The transformer is the game engine. It executes instructions, updates machine memory, and renders every frame through next-token prediction. Every generated token is a memory write, and your keypresses go directly into the model's context window. There's no separate emulator. Pong, Tetris, Space Invaders and a bunch of other CHIP-8…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 164
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6uaav/i_turned_a_transformer_into_a_game_console_that/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I turned a transformer into a game console that runs Pong, Tetris, Space Invaders and 116 more games.

Reddit · RevealIndividual7567 · 2026-10-15

I turned a CHIP-8 game console into a decoder-only transformer. The transformer is the game engine. It executes instructions, updates machine memory, and renders every frame through next-token prediction. Every generated token is a memory write, and your keypresses go directly into the model's context window. There's no separate emulator. Pong, Tetris, Space Invaders and a bunch of other CHIP-8 games run on the same model. Just swap the ROM in the prompt to switch games. The weights are compiled from a circuit, not learned through training. Attention handles memory reads by finding the most recent write to an address, while ReLU circuits handle opcode decoding, arithmetic, comparisons and bitwise operations. Even the compatibility quirks are encoded in the initial prompt, so different games don't need different weights. The model has 18 layers, 42 attention heads and 32M parameters (139k nonzero). It uses fp64 and can be loaded through Hugging Face transformers. Model weights: https://huggingface.co/divagr1925/chipformer Try it out: https://divagr.com/chipformer Code + desktop app: https://github.com/divagr18/chipformer
