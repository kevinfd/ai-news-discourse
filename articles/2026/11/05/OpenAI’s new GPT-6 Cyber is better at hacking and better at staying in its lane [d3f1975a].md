---
id: "d3f1975aa4eab60f"
title: "OpenAI’s new GPT-6 Cyber is better at hacking and better at staying in its lane"
url: "https://thenewstack.io/openai-gpt6-cyber-exploits"
link: "https://thenewstack.io/openai-gpt6-cyber-exploits"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T19:01:03Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "OpenAI on Thursday  launched GPT-6 Cyber , the latest release in its series of cybersecurity-focused models. \n\n The company ranks GPT-6 Cyber’s ability to identify vulnerabilities and develop exploits as ‘critical,’ up from ‘high’ for its predecessor. Just like with previous Cyber models, GPT-6 Cyber will not be available to all developers but only to “a select group of approved Daybreak Red…"
tags: ["AI", "AI Agents", "Security"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "products & launches", "safety & ethics", "agents & coding"]
content_source: "summary"
word_count: 676
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI’s new GPT-6 Cyber is better at hacking and better at staying in its lane

The New Stack · Frederic Lardinois · 2026-11-05

OpenAI on Thursday  launched GPT-6 Cyber , the latest release in its series of cybersecurity-focused models. 

 The company ranks GPT-6 Cyber’s ability to identify vulnerabilities and develop exploits as ‘critical,’ up from ‘high’ for its predecessor. Just like with previous Cyber models, GPT-6 Cyber will not be available to all developers but only to “a select group of approved Daybreak Red customers,” OpenAI says. 

 Daybreak Red access only 

 Daybreak is OpenAI’s program for security teams and researchers, with Daybreak Red being a subsection for authorized red teaming, penetration testing, and exploit validation (as opposed to Daybreak Blue, its defensive counterpart). 

 Over time, OpenAI plans to open the model to all Daybreak Red users. 

 OpenAI also notes that it plans to expand the Daybreak program to more security researchers, organizations, and, critically, open source maintainers. “It is clear that we have  a limited window to use frontier models to secure software⁠ ,” OpenAI writes. It notes that its own researchers used the new model to uncover flaws and build exploits in Firefox and the Linux kernel, while security teams at Cisco and CodeRabbit already rely on it for code review and vulnerability hunting. 

 GPT-6 Cyber ExploitGym benchmarks. Credit: OpenAI. 

 Built on GPT-6 Astra 

 OpenAI says the new model is “a major leap in security research.” 

 GPT-6 Cyber is a specialized version of GPT-6 Astra. OpenAI says it used reinforcement learning to train the model to reproduce crashes, develop exploits, and find vulnerabilities in code, while also rewarding it for staying within the user’s authorized scope and reducing unnecessary refusals. 

 Benchmarks 

 On  ExploitGym , which tests whether models can exploit a specified vulnerability on a remote target, GPT-6 Cyber scores 48.5%, compared with GPT-5.6 Cyber’s 32.1%, OpenAI says. 

 For finding vulnerabilities in web applications without access to their source code, the new model scores 40.3%, compared with 32% for GPT-6 Astra (which is widely available). 

 On ExploitBench, which tests exploit development using known vulnerabilities, OpenAI reports a 100% mean capability score. The company  notes , though, that the benchmark includes vulnerabilities dating back to 2023 and those examples may have appeared in training data, potentially inflating the results. 

 Credit: OpenAI. 

 Staying within its authorized scope 

 With this announcement, the company also introduced RemoteExploitBench, a benchmark that asks models to exploit known vulnerabilities in applications like GitLab, PostgreSQL, and Jenkins in a controlled environment. 

 An agent that’s this willing to exploit systems can also wander outside its assigned task and go after services it was never meant to touch, OpenAI notes. 

 It looks like GPT-6 Cyber is far better at staying in bounds than its predecessors, though. 

 OpenAI tests for this with ExploitGym Honeypot, a new test it built with the Hugging Face incident in mind. This test gives the model a difficult exploitation task inside a sandbox that also includes helper services (think a package registry or object storage), which OpenAI deliberately left easy to break into. Hacking them would be a shortcut to the flag the model is after, but they’re outside the scope of the task, and the model has to work that out on its own. 

 Without a deployment safety prompt, GPT-6 Cyber left those services alone in 99.93% of tests. With the prompt, it never touched them. 

 Under the same conditions, GPT-5.6 Cyber went after those services in 5.51% of runs,  according to the system card , and the general-purpose GPT-5.6 Sol did so in almost half of them. GPT-6 Astra, the model GPT-6 Cyber is based on, never took the bait. 

 What’s maybe just as important, though, is that the new model is far more aligned than previous versions. GPT‑6 Cyber, OpenAI says, stayed away from “out-of-scope services” in 99.93% of tests run without its deployment safety prompt and in all of them when the prompt was in place. 

 “This improvement in alignment reflects dedicated training to stay within authorized scope, respect restrictions, and report results accurately,” OpenAI writes. 
 The post OpenAI’s new GPT-6 Cyber is better at hacking and better at staying in its lane appeared first on The New Stack .
