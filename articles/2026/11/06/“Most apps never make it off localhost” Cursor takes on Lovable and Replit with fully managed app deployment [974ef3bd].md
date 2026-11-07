---
id: "974ef3bd3bfd8c31"
title: "“Most apps never make it off localhost”: Cursor takes on Lovable and Replit with fully managed app deployment"
url: "https://thenewstack.io/cursor-ai-app-deployment"
link: "https://thenewstack.io/cursor-ai-app-deployment"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-06T15:15:21Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Paul Sawers"]
language: "en"
summary: "AI coding agents have certainly made it easier to transform an idea into a working application. However, getting that application off a local machine and into the hands of real users remains a hurdle, requiring essential infrastructure steps spanning everything from hosting and database provisioning, to critical security checks. \n\n Cursor, the AI coding platform acquired by Elon Musk’s SpaceX…"
tags: ["AI", "AI Agents", "Developer tools", "Vibe Coding"]
orgs: ["Cursor", "Tesla"]
topics: ["agents & coding", "products & launches", "chips & infrastructure", "business & funding"]
content_source: "summary"
word_count: 1308
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “Most apps never make it off localhost”: Cursor takes on Lovable and Replit with fully managed app deployment

The New Stack · Paul Sawers · 2026-11-06

AI coding agents have certainly made it easier to transform an idea into a working application. However, getting that application off a local machine and into the hands of real users remains a hurdle, requiring essential infrastructure steps spanning everything from hosting and database provisioning, to critical security checks. 

 Cursor, the AI coding platform acquired by Elon Musk’s SpaceX for $60 billion back in August , acknowledged the problem in an X post published on Thursday. 

 “Agents have made it easier to write code, but most apps never make it off localhost,” the company notes. 

 To address this, Cursor is introducing new app-building and deployment functionality , designed to take AI-generated applications from development to a live, shareable URL, without users having to even think about the underlying infrastructure themselves. 

 “Agents have made it easier to write code, but most apps never make it off localhost.” 

 Built on cloud agents 

 The new feature is built around cloud agents , which Cursor introduced last year as a way for developers to run multiple AI coding agents remotely without having to keep their laptops engaged. At the time, the company highlighted their ability to fix bugs, handle smaller coding tasks and implement some complex features. 

 With this latest update, those same agents can now take applications all the way through to deployment, handling the important steps needed to make them accessible to other users. The functionality is only available through cloud agents, though, which means it can’t be used with agents running locally. 

 Users start by describing the application they want to build in natural language, with Cursor managing the code generation and development process as usual. 

 1. Prompt Cursor as usual 

 From there, the agent creates the application and sets up the underlying project, including the necessary components to get it running. 

 2. Cursor’s agent builds the application 

 Once the application is ready, users can preview the result before deciding whether to hit publish. 

 3. Preview the app before publishing 

 Publishing makes the application accessible through a live URL, allowing users to share it with colleagues or other users without having to configure hosting themselves. 

 4. Share the app via a live link 

 It’s worth noting that there are two ways to get started. Users building an application from scratch will automatically have a new repository created on Cursor Origin , the company’s Git-based code-hosting platform launched in August as an agent-centric alternative to GitHub. 

 Alternatively, users can deploy applications from an existing GitHub repository. This means developers who already have an application under development can use Cursor’s cloud agents to prepare and publish it, without having to move their code to Origin or set up deployment infrastructure manually. 

 Judging by Cursor’s own examples , the feature seemingly targets employees who need to create internal business applications, such as sales dashboards, onboarding programs, customer presentations and developer portals. So in that regard, it could prove a boon for non-developers who have an idea for a tool but lack the technical nous to get it running themselves. 

 Of course, there’s nothing restricting the feature to business applications. An aspiring vibe coder could just as easily create a neighbourhood football league tracker or interactive family holiday planner. And because individual subscribers can publish apps publicly, those creations can be shared with anyone who has the link. 

 Under the hood: hosting, databases and security 

 Cursor had actually begun closing this gap, when in August it introduced the ability to preview cloud-agent projects and publish them to a live URL. However, users still needed to connect their own Vercel accounts. 

 Cursor’s earlier app-building feature, introduced in August 2026. 

 The latest release removes that requirement while introducing various new smarts to the mix. 

 Behind the scenes, Cursor now takes care of several infrastructure requirements, including hosting, databases, and authentication. 

 For hosting, Cursor automatically creates a dedicated account for each team or individual subscriber, isolated from other customers. While Cursor’s announcement doesn’t identify the underlying hosting provider, Vercel revealed in a separate response on X that the new functionality is built on its Vercel for Platforms infrastructure . This basically allows users to deploy applications without having to create their own Vercel accounts or configure hosting themselves. 

 Deploy apps in one click with @cursor_ai . • No account to create • No deployment configuration • Database provisioning included Built on Vercel for Platforms → https://t.co/09OAnq0Q7W https://t.co/SiMHJlOIvD — Vercel (@vercel) November 5, 2026 

 If an application needs a database, Cursor provisions one using PostgreSQL, while private and team applications are protected by Cursor’s existing sign-in system. Individual subscribers can also make their apps publicly accessible. 

 Applications can connect to external services, such as company databases or data warehouses, with users supplying the necessary credentials. Cursor says these secrets are managed separately, meaning the AI agent never sees their actual values. 

 Then there’s the thorny issue of security. When users choose to publish an application, Cursor says it runs “a series of deterministic and agentic security checks” before allowing it to go live. These include mandatory checks for exposed credentials, secrets and sensitive files, alongside an AI-powered review intended to identify more serious vulnerabilities. 

 However, it’s unclear how reliably these automated checks can identify more complex problems, such as incorrectly configured database permissions or application-level access controls. This is an important consideration for organisations contemplating connecting AI-generated applications to sensitive internal systems, where additional security scrutiny would still be advisable. 

 There is precedent for such concerns, too. In May last year, Semafor reported that two Replit employees examined 1,645 Lovable-built applications and discovered that 170 of them exposed sensitive information. The problems involved incorrectly configured database permissions, highlighting the difficulties of securing applications created through AI tools. Lovable says it subsequently introduced further security checks to identify potential vulnerabilities before applications are published. 

 Cursor moves onto Lovable and Replit’s turf 

 Of course, Cursor is entering territory already occupied by the likes of Lovable and Replit , which allow users to create and publish applications through natural-language prompts. 

 While Cursor’s latest announcement emphasizes internal business tools, Lovable and Replit have traditionally appealed to a broader audience of aspiring application creators. Still, the overlap is clear, and Cursor’s move into deployment has already caught the attention of developers. 

 “Cursor just came for the localhost graveyard.” 

 One software engineer writes on X that “ cursor just came for the localhost graveyard ,” riffing on Cursor’s own messaging about AI-generated applications that never make it beyond local development. 

 There’s also an interesting overlap with Grok Build , particularly given SpaceX’s acquisition of Cursor in August. 

 SpaceXAI introduced Grok’s Build Mode in July , before expanding it to all Grok plans the following month . The feature allows users to create apps, games and websites directly inside a Grok conversation, then publish them to shareable grok.me links. 

 That bears something of a resemblance to Cursor’s latest offering, although Cursor is approaching it through its established coding environment and cloud agents, and with a stronger emphasis on business applications and managed infrastructure. 

 The overlap hasn’t gone unnoticed though. One X user responded to Cursor’s announcement by asking, “ so cursor is now properly replacing grok build ?” 

 There’s no indication that Grok Build is being replaced, but the two offerings now cover some notably similar ground, raising questions about how SpaceXAI intends to distinguish them going forward. 

 For those wanting to check out Cursor’s new functionality, it’s available on all paid Cursor plans with cloud agents enabled. 

 With deployment increasingly becoming part of the AI coding experience, Cursor’s latest move could put further pressure on dedicated app-building platforms as the distinction between tools aimed at professional developers and those targeting aspiring vibe coders continues to narrow. 
 The post “Most apps never make it off localhost”: Cursor takes on Lovable and Replit with fully managed app deployment appeared first on The New Stack .
