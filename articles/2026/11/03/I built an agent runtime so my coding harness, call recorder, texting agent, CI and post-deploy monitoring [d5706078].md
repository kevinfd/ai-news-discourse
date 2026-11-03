---
id: "d5706078df2f0469"
title: "I built an agent runtime so my coding harness, call recorder, texting agent, CI and post-deploy monitoring are all one system that talks to itself. What I learned about harness design along the way."
url: "https://reddit.com/r/ClaudeAI/comments/1xmg0a1/i_built_an_agent_runtime_so_my_coding_harness"
link: "https://reddit.com/r/ClaudeAI/comments/1xmg0a1/i_built_an_agent_runtime_so_my_coding_harness"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T01:40:45Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["CaptainCrouton89"]
language: "en"
summary: "Obviously you can run Claude Code on the backend and hook up a VM to make it actually do things, but usually it's not in a safe environment, and even when it is, it's not easy to integrate with. A lot of tasks I want Claude Code doing also need a frontend, need to run in the cloud, and need to be wired into a bunch of APIs. I kept realizing, over and over and over again, \"God damn, it would be…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "Amazon"]
topics: ["agents & coding", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 691
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmg0a1/i_built_an_agent_runtime_so_my_coding_harness/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an agent runtime so my coding harness, call recorder, texting agent, CI and post-deploy monitoring are all one system that talks to itself. What I learned about harness design along the way.

Reddit · CaptainCrouton89 · 2026-11-03

Obviously you can run Claude Code on the backend and hook up a VM to make it actually do things, but usually it's not in a safe environment, and even when it is, it's not easy to integrate with. A lot of tasks I want Claude Code doing also need a frontend, need to run in the cloud, and need to be wired into a bunch of APIs. I kept realizing, over and over and over again, "God damn, it would be so nice if I could just use Claude Code on the backend for this application, because Claude Code has so many more capabilities." But I'd have to rewire everything, and it's just a fucking mess. You keep doing the same boilerplate over and over with minor deviations, mostly to control what permissions things have. So I built an agent runtime called crouter (on the pi harness, not a modified Claude Code) and an SDK on top of it, and now every app I write runs on it. The other thing was making it so the apps can integrate with each other properly. Rather than just having an MCP server, they integrate bidirectionally. What I mean by that is, in the same way an agent can call your backend, your backend can call an agent, and different backends can call each other. This is why I took a security-first approach, or governance-first approach I guess, to access between applications. You wire your runtime up to multiple apps, those apps ping each other with tasks and hit each other's endpoints as permitted by you, and the ecosystem grows and grows. The thought that got me here was basically: oh shit, if they all build on this SDK, on the same network, it's one giant graph of applications with edges between everything. I've been using it for internal tooling. I know everyone says this, but it has actually changed the way I do dev work. Our CI on GitHub is just an app baked into the system. PR reviews are an agent too, running on the reviewer's own runtime. I built a little texting app and gave it permission to use everything else, so I can kick off work from my phone. Also, other apps can piggyback off it and alert me of things using text. And because the texting app can talk to my laptop and the agent I use for coding there (just another app on the ecosystem lol), I can fire off dev work while taking a shit lmao. There's a call recorder that writes notes and action items from my meetings, and because it's a CLI like everything else, any agent on the runtime can search the transcripts when a task needs what was said on a call. I built an error-monitoring app that aggregates logs and issues from our AWS cluster, Cloudflare, vendor status pages, Sentry, and all the logging inside our applications. An agent reads it and only sends a report when there's actually an issue, and the text has a button that starts an agent working on it. Claude built most of it. The first version, in May, was a CLI I made with Claude Code for spawning Claude Code sessions into tmux panes. In June I moved the sessions onto the pi harness, and since then crouter has mostly been built on crouter. Opus does the design, planning and orchestration and hands pieces to Sonnet agents that write the code, all on the same runtime. I write the specs and approve the design changes. The repo has about 5,000 commits since May. The "How it works" page on the site shows the actual tree of agents that built that page, and one bigger run in October used 447 agents over 5 days and merged 115 PRs across 10 repos. It's free to try: npm install -g @north-light/cli , then run crtr . It runs on whatever model account you already have (Claude or ChatGPT subscription, or an API key). Site and docs are at code.northlight.ai, and the full trace of one run plus what I learned about the harness are in the first comment.
