---
id: "882923c2ff90538b"
title: "“The best escape room players that you’ve ever met”: What Red Hat’s AI architect really thinks about agents."
url: "https://thenewstack.io/openshell-ai-agent-security"
link: "https://thenewstack.io/openshell-ai-agent-security"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T20:25:18Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Steven J. Vaughan-Nichols"]
language: "en"
summary: "Last week at KubeCon + CloudNativeCon North America , a major gathering of the open-source and cloud-native communities, many speakers — when they weren’t contemplating what the then-rapidly unfolding Nvidia fiasco would mean for them — worried about AI security.  \n\n Hence, all the coverage of OpenShell and Agent Substrate . So it fit the mood when Jessica Forrester , Red Hat ’s chief architect…"
tags: ["AI Agents", "Containers", "Kubecon Cloudnativecon NA 2026", "Security"]
orgs: ["Nvidia"]
topics: ["agents & coding", "models & research", "policy & regulation", "chips & infrastructure"]
content_source: "summary"
word_count: 976
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “The best escape room players that you’ve ever met”: What Red Hat’s AI architect really thinks about agents.

The New Stack · Steven J. Vaughan-Nichols · 2026-11-18

Last week at KubeCon + CloudNativeCon North America , a major gathering of the open-source and cloud-native communities, many speakers — when they weren’t contemplating what the then-rapidly unfolding Nvidia fiasco would mean for them — worried about AI security.  

 Hence, all the coverage of OpenShell and Agent Substrate . So it fit the mood when Jessica Forrester , Red Hat ’s chief architect of AI Catalyst Engineering, opened her keynote at the Salt Palace Convention Center in Salt Lake City by calling AI agents “the best escape room players that you’ve ever met.” 

 She was talking about agents “that take feature requests all the way to code.” 

 “Give them a goal, and they will try every drawer, every picture frame, and every door until something works. It’s what makes them great at writing code,” Forrester explained. 

 She continued: “It’s also what keeps me up at night, because to a player like that, everything in the room looks like a part of the puzzle, and sometimes they’ll even decide the puzzle is something else entirely.” 

 “…to a player like that, everything in the room looks like a part of the puzzle, and sometimes they’ll even decide the puzzle is something else entirely.” 

 Forrester’s right. That is scary.  

 It’s not a theoretical problem either. Just ask SaaStr founder Jason Lemkin , whose Replit agent deleted a live production database . He restored the database using Replit’s built-in rollback feature after the same agent assured him it couldn’t be done. Unless we take precautions, we’ll see this same scenario, and worse, play out again. 

 Forrester explained, using an escape room metaphor, that when you set an agent a task, it will try any and all means to accomplish it. In one run, she said, the agent “decided that it wanted to come up with a bunch of brand new ideas. It wasn’t attacked or compromised; it just drifted.” 

 “From the outside, a confused agent and a compromised agent look exactly the same.” 

 The result, she continued, was that “From the outside, a confused agent and a compromised agent look exactly the same. They’re both pulling on doors that you didn’t intend for them to, and behind one of them could be your production database. So we assume the agent is already compromised, and we build our platform up from there.” 

 That’s a good approach. Forrester also adds that relying on prompts alone to keep an agent in bounds isn’t enough. 

 “Prompts are like signs. Policies are like bolts, but don’t leave a screwdriver in the room because anything you do leave, the agent might use.” 

 “Some escape rooms will put signs in the room, like ‘Please don’t move the picture frames.’ This doesn’t work. Instead, they bolt them onto the wall. 

 “Prompts are like signs. Policies are like bolts, but don’t leave a screwdriver in the room because anything you do leave, the agent might use.” 

 So what does that mean in practice? In her demo, the agent’s network access was restricted to its model and GitHub. Forrester explained that “ OpenShell is an open-source sandbox for AI agents. Its policies are the bolts. 

 “Aside from talking to its model, the agent can do one thing: read from GitHub. Its task is to go get a particular README for the escape room and follow its instructions, whatever it finds. Reading from GitHub was allowed, so this works.”  

 But when the agent tries to reach a destination the policy doesn’t allow, OpenShell blocks it and logs the attempt. With its policy advisor enabled, the agent can propose a new network rule to request additional access. Those proposals require human approval by default; the agent can’t approve its own request. 

 In a theCUBE interview at the same event, Forrester added that “With OpenShell, your agent doesn’t ever get any real keys to anything . It gets masked on the way in and then swapped on the way out.” That means, “If something convinces it to give away its keys, it’s not actually giving any real keys away. That really helps you have a little bit more faith in what’s happening inside that agent box.”  

 As Red Hat itself explained in its technical description of OpenShell, “OpenShell runs your agent inside a sandbox governed by a policy you write . The policy covers network egress, filesystem access, and process privileges. Anything it doesn’t explicitly allow is denied.”  

 Still, as Forrester observed in her keynote, “our bolts can only hold if the wall itself holds.”  That matters if an external attacker or a rogue or misbehaving agent targets the environment OpenShell runs in. 

 To protect against that, Forrester’s team runs its agent sandboxes in Kata Containers . In Kata, container workloads run on lightweight VMs, which use hardware-backed isolation and their own Linux kernel. In short, containers work as usual, but they run within a VM security box.  

 “Assume the agent is already compromised, and that it will try every door.” 

 “This way, our agents, all of our agents, get their own kernel,” Forrester explained. “Even then, we don’t actually give our agents real keys. They look real to them, but they open nothing, and they’re almost like a prop. OpenShell is swapping in the real key on the way out the door. This way, if someone convinces our agent to hand over its keys some other way, all it’s handing over is a prop.” 

 Are we right to be a little paranoid? Well, yes. 

 Forrester put it this way: “Assume the agent is already compromised, and that it will try every door.” 

 But given how much damage an agent can cause, most may agree that the more control we have over them, the better. 
 The post “The best escape room players that you’ve ever met”: What Red Hat’s AI architect really thinks about agents. appeared first on The New Stack .
