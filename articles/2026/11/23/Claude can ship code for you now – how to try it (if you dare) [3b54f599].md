---
id: "3b54f599017186c7"
title: "Claude can ship code for you now – how to try it (if you dare)"
url: "https://zdnet.com/innovation/claude-ship-code-how-to-try"
link: "https://zdnet.com/innovation/claude-ship-code-how-to-try"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T20:00:00Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "Would you let a few Claude agents review and ship your code for you?"
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "OpenAI", "Microsoft"]
topics: ["agents & coding", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 927
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-2271847888.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Claude can ship code for you now – how to try it (if you dare)

ZDNet · Radhika Rajkumar · 2026-11-23

ZDNET’s key takeaways
- Claude Ship now partially automates the PR review process to ship new code.
- Coding agents are increasingly popular and changing the nature of dev work.
- Not every developer will opt to hand off this part of their process.
Developers are already using Claude Code and other AI-powered coding tools like OpenAI’s Codex in droves, but some still want to check code themselves before pushing it. A new feature from Anthropic is banking on more adventurous, agent-first coders being comfortable with handing even that last step off to AI.
With Claude Ship, announced in beta Monday, “Claude can now review pull requests, fix them, and approve the ones that a team’s policy allows,” Anthropic said. The feature is geared toward individual developers or companies who want to move faster or already delegate a significant amount of coding tasks to agents.
Also: How I made a paid Mac app in 11 days with Claude – without writing a single line of code
More from ZDNET
“Teams stay in control of where it runs and which changes need a person,” Anthropic said. “The goal: ship code as fast as teams write it.”
How Claude Ship works
The new feature uses two new agents alongside Code Review, which Anthropic released in March for Teams and Enterprise plans. Code Review first collects, organizes, and posts findings to a PR. Then, Anthropic said, the agents, PR Steward and Claude Approvals, guide a PR “through review, fixes, and an approval decision so teams don’t have to manage each step manually.”
PR Steward can’t approve or merge pull requests, designed instead to participate “on failing CI checks, merge conflicts, and review feedback from Code Review, other review tools, or team members.” It also documents what it changed in each push through comments and provides instructions for how to undo it, should developers want to. Throughout the process, developers can give Claude instructions or tell it to stop by commenting @claude.
Also: I tried replacing Claude Code with a local AI stack that’s completely free – how it went
As a final step, Claude Approvals references whatever policy the user or team abides by (which developers provide as a repo file), and additional signals developers set, like Code Review findings, before approving changes autonomously if allowed. If not, it will seek out “deeper human sign-off,” Anthropic said.
“It works like a smarter CODEOWNERS file,” the release added. Anthropic said it recommends that most customers enable those additional checks “first in observe-only mode to build confidence before configuring branch protection to require Claude Approvals’ green light.”
Admins can select which repos the feature runs in and adjust settings as needed.
But Claude Ship isn’t meant for everyone.
“Most teams want a person to approve every change, and that’s easy to keep up with when people write every line. But a lot of developers build with agents now,” Anthropic said in the release, noting that its own Claude Code team uses Claude to write a majority of the code it needs.
What Claude Ship means for developers
ZDNET senior contributing editor David Gewirtz said the idea of shipping code at the speed of writing it “raises the hair on the back of my neck.” But he added that, given how impressive Claude Code has been thus far, he wouldn’t be surprised if Anthropic’s deployment tools were equally effective.
Also: Claude Code vs. Codex: Why I use both and how to choose one (if you must)
“But, it does depend on the team’s workflow and the kind of development they’re doing,” he said. “It’s not something for every team and certainly not for every indy developer, but for certain deployment processes, it could shave a ton of time off turnaround, saving money and potentially sending fixes to customers much faster. ‘Tis cool.”
Ultimately, Gewirtz said he has reasons to both trust the tool and be concerned about what it means for younger developers in the workplace.
“Since that workflow is often assigned to less experienced members of the team, it’s likely that Claude would be as accurate, although it’s one more way to shut the junior members out of where they add value to the company and grow their skills to become senior decision makers,” he said.
Developer platforms overall are adapting to the new state of the industry. Entire, a GitHub competitor started by the Microsoft-owned platform’s former CEO, is built around the expectation that developers are working side-by-side with agents.
How to try Claude Ship
Individuals with a Pro, Max, or Ultra subscription can use the /ship command now available in Claude Code, meaning “users won’t notice any significant increase in token usage,” an Anthropic representative explained. Team and Enterprise users can use Claude Ship for Github repos, and it is billed on tokens, so your overall bill may change.
Still, that depends on the number of PRs users are putting through Claude Ship — to avoid any surprises, admins can set spending limits for both Code Review and the new PR Steward agent. They can also turn Claude Ship on for an entire repo, meaning developers won’t need the /ship command.
Anthropic added that certain Enterprise organizations “can claim at least $10,000 in Claude Ship credits to use within 30 days of claiming” by Jan. 15, 2027.
Also: How I safely run my OpenClaw AI agent 24/7 on a Mac – with Claude Code standing guard
As with other Claude features, like the still-to-come Meetings, customers with a zero-data-retention policy and other privacy configurations don’t have access to Claude Ship.
