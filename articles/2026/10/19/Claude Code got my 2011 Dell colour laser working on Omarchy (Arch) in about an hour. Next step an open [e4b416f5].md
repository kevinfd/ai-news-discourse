---
id: "e4b416f557dbe6d5"
title: "Claude Code got my 2011 Dell colour laser working on Omarchy (Arch) in about an hour. Next step: an open 64-bit driver."
url: "https://reddit.com/r/ClaudeAI/comments/1x9w4f6/claude_code_got_my_2011_dell_colour_laser_working"
link: "https://reddit.com/r/ClaudeAI/comments/1x9w4f6/claude_code_got_my_2011_dell_colour_laser_working"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T12:54:47Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["looneycheetah"]
language: "en"
summary: "I'm a GP, not a Linux engineer. I have a Dell C1760nw colour laser. Dell never made a Linux driver for it. My estimate for sorting it myself with web searches and trial and error: two days. With Claude Code in the Claude desktop app on Linux, it took about an hour from plugging in the USB cable to printing. Claude Code taught me that, - The C1760nw is a rebadged Xerox Phaser 6000/6010. Its USB…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 480
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9w4f6/claude_code_got_my_2011_dell_colour_laser_working/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code got my 2011 Dell colour laser working on Omarchy (Arch) in about an hour. Next step: an open 64-bit driver.

Reddit · looneycheetah · 2026-10-19

I'm a GP, not a Linux engineer. I have a Dell C1760nw colour laser. Dell never made a Linux driver for it. My estimate for sorting it myself with web searches and trial and error: two days. With Claude Code in the Claude desktop app on Linux, it took about an hour from plugging in the USB cable to printing. Claude Code taught me that, - The C1760nw is a rebadged Xerox Phaser 6000/6010. Its USB ID confirms it speaks HBPL v1, an old host-based printer language. - foo2zjs only covers HBPL v2, so that was a dead end. - The AUR package xerox-phaser-6000-6010 is the right driver, but its build is broken: the Xerox download link redirects to itself forever. Claude found the same zip on the Wayback Machine (July 2025 snapshot) and checked it against the PKGBUILD sha256 before using it. It matched exactly. If you have this printer, put that file in yay's build folder and the package builds. - The driver is 32-bit from 2011. It needs lib32-libstdc++5 and libstdc++5 from the AUR, which compile parts of GCC 3.3.6 from source. Wall of warnings, but it built fine on a current system. Then the real-world gotchas, which is where it got interesting in Claude Code's own words: A PDF printed as blank pages. Instead of wasting more paper, Claude ran the PDF through the CUPS filters on the computer and measured the output: 0% ink. CUPS pdftopdf could not read how ReportLab packs its pages ("Unsupported compound stream filter"). Fix: rewrite the PDF with Ghostscript first. My idea was to test one page before printing 60. Two copies printed as four. CUPS makes the copies, and then the old Xerox driver also tells the printer COPIES=2. Fix: an 8-line wrapper that tells the driver 1 copy, plus one PPD setting. Test: 1 page x 2 copies = 2 sheets. Bonus: the toner levels are hidden in the printer's USB status string. They match the bars on its LCD. It was not flawless. At one point Claude's background checker reported the install as finished while it was still compiling. It caught the mismatch itself and told me. I typed my own sudo password every time; I am glad Claude never saw it. I made the calls; Claude did the digging. Now the stirring bit. CUPS warns that classic drivers like this will stop working in a future version, and this one is a 32-bit binary from 2011. So the plan, if CUPS ever breaks it, is to build an open 64-bit HBPL v1 driver. Not from nothing: Claude found that people have already reverse-engineered the format, and there are open-source starting points. We would build on that and test against the real printer. Call it vibe coding if you like. I would call it working with a very patient colleague who reads hex dumps for fun 😄.
