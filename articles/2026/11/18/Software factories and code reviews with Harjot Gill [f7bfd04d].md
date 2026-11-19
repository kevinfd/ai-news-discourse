---
id: "f7bfd04d60285012"
title: "Software factories and code reviews with Harjot Gill"
url: "https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews"
link: "https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews"
source: "The Pragmatic Engineer"
domain: "newsletter.pragmaticengineer.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-18T18:08:52Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Gergely Orosz"]
language: "en"
summary: "Listen and watch now on YouTube , Apple , and Spotify . See the episode transcript at the top of this page, and timestamps for the episode at the bottom. Brought to You by • turbopuffer – a ridiculously scalable, fast and cheap hybrid search engine, built on top of object storage, used by cutting-edge companies like Anthropic, Linear, Ramp and many others. Many companies that switch to…"
tags: []
orgs: ["Anthropic", "Google", "Apple", "OpenAI", "Microsoft"]
topics: ["agents & coding", "search & media", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 2256
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Software factories and code reviews with Harjot Gill

The Pragmatic Engineer · Gergely Orosz · 2026-11-18

Listen and watch now on YouTube, Apple, and Spotify. See the episode transcript at the top of this page, and timestamps for the episode at the bottom.
Brought to You by
• turbopuffer – a ridiculously scalable, fast and cheap hybrid search engine, built on top of object storage, used by cutting-edge companies like Anthropic, Linear, Ramp and many others. Many companies that switch to turbopuffer are cutting their search bills by 50% or more and getting much faster results. Check it out.
• Entire – Entire launched its own Git forge, shipped Continuous Memory, and reinvented the pull request (called Trails). Trails are a much more natural workflow when agents keep pushing new changes, after iterating on feedback – and you have more context and control on when a change is ready to merge. Check it out
• WorkOS – WorkOS built Airlock, the authorization layer for AI agents. It evaluates every request against the agent’s intent + your rules, and either allows it, denies it, or routes it to a human. Works with Claude Code, Codex & MCP gateways. Learn more
In this episode
In this conversation, we step into the world of an AI-pilled CEO to explore how their startup works. This episode might as well be a way of succeeding that contradicts the growing convention that AI spending costs are too high and must be clamped down on.
Harjot Gill is founder and CEO of CodeRabbit, an AI code review business, and he shipped over 5,000 pull requests last month, spending on AI at a monthly run rate of $250,000(!) It’s certainly not a conventional approach and Harjot gets into detail about the thinking and reasoning behind it.
In this episode of The Pragmatic Engineer Podcast, we talk about his background in building software and founding infra startups for the last 30 years, and how things changed into the era of building software factories at CodeRabbit. We talk about why he believes human code review is dead, and how his team maintains quality while shipping at unprecedented speed.
We also get into the rising costs of AI development, why Harjot is convinced that tech startups need more funding than ever, and how AI is changing recruitment and the skills for success.
Takeaways from the conversation with Harjot
1. Janitorial work formed a large part of his 5,000 PRs last month, pushed with agents. He sets off his agents to improve systems like the CI, fixing flaky tests, and refining caching. A lot of the PRs are generated during his commute, and at evenings and nights. In a few cases, he steers agents to make the UI feel better. Examples of stuff Harjot has built:
- A write-ahead log (WAL) on top of object stores using Rust (the agent ran for six weeks!). This WAL is now in production.
- Migrating all of CodeRabbit’s services over to Bun – running over a weekend
- A new CI system after the previous one had performance issues
2. CodeRabbit spends millions of dollars per month on AI, with a team of 40 engineers. Harjot estimates that a PR costs him around $150 in a personal spend of around $250-$275K per month. He compares it to marketing teams with 10 marketers at VC-funded companies who can drive $100M in spend. I point out that his startup is an outlier; the AI spend I hear about elsewhere is in the region of between $200-$2,000 per month, per dev. Finding out how this spend makes sense was one reason I was keen to meet Harjot.
3. For dev tooling startups like CodeRabbit, massive AI spend can be justified by launching new, AI-related products faster. It feels to me that CodeRabbit is not a typical company: its AI spending is a form of R&D if it creates new solutions that can be commercialized and sold. It’s not the same at places with fixed customer bases willing to pay a certain amount for an existing product, and no more.
Also, Harjot says that they got quoted $13M/year for a CI solution to handle their PR output, but the price made him decide they’d build their own CI system using agents. It took a week, and the new CI cost 50% less than the quote, with similar performance.
4. In 2021, Harjot believed AI would write most of the code. When working at FluxNinja, Harjot found that code review was already becoming a bottleneck, with GitHub Copilot’s autocompletions somewhat speeding up writing code. He misjudged the potential market size, assuming only larger companies that bought code verification solutions like Snyk and SonarSource, would buy AI-code review tools – instead, it’s pretty much everybody!
5. Harjot believes agents need to be “hill climbing”; they need to have ways to verify their own work
These are the layers that he believes are necessary, including ones he and the team use:
- Formal models like TLA+ and Lean. For one of their products, the engineering team utilized TLA+, and found race conditions that the code review overlooked. More recently, Harjot is experimenting with another formal method, Lean.
- Local deterministic simulations. One of the infra pieces built at Harjot’s startup is a simulation harness to fuzz different interleavings (concurrent operations).
- Emulating real APIs. Harjot mocks up and emulates APIs like Google Cloud APIs as part of testing.
- Dev environments. Agents can spin up services in environments like Google Cloud and Vercel, and confirm they work correctly on development deployments
- Production: staged rollouts. Harjot believes in releasing features with feature flags, and doing progressive rollouts. He said they often have an agent observe the performance characteristics of the rollout, check the logs, and continue the wider rollout when things are stable. This last part reminds me of OpenAI’s Perf Factory inside its software factory.
6. Human code review is dead, long live the human review! Harjot thinks that we will stop reviewing code generated by agents. Instead, we’ll spend more time reviewing the planning and final asset. Inside of CodeRabbit, engineers are reviewing releases (multiple PRs), not individual PRs.
7. Engineers can be banned from committing without human review. The company has a “review exempt list” of devs who can push to production without anyone reviewing their releases. When an outage happens, the team traces the PR that broke prod, and the dev who pushed it gets a ‘strike.’ Rack up enough strikes and releases have to be reviewed by colleagues. I personally like this idea of giving trust to devs to push to prod, but pairing it with accountability: the trust gets revoked if you cause production to be unstable!
8. Fine-tuning models stopped being worthwhile. CodeRabbit used to invest in fine-tuning models used in AI review, but Harjot says that new frontier models moving faster means that it would be tough to maintain their own fine-tuned ones, so it’s not worth it.
9. There are “war rooms”. To get important stuff done, engineers, product folks, and designers gather in the room and steer the agents as together they build a prototype, then a working product. This approach reminds me of Uber in 2016, except ‘war room’ efforts took 2-3 weeks, people flew in from different offices, and it meant aligning on the plan and putting a rudimentary prototype together. The teams finished the remaining work over a matter of months.
10. What Harjot looks for when hiring engineers: agency, breadth of experience, and systems thinking. He posted an unconventional job ad, only inviting candidates who had shipped 1,000+, non-slop PRs in the past 30 days, or had played 500+ hours of strategy and management games like Civilization, Age of Empires, Transport Tycoon, or Factorio. Harjot says he cannot unsee the similarities between running dozens of agents in parallel and playing a strategy video game involving tracking what dozens of units do.
Additional thoughts
This conversation gave me lots to think about. My kneejerk reaction was to question why anyone would spend so much on AI each month; I would assume it’s just wasteful. So, I’m delighted to learn more about where Harjot is coming from. I sense he is pushing the limit of what a single human developer can do when running hundreds of agents in parallel, and he still has more ideas than can be built. Plus, he doesn’t have to worry about his AI spending budget!
Could spending be much cheaper for the same usage? Harjot and CodeRabbit are paying frontier API costs, not using open models. We cover how profitable coding use cases are for inference vendors and frontier companies due to KV cache nuances in this week’s inference deepdive, and how the $200/month Max plans for individuals and small businesses offer usage closer to $8,000-14,000/month in API usage, due to the same KV cache profitability detail. Moving to open models could surely reduce a good part of this spend, but at the cost of some capability.
The engineer + strategy gamer combination helps push AI agent usage? Harjot is not some nontechnical “vibe coder”: he’s been coding for 30 years, and mostly used Neovim before moving over to AI agents. He’s long been obsessed with infra and distributed systems, and in his younger years, played Civilization. He detects parallels between the two activities and it’s interesting that he incorporated them into a job description.
The “Dracula effect” is real with AI agents. I often see the “Dracula effect” of AI agents draining people, like Steve Yegge mentioned in February. Harjot also reports disturbed sleep, like waking up at night to nudge his agents.
Well-funded AI-pilled startups could enjoy a massive upside of building with AI. Over the course of our conversation, I started to understand why it makes sense for Harjot and CodeRabbit to spend so much on AI. They need to build solutions that AI-native startups want to use, and CodeRabbit being AI-pilled itself confers the advantages of firsthand insights and empathy with customers. There’s much that can be learned from how Harjot and CodeRabbit work, all while this approach looks set to remain niche at a time when most companies are tightening the reins on AI spend.
CodeRabbit’s business is being an AI infra startup, and the time-to-market with new products is a massive differentiator. In that context, it makes sense for CodeRabbit to build a lot of software internally and then productionize some of it, contributing to their revenue and valuation possibly increasing down the road. I find it useful to learn about such approaches, even if you decide that this direction would not be feasible for yourself, your team, or company.
The Pragmatic Engineer deepdives relevant for this episode
• Inside OpenAI’s agentic software factory
• What is happening with code reviews?
• What’s the ROI of software engineers’ spending on AI?
• Why Ramp built its own in-house coding agent, Inspect
• AI SRE: what is it, how could it change on-call – and does it work?
• Context engineering with Dex Horthy
• Formal methods with Hillel Wayne
• Building Codex with Tibo Sottiaux
Timestamps
00:00 Intro
03:17 How Harjot shipped over 5,000 pull requests in a month
08:46 Harjot’s path into tech and his first startups
12:25 Early conviction around AI and founding CodeRabbit
14:40 Switching to AI coding
20:35 Software factories explained
25:37 What’s replacing human code review
38:44 Technical debt and deslopping tests
46:05 Evals
50:25 Formal methods
52:05 AI cost at CodeRabbit
54:57 Startup funding in 2026 and the value of AI spend
1:08:20 Hiring
1:13:03 Work pace, sleep, and burnout
1:21:55 Skills for the AI era
1:24:30 Book recommendation
References
Where to find Harjot Gill:
• X: https://x.com/harjotsgill
• LinkedIn: https://www.linkedin.com/in/harjotsgill
Book recommendation by Harjot The Black Swan by Nassim Nicholas Taleb: https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/
Mentions during the episode:
- Harjot’s post on his pull request stats and token spend:
- Harjot’s dotfiles: https://github.com/coderabbitai/dotfiles
- Tesla Full Self-Driving (Supervised): https://www.tesla.com/fsd
- AI tools for software engineers, but without the hype – with Simon Willison (co-creator of Django): https://newsletter.pragmaticengineer.com/p/ai-tools-for-software-engineers-simon-willison
- Alcatel-Lucent: https://en.wikipedia.org/wiki/Alcatel-Lucent
- University of Pennsylvania: https://www.upenn.edu
- When AI writes almost all code, what happens to software engineering?: https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what
- Git at any scale (Cursor’s post on Origin): https://cursor.com/blog/git-at-any-scale
- Write-ahead logging: https://en.wikipedia.org/wiki/Write-ahead_logging
- What is SOC 2 Compliance?: https://www.paloaltonetworks.com/cyberpedia/soc-2
- Jake Runzer’s post on the Railway incident:
- The Pulse: a new trend of CPU shortages: https://newsletter.pragmaticengineer.com/p/the-pulse-a-new-trend-of-cpu-shortages
- How Kubernetes is Built with Kat Cosgrove: https://newsletter.pragmaticengineer.com/p/how-kubernetes-is-built-with-kat
- Formal methods with Hillel Wayne: https://newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne
- Harjot’s post with CodeRabbit’s weekly commits chart:
- Harjot’s post on $8M+ seed rounds no longer being enough:
- Why Ramp built its own in-house coding agent, Inspect: https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect
- Spotify Confidence: https://confidence.spotify.com
- Harjot’s post on shipping 5K PRs in a week, with CodeRabbit’s hiring criteria: https://www.linkedin.com/posts/harjotsgill_we-at-coderabbit-shipped-5k-prs-last-week-share-7518364258942758912-Bts_/
- Why We Sleep by Matthew Walker: https://www.amazon.com/dp/1501144324
- Polyphasic sleep: https://en.wikipedia.org/wiki/Polyphasic_sleep
- Harjot’s post on burnout:
- Inside Fast’s rapid collapse: https://newsletter.pragmaticengineer.com/p/the-scoop-fast
Technology, tool and vendor mentions:
- CodeRabbit: https://www.coderabbit.ai
- Codex: https://chatgpt.com/codex
- Opus: https://www.anthropic.com/claude/opus
- Claude Code: https://claude.com/product/claude-code
- Neovim: https://neovim.io
- Netsil: https://www.linkedin.com/company/netsil
- New Relic: https://newrelic.com
- AppDynamics: https://en.wikipedia.org/wiki/AppDynamics
- eBPF: https://ebpf.io
- Nutanix: https://www.nutanix.com
- FluxNinja: https://www.fluxninja.com
- Tabnine: https://en.wikipedia.org/wiki/Tabnine
- GitHub Copilot: https://github.com/features/copilot
- LTX (SQLite replication file format): https://github.com/superfly/ltx
- Effect: https://effect.website
- XState: https://stately.ai/docs/xstate
- OrbStack: https://orbstack.dev
- Snyk: https://snyk.io
- SonarSource: https://www.sonarsource.com
- TLA+: https://lamport.azurewebsites.net/tla/tla.html
- Lean: https://lean-lang.org
- Sid Meier’s Civilization: https://civilization.2k.com
- Datadog: https://www.datadoghq.com
- Devin: https://devin.ai
- Bun: https://bun.com
- Rippling: https://www.rippling.com
- Age of Empires: https://www.ageofempires.com
- Transport Tycoon: https://www.transporttycoon.com
- Factorio: https://www.factorio.com
—
Production and marketing by Pen Name.
