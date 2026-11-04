---
id: "e411e594afaa8804"
title: "I’m a graphic designer with no coding background. Here’s what I learned building a 3D Solar System with Claude Code in two months"
url: "https://reddit.com/r/ClaudeAI/comments/1xnk173/im_a_graphic_designer_with_no_coding_background"
link: "https://reddit.com/r/ClaudeAI/comments/1xnk173/im_a_graphic_designer_with_no_coding_background"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T09:37:02Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Shevei1342"]
language: "en"
summary: "What: SOLARIA ( https://solaria3d.com ) is a browser model of the Solar System and the Milky Way. Planets and spacecraft are where they really are (NASA JPL data), and you can slice planets open, split their light into a spectrum, follow narrated tours, or zoom out to the Galaxy. Why: I wanted one place that explains space without overwhelming beginners, but still has depth if you dig. I’ve been…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 400
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnk173/im_a_graphic_designer_with_no_coding_background/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I’m a graphic designer with no coding background. Here’s what I learned building a 3D Solar System with Claude Code in two months

Reddit · Shevei1342 · 2026-11-04

What: SOLARIA ( https://solaria3d.com ) is a browser model of the Solar System and the Milky Way. Planets and spacecraft are where they really are (NASA JPL data), and you can slice planets open, split their light into a spectrum, follow narrated tours, or zoom out to the Galaxy. Why: I wanted one place that explains space without overwhelming beginners, but still has depth if you dig. I’ve been a graphic designer for 20 years and only remember some HTML and CSS, so without Claude Code this would have stayed an idea. How (the useful part, I hope): Give Claude a map, not the whole codebase. The main file is ~700 KB, too big to read at once. CLAUDE.md describes every file, and a script regenerates a map of the main file with line numbers after every change. Claude reads the map, then only the lines it needs. Turn every repeated mistake into a written rule. Claude once inserted a comment in the middle of a one-line function and commented out the rest of the code. It happened 7 times before it became a rule in CLAUDE.md. Since then it hasn’t come back. I keep separate cheat sheets for planets and stars, so every bug we’ve fixed once stays fixed. Automate the scary steps. Early on, a manual upload overwrote a file on the server and broke the site. Now one deploy script runs the tests, uploads only changed files, and checks them against the live site. I never upload by hand anymore. Build sliders instead of describing. “Move the camera a bit to the left” goes nowhere. So I had Claude build small tuning panels: I set the shot with sliders, copy the JSON and paste it back. Exact numbers, no guessing. Cheap model first, then check. Simple tasks go to a smaller model, and a bigger one only steps in when the result fails a check. Test on a real phone. Making the same app readable and smooth on a phone and a desktop was the hardest part of the whole project. Claude can drive my phone over adb and take screenshots, which caught problems the desktop never showed. What Claude didn’t do: decide what a beginner will understand. It offers a lot, but every “is this clear?” call was mine, and that’s where most of the 572 deployed versions went. Happy to answer questions about the setup.
