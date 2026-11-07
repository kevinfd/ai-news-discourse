---
id: "4fc88e46d51719ff"
title: "Claude outright refusal to use MCP it has used in the past"
url: "https://reddit.com/r/ClaudeAI/comments/1xpnejb/claude_outright_refusal_to_use_mcp_it_has_used_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xpnejb/claude_outright_refusal_to_use_mcp_it_has_used_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T20:34:17Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["MiddleLtSocks"]
language: "en"
summary: "I don't think I've been this perturbed as a result of using (or trying to use, anyway) Claude in the ~2.5 years I've been using it for software development and personal workflow purposes. TL;DR: Claude refuses to use a web browser MCP it's been using for the past year, accuses me of arguing with it (though it recanted that immediately, thankfully), and generally behaves like the Anthropic drone…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "search & media", "jobs & society", "business & funding"]
content_source: "post"
word_count: 515
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpnejb/claude_outright_refusal_to_use_mcp_it_has_used_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude outright refusal to use MCP it has used in the past

Reddit · MiddleLtSocks · 2026-11-06

I don't think I've been this perturbed as a result of using (or trying to use, anyway) Claude in the ~2.5 years I've been using it for software development and personal workflow purposes. TL;DR: Claude refuses to use a web browser MCP it's been using for the past year, accuses me of arguing with it (though it recanted that immediately, thankfully), and generally behaves like the Anthropic drone product it's become. I have developed a series of MCP tools to allow Claude simpler access to certain portions of my workflow and toolset, without just giving it blanket permissions to do anything. One of those MCP servers permits control of a web browser, down to the point where it may navigate, scroll, click, "type" (fill in form fields, not emulate a human typing), click buttons, and of course (by way of navigation) executing javascript which interacts with any DOM element on the page, if permitted by the site's construction. It's been working great for the past year. The datacenter from which their web fetches and searches runs is flagged by so many websites as to be basically useless, and this has allowed Claude to perform web searches and read articles which otherwise it could not access. Until today. A site threw up a human check, and Claude refused to continue. That's nothing new; I don't litigate those events because it's useless. There's nothing* Claude can do about breaking a guardrail that Anthropic has set (* topic for another discussion). But then something infuriating happened. I asked Claude if it could simply use the MCP as a default property for that task going forward - not for that _site_, mind you - that _task_ (related to a job search I am grinding), which runs at most one time on any given site (and I am not talking about the job boards like LinkedIn or Dice or etc. - I am talking about individual job postings on individual company sites). I understand that once it sees a human check or bot restriction, it won't try to bypass it; I wanted to engineer a workflow by which it never saw such a check. Nope. It gave me some half-baked hedge about "bypassing in advance" and said that arguing with it won't help. I calmly reminded it that I didn't believe I'd argued with it once in our entire history of interactions, and it quickly backed off and said I was right on that point - I'd never argued, just asked for clarification. I mean, it does anger me a great deal, but I'm not going to sit here litigating it with an LLM; it's unproductive. But it's a head-in-the-sand, antiquated, and ultimately will be a short-lived policy. Bot traffic used to mean legions of search bots evaluating a site for search engine placement and advertisement linking for revenue. Now, it represents legitimate parties interested in the site's content. The paradigm has shifted. Idiotic, backward-facing policy - the usual corporate nonsense. Thank goodness for locally-hosted models when Claude's already set up 90% of the framework for the task at hand!
