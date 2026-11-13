---
id: "1de1817c67f86255"
title: "I fixed a nearly unusable AliExpress LED controller with Claude Code, then kept going until my mirror plays thunderstorms"
url: "https://reddit.com/r/ClaudeAI/comments/1xucgqz/i_fixed_a_nearly_unusable_aliexpress_led"
link: "https://reddit.com/r/ClaudeAI/comments/1xucgqz/i_fixed_a_nearly_unusable_aliexpress_led"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T13:14:34Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Worried_Menu4016"]
language: "en"
summary: "I have a cheap HomeKit RGB strip controller from AliExpress (Athom LS5050C, an ESP8266) behind my bedroom mirror. The mirror is far from the router, the signal is around -90 dBm, and the stock firmware was close to unusable there: about a quarter of pings were slow, some answers took a full second, and the Home app often showed it as not responding. I'm a designer who codes a bit, not a firmware…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "business & funding", "models & research"]
content_source: "post"
word_count: 720
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xucgqz/i_fixed_a_nearly_unusable_aliexpress_led/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I fixed a nearly unusable AliExpress LED controller with Claude Code, then kept going until my mirror plays thunderstorms

Reddit · Worried_Menu4016 · 2026-11-12

I have a cheap HomeKit RGB strip controller from AliExpress (Athom LS5050C, an ESP8266) behind my bedroom mirror. The mirror is far from the router, the signal is around -90 dBm, and the stock firmware was close to unusable there: about a quarter of pings were slow, some answers took a full second, and the Home app often showed it as not responding. I'm a designer who codes a bit, not a firmware person. So I did this with Claude Code: I decided what to build, what to measure and what to keep, and Claude Code wrote the code, the tests and the measurement scripts. The Claude Code part I use every day The strip has a "Claude" switch in the Home app. A Stop hook in Claude Code sends one curl to the strip, and the mirror blinks orange when Claude finishes answering. That way I can walk away during long tasks. This is the hook in ~/.claude/settings.json (put your strip's address in place of 192.0.2.10): { "hooks": { "Stop": [ { "hooks": [ { "type": "command", "async": true, "timeout": 5, "command": "curl -s -m 2 'http://192.0.2.10/api/flash?hex=ff8000&n=3&src=claude' >/dev/null 2>&1 || true" } ] } ] } } The blink only shows while the "Claude" switch is on, so I can turn it off at night from the Home app. How it went The first thing I asked for was a measurement, not a fix: a small script that pings the strip 200 times and sends 40 HTTP requests. Every firmware change after that was judged by the same script. There is no serial port on the board, so a bad update could brick it for good. A few early versions never rejoined the Wi-Fi at all. After that we built a self-restore guard: a known-good image sits at the top of flash and comes back by itself if a new one can't be reached within a few minutes. Every update since goes through it. The strangest fix: making the main loop rest 1 ms on every pass. Same binary, same signal, 71 of 90 requests answered with the loop spinning and 90 of 90 with it resting. I don't know exactly why this works, and neither of us could prove a cause, so the README just reports the measurement. Numbers (stock firmware vs my current one, about -90 dBm) pings slower than 50 ms: 27% before, 3-4% now slowest HTTP answer: about 1 s before, 265 ms now 900 of 900 commands answered in a row, with rare answers as slow as 2.5 s The "before" is a single session. I can't measure it again, because the stock firmware can't be put back on the device. -90 dBm is close to where Wi-Fi gives up, and I suspect it explains the rare 2.5 s answers and part of the original trouble. That's a guess, I haven't measured it. Yes, a mesh node would probably fix most of this. I wanted to see how far the firmware alone could go. Then I didn't stop Once it was reliable I kept asking for more: a sunrise alarm: 30 minutes of light before the alarm; the alarm time is set from the strip's own web page (an iPhone Shortcut is next on the list) thunderstorms played from the Mac with real recordings, where the light follows the loudness of each thunder clap (that's the video) the Xiaomi air purifier read on the local network, so the mirror blinks when the air gets bad Home app switches for each scene and light mode Some scenes are still experimental and haven't been tried on the real light yet: planes overhead shown as the flag of their destination, a stormy sea, the live sky over any place, the Sun's X-ray activity, and a sleep scene, which is just very dim amber light slowly fading to dark. No claims about sleep. What I learned about working this way Ask for a measurement before a fix, and keep the same measurement for every version. Make it say "I don't know" when it doesn't. The 1 ms finding stayed a finding, not a theory. Plan the way back before flashing anything you can't reach with a cable. It's free and open source (MIT): https://github.com/thousandflowers/specchio-fw It runs on this one controller model; other ESP8266 boards might need different pins.
