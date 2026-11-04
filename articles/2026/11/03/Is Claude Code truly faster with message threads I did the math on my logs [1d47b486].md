---
id: "1d47b486cd08ac13"
title: "Is Claude Code truly faster with message threads? I did the math on my logs"
url: "https://zdnet.com/innovation/claude-code-message-threads-speed-test"
link: "https://zdnet.com/innovation/claude-code-message-threads-speed-test"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T07:28:00Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["David Gewirtz"]
language: "en"
summary: "Claude Code’s update could save you time during demanding, hours-long coding sessions at no extra cost. But by how much? Here’s my real-world result."
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "Meta"]
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 928
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/anthropic_004de4.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Is Claude Code truly faster with message threads? I did the math on my logs

ZDNet · David Gewirtz · 2026-11-03

ZDNET’s key takeaways
- Anthropic’s message threads make Claude Code a tad more responsive.
- My tests suggest savings of 2 to 4 minutes per coding session.
- You get faster responses, but no savings on token costs.
My real-world speed estimates
This feature is on by default for most Claude Code users. API users can turn it on using the “thread” parameter for API requests.
Token consumption remains unchanged, so this capability doesn’t provide a cost savings. The 35% savings is Anthropic’s measurement.
More from ZDNET
Also: Claude Code’s revised projects adds AI orchestration, but local developers must wait
Timing data from roughly 980 turns in my own Claude Code logs before this feature became available shows that Claude usually began a response about 3 seconds after each mid-task request when running contexts of 500,000 tokens and up. During five busy evenings last month, my conversations made roughly 100 to 225 model calls in a four hour stretch.
Using Anthropic’s reported 35% median time-to-first token reduction in a quick projection, Claude estimated a 2- to 4-minute savings per four hour work session.
Message threads reduce repeated uploads
Agents often send a bunch of requests to the model during each conversation. Before message threads, each message sent the entire conversation with each request.
Imagine if you’re in a very long texting chat with a friend. Now imagine if every time you sent a text to that friend, you also had to send every other text and every other reply along with that original text. That’s how model messaging has always worked. Except now, with message threads, there’s a better way.
Also: 75% of developers I surveyed prefer Claude Code – here’s why they choose it over Codex
With message threads turned on, agents only have to send what’s changed since the last turn. This reduces the amount of data transmission and increases responsiveness, what Anthropic calls time-to-first-token.
The benefit is seen most strongly in sessions that have a context of 500,000 to a 1 million tokens. About half of my sessions hit that context ceiling multiple times a night.
How much faster is it?
Anthropic reports that Claude’s message threads reduce median time-to-first-token by 35% for large requests. While my estimated savings of several minutes per session isn’t huge, the benefit increases with very long-running coding agents, and agents that transmit documents and image-heavy workloads.
For computer-using agents, all those screenshots “stay with the thread instead of being re-uploaded on every turn,” according to the Anthropic blog post on the feature.
Also: How I made a paid Mac app in 11 days with Claude – without writing a single line of code
While the time savings may not seem huge, in larger enterprise deployments or deployments where you want the AI to respond faster, any reduction in latency is a big deal and will be seen in any application of Claude technology that has a lot of back-and-forth turns with large data payloads.
Faster doesn’t mean cheaper, or more expensive
Even though the addition of threads to the Messages API can reduce latency, token usage and therefore cost won’t go down. That’s because the model itself will still process the full conversation during every turn. Rate limits also don’t change.
Message threads and prompt caching can work together to reduce workload. Prompt caching has been around for about two years now, and it does save money. That’s because prompt caching allows the model to avoid re-processing prompts over and over (for example, in looping analysis calls).
On the other hand, the message threads capability does offer an extra smidge of performance, at no extra cost. So, there’s that.
It also won’t make Claude smarter
Context is the size of the full session that Claude is currently working with. The rough human equivalent is current working or short-term memory. Most Claude Code sessions max out at a million token context, where a locally-hosted AI on my 128GB Mac Studio handles a context no bigger than 64K, or about 6% of the Claude Code context size.
Also: After the vibe-coding rush comes the debugging hangover
Compaction is a process where the AI attempts to reduce and eliminate extra information to fit the current session’s turns into the available context. An oversimplified analog is when you save a JPEG with quality turned way down in order to save space. You lose a lot of the visual fidelity, but you still get the main idea.
The larger the context you have, the longer you can go before the session has to initiate compaction. But there’s a gotcha. The larger the context you have, the more chance there is the model will lose track of what it’s working on or make reasoning errors.
Individual one-off requests also won’t see an improvement from message threads. Also, any conversation that delays longer than 5 minutes between turns will send the full message contents and not just the new stuff.
This feature doesn’t eliminate context management or compaction. But if your context is quite large, it will make responses a bit snappier.
A small but helpful speed boost
Overall, message threads are a good thing, a solid if small innovation that increases responsiveness. While the feature doesn’t reduce costs, there’s also no additional cost for the additional performance, which is itself a win.
You can follow my day-to-day project updates on social media. Be sure to subscribe to my weekly update newsletter, and follow me on Twitter/X at @DavidGewirtz, on Facebook at Facebook.com/DavidGewirtz, on Instagram at Instagram.com/DavidGewirtz, on Bluesky at @DavidGewirtz.com, and on YouTube at YouTube.com/DavidGewirtzTV.
