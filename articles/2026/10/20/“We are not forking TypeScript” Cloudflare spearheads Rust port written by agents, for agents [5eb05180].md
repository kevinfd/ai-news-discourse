---
id: "5eb0518058f5d81b"
title: "“We are not forking TypeScript”: Cloudflare spearheads Rust port written by agents, for agents"
url: "https://thenewstack.io/cloudflare-rust-typescript-tsrs"
link: "https://thenewstack.io/cloudflare-rust-typescript-tsrs"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T21:36:25Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Cloudflare is going all-out to ensure that AI coding agents can check their work without exhausting available computing resources, leading a new effort to bring Microsoft’s TypeScript compiler to Rust. \n\n But whatever you do, don’t call it a fork. \n\n Taking to X, Cloudflare’s director of engineering Christoph Nakazawa confirmed that the company is taking ownership of tsrs , a Rust port of…"
tags: ["AI", "AI Agents", "Rust", "TypeScript"]
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 1166
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “We are not forking TypeScript”: Cloudflare spearheads Rust port written by agents, for agents

The New Stack · Paul Sawers · 2026-10-20

“We are not forking TypeScript”: Cloudflare spearheads Rust port written by agents, for agents
Cloudflare is going all-out to ensure that AI coding agents can check their work without exhausting available computing resources, leading a new effort to bring Microsoft’s TypeScript compiler to Rust.
But whatever you do, don’t call it a fork.
Taking to X, Cloudflare’s director of engineering Christoph Nakazawa confirmed that the company is taking ownership of tsrs, a Rust port of TypeScript that it claims is up to eight times faster, and uses 70% less memory than TypeScript 7.0.
Microsoft’s own TypeScript compiler is reaping the benefits, too, with the teams sharing optimizations as they work to keep the two implementations in sync.
“We are not forking TypeScript — we are working with the TypeScript team and as a result 7.1 is already ~2.5x faster, too,” Nakazawa writes.
That “port vs fork” message runs throughout the accompanying blog post, co-authored by Nakazawa and fellow Cloudflare engineers Boshen Chen and Dimitri Mitropoulos, who go to great lengths to explain that they very much see TypeScript as Microsoft’s to continue steering.
“To be clear, we are not forking TypeScript. We believe the TypeScript team should remain in full control of the language’s design and direction.”
“To be clear, we are not forking TypeScript,” they write. “We believe the TypeScript team should remain in full control of the language’s design and direction. They have maintained a long-term vision while guiding TypeScript’s adoption across the JavaScript community. We do not want to change that.”
Why Rust, when Microsoft already has Go?
Developed and released by Microsoft back in 2012, TypeScript extends JavaScript with a type system that helps developers catch errors before their applications run. However, checking those types can consume considerable computing resources, particularly in large projects where multiple AI agents may be writing and validating code simultaneously.
Microsoft addressed some of those performance problems in July with TypeScript 7.0, replacing its JavaScript-based compiler with one written in Go and delivering roughly tenfold speed improvements.
As The New Stack previously reported, Microsoft had considered Rust for the rewrite, but concluded that reproducing TypeScript’s existing architecture in Rust would introduce significant complications around memory management and compatibility.
The performance gains reported for tsrs make for an interesting comparison with Microsoft’s own Go implementation. Commenting in a Hacker News discussion about the Rust port, Daniel Rosenwasser, Microsoft’s principal product manager for TypeScript, notes that “a lot of the speed does not just come down to language choice,” adding that “some of what is going to make TS 7.1 faster and leaner… actually comes from optimizations discovered in tsrs.”
“Some of what is going to make TS 7.1 faster and leaner… actually comes from optimizations discovered in tsrs.”
Separately, Rosenwasser announced TypeScript 7.1 beta earlier today, detailing substantial speed and memory optimizations.
Cloudflare, for its part, sees another opportunity in Rust, particularly its compatibility with WebAssembly (Wasm). Go can compile to Wasm, but it has to bring its garbage collector along. Rust offers more direct control over memory, reducing the overhead of running development tools in resource-constrained environments. For Cloudflare, that could make it easier to run complete development environments inside browsers and isolated Workers sandboxes, where AI agents can write, check, and build applications.
The move also fits into Cloudflare’s growing JavaScript ecosystem. As The New Stack reported last week, the company has been assembling an extensive collection of JavaScript tools and expertise, including through its acquisition of VoidZero in June and the recent release of Void, an open-source platform for deploying and managing AI-built applications.
With that in mind, it’s the Cloudflare and VoidZero teams who are are now developing tsrs as part of Oxc, VoidZero’s Rust-based JavaScript toolchain, with plans to integrate it into other developer tools.
Owner and operator: A tsrs origin story
It’s worth noting that the tsrs project began just last month at restaurant software company Owner.com, where head of AI developer experience Max Schwenk says he faced a 37,000-file TypeScript backend. Writing in a blog post published on Monday, he notes that Microsoft’s Go compiler consumed 19 GiB of memory and took 80 seconds for a single-threaded check, restricting how many coding agents could work concurrently.
With multiple agents generating code simultaneously, the resource demands made it difficult for each to check its changes independently, forcing Owner.com to experiment with cloud-based development environments and other compromises.
“For a coding agent to be maximally productive, it needs to be able to validate its work in the tightest possible loop,” Schwenk writes.
After running into limits while trying to improve the Go compiler’s memory usage, Schwenk tried something somewhat more ambitious: use Anthropic’s Claude Opus 5.5 to recreate the compiler in Rust. He would direct the experiment and evaluate the results, leaving the implementation entirely to AI agents.
“I wrote zero code,” Schwenk writes. “Not ‘barely any’. Zero.”
“I wrote zero code. Not ‘barely any’. Zero.”
And the results came remarkably quickly. Schwenk says he deployed more than 20 AI subagents in parallel, waking the following morning to a functioning typechecker. Further optimizations brought Owner.com’s typechecking time down to roughly seven seconds in CI, and across more than a dozen public projects, Schwenk reports tsrs running 2.5 to five times faster than Microsoft’s newer Go compiler nightly, while using about a third as much memory.
Agentic rewrites in Rust
In truth, the tsrs project is just the latest example of AI agents being enlisted for substantial Rust migrations. As The New Stack reported last month, GitHub used its own Copilot agents to rewrite its coding-agent runtime in Rust, while Anthropic had previously used Claude agents to help migrate its Bun JavaScript runtime from Zig to Rust.
Elsewhere, Meta has also used AI to help port the React Compiler to Rust, while in September OpenAI revealed two engineers used Codex and GPT-5.5 to rebuild its Habitat storage service in Rust.
But such rapid, AI-assisted rewrites raise questions about how developers verify that the resulting software behaves as intended. For a TypeScript compiler, that means ensuring it catches the same errors as Microsoft’s implementation. Schwenk says the project uses TypeScript’s conformance tests, deliberately introduces errors into real projects and runs Miri, a tool for detecting memory-safety problems in Rust. Those checks have already uncovered a memory bug that appeared only in an optimized build.
“A faster compiler that finds fewer errors is a broken compiler with good marketing.”
“A faster compiler that finds fewer errors is a broken compiler with good marketing,” Schwenk writes.
Maintaining compatibility, it’s fair to say, will be an ongoing challenge. Cloudflare plans to borrow the AI-assisted approach behind Vinext, its Vite-based reimplementation of the Next.js web framework, where agents monitor Next.js for changes, run compatibility tests, and propose fixes when differences emerge. Some discrepancies remain in tsrs, including the order in which diagnostic messages are displayed.
“We will apply the same process to TypeScript, taking extreme care that we don’t introduce diverging behaviors from upstream TypeScript,” the Cloudflare authors write.
