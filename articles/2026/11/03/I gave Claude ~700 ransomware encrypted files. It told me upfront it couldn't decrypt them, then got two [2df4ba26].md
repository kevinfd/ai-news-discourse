---
id: "2df4ba2698289617"
title: "I gave Claude ~700 ransomware encrypted files. It told me upfront it couldn't decrypt them, then got two thirds of them usable again"
url: "https://reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it"
link: "https://reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T22:10:39Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Rare-Protection4270"]
language: "en"
summary: "The most interesting thing I've done with Claude, so sharing how it went. Background: ransomware encrypted my files back in 2019. I kept them for seven years, hoping something would eventually be able to open them. What stood out about how it worked: - It was honest from the start. The first answer was: no decryption, per-file AES keys under RSA, forget it. Then it looked for another way in. -…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 315
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude ~700 ransomware encrypted files. It told me upfront it couldn't decrypt them, then got two thirds of them usable again

Reddit · Rare-Protection4270 · 2026-11-03

The most interesting thing I've done with Claude, so sharing how it went. Background: ransomware encrypted my files back in 2019. I kept them for seven years, hoping something would eventually be able to open them. What stood out about how it worked: - It was honest from the start. The first answer was: no decryption, per-file AES keys under RSA, forget it. Then it looked for another way in. - Found the weak spot itself. It compared the encrypted files with a few unencrypted copies I had and saw that only the first 16 KB of each file is encrypted. - Built a real tool, not a one-off script. A module per format (JPEG, PNG, PSD, Excel, PDF, MP4...), re-run over all the files after each improvement. The last round alone brought back about 100 more files. - Decided on its own to train a model. The web pictures came back without light and color, and it concluded better formulas wouldn't fix that. So it trained a U-Net on my RTX 4070, using intact photos damaged the same way. Color errors dropped by more than half. - It wrote its own SketchUp reader. Using openskp's format notes as a reference, it wrote a parser from scratch, decoded three undocumented record types from the bytes, and got the whole 239 MB model out as format I imported into Blender. - Checked its own work. It scripted the whole Blender scene for me and fixed what I pointed out. Left: original SketchUp render. Right: Blender, rebuilt from encrypted model. Results: 26% fully restored, 27% open with some damage, 12% content saved into new files, 35% lost. I also tried GPT-6.1 Astra on the same files. It recovered some, but fell behind after the first session. [How I worked: Claude Code in VS Code, Opus 5.5, about 1 week of sessions] Full write-up with before/after pictures: https://medium.com/@weaxdesign/ai-unlocked-my-ransomware-encrypted-files-without-the-key-262212277514?sk=c58cddebd2f5a6aee8524f900f29488c
