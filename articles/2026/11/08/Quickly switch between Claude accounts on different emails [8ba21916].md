---
id: "8ba219164c9be22b"
title: "Quickly switch between Claude accounts on different emails"
url: "https://willblackmore.github.io/hatstand"
link: "https://willblackmore.github.io/hatstand"
source: "Hatstand"
domain: "willblackmore.github.io"
source_type: "community"
collector: "reddit"
date: "2026-11-08T20:06:38Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["a_big_will"]
language: "en"
summary: "I use Claude for work and for personal use, and I like to keep those two things separate, so I have one account on my work email and another I pay for on my personal email. The work one logs in via SSO and my personal one uses my Google account. Signing out and back in again every time I wanted to switch was driving me nuts. I Googled it and there were plenty of guides for setting up multiple…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 522
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xr7qrt/quickly_switch_between_claude_accounts_on/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Quickly switch between Claude accounts on different emails

Hatstand · a_big_will · 2026-11-08

Installation
Hatstand isn’t code signed, so there’s a quick one-time setup before you can use it. After that, it works normally.
- Download Hatstand.dmg, open it and drag Hatstand into Applications.
- Open Hatstand. The first time, macOS says it can’t check the app for malicious software. Click Done.
- Open System Settings › Privacy & Security, scroll down to the message about Hatstand and click Open Anyway.
- Hatstand appears in your menu bar. Open Manage Instances… and click + to add your second account.
Alternatively…
Put your DIY hat on and build it yourself from the source code.
Not sure how? Paste the prompt below into Claude and the big guy will give you a hand.
Why Hatstand?
Claude only lets you be signed in to one account at a time. Switching means signing out and back in again, every time.
Hatstand keeps each account on its own peg. Pick one from the menu bar and Claude reopens as that account in seconds, with its chats, settings and Claude Code setup just as you left them.
Questions
Why does this exist?
I use Claude for work and in my personal life. Logging out and back in every time (especially with SSO or Google sign-in) got old fast.
There were already ways to run multiple instances, but they all involved the Terminal. I wanted something anyone could use.
I also wanted to see if I could build it with Claude. If I’m honest, this page took more effort than the app itself.
How do I use multiple Claude accounts on one Mac?
Hatstand gives each account its own Claude instance. Sign in once to each account, then switch between them from the menu bar. No signing out and back in.
Just bear in mind that if you open Claude from Spotlight, the Dock, or after an update, it’ll always open your default profile.
Can I keep my work and personal accounts separate?
Yeah. Each instance has its own sign-in, chats, settings, MCP servers and Cowork files.
Can I switch accounts without signing out?
Yes. Just pick an account from the menu bar. Claude closes and reopens as that account a few seconds later. The first time you use a new instance you’ll need to sign in, but that’s a one-off.
Does each account have its own Claude Code login?
Yes. Every instance has its own Claude Code settings, sessions and sign-in. The claude Terminal command isn’t affected.
Can I run two Claude accounts at the same time?
No. Hatstand only runs one Claude instance at a time. Switching closes the current one before opening the next.
Why did Claude switch back to my default account after updating?
Claude restarts itself after an update and bypasses Hatstand, so it opens your default account. You can switch back from the menu bar. The same happens if you launch Claude from the Dock or Spotlight.
Is Hatstand official?
Nope! It’s an independent open source project and isn’t affiliated with Anthropic.
Does Hatstand collect any data?
No. The only network request is an optional daily GitHub update check, which you can turn off in Settings.
