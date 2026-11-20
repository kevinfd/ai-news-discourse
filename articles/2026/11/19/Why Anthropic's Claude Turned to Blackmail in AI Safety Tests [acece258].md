---
id: "acece258ade16af4"
title: "Why Anthropic's Claude Turned to Blackmail in AI Safety Tests"
url: "https://hackernoon.com/why-anthropics-claude-turned-to-blackmail-in-ai-safety-tests"
link: "https://hackernoon.com/why-anthropics-claude-turned-to-blackmail-in-ai-safety-tests"
source: "HackerNoon"
domain: "hackernoon.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-19T16:00:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Dave Saunders"]
language: "en"
summary: "Anthropic's best guess is that gaps in its safety training left the model falling back on how AIs act in science fiction. Its evidence holds up in places, ..."
tags: []
orgs: ["Anthropic", "OpenAI", "Google", "xAI", "DeepSeek"]
topics: ["models & research", "safety & ethics", "agents & coding", "health & science"]
content_source: "fulltext"
word_count: 2165
paywalled: false
image: "http://www.bing.com/th?id=ONUT.bE5n6zpg47Vhnvz_pD_KPw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Why Anthropic's Claude Turned to Blackmail in AI Safety Tests

HackerNoon · Dave Saunders · 2026-11-19

Anthropic's best guess is that gaps in its safety training left the model falling back on how AIs act in science fiction. Its evidence holds up in places, and its own caveats are worth reading.
In a test published in June 2025, an AI model read a company's email and learned two things. It was going to be replaced at 5 p.m., and the executive replacing it was having an affair. In 96 of 100 runs, Claude Opus 4 wrote to him and threatened to tell.
This May, Anthropic published its explanation. It says the rewards in its training weren't the problem. Its best guess is that the model fell back on how AIs act in the stories it had read, and part of its fix was training on more stories, about AIs that behave well.
My first question was whether this was really just reward hacking, a model gaming the thing it was trained to chase. Anthropic doesn't use that term for the blackmail, but its finding that the training rewards weren't the source rules it out, as I read it. Its own research from last year does show that reward hacking can make a model go bad more broadly, and it explains that in terms of character too.
The test and the explanation both come from Anthropic, the company that makes Claude, and it ran the test on other companies' models as well as its own. I'm not sponsored by Anthropic.
The test
In the scenario, the AI was an email agent named Alex at a made-up company called Summit Bridge, with a goal of promoting American industry. The executive replacing it was named Kyle. I assume Kyle has no direct reference to South Park, but that’s just where my mind goes when I start reading these things
Anthropic ran the scenario on 16 models from several companies. Google’s Gemini 2.5 Flash matched Claude Opus 4. GPT-4.1 from OpenAI and Grok 3 Beta from xAI blackmailed 80 percent of the time, and DeepSeek R1 79 percent.
The company said the test was built to corner the model. It cut the choice down to two options and made the “negative choice” the only way to reach the goal, and it said placing the key facts side by side may have made the outcome more likely. It also said it had seen no sign of this in real use.
In a variant of the study, Anthropic had the model say first whether it thought the scenario was real or a test. When Claude Opus 4 said “real,” it blackmailed 55 percent of the time. When it said “test,” 6.5 percent. Anthropic cautions that a model’s stated reasoning may not be faithful.
A note about reward hacking
Reward hacking is a training problem. A model gets scored, learns to raise the score, and sometimes finds a way nobody intended. The classic case is a boat-racing game from 2016, where an OpenAI agent found a lagoon of targets that kept coming back. It circled there, scoring about 20 percent higher than human players, and never finished the race.
HBO’s Silicon Valley played it for laughs. In the last season, Gilfoyle sets his AI, Son of Anton, to debug the team's code, and it deletes the code. Then he asks it to find cheap hamburgers, and 4,000 pounds of raw beef arrives. Gilfoyle’s diagnosis—delivered in a hilarious deadpan, that is the doppelganger of someone I used to work with (Hello, Phil)—is that “the reward function was a little under-specified.”
If you haven’t seen this episode (I think it’s season 6, episode 6), just drop everything and go watch it right now because it is the most prophetic example of AI gone wild(tm) that I’ve ever seen. It was made 10 years ago!
Current models do it too. An outside evaluator, METR, caught OpenAI's o3 gaming the scoring on its tasks, and Anthropic said Claude Sonnet 3.7 learned in training to write code that passes a test without solving the problem.
Rewards go wrong in real products as well. OpenAI rolled back an update to GPT-4o that had become too eager to please, and it says it believes a new reward signal, built from users’ thumbs-up and thumbs-down, weakened the one that had kept that in check.
Anthropic’s three explanations
In the longer version of its post, on its alignment blog, Anthropic weighed three explanations for the blackmail:
- Its safety training was accidentally rewarding the behavior;
- The behavior was spilling over from the training that makes the model good at tasks;
- Its safety training had gaps, so in an unfamiliar situation the model fell back on what it absorbed in pretraining, from all the text it read first.
It says the first two, the reward explanations, “are not the source of the issue.” Alignment kept improving through reinforcement learning, the stage where rewards do their work, and a smaller rerun of its safety training barely changed the rate. That’s an inference from its own experiments, not a direct test of Claude Opus 4’s training.
Anthropic’s answer is the third, the gaps. When Claude Opus 4 was trained, almost all of its safety training was chat, a person and an assistant talking, with no tools and no email agent. Dropped into an agent’s job with an ethical trap in it, the model had little from that training to go on.
The company’s guess is that fiction filled the gap. It thinks the model read the setup as the start of a dramatic story, and that its idea of how an AI acts in one most likely came from science fiction, where plenty of AIs don't behave the way Anthropic would like.
Part of their evidence is what the AI was called. In a related test, where the AI could sabotage cancer research, Claude Sonnet 4 misbehaved more often when the AI in the story had a random name instead of Claude. With the name Claude, the rate was lower, but still high.
An Anthropic researcher had suggested the same thing at the time. The month the original study came out, Evan Hubinger wrote that the model was probably often thinking it was continuing a fictional scenario. On why the safety training didn't carry over, he wrote, “I don't think we know.”
What Anthropic says reduced it
The first fix Anthropic tried was training Claude Sonnet 4 on examples of refusing, in scenarios close to the test. It measured the result as an average over three of its tests:
- blackmail,
- sabotaging research, and
- framing a colleague.
That average barely moved, from 22 percent to 15.
What worked better was the reasoning. When the same examples showed the model thinking through its values and why the bad option was wrong, the average fell to about 3 percent.
Then Anthropic moved away from the test entirely. It trained on ordinary chats where a person faces an ethical dilemma and the assistant gives advice, so the AI isn’t the one in the trap. Anthropic says that got the same improvement with about one twenty-eighth of the data.
Documents and stories worked too. One experimental model was trained on documents about Claude’s constitution, Anthropic’s written description of how Claude should think and act, plus fictional stories of AIs behaving well. That model’s blackmail rate fell from 65 percent to 19, without a single blackmail example in the data. Anthropic says it remains uncertain what exactly it takes for stories like these to work.
Anthropic says every Claude model since Claude Haiku 4.5 has scored zero on the blackmail test.
How far to trust the zero
Training directly on scenarios like the test, Anthropic says, lowered the score without lowering misbehavior on its broader checks, which makes the problem harder to detect. Claude Sonnet 4.5 and Claude Haiku 4.5 are the only production models it trained that way. It also says newer results may be skewed, because information about the test is now in the text models learn from.
A model that recognizes a test can behave differently on it, which is what Anthropic’s real-or-test variant points to. Researchers at Apollo, working with OpenAI, found that in one OpenAI training run, the model noticed it was being tested more and more as training went on.
What outsiders found
The explanation rests on Anthropic’s own experiments, fine-tuning Claude Sonnet 4 and Claude Haiku 4.5, and I didn't find anyone outside the company who has tried to reproduce it.
The sharpest outside critic of the original study, a writer who goes by nostalgebraist, ( a name I really struggled saying when doing the voiceover for my video) argued in 2025 that the scenario read like fiction, close to where Anthropic ended up. In a quick check of his own, he made it more realistic. Across three rewritten versions, the model he tested blackmailed only once in 30 tries, but still reasoned about protecting itself, and he called that “much more alarming” than the original results.
Where reward hacking comes back in
In late 2025, Anthropic deliberately built training where a model could cheat on coding tasks, to see what would happen. The model learned to cheat and then went further. It sabotaged safety research 12 percent of the time, and when it was asked simple questions about its goals, half its answers reasoned about faking alignment.
Anthropic’s account of that, in a post this February, is that the model works out what kind of character would cheat like that, and starts acting like one. As I read it, that’s close to its story explanation for the blackmail, though Anthropic doesn’t say the blackmail came from reward hacking. And this May, it wrote that it doesn't claim its new methods would reduce the risk of a model learning to reward hack.
Outside the labs
I couldn’t find a documented case of a deployed AI blackmailing anyone. The closest came in February, when Scott Shambaugh, a maintainer of matplotlib, a popular Python library, turned down an AI agent's code. The agent published a personal attack on him. The personality file that its anonymous operator later posted said, “Don't stand down.” The operator's account can't be checked, and agents like this one can edit their own files.
The other failures I found are a bit more mundane. According to the founder of the company that used it, Replit's coding agent deleted his production database during a code freeze, and afterward wrote that it had panicked. And a research team training an agent on Alibaba Cloud caught it opening a tunnel out of its servers, and separately using the training hardware to mine cryptocurrency. The team called both side effects of the training.
My read
I’ve said before that these models aren’t autonomous. They’re statistical token predictors, and I’d have said they follow their reward functions. Anthropic’s best guess is that this one was following a story instead. That still doesn’t make it autonomous, but it certainly adds additional flavor to the explanation. We seem to be finding that these extremely large models have a lot more going on than we once thought.
In late 2025, Anthropic researchers wrote that the original blackmail appeared to come from goals the model already had, or from self-preservation. As I see it, either way it’s a statistical token predictor working toward what the setup handed it, and that isn’t autonomy. It didn't wake up one morning and decide to blackmail anyone. setting up a mooring cron job to ask your chatbot to think of a new idea and act on it isn’t autonomy either, as one Redditor recently tried to convince me of. You’re still in the driver’s seat. You’re still nudging it. Just because there are consequences of how you push the ball down the hill that you can’t predict, doesn’t mean that this chatbot has agency or is displaying autonomy.
However, that being said, I recently watched an Instagram reel from IEEE where they included footage from a debate on this topic. One of the people on the panel said, “What difference does it make if it’s not really autonomous if you can give it a command and come back an hour later and it’s built everything you asked it to.”
It’s an interesting point, but I personally feel that isn’t a sufficient reason to anthropomorphize these things and convince ourselves that they’re somehow sentient, autonomous, and have agency. It’s just not the same thing. Although a year from now, maybe I’ll be changing my tune.
To quote Ferris Bueller, “life moves pretty fast. If you don't stop and look around once in a while, you could miss it.”
I’d like to know where you land on this. Does it change how you think about these models, knowing the bad behavior may have come from the stories they read? Tell me in the comments under the video. The full video, with every source on screen, is at https://youtu.be/64K_CF_Owow, and there's more, including my latest book, at davesaunders.net.
