---
id: "40c0889d422eab09"
title: "I’m using Claude Code to build an AI accelerator. It now runs Qwen3.5 on an FPGA."
url: "https://reddit.com/r/ClaudeAI/comments/1x6ajc5/im_using_claude_code_to_build_an_ai_accelerator"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T02:53:28Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["ScarionnS"]
language: "en"
summary: "I wanted to learn more about AI accelerator design, so I started openTPU: an open-source accelerator developed with AI coding agents, including Claude Code. It already runs Qwen3.5 and other open-weight models on a Kintex-7 FPGA card. The part that's interesting is the hardware optimization workflow: An agent reads the hardware code, timing reports, and lessons from previous attempts, then…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 243
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6ajc5/im_using_claude_code_to_build_an_ai_accelerator/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I’m using Claude Code to build an AI accelerator. It now runs Qwen3.5 on an FPGA.

Reddit · ScarionnS · 2026-10-15

I wanted to learn more about AI accelerator design, so I started openTPU: an open-source accelerator developed with AI coding agents, including Claude Code. It already runs Qwen3.5 and other open-weight models on a Kintex-7 FPGA card. The part that's interesting is the hardware optimization workflow: An agent reads the hardware code, timing reports, and lessons from previous attempts, then proposes a change. Another agent implements it. Automated checks compare the hardware against a Python simulator, test performance, and run simulations to measure the result. The biggest lesson so far has been giving the agents useful feedback: exactly which test failed, where the timing bottleneck is, and whether a change actually improved anything. Keeping that loop cheap makes experimentation much easier. I still have to nudge the larger architectural changes. Verification also has blind spots, we found floating-point bugs that our LLM inference tests hadn’t caught. Passing those tests only tells you so much. The whole stack is in one repo: hardware code, instruction set, simulator, a compiler for Python-style kernels, a profiler that shows what each hardware unit does cycle by cycle, and host tools for chat and monitoring. It’s free and open source, and you don’t need an FPGA to try it. You can run models through the simulator on a laptop and explore how the accelerator works. https://github.com/FeSens/openTPU Anyone else here using Claude Code for hardware design? I’d be interested to compare workflows and hear how you verify its changes.
