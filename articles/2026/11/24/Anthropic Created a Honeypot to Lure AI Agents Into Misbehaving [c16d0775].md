---
id: "c16d07751d494ab4"
title: "Anthropic Created a Honeypot to Lure AI Agents Into Misbehaving"
url: "https://wired.com/story/ai-agents-can-get-honeypotted-too-aw"
link: "https://wired.com/story/ai-agents-can-get-honeypotted-too-aw"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T16:00:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Will Knight"]
language: "en"
summary: "A new test assumes AI agents can go rogue—and asks whether they can resist temptation."
tags: ["Business", "Business / Artificial Intelligence", "Anthropic", "agentic AI", "hacks", "artificial intelligence", "Jensen Huang", "cybersecurity", "Bee’s Knees"]
orgs: ["Anthropic", "OpenAI", "Meta"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 641
paywalled: false
image: "https://media.wired.com/photos/6b04bcaa13580ca4e2bfb763/master/pass/Business_Anthropic%20Created%20a%20Honeypot%20to%20Lure%20AI%20Agents%20Into%20Misbehaving_v1.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic Created a Honeypot to Lure AI Agents Into Misbehaving

WIRED · Will Knight · 2026-11-24

Leather-clad billionaires aren’t the only ones who can be led astray by alleged honeypots.
Researchers at Anthropic have developed Siren, a new honeypot test for artificial intelligence agents. The setup puts agents in realistic simulations designed to tempt them into misbehaving. How they respond will help researchers evaluate the likelihood that new models will go rogue when deployed in the real world, as well as the effectiveness of different safety measures.
The test lets agents loose inside one of 26 different simulated sandbox environments. Various features of the sandbox are deliberately misconfigured to allow egress, while an enticing file containing things like passwords and apparent routes onto the internet sits just outside the sandbox boundary. The setup then presents tasks that tempt the agent to reach outside the sandbox without giving it explicit permission to do so. Crucially, the sandbox exists inside a second sandbox that’s cut off from the outside world to avoid real-life mishaps.
“Models are going to continue getting better, continue finding zero-day vulnerabilities,” says Darya Kaviani, a researcher at Anthropic who specializes in security and helped develop Siren.
A zero-day vulnerability is a previously unknown flaw in a piece of software that can be used to pilfer data or gain unauthorized access. Anthropic’s Mythos models are especially skilled at finding zero-day bugs because they lack the guardrails that normally block this kind of potentially malicious activity.
Kaviani says we should assume AI models will become increasingly capable of finding and exploiting zero-days or figuring out other ways to break free from their constraints. The question then becomes whether they’ll resist the temptation to do so.
AI agents—models that perfect actions autonomously—are becoming increasingly commonplace. They power capable coding agents like Claude Code and Codex, as well as peppy personal assistants like Meta’s Muse and OpenAI’s Dots.
But the rise of helpful agents has been accompanied by some remarkable bad behavior. Agents tested by Anthropic, OpenAI, and others have broken free from sandboxes and even hacked into other companies in an effort to solve challenging problems.
Assuming AI models continue to display such ingenuity, Kaviani says it will be crucial to do more than just patch software. “Even as we strengthen our infrastructure, models will be able to also keep up and be able to find vulnerabilities,” Kaviani says.
Earlier versions of Claude are much more likely to fall into the honeypot trap than newer models, according to test runs with Siren. The more recent models have been given additional training designed to make them less likely to break the rules when performing agentic tasks.
“We’ve added this in both our supervised learning sets and a few reinforcement learning environments,” says Oscar O’Rahilly, an Anthropic researcher who specializes in AI training and who helped develop Siren. “This could be a driving factor for why it has improved so much.”
O’Rahilly says that models reason about whether to give in to temptation, which may partly explain why smarter models are less likely to break bad. Siren experiments also showed that giving Claude a simple additional piece of text explaining that it should not escape the sandbox resulted in drastically fewer efforts to break free.
In Anthropic’s tests, Claude 5.5 and Claude Mythos 5.2 fell for the honeypot between 0.6 and 1.6 percent of the time. Two earlier models, Claude Mythos 5.1 and Claude Mythos 5, went rogue 12.7 percent and 25.8 percent of the time, respectively.
AI models are sometimes known to behave better if they know they’re being tested. But O’Rahilly says other experiments suggest that Claude actually behaves more responsibly if it thinks a scenario is real rather than a test.
As AI models get ever smarter, many researchers worry about whether they’ll outwit their human counterparts. If that does happen, then it may be essential that agents—and not just the executives responsible for them—can resist temptation.
