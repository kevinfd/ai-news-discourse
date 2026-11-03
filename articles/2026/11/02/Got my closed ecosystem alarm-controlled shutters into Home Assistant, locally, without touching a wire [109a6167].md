---
id: "109a61675a04f45d"
title: "Got my \"closed ecosystem\" alarm-controlled shutters into Home Assistant, locally, without touching a wire. Thanks Claude! :)"
url: "https://reddit.com/r/ClaudeAI/comments/1xmc6en/got_my_closed_ecosystem_alarmcontrolled_shutters"
link: "https://reddit.com/r/ClaudeAI/comments/1xmc6en/got_my_closed_ecosystem_alarmcontrolled_shutters"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T22:51:12Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Loochanee"]
language: "en"
summary: "When we bought our place, the shutters came wired into the house alarm system. I didn't think too much about what it would mean at that time, but in practice it's a proprietary system that doesn't talk to anything: no Home Assistant integration, Google Home or public API. Just the vendor's phone app. This means I never had the whole house connected systems under control in one place. I had…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 685
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmc6en/got_my_closed_ecosystem_alarmcontrolled_shutters/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Got my "closed ecosystem" alarm-controlled shutters into Home Assistant, locally, without touching a wire. Thanks Claude! :)

Reddit · Loochanee · 2026-11-02

When we bought our place, the shutters came wired into the house alarm system. I didn't think too much about what it would mean at that time, but in practice it's a proprietary system that doesn't talk to anything: no Home Assistant integration, Google Home or public API. Just the vendor's phone app. This means I never had the whole house connected systems under control in one place. I had Shellys and a few cameras on Home Assistant but that was it. Couldn't control the rest and automations with combinations of shutters movemets and lights to discourage intruders when we are away were unreachable for me. Since the vendor alarm/shutters app works remotely, I assumed everything went through their cloud and gave up on a clean integration. The only options I could see were additional relays behind the wall switches (warranty headaches, and an unhappy alarm installer) or some fragile cloud-scraping hack. After reading posts from redditors about Claude interacting with all kinds of connected appliances in their homes, I decided to ask whether we could bring the shutters controls into Home Assistant, as a fun interoperability project. At first I imagined Claude would connect to the alarm panel, work out how it behaves and replicate the commands needed to move the shutters. I was wrong. Claude decided to take a look at the vendor's app instead: it decompiled it with jadx and realized that everything it needed was already written in the app. It pointed out that the app doesn't only use the cloud: it can also talk to the panel directly over the home network. The panel listens on a port on the LAN, and the app speaks a small encrypted binary protocol to it. Because the encryption is built into the app itself, the app's code shows how a session works: a handshake, a login with a user PIN, then short request/response messages. The strategy: validate Claude's findings capturing packets, then a read-only test, and only then a single command test while someone checks the shutter. And the PIN of the alarm system user lives in a local config file only, never in chats or logs, under a dedicated user created with only shutters controls permissions. Capturing packets on my router didn't work due to hardware offload. In the end I captured the app's traffic from my iPhone over USB, with a packet capture tool on my Linux box, while I opened and closed one shutter from the app. The capture matched what Claude had already reconstructed from the app's code, with one exception: the PIN was encoded slightly differently than expected which required 3 additional seconds for a fix. Then came the tests, one step at a time. First read-only: log in, read the state and the configuration with all the zone and shutter names, log out, and check that nothing odd happened on the panel. Then the real test: Claude sent one single command for one single shutter. I was sitting at my computer next to that shutter, phone on the desk, hands off everything, watching Claude Code do its thing in the terminal and trying to grasp what it was doing, step by step. Then the shutter just started moving. Nobody had touched a switch or an app; a test command written from scratch by Claude, on my own computer, was driving a system that a few days earlier I was convinced I could never reach. I was honestly impressed. This was one of the most satisfying "it works!" moments I can remember. The end result is a small custom Home Assistant integration, written by Claude, where each shutter is a proper controllable entity, plus an "all shutters" entity. It's 100% local, no vendor cloud involved, and the panel only sees a short session when a command is actually sent. Now I have a Home Assistant dashboard for the whole house: lights, AC, shutters, cameras and the intercom. My wife has her own account, and automations are finally possible. YAY! Disclosure: written with Claude. Since I started using Claude Code I get tired more easily (read: I've become lazy).
