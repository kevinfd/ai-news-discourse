---
id: "67597aa6bdc9e3ff"
title: "Back up your Claude Code sessions and use them on any machine"
url: "https://session-vault.dev"
link: "https://session-vault.dev"
source: "session-vault.dev"
domain: "session-vault.dev"
source_type: "community"
collector: "hackernews"
date: "2026-11-26T13:43:14Z"
published_date: "2026-11-26"
collected_at: "2026-11-27T13:04:05Z"
authors: ["me2too"]
language: "en"
summary: "Back up your Claude Code sessions and use them on any machine\nClaude Code keeps each conversation in ~/.claude, only on\nthe machine where it happened, and by default deletes transcripts older\nthan 30 days. Session Vault keeps an encrypted copy of the sessions you\nwant to hold on to.\nA saved session survives that cleanup, a new laptop or a wiped disk, and you can fetch it on any of your machines…"
tags: []
orgs: ["Anthropic"]
topics: []
content_source: "fulltext"
word_count: 329
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50655243"
score: 26
comments: 6
community: "Hacker News"
---

# Back up your Claude Code sessions and use them on any machine

session-vault.dev · me2too · 2026-11-26

Back up your Claude Code sessions and use them on any machine
Claude Code keeps each conversation in ~/.claude, only on
the machine where it happened, and by default deletes transcripts older
than 30 days. Session Vault keeps an encrypted copy of the sessions you
want to hold on to.
A saved session survives that cleanup, a new laptop or a wiped disk, and you can fetch it on any of your machines and carry on where you left off.
/session-vault:save    save the current session
/session-vault:fetch   restore a saved session here
It's a Claude Code plugin, so both commands run inside Claude Code.
How it works
Before uploading, the plugin encrypts the transcript with age, using a key created on your machine the first time you save. The server keeps the encrypted file plus what it needs to find it again: the session ID, the project, the folder it was saved from and an optional name. It can't read the conversation.
To fetch on another machine, copy the key
    (~/.config/session-vault/age.key) there. Keep a backup of
    it too: it's the only copy, and without it nobody can decrypt your
    sessions, us included.
Plans
Plans differ only in how many sessions you can store.
Saving a session again doesn't count as a new one. If you move to a smaller plan nothing is deleted; you just can't add sessions until you're under the new limit.
Running it yourself
The server is open source. If you'd rather keep your sessions on your own hardware, run it there and point the plugin at it. You won't need an account here.
Get started
1. Enter your email and we'll send you a link. The first time, it creates your account and shows you your token; after that it just signs you in.
2. Install the plugin in Claude Code:
/plugin marketplace add galeone/session-vault-plugin
/plugin install session-vault@galeone-plugins
3. Put your token in
    ~/.config/session-vault/config:
SESSION_VAULT_URL=https://session-vault.dev
SESSION_VAULT_TOKEN=your-token
4. Run /session-vault:save. The first
    save creates age.key in
    ~/.config/session-vault/.
