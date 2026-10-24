---
id: "654632e8e067d6f7"
title: "A 4B model faster than a 395M encoder? 14 ms vs 31 ms (2.2x). Another 4B model: 150 ms (10x slower)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdkl55/a_4b_model_faster_than_a_395m_encoder_14_ms_vs_31"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdkl55/a_4b_model_faster_than_a_395m_encoder_14_ms_vs_31"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T17:35:20Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Top-Evidence174"]
language: "en"
summary: "This is Mica v0.5, the next version after v0.1. It's a decision model, the same kind of thing as Jev, which has been getting a lot of attention lately. It's 4B (Qwen3.5-4B + LoRA) and it doesn't write text. You hand it a state, a question and a list of options, and it gives back a probability for each option in a single forward pass. Stuff like \"which of these 5 moves\", or \"allow / block / send…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 625
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdkl55/a_4b_model_faster_than_a_395m_encoder_14_ms_vs_31/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A 4B model faster than a 395M encoder? 14 ms vs 31 ms (2.2x). Another 4B model: 150 ms (10x slower)

Reddit · Top-Evidence174 · 2026-10-23

This is Mica v0.5, the next version after v0.1. It's a decision model, the same kind of thing as Jev, which has been getting a lot of attention lately. It's 4B (Qwen3.5-4B + LoRA) and it doesn't write text. You hand it a state, a question and a list of options, and it gives back a probability for each option in a single forward pass. Stuff like "which of these 5 moves", or "allow / block / send to a human". Speed is the whole point, so I ran it side by side with two other decision models on one RTX 6000 Ada: PPLX Decider 1.2 Flash, also 4B, run in its fast mode Laya, built on a 395M-parameter encoder (ModernBERT-large), so about 10x smaller than Mica Every model saw the exact same options on every turn. The clips are Tetris, Snake, chess against a random-move opponent, and a log hunt where a day of security logs is cut into 150 blocks and each block gets allow, block or check. The video is a cut of all four. If you're looking for each demo in full, they're here: Tetris: https://huggingface.co/sky7350/Mica-v0.5-4B/resolve/main/assets/demo/tetris.mp4 Chess: https://huggingface.co/sky7350/Mica-v0.5-4B/resolve/main/assets/demo/chess.mp4 Snake: https://huggingface.co/sky7350/Mica-v0.5-4B/resolve/main/assets/demo/snake.mp4 Log hunt: https://huggingface.co/sky7350/Mica-v0.5-4B/resolve/main/assets/demo/loghunt.mp4 Median time per decision: Tetris: Mica 14.5 ms, PPLX 150 ms (10.3x slower), Laya 32 ms (2.2x slower) Chess: Mica 14 ms, PPLX 133 ms (9.4x slower), Laya 31 ms (2.2x slower) Snake: Mica 18 ms, PPLX 154 ms (8.4x slower), Laya 33 ms (1.8x slower) Log hunt: Mica 11 ms, PPLX 157 ms (13.9x slower), Laya 31 ms (2.8x slower) So about 10x faster than the other 4B model, and roughly 2x faster than a model a tenth of its size. The log hunt is my favorite. Mica went through all 150 blocks in 1.7 seconds and caught 21 of the 22 planted intrusions. PPLX took 23.5 seconds and caught 18. Laya caught none. A plain keyword grep over the same logs caught 6. A few notes: Times are each model's own call time on the same box, not API round trips. Laya had a one-time 12.9 s warm-up on its first long log block. I left that out of the video and it says so on screen. The logs are synthetic, written for this test. The 22 intrusions were written to avoid obvious keywords, which is why grep does badly. The games are just an easy way to see the speed. Mica v0.5 was trained on more than 200 real-world use cases, so I'd expect it to do better than other 4B models on actual work too. Why no Jev in the comparison? The response times are so far apart that a side-by-side wouldn't tell you anything. On the same request set Jev takes about 498 ms against Mica's 15.6 ms, more than 30x slower (that's over its API, so network time is included). One more thing. Most benchmarks used to compare decision models are pretty contaminated. A lot of decision models are coming out right now, and most open-weight ones are heavily tuned for public benchmarks like JDI. JDI itself is also quite far from what real decisions look like, and there are models on the JDI leaderboard trained only on public benchmark data. So a JDI score can be a long way from how a model feels in real use. Mica v0.5 gets about 95% right across cases from more than 200 real-world use cases. When you pick a decision model, look less at public benchmark scores and more at whether it makes the right calls on your own use case, and how fast it answers. For the runtime and the full numbers, see the Hugging Face page. Code and runtime: https://github.com/akivet/Mica Weights: https://huggingface.co/sky7350/Mica-v0.5-4B All four demos on one page: https://huggingface.co/sky7350/Mica-v0.5-4B#demo Feedback is welcome.
