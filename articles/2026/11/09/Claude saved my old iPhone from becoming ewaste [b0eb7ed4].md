---
id: "b0eb7ed4d296f748"
title: "Claude saved my old iPhone from becoming ewaste"
url: "https://reddit.com/r/ClaudeAI/comments/1xrevbv/claude_saved_my_old_iphone_from_becoming_ewaste"
link: "https://reddit.com/r/ClaudeAI/comments/1xrevbv/claude_saved_my_old_iphone_from_becoming_ewaste"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T01:30:10Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Intelligent_Equal688"]
language: "en"
summary: "Semi - new Claude user here. I had my old iPhone se that would not boot into anything, restore, ramdisk, nothing. Got to a point where I thought the nand had failed as it'd kernel panic or just die instantly. After longer than I want to admit of trying fixes I sent Claude the logs from a kernel panic it kept encountering when booting a ramdisk. It diagnosed the problem first try, the light…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 213
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrevbv/claude_saved_my_old_iphone_from_becoming_ewaste/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude saved my old iPhone from becoming ewaste

Reddit · Intelligent_Equal688 · 2026-11-09

Semi - new Claude user here. I had my old iPhone se that would not boot into anything, restore, ramdisk, nothing. Got to a point where I thought the nand had failed as it'd kernel panic or just die instantly. After longer than I want to admit of trying fixes I sent Claude the logs from a kernel panic it kept encountering when booting a ramdisk. It diagnosed the problem first try, the light sensor broke. But after opening the device, I saw it was the board connector, it was water damaged so a new screen wouldn't do anything. So as a test, it patched the sensor out of the boot process in sshrd_script, where the panic kept happening. Booted first try without a panic and the rest of the script worked as usual, I rooted right in and backed up some files. It pushed the fix into a new tool it made to patch the check out of regular Ipsw files, I restored one of the patched files to the phone and it worked first try!! Only boots tethered right now, however everything else is flawless. Ik it's on a smaller scale than others projects but it solved the issue I'd been working on for hours in 20 minutes. Claude is fantastic.
