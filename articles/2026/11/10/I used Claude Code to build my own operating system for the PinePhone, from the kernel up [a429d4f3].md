---
id: "a429d4f30427bf68"
title: "I used Claude Code to build my own operating system for the PinePhone, from the kernel up"
url: "https://reddit.com/r/ClaudeAI/comments/1xsyor4/i_used_claude_code_to_build_my_own_operating"
link: "https://reddit.com/r/ClaudeAI/comments/1xsyor4/i_used_claude_code_to_build_my_own_operating"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T21:05:59Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Elian_D"]
language: "en"
summary: "I bought a PinePhone a couple of years ago, and it sat in a drawer because every app loaded so slowly. I work in embedded, so I treated it as an embedded device instead of a small desktop, and with Claude Code I built a firmware for it. It covers calls, SMS, contacts, notes, music and the camera, plus an ePub reader, maps, a Telegram client, Doom and a Genesis emulator. All the apps were written…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 466
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsyor4/i_used_claude_code_to_build_my_own_operating/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to build my own operating system for the PinePhone, from the kernel up

Reddit · Elian_D · 2026-11-10

I bought a PinePhone a couple of years ago, and it sat in a drawer because every app loaded so slowly. I work in embedded, so I treated it as an embedded device instead of a small desktop, and with Claude Code I built a firmware for it. It covers calls, SMS, contacts, notes, music and the camera, plus an ePub reader, maps, a Telegram client, Doom and a Genesis emulator. All the apps were written from scratch. It's a single LVGL program drawing straight to the screen, on Buildroot and a mainline kernel, and most screens run at the display's full 66 FPS. You can try it in your browser without an actual PinePhone: eliandoran.github.io/PinePhone/ (the same UI compiled to WebAssembly). Going below the app layer. Speed and battery life came mostly from patching what sits underneath: 81 patches, 72 of them written for this project. Linux (46): USB and USB-C, cameras, charging, the device tree, and waking from deep sleep on a call or SMS. LVGL (23): mostly making its OpenGL ES renderer fast on the Mali-400 GPU. The rest are for the HTML engine and the build. A typical loop was: profile on the phone, form a hypothesis, patch, rebuild, flash and measure again. The hard part was rarely writing the C. It was the hours of reading driver code and logs to find the one line to change, which is where an agent that doesn't tire of tracing helps most. I've used mostly Opus 5.5 with medium effort and more recently Fable 5.2 for some deep problems like VoLTE debugging. Making it safe to let an agent flash a phone. Updates are A/B, so a bad image rolls back by itself if it doesn't reach the home screen. That's why I let Claude build and flash on its own. Before anything reaches the phone, though, a test suite runs on my PC: 1,892 tests that drive the whole UI headless, like a user would. The modem, Wi-Fi, Bluetooth, sound and cameras are replaced by fakes. Tests run under sanitizers, and a memory leak fails them. The rule is test first: a bug gets a failing test before it gets a fix, which catches confident-but-wrong fixes. (The external apps' code is at 99% line coverage.) Where it went wrong. Early on, Claude tapped through menus blind and overwrote my Genesis saves. Now it takes a screenshot after every tap. RAM overclocking experiments hung the phone. Rollback made those an inconvenience, not a brick. A key aspect is that I manually reviewed every change and tested it on the device with the rapid loop. A long CLAUDE.md holds what each session learns: why a patch exists, which modem quirk needs what. New sessions start knowing why things are the way they are. GitHub: https://github.com/eliandoran/PinePhone
