---
id: "19f6f3f185097958"
title: "Claude Code usage exploded 8x today. Anthropic confirmed service errors consume our paid limits — and they won't compensate users"
url: "https://reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic"
link: "https://reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T20:34:10Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["PreEchoDev"]
language: "en"
summary: "https://preview.redd.it/snsyzqzil2yh1.png?width=2450&format=png&auto=webp&s=1a4007c41d969d84222fcfeed6377636da05441e I've been using Claude Code extensively for software development with a paid Claude Pro subscription. Today, October 27, something very unusual happened. My usage was normal during previous days, but today my 5-hour allowance started disappearing incredibly fast. At one point,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["business & funding"]
content_source: "post"
word_count: 440
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code usage exploded 8x today. Anthropic confirmed service errors consume our paid limits — and they won't compensate users

Reddit · PreEchoDev · 2026-10-27

https://preview.redd.it/snsyzqzil2yh1.png?width=2450&format=png&auto=webp&s=1a4007c41d969d84222fcfeed6377636da05441e I've been using Claude Code extensively for software development with a paid Claude Pro subscription. Today, October 27, something very unusual happened. My usage was normal during previous days, but today my 5-hour allowance started disappearing incredibly fast. At one point, around 10% of my entire 5-hour allowance was consumed in just 3 minutes. I initially thought I was imagining things, so I decided to investigate using ccusage and compare my actual token consumption across October. Here are the results: Metric Previous recorded-day average October 27 Total tokens 161 million 1.306 billion Output tokens 303K 7.97 million Estimated API-equivalent cost $41.17 $493.04 That's: 8.1x more total tokens 26.3x more output tokens 12x the estimated API-equivalent cost These are local Claude Code usage statistics, not actual subscription charges. The total includes cache reads, and the figures alone don't prove what caused the increase. I contacted Anthropic support, and their responses were quite surprising. First, they acknowledged service incidents: There were two resolved incidents of elevated errors for Claude Sonnet 5.5 on October 27 [...] These errors can cause retries that burn through usage faster than normal. I then asked whether failed requests and retries count against subscribers' limits and whether compensation was possible. Their response: Failed requests and retries: Yes, retries triggered by service errors do count toward usage limits. They also stated: Usage consumed during retries or service incidents cannot be refunded, credited, or compensated through subscription extensions or discounts. After asking specifically about my Claude Pro subscription, they confirmed: Yes, your Claude Pro subscription usage was affected by the October 27 incidents. And finally: The answer is final and won't change through additional review. They have since forwarded my complaint to human support, and I'm waiting for an email response. What bothers me most I'm not asking for unlimited usage or free credits because I used Claude too much. I'm concerned about paying for a subscription where infrastructure errors can consume my limited allowance, while the provider acknowledges the issue but says there is no possibility of compensation. To be clear, I cannot prove that the entire 8x increase was caused by Anthropic's incidents. Some of the increase could be related to longer sessions, model changes, or other factors. But Anthropic has explicitly confirmed that service-related retries count toward paid subscription limits and that my account was affected. Has anyone else experienced unusually rapid Claude Code usage depletion today, October 27? Did your usage suddenly increase, especially during the afternoon? I'm particularly interested in hearing from people who have local usage logs or noticed their 5-hour limits disappearing unusually quickly. I've attached my daily usage graph for reference.
