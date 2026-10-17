---
id: "58d59342bad9e081"
title: "BitRun now runs 1-bit LLMs on your CPU with a split-screen TUI and live wattage telemetry (70+ t/s on laptops, supports 8B ternary models)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7fj2c/bitrun_now_runs_1bit_llms_on_your_cpu_with_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7fj2c/bitrun_now_runs_1bit_llms_on_your_cpu_with_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T12:58:02Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["The_VibePreneur"]
language: "en"
summary: "You know that feeling when you try running a local LLM on your everyday laptop, and within twenty minutes your battery is begging for mercy, your fans are howling, and you are staring at a raw terminal scroll wondering how many watts your CPU is actually burning? After the first v alpha, a lot of you pointed out the obvious blind spots: where are the real power numbers? Why are we stuck under 3B…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Microsoft", "Apple", "Cursor"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 440
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7fj2c/bitrun_now_runs_1bit_llms_on_your_cpu_with_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# BitRun now runs 1-bit LLMs on your CPU with a split-screen TUI and live wattage telemetry (70+ t/s on laptops, supports 8B ternary models)

Reddit · The_VibePreneur · 2026-10-16

You know that feeling when you try running a local LLM on your everyday laptop, and within twenty minutes your battery is begging for mercy, your fans are howling, and you are staring at a raw terminal scroll wondering how many watts your CPU is actually burning? After the first v alpha, a lot of you pointed out the obvious blind spots: where are the real power numbers? Why are we stuck under 3B parameters? And why does the interface still feel like raw terminal output from three years ago? So over the last couple days, I went back and reworked the entire stack. What is new in v0.2.0-beta: The biggest change you will notice right away is what I call the BitRun Cockpit. Instead of dumping tokens into a raw terminal, running bitrun cockpit <model> splits your screen into a two-panel dashboard. On the left, your tokens stream in cleanly with its own scrollback so you can read previous answers while new ones generate. On the right, it hooks directly into hardware telemetry, showing you live CPU package power in Watts, Joules per token, P-core versus E-core loads, and time-to-first-token as it runs. On the model side, we wanted to see if 1-bit computing actually holds up on larger models without melting your machine. We detached from Microsoft's frozen submodule, rebased on modern llama.cpp, sorted out the GGUF Type 42 collision, and got PrismML's 8B ternary model ( bonsai-8b ) running entirely on CPU memory in just about 2 GB of RAM. Here's the numbers on some actual hardware: On an Apple M4 Pro (zero GPU, pure CPU): Bonsai 1.7B hits ~73 tokens/sec generation while pulling 11.7 Watts (about 0.31 Joules per token). Falcon3 1B runs right next to it at ~73 tokens/sec. Even the 8B Bonsai model churns out 21 tokens/sec on pure CPU, pulling the exact same 11.7 Watts. On a standard Windows PC (Core i5-12600K): Bonsai 1.7B generates at 85 tokens/sec pulling around 22 Watts. BitNet 70M clocks almost 600 tokens/sec. If you want to spin it up and see what your CPU pulls: macOS / Linux: curl -fsSL https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.sh | sh Windows (PowerShell): irm https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.ps1 | iex Just run bitrun cockpit bonsai-1.7b and it pre-downloads the checkpoint and drops you straight into the cockpit. There is also bitrun serve if you want a local OpenAI endpoint on port 8080 for Cursor or Open WebUI. The code and pre-compiled binaries are up on GitHub: https://github.com/IshekKhal/bitrun Give the cockpit a spin on your rig and tell me what kind of wattage your CPU clocks. Really curious to see how the power numbers hold up across different chips.
