---
id: "15f227957c876f67"
title: "I used Claude Code to get an old Rockchip chip running modern Debian. The drivers are now open source."
url: "https://github.com/Comzee/rk3128-linux"
link: "https://github.com/Comzee/rk3128-linux"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T20:49:20Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["layerone"]
language: "en"
summary: "I built an open-source collection of Linux drivers, patches, configuration, and technical documentation for running modern Debian on the Rockchip RK3128. I used Claude Code to help investigate hardware behavior, develop and debug driver changes, and write validation tests. The work covers Mali-400 graphics through Mesa Lima, H.264/HEVC hardware decoding, hardware JPEG decoding, display…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 277
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xs3bb3/i_used_claude_code_to_get_an_old_rockchip_chip/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to get an old Rockchip chip running modern Debian. The drivers are now open source.

GitHub · layerone · 2026-11-09

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert
Reference for Rockchip Linux kernel drivers and modern Debian: native RK3128 support on Linux 7.3.1 / Debian 13 armhf, tested on an RK3128 reference board with 1 GiB RAM and a 1920×1080 LVDS display. Source, patches, configuration, examples and checks are included; applications and a complete bootable system are outside this collection. Versions and patch order · Source pins · Validation.
Tested on RK3128. Shared Rockchip IP drivers and techniques may help other RK31xx ports; register maps, clocks, resets, power domains and board device trees require chip-specific checks.
Measured improvements
Lima/Mali-400 graphics: captured demo fragment shaders compile to 42 instructions instead of 76 with upstream Lima (~45% fewer). The full optimized graphics stack doubled bottlenecked demo scenes from ~25.5 to 51 FPS at unchanged clocks, including presentation-pacing changes outside this collection. Measurements and scope.
Hardware video: RK3128 HEVC enablement, shared Hantro/HEVC bus arbitration and H.264 fixes, validated with reference-frame comparisons and zero-drop 1080p playback tests. Media.
Stable scanout: initializing the LCDC NoC priority eliminated measured FIFO underflows in matched workloads, where decoder drop counters alone had missed the problem. Display evidence.
Audio CPU cost: patched ALSA reduced one-core CPU use from 2.18% to 0.82% (~62% less) versus Debian libasound in the same 44.1 kHz stereo playback test, with zero underruns. Measurement.
Hardware JPEG: a tested 12 MP baseline JPEG decoded and converted to RGB in 386 ms versus 1.70 s with stb_image software decoding (~4.4× faster). Measurement and limits.
