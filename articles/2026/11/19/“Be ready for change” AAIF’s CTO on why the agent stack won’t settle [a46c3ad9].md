---
id: "a46c3ad918ad3649"
title: "“Be ready for change”: AAIF’s CTO on why the agent stack won’t settle"
url: "https://thenewstack.io/agentic-ai-foundation-projects"
link: "https://thenewstack.io/agentic-ai-foundation-projects"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T18:24:12Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "If you’ve spent any time over the past year trying to get AI agents to talk to each other without tearing your architecture apart, you know the struggle: vendor lock-in, fragmented protocols, and context that definitely vanishes the second you attempt to make a cross-framework handoff. \n\n It’s astounding how fast developers’ needs have changed just in 10 months since the Agentic AI Foundation…"
tags: ["AI", "AI Agents", "AI Infrastructure", "Open Source", "Podcast", "Sponsored", "sponsored-podcast", "Video"]
orgs: ["OpenAI", "Anthropic", "Hugging Face", "Alibaba"]
topics: ["agents & coding", "models & research", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 1050
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “Be ready for change”: AAIF’s CTO on why the agent stack won’t settle

The New Stack · Chris J. Preimesberger · 2026-11-19

If you’ve spent any time over the past year trying to get AI agents to talk to each other without tearing your architecture apart, you know the struggle: vendor lock-in, fragmented protocols, and context that definitely vanishes the second you attempt to make a cross-framework handoff. 

 It’s astounding how fast developers’ needs have changed just in 10 months since the Agentic AI Foundation (AAIF) was formed to help solve those problems.  

 The Linux Foundation-backed AAIF gives shared agent infrastructure a home outside any one vendor’s control. It launched in December 2025 with three projects, including the Model Context Protocol (MCP), which connects AI applications to external tools and data. 

 On October 22 , Anthropic contributed Agent Skills, and OpenAI contributed Open Responses to the foundation, alongside projects from Hugging Face and Alibaba. The additions brought AAIF to 10 hosted projects. 

 The New Stack Editor-in-Chief Nick Lucchesi sat down with Manik Surtani , AAIF’s co-founder and CTO, for The New Stack podcast at AGNTCon + MCPCon in San Jose, shortly after Surtani announced the additions in his October 22 keynote. The news was still fresh — the problems behind it, though, were all too familiar. 

 “I think that’s always been there,” Surtani said of the needs these projects address. “We’ve always known that sandboxes are really important.” Agent Skills, too, was already in use before joining the foundation. What had changed was where these projects would be governed. 

 “…having a standardized way to speak to a model is super important.” 

 “I’m really happy [Agent Skills] is here. And Open Responses as well. I mean, having a standardized way to speak to a model is super important. And I’m glad to see that it’s now happening in a way that is vendor-neutral, in a neutral governance and everything else.” 

 Four giant projects join the foundation 

 The big news from Surtani was this: Four heavy-hitting projects had joined the AAIF. Here’s what each brings to the table: 

 Agent Skills (Anthropic): An open format for bundling instructions, scripts, and reference materials that an agent can load when it needs to perform a particular task. Write those instructions once, and use them across agents that support the format. 

 Open Responses (OpenAI): An open specification, based on OpenAI’s Responses API, for how applications send requests to language models and receive results. A shared format means less translation work when developers switch between compatible model providers. 

 OpenEnv (Hugging Face): A framework for building and sharing reinforcement learning environments, where agents practice tasks and receive feedback that can be used to train them. 

 OpenSandbox (Alibaba): A platform for running agent-generated code and other work in isolated environments, separating that execution from the surrounding system. 

 While Anthropic, OpenAI, Hugging Face, and Alibaba rallying around a neutral foundation sounds like an AI miracle, Surtani noted that developer demand for open governance has existed from Day 1. 

 “More than faster, I think people are going to be able to build on top of things that they can trust more.” 

 “More than faster, I think people are going to be able to build on top of things that they can trust more,” Surtani said. “It’s not like you couldn’t trust open responses before. Of course you could. But now everyone has a say in how it’s going to grow and how it’s going to get shaped.” 

 Developers learned this lesson the hard way during the early cloud-native boom. Nobody wants to build core enterprise infrastructure on tech they can’t help steer. 

 Tackling the real pain points: Agent memory and portability 

 What problem keeps Surtani up at night? In the near term, it’s agent memory and context management — the information an agent needs to keep working on a task, including what’s already happened. A harness is the software around a model that manages its tools and workflow. Carrying that context from one model or harness to another remains difficult, Surtani said; he wants teams to be able to share it across the agents and people working on the same problem. 

 Beyond context portability, Surtani emphasized that software engineering teams should design for model independence right now using abstractions, proxies, and standardized interfaces. In practical terms, that means keeping the application from being tied too tightly to one model provider: A proxy or router sits between the application and the model, letting a team switch the model behind the scenes. It doesn’t solve everything, he cautioned, but it handles much of the heavy lifting. 

 Unlike the cloud stack associated with the Cloud Native Computing Foundation (CNCF) — which Surtani described as already well-defined — the agentic AI stack is inherently fluid. 

 “My advice to people is just be ready for change. Change is going to happen.” 

 “My advice to people is just be ready for change. Change is going to happen,” Surtani told The New Stack . “Now, the good thing in all of this is that change is actually easy as well. With agents actually building themselves and writing code, it’s not going to be that expensive or that hard to migrate from one thing to the other.” 

 A sandbox for early-stage projects 

 With more than 300 member organizations signing on in just 10 months (ranging from fintechs to non-tech giants such as the Gates Foundation), AAIF realized its initial high barrier to entry — borrowed from the mature CNCF template — was ill-suited for a space evolving at warp speed. 

 To adapt, the foundation launched a new Sandbox lifecycle phase on September 1 to bring in early-stage, high-momentum community tools before they hit massive enterprise scale. 

 This Sandbox phase is a project maturity category, separate from the isolated execution environments provided by OpenSandbox. It gives promising young projects a place to develop under neutral governance, even before they have widespread production use. 

 Surtani’s main call-to-action for developers? Push your vendors for open standards, transparent specs, and true longevity. 

 Watch the full interview 

 Watch our full interview with Surtani to get his take on agentic commerce, agent permissions, advertising without human eyes, and why an AI stack might never fully solidify. Subscribe to The New Stack ‘s YouTube channel to keep up with our new episodes as they are released. 
 The post “Be ready for change”: AAIF’s CTO on why the agent stack won’t settle appeared first on The New Stack .
