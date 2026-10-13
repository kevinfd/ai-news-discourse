---
id: "48926f953b564848"
title: "Show HN: MemorySync – Memory for AI Agents"
url: "https://memorysync.io/try"
source: "MemorySync"
domain: "memorysync.io"
source_type: "community"
collector: "hackernews"
date: "2026-10-13T12:35:42Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["mohd_rafay"]
language: "en"
summary: "I created MemorySync because I kept running into the problem of AI agents not being able to remember useful things about users between conversations. I wanted an easy way to give the agents memory in my application without having to build the whole thing myself.\nMemorySync is an API for giving AI agents memory. The application sends MemorySync information provided by the user, MemorySync saves…"
tags: []
orgs: []
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 662
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50070688"
score: 22
comments: 1
community: "Hacker News"
---

# Show HN: MemorySync – Memory for AI Agents

MemorySync · mohd_rafay · 2026-10-13

Playground
Try persistent memory in your browser
Tell MemorySync one fact, reload the page, then ask for it back in your own words. No signup, nothing to install — and every API call is shown as it happens.
- No signup
- Real production API
- Private to your browser
- Saving to
- Demo space
- Page load
- —
Write one fact about you or your work. It’s saved on MemorySync’s servers, not in this page — and not word for word: the lasting facts are pulled out, so one sentence can become more than one memory.
Now reload. Reloading throws this page away — every variable and all of its state. Watch the page load number above change. If the fact still comes back in step 3, it was stored on the server, not in your browser. That’s the boundary most agent memory doesn’t survive.
Ask in your own words. MemorySync searches by meaning, so you don’t need to repeat the words you used.
API calls
Every button calls the production API.
“Remember this” will send this request. It updates as you type.
curl -X POST https://api.memorysync.io/memory/add \  -H "X-API-Key: $MEMORYSYNC_API_KEY" \  -H "X-End-User-ID: YOUR_END_USER_ID" \  -H "Content-Type: application/json" \  -d '{"text":"I always use Postgres for new services and never MySQL.","source":"playground","tags":["playground"]}'
The demo key is kept on our server and never sent to your browser. Put your key in MEMORYSYNC_API_KEY and every request here runs as-is.
Get your own API key
Free, with no signup form. Create a key now, then add your email to keep it.
1 · Create
A real key for the MemorySync API, created instantly. From then on the steps above save to your own account, and anything you already saved is copied into it.
2 · Keep it
After you create a key, add your email here. The same key keeps working and stops expiring, and your account moves to the free plan — 10,000 writes and 1,000 searches a month.
Questions
Is this the real MemorySync API?
Yes. Every button calls the production API at api.memorysync.io, and the API calls panel shows each request exactly as it was sent, with the demo key hidden.
Can anyone else see what I type?
Other visitors cannot. Your browser gets its own private scope, and memories stored under it are only returned for that scope. Until you create a key, the playground runs on MemorySync’s own demo account, so please don’t enter anything sensitive.
What does reloading the page prove?
That the memory is not kept in your browser. Reloading throws the page away, and the fact still comes back because it is stored on MemorySync’s servers — the same way it survives between your agent’s sessions.
How is this different from chat history?
Chat history is the raw conversation, and a new session starts without it. MemorySync pulls out the lasting facts, stores them outside any single session, and returns the relevant ones by meaning, so a new session can use what an earlier one learned.
What does my own key include, and what does it cost?
It is free. A key created here allows 200 writes and 500 searches and lasts 7 days. Claim it with your email to keep it: the same key keeps working, and your account moves to the free plan with 10,000 writes and 1,000 searches a month.
Will what I save here be in my account?
Yes, once you create a key. The facts you already saved are copied into your new account, and from then on every step saves there directly. Keep the key with your email and sign in: your memories are in Memory Explorer, and each call the key made is in Request Logs.
Playground
Put it in your own agent
The playground uses two endpoints: one to store and one to search. The quickstart walks through both with your own key, and the free tier needs no credit card.
Start free. No credit card required.
