---
id: "b0c19766cafbc908"
title: "When non-dev colleagues build internal apps with Claude Code, where do you host them?"
url: "https://reddit.com/r/ClaudeAI/comments/1xci77z/when_nondev_colleagues_build_internal_apps_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xci77z/when_nondev_colleagues_build_internal_apps_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T13:12:22Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Marmelab"]
language: "en"
summary: "This keeps coming up at work and I’m curious how other companies handle it. Some of my colleagues aren’t developers, but they build internal apps with Claude Code. Once an app works on their laptop, the questions are always the same. Where does it live, who can log in, where’s the data, and does IT even know it exists? It’s a bit like Excel files going around by email, except now it’s apps, and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 368
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xci77z/when_nondev_colleagues_build_internal_apps_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# When non-dev colleagues build internal apps with Claude Code, where do you host them?

Reddit · Marmelab · 2026-10-22

This keeps coming up at work and I’m curious how other companies handle it. Some of my colleagues aren’t developers, but they build internal apps with Claude Code. Once an app works on their laptop, the questions are always the same. Where does it live, who can log in, where’s the data, and does IT even know it exists? It’s a bit like Excel files going around by email, except now it’s apps, and the data can end up hosted outside the company. So I looked at AI platforms, meaning platforms that host apps built by AI. The needs seem roughly the same everywhere: a backend per app with company SSO, frontend hosting, deploying straight from the tool that built the app, an inventory for IT with a way to stop apps, a low cost per app, and control over where the data lives. I compared two dozen options in four families, and none of them ticks every box. → SaaS builders like Lovable, Bolt or Replit are the fastest path for non-developers. The downside is that none of them runs on your own infrastructure, and apps built elsewhere (like with Claude Code for example) have no way in. → Vendor platforms (Microsoft, ServiceNow, Databricks, Snowflake and others) are the strongest on IT control. There’s a catch though, they tie you to the vendor’s platform and licenses, and except for Retool, you can’t self-host them. → Open-source backends give you back control over the data, but only three of them (Nubase, PocketBase with PocketHost, Appwrite) host dozens of apps on one server out of the box, each with a trade-off. Supabase is the one most AI tools already know, but self-hosted it needs a full stack per project and doesn’t host frontends. → Building your own is the only option that checks every box. A first version can take one developer about two weeks with Claude Code. The main risk is running it, since the company becomes its own vendor for every upgrade, security patch and backup restore. The market is moving fast too, most of these offers launched or changed in 2026. So where do vibe-coded apps live in your company, and does IT know about them?
