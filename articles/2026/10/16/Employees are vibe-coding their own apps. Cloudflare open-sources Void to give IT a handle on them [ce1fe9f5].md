---
id: "ce1fe9f525bbc56e"
title: "Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them"
url: "https://thenewstack.io/cloudflare-voidzero-void-vibe-coding"
link: "https://thenewstack.io/cloudflare-voidzero-void-vibe-coding"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-16T12:16:01Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Many companies are keen to let employees build their own applications using AI, even those with little or no programming experience. Just yesterday, Gergely Orosz of The Pragmatic Engineer highlighted the likes of Ramp and Stripe , which have developed internal tools that allow non-engineers to create software for their colleagues to use. \n\n But this newfound freedom also creates a headache for…"
tags: ["AI", "JavaScript", "Platform Engineering", "Vibe Coding"]
orgs: []
topics: ["business & funding", "models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1379
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them

The New Stack · Paul Sawers · 2026-10-16

Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them
Many companies are keen to let employees build their own applications using AI, even those with little or no programming experience. Just yesterday, Gergely Orosz of The Pragmatic Engineer highlighted the likes of Ramp and Stripe, which have developed internal tools that allow non-engineers to create software for their colleagues to use.
But this newfound freedom also creates a headache for IT departments. Who tracks these applications, what company data can they access, and who’s responsible for ensuring they’re secure? In many regards, vibe-coded apps are the new shadow IT, with employees deploying software beyond the oversight of their IT teams.
And that’s why Cloudflare wants to bring some order to proceedings. On Thursday, the company announced the release of Void, a collection of three open-source tools that includes a self-hosted platform where companies can deploy and manage their employees’ AI-built applications. The idea is to give staff somewhere to publish their wares, all the while letting admins control who can deploy and access them.
Cloudflare’s growing JavaScript empire
Cloudflare has compiled quite the collection of JavaScript expertise over the past year. Just last week, the company announced its acquisition of Deno, the company behind the JavaScript runtime founded by Node.js creator Ryan Dahl. And way back in January, it snapped up the team behind Astro, the open-source web framework. Then in June, it acquired VoidZero, the open-source tooling company founded by Vue.js and Vite creator Evan You.
All three operate within the JavaScript ecosystem, albeit with different specialties spanning web frameworks, development tooling, and server-side runtimes.
You formally unveiled VoidZero in October 2024, with a founding mission to bring together the disparate tools developers rely on when writing JavaScript. It already had considerable open-source pedigree, with its team contributing to established projects such as Vite and the Vitest testing framework, alongside developing the Rust-based Rolldown bundler and Oxc, a collection of tools for processing and analyzing JavaScript code.
In October 2025, VoidZero announced Vite+, an effort to bring its various development tools together under a single command-line interface (CLI). Originally conceived as a commercial offering, Vite+ was eventually released as open source under the MIT license in March, while that same month, the company also introduced Void, an early-access deployment service for Vite applications, which it hoped would provide a way to generate revenue from its open-source ecosystem.
“We started working on Void before the acquisition, originally intended to make it a commercial product. But now we no longer need to, so we’ve made it open source!”
Since the Cloudflare acquisition, Vite+ has continued to develop, reaching beta over the summer before its stable 1.0 release at the tail-end of September. But the biggest change, arguably, has been to Void, with Cloudflare’s ownership prompting a rethink of how the deployment platform would be offered. Indeed, the acquisition has eased the pressure on VoidZero to find its own sources of revenue, something You acknowledged on X following Thursday’s announcement.
“We started working on Void before the acquisition, originally intended to make it a commercial product,” You writes. “But now we no longer need to, so we’ve made it open source!”
Into the void: Full-stack apps via Vite
Void comprises three main components, each serving a different purpose. The Void SDK provides the building blocks for creating full-stack applications with Vite, including server-side functionality and integrations with databases and other services. The Void CLI, meanwhile, handles deployment, automatically provisioning the necessary Cloudflare resources, while Void Platform provides a shared environment where companies can host applications and manage them through an administrative dashboard.
The SDK and CLI were already distributed through npm under the MIT license, but Thursday’s release makes the full source code, including the platform, publicly available alongside Void 1.0.
Running void deploy initiates the application build, provisions the required infrastructure, and publishes the finished application to Cloudflare, including applying any necessary database migrations.
The self-hosted platform represents a significant departure from VoidZero’s original plans. Michael Dong, who joined Cloudflare from VoidZero and is now a strategy lead at the company, says the acquisition prompted a substantial overhaul of the technology.
“After the Cloudflare acquisition of VoidZero, we rebuilt the platform from the ground up to work as a self-hosted platform that anyone can install and self-host on Cloudflare.”
“After the Cloudflare acquisition of VoidZero, we rebuilt the platform from the ground up to work as a self-hosted platform that anyone can install and self-host on Cloudflare,” Dong tells The New Stack.
Companies can install their own instance using the void platform install command, which guides administrators through setting up authentication, database connections and storage.
The original Void Cloud service, meanwhile, remains in operation privately. Christoph Nakazawa, formerly a product lead at VoidZero and now director of engineering at Cloudflare, says access has been limited to the company’s own team and a small group of invited testers.
“It was never made publicly available,” Nakazawa tells The New Stack.
Dong also says more than 100 beta users have deployed applications through the Void SDK, although he didn’t specify whether they used Void Cloud or deployed directly to Cloudflare.
Keeping employees’ apps in check
Void Platform gives administrators the ability to determine who can deploy applications and who can access them. They can also inspect deployments, review logs, monitor resource consumption and impose usage limits. Integration with identity providers and Cloudflare Access allows companies to restrict applications to authorised employees.
Void also provides tools for troubleshooting applications after deployment. Developers can inspect error logs through the CLI and roll back problematic deployments to earlier versions.
Dong says Cloudflare is already using Void Platform internally, with corporate authentication providing a measure of protection against employees inadvertently exposing company information.
“We have a Void Platform at Cloudflare that is only accessible to employees, preventing data leaks through vibe coded apps by default,” Dong says.
There are limits to this protection, however. Restricting access to an application doesn’t necessarily prevent that application from retrieving sensitive information or sending it elsewhere. Moreover, Void’s documentation confirms that administrators can configure new applications to be public by default, while individual project owners can subsequently make their own applications publicly accessible.
Void’s documented deployment process also contains no mandatory IT security review before an application goes live. Asked specifically whether administrators can review or approve applications before deployment, Nakazawa points to the platform’s existing access controls and the freedom companies have to extend them.
“Since Void is open source, other companies can adjust the platform to their needs.”
“Since Void is open source, other companies can adjust the platform to their needs,” Nakazawa says.
That could mean developing additional approval mechanisms or more restrictive access policies, though organizations would have to implement those measures themselves.
There is also the matter of cost. Companies self-hosting Void Platform require a paid Cloudflare Workers for Platforms plan, which starts at $25 per month, with additional charges depending on usage. The installation also requires R2 storage and a separately hosted PostgreSQL database, bringing further potential expenses.
Dong confirms that developers using the Void SDK to deploy applications directly to Cloudflare don’t need a paid Cloudflare plan. However, companies hoping Cloudflare will operate their Void Platform for them are out of luck for now, with no fully managed version currently available.
For Cloudflare, then, there’s a potential commercial upside to making Void open source. While the software itself is freely available, companies running their own Void Platform will consume Cloudflare infrastructure, with all the associated costs. In effect, Cloudflare stands to benefit from wider adoption of the software through the underlying services that power it.
And those infrastructure requirements raise another question: how closely tied to Cloudflare will Void remain? Cloudflare has pledged to keep Vite and VoidZero’s other established development tools vendor-neutral, while Void’s automatic infrastructure provisioning currently depends on Cloudflare. Nakazawa says this reflects the platform’s origins, with Void having been designed around Cloudflare’s infrastructure from the outset.
That may change as the open-source project develops, although Nakazawa stopped short of committing to support for competing cloud providers.
“Now that it’s open source, we look forward to working with the community to provide support for additional providers that offer the same baseline capabilities,” Nakazawa says.
