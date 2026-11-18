---
id: "c7b3927bffdce82b"
title: "With macOS 27.3, Apple Warns Users Against Giving AI Agents Full Disk Access"
url: "https://pcmag.com/news/with-macos-273-apple-warns-users-against-giving-ai-agents-full-disk-access"
link: "https://pcmag.com/news/with-macos-273-apple-warns-users-against-giving-ai-agents-full-disk-access"
source: "PCMag"
domain: "pcmag.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T19:37:59Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Jibin Joseph"]
language: "en"
summary: "Apple is adding granular controls for app overrides and hard-drive access to ensure AI agents only have access to apps or folders deemed safe by users."
tags: []
orgs: ["Apple"]
topics: ["products & launches", "agents & coding", "safety & ethics"]
content_source: "fulltext"
word_count: 456
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# With macOS 27.3, Apple Warns Users Against Giving AI Agents Full Disk Access

PCMag · Jibin Joseph · 2026-11-17

After multiple AI agents went rogue earlier this year, Apple informed developers in October that it would soon introduce clearer warnings and stricter settings to help macOS users understand the risks associated with granting full-disk access to apps. Those guardrails have now appeared in macOS 27.3 beta 2.
Among the biggest changes is a split in the Device Control and Data Access API. While the earlier unified toggle could grant apps complete control over other apps for AI tasks, the latest macOS beta splits it into two controls: System & App Protection Override and Accessibility.
According to 9to5Mac, the Accessibility setting is designed to allow permissions for assistive tools to be managed through an entitlement process. The System & App Protection Override menu, meanwhile, lets you decide whether an app must seek your permission before it can control another app.
Within the System & App Protection Override menu, Apple will also encourage you to grant access to just specific apps instead of the whole system. Additionally, instead of granting the app unlimited access to another app, you can require it to request permission each time it needs access. When an app finally gains control over another through this setting, you’ll also see a transparency indicator somewhere on your screen, Apple says.
Similar granular controls are also being made available for the Full Disk Access setting. When backup apps, disk cleaners, file indexers, or security apps ask for complete hard-drive access, you can now choose the exact folders it can access.
While the new changes don’t remove an app’s ability to gain control over other apps or access the entire disk, they alert users to the risks associated with system-wide access. “Before granting an app such extraordinary access, users should understand that it puts all of the data on their Mac at risk. These changes are designed to help them do that and to empower them to make informed decisions about their own data and privacy,” Apple says in a developer blog post.
Permissions granted before the change will remain as is, but developers should be prepared to handle the new protections, Apple added, noting that apps should “gracefully handle having access to only a limited set of folders or apps when utilizing these APIs.”
The changes arrive after Mac computers, especially the mini and the Studio, became popular for running AI models locally. Apple was short on supply earlier this year, and former CEO Tim Cook said in May that the company was surprised by the unexpected demand.
About Our Expert
Jibin is a tech news writer based out of Ahmedabad, India. Previously, he served as the editor of iGeeksBlog and is a self-proclaimed tech enthusiast who loves breaking down complex information for a broader audience.
