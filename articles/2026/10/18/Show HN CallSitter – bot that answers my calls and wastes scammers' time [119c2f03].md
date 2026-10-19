---
id: "119c2f0303cf55e0"
title: "Show HN: CallSitter – bot that answers my calls and wastes scammers' time"
url: "https://github.com/szerintedmi/callsitter"
link: "https://github.com/szerintedmi/callsitter"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-18T12:24:53Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["szert"]
language: "en"
summary: "Anyone else get a lot of dumb scam calls? These days I mostly get them on my mobile. I used to just ignore them, but then I got fed up and built a bot that answers my calls and wastes their time. It runs on OpenAI Live 1. Jev classifies each call as spam, scam or genuine and steers the bot accordingly. Works like a charm. All my calls go to the bot now. I can also steer it from Telegram…"
tags: []
orgs: ["OpenAI"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 734
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50140472"
score: 13
comments: 10
community: "Hacker News"
---

# Show HN: CallSitter – bot that answers my calls and wastes scammers' time

GitHub · szert · 2026-10-18

An AI that answers my phone. Scammers get their time wasted, sales calls get a polite no, and real callers get their message taken.
Try to scam the bot, or get a message through to me, from your browser: callsitter.org/play.
Calls to my number divert to a Telnyx number, where an OpenAI gpt-live-1 agent answers. TypeSafe Jev classifies the growing transcript, and a deterministic call flow (config/call-flow.yaml) steers the agent:
- Scam (Jev ≥ 0.80): waste their time, mixing a few tactics.
- Sales call (spam, Jev ≥ 0.85): decline politely, ask to be taken off the list, say goodbye.
- Genuine caller (Jev ≥ 0.7): take a message; it reaches me in the call summary.
- Urgent (urgency ≥ 0.85 while scam + spam is under 0.5, or Luna says I may want to act while the caller is on the line): a notifying 🚨 reply on Telegram, once per call (telegram.yaml → status.urgent_alert). It doesn't steer the call.
GPT-6 Luna writes for me, not the caller: the rolling summary, open questions and suggested replies, and the end-of-call summary. She doesn't steer the agent mid-call.
Telegram (telegram.yaml): one status message per call, edited as it goes with the verdict, the stage, Luna's summary and open questions, and the transcript (newest first, collapsed). Jev decides when the summary is out of date (jev.yaml → owner_update, ≥ 0.8), with a refresh every 30 s anyway while the caller talks (luna.yaml → progress). When the call ends, Luna's summary, the cost and a link to the call page replace it.
Steering from Telegram: reply to a status message, or send one while a call is live, and it reaches the agent as a SUPERVISOR: line: plain text as commentary, ! for instructions (cuts the agent off), ~ for thinking. The Genuine, Scam and Spam buttons move the call into that stage (genuine, waste_time, decline_spam) as if Jev had decided; Hang up (or /hangup) has the agent say goodbye, then ends the call. A message alone can't end a call. Up to 3 replies Luna suggests go as commentary (telegram.yaml → steering.suggestions). The automatic flow keeps running, but a stage text it sends within 30 s of your message or button waits until then, so it doesn't replace what you said (steering.hold_stage_ms). Your messages show on the call page as "owner → Live".
Taking a call over: a Take over button under a live call's status message (private chat only) opens a page inside Telegram. The agent tells the caller it's putting them through, and from then on I talk to the caller myself, through the page's microphone and speaker. Over OpenAI SIP the call is transferred (SIP REFER) to the Telnyx Call Control app and bridged through the server; the bot stops, the recording keeps going, and Live is billed only up to the handover (setup). The admin call page has the same Take over button; it opens the page in a new tab, signed in by Cloudflare Access instead of Telegram.
Costs come from what the vendors report: Live per second, Luna's tokens (uncached, cached, cache writes, output, times the service tier) and Jev's input tokens (cost.yaml). Each call stores the breakdown; the call list, the call page and the final Telegram update show it.
Limits (limits.yaml, src/core/limits.ts), per channel (the phone number, admin test calls, the public page): spend, calls a day, calls at once, calls per caller a day and call length, counted over a rolling 24 h from the call list. Once the last 24 h's phone calls have cost $20, the next caller hears busy (SIP 486) before anything billed starts, and I get one Telegram line about it; the call that crosses the cap runs to its end.
bun install
cp .env.example .env      # fill in keys
bun run dev               # http://127.0.0.1:8787/ (admin UI), config hot-reloads
- Development: replay, evals, test calls, the code layout, the config files and what reaches Live when.
- Setup: Telnyx, Telegram, the Cloudflare tunnel, OpenAI SIP, owner takeover.
- Public site: the real-call pages, the games and their caps.
- Vendor APIs: how the design maps to Live, Jev and Telnyx, and what's been verified on real calls.
- Production deploy: the VPS, deploys, backups, copying prod data.
- Real-call demos: making a new recording for the public page.
The code is Apache-2.0. The call recordings in demos/ are not: all rights reserved (NOTICE).
