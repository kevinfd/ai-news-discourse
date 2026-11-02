---
id: "b3a231f57ed14555"
title: "Non-developer building a two-sided B2B2C app with Claude Code – what should I watch out for, especially security?"
url: "https://reddit.com/r/ClaudeAI/comments/1xlsng3/nondeveloper_building_a_twosided_b2b2c_app_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xlsng3/nondeveloper_building_a_twosided_b2b2c_app_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T09:24:47Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["New-Jackfruit-1956"]
language: "en"
summary: "Body: I'm planning to build an app with Claude Code and sell licenses to individual organizations. I'm not a professional developer, so I'd like to learn from people who have done something similar before I start. The setup: Two user types: organizations (the paying customers) post offers, and private individuals browse them and sign up / claim them Role-based access: one account can have…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Apple", "EU"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 303
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlsng3/nondeveloper_building_a_twosided_b2b2c_app_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Non-developer building a two-sided B2B2C app with Claude Code – what should I watch out for, especially security?

Reddit · New-Jackfruit-1956 · 2026-11-02

Body: I'm planning to build an app with Claude Code and sell licenses to individual organizations. I'm not a professional developer, so I'd like to learn from people who have done something similar before I start. The setup: Two user types: organizations (the paying customers) post offers, and private individuals browse them and sign up / claim them Role-based access: one account can have several roles (e.g. someone can create offers and take part as a regular user) Users check in on-site (location + photo) to confirm they took part Prototype: a web app first, to validate the idea with a pilot customer Later: native apps on the App Store and Play Store Based in the EU, so GDPR applies, and customers will expect EU hosting My questions: Architecture: What stack would you choose so the web prototype can turn into native apps later without a full rewrite? (React Native/Expo, Flutter, PWA first, …?) Auth & roles: Build it myself or use a provider (Supabase, Firebase, Clerk, Auth0)? How do you set up role-based permissions so Claude doesn't introduce access-control holes? Multi-tenancy: Each organization should only see and manage its own data. What's the safest pattern for that (e.g. row-level security)? Security with AI-written code: What's your process? I'm planning AI code review, automated scanners and a one-time external pentest before launch. Is that enough? What do people usually miss? Privacy: Location data and photos from private users: how do you store them in a GDPR-compliant way, and when do you delete them? Workflow with Claude Code: Any tips on structuring the project (CLAUDE.md, tests, small PRs) so it stays maintainable once it gets bigger? App stores: Any pitfalls with Apple/Google review for apps that have business accounts plus consumer accounts? Thanks in advance. Pointers to repos, templates or post-mortems are very welcome.
