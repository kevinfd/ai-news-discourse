---
id: "9ab7d04e0f6289d3"
title: "I built a tiny helper that lives in my MacBook notch, works along with Claude Code and jumps for joy when it's done"
url: "https://reddit.com/r/ClaudeAI/comments/1xpxe0l/i_built_a_tiny_helper_that_lives_in_my_macbook"
link: "https://reddit.com/r/ClaudeAI/comments/1xpxe0l/i_built_a_tiny_helper_that_lives_in_my_macbook"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T04:25:46Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Nkgsporty"]
language: "en"
summary: "I built Nosy Notch, a free and open-source macOS app, almost entirely with Claude Code. It's free to try, no paid tier. What it does Claude Code often works on its own for minutes, then waits for a \"yes\" I never saw. Nosy Notch shows every Claude Code session in the MacBook notch, with a small helper called Nosy living in it: - While Claude works, the notch shows the tool it's running and Nosy…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple", "Cursor"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 443
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpxe0l/i_built_a_tiny_helper_that_lives_in_my_macbook/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a tiny helper that lives in my MacBook notch, works along with Claude Code and jumps for joy when it's done

Reddit · Nkgsporty · 2026-11-07

I built Nosy Notch, a free and open-source macOS app, almost entirely with Claude Code. It's free to try, no paid tier. What it does Claude Code often works on its own for minutes, then waits for a "yes" I never saw. Nosy Notch shows every Claude Code session in the MacBook notch, with a small helper called Nosy living in it: - While Claude works, the notch shows the tool it's running and Nosy concentrates. When the context compacts, he gets dizzy. - When Claude asks for permission, Nosy waves and the notch shows Deny / Always allow / Allow. Claude's own dialog stays open too. - When a turn is done, he drips out of the notch and jumps for joy, with the first lines of the answer. You can read the conversation and reply right from the notch. - Hover for all sessions, context fill and your 5-hour / weekly limits. When nothing runs, he falls asleep in the notch. - Finished tasks give him energy, levels and a streak. He never dies and never guilt-trips you. - Also: music player, file shelf with AirDrop, calendar heads-ups, battery and AirPods status, focus timer. Works with Codex and Cursor too. How Claude Code helped Claude Code wrote the Swift/SwiftUI app, the local hook server, the npx installer and the website. My part was the idea, the character design and testing on my Mac. Some things it did on its own: - It read the hooks docs, then ran real Claude Code sessions with a test PermissionRequest hook. That's how it found out Claude's dialog stays open while the hook waits, which is what makes approving from the notch possible. It also saw that one "always allow" suggestion switches the session mode, so it filters that out. - When the app froze on launch, it profiled the process with sample and found an Apple Events permission check blocking the main thread. - For Nosy, it drew several rounds of sketches in the chat until we had the character, then built the "jumps into the notch like a tar puddle" animation in SwiftUI. - It built a recorder that renders the animations frame by frame on a virtual clock, which made the clips in this post. - A security pass it ran found that a website could post to the local server, so the server now rejects browser requests. Try it (free) macOS 14+ and Node: npx nosynotch installs the app, connects the hooks and starts it. npx nosynotch uninstall removes everything. Everything stays on your Mac, MIT licensed. Website: https://nosynotch.davidkubus.dev GitHub: https://github.com/ddkbs/nosynotch Feel free to try it out and leave your feedback!
