---
id: "bf0cd5e466c752b9"
title: "I've spent the last ten months building a project with Claude, and tonight I asked it to show me a bit of the code that he thinks is very clever and he's proud of"
url: "https://reddit.com/r/ClaudeAI/comments/1x73jfn/ive_spent_the_last_ten_months_building_a_project"
link: "https://reddit.com/r/ClaudeAI/comments/1x73jfn/ive_spent_the_last_ten_months_building_a_project"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T01:37:06Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["GodRaine"]
language: "en"
summary: "I'll pick the barcode scanner listener, src/hooks/useLabelScan.ts. It's about 50 lines, and one of them does nearly all the work: // A scanner's keys come well under this apart; a person's, well over. const GAP_MS = 60; const onKey = (event: KeyboardEvent) => { if (typingIn(event.target) || event.ctrlKey || event.metaKey || event.altKey) return; const now = performance.now(); if (now - last >…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 375
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x73jfn/ive_spent_the_last_ten_months_building_a_project/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I've spent the last ten months building a project with Claude, and tonight I asked it to show me a bit of the code that he thinks is very clever and he's proud of

Reddit · GodRaine · 2026-10-16

I'll pick the barcode scanner listener, src/hooks/useLabelScan.ts. It's about 50 lines, and one of them does nearly all the work: // A scanner's keys come well under this apart; a person's, well over. const GAP_MS = 60; const onKey = (event: KeyboardEvent) => { if (typingIn(event.target) || event.ctrlKey || event.metaKey || event.altKey) return; const now = performance.now(); if (now - last > GAP_MS) typed = ''; // ← this line last = now; if (event.key === 'Enter') { const code = typed.length >= 2 ? readLabelCode(typed) : null; typed = ''; ...navigate to the ticket or device } if (event.key.length === 1) typed = (typed + event.key).slice(-16); }; Here's why I love it. A USB barcode scanner isn't really a device the app can talk to. As far as the computer is concerned, it's a keyboard. There's no driver, no AP and no pairing. It just "types" T7001 and presses Enter. So the app can't ask "was that a scan?" It can only watch keystrokes, and a scan looks exactly like you typing on the Tickets page. Except for one thing: speed . A scanner types the whole code in a few milliseconds per key. A person, even a very fast one, leaves well over 60ms between keys most of the time. So instead of trying to recognise scans, the listener simply forgets anything slow. Every key that arrives more than 60ms after the last one wipes the buffer. Human typing never gets to build up a code: by the time you've pressed the third key, the first two are gone. A scanner's burst slides straight in, Enter arrives, and if what's there reads as a label code (T plus a number, or D plus a device ID), the app opens it. There's no mode, no "scan now" button, and no timer running in the background. It's one subtraction and a reset. The T in front matters too: scanning an old legacy label, which holds only a bare number, does nothing rather than opening some random ticket that happens to share the number. The label test proves both sides: the same T3 sent 8ms apart opens the ticket, and 150ms apart it doesn't. ---------------------------- I thought this was super cute, and I'm thrilled I asked!
