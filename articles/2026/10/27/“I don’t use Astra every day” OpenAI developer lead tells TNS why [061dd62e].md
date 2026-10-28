---
id: "061dd62e60a100d7"
title: "“I don’t use Astra every day”: OpenAI developer lead tells TNS why"
url: "https://thenewstack.io/openai-devday-models-agents"
link: "https://thenewstack.io/openai-devday-models-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T14:23:01Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Jennifer Riggins"]
language: "en"
summary: "OpenAI’s recent releases have given developers more options for using AI in software. At its 2026 DevDay, the company introduced new models, tools, and agents that raise practical questions about cost, speed, safety, and how teams keep up. \n\n On September 29, OpenAI held its fourth annual DevDay near its San Francisco headquarters. The company listed more than 20 major announcements across…"
tags: ["AI", "AI Models", "Large Language Models"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 2331
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “I don’t use Astra every day”: OpenAI developer lead tells TNS why

The New Stack · Jennifer Riggins · 2026-10-27

“I don’t use Astra every day”: OpenAI developer lead tells TNS why
OpenAI’s recent releases have given developers more options for using AI in software. At its 2026 DevDay, the company introduced new models, tools, and agents that raise practical questions about cost, speed, safety, and how teams keep up.
On September 29, OpenAI held its fourth annual DevDay near its San Francisco headquarters. The company listed more than 20 major announcements across ChatGPT, Codex, its models, and developer APIs. Among them were GPT-6.1 Sol and a faster Ultrafast tier for GPT-6 Astra; Ultrafast support for Sol followed on October 8.
The announcements included OpenAI dots, persistent agents that can work in the background. Backed by GPT-6 Astra, they can connect to more than 4,000 apps through OpenAI’s plugin ecosystem and take on ongoing responsibilities.
These agents run continuously in the background, researching and monitoring, then suggesting actions — completing pull requests (PRs), drafting messages, documentation, and analysis, or booking meetings — for human-in-the-loop review. Depending on a user’s rules and the action involved, a dot may proceed, request approval, or leave a sensitive task to the user.
Other updates included the Decisions API, which uses predefined answer choices to classify inputs or route requests, and computer use in the Agents API, which lets agents interact with software interfaces.
Ahead of OpenAI’s Dev Day Exchange on November 3 in London, Vaibhav “VB” Srivastav, OpenAI developer experience and community lead for EMEA, told The New Stack about the cascade of features the company is releasing. The London-based Srivastav also noted how the new releases may affect the day-to-day work of engineers.
This interview has been edited for clarity and brevity.
The New Stack: At DevDay, OpenAI announced more than 20 products and updates. In a time of rapid change, how do developers and engineering managers decide what to use? And how does OpenAI consider the cost of developers absorbing these changes?
Vaibhav Srivastav: We did ship a lot, right? The overarching goal was to reduce friction for pretty much everyone across the board when we want to release something. This ranges from the average person using ChatGPT to answer questions, to more advanced folks using Codex for day-to-day engineering tasks, to folks in hybrid roles like engineering managers or people managers. From a developer’s lens, I’m particularly passionate about four of those 20 and helped ship them with the team.
First and foremost is GPT-6.1 Sol. It gets up to 95% of Astra’s performance, but at one-fifth the cost. When we shipped GPT-6 Astra, everyone was like, “Hey, this is a very good model. We love it,” but we couldn’t bring it to a price point everyone could afford for this level of intelligence. That’s why we worked to bring GPT-6.1 Sol to a price point that lets everyone benefit from it across plans.
I don’t use Astra every day. I do use GPT-6.1 Sol as my main go-to.
Sol vs. Astra trade-offs
TNS: OpenAI describes GPT-6.1 Sol as offering “near-Astra intelligence” at one-fifth of Astra’s standard input and output token prices. What type of evaluations back up this idea of ‘near,’ and where does Sol fall short of Astra?
VS: When we get a model, we run traditional benchmarks, including Terminal-Bench 4.0, GDPval, GDP.pdf, SWE-bench, and many others. On those benchmarks, GPT-6.1 Sol and GPT-6 Astra are very close. Both Terminal Bench and SWE-Bench are good indicators of how a model would perform on difficult and long-running tasks. In both benchmarks, 6.1 Sol is empirically very close to GPT -6 Astra.
Second, and more importantly, we dogfood these models internally before they’re ready to ship to see how good a particular model is. A good measure of success is when everyone starts adopting that model as their daily driver across engineering, product, and adjacent teams like marketing, human resources, and so on. When we started dogfooding this model, we saw a rapid increase in people switching to GPT-6.1 Sol as their daily driver.
They could use whatever they want. We have no internal limits on what people can do with these models, so they can choose whichever model they want, and they keep choosing 6.1 Sol.
TNS: For a developer or a team choosing among GPT-6.1 Sol, GPT-6 Astra, and the Ultrafast speed tier, what’s the decision rule? When is premium worth paying for?
VS: In my opinion, Sol gets you about 95% there for most tasks. For a new project or an unfamiliar problem, I would turn to Astra to look for loopholes or things I may have missed.
“If I use GPT-6.1 Sol to work on that feature and then use the same model for code review, it’s like checking my own work. I’d be biased toward saying it’s good.”
If I use GPT-6.1 Sol to work on that feature and then use the same model for code review, it’s like checking my own work. I’d be biased toward saying it’s good. For an adversarial review, I give GPT-6 Astra fresh context and ask it to poke holes, take the work apart, and help me make sure it’s safe, secure, and gets me the outcome I want.
TNS: Where does Ultrafast mode fit in?
VS: Ultrafast is for important, real-time use cases like fraud detection, financial investigations, and code investigations. Developers have told us they want something extremely fast for those cases. Ultrafast mode lets GPT-6 Astra, and now also GPT-6.1 Sol, deliver remarkably fast outputs — over 300 tokens per second — at a higher price than the standard tier, but still quite affordable.
We later added 6.1 Sol to Ultrafast. It costs 1.2 times standard Astra, so you get near-Astra performance at more than 300 tokens per second for 20% more than Astra.
Guardrails and Auto-review
TNS: Let’s talk about guardrails both around the plans developers can use, and also around safety and governance.
VS: Any feature that could add costs for enterprise or business users is off by default. They need to opt in explicitly.
The more interesting point for me is safety. As models do more and get faster, we want their actions to align with what you want. One of my favorites is called Auto-review. Before the model acts, a Luna-level [lightweight, ultra-efficient] model checks it against a policy you define.
For example: I don’t want the model to submit anything on my behalf, send emails, or share personally identifiable information. An organization or solo developer can define the policy, allowing these models to run safely and autonomously for longer.
Last week we made Auto-review free for Codex and ChatGPT subscribers — over 5 million weekly active users can benefit. We think it’s important to let these models run safely.
See also: OpenAI’s GPT-6.1 Terra worked around restrictions in 29.6% of runs in a controlled test
TNS: Now let’s talk about the development and impact of Decisions API.
VS: The Decisions API came together four or five days before DevDay. A team of four or five people shipped a production-ready API in preview for DevDay, then in beta a couple of days later. The Decisions API is multimodal: it classifies text and images and quickly returns structured output. Traditionally, you’d give an LLM a schema and ask for structured output. Now it’s 10 times faster at the same accuracy and costs $0.10 per million uncached input tokens.
How OpenAI dots work
TNS: Finally, let’s talk about one of the major DevDay announcements: OpenAI dots.
VS: A dot is a persistent, always-on agent that looks across the tools, plugins, and other surfaces you’ve given it access to. It identifies what needs your attention and orchestrates the work to get it done.
TNS: How does a dot decide what to act on without being asked, and what does a user see when it’s done something on their behalf?
VS: My dot is connected to Slack, where much of OpenAI’s work happens. It is also connected to my GitHub, where I contribute engineering work, and to my Gmail and calendar. Every so often, my dot looks through my Slack messages, DMs, mentions, mail, and calendar. It brings that information together and surfaces things I haven’t acted on or that it can take off my plate.
My team is spread globally, so someone is working around the clock. My dot could be like: Person X tagged you to review this pull request, or Person Y is waiting for information about upcoming model launches. Previously, I spent the morning sifting through thousands of Slack mentions and threads. I specifically tell my dot: Here’s someone on my team and what she does. When she flags things A, B, or C, make sure I know about it. It keeps gathering more context. It knows I want to respond quickly if my boss messages me, so that goes to the top of my list. If a product I’m working on launches tomorrow or the next day, that’s automatically a high priority.
My dot also looks through my engineering work, including PRs, and might say: This is already approved. You can merge it. Or it might say: I can merge it for you as well. I can say yes on my phone, and it can merge the PR, check that tests pass, and verify it looks right in production.
TNS: Some developers say AI leaves them feeling more isolated. Do you miss the sillier things in Slack, like meme sharing or other ways to bond with your engineers?
VS: I’ve had the opposite reaction. I joined OpenAI in December last year. At the time, models were good but couldn’t reliably do things autonomously for me. Now the models are much better. They can get context from wherever you point them to. Before, I spent a lot of time making sure the model did what it was supposed to, leaving less time to catch up or banter with my team.
“Every Friday, it checks my calendar and blocks 30 minutes with someone I haven’t spoken to in the past three or four days. If I did it manually, I would never stick to it.”
Now I’m more on top of my work because I’m not spending an hour or two sifting through Gmail and Slack messages. I’ve asked my dot to help me catch up each week with someone on my team I haven’t spoken to in a while. Every Friday, it checks my calendar and blocks 30 minutes with someone I haven’t spoken to in the past three or four days. If I did it manually, I would never stick to it.
TNS: With so many recent updates, different teams will be piloting different features. What should they measure to know if it’s working? What metrics turn out to be misleading?
VS: Every new model should be better overall, based on metrics and what we see internally. But the performance boost varies by use case.
When we ship a model, test it on an isolated use case — a migration, new product, or monitoring task — and measure the lift. The lift can mean the same outcome at a lower cost or a better result.
For an organization, the question is how much it’s willing to pay for a given outcome. That’s where the other models in the family come in. We’ve got GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, with others in the pipeline.
The same goes for features like Ultrafast. Not every problem needs Ultrafast, but you might need it to monitor a major user-impacting migration. That’s where Ultrafast with 6 Astra or 6.1 Sol comes in.
Put a few problems through that test to see whether the model or feature helps. We do the same internally. We run A/B tests to see how features work for users. We also look at product-market fit for each feature or model.
Model deprecation and migration
TNS: OpenAI has accelerated its model release cycle. What commitments can you make to developers building production-ready systems on these APIs about stability and migration paths?
VS: Stability and the end-user experience are important to us. If you go to status.openai.com, you can see our availability, with four or five nines, which means that we actually take this very seriously.
The way we ship models has changed a lot in the past year. Better models help us build the next generation faster, improving productivity for developers and researchers.
“Because we ship faster, we don’t deprecate a model until we’re certain the next generation is cheaper and more accurate across the board.”
Back in November of last year, we had GPT-5.1. We’re now at GPT-6 Astra and GPT-6.1 Sol. Because we ship faster, we don’t deprecate a model until we’re certain the next generation is cheaper and more accurate across the board.
For the API, we give three months’ deprecation notice and a migration path so your workflows can be cheaper and better with the next model.
We still serve GPT-5.5 to API users, even though we’re already at 6.1 Sol.
TNS: How can developers manage that much continuous change and migration? What has to change in the traditional agile software development lifecycle?
VS: We see this internally: you build something, and the next model helps you improve it. It’s always a trade-off. There’s always something you care less about. If I built software to solve a problem within my team, I might not need the best frontier performance.
But let’s say I’m building something that handles transactions for my users or another product they use directly. Then I’d want the best performance and current state of the art.
Before AI, teams developed software in sprints toward a launch, then paused new features to fix what was broken. They repeated that cycle over months or quarters. We see the same thing with models.
A new generation arrives; you sprint to use it, then pause. When another model arrives, you use it to improve security and build better features. I see it as an extension of what developers were already doing.
