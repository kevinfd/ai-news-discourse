---
id: "e04b4e930bcdca98"
title: "From learning to leaderboard: How Cisco upskilled 1,200 engineers in agentic AI with AWS AI League"
url: "https://aws.amazon.com/blogs/machine-learning/from-learning-to-leaderboard-how-cisco-upskilled-1200-engineers-in-agentic-ai-with-aws-ai-league"
link: "https://aws.amazon.com/blogs/machine-learning/from-learning-to-leaderboard-how-cisco-upskilled-1200-engineers-in-agentic-ai-with-aws-ai-league"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-19T18:26:22Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Rakesh Vangari"]
language: "en"
summary: "Cisco, like many large engineering organizations, is adopting generative and agentic AI to change how its engineers build software. The hard part is no longer access to the technology. It’s helping thousands of engineers move from watching a demo to confidently building with it. Recorded sessions and slide decks rarely close that gap. Engineers learn fastest when they build something real, see…"
tags: ["Amazon Bedrock AgentCore", "Amazon SageMaker AI", "Customer Solutions", "Intermediate (200)"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "safety & ethics"]
content_source: "fulltext"
word_count: 2324
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# From learning to leaderboard: How Cisco upskilled 1,200 engineers in agentic AI with AWS AI League

AWS Machine Learning Blog · Rakesh Vangari · 2026-11-19

Artificial Intelligence
From learning to leaderboard: How Cisco upskilled 1,200 engineers in agentic AI with AWS AI League
Cisco, like many large engineering organizations, is adopting generative and agentic AI to change how its engineers build software. The hard part is no longer access to the technology. It’s helping thousands of engineers move from watching a demo to confidently building with it. Recorded sessions and slide decks rarely close that gap. Engineers learn fastest when they build something real, see it fail, fix it, and try again.
AWS designed AWS AI League for exactly that. It turns hands-on AI learning into a gamified competition, where participants customize models and build agents on AWS, get instant feedback on a live leaderboard, and compete in a game-show-style finale.
Cisco is one of the clearest examples of what this looks like at scale. In 2025, Hemanth V, a Cisco software engineer, went from an internal Cisco event to being crowned the first AWS AI League Champion at AWS re:Invent 2025. In 2026, 1,200 Cisco engineers competed in an AWS AI League tournament at Cisco Transformation Fest 4.0. The winner, Nishanth Aluhonnu, earned a full event pass to AWS re:Invent 2026 in Las Vegas.
In this post, we share how Cisco and AWS used Cisco Transformation Fest and AWS AI League to build a lasting culture of learning by doing. We previously covered this program in From theory to delivery: How Atos upskilled 400 engineers in agentic AI, and here we look at Cisco’s experience. We walk through Cisco’s journey, share technical lessons from the 2026 winning agent, and explain how your organization can host its own AWS AI League.
What is AWS AI League?
AWS AI League helps organizations build advanced AI skills through competition. Each league follows three steps:
- Learn – A hands-on, 2-hour workshop led by AWS experts introduces the tools and the challenge.
- Build – Participants experiment at their own pace and submit to a live leaderboard, with an automated evaluator giving real-time feedback after each submission.
- Compete – Top finalists take the stage in a live, game-show-style grand finale.
Although AWS AI League offers multiple use cases, at Cisco it offered the following two challenges:
- Agentic AI challenge – Participants build agents with Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale with any framework or model. The agents move through a maze-like grid, solving challenges on the way to a treasure chest. The challenges map to real-world tasks such as handling inappropriate content, running code, retrieving information from the web, and extracting structured data. Builders can choose models for supervisor and sub-agents and add tools such as AgentCore memory, a capability of Amazon Bedrock AgentCore, and AWS Lambda Event Functions. Builders use Amazon Bedrock Guardrails to apply safety controls to their agents.
- Model customization challenge – Participants fine-tune models in Amazon SageMaker Studio using the latest training recipes. The challenge awards points when an automated evaluator rates a participant’s customized model as more accurate and comprehensive than a reference model on the specific tasks in the competition.
Finalists are scored on time efficiency, accuracy, agent planning, and token consumption efficiency.
The Cisco and AWS partnership
The AWS AI League story at Cisco grows out of a deep engineering partnership. Cisco and AWS bring together networking, cloud, security, and observability for shared customers including:
- Cisco SD-WAN, whose controller architecture runs on AWS and serves customers globally as a software as a service (SaaS) application.
- Cisco Meraki, Cisco Spaces, and Cisco’s IoT and smart buildings group.
- Cisco Cloud Control, a cloud-native, AI-powered application integrated with AWS services that brings together security, networking, observability, and collaboration.
- Cisco AI Defense, where Cisco’s security team uses Amazon Bedrock and Amazon SageMaker AI to embed AI governance and guardrails across the Cisco portfolio.
The two companies have also published joint deployment guides and Cisco Validated Designs across networking and AWS. A recent example of co-innovation is SD-WAN fabric on demand across the AWS backbone, built to deliver the resilience and uptime customers expect.
        “When you see that many business units independently choosing to build their next-generation platforms natively on AWS, that’s not a vendor relationship anymore. It’s a true engineering partnership.”
— Kumaril Kapoor, VP of Engineering, Cisco
Cisco’s VP of Engineering Kumaril Kapoor and AWS Industries India leader Chandra Balani sit down to discuss the AWS and Cisco partnership story, from co-innovation across networking, cloud, and AI to enabling thousands of engineers through the annual Cisco AWS Transformation Fest.
Cisco Transformation Fest: Enablement at scale
As the partnership grew, it extended beyond technology to people. Working closely with Cisco teams in India, AWS saw a strong appetite for learning and experimenting among Cisco engineers across many business units. The question was how to scale that impact beyond the day-to-day touchpoints of the partnership.
The answer was Cisco Transformation Fest, first held in 2022. The program is built on five tenets the team summarized as SCALE:
Transformation Fest brings together several formats: AWS GameDays, AWS AI League, sessions where Cisco leaders share best practices and success stories with peers, and sessions on Amazon and AWS culture. What began as a single event is now an annual, three-day program that has completed its fourth edition and reached around 2,000 engineers. AWS continues to engage Cisco teams with hands-on workshops and experience-based accelerations.
        “It has been genuinely valuable for us, and it’s really a journey, but I appreciate most is the intent behind it. It’s built around our people. It gives our engineers the time, the space, and the hands-on support to grow real skills on AWS. For us, it has turned into a lasting culture of learning by doing. It’s not a one-off event.”
— Kumaril Kapoor, VP of Engineering, Cisco
Where enablement becomes execution: AWS AI League at Cisco
Of all the Transformation Fest formats, AWS AI League has had the most visible impact. Its gamified, hands-on structure puts engineers to work with Amazon SageMaker on fine-tuning, model customization and Amazon Bedrock AgentCore for agent building, against a clock and in front of their peers. Participants leave with practical experience and genuine confidence in their AI skills.
        “This is where enablement actually turns into real execution.”
— Kumaril Kapoor, VP of Engineering, Cisco
2025: From the Cisco campus to global champion
Hemanth V, a software engineer in Cisco’s switching core platform team, had an inspiring journey that set the benchmark for Cisco.
His journey had two stages:
- AWS AI League at Cisco AWS Transformation Fest 3.0. He competed against more than 600 participants from Cisco in a model customization challenge, fine-tuning a small model in Amazon SageMaker, and won the title.
- Global grand finale at AWS re:Invent 2025. In Las Vegas he faced a completely different challenge: the agentic AI track, where he built an agent to navigate a dynamic, game-style maze. He took first place and was recognized during the re:Invent keynote.
Hemanth finished ahead of Ross Williams from Aqfer (second place) and Deepesh Khanna from Capital One (third place).
        “You don’t need to know everything beforehand. You will learn a lot of things on the way. The only thing that matters is your curiosity and willingness to learn.”
— Hemanth V, Software Engineer, Cisco, and 2025 AWS AI League Champion
2026: 1,200 engineers, one champion
In 2026, Cisco Transformation Fest 4.0 hosted a full AWS AI League agentic AI tournament. The AWS account team ran pre-event training so that engineers with no prior agentic AI experience could compete from day one. The format was designed to narrow a large field down to a single winner:
Nishanth Aluhonnu, a software engineer at Cisco, finished first at every stage and earned a full conference pass to AWS re:Invent 2026.
The finale itself showed why the format works. Participants could not change code, tools, or prompts during the finale, only a short steering instruction before each round. Success depended on how well each agent made decisions on maps it had never seen before. Nishanth lost the first round, then won the second by a wide margin by ignoring a board full of low-value coins in favor of a single high-value challenge.
Examining what it takes to win an agentic AI challenge
The 2026 winning agent offers lessons that go well beyond the game. Each design choice maps to a decision teams face when they run agents in production.
Output tokens are the real cost
The agentic AI challenge scores agents on challenge points, a treasure bonus, remaining lives, and a token bonus, computed as tokenBonus = 1000 - (totalOutputTokens / challengesVisited).
In the qualifier, the top four agents all solved the map. The first-place agent emitted 1,220 output tokens and the second-place agent emitted 1,430, and the final margin was only 16 points out of nearly 16,000. After every agent can solve the problem, efficiency decides the winner.
To understand which tokens mattered, Nishanth built nine variants of the same agent, changing one thing at a time. The result was clear: tool results and the system prompt didn’t count against the score, but everything the agent wrote, including tool call arguments, did. Each tool call carried roughly 52 tokens of fixed overhead on top of its arguments.
This mirrors real-world cost. Generating output is sequential and is typically priced several times higher than input, and in an agent loop that cost compounds across every step. A long, well-structured system prompt (which you can also cache) is cheap. A chatty agent isn’t.
One agent, not five
A common architecture for this challenge is a supervisor agent on Amazon Bedrock AgentCore that delegates to specialist sub-agents for navigation, computation, and web retrieval. It’s a sound pattern for many production systems. The winning design used a single agent with no sub-agents. Instead, the prompt began with a short dispatch table that matched each challenge type to the right approach in a single turn.
The reasoning was simple: every handoff between agents is a message the model has to write, and in this challenge every written token is scored. The lesson isn’t that sub-agents are bad. It’s to choose your architecture based on what coordination costs you. When coordination is expensive, a flatter design can win.
The following diagram shows the AWS reference architecture for the agentic AI challenge: a supervisor agent with specialist sub-agents. The winning design deliberately didn’t use this multi-agent pattern.
In this reference architecture, a supervisor agent runs in Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore, and coordinates three sub-agents, with Amazon Bedrock Guardrails and AgentCore memory connected to the runtime. The supervisor and sub-agents route through the Amazon Bedrock AgentCore Gateway, a capability of Amazon Bedrock AgentCore, to four tools: a navigation tool, browser tool, code execution tool, and custom tools using AWS Lambda functions.
Put deterministic logic in tools
Route planning was not left to the model. It ran in an AWS Lambda function that treated the board as an optimization problem. Each tile carried an expected value: the points it paid, minus the lives it could cost, minus the tokens the agent would spend to solve it. The planner respected constraints, such as collecting a key before its door, and refined the route within a time budget.
This is a useful pattern for most agents: let the model handle language and judgment, and move search, math, and rules into tools where they are faster, cheaper, and repeatable.
Make decisions on value, not habit
The second finale round was designed as a trap. A seven-by-seven board was almost entirely covered in coins worth 25 points each, while a single scheduling challenge tile was worth 1,500 points. Habit said to collect the coins. The planner’s value table said the coins were noise. The agent went for the high-value challenge and scored 7,537 points in that round, compared with 5,953 for the next finalist. That round built the lead that carried the agent to the overall win.
Impact for Cisco
Across two years of AWS AI League at Cisco, the impact shows up in skills, culture, and recognition:
- Hands-on AI skills at scale. 1,200 engineers took part in the 2026 tournament, building agents on Amazon Bedrock AgentCore, many of them with no prior agentic AI experience.
- Connections across business units. Engineers who would otherwise never have met competed in the same tournament, shared approaches, and learned from each other.
- A lasting culture of learning. Now in its fourth year, Transformation Fest has become an annual commitment rather than a one-off hackathon.
- Recognition, two years in a row. A Cisco engineer won the 2025 AWS AI League global title, and the 2026 Cisco champion will attend AWS re:Invent 2026.
- Leadership visibility. The 2026 finale took place in front of Cisco and AWS senior leadership, giving engineers a real stage for their work.
For Hemanth, the biggest takeaway was confidence. You do not need to master everything before you start. You learn by getting hands-on.
        “Technology alone isn’t enough. You need people who are empowered to experiment with it. Transformation Fest created that enablement environment, and AWS AI League created the opportunity for execution.”
— Kumaril Kapoor, VP of Engineering, Cisco
Conclusion
In this post, we showed how Cisco and AWS turned enablement into execution. Cisco Transformation Fest created a space for engineers to learn by doing, and AWS AI League gave them a real challenge, a scoreboard, and a stage. The result is a culture of hands-on AI building that reaches thousands of engineers.
To get started:
- Learn how to host a tournament in your organization on the AWS AI League page.
- Build your agentic AI and model customization skills with the AWS AI training catalog on AWS Skill Builder.
- Follow the AWS AI League 2026 global finale at AWS re:Invent 2026 in Las Vegas.
We look forward to seeing what your teams build.
