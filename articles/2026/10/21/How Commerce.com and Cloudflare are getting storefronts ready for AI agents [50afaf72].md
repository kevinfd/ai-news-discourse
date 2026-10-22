---
id: "50afaf72bfb9fbf4"
title: "How Commerce.com and Cloudflare are getting storefronts ready for AI agents"
url: "https://blog.cloudflare.com/webmcp-commerce"
link: "https://blog.cloudflare.com/webmcp-commerce"
source: "Cloudflare Blog"
domain: "blog.cloudflare.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-21T13:00:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Jenny Lea", "Max Brosnahan", "Matthew Conroy"]
language: "en"
summary: "AI can write code and pass the bar exam, but it still struggles to buy a pair of shoes online. That’s because websites were built for humans, not agents. Most agents that shop for someone today work from a site’s HTML — they look at the page, guess which button does what, click, and try again when they get it wrong. This process is slow, uses a lot of tokens, and something as seemingly innocuous…"
tags: ["Agents", "AI", "eCommerce", "WebMCP"]
orgs: ["Google"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 1158
paywalled: false
image: "https://blog.cloudflare.com/_emdash/api/media/file/01M5AYSA5Z4MMJ6XYBSMECP05T.png"
discussion_url: null
score: null
comments: null
community: null
---

# How Commerce.com and Cloudflare are getting storefronts ready for AI agents

Cloudflare Blog · Jenny Lea, Max Brosnahan, Matthew Conroy · 2026-10-21

How Commerce.com and Cloudflare are getting storefronts ready for AI agents
AI can write code and pass the bar exam, but it still struggles to buy a pair of shoes online.
That’s because websites were built for humans, not agents. Most agents that shop for someone today work from a site’s HTML — they look at the page, guess which button does what, click, and try again when they get it wrong. This process is slow, uses a lot of tokens, and something as seemingly innocuous as a theme change can break it.
Enter WebMCP: a browser standard from Google that gives AI agents structured tools on a page, like search_products. Instead of hunting for buttons, the agent calls the exact tool it needs directly, making shopping faster, cheaper, and far more reliable. Because WebMCP is still an experimental proposed browser standard in early preview, it’s currently available behind experimental Chrome flags (chrome://flags/#enable-webmcp-testing), in Chrome Origin Trials, in some agentic browsers, and across developer environments like Cloudflare Kitesurf.
In August, we launched edge implementation of WebMCP in beta. Turn it on, and Cloudflare injects a tiny script at the edge to make those tools available automatically, without site owners writing a single line of code.
Commerce.com, a flexible commerce platform built for the age of AI, already uses Cloudflare to run their almost 100,000 domains. So when the preview came out, they asked: Can we turn this on for all of our stores at once?
Here’s why Commerce.com wanted WebMCP, how we built edge-level opt-outs to give every merchant control, and what we learned along the way.
Why Commerce.com wanted WebMCP
Kristina Pototska, Product Management Director at Commerce.com, explains why this matters for storefronts:
“Merchants keep asking us how they can keep up with agentic shopping. When a shopper asks an agent to find something, merchants want their store to be in the answer. They want to keep the customer, keep control of the checkout, and do it without rebuilding their site. WebMCP helps with all three. The agent gets real tools to search products, check details, build a cart, and get a checkout link, so it doesn’t have to guess its way around the page. The human shopper stays on the merchant’s site, and the merchant keeps the relationship.
We wanted to turn this on in a secure way, and without asking merchants to edit their theme or do anything by hand. That’s where the Cloudflare partnership worked perfectly.
WebMCP also works side by side with our server-side MCP, and together they cover the different ways people shop with agents. Server-side MCP supports agents that connect to a store directly, like an assistant helping someone shop across several sites. WebMCP supports agents that work in the shopper’s browser. It’s the same set of shopping tools in both cases, so merchants don’t have to choose between the two or manage them separately.”
Under the hood, this integration relies on two key principles. First, the WebMCP tools execute directly inside the shopper's active browser session on the storefront's domain, ensuring the agent sees the same prices and cart. No credentials go to a third party, and the visit still happens on the merchant's site. Second, Cloudflare serves as the edge delivery layer for Commerce.com’s backend MCP server, proxying tool definitions and actions unchanged so merchants maintain full control over their tool logic.
What a shopper's agent sees
When visiting an enabled Commerce.com storefront, an AI assistant no longer has to guess how to navigate the site. Instead, it can instantly discover tools via WebMCP.
Suppose you tell your agent: "Find me a waterproof trail running shoe under $140 in size 10 and add it to my cart."
Without WebMCP: The agent attempts to simulate human clicks, only to get blocked by cookie banners, misinterpret variant drop-downs, or get tripped up by bot challenges that try to distinguish automated traffic from real customers.
With WebMCP: The agent detects the store's tools on document.modelContext and makes two clean calls:
- search_products({ query: "trail running shoe", max_price: 140, size: 10 })
- add_to_cart({ product_id: "shoe_123" })
Because the agent runs inside your active browser session on the store's domain, your cart updates in real time. Commerce.com’s backend MCP server determines the commerce flow: when you’re ready to complete the purchase, you click checkout yourself — keeping your payment details secure and leaving you in complete control of the final buy.
What we built together
When Commerce.com asked to turn on WebMCP across almost 100000 storefronts, we ran into a practical challenge: WebMCP was originally designed as a single on-or-off switch for an entire domain zone.
Commerce wanted to enable our mcp-server-client toolpack, which acts as an edge bridge — proxying tool definitions and requests directly from Commerce.com’s backend MCP server to the visitor's browser. Because Commerce.com uses Cloudflare for SaaS to host thousands of merchant vanity domains on shared zones, we needed a way to deliver this platform-wide while giving individual store owners an easy way to opt out.
1. On for all stores on Commerce.com, with an opt-out for each merchant
Instead of building a complex custom allowlist, we hooked WebMCP into the existing Cloudflare concepts of Configuration Rules and custom hostname metadata.
Commerce.com turns WebMCP on for their main zone, then adds a rule at the edge that checks merchant metadata. If a merchant flips the "opt-out" switch in their Commerce.com dashboard, Cloudflare bypasses WebMCP for that specific storefront automatically:
{
  "action": "set_config",
  "expression": "cf.hostname.metadata.webmcp_opt_out eq \"true\"",
  "action_parameters": {
    "webmcp_enabled": false
  }
}
Because Cloudflare evaluates these rules at the edge before serving the page, an opted-out store gets zero extra latency, no remote lookups, and no injected scripts.
2. Tailored endpoints and safe fallbacks
As with any preview release, working with a partner in the real world revealed a few practical details we hadn't accounted for:
Custom MCP paths: When the mcp-server-client toolpack was enabled, our bridge originally expected to find every site's MCP server at /mcp. Commerce.com’s server lives at /api/mcp. To handle this, we added a configurable MCP URL setting at the zone level. When this is set, we pass the custom path into the injected script tag:
<script type="module"
    src="/.webmcp/bridge.js"
    data-packs="c2pa,mcp-server-client"
    data-mcp-url="/api/mcp"></script>
Seamless fallbacks: If a store's MCP server is offline or a customer's browser doesn't support WebMCP, the script exits. The storefront loads normally and human shoppers aren't affected.
What's next
We'll keep investing in WebMCP as the standard evolves, starting with helping agents find a site's tools more easily. Cloudflare and Commerce.com will continue to work together to make shopping with agents fast, reliable and safe for both merchants and shoppers.
If you're at Cloudflare Connect in San Francisco on October 21, 2026, come see us at Getting your storefront agent ready for peak season, a panel discussion featuring Kristina Pototska (Product Management Director, Commerce), Justis Blasco (CTO and Co-Founder, Popmenu), Ross Harvey (Head of Infrastructure, Fruugo), and Josh Mills (VP of Engineering, Gopuff).
