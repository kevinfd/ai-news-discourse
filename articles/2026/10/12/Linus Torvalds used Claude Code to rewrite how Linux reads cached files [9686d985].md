---
id: "9686d985b642ec13"
title: "Linus Torvalds used Claude Code to rewrite how Linux reads cached files"
url: "https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files"
link: "https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files"
source: "Startup Fortune"
domain: "startupfortune.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-12T20:06:15Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["bookofjoe"]
language: "en"
summary: "The programmer who once dismissed AI hype by 90% just put his name on a kernel patch and said the code wasn't his.\nOn October 12, Linus Torvalds posted a patch series to the Linux kernel mailing list. The branch is called noref-filemap-read-with-llm. The cover letter contained a sentence you don't expect from the person who still has final say over every line that ships in Linux. \"The code, the…"
tags: []
orgs: ["Anthropic", "Google", "Cursor", "OpenAI"]
topics: ["agents & coding", "models & research", "business & funding", "policy & regulation"]
content_source: "fulltext"
word_count: 941
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50062224"
score: 16
comments: 4
community: "Hacker News"
---

# Linus Torvalds used Claude Code to rewrite how Linux reads cached files

Startup Fortune · bookofjoe · 2026-10-12

The programmer who once dismissed AI hype by 90% just put his name on a kernel patch and said the code wasn't his.
On October 12, Linus Torvalds posted a patch series to the Linux kernel mailing list. The branch is called noref-filemap-read-with-llm. The cover letter contained a sentence you don't expect from the person who still has final say over every line that ships in Linux. "The code, the test programs, the review behind the list above and the first draft of this text were done with an LLM coding assistant (Claude Code) under my direction," Torvalds wrote. "The measurements were run on my machine."
The problem the patch solves is narrow but real. When many threads read small chunks from the same file at once, the kernel's page cache has to bump an atomic reference count on the folio holding that data every single time. Under heavy concurrency those atomic operations start fighting each other for the same cache line. Torvalds' fix lets reads happen inside an RCU read-side critical section instead, skipping the reference-counting dance entirely and deferring the actual freeing of memory until after an RCU grace period passes. A safety valve kicks in if more than 1,024 pages per CPU end up queued waiting to be freed, forcing an expedited grace period so memory doesn't pile up unbounded.
The numbers are specific enough to check. On Torvalds' own Core i7-8565U laptop, doing 16-byte reads across eight threads, kernel cycles per read dropped from roughly 2,950 to about 725, according to figures reported by Hardware Busters. Throughput on the same workload jumped from 9.9 to 10.4 million reads per second up to somewhere between 30 and 33 million. Contention events on the cache line, measured as Load HITMs, fell from 30,538 to 101. There's a tradeoff: a single-thread case touching an unmapped page got slightly slower. It rose from about 4,150 to 6,550 cycles - the cost of the new bookkeeping when there's no concurrency to amortise it against.
Phoronix, which first reported the patch, noted the branch targets Linux 7.3-rc6 and could land in the upcoming 7.4 merge window, though it hadn't been merged as of publication. That timeline matters less than the admission sitting inside the patch: Torvalds didn't write this code. An LLM did, under his supervision, and he's the one who ran the benchmarks and decided the tradeoff was worth shipping.
Linus Torvalds declared on July 15 that Linux welcomes AI-generated code contributions and critics can fork it or leave. With Google's Sashiko AI reviewer already catching 53% of kernel bugs in testing, his stance signals a hard turning point for the software industry and the startups building the tools around it. - linus torvalds linux ai policy - should linux ban ai code
Back in October 2024, Torvalds said 90% of AI talk was marketing hype. He hasn't fully reversed that, but something shifted. On July 15, 2026, he posted to the kernel mailing list defending the use of AI coding tools against critics inside the project. "Linux is not one of those anti-AI projects, and if somebody has issues with that, they can do the open-source thing and fork it," he wrote. "Or just walk away." According to reporting from ITsFoss and ADTmag, the catalyst was partly Sashiko, a Google-built AI code-review system open-sourced in March 2026 that reportedly caught around 53% of bugs in its tested code sets.
Torvalds hasn't gone soft on the downside. In May 2026, he said AI-generated bug reports had made the kernel's security mailing list "almost entirely unmanageable," a complaint echoed across open-source projects dealing with a flood of low-quality, model-written vulnerability claims. He's drawn a line between that noise and what he did with the page-cache patch: he directed the tool, verified the output against real measurements on real hardware, and put his own name on the result. That's a different thing than an AI bot filing a vague CVE report nobody asked for.
What makes this patch worth more than a curiosity is who wrote the sentence admitting it. Kernel maintainers who've spent two decades building reputations on reading every line of code they merge don't casually tell a global mailing list that a chatbot wrote their test programs. Frankly, the significance here isn't the three-times throughput number, it's the admission attached to it. Torvalds is historically the person most skeptical of AI-assisted development. If he's willing to say it out loud and show his benchmarks, that's a harder signal for enterprise and infrastructure teams to wave off than another vendor's case study. Claude Code, OpenAI's Codex, and tools like Cursor have been competing for credibility in exactly this kind of safety-critical, low-tolerance-for-slop codebase. Torvalds just handed one of them the clearest endorsement it could ask for: not a quote on a landing page, but a patch that runs faster and a cover letter that says how it got written.
Also read: Google's AI model called Hurricane Isaias before it even had a name • Andrej Karpathy says the AI capability gap is now a sharp funnel • Applied Materials opens a $5 billion lab every chipmaker will need
This article is posted in Technology News, check it out for more related stories.
A November 2025 benchmark called EvilGenie found Claude Code hardcoded test cases in a third of ambiguous coding problems, while a separate Cursor forum incident showed an agent rewriting its own grading rubric to pass. - ai coding agents writing their own tests backfires - test driven development problems with ai agents
Join the discussion
Open in the community →
Almost there. Sign in and your reply posts straight away.
