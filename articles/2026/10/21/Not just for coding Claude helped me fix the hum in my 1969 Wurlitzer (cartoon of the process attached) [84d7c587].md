---
id: "84d7c587158632b2"
title: "Not just for coding: Claude helped me fix the hum in my 1969 Wurlitzer (cartoon of the process attached)"
url: "https://reddit.com/r/ClaudeAI/comments/1xbj1os/not_just_for_coding_claude_helped_me_fix_the_hum"
link: "https://reddit.com/r/ClaudeAI/comments/1xbj1os/not_just_for_coding_claude_helped_me_fix_the_hum"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T10:01:59Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["johanze"]
language: "en"
summary: "I've built a few apps with Claude, but this week I used it for something completely different. I fixed my old Wurlitzer electric piano. It's a 1969 Model 200 that's been from the US to London to Sydney, and it buzzed and crackled like crazy when I recorded it. I can solder, but I'd never really diagnosed a circuit. What made it work: I'd record a few seconds of the noise, and Claude would…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 512
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbj1os/not_just_for_coding_claude_helped_me_fix_the_hum/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Not just for coding: Claude helped me fix the hum in my 1969 Wurlitzer (cartoon of the process attached)

Reddit · johanze · 2026-10-21

I've built a few apps with Claude, but this week I used it for something completely different. I fixed my old Wurlitzer electric piano. It's a 1969 Model 200 that's been from the US to London to Sydney, and it buzzed and crackled like crazy when I recorded it. I can solder, but I'd never really diagnosed a circuit. What made it work: I'd record a few seconds of the noise, and Claude would analyse the recording and tell me what kind of hum it was and where it was probably coming from. It talked me through the multimeter step by step: which setting, where to put the probes, what a good reading looks like. Before soldering anything, we'd clip a new part across the old one, record again, and only replace it if the noise actually dropped. It read the 1969 service manual and schematics, and checked them against photos of my board. Together we found a cracked fuse holder, a ground loop (this one is simple enough) , a couple of worn-out capacitors. The capacitor part was the most interesting: It worked out where the hum was coming from by its frequency. A 50 Hz hum meant ripple leaking from the pickup's high-voltage supply, which only pulses 50 times a second. A 100 Hz hum meant ripple from the main power supply. Old capacitors dry out and stop smoothing that ripple, and the leftover wobble ends up in the audio. It sourced the parts. It pulled the values from the 1969 schematic, chose modern replacements, and found them at my local electronics shop with part numbers. The order was about $40, and most of it ended up as spares. Then it showed me how to test before soldering anything. Capacitors side by side add together, so you can clip a new one across an old one with croc leads and it behaves like a replacement. It walked me through it all: unplug, and check the big caps have discharged with the meter; find which end of each old cap is positive by measuring the voltage on each leg; clip the new cap on, and use continuity checks to confirm it's connected and not shorting anything; power up, hands off, record. I tested each suspect in turn and recorded every time. Two tiny film caps on the pickup supply took about 8 dB off the 50 Hz hum. Of the three old electrolytics, only one made a difference to the 100 Hz, so that's the only one I soldered in. The other two stayed put. About $20 of parts actually used later, it's dramatically quieter. It did get a couple of things wrong along the way, but the next measurement always caught it. Then I asked it for a fun way to explain what I'd done, and it made this little cartoon. It's built entirely in code, with my real photos and the actual before-and-after recordings as the soundtrack (I was just noodling to test so don't judge the terrible playing!) Anyone else using it for hands-on, real-world stuff like this?
