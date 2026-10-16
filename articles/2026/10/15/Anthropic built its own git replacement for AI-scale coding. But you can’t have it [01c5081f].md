---
id: "01c5081f78187f5d"
title: "Anthropic built its own git replacement for AI-scale coding. But you can’t have it."
url: "https://thenewstack.io/anthropic-scion-git-replacement"
link: "https://thenewstack.io/anthropic-scion-git-replacement"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T14:12:53Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "This week, Anthropic revealed it built an in-house version control system  to handle exploding code merges. It says Claude was both part of the problem that caused the bottleneck and instrumental in building the solution.  \n\n When the AI company’s daily code merges hit more than 30,000 in September 2026 (up from just 2,500 in May), it realized this trend was likely to continue, and it needed an…"
tags: ["AI Engineering", "CI/CD", "Developer tools"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 1012
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic built its own git replacement for AI-scale coding. But you can’t have it.

The New Stack · Meredith Shubel · 2026-10-15

Anthropic built its own git replacement for AI-scale coding. But you can’t have it.
This week, Anthropic revealed it built an in-house version control system to handle exploding code merges. It says Claude was both part of the problem that caused the bottleneck and instrumental in building the solution.
When the AI company’s daily code merges hit more than 30,000 in September 2026 (up from just 2,500 in May), it realized this trend was likely to continue, and it needed an alternative to the git-based system that was beginning to falter: “Every bottleneck we remove immediately leads to a further increase in the amount of code we produce.”
Dubbed Scion, its in-house version control system has a 200x smaller infrastructure footprint in CPU and memory than its previous git-mirroring infrastructure, per Anthropic. Plus, it says CI and research jobs can now check out code two orders of magnitude faster.
That’s great news for Anthropic — but just a tease for everyone else. Even though Anthropic expects other companies to hit similar bottlenecks, it has no plans to release Scion or create a public version any time soon. For developers dealing with similar scaling issues, inspiration from Anthropic is all they’ve got for now — though it says it wants to partner with GitHub, GitLab and the open source community to bring some of Scion’s ideas to git.
Why Anthropic built Scion (and why it says git wasn’t enough)
Scion is Anthropic’s in-house version control system, which it says it built and fully migrated its monorepo to in just five months.
The project started around the same time Anthropic made Claude Mythos Preview and Claude Tag available internally. The AI company says those releases were part of the reason it needed Scion in the first place—and why it was able to build it so quickly.
“At Anthropic, coding is no longer the bottleneck to building systems or doing research,” the company wrote, citing Claude’s ability to write code at speed and scale as the reason why developer infrastructure is floundering to keep up. “The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI.”
git, Anthropic says, is no longer a match for high-volume AI coding, at least not for its enormous monorepo and unusually large volume of code changes. Scion, in contrast, can handle that scale and even reduce infrastructure overhead.
“Every bottleneck we remove immediately leads to a further increase in the amount of code we produce.”
For one, Scion delivers always-on server access, letting clients fetch data whenever needed. For clients that Anthropic says are always online, git’s assumption that they need to work offline with complete repository copies adds unnecessary work.
The Anthropic version control system also offers API-based source control, letting a CI job or tool ask questions about code history and other repository information without maintaining a local repository, à la git.
Plus, because Anthropic says Scion is horizontally scalable (i.e., its repository data is distributed across independently scalable components), it can expand capacity as needed without having to maintain hundreds of git mirrors.
Anthropic said Claude’s fast coding prowess also helped make Scion “among the most well-tested and well-defended codebases we have ever worked on,” with extensive simulations, fuzzing, and sophisticated rate limiting.
That’s just a taste of what Anthropic says Scion can do, likely attractive capabilities for other teams facing the same challenges. But if they want to get in on the Scion benefits, they’re out of luck.
It says the same scaling problem is coming for other AI-heavy teams
The juggernaut AI company may be dealing with more AI-generated code than the average team, but it predicts its story of AI coding outpacing developer infrastructure won’t be unique for long.
As written in its announcement, “Anthropic uses Claude to write software far more than almost any other company, so we’re often the first to see where tools built for human scale start to strain. Source control is just one example of this.”
The strain, it says, has exceeded the capacity of traditional developer infrastructure and Git’s original design assumptions.
Even though Anthropic expects other companies to hit similar bottlenecks, it isn’t offering Scion publicly and has made no commitment to a public version.
Source control, though, isn’t the only area facing a paradigm shift from AI coding agents, Anthropic reminds. Going forward, the company predicts small engineering teams will more often develop new systems quickly.
That’s what happened with Scion. Anthropic says a team of just seven built Scion (plus a new code review tool, Antique, and a half dozen other systems) in five months — a far cry from what it says would normally take a large-scale engineering team years of work.
Why it’s not sharing
Though Anthropic thinks other companies will face similar source control issues soon, it’s not sharing its solution.
For starters, it says token costs could be prohibitive for many companies: “Anthropic is unique in that our ability to spend tokens for internal use far exceeds what any other business would realistically want to spend.”
Scion is simply too niche to be broadly useful outside Anthropic’s work environment.
Plus, it says Scion is simply too niche to be broadly useful outside Anthropic’s work environment. Because the version control system is a significant departure from git, other companies would need a boatload of migration work to make it suitable.
For now, then, Anthropic is putting the kibosh on building a public version. It’s also clear about where it stands on Scion’s broader applicability, calling its source control system “by no means a suitable replacement for git for general use.”
So why all the talk? Because Anthropic believes Scion still has a role to play — however small — in addressing the scaling concerns that come with increasingly capable AI coding agents. By sharing its thinking, it hopes to peel back the curtain on its in-house solution so other developers can apply some of Scion’s most successful ideas to git.
For Scion-curious developers, that seems like the best they can hope for right now.
