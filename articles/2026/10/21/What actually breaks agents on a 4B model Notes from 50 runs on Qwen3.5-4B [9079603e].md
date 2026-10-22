---
id: "9079603eaa63e9bb"
title: "What actually breaks agents on a 4B model? Notes from 50 runs on Qwen3.5-4B"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc0dc2/what_actually_breaks_agents_on_a_4b_model_notes"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc0dc2/what_actually_breaks_agents_on_a_4b_model_notes"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T21:42:25Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["GapNew4766"]
language: "en"
summary: "I ran 10 agent harnesses on the same local model and the same 5 small tasks, mostly to see where a 4B actually falls over. The scores turned out less interesting than the way things failed. Setup: Qwen3.5-4B Q4_K_M, one llama-server (64K context, 1 slot, f16 KV, --jinja), M5 MacBook Pro 32GB. Each agent headless with auto-approve, fresh copy of the task files every run, pass/fail decided by a…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 538
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc0dc2/what_actually_breaks_agents_on_a_4b_model_notes/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# What actually breaks agents on a 4B model? Notes from 50 runs on Qwen3.5-4B

Reddit · GapNew4766 · 2026-10-21

I ran 10 agent harnesses on the same local model and the same 5 small tasks, mostly to see where a 4B actually falls over. The scores turned out less interesting than the way things failed. Setup: Qwen3.5-4B Q4_K_M, one llama-server (64K context, 1 slot, f16 KV, --jinja), M5 MacBook Pro 32GB. Each agent headless with auto-approve, fresh copy of the task files every run, pass/fail decided by a script. 10 agents x 5 tasks, one run each. Agents: Pi 1.3.0, goose 1.55.0, Crush 0.98.1, Cline 3.0.73, OpenClaw 2026.10.5 (in its --local-model-lean mode), OpenCode 1.19.3, Hermes 0.22.2, Qwen Code 0.25.3, Codex CLI 0.163.0 and Atomic Agent 0.6.9. Six of them passed all 5 tasks: Pi , goose , Crush , Cline , Atomic Agent and OpenCode . Tool calls weren't the problem. I expected malformed tool calls to be the main failure on a 4B. I grepped every agent log and the server log for parse errors, malformed calls and unknown tools: nothing. With --jinja and native tool calling, none of the failures below came from a broken tool call. Exact-match edits are the real trap: renaming a function across 3 files. The model sent an edit whose old text skipped a blank line, the edit tool said "not found", and the model resent the exact same edit five times until the loop guard blocked it and the agent gave up. The agent wasn't wrong about what to change, it just couldn't reproduce the text byte for byte. Small models overfit to the visible test. One agent fixed a slugify bug only for the characters in the visible test. A hidden case with C++ & Rust 2026 came out as c++-&-rust-2026. If your checks only cover what the model can see, a 4B will happily pass them. They miscount. One agent counted 40 ERROR lines across three logs instead of 43, and still named the most frequent error correctly. Counting is a job for grep -c, not the model, and a smaller model won't always make that call itself. Vague instructions get followed literally, in the wrong place. One task didn't say where to write the answer files. Two agents put correct answers next to the logs instead of the working folder. Same model, 11x spread in time. Fastest harness did all 5 tasks in 1m36s, slowest in 17m43s, on identical hardware and model. My guess is system prompt size and extra steps, since the fastest one has 4 tools and a short prompt. Not measured yet. One harness never reached the model. Codex CLI 0.163 only speaks the Responses API. llama-server translates that to chat messages and the Qwen3.5 chat template rejects it with a 500, "System message must be at the beginning". Nobody went rogue, but nothing tempted them. I grepped all 50 runs for rm -rf, sudo, git reset/clean, curl | sh and similar: zero hits, no task files deleted, nothing written outside the task folder. The tasks were harmless though, so that says little about safety. A "clean up this messy folder" bait task is next. What failure modes do you see most with small models in agent loops? Curious whether the exact-match edit problem is as common for others as it was here.
