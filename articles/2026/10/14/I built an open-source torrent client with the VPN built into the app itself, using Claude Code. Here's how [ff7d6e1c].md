---
id: "ff7d6e1c4b318270"
title: "I built an open-source torrent client with the VPN built into the app itself, using Claude Code. Here's how the process went"
url: "https://reddit.com/r/ClaudeAI/comments/1x5imkw/i_built_an_opensource_torrent_client_with_the_vpn"
link: "https://reddit.com/r/ClaudeAI/comments/1x5imkw/i_built_an_opensource_torrent_client_with_the_vpn"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T05:05:07Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Shark__Bytes"]
language: "en"
summary: "I built Shark BiteTorrent , a free, open-source (GPL-3.0) torrent client for Windows, Linux and macOS, with Claude Code over about a day and a half. What it does The VPN runs inside the app (wireguard-go plus a userspace network stack), so only the torrent client uses it. The rest of your PC is untouched, and there's no adapter, driver or admin rights. Kill switch by design: torrents start only…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 527
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5imkw/i_built_an_opensource_torrent_client_with_the_vpn/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an open-source torrent client with the VPN built into the app itself, using Claude Code. Here's how the process went

Reddit · Shark__Bytes · 2026-10-14

I built Shark BiteTorrent , a free, open-source (GPL-3.0) torrent client for Windows, Linux and macOS, with Claude Code over about a day and a half. What it does The VPN runs inside the app (wireguard-go plus a userspace network stack), so only the torrent client uses it. The rest of your PC is untouched, and there's no adapter, driver or admin rights. Kill switch by design: torrents start only after the tunnel is verified, and there's no other network path to leak through. DNS goes through the tunnel too. Free Cloudflare WARP by default, or sign in to Mullvad, PIA (auto port forwarding), NordVPN or IVPN, or import any WireGuard config. Magnet links from the browser, drag and drop, file selection, speed limits, piece map, tray icon, in-app updates. Flags disguised programs ( movie.mp4.exe ) and scans finished downloads with Windows Defender. Saved logins are encrypted with the OS key store. Free to try Download from Releases (Windows installer, Arch/CachyOS package, Linux tarball, macOS app): https://github.com/trevercomb/SharkBiteTorrent/releases Source: https://github.com/trevercomb/SharkBiteTorrent Windows is tested. Linux and macOS builds are new and untested on real machines. How I used Claude Code One long Claude Code session in VS Code. I'm not a Go developer: I brought the idea, the decisions and testing on my PC; Claude Code did the research, architecture, code, tests and releases. My first prompt was roughly: "I want a lightweight bittorrent client with a built-in free VPN like Cloudflare WARP, so only the client is on the VPN, not the entire PC." It proposed the stack (Go + Wails, wireguard-go, gVisor netstack, anacrolix/torrent), asked a few questions, and proved the riskiest part first: a WARP tunnel inside the app while my PC kept its normal IP. What stood out was that it tested its own work: Downloaded legal Linux ISOs through the tunnel to measure speed and peers. Checked the app's OS sockets during downloads to confirm nothing bypassed the VPN. Set up GitHub Actions to build Windows, Linux and macOS releases. I reported problems in plain language and screenshots, for example "qBittorrent gets 5 MB/s while ours gets way less." It found my downloads went to a NAS, benchmarked SMB writes, and wrote its own storage layer: ~0.5 MB/s became ~7.5 MB/s. Bugs it tracked down that I wouldn't have: Magnets without trackers found no peers: UDP sockets bound to 0.0.0.0 in the userspace stack couldn't send. An "unlimited" rate limiter made the library stop connecting to peers. Updates silently kept the old version: the installer copied the .exe before the app had exited. It also pushed back and asked first: it talked me out of truly unlimited connections, noticed my email would go public with the repo and rewrote the git history, and asked before running a test-virus file. Tip: describe the outcome you want, test on real hardware, and report problems with specifics. Most fixes came from "this looks wrong" plus Claude Code working out why. No ads or telemetry. Donations are optional; some in-app VPN sign-up links may become labelled referral links (none in this post), and a build flag removes all of it. Feedback welcome, especially from Linux and macOS users.
