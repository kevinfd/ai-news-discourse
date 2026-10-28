---
id: "104941fb9a4384a1"
title: "Claude Code reverse-engineered the Xbox 360 kernel and wrote a native driver so Series X|S controllers work on it"
url: "https://reddit.com/r/ClaudeAI/comments/1xgtghe/claude_code_reverseengineered_the_xbox_360_kernel"
link: "https://reddit.com/r/ClaudeAI/comments/1xgtghe/claude_code_reverseengineered_the_xbox_360_kernel"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T14:05:19Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Hot-Ad2974"]
language: "en"
summary: "Microsoft's Xbox Wireless Adapter (the USB dongle for Series X|S controllers) has never worked on an Xbox 360. It's a MediaTek Wi-Fi chip that relies on the host for everything: firmware upload, radio setup, pairing, an ECDH security handshake and Microsoft's GIP controller protocol. On PC that's Microsoft's driver, on Linux it's xone. The 360 had nothing. I wanted it on my modded 360 (kernel…"
tags: ["r/ClaudeAI"]
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 489
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgtghe/claude_code_reverseengineered_the_xbox_360_kernel/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code reverse-engineered the Xbox 360 kernel and wrote a native driver so Series X|S controllers work on it

Reddit · Hot-Ad2974 · 2026-10-27

Microsoft's Xbox Wireless Adapter (the USB dongle for Series X|S controllers) has never worked on an Xbox 360. It's a MediaTek Wi-Fi chip that relies on the host for everything: firmware upload, radio setup, pairing, an ECDH security handshake and Microsoft's GIP controller protocol. On PC that's Microsoft's driver, on Linux it's xone. The 360 had nothing. I wanted it on my modded 360 (kernel 17559), so I built it with Claude Code. It's free and open source (GPL-3.0) : https://github.com/Jacckii/Xbox360-Series-Controllers-Native What it does: up to 4 Series X|S controllers connect wirelessly to the 360 as normal controllers, with rumble and a working Guide button, in the dashboard and in games. It loads at boot, just Microsoft's own adapter, nothing in between. What Claude did Reverse-engineered the 360 kernel's undocumented USB stack (Usbd) and XAM's input path in Ghidra through an MCP server: the runtime USB class-driver list, transfer block layouts, which callbacks run on which DPC, and the callback table XAM uses for the Guide button Ported xone's MT76 radio code, pairing, ECDH P-256 handshake and GIP protocol into portable C, and wrote the 360 side as a kernel-mode system DLL Wrote PowerPC function hooks (instruction relocation into trampolines) to feed the controllers into XInput Debugged it on the live console by reading memory over the debug monitor Bugs it tracked down The toolchain saves registers as 32-bit values, the kernel expects 64-bit ones → asm thunks around every kernel callback Kernel DPCs have no floating-point context, but variadic functions spill FP registers anyway → soft-float, plus a build check that fails on any FP instruction Pressing Guide deadlocked the console: the thread feeding XAM input was also calling into XAM → every XAM call moved to its own thread on another hardware thread The driver thread starved while the guide was open → it found the kernel clamps system threads to priority 9 and raised the driver to that An adapter plugged in before boot was ignored → it found the kernel's list of unclaimed USB devices and the routine that offers them to drivers again How the workflow went Give it eyes on the target. The driver writes a status block and a log ring into memory, and Claude read them over the network after every test. Give it the right tools. Ghidra MCP for the kernel, the cross-compiler, and the console's debug port. It ran the build → upload → read logs loop on its own. Make mistakes fail the build. Each rule it learned the hard way became a check in the build script, so fixed bugs stayed fixed. I was the hands. Plugging the dongle, pairing controllers, rebooting the console when it hung, and describing what was on screen. I released it on r/360hacks a few hours ago ( thread here ), and a couple of people are ordering adapters to test it with their own controllers. Still early, so feedback is welcome.
