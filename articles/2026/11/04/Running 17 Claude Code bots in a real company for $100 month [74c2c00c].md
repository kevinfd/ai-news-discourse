---
id: "74c2c00cb5e51cc2"
title: "Running 17 Claude Code bots in a real company for $100/month"
url: "https://botsinproduction.com/blog/what-10-claude-code-bots-cost-per-month"
link: "https://botsinproduction.com/blog/what-10-claude-code-bots-cost-per-month"
source: "Bots in Production"
domain: "botsinproduction.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-04T02:02:12Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["oi_ops"]
language: "en"
summary: "What 17 Claude Code Bots Cost Per Month: US$100 (Real Numbers)\nThe real monthly bill for 17 Claude Code bots in a B2B company: a US$100 Claude Max plan, zero API spend, and the one hidden cost nobody lists.\nEvery “I automated my whole business with AI” post has the same mysterious hole in it. The bill. It’s never there. It’s like a cooking show that skips the part where someone pays for the…"
tags: []
orgs: ["Anthropic"]
topics: ["models & research", "policy & regulation", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1406
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50360720"
score: 13
comments: 5
community: "Hacker News"
---

# Running 17 Claude Code bots in a real company for $100/month

Bots in Production · oi_ops · 2026-11-04

What 17 Claude Code Bots Cost Per Month: US$100 (Real Numbers)
The real monthly bill for 17 Claude Code bots in a B2B company: a US$100 Claude Max plan, zero API spend, and the one hidden cost nobody lists.
Every “I automated my whole business with AI” post has the same mysterious hole in it. The bill. It’s never there. It’s like a cooking show that skips the part where someone pays for the groceries.
So here’s mine. All of it. It fits in one table and you will probably be annoyed by how short the table is.
Quick intro so you know who’s talking: I run operations at a B2B distribution company in Korea. I am not a developer. I’ve never deployed anything to “the cloud” on purpose. And yet, since 2025, seventeen Claude Code bots have been doing real work for us every day: reading customer complaints out of chat transcripts and filing them, emailing monthly statements, watching Slack for errors, pricing products off market data. They all run on one Mac in the office.
The bill
One hundred dollars a month. That’s it. That’s the post.
OK, it’s not the post. The reason it’s a hundred dollars and not a thousand is the part worth stealing, so keep reading.
Why the API line is zero: the bots just… run the CLI
Every tutorial wires a bot to the API with a key and pays per token. I wired that up for exactly one job (summarising closed support chats, because three of those run at once and I wanted them fast), and even that one runs on the CLI in practice. Here’s the part that surprised me when I went back and counted for a later post: of the seventeen bots, only three talk to a model at all: the chat summariser, the photo matcher, and the error watcher. The other fourteen are plain Python: database in, template out, Slack card. The three that do need a model do something much dumber and much cheaper than the API: they shell out to the Claude Code CLI.
claude -p --model <model> --restricted \
  --no-session-persistence --strict-mcp-config \
  --output-format json --system-prompt "<system>"
That one line is the entire “AI integration layer” for the claims logger, the error watcher, the statement sender and the price bot. A bot writes a prompt to stdin, gets JSON back on stdout, parses it, moves on with its life. No SDK. No token accounting. No key rotation ceremony. It runs on the same subscription I use to build the bots in the first place, which still feels faintly like cheating.
The flags are not decoration:
- --restricted and --strict-mcp-config: the bot can’t touch tools I didn’t hand it. A chat summariser has no business browsing my filesystem, however curious it gets.
- --no-session-persistence: every call starts with amnesia. Bots must not remember the previous customer. (Humans shouldn’t either, but that’s a different post.)
- --output-format json: I get an envelope with an is_error field. A failure is a failure, not a half-finished sentence that looks like a summary.
The trade-off: Max has usage limits (5x the Pro allowance on this tier), and if the CLI’s login expires on the machine, all seventeen bots fall over at the same moment, like dominoes that were also my fault. That happened. It’s further down. For what it’s worth, I haven’t hit the limit with 17 bots, because bot calls are tiny: one prompt in, one short JSON out, a few hundred times a day. Bots don’t have long heartfelt conversations.
Where the API key still earns its keep (it doesn’t, yet)
The summariser has an API fallback:
body = {
    'model': os.environ.get('CRM_API_MODEL', 'claude-sonnet-5'),
    'max_tokens': 1200,
    'system': SYSTEM,
    'messages': [{'role': 'user', 'content': prompt}],
}
If ANTHROPIC_API_KEY is set, summaries go through the API. It isn’t set. The fallback exists so that the day the subscription becomes the bottleneck, I flip one environment variable instead of rewriting anything at 11pm. So far the API line on my bill is a very round zero.
Two guardrails in there that I’d keep even if tokens were free: max_tokens is capped at 1,200 because a claim summary that needs more than that has gone wrong. And the model may return at most eight items. More than eight means it stopped summarising the complaint and started transcribing the customer’s order history. We throw that away and try again.
Summaries run three at a time. Sheet writes run one at a time. That’s not a style preference. The one evening I let the writes run in parallel I got 300-odd database is locked errors and seven chats the bot simply gave up on. That night has its own post, with the log.
The hidden cost: my hours, counted honestly
I spend about one hour a week on the bots now. In the first two months it was closer to ten. That time went to:
- Writing and rewriting rules. The claims logger alone has more than 40 rules that no tutorial mentions, like “a replacement that’s also defective is a new row, not an edit” and “if the customer says not everything arrived, that’s a missing item, not a quality complaint”. Every one of those came from a wrong row and a mildly irritated colleague.
- Reading alerts. Every bot error goes to my DM. Not a channel. That was deliberate, and it means I’m the person who sees all of them. Lucky me.
- Benchmarking. When I swapped the summariser’s model, I re-ran it over old chats and compared rows. Accuracy went up when I fed it the company’s recent claims and the order items as context. That bench is why I trust the sheet.
If you price those hours at anything, it’s the biggest line on the bill by a mile. I think it’s worth it. I’m just not going to pretend it’s zero.
You don’t need a server. You need a laptop that doesn’t sleep.
The bots run on a perfectly ordinary MacBook. launchd keeps one Python process alive. There is no cloud instance, no Docker, no deployment pipeline, no YAML. If you already own a laptop, your hardware budget is spent.
And you don’t need to be near the laptop either. That’s me on a station bench at 09:05, reading the overnight report on an iPad before I’ve reached the office. The MacBook did the work; I just check the homework.
The only real requirement is that the machine stays awake. “The bot didn’t log anything last night” turned out, more than once, to mean “the laptop went to sleep”. The first thing I check now when a bot goes quiet is the Mac’s power log, not the bot. Plug it in, turn off sleep-on-power, done.
One trap on the way from “I run it in a terminal” to “it runs as a service”: launchd does not load your shell’s PATH. So a bot that worked beautifully from the terminal fails silently as a service because it can’t find claude. The fix is full paths in the config and a solemn vow never to call the bare name from code again.
What I’d tell myself a year ago
- Start on the subscription, not the API. You will rewrite your prompts thirty times before anything is stable. Paying per token during that phase is paying to learn. I started on Pro (US$20) and moved to Max 5x (US$100) when the bots multiplied; that tier has been enough for 17 of them.
- Cap output tokens per task. It’s a correctness tool, not a cost tool. A summary that needs 3,000 tokens is a summary that’s gone off the rails.
- Don’t buy a server. A laptop that’s plugged in and forbidden to sleep removed more failures than any prompt change, and cost nothing.
- Count your hours. The US$100 is small precisely because a human is doing the parts that are hard to automate: writing the rules and reading the alerts.
Next in this series: the Slack approval button that sits in front of every bot action, and why nothing ships without a human click.
One line from me
US$100 a month, one laptop that doesn’t sleep, and about an hour a week of my time. The bill was never the hard part.
The month-by-month version lives in the September report; why only three of the bots call a model at all is in Haiku, Sonnet or Opus.
