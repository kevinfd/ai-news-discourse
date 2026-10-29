---
id: "e4061f1f7b12c67f"
title: "I Put a Bunch of AI Agents in Charge of a Fantasy Soccer Team. They’re Not Better Than Humans—Yet"
url: "https://wired.com/story/i-put-ai-agents-in-charge-of-a-fantasy-team"
link: "https://wired.com/story/i-put-ai-agents-in-charge-of-a-fantasy-team"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T18:30:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Will Knight"]
language: "en"
summary: "To experiment with AI’s predictive skills, I let Codex loose on a fantasy team. It tried to bench Erling Haaland at first, but it soon learned the error of its ways."
tags: ["Business", "Business / Artificial Intelligence", "AI Lab", "artificial intelligence", "soccer", "Sports", "agentic AI", "OpenAI", "research", "prediction markets", "Kalshi", "Polymarket"]
orgs: ["OpenAI", "Anthropic", "Google", "Meta", "xAI", "UK"]
topics: ["agents & coding", "models & research", "search & media", "policy & regulation"]
content_source: "fulltext"
word_count: 876
paywalled: false
image: "https://media.wired.com/photos/6ae108712ec9b10c531020d9/master/pass/business_ai_predict_future.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# I Put a Bunch of AI Agents in Charge of a Fantasy Soccer Team. They’re Not Better Than Humans—Yet

WIRED · Will Knight · 2026-10-28

I have consulted my AI-powered crystal ball, and it’s telling me that frontier models are going to get a lot better at making predictions in the near future. Just ask my Premier League fantasy team.
A few weeks ago, I deployed a small horde of AI agents to craft and manage an experimental roster. Given the proliferation of AI agents into pretty much every aspect of our lives, I wanted to know if a swarm of bots could put together a winning team.
I first looked at the potential for AI here a few years ago, playing around with a tool from the UK’s Turing Institute that selected teams after modeling previous fantasy league data. Its suggestions were remarkably bonkers—it didn’t incorporate real-world information, like a player’s injury or a team’s change in management.
This time, while on a flight to visit family, I asked Codex for help. First, I fed the model a couple of relevant research papers. Then, I asked it to build a harness—instructions and code that guides different agents through various steps—that would check recent news and run a model to make predictions.
It quickly came up with a setup that seemed to collate and analyze way more information than I ever would have. And yet I was surprised by how dumb the initial team suggestions were. Leaving Erling Haaland on the bench? Really, Codex?
I then asked Codex to create a team of agents that did different things: several that read news and blog posts; others that analyzed recent results; more that ran models; and a bunch that critiqued suggestions. This seemed to significantly improve the suggestions. I tried increasing the number of agents to more than 100, hoping this would make the system smarter still, but it didn’t change much besides running up my API bill.
Still, the improvement from a few years ago was striking. According to Haifeng Xu, a computer scientist at the University of Chicago who studies the uses of AI in market situations, newer models may be even better at making predictions because they’re able to consume and analyze huge amounts of real-world information, and they’re able to orchestrate more complex systems for their guesses.
“AI is just getting smarter in understanding the world—I feel like that's the fundamental reason they’re improving,” Xu tells me.
Late last year, Xu was marveling at the growing popularity of prediction markets like Kalshi and Polymarket. He wondered how the best commercial models might fare on those markets, so alongside several colleagues, he began testing their forecasting skills.
They had models guess, for example, who would win the NBA Championship and who President Trump would meet with.
“Very quickly we started to realize that models did really well,” Xu tells me. The models were sometimes able to do better than the average person without any special instructions or guidance, he says. In their testing, GPT-5 was the best at making predictions, followed by Grok 4, Claude Sonnet, Gemini, and Llama.
The team went on to develop Prophet Arena, a benchmark that measures a model’s ability to make predictions. It’s one of a number of benchmarks designed to test AI’s future-gazing capabilities; another, Prediction Arena, from researchers at Harvard University and a company called Arcada Labs, recently gave frontier models $10,000 to wager on prediction markets over 57 days. The models consistently lost money in their experiment, but the researchers saw evidence of them improving consistently over time.
Xu tells me that AI can most effectively make predictions using a custom harness, and notes that having agents with unique tasks—reading the news, collecting other data, and analyzing the whole system, for instance—seems to be the most effective approach.
Interestingly, AI still often lags behind very skilled experts known as superforecasters. Xu explains that, although humans cannot consume as much information, their understanding of the real world—that is, of the dynamics behind a news story—is deeper.
That said, there’s growing evidence that the human superforecaster’s edge is eroding. A contest called the Metaculus Cup recently showed that AI can sometimes beat even the best human predictors. And a benchmark called ForecastBench could provide further evidence that AI can match human skills when the results of an ongoing contest conclude soon. In fact, I think we can expect the big labs to turn their attention to future-gazing as a powerful new way to measure progress in machine intelligence.
All of these predictive experiments seem to suggest that, like math, coding, and law, industries predicated on trading may soon be upended by AI. Perhaps the best human traders will take on a new kind of role: supervising and orchestrating AI agents capable of divining the future far better than they can.
For the time being, my AI’s suggestions still don’t seem all that impressive. Its team hasn’t outscored the average over the past weeks. I certainly won’t be using any of its suggestions in my own selections.
But AI will no doubt get better, perhaps making it all too easy to dominate fantasy league pretty soon. I’m kind of hoping it won’t, though, as it would spoil the fun of trying to earn bragging rights by winning all by yourself.
This is an edition of Will Knight’s AI Lab newsletter. Read previous newsletters here.
