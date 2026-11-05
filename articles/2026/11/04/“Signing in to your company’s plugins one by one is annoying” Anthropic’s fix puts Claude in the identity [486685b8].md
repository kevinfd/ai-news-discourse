---
id: "486685b8723d52a3"
title: "“Signing in to your company’s plugins one by one is annoying”: Anthropic’s fix puts Claude in the identity business"
url: "https://thenewstack.io/claude-plugin-identity-issuer"
link: "https://thenewstack.io/claude-plugin-identity-issuer"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-04T16:59:22Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Anthropic is now letting businesses automatically connect employees to approved Claude plugins, saving staff from having to sign in to and authorize each service individually. The feature also allows Claude to verify users’ organizational membership directly, making it easier for companies to manage access to workplace applications. \n\n The feature builds on the Enterprise-Managed Authorization (…"
tags: ["AI", "AI Agents", "Model Context Protocol (MCP)", "Security"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "summary"
word_count: 959
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “Signing in to your company’s plugins one by one is annoying”: Anthropic’s fix puts Claude in the identity business

The New Stack · Paul Sawers · 2026-11-04

Anthropic is now letting businesses automatically connect employees to approved Claude plugins, saving staff from having to sign in to and authorize each service individually. The feature also allows Claude to verify users’ organizational membership directly, making it easier for companies to manage access to workplace applications. 

 The feature builds on the Enterprise-Managed Authorization ( EMA ) extension to the Model Context Protocol (MCP), which debuted back in June. As The New Stack reported at the time , this ushered in a way for companies to manage MCP connections centrally through their existing identity providers, with Okta becoming the first to support it. 

 Anthropic also announced support for the extension in Claude, Claude Code and Cowork on the same day, and published implementation guidance for developers building compatible MCP servers. 

 In its original guise, the approach relied on the company’s identity provider being compatible with EMA. Okta was the first to support the extension, and adoption among other providers remains limited, meaning many organizations have still had to authorize connections individually. 

 “Claude itself can issue the signed identity assertions that participating MCP services use to recognize employees.” 

 On the ClaudeDevs X account on Tuesday, Anthropic introduced another option : Claude itself can issue the signed identity assertions that participating MCP services use to recognize employees. This effectively means businesses can enable automatic connections without requiring their identity provider to support the extension. 

 “If you’re building plugins for Claude, add support so users get started faster and stay connected without re-authorizing,” the company writes. 

 The new Claude authorization feature is available in beta now, for Team and Enterprise customers. 

 Claude takes over the identity check 

 Taking to X on Tuesday, Boris Cherny , head of applications at Anthropic, points to the frustration of employees having to repeatedly authenticate workplace applications. 

 “Signing in to your company’s plugins one by one is annoying.” 

 “Signing in to your company’s plugins one by one is annoying, so we let Claude auto-connect to them now,” Cherny writes . 

 Signing in to your company's plugins one by one is annoying, so we let Claude auto-connect to them now. Team and Enterprise admins can set them up, and teammates are connected automatically the first time they use the plugins. https://t.co/w2oxw0bKOZ — Boris Cherny (@bcherny) November 3, 2026 

 Administrators can choose which supported services to enable, and which employee roles should receive access. For example, a company might be comfortable giving all employees access to a general-purpose productivity tool, while restricting access to more sensitive systems, such as company databases, to specific roles because of the risks associated with exposing confidential information or making unauthorized changes. 

 When an eligible user opens a plugin, Claude sends a signed assertion identifying them as a member of the organization. The receiving service checks that assertion before providing an access token. 

 The process also handles subsequent connections automatically, so users don’t have to repeatedly authorize the same service when tokens expire. 

 The initial rollout spans a broad array of more than a dozen services, including Amplitude, Apollo.io, Atlassian, Datadog, Dropbox, Figma, Granola, HubSpot, Linear, Mixpanel, Notion, PagerDuty, Semrush, and Supabase. 

 14 services have signed up to Claude’s auto-connect plugins at launch. 

 In a November 3 blog post , Supabase explained that customers can now use Claude to authenticate employees accessing its MCP server, even if their identity provider lacks EMA support. 

 Indeed, the company points specifically to the limited adoption of the extension among enterprise identity providers as a key obstacle that the new feature addresses. 

 “Okta was the only identity provider that supported the extension at launch and most still don’t,” Supabase writes. “Organizations on those providers no longer have to wait because Claude can now be the issuer instead.” 

 To configure the connection, a Supabase administrator first approves Claude for the organization. An administrator then selects Claude-issued authorization in Claude’s connector settings, registers the unique issuer URL in Supabase, tests the connection and enables access for the relevant employee roles. 

 Authorizing Claude to access Supabase. 

 It’s worth noting that employees must already have a matching Supabase SSO account, and their existing permissions determine what they can access. The company also cautions that removing someone from the company’s identity provider alone will not revoke Claude-issued access, and administrators must remove departing employees from both Claude and Supabase. 

 Claude as an identity provider? 

 The upshot of all this is that Claude is now taking on a role traditionally handled by enterprise identity providers, vouching for users when they access third-party services. While it’s still early days, and the feature is currently limited to those in the business realm, the announcement has already prompted some positive reactions. 

 “Tired of reauthorizing in every other session.” 

 “This is soo good, tired of reauthorizing in every other session,” one user writes on X . 

 Others are keen to see more companies support the feature, with one eager for payments giant Stripe to join the party. “I spend more time reconnecting Stripe than every other plugin combined,” the user writes . 

 The implications for enterprise authentication also caught people’s attention. “Claude becoming an identity provider,” one user remarked , raising a broader question about Anthropic’s growing role in verifying user identities. 

 Technically, Claude is acting as a trusted issuer for participating MCP services, verifying that users belong to a particular Claude organization. It doesn’t provide the full range of functions associated with a traditional identity provider, and connected services remain responsible for enforcing their own access permissions. 

 So for now, Claude’s identity ambitions extend only as far as the services willing to take its word for who you are. 
 The post “Signing in to your company’s plugins one by one is annoying”: Anthropic’s fix puts Claude in the identity business appeared first on The New Stack .
