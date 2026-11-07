---
id: "040bccaf30305ecf"
title: "App made for college capstone turned into a full SSH client on 5 platforms, built mostly with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xpnof8/app_made_for_college_capstone_turned_into_a_full"
link: "https://reddit.com/r/ClaudeAI/comments/1xpnof8/app_made_for_college_capstone_turned_into_a_full"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T20:45:46Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["ISpeakTheLie"]
language: "en"
summary: "So basically I’m a cybersecurity student and I work in infosec full time. My capstone was supposed to be a small SSH app just for funsies which then turned into ZestSSH, a full SSH client for phone and PC with end-to-end encrypted sync, built mostly with Claude Code. Why I built it: JuiceSSH died, and Termius wanted a yearly subscription just to sync my hosts between my phone and my PC. What it…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Microsoft"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 398
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpnof8/app_made_for_college_capstone_turned_into_a_full/"
score: null
comments: null
community: "r/ClaudeAI"
---

# App made for college capstone turned into a full SSH client on 5 platforms, built mostly with Claude Code

Reddit · ISpeakTheLie · 2026-11-06

So basically I’m a cybersecurity student and I work in infosec full time. My capstone was supposed to be a small SSH app just for funsies which then turned into ZestSSH, a full SSH client for phone and PC with end-to-end encrypted sync, built mostly with Claude Code. Why I built it: JuiceSSH died, and Termius wanted a yearly subscription just to sync my hosts between my phone and my PC. What it does now: Runs on Android, iPhone, Windows, Mac and Linux Hosts, keys and snippets sync across all of them, end-to-end encrypted. Use your own Nextcloud/WebDAV, Google Drive or sync server, or let me host it SFTP, port forwarding, split panes, jump host chains Teams: invite someone with a QR code and share a vault with them Recording mode that hides every host name and IP, so you can stream or screenshot without leaking your whole lab How Claude Code helped: Every feature starts as a spec I write with Claude: exact files, code skeletons, and a checklist of what “done” means. Claude Code builds against the checklist and I test against it. That fixed most of the “it says it’s done but it isn’t” problem. I have Claude mock up screens before anything gets built. Way easier to fix a layout in a mockup than in Flutter code. Claude proposed the encryption design for sync and I reviewed it, since that’s literally my job lol. Then I had Claude audit the whole thing with agents, and it caught my own security doc describing stuff the backend didn’t fully do yet. Nothing had synced in production yet so nobody was affected, but that was humbling - tis why you never blindly trust AI. What didn’t work: Drag-to-detach windows on desktop. Claude tried a bunch of approaches, Flutter just isn’t there yet. Honestly thought about just making my own fork of it at this point lmfao Huge UI changes in one go drift. Smaller specs work way better. It’ll agree with a bad idea if you let it, so now I ask it to argue against me first. Try it: free to use with no account needed. Google Play, App Store, Microsoft Store, or zestssh.com for Mac and Linux. Upgrades are one time, no subscription. https://zestssh.com/ Tell me what you think, or roast it, either works. I plan on open sourcing it once I’m happy with everything!
