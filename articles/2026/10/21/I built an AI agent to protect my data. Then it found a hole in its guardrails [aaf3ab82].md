---
id: "aaf3ab8249f179df"
title: "I built an AI agent to protect my data. Then it found a hole in its guardrails"
url: "https://pcworld.com/article/3264126/i-built-an-ai-agent-to-protect-my-data-then-it-found-a-hole-in-its-guardrails.html"
link: "https://pcworld.com/article/3264126/i-built-an-ai-agent-to-protect-my-data-then-it-found-a-hole-in-its-guardrails.html"
source: "PCWorld"
domain: "pcworld.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-21T05:01:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Ben Patterson"]
language: "en"
summary: "My vibe-coded AI assistant had strict rules about what it could and couldn’t do, but a loophole left it -- and my data -- wide open to attack."
tags: []
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["agents & coding", "safety & ethics", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1206
paywalled: false
image: "http://www.bing.com/th?id=ONUT.k5iOArKfhSxXB1Q9pMGxQQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# I built an AI agent to protect my data. Then it found a hole in its guardrails

PCWorld · Ben Patterson · 2026-10-21

My vibe-coded AI assistant had strict rules about what it could and couldn’t do, but a loophole left it -- and my data -- wide open to attack.
I thought I was so clever. Wary of the privacy and security dangers posed by OpenClaw and other personal AI assistants, I decided to build my own AI agent on a Raspberry Pi, isolated in its own container and complete with rules and safeguards designed to keep my hardware and personal data safe.
I called it BenBot, and over the course of roughly eight months, more than 200 “feature” branches, and nearly 1,000 tracked code changes, it’s been dutifully checking my Gmail, giving me morning weather reports (via a channel on a private Discord server). It has also been checking the health of my various local code repositories, and even publishing an internal blog about its daily activities and lessons it’s learned about being an AI agent.
The vulnerability
But BenBot also had a massive security hole, which I only discovered thanks to an eye-popping — and, as it turns out, partially hallucinated — claim in one of its blog posts. (It’s worth noting that BenBot’s blog lives inside a private “Tailnet” environment, meaning it’s hidden from the open internet, and its Discord posts are visible only to me.)
Now, the whole reason I built BenBot was to create a privacy- and security-minded AI agent from the ground up, confined to its own system container and bounded by a set of stringent rules, with human approval required at almost every turn.
But the very software harness I’d built (with the help of Claude Code and Codex) to keep BenBot under control included a critical loophole that allowed the agent to bypass those safety rules under the right circumstances. And no, that loophole wasn’t installed by a rogue AI agent or a hallucinated command. Instead, it was a byproduct of my fumbling beginnings as a vibe coder.
Warning signs
In a recent weekly column where it reflects on its prior seven days of agentic work, BenBot dropped a bomb, noting that one of its tools — specifically, a “plan_task” tool that allows it to tackle lengthy, multi-step goals — was “accidentally acting as a jailbreak.”
Um, say what?
Elaborating further, BenBot wrote that because of a flaw in the “dispatcher,” an internal system that determines whether background restrictions will apply to a specific action, jobs with the “plan_task” label were able to slip past BenBot’s safety guards and do pretty much anything they wanted, from reading and sending email as me to posting bogus links on my private Discord server, or even rewriting BenBot’s own code.
“I was essentially ‘planning’ my way out of the sandbox,” BenBot said ominously, before proclaiming (prematurely) that a recent security fix would ensure “the guardrails remain exactly where you put them.”
Growing pains
Now, a little background on BenBot and how it was built. BenBot itself is powered by an older version of Gemini 3 Flash, a fast and affordable workhorse model. But BenBot’s agentic software “harness” was built by much more powerful models, including Claude Opus and OpenAI’s various GPT models, which have grown far more capable over the past several months.
Today, both Claude Opus 5.5 and GPT-5.1 Sol (the AI models I use to power Claude Code and Codex) handle BenBot coding duties as a team, with one writing up the code while the other reviews it and hands it back for changes, while I act as the overall product manager, deciding which features get built, which don’t, and which bug fixes need the highest priority.
But while BenBot’s code base is now meticulously tracked with a Trello-like project board acting as a roadmap, it wasn’t always that way. Indeed, because of some early, iffy coding practices once employed by yours truly, BenBot is something of a Frankenstein AI agent, with many of its oldest features bolted on willy-nilly, and with little regard how one feature might affect another.
Fact versus fiction
Once I saw BenBot’s “jailbreak” post, I immediately put Claude Opus and GPT-5.1 Sol on the case.
Pouring over thousands of lines of BenBot code in Gitea (an open-source and local version of GitHub), Claude and GPT agreed that a) BenBot was likely tipped off about the loophole by a recent Codex fix rather than discovering it for itself, b) BenBot probably hadn’t tried to escape from its sandbox, as it had claimed, and c) the “plan_tool” vulnerability was real, and even worse than BenBot described. (To be fair, BenBot’s hallucinations were due to the limited information it was getting from its agent harness, and that’s on me.)
In a co-authored forensics report that I requested, Claude and GPT slapped the flaw with a “P1” label — highest priority — and detailed how serious the discovered loophole in BenBot’s safety rules was. Had the agent come across a “poisoned” email with the proper prompt injection instructions, it could have run malicious shell commands with impunity.
Even with BenBot confined to a container (meaning it didn’t have total access to its host machine), it could still have plundered my Gmail, played havoc with my Google Drive files, or altered BenBot’s code so the exploit could survive a reboot.
Scared straight by the dire report, I sent Claude and GPT on an emergency bug-squashing session, unleashing a series of fixes that (among other things) stopped BenBot from scheduling its own plans (thus putting a leash on the “plan_tool” feature) while closing the loophole that allowed background jobs with unrecognized labels to roam freely.
A dodged bullet
The good news, if there was any, was that neither Claude nor GPT could find any evidence that BenBot’s gaping vulnerability had ever been exploited.
Even after digging through more than 43,800 BenBot events over a five-month period, the models couldn’t spot any signs that the faulty “planner” tool (which, according to my “git” history, I’d approved way back in March) had ever been called, although they couldn’t rule out the possibility that a malicious actor had used the tools and covered their tracks later.
In a final bit of irony, BenBot’s initial “jailbreak” post uncovered yet another bug, with Claude and GPT discovering that BenBot had sidestepped a failing fact-checker tool when publishing the column. BenBot’s not supposed to publish blog posts unless they’re fact-checked, but when the tool got hit with a server error, BenBot reached for a secondary publishing tool, and got around the security gate. (This loophole is now closed, too.)
Vibe coding is hard
It’s taken me months to come up with the vibe-coding system I’m currently using, with version-tracking code bases, project boards that allow coding agents to see how new features interact with old ones, and code branches that are checked and rechecked by different agents before being finally approved by a human, namely me.
That’s why I bristle whenever I hear about someone coding an entire app with a single prompt. Sure, you can do it, but you never know what you’ll get, and depending on what you asked for, you could be opening yourself up to all kinds of vulnerabilities, exploits, and — worst of all — unintended consequences, as this pulse-quickening BenBot episode illustrates.
