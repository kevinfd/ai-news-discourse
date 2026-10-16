---
id: "576253ed894737fc"
title: "How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore"
url: "https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore"
link: "https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-13T15:54:49Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Kenneth Salmon"]
language: "en"
summary: "This post is co-written with Kenneth Salmon, Edward Boswell, Jack Armstrong, Robert Bahn, and Nick Ciubotariu from ShipStation Global. \n Answering the same IT questions and clearing routine tickets drains time that IT teams could spend elsewhere. To reclaim it, the ShipStation Global Engineering team built Deckhand , an AI-powered IT help desk agent for Slack, on Amazon Bedrock AgentCore . \n…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Customer Solutions"]
orgs: ["Amazon", "Anthropic", "UK"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 2209
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore

AWS Machine Learning Blog · Kenneth Salmon · 2026-10-13

Artificial Intelligence
How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore
This post is co-written with Kenneth Salmon, Edward Boswell, Jack Armstrong, Robert Bahn, and Nick Ciubotariu from ShipStation Global.
Answering the same IT questions and clearing routine tickets drains time that IT teams could spend elsewhere. To reclaim it, the ShipStation Global Engineering team built Deckhand, an AI-powered IT help desk agent for Slack, on Amazon Bedrock AgentCore.
ShipStation Global is the leading intelligent shipping and logistics platform for small and mid-sized shippers, and it operates on a simple belief: the more efficient its teams are, the better it delivers for customers. Deckhand puts that belief to work. It answers routine IT and company questions from a curated knowledge base, reads error-message screenshots, and creates and updates Jira Service Management tickets.
In this post, we discuss how ShipStation architected Deckhand, which resulted in resolving 97.5 percent of incoming channel queries while earning a 96 percent positive feedback rating by employees (Figure 1).
Business challenge
The problem Deckhand solves is the one every IT team will recognize: the same questions are routinely asked, error messages are posted after business hours, and information needs to be gathered from different teams. At ShipStation Global, those conversations lived in a busy help desk Slack channel, where employees asked, and IT answered, one thread at a time. The answers usually already existed in a Confluence how-to article, on a company intranet page, or in a thread from eight months earlier. Finding them was the hard part.
The channel data made the scale concrete. In the 12 months before launch:
- Employees posted more than 1,500 threads, and volume kept growing.
- With employees in the US, UK, Spain, Poland, Australia, and the Philippines, more than a fifth of questions arrived outside US business hours.
- Answers were split across different places: Confluence articles, intranet pages and PDFs, IT-maintained guides, and the channel’s own history.
- Repetitive questions consumed time that structured self-service steps could have handled.
        “We created Deckhand because getting help should be as simple as asking a question in Slack, not deciphering a ticket form or sending an email into the void. We believe that tickets are an indication of operational friction not productivity. Deckhand resolves common questions on the spot and, when it can’t, converts the conversation into a fully contextualized ticket with one click, improving the employee experience and freeing our team from endlessly repeating the phrase: ‘Please file a ticket.’”
— Chris Collins, Senior Director IT at ShipStation Global
Solution overview
Deckhand works in Slack like any teammate—joining channels, reading the conversation, and drawing context from Slack profiles to answer IT questions in place. We run it on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale, with any framework or model. AgentCore runtime, a capability of Amazon Bedrock AgentCore, hosts the agent in isolated sessions, so we run no servers or containers.
The solution has four main components, shown in Figure 2:
- Slack service: A FastAPI and Slack Bolt application, hosted on AWS App Runner. It receives Slack events, decides whether the bot should respond, and builds a user-context payload from the requester’s Slack profile, including name, email, time zone, and manager.
- Agent service: A Strands agent, deployed as a container on Amazon Bedrock AgentCore runtime, manages the multi-turn tool agent loop using Anthropic’s Claude in Amazon Bedrock.
- Tools and knowledge: A single AWS Lambda function, exposed as Model Context Protocol (MCP) tools through AgentCore Gateway, a capability of Amazon Bedrock AgentCore, classifies requests, creates and updates Jira tickets, and analyzes images. An Amazon Bedrock knowledge base indexes content from Confluence, the company intranet, Slack, and marketing pages, storing it in Amazon Simple Storage Service (Amazon S3).
- Operations and feedback. Amazon DynamoDB stores feedback, AWS X-Ray traces request paths using OpenTelemetry, and the services log to Amazon CloudWatch.
When an employee posts in a channel where Deckhand is a member, the Slack service assembles the full thread history and user context. It then invokes the agent through the AgentCore runtime API. The agent searches the knowledge base and calls tools as needed. When it finds an answer, it returns a final response (Figure 3). When it doesn’t, it asks a clarifying question or offers to create a ticket (Figure 4).
Deckhand workflow
This section walks through how Deckhand is implemented, from prerequisites to a working deployment.
Prerequisites
To implement this pattern, you need the following:
- An AWS account with access to Amazon Bedrock, AgentCore runtime, and AgentCore Gateway.
- A Slack app with event subscriptions, a signing secret, and a bot token scoped to your use case.
- A container image registry such as Amazon Elastic Container Registry (Amazon ECR).
- An Amazon S3 bucket and an Amazon Bedrock knowledge base.
- AWS Identity and Access Management (IAM) roles scoped to each runtime and tool, and AWS Secrets Manager entries for third-party credentials.
Building the agent with Strands Agents and AgentCore
The agent is intentionally lightweight. Using the open source Strands Agents SDK, an agent consists of a model, a set of tools, and a system prompt. The SDK manages the reasoning loop, allowing the model to select tools, process results, and iterate until it produces an answer. Deckhand’s agent service is implemented in a few lines of Python.
The model ID is set through an environment variable, which allows switching models without modifying application code.
Tools are integrated with the agent in two ways. Amazon Bedrock Knowledge Bases retrieval is a native Strands tool that supports knowledge base search with a single import. Other functions, including classification, ticket management, user resolution, and image analysis, are handled by a Lambda function registered on AgentCore Gateway. The Gateway exposes these as MCP tools, and the Lambda routes each invocation by tool name. This separation allows tool logic to be updated independently, and the agent can access new tools from the Gateway without requiring a rebuild.
AgentCore runtime hosts the agent as a container, avoiding the need for server or session management. The Slack service calls the agent synchronously for each message, providing the thread transcript and user context, and posts the final response. Since context, including the employee’s profile, is included with every request, the agent can complete ticket details automatically.
Knowledge base design and answer routing
Deckhand answers from a single Amazon Bedrock knowledge base with core S3-backed data sources:
- Articles synced from Confluence.
- Internal pages, PDFs, and events synced from the company intranet.
- Resolved support threads mined from Slack (covered in the next section).
Each document includes metadata such as title, source URL, content type, and event dates. This allows the agent to filter content, for example, when users ask about upcoming events or weekly lunch menus in the Austin office.
Mining Slack history with Recursive Language Models (RLMs)
The most valuable data source is the archive of resolved support threads. Before Deckhand existed, Slack was where problems got solved: years of employees describing issues and IT walking them through fixes. That history is an organic knowledge base, validated by the best possible reviewer: the person whose problem got fixed. It’s also noisy: a raw export mixes banter, automated alerts, and threads that never actually got resolved. Indexing an unverified fix or a garbled summary means the knowledge base surfaces an incorrect answer with the same confidence as a correct one, so extraction needs to be precise.
The mining process follows a three-stage pipeline (Figure 5):
- A script exports the channel’s full history via the Slack API, retrieving complete replies for every thread and writing a structured dump that includes thread markers, timestamps, and reply counts.
- DSPy’s Recursive Language Model (RLM), running Claude on Amazon Bedrock, treats that export as a navigable memory space inside a sandboxed Python read-eval-print loop (REPL) rather than a single prompt. Working iteratively over the data, it classifies each thread as resolved, unresolved, or escalated and filters out announcements and non-questions. Strict criteria keep quality high: a thread counts as resolved only when the full, workable fix is visible in the thread itself.
- For each resolved thread, the RLM orchestrates recursive sub-LLM (large language model) calls to extract structured fields, each validated against a Pydantic model. The fields include an issue summary, the original question, and the resolution. They also capture whether the fix is self-service or needs a ticket, the self-service steps, the application and system involved, error messages, and tags. When a sub-LLM call returns something that fails the schema, the RLM’s code-based loop catches the validation error in the interpreter and retries. The results are written as a markdown document organized by issue. The pipeline uploads it to Amazon S3 for the knowledge base to index.
We chose RLM because it maintains the entire Slack history in a persistent sandbox variable space, allowing iterative reasoning over the export and consistent output structure. As a result, when an employee encounters a problem previously solved by a colleague, Deckhand provides the proven solution, often as actionable, numbered steps.
Knowing when not to answer
An AI bot in a shared channel fails socially before it fails technically. Deckhand’s most refined logic decides when to stay quiet:
- The agent’s first decision on every message is whether it’s an announcement, a social message, or a conversation between people. If so, it outputs “SKIP,” and the Slack service suppresses the reply.
- In threads, it replies only to the original poster.
- If the last reply came from another human helper, it stays silent, because a person has taken over.
- If a reply starts by @naming a person, the message isn’t for the bot.
Collecting feedback
Each answer includes feedback buttons. A thumbs-up is recorded directly, while a thumbs-down prompts a brief “what went wrong” field. Ratings are stored in DynamoDB with the original question and the bot’s response.
Negative feedback is a valuable dataset used to improve the system prompt and agent behavior, and to update incorrect knowledge base information.
Security and validation
Prompt rules enhance behavior but do not replace access controls. Enforcement is managed through code and infrastructure:
- Ticket creation requires explicit confirmation. When Deckhand offers to create a ticket, the Slack service adds a Create Ticket button, and selecting it sends confirmation through the agent. Ticket updates only accept valid keys matching the helpdesk project pattern and reject empty comments.
- Classification is validated before it acts. Request classification runs as a separate Amazon Bedrock Converse API call that returns structured ticket fields, validated with Pydantic before anything reaches Jira.
- The image tool is restricted to downloading only from Slack’s file host. It authenticates with the bot token, limits each request to five images of up to 5 MB each, and sends the files to a vision model using the Converse API.
- Credentials stay out of code. Slack tokens, the signing secret, and Jira credentials live in AWS Secrets Manager, and each service and tool runs under its own scoped IAM role.
- The prompt enforces behavioral safeguards: never request passwords or multi-factor authentication (MFA) codes, never write credentials in ticket comments, and never expose profile metadata used for ticket fields.
Outcome
Deckhand launched in April 2026. It started at about 30 messages a day and reached as many as 100 by early summer. In its first three months it handled 1,935 messages, started 1,221 agent conversations, and opened 409 Jira tickets. It replied to 97.5 percent of messages. A third of the questions came in after hours, when no one on the IT team was working, and Deckhand answered 94 percent of those. People who would have waited until the next morning got an answer that night.
Feedback improved as the team worked on it. Positive ratings went from 82 percent in April to 96 percent in June, after they revised the system prompt and knowledge base to fix what people complained about.
The clearest win was ticket deflection. An agent conversation is a question that would otherwise have become a Jira ticket. Of the 1,221 conversations, only 409 turned into tickets. The other 812 were handled in chat. Filing a ticket and then working and closing it runs about 30 minutes. Those 812 conversations add up to roughly 406 hours over three months, or around 1,600 hours a year. Employees kept that time for their own work, and IT never spent it on intake.
Conclusion
Deckhand took repetitive IT questions off people’s plates and gave the time back to employees and the IT team. It works because each part of the stack has one job and runs as a managed service: AgentCore runtime hosts the agent, AgentCore Gateway turns a Lambda function into MCP tools the agent can call, and Amazon Bedrock Knowledge Bases handles retrieval. The team shipped it without standing up servers or maintaining orchestration code.
To build a similar solution, begin with a well-maintained knowledge source and a clearly defined action. Refer to the Amazon Bedrock AgentCore documentation and Strands Agents SDK for agent development, and the Amazon Bedrock Knowledge Bases documentation for connecting content sources.
To discuss an agentic AI use case for your organization, contact your AWS account team.
