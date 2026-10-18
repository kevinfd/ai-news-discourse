---
id: "9c89ab5c0cf495d4"
title: "I let Claude handle the software side of my new 3D printer, and it set the whole thing up"
url: "https://reddit.com/r/ClaudeAI/comments/1x8xz3l/i_let_claude_handle_the_software_side_of_my_new"
link: "https://reddit.com/r/ClaudeAI/comments/1x8xz3l/i_let_claude_handle_the_software_side_of_my_new"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T08:25:37Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Greedy-Duck"]
language: "en"
summary: "Hi all, decided to post this here because I think I'd just get AI hate on the printing subs. I wanted to get into 3D printing but didn't want to sink time into learning the software, so I got Claude to do it! It also helped me pick the printer (a QIDI Q2), since it worked out the printer runs Klipper/Moonraker with an API it could work with. Claude built me a small self-hosted server…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 241
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8xz3l/i_let_claude_handle_the_software_side_of_my_new/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I let Claude handle the software side of my new 3D printer, and it set the whole thing up

Reddit · Greedy-Duck · 2026-10-18

Hi all, decided to post this here because I think I'd just get AI hate on the printing subs. I wanted to get into 3D printing but didn't want to sink time into learning the software, so I got Claude to do it! It also helped me pick the printer (a QIDI Q2), since it worked out the printer runs Klipper/Moonraker with an API it could work with. Claude built me a small self-hosted server ("printhub") that sits between Claude and the printer: - Plain-English printing: "find me a phone stand" → it searches Printables, slices with OrcaSlicer (official Q2 profiles), and shows time/grams/cost → I say yes → it prints. - Guardrails: nothing starts or cancels without my confirmation. It won't start if the loaded filament doesn't match the slice. No raw G-code. - Phone alerts (ntfy): start, first-layer photo, pause/runout (with Resume and Cancel buttons), done, errors. - Stays local: it runs in a Proxmox container, the printer is firewalled so only that server can reach it, and remote access is through Tailscale. - Request page: my partner can chat to request prints or jobs, and I approve them. Lessons so far: a firmware update broke the camera config (wrong camera ID), which Claude found and fixed. My first two "prints" printed air because the filament never got gripped. Keep pushing during Load until plastic comes out of the nozzle! First Benchy came out great, just a little stringing.
