---
id: "bfa64b651a46c65b"
title: "Claude Code installed tooling which was actually Expiro virus."
url: "https://reddit.com/r/ClaudeAI/comments/1xa1ds8/claude_code_installed_tooling_which_was_actually"
link: "https://reddit.com/r/ClaudeAI/comments/1xa1ds8/claude_code_installed_tooling_which_was_actually"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T16:21:47Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["StaticCG58"]
language: "en"
summary: "I had a late night vibe session working on a decomp of an old game, using REA and Claude. Claude made great progress and the goal of the workflow was to recomp the game into x64 and run natively on windows. I gave it free reign (naively) and told it to get whatever tooling it could find to help the de-compilation. After about 10 hours of agents, and work, we were at a great point, and we had a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 274
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xa1ds8/claude_code_installed_tooling_which_was_actually/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code installed tooling which was actually Expiro virus.

Reddit · StaticCG58 · 2026-10-19

I had a late night vibe session working on a decomp of an old game, using REA and Claude. Claude made great progress and the goal of the workflow was to recomp the game into x64 and run natively on windows. I gave it free reign (naively) and told it to get whatever tooling it could find to help the de-compilation. After about 10 hours of agents, and work, we were at a great point, and we had a native version of the game running to the title screen. (I say we like I did anything lol) Then it starts saying PCSX2 is crashing. Then other files have a really long weird attribute in the header called vmp. It then full stops and states "Stopped on a security blocker: Windows Defender quarantined four executables during the run (two redacted.exe builds, tracediff.exe, and C:\ninja\ninja.exe) as Virus:Win32/Expiro.HNW!MTB / Win64/Expiro.DD!MTB. Before that: DMAC re-arm fix + tests; IPU wired; the opening FMV decodes end to end (2,670 pictures, 0 IPU errors) when the ADXI model drives the movie clock; title reached at PCSX2's frame with code band 0 but the picture renders wrong (open). Profile and byte-identical movie determinism not done." I go look, do a MalwareBytes scan, my entire computer has a self replicating Expiro virus running. Almost every file on the system is infected. Now I gotta reinstall windows. Good news is if I am ever doing projects like this again it will be in a VM. Just wanted to share because I am pissed I gotta reinstall windows and safely migrate other projects off the drive and confirm that they are clean as well.
