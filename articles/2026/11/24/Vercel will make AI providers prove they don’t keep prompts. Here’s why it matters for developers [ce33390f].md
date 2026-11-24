---
id: "ce33390feaad5122"
title: "Vercel will make AI providers prove they don’t keep prompts. Here’s why it matters for developers."
url: "https://thenewstack.io/vercel-audited-zdr-inference"
link: "https://thenewstack.io/vercel-audited-zdr-inference"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T12:00:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Luke James"]
language: "en"
summary: "Since April, developers using Vercel’s AI Gateway have been able to request provider-level zero data retention (ZDR). Vercel says its existing provider-level ZDR routing relies on providers’ policies and agreements with the company; the new tier adds a requirement for published independent audits.  \n\n On Monday, Vercel announced Audited ZDR , a tier that will admit providers only after…"
tags: ["AI Infrastructure", "Compliance", "Security"]
orgs: ["Amazon", "China"]
topics: ["models & research", "agents & coding", "policy & regulation", "chips & infrastructure"]
content_source: "summary"
word_count: 1213
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Vercel will make AI providers prove they don’t keep prompts. Here’s why it matters for developers.

The New Stack · Luke James · 2026-11-24

Since April, developers using Vercel’s AI Gateway have been able to request provider-level zero data retention (ZDR). Vercel says its existing provider-level ZDR routing relies on providers’ policies and agreements with the company; the new tier adds a requirement for published independent audits.  

 On Monday, Vercel announced Audited ZDR , a tier that will admit providers only after independent security firms test their retention claims against their code, infrastructure, and live traffic and publish the reports. Vercel says a planned team-wide toggle will restrict routing and failover to providers with qualifying published audits. The announcement does not give a separate general-availability date for the toggle. 

 Vercel says launch partners Baseten , Modal , and Wafer have begun their audits, with reports expected by December 8. Each provider will enter the tier once its qualifying report is published.  

 The announcement follows research published November 19 by industrial cybersecurity firm Dragos , which sent about 2 million prompts containing trackable credentials and URLs to AI services. Vercel’s announcement does not cite that research. On Sunday, OpenRouter said it’d removed three providers and stripped 125 endpoints of their ZDR eligibility as a result. 

 Singing like a canary 

 Dragos’s prompts carried canary tokens: AWS keys (real ones, tied to empty, fully logged accounts) and unique links that alert whoever planted them when they’re subsequently used. The company says that data from “at least three AI providers was exposed,” and none of the three knew until Dragos told them.  

 The company says that data from ‘at least three AI providers was exposed,’ and none of the three knew until Dragos told them. 

 Dragos also reported cases in which privacy settings appeared not to be honored. 

 According to Chief Research Officer HD Moore , an unnamed Chinese AI lab’s systems fetched unique URLs from more than half the prompts sent to its models between July and October, including roughly two-thirds of requests marked for no data collection or ZDR. Moore attributes such failures to deliberate practices or processing bugs; those findings do not establish that every provider ignores ZDR settings. 

 Routers can add further intermediaries between an application and the provider running a model, complicating the task of tracing where prompts go. “Some routers are open marketplaces where the seller with the lowest price gets the request,” Moore writes, and a privacy flag “only binds the first hop.”  

 Vercel has also offered free stealth models, including Cat Jam , but its announcement explicitly said ZDR was unavailable and prompts could be retained for safety reasons. 

 OpenRouter, which Stripe agreed to buy in August , published a notice Sunday. It says it off-boarded three providers, pulled 125 endpoints from ZDR eligibility (some purely as a precaution), and notified affected customers. The notice does not identify the three off-boarded providers. It separately links to statements from Atlas Cloud, Novita, Phala, and Together, without identifying them as the three removed providers. 

 OpenRouter says the findings did not show a breach or unauthorized access of OpenRouter itself. The providers’ statements describe different issues: Atlas Cloud and Novita discuss upstream MiniMax request handling, while Phala and Together describe security incidents.  

 It’s also planning to run its own Dragos-style canary tests, “adapting the researchers’ testing approach so we can run these checks on an ongoing basis,” and will require validation before any endpoint gets ZDR status back.  

 Receipts, not promises 

 In its Audited ZDR announcement, Vercel says contracts and self-attestation aren’t enough for proprietary code or regulated data. It asks, among other things, whether prompts end up in debug logs or crash dumps, and whether support tools can find them. Vercel presents Audited ZDR as the next step after April’s team-wide ZDR and its own ISO/IEC 42001:2023 certification.  

 Vercel says contracts and self-attestation aren’t enough for proprietary code or regulated data. 

 An audit would cover everything from request logs, traces, and crash dumps to prompt caches and support tools. The audit would also cover any training, fine-tuning, or eval datasets. To qualify for the audited tier, a provider must also demonstrate that ZDR requests do not fail over to non-ZDR endpoints, tools, or features.  

 Auditors review the provider’s serving-path source code and infrastructure configuration, then send marked prompts through the gateway and search logging, caching, and storage systems for traces. Published reports must disclose exceptions and fix status, with redactions limited to exploit detail. 

 Vercel is also running its own canaries . The gateway creates unique URLs connected to a model, slips them into ZDR-flagged prompts, and logs any request that comes back.  

 “Any request to a canary URL triggers an investigation into the provider and model involved,” a Vercel spokesperson tells The New Stack . 

 “Any request to a canary URL triggers an investigation into the provider and model involved,” a Vercel spokesperson tells The New Stack , though “a URL fetch does not by itself establish that a provider retained data.”  

 The canaries have limits, and Vercel says so: they can’t detect prompts written to disk and never read. Independent audits examine a provider’s systems at a point in time; canaries add monitoring between audits. Neither should be presented as an unconditional guarantee against future breaches. 

 Where your prompts end up 

 Teams can already use ZDR either per request ( zeroDataRetention: true in providerOptions.gatewa y ) or through the team-wide setting, which costs $0.10 per 1,000 requests. Both require a Pro or Enterprise plan or purchased AI Gateway credits. The planned Audited ZDR tier would further restrict routing to providers with qualifying published audits. Its announcement does not specify a separate surcharge. 

 Existing ZDR also has scope limits: provider-run tools and short-lived prompt caches can be treated differently under provider policies, so teams should check what their chosen route covers.  

 With open-weight models, the inference host may be a different company from the model developer, so teams need to check who actually processes their requests; open-weight models handled 56% of tokens on Vercel’s gateway in August .  

 Coding agents add another potential exposure: their requests can include credentials and other sensitive material available in their context. Dragos recommends choosing upstream providers explicitly rather than accepting a router’s default pool.  

 Dragos also recommends planting canaries as an additional detection measure. Separately, Vercel’s gateway offers routing controls: teams can filter routing by the country where a provider’s parent company is headquartered, or pin inference to the US, Europe, Australia, or Japan. Provider headquarters and inference location are separate controls.  

 Vercel’s announcement does not name the firms auditing the three launch partners, though each report is to be published under its auditor’s name. Each provider “engages an independent security firm to run the audit,” the spokesperson said.  

 “The firm then tests the provider’s zero data retention policy across the serving path for every model, endpoint, feature, and tool that handles AI Gateway traffic.” The announcement does not specify when other existing ZDR providers might join the audited tier. Providers engage the independent firms; Vercel is not describing audits conducted by its own staff.  

 Vercel says it expects the launch partners’ audit reports by December 8. That is an expected report-publication date, rather than a confirmed general-availability date for the entire tier.  
 The post Vercel will make AI providers prove they don’t keep prompts. Here’s why it matters for developers. appeared first on The New Stack .
