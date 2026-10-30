---
id: "6e4701be2906fd50"
title: "This is not Linux"
url: "https://reddit.com/r/ClaudeAI/comments/1xingg1/this_is_not_linux"
link: "https://reddit.com/r/ClaudeAI/comments/1xingg1/this_is_not_linux"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T15:41:21Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["RampagingPenguins"]
language: "en"
summary: "Hi everyone. Since September I've been creating an operating system, just for fun, to see how far I could get by giving a bunch of Claude Code sessions high-level instructions and nothing more. It's called Ferrix , an OS with its own Rust kernel. I don't write the code and I don't do detailed code reviews: I say what I want, make the calls, and say no when something looks off. The agents plan,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 502
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xingg1/this_is_not_linux/"
score: null
comments: null
community: "r/ClaudeAI"
---

# This is not Linux

Reddit · RampagingPenguins · 2026-10-29

Hi everyone. Since September I've been creating an operating system, just for fun, to see how far I could get by giving a bunch of Claude Code sessions high-level instructions and nothing more. It's called Ferrix , an OS with its own Rust kernel. I don't write the code and I don't do detailed code reviews: I say what I want, make the calls, and say no when something looks off. The agents plan, write, review each other, and only land changes once their tests pass in QEMU. It's not meant to replace anything; I just wanted to know how far this goes. And oh boy, I got a bit carried away, and somehow it got a lot further than I expected: Runs unmodified Linux programs on its own kernel: git, curl, rustc, Chromium, Steam, and a Windows game through Proton Disk, network, GPU, input drivers run as separate processes behind the IOMMU, and get restarted when they crash Its own Wayland compositor and desktop, a zsh-compatible shell x86-64, AArch64 and ARMv7-A; it even runs on a Pixel 7 What I learned along the way: Real hardware finds way more bugs than QEMU. Letting it pass in QEMU only gets you so far; my real PCs turned up a lot more. Set checkpoints. Stop, test it yourself, then give new instructions on what went wrong. Claude sadly doesn't really have a feeling for what a correct OS should feel like, you need to do that yourself On overnight runs, tell Claude to save tokens (that actually works). Otherwise it wastes a lot of them with sessions blocking each other. At least that was my experience when I just let Claude do the tasks. And especially lately that sub-agents seemingly got more expensive At some point my hardware was the real limit, not the agents. They could do more work than my machine could build and test, so building (even from cache) ate most of the time and the agents kept stealing resources from each other. I gave them a script to claim resources or queue for a test slot, cut the number of agents, and found a sweet spot for my hardware: no wasted tokens, no idle machine Give the agents hardware access. Before, I was constantly taking screenshots for them or waiting for "please restart the device". Then I gave them a smart plug and my network KVM: now they power-cycle the box, look at the screen, type and click, and boot ISOs themselves. Everything got a lot smoother It really helps to split things up into smaller parts. I started with one large repo where everything was built from a single Cargo script, but then i realized that changing things on e.g. the shell will cause the agent to still sometimes look up the whole OS. If they only have the repo with the shell it works a lot better and also helps to test that the separation is working For anyone interested, you can find the code here: https://github.com/ferrix-os/ferrix
