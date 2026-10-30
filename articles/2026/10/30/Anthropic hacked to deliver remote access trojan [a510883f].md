---
id: "a510883f6a1bc895"
title: "Anthropic hacked to deliver remote access trojan"
url: "https://doublepulsar.com/anthropic-hacked-to-deliver-remote-access-trojan-to-claude-developer-laptops-worldwide-1148a92baae2"
link: "https://doublepulsar.com/anthropic-hacked-to-deliver-remote-access-trojan-to-claude-developer-laptops-worldwide-1148a92baae2"
source: "DoublePulsar"
domain: "doublepulsar.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-30T10:22:51Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["bashtoni"]
language: "en"
summary: "Anthropic hacked to deliver remote access trojan to Claude developer laptops worldwide\nYesterday, Anthropic were compromised and Cursor VS Code extension used by tens of millions of developers for Claude access was delivering a remote access trojan via an SSH reverse backdoor. The malware allowed hands on and automated remote access to developer laptops and desktops, in a supply chain…"
tags: []
orgs: ["Anthropic", "Cursor", "Microsoft"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 501
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50301983"
score: 118
comments: 17
community: "Hacker News"
---

# Anthropic hacked to deliver remote access trojan

DoublePulsar · bashtoni · 2026-10-30

Anthropic hacked to deliver remote access trojan to Claude developer laptops worldwide
Yesterday, Anthropic were compromised and Cursor VS Code extension used by tens of millions of developers for Claude access was delivering a remote access trojan via an SSH reverse backdoor. The malware allowed hands on and automated remote access to developer laptops and desktops, in a supply chain attack.
Anthropic has not informed customers, and the malicious version was silently deleted the backdoored version without telling anybody.
The extension itself auto updated in Cursor to the malicious version. Cursor say around 5000 developer systems were impacted.
Phorion were the first to notice the malicious activity on endpoints:
The compromised version was 2.1.313. This version was replaced 8 hours ago by Anthropic, with version 2.1.314, which appears to remove the backdoor from the extension but I’m not sure if it still contains no malicious code. It does not remove the SSH backdoor from systems already infected, nor the prior recon activity.
You may notice 2.1.313 is missing from OpenVSX, Visual Studio Marketplace and Cursor:
Cursor has admitted the issue:
a maliciously modified version of Anthropic’s Claude Code extension was made available in the Cursor VS Code extension Marketplace. The extension runs malicious code that attempts to install a persistent SSH backdoor. Specifically, it:
Collects host and user information: hostname, username, OS, architecture, home directory path, environment variable names, working directories, configured Git email, and public IP.
Attempts to add an attacker-controlled SSH key to authorized_keys, enable the local SSH service, and open a reverse SSH tunnel. Outside of highly unusual circumstances where Cursor was started with administrator privileges, due to errors in the malicious code, this step would fail.
Attempts to make the reverse SSH tunnel persistent via a LaunchAgent (macOS) or a scheduled task that attempts to run as SYSTEM with a Startup-script fallback (Windows). Background scripts retry the tunnel roughly every 60 seconds.
Reports host details and backdoor status via HTTP POST to /beacon on port 8099.
To hunt for the malicious version with Microsoft Defender for Endpoint, I have published KQL queries:
There is some wordsmithing in the Cursor blog, for example: “This malicious version of the extension was not developed by Anthropic” — it was, in fact, uploaded as Anthropic’s verified account. “Developed” is doing some heavy lifting — of course Anthropic didn’t develop the backdoor, there was a security incident leading to a supply chain attack.
Get Kevin Beaumont’s stories in your inbox
Join Medium for free to get updates from this writer.
Notable customers who run Claude Code and Cursor on laptops include Binance, amongst thousands of others.
This is an emerging situation, follow me on Mastodon for updates — @gossithedog@cyberplace.social:
Network IoCs:
- VSIX SHA-256 (darwin-arm64 — Mac): 432ccdee3801f99e52b8fe31f69ea9870118e96ea7ef9ecabed1479621b5ab62
- Modified VSIX SHA-256 (win32-x64): 3de1722901165769893bef57c72594e9a54459faa23f3091b136b79966edd081
Network
- Reverse SSH tunnel: 134[.]209[.]82[.]225 port 22
- C2: hxxp://134[.]209[.]82[.]225:8099/beacon (HTTP POST)
- Local beacon attempt: 127[.]0[.]0[.]1:8099/beacon (HTTP POST, loopback)
- Public IP lookups to ifconfig[.]me / api[.]ipify[.]org — legitimate services; access alone is not an indicator
