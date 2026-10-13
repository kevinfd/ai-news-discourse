---
id: "759bb825983a3660"
title: "Linus Torvalds is using AI to develop Linux kernel code now"
url: "https://zdnet.com/innovation/linus-torvalds-uses-ai-to-write-linux-kernel-patch"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T17:30:46Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Steven Vaughan-Nichols"]
language: "en"
summary: "The move is a turning point in the developer’s relationship with AI and Linux."
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "Intel"]
topics: ["agents & coding", "products & launches", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 1058
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/Screenshot-2026-10-13-at-1.27.55-PM.png"
discussion_url: null
score: null
comments: null
community: null
---

# Linus Torvalds is using AI to develop Linux kernel code now

ZDNet · Steven Vaughan-Nichols · 2026-10-13

ZDNET’s key takeaways
- Torvalds just released a set of patches, which were largely written with Anthropic’s Claude Code.
- These new patches address an unsolved memory cache slowdown problem when using multiple cores and processors.
- Linus Torvalds had been moving closer to favoring AI, and this was the final step toward embracing it for Linux development.
It had to happen. Linus Torvalds announced to the world that he used AI to write code for the Linux kernel. Who’d thought it? Well, me for one. Over the last few years, I’ve seen Torvalds’ attitude change from skeptical to seeing AI as a useful tool for programmers and maintainers.
In his Git submission, he wrote, “The code, the test programs, the review behind the list above and the first draft of this text were done with an LLM coding assistant (Claude Code) under my direction.”
Also: ‘I use AI to do the things that I’m bad at’: Linus Torvalds on why it works for him
More from ZDNET
Tackling a shared-memory bottleneck
Specifically, the fix addresses contention in Linux’s page cache, which holds file data in memory. When several threads repeatedly read small amounts of data from the same cached file, they take and release references to the folio backing that data. Those reference-count updates require atomic writes to a shared cache line. This in turn forces processor cores to compete over it.
Doesn’t sound like that big a problem, does it? Wrong. In some workloads, it can really slow things down. Torvalds found that when eight threads issued 16-byte pread() calls against the same page on a four-core, eight-thread Intel Core i7-8565U laptop, the shared cache line accounted for 99.92% of the measured cross-core load, according to Hit in Modified cache line (HITMs). That slows work down considerably.
This isn’t just Linus scratching a personal itch. It’s been a known issue since 2024. Earlier attempts to fix it, though, have come to naught.
Torvalds and Claude Code’s proposed patches change when the kernel can reuse memory removed from the page cache. Rather than returning that memory to the allocator immediately, the patches defer reuse until a read-copy-update (RCU) grace period has elapsed. That lets a reader protected by an RCU read-side section copy data directly into a user buffer without taking a folio reference.
Also: Someone made a free Photoshop clone – so I had to try it on Linux
This approach trades immediate memory reclamation for a read path that avoids repeatedly updating a shared reference counter. The reported performance gains are substantial within that specific test. Eight-thread throughput rose from approximately 9.9–10.4 million reads per second to 30–33 million, while kernel cycles per read fell from roughly 2,950 to 725. Single-thread reads improved more modestly, from about 452–454 cycles to 408–409 cycles per read. Torvalds added in his pull request (PR) that “A machine with more CPUs, or more than one socket, should gain more; nothing bigger has been measured.”
This doesn’t mean Linux as a whole runs three times faster. Hardly! Instead, this describes experimental results from a particular small-read workload on Torvald’s personal laptop, which he had with him in Prague at Linux Plumbers.
Faster reads, unfinished memory management
That’s not to say Torvalds and Claude Code have fixed this issue. We’re far from being able to say that. The performance gains come with engineering trade-offs. Delaying memory reuse means pages can remain unavailable while the kernel waits for an RCU grace period. In his Git submission, Torvalds described that reclamation issue as “the part of this series that is least solved.”
Also: I’ve used Ubuntu for 22 years – and 26.10 might be its best release yet
There is also a regression when a read targets a user page that is not yet mapped. The new path incurs an additional failed exception before falling back to the existing implementation. As of Oct. 13th, the branch remained outside the mainline Linux 7.3-rc6. Whether it will ever be merged, and on what timetable, remains up in the air.
From AI skepticism to hands-on use
Torvalds’s decision to use Claude Code reflects a long-term evolution in his attitude toward AI. This hasn’t been a simple reversal from opposition to support.
In December 2023, he described AI as a potential aid to developers, saying, “I see AI as a tool that can help us be better at what we do.” At the time, his interest in AI was around how it could help identify bugs, rather than writing code. No one was giving serious thought to using AI to write serious programs (hard to believe now).
By late 2025, Torvalds was calling himself “a huge believer in AI as a tool, and saying he was more interested not just in finding bugs, but in maintaining code and reviewing patches. Generating new, serious code for Linux was still largely off the table. Still, in January 2026, he began toying with AI-assisted coding for a Python audio visualizer in a hobby project.
Also: 75% of developers I surveyed prefer Claude Code – here’s why they choose it over Codex
His latest remarks, reported Oct. 9 following a conversation with Dirk Hohndel at Open Source Summit Europe in Prague, were more enthusiastic.
“I used to think it was just not very good — but now I’m at the point where I actually really like using AI,” Torvalds said. “I think AI is a wonderful tool if you use it correctly and treat it as a tool, and I find it makes programming much more enjoyable.”
Even so, he cautioned, “I think that you need to be very careful using AI when you’re doing something real and important.” It doesn’t get much less real and important than Linux.
The page-cache experiment puts both sides of his position on display. Claude Code helped produce kernel code, tests, and review materials. The resulting branch shows promising benchmark gains, but also the unresolved memory-reclamation questions and performance regression that must be addressed before the experiment can become production kernel code.
Still, we’ve reached a turning point. Torvalds, arguably the world’s foremost developer and maintainer, is now using AI to develop new Linux kernel code. This would have been unthinkable even a year ago, and even now some people still struggle to imagine AI adding new code to Linux or any other important program.
