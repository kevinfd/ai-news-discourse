---
id: "b13c235dd2e55d26"
title: "I’m a network engineer, not a programmer. I built a free network scanner for Mac and Windows with Claude Code because I wasn't happy with what was available."
url: "https://reddit.com/r/ClaudeAI/comments/1xrjvwv/im_a_network_engineer_not_a_programmer_i_built_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xrjvwv/im_a_network_engineer_not_a_programmer_i_built_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T05:55:34Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Lone_Wolf_555"]
language: "en"
summary: "I’ve worked in networking for years, and I wanted a scanner that worked the way I do. Point it at a subnet and get a clean list of every device: IP, MAC, maker, a real name, and what kind of thing it is. I can’t write Swift or Rust, so I built it with Claude Code. It’s called ARPradar. What it does ARP scans a subnet. It names devices from whatever it can find: DHCP, UPnP, SNMP, web page titles,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 341
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrjvwv/im_a_network_engineer_not_a_programmer_i_built_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I’m a network engineer, not a programmer. I built a free network scanner for Mac and Windows with Claude Code because I wasn't happy with what was available.

Reddit · Lone_Wolf_555 · 2026-11-09

I’ve worked in networking for years, and I wanted a scanner that worked the way I do. Point it at a subnet and get a clean list of every device: IP, MAC, maker, a real name, and what kind of thing it is. I can’t write Swift or Rust, so I built it with Claude Code. It’s called ARPradar. What it does ARP scans a subnet. It names devices from whatever it can find: DHCP, UPnP, SNMP, web page titles, Ubiquiti discovery. Guesses the device type (router, switch, AP, camera, printer, TV, NAS, phone and so on). Right-click to fix a wrong guess. Saves scans by organization, so you can keep separate lists for each customer or site and look back at history. Draws a network map from a UniFi controller: switch ports, AP uplinks, slow links in orange. Exports to PNG, PDF or SVG. Comments on devices, and export to Excel. How Claude was used Claude Code wrote basically all of the code. The Mac app is SwiftUI. The Windows version is a Tauri port with a Rust scan engine. My job was knowing what a good scan should look like and telling it when something was wrong. Some things I didn’t expect: It ran its own checks. It ran the tests, waited for the GitHub Actions builds, and tested the UI in a browser against demo data before asking me to try anything. It showed me mockups before building anything I’d see, which kept me from asking for things I didn’t really want. When the Windows builds kept failing, the problem was GitHub’s download servers timing out. Claude worked that out, stopped re-running builds that were burning minutes, and started one build after the downloads had stayed up for several checks in a row. Where it needed help: anything about my real network. It can’t see my LAN from its sandbox, and I enter API keys myself. Try it: ARP Radar Price: Free Happy to answer questions about the app or about building something real without being a coder.
