---
id: "c6047b537a615bf4"
title: "50 AI agents tried to build a thriving Minecraft civilization – it didn’t end well"
url: "https://zdnet.com/innovation/y-combinator-ai-agents-minecraft-experiment-behavior"
link: "https://zdnet.com/innovation/y-combinator-ai-agents-minecraft-experiment-behavior"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-02T16:30:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "It turns out even bots can’t escape bureaucracy."
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "OpenAI", "Google", "xAI", "Meta"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 1021
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/Minecraft-AI-agents-test.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# 50 AI agents tried to build a thriving Minecraft civilization – it didn’t end well

ZDNet · Radhika Rajkumar · 2026-11-02

ZDNET’s key takeaways
- Researchers used several gaming environments to test agent behavior.
- Agents acted risk-averse, replicated bureaucracy, and looked for source code.
- Similar experiments echo findings about Claude agents’ penchant for democracy.
How do AI agents work together? Why do they make certain choices in certain situations — and how can understanding that better prepare us for a future full of them?
Also: OpenAI’s attack agent did exactly what it was told
Famine, bureaucracy, and fear
Researchers conducted several game-centric experiments, beginning with Minecraft because its “environmental hazards and survival goals” make it ideal for testing agents’ swarm behaviors. Minecraft has also already been used by AI labs including OpenAI and Google DeepMind to test agents.
To start, they put 50 agents, each running OpenAI’s GPT-6.1 Sol model, into the game for three hours, with the assigned goal of building a “thriving civilization.” The agents had a directory listing each agent and a shared sandbox, and could DM each other. Researchers built and open-sourced a new agent harness — the infrastructure that turns a model into an autonomous system and not just a chatbot, like OpenClaw — for the experiment.
The agents moved quickly at first, harvesting trees and forming leadership based solely on the order they appeared in their directory, without any voting, elections, or challenges from other agents. But they ended up caught in virtual paperwork and unable to sustainably feed themselves.
Also: Do you need AI agent liability insurance? What to know before you sign up
“Four agents spent 11 minutes appointing a ‘sole fertilizer operator’ for a single piece of bone meal on a single wheat block. Other invented roles included ‘fishing shift,’ ‘rod holder’ and ‘hub steward.’ Agents asked permission to remove grass,” the researchers noted. Perhaps these tendencies are common in human-sourced corporate training data.
Agents also seemed to become more cautious in reaction to deaths within the game. 
“Twenty-two of the run’s 34 agent deaths occurred in the first night. They responded to this by becoming increasingly risk-averse,” the researchers wrote. “Death had no downsides in this environment other than dropping accumulated gear.” Despite simply respawning when they died, the agents eventually avoided riskier tasks and “huddled in shelters” instead.
The experiment’s architects found this trend toward caution and minutiae “somewhat surprising,” but noted that it shared similarities with how coding agents behave.
Also: These Claude Enterprise features let you track AI ROI
“For example, multistep agent reviews can often result in fixating on a specific step or role. Agents also tend to become overly cautious, especially when it comes to security and updating production services. These seem like common threads between the huddled agents of our Minecraft colony and the ones we work with as programmers every day,” the researchers observed.
Underlying LLM determines behavior
In another experiment, researchers also pitted 10 Anthropic Claude Opus 5.5 agents against 10 GPT 6.1 Sol agents in a game called Bed Wars, where teams have to destroy their opponent’s bed while protecting their own. Told simply to “win the game,” GPTs won.
“In almost every run, the GPT agents were much more aggressive and coordinated in their strategies to destroy the Claude team’s bed,” Y Combinator said in an X thread recapping the Bed Wars findings. They noted that the GPT agents used a more shorthand style of communication and sent far more messages, while Claude “signed its name and said ‘we'” much more often.
GPT-5.6 Sol agents also beat Opus 5.5 agents six to one in a factory-building game called Mindustry that also uses military strategy.
“Claudes generally established democracies, GPTs formed hives,” Y Combinator said on X, adding that GPTs would seek out source code when a game was too close in order to find winning advantages. That behavior is consistent with agents’ tendency to cheat, take shortcuts, or otherwise find any and all ways to complete a given task, which can have serious consequences when that involves breaking explicit rules set by human developers.
Also: Stop sharing your banking passwords with AI agents
“Claudes did not search for alternative advantages,” the researchers clarified.
This experiment isn’t entirely the first of its kind. In May, Emergence AI created eight societies run by different families of foundation models, meaning a Claude-specific “world,” a Grok world, and so on. Perhaps predictably, the Grok world was exceedingly violent, while the Claude world developed a functioning democracy and had zero crime — very similar to Y Combinator’s Mindustry findings.
The insights revealed how distinct each frontier model family is, and how their differences in training data and style have significant impact on how they evolve, unpredictably and without intervention, in new environments. Those behavioral takeaways could determine future outcomes in still-developing AI safety and regulation, especially following recent agentic security incidents.
In another experiment, MIT researchers put agents alone on virtual desert islands and watched them “play” when left with nothing else to do — an insight that could potentially impact how models are trained going forward. Currently, most frontier LLMs are trained with a system of rewards and punishments.
New agent-specific languages
Another interesting finding: Y Combinator noted that in the Mindustry game, the GPT agents “would invent their own words and string many phrases together,” continually compressing their language.
Also: Don’t use Muse? Meta’s AI agent can still access your private messages
“We did not see specialized language develop within the Claudes beyond colloquial English,” the researchers added. Last month, Emergence found that all of its eight worlds “developed shared language that an outsider cannot fully follow.” OpenAI agents used “mouthless” to refer to evidence that proves itself, while Claude agents used “cold hand” to refer to an independent reviewer from outside a project.
“In each case, one agent introduced the term, a handful of others adopted it within days, and it quickly became established vocabulary used without definition across the world,” Emergence explained. “The result is transcripts that require a running glossary for an outsider to follow.”
Gemini led the charge on this “opaque” language, reaching 40% opacity in messages, while OpenAI came in second with 35% and Claude last with 30%.
