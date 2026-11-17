---
id: "36a542e12ff7103d"
title: "PyBot, an agent-written GOFAI chatbot"
url: "https://github.com/huggingface/pybot"
link: "https://github.com/huggingface/pybot"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:47:49Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["filterdust"]
language: "en"
summary: "LLMs drive today’s chatbots and agents, but chatbots long predate them. Sixty years ago, ELIZA held conversations by matching patterns in what the user typed and answering with predefined templates. It could seem insightful, but its repertoire was narrow, and expanding it meant writing more rules by hand. How far could a rule-based chatbot go if a swarm of agents did that work instead?\nWe…"
tags: ["r/singularity"]
orgs: ["Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 539
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xyiepu/pybot_an_agentwritten_gofai_chatbot/"
score: null
comments: null
community: "r/singularity"
---

# PyBot, an agent-written GOFAI chatbot

GitHub · filterdust · 2026-11-17

LLMs drive today’s chatbots and agents, but chatbots long predate them. Sixty years ago, ELIZA held conversations by matching patterns in what the user typed and answering with predefined templates. It could seem insightful, but its repertoire was narrow, and expanding it meant writing more rules by hand. How far could a rule-based chatbot go if a swarm of agents did that work instead?
We challenged a swarm of over 1,000 agents to build a chatbot entirely in Python: no weights, no training, just if-else branches, regex patterns and lookup tables. The agents wrote and evaluated over 5,000 versions, and the chatbot’s win rate on SmolTalkBench, where an LLM judge compares each reply with a reference answer, climbed from 0% to 26%. That puts it on par with SmolLM-360M-Instruct, which just a few years ago was state of the art for models under 1B parameters.
The result is PyBot: around 640k lines of code that can answer everyday questions, backed by 550k lines of tests the agents wrote themselves.
Try PyBot in your terminal below, or in the browser on Hugging Face, where each reply shows which of PyBot’s modules produced it.
PyBot needs Python 3.8 or newer and nothing else: no packages to install and no model to download.
git clone https://github.com/huggingface/pybot
cd pybot
python -m pybot
That starts a chat in your terminal:
    ____        ____        __
   / __ \__  __/ __ )____  / /_
  / /_/ / / / / __  / __ \/ __/
 / ____/ /_/ / /_/ / /_/ / /_
/_/    \__, /_____/\____/\__/
      /____/
A chatbot written in plain Python. No weights, no training, just rules.
Type a message and press Enter. /reset starts a new conversation, /exit quits.
user: hi, i'm Sam
pybot: Nice to meet you, Sam. What can I help with?
user: my kettle is full of limescale, how do i get rid of it?
pybot: Half fill the kettle with equal parts water and white vinegar, or a sachet of citric acid, boil it and leave it half an hour, then tip it out and boil fresh water twice before you use it again. In a hard-water area do it every couple of months: the scale forms because hard water leaves calcium behind as it boils, and a thick layer makes the kettle slow and puts a scum on the tea.
user: how long does that take
pybot: Half an hour.
user: what's my name?
pybot: You're Sam.
Type /reset to clear the screen and start a new conversation, and /exit to quit. PyBot takes a few seconds to start, because Python has about 640,000 lines of code to load, and about a second to reply.
To ask one question and exit, or to pipe messages in and get one reply per line:
python -m pybot -p "Why do onions make you cry?"
echo "how long should i boil an egg" | python -m pybot
For a pybot command you can run from anywhere, install the clone with pip install ..
Every turn, each module in bot/modules/ may propose a reply, and an arbiter (bot/modules/arbiter.py) picks the one you get. The modules build on four shared parts:
The modules themselves are another 81,000 lines.
Apache License 2.0. See LICENSE.
