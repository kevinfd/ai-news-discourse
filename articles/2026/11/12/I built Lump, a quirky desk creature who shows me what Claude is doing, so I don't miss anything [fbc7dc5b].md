---
id: "fbc7dc5b8d33fe02"
title: "I built \"Lump,\" a quirky desk creature who shows me what Claude is doing, so I don't miss anything"
url: "https://reddit.com/r/ClaudeAI/comments/1xumt47/i_built_lump_a_quirky_desk_creature_who_shows_me"
link: "https://reddit.com/r/ClaudeAI/comments/1xumt47/i_built_lump_a_quirky_desk_creature_who_shows_me"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T19:51:40Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["joxy1999"]
language: "en"
summary: "This is Lump. He lives in a tiny glass cube on top of my monitor and keeps an eye on my Claude sessions, so I don't have to. I kept leaving Claude Code to work and then either staring at it waiting, or wandering off and coming back to find it had been sat on a permission prompt for 20 minutes. Now I just glance at Lump! What he does Works when Claude works. He opens his little laptop and types…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "business & funding"]
content_source: "post"
word_count: 697
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xumt47/i_built_lump_a_quirky_desk_creature_who_shows_me/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built "Lump," a quirky desk creature who shows me what Claude is doing, so I don't miss anything

Reddit · joxy1999 · 2026-11-12

This is Lump. He lives in a tiny glass cube on top of my monitor and keeps an eye on my Claude sessions, so I don't have to. I kept leaving Claude Code to work and then either staring at it waiting, or wandering off and coming back to find it had been sat on a permission prompt for 20 minutes. Now I just glance at Lump! What he does Works when Claude works. He opens his little laptop and types while any session is busy. Raises the alarm when Claude needs you: a permission prompt, a question, a plan to approve. Leave him long enough and he gets grumpy and holds up a sign. Celebrates when it's done. Changes colour with your usage. He's tangerine normally and flushes red as you get close to your 5-hour or weekly limits. Keeps time. Optional: give him your calendar and he fades to blue in the 10 minutes before a meeting, then sets off an alarm clock when it starts. Sleeps at night (midnight to 8am), with a blanket and a snore. Tap the glass and he does a bit. There's a motion sensor in the cube, so a tap plays one of 12 silly animations. He has his own little voice. He chirps on a tiny ocarina when Claude needs you or finishes, and every gag has its own sound effects, timed to the drawings. It's all optional: you can switch the sounds off completely, or just the moments you don't want, and he keeps quiet at night if you're not around. Little counters in the corners show how many sessions are working, waiting on you, or finished and unread. He follows Claude Code, and also Chat and Cowork in the Claude desktop app. There are optional extras too: a paper plane when someone DMs you on Slack, and a letter he holds up when someone important messages you. There's also a tiny Lump for your Mac. He sits beside the notch (or in the menu bar) when you're away from your desk, and hides when you're back at it. How it works The hardware is a Waveshare/SpotPear ESP32-S3 "prism" display: a 240×240 screen behind a glass cube, about $20 on AliExpress. The mount is 3D printed. It sticks to the back of my monitor and holds him just above the top edge, so he sits at eye level against a dark background. It tilts and swivels, with printed thumbscrews to set the angle by hand, and the STLs are in the repo. Claude Code hooks (small async ones, plus the status line for usage) tell a little bridge service on the Mac what every session is doing. The bridge boils all that down to one mood and sends it to the cube over USB or Wi-Fi. Chat and Cowork don't have hooks, so a small Swift helper reads the Claude app's window through macOS Accessibility. The animation is all pre-baked: around 11 MB of frames sit in the board's flash and play at 24 fps, with transitions between moods so he wakes up, startles or dozes off instead of cutting. If the Mac goes quiet, he notices, shows a little unplugged-cable mark and just potters about on his own. Everything stays on your machine. The only things that go out are the optional calendar and Slack lookups, which run with your own links and tokens. Make your own It's open source: https://github.com/joebentham/desk-buddy You need: the ESP32-S3-LCD-1.3 prism (the listing is linked in the README) a USB-C data cable for the first flash a Mac (the bridge is macOS-only for now) Claude Code optionally, a 3D printer for the mount (print settings and assembly are in the repo) Setup is four commands: flash the board, install the bridge, install the hooks, and (optionally) set up Wi-Fi. After that he only needs power, and updates go over the air. The code and 3D models are MIT licensed. Lump himself is CC BY-NC, so build one, remix him and share it, just don't sell him. If you want to redraw him or add gags, the whole character lives in one HTML file with a live preview. Happy to answer questions.
