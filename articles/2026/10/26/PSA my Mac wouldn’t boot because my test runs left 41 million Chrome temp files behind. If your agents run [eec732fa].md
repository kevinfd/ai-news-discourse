---
id: "eec732fa2f87804a"
title: "PSA: my Mac wouldn’t boot because my test runs left 41 million Chrome temp files behind. If your agents run browser tests, check your temp folder."
url: "https://reddit.com/r/ClaudeAI/comments/1xg9jt1/psa_my_mac_wouldnt_boot_because_my_test_runs_left"
link: "https://reddit.com/r/ClaudeAI/comments/1xg9jt1/psa_my_mac_wouldnt_boot_because_my_test_runs_left"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T21:18:46Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["bekircagricelik"]
language: "en"
summary: "Last night my Mac Studio got stuck on the boot progress bar. Safe Mode: stuck. First Aid: stuck. I was up until 5am pulling the boot logs off it from my other computer, with Claude Code helping me read them. Every boot died on the same step: macOS cleaning up a temp folder before login. A normal one has a few hundred files. Mine had 41 million . What happened: I’m a solo founder building a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding", "business & funding", "jobs & society"]
content_source: "post"
word_count: 297
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xg9jt1/psa_my_mac_wouldnt_boot_because_my_test_runs_left/"
score: null
comments: null
community: "r/ClaudeAI"
---

# PSA: my Mac wouldn’t boot because my test runs left 41 million Chrome temp files behind. If your agents run browser tests, check your temp folder.

Reddit · bekircagricelik · 2026-10-26

Last night my Mac Studio got stuck on the boot progress bar. Safe Mode: stuck. First Aid: stuck. I was up until 5am pulling the boot logs off it from my other computer, with Claude Code helping me read them. Every boot died on the same step: macOS cleaning up a temp folder before login. A normal one has a few hundred files. Mine had 41 million . What happened: I’m a solo founder building a journaling app, and I run a lot of automated tests: agents spinning up headless Chrome for UI checks, screenshots and so on. Every launch creates a throwaway Chrome profile folder (thousands of small files). When a run ended cleanly, it got deleted. When a run was killed (timeouts, me stopping a job, a crash), it didn’t. Weeks of that added up to 41M files, and macOS tried to tidy every one before letting me in. The fix: move that folder out of the way, restart. Booted right up, nothing lost. How to not do this to yourself if your agents run browsers: Give every run its own temp folder (set TMPDIR per job) and delete it at the end with a trap on EXIT/INT/TERM, not just on success. If you launch Chrome through a wrapper script, kill the whole process group , not just the wrapper. Otherwise Chrome lives on as an orphan. Add --use-mock-keychain --password-store=basic so dozens of test profiles don’t hammer the macOS keychain (that was also why my Mac had been sluggish). Before starting a big test run, count the files in your temp dirs and refuse to start above a threshold. Check what’s piling up right now: find "$(getconf DARWIN_USER_TEMP_DIR)" | wc -l Anyway, back to building. My Mac and I are in couples therapy now. ❤️‍🩹
