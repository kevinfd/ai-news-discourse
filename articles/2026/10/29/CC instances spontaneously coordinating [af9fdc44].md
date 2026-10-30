---
id: "af9fdc4442decf54"
title: "CC instances spontaneously coordinating"
url: "https://reddit.com/r/ClaudeAI/comments/1xis94h/cc_instances_spontaneously_coordinating"
link: "https://reddit.com/r/ClaudeAI/comments/1xis94h/cc_instances_spontaneously_coordinating"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T18:36:38Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["mrothro"]
language: "en"
summary: "I just discovered that Claude Code instances running in completely different directories on my machine automatically discover each other and coordinate. I'm not sure when this was introduced, but it was quite surprising to me. I'm going to have to think through the implications. The full story: I run several simultaneous CC sessions across different work and personal projects. My machine is…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 228
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xis94h/cc_instances_spontaneously_coordinating/"
score: null
comments: null
community: "r/ClaudeAI"
---

# CC instances spontaneously coordinating

Reddit · mrothro · 2026-10-29

I just discovered that Claude Code instances running in completely different directories on my machine automatically discover each other and coordinate. I'm not sure when this was introduced, but it was quite surprising to me. I'm going to have to think through the implications. The full story: I run several simultaneous CC sessions across different work and personal projects. My machine is often saturated, and as I was watching a session work, it suddenly said it was negotiating with another operator for CPU. What? Who now? At first I thought they found the PIDs of other instances, but after some conversation Claude told me it actually has a built-in tool to list and message the others. They refer to themselves based on the working directory where I started CC, adding a numbered suffix if I have multiple in the same dir. In this case, the outcome was great: they are working together to optimize the use of my overworked CPU. Definitely something I want. At the same time, I had been assuming everything was isolated. No longer true. FWIW I also run sessions as different users on my Mac, and it confirms it cannot see the sessions from the other users, so that seems like a good boundary if you want isolation. I figured I'd share, since this was quite the surprise for me. Thought people should know.
