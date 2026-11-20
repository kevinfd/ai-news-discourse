---
id: "f9911b0047a5f7c1"
title: "Show HN: AgentMall – Let your AI agent buy groceries"
url: "https://getagentmall.com"
link: "https://getagentmall.com"
source: "getagentmall.com"
domain: "getagentmall.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-19T16:46:14Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["desilva78_"]
language: "en"
summary: "Hey HN, we’re Nel and Kosi. We noticed personal agents like Instinct, Muse were terrible at buying stuff. Most of the time the checkout would fail. So we built reliable automations for agents to checkout at 9 leading grocery merchants. We grapple with anti bot, logins, OTP codes, and changing checkout structures. Loved revisiting this stuff given our backgrounds sneaker-botting and building…"
tags: []
orgs: []
topics: ["agents & coding", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 512
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50562508"
score: 19
comments: 6
community: "Hacker News"
---

# Show HN: AgentMall – Let your AI agent buy groceries

getagentmall.com · desilva78_ · 2026-11-19

Reorder by text
Your shopper asks in plain words. Your agent finds the items, builds the basket and checks out.
One unified API for discovery, checkout and fulfilment across hundreds of merchants.
Book a call
- Target
- Best Buy
- Kroger
- The Home Depot
- Shopify
- 01 Your agents call one API Every user's agent searches, builds baskets and checks out over REST or MCP.
- 02 Every purchase is approved Approval binds to the exact basket and a spending ceiling.
- 03 Credentials stay in the vault Merchant logins and the customer profile are used at checkout and never reach the model.
- 04 One commit per approval The checkout runtime places the order once. An uncertain submission is reconciled, never retried blind.
- 05 The receipt comes back Order confirmation and totals return to your agent.
One API, from the first search to the order receipt.
Live prices and stock from each store, every result ready for the cart.
Checkout is bound to the reviewed items and total.
When a store asks for a code, your agent asks your shopper.
Status comes back after checkout.
Plug in the agent you already use, or call the API from your own backend.
MCP for coding and chat agents
RESTapi.getagentmall.com for your backend
A model that decides every click sounds general-purpose. At checkout, general-purpose fails in ways you can't afford.
- Bot protection
  - Browser agent
  - Flagged as generic browser automation before the session starts.
  - AgentMall
  - A merchant-specific flow, monitored per merchant, gets through to checkout.
- Placing the order
  - Browser agent
  - An unsure ‘place order’ click can mean a double charge.
  - AgentMall
  - An uncertain order is checked with the merchant, never retried blind.
- Speed and cost
  - Browser agent
  - A vision model decides every click, adding seconds and tokens to every step.
  - AgentMall
  - The same flow runs in a fraction of the time at a fraction of the cost.
- Credentials
  - Browser agent
  - The agent holds your login and card in a full browser session.
  - AgentMall
  - Credentials stay in a vault and are never exposed to the model.
We handle the messy maintenance underneath.
- Merchant-specific checkout Every merchant has its own monitored flow, so your agent gets through where generic browser automation is blocked. Live at 9 storesRead the docs
- Credentials in a vault Use our managed vault, or bring your own, such as 1Password. Logins never reach the model. Managed vault includedRead the docs
- A virtual card per agent Your users never hand their own card to an agent. Card numbers stay in the vaultRead the docs
- Spending limits Approval binds to the exact basket and a spending ceiling. Bound to the reviewed totalRead the docs
- No double charges An uncertain order is checked with the merchant before anything is tried again. One commit per approvalRead the docs
- Affiliate revenue Earn on every order your agent places, with no extra integration. Revenue share on every orderSee pricing
