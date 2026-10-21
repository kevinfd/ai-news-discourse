---
id: "a03e1f43103aa41a"
title: "Beam pulls single app windows off the Mac Mini running your agents"
url: "https://thenewstack.io/beam-mac-mini-agents"
link: "https://thenewstack.io/beam-mac-mini-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T14:07:14Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Matthew Burns"]
language: "en"
summary: "Beam is a new Mac app that takes a window running on one Mac and puts it on another, where it behaves like a locally installed app. Why? Agents. \n\n Serial founder Hiten Shah , who co-founded Crazy Egg and KISSmetrics, built it with Sam Asante under a company called Noats. It launched on Product Hunt on Tuesday and is aimed at the headless Mac Mini sitting in a closet running AI agents. \n\n The…"
tags: ["AI Agents", "AI Infrastructure"]
orgs: ["Apple", "Perplexity"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 579
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Beam pulls single app windows off the Mac Mini running your agents

The New Stack · Matthew Burns · 2026-10-20

Beam pulls single app windows off the Mac Mini running your agents
Beam is a new Mac app that takes a window running on one Mac and puts it on another, where it behaves like a locally installed app. Why? Agents.
Serial founder Hiten Shah, who co-founded Crazy Egg and KISSmetrics, built it with Sam Asante under a company called Noats. It launched on Product Hunt on Tuesday and is aimed at the headless Mac Mini sitting in a closet running AI agents.
The pitch is great: Instead of opening Screen Sharing and steering a full remote desktop, a user picks a single window on the other machine, say a Terminal session or a browser window an agent is working in, and it opens alongside everything else on the Mac in front of them. It gets its own Dock icon and can be called using the Command+Tab switcher. Resizing the window resizes the window on the other Mac. Keyboard shortcuts work, files can be dragged across, and the app’s audio can play locally. The app itself never leaves the original machine. When one window isn’t enough, Beam can pull over a full display or the whole Mac.
Shah frames it around his own setup in his Product Hunt launch post, describing Macs running agents and local models “with work continuing even when nobody’s sitting in front of them.” Getting to one of those machines usually means Screen Sharing and a second desktop to navigate. Beam is meant to cut that down to the one window that matters.
Beam plays into the exploding ecosystem of Macs powering AI systems, so the app runs only on macOS. And both Macs need Apple Silicon, macOS Sonoma or later, and Beam installed. The machines find each other on the same Wi-Fi network, or anywhere through Tailscale.
The company says windows, keystrokes, clipboard, and audio travel directly between Macs, encrypted, and never pass through its servers. It also says hidden windows and password managers never show up in the window picker.
For devices without Beam, a share link opens a single window in any browser, view-only unless control is granted, and expires after anywhere from an hour to a week.
Asante said on Product Hunt that native iOS and Android apps are on the way.
Pricing depends on the setup. Hosting a Mac and joining a share link are free. Using your own Mac is free for 20 minutes a day, then $12 a month, $84 a year, or $199 for a lifetime license.
Beam follows where agents’ hardware is growing. The Mac Mini is becoming the default home for always-on agents, driven initially by OpenClaw, but others like Perplexity followed. Apple credited agentic workloads on its April earnings call.
The New Stack‘s Janakiram MSV caught the trend early and covered the shift in May, writing, “the Mac mini just became infrastructure.”
Beam isn’t the first to this problem. I used Astropad’s Workbench for a few weeks, and it let me remotely access agents on my desktop and through iOS apps. Workbench bets on mobile devices, while Beam bets that the unit of remote access should be the window, not the screen. Jump Desktop, Screens and Apple’s own Screen Sharing all cover the basics too.
Still, the problem is real and growing. The Mac stashed in a closet or on a rack is becoming a normal part of a developer’s setup. Beam’s answer is to stop treating it like a second desktop at all.
