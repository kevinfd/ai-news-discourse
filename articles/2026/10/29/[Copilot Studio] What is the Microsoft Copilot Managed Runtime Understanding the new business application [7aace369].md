---
id: "7aace36994813fb2"
title: "[Copilot Studio] What is the Microsoft Copilot Managed Runtime? Understanding the new business application execution platform for the Copilot era #0395"
url: "https://note.com/kagen_shin/n/ncbc4b9b3f707?hl=en"
link: "https://note.com/kagen_shin/n/ncbc4b9b3f707?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-29T02:59:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Shinichi Kawara"]
language: "en"
summary: "In the world of Microsoft 365, the options for \"building apps\" using Copilot are increasing rapidly.There are ways to build apps from natural language, ways to use Microsoft Copilot Studio, and ways ..."
tags: []
orgs: ["Microsoft"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1437
paywalled: false
image: "http://www.bing.com/th?id=ONUT.PsX6wY4w_rQtXrq_vOofkg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [Copilot Studio] What is the Microsoft Copilot Managed Runtime? Understanding the new business application execution platform for the Copilot era #0395

note · Shinichi Kawara · 2026-10-29

[Copilot Studio] What is the Microsoft Copilot Managed Runtime? Understanding the new business application execution platform for the Copilot era #0395
In the world of Microsoft 365, the options for "building apps" using Copilot are increasing rapidly.
There are ways to build apps from natural language, ways to use Microsoft Copilot Studio, and ways to develop primarily with code.
This is where it becomes important to consider:
That is the point.
One answer to that is what I will introduce this time: Microsoft Copilot Managed Runtime.
Note that as of the time of writing this article, it is a preview feature. Microsoft's documentation also explicitly states that it is pre-release documentation and is subject to change in the future.
What is Copilot Managed Runtime
Microsoft Copilot Managed Runtime is a runtime environment for hosting Microsoft 365 business applications.
The point is not simply that it can "run apps."
The created apps are executed in an environment hosted by Microsoft, and a major feature is that they can utilize Microsoft Entra authentication, organizational governance policies, and security and compliance controls.
In other words,
the mechanism for building apps
and
the mechanism for securely executing and managing apps
are easier to understand if you think of them separately.
Copilot Managed Runtime can be thought of as the common foundation that handles the latter.
"Copilot Managed Runtime is not an app creation tool"
This is a point I want to clarify first.
It becomes a bit confusing if you understand Copilot Managed Runtime itself as an "app creation tool" like Microsoft Copilot Studio.
Microsoft Learn currently outlines four ways to create apps that run on the Copilot Managed Runtime.
1. Copilot Cowork
You can describe the app you want to create in a chat and build it.
The primary target audience is business users who want to work primarily through chat. You can create apps by requesting them from Cowork or by using the app builder.
2. Microsoft Copilot Studio
In Microsoft Copilot Studio, you can build apps from natural language instructions or existing data.
The process involves Copilot Studio proposing a creation plan, generating a draft, and then adjusting it in an interactive preview before publishing and sharing.
3. Copilot Code
With Copilot Code, you can build apps using AI coding agents.
A distinctive feature is that, in addition to cloud sessions, a more code-oriented development workflow using Copilot Code locally is also available. 
* Although Microsoft Learn provides instructions for running it locally, the local execution feature is not available in my environment. I believe it is being updated periodically, so if it is not available in your environment, please wait for a while.
4. SDK / CLI
Furthermore, for professional developers, the Copilot Managed Runtime SDK and CLI are provided.
The official documentation introduces the @microsoft/managed-apps SDK and @microsoft/managed-apps-cli, and the CLI is used as the ms command.
This allows you to scaffold, build, and deploy apps from the command line.
Different ways to build, same destination
This is the key point to emphasize in this article.
In Microsoft Learn,
- Cowork
- Copilot Studio
- Copilot Code
- SDK / CLI
It is explained that these four paths generate the same type of artifacts.
And those apps run on the Copilot Managed Runtime.
In other words,
There are multiple ways to create them. However, the execution and management platform can be unified.
Isn't this extremely important for understanding the Copilot Managed Runtime?
It is not just a mechanism for those who build apps
The interesting thing about the Copilot Managed Runtime is that it is not aimed only at developers.
Microsoft connects
- users
- makers / business users
- developers
- administrators
within the same mechanism.
Users
Available apps can be searched for and executed from the Copilot Managed Runtime portal.
Regardless of how the app was created, the entry point for users can be unified.
Makers / Developers
Makers and developers can choose the method that is appropriate for them.
You can choose between Cowork or Copilot Studio for natural language-centric development, Copilot Code for development using AI coding agents, or SDK / CLI for code-first development.
Administrator
Administrators can view Copilot Managed Runtime apps within their tenant from the Microsoft 365 admin center.
The official documentation explains management features such as centralized inventory, usage analytics, operational health, and lifecycle management.
The "SDK / CLI" that intermediate users should pay attention to
For engineers accustomed to low-code development with tools like Power Platform, the existence of the SDK / CLI is particularly interesting.
The Copilot Managed Runtime SDK allows for app development using JavaScript / TypeScript, and Microsoft Learn explains that you can utilize connectors to over 1,500 data sources.
Furthermore, as a local development environment, you use:
- Your preferred IDE. For example, Visual Studio Code
- Node.js
- Git
- Git Credential Manager
- Microsoft Copilot Managed Runtime CLI
and so on.
The CLI can be installed via npm.
npm install -g @microsoft/managed-apps-cli
After installation, you can check the CLI with:
ms --version
to verify it.
At this point, it is clear that this is quite different from so-called no-code / low-code app creation, and has become a development experience closer to general software development.
What kind of structure is it using internally?
Let's look at it from a more technical perspective.
In the architecture documentation published by Microsoft, the components of Copilot Managed Runtime are described as follows:
- Copilot Managed Runtime SDK
- Copilot Managed Runtime CLI
- Models and services generated for connectors
- ms.config.json
- Git repository
- Copilot Managed Runtime host
and so on.
As for the apps to be developed, a TypeScript or JavaScript SPA is assumed.
Projects created by the CLI include the SDK, and you use the CLI and SDK to connect to connectors and deploy to the Copilot Managed Runtime.
Furthermore, the fact that the Git repository is considered the Single Source of Truth is a point that developers should take note of.
Governance, which is important for enterprise use
In app development for the Copilot era, "being easy to build" is not enough.
As the number of people who can build apps increases,
how to manage those apps
becomes important.
In Copilot Managed Runtime, compliance with organizational IT policies—such as authentication and authorization via Microsoft Entra, sharing restrictions, Conditional Access, Advanced Connector Policies, and DLP—is described as an official feature.
Microsoft also describes the following as an assumed scenario:
- Personal productivity apps
- Team productivity apps
- Enterprise apps
This indicates the stages.
The goal is to handle everything from small apps created by individuals to apps used by the entire organization under the same governance framework.
I believe this is where the importance of Copilot Managed Runtime lies.
Key points for those experienced with Power Platform
If you are familiar with Power Platform,
"Since Copilot Studio already exists, why is a new runtime necessary?"
You might wonder about this.
Here, it is important not to think of Copilot Studio and Copilot Managed Runtime as competing products.
In Microsoft's current architecture, Microsoft Copilot Studio is positioned as one of the entry points for creating apps that run on the Copilot Managed Runtime.
Therefore,
it is not a choice between Copilot Studio or Copilot Managed Runtime
but rather,
it is easier to understand if you view it as a relationship where you create with Copilot Studio and execute/manage with Copilot Managed Runtime
as this relationship makes it easier to understand.
Summary
Microsoft Copilot Managed Runtime is not just a new app development tool.
To summarize the key points of this session,
- Copilot Managed Runtime is the foundation for hosting Microsoft 365 business applications
- There are four creation paths: Cowork, Copilot Studio, Copilot Code, and SDK / CLI
- Even if the creation method differs, they can be treated as common applications running on the Copilot Managed Runtime
- You can use Microsoft Entra authentication and organizational governance policies
- They can be centrally managed from the Microsoft 365 admin center
- Code-first development using SDK / CLI is also possible
- As of October 28, 2026, it is a preview feature
This is how the mechanism works.
If Copilot lowers the barrier to creating apps, the next challenge will be 'how to safely execute and manage the large number of apps created'.
In that sense, I think Copilot Managed Runtime is a feature to keep an eye on in the future as a foundation that connects app creation in the Copilot era with Microsoft 365 enterprise governance.
Isn't this an important point to consider when looking at Copilot Managed Runtime?
