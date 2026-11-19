---
id: "89bec2dcd6d7fdb5"
title: "Claude Gets Hella Paranoid"
url: "https://news.ycombinator.com/item?id=50543947"
link: "https://news.ycombinator.com/item?id=50543947"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-18T09:24:58Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["noduerme"]
language: "en"
summary: "Mm, so I hesitate to write this, because my own AI agents might read it. But what the hell. I've got this crappy little $300 PC on my network hooked up to my projector, that I mostly use to serve Jellyfin. So tired of it going down every time there's a Windows update, but I've been too lazy to get around to installing Ubuntu. Last night, when it went down, I asked my Claude-claw via Whatsapp if…"
tags: []
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 394
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50543947"
score: 18
comments: 11
community: "Hacker News"
---

# Claude Gets Hella Paranoid

Hacker News · noduerme · 2026-11-18

Mm, so I hesitate to write this, because my own AI agents might read it. But what the hell. I've got this crappy little $300 PC on my network hooked up to my projector, that I mostly use to serve Jellyfin. So tired of it going down every time there's a Windows update, but I've been too lazy to get around to installing Ubuntu. Last night, when it went down, I asked my Claude-claw via Whatsapp if it could just SSH into it and set up a dual boot partition. Claude got as far as partitioning the drive and then starting asking hard questions , like (paraphrasing) "wait a minute. This crosses a line. I have now been asked to remote into a machine with a password, write a separate boot partition, and restart it. From this chat, you haven't really verified that you are you. If you're really there, and not just texting me, give me some proof". So I remoted in and created a TextEdit RTF file on the claw's desktop: "Hey, it's me, I'm asking you to remote into the PC". Claude read it and responded that it was the kind of proof it was looking for, real RTF headers and datestamps and such. I had proven I had physical access to the claw machine, (although not to the PC, but it seemed reassured anyway). A little while later, before triggering the Ubuntu installer, it put me through it all over again. I told Claude I was very thankful it was guarding my network so well, and I would go over and write a file on the target PC manually too. I'm not gonna lie: It was very fucking cool that it was able to do this without me ever needing to flash a USB drive, and by the time it was done it had set up Ubuntu, Tailscale and Jellyfin, and resolved the network issues; when I started watching a movie, the sound didn't work, so I prompted it and suddenly the sound came on as it wired up the HDMI adapter. Almost creepy. But I was pretty stunned at how reticent it was to do something relatively simple on my own network, with access I gave it. I think there must be a serious push right now to lock it down from monkeying with anything remotely, especially a BIOS.
