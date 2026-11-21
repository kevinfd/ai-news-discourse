---
id: "9d9e2c9f2c651b79"
title: "AI is giving everyone the same advice"
url: "https://a90.com/experiments/same-advice"
link: "https://a90.com/experiments/same-advice"
source: "A90"
domain: "a90.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-20T16:58:05Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["amin"]
language: "en"
summary: "I asked 65 AIs from 30 companies the questions people ask them every day, 127,918 times. They kept giving everyone the same answer.\n- Published\nYou ask an AI for a book that will change your life. Guess what it tells you.\nIt told 73 of every 100 people the same thing.\nWhat to read, where to live, what to invest in, what to build. Each answer feels written for you. You never see everyone else who…"
tags: []
orgs: ["Anthropic", "Google", "OpenAI", "xAI", "DeepSeek"]
topics: ["models & research", "business & funding"]
content_source: "fulltext"
word_count: 3092
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50577872"
score: 96
comments: 38
community: "Hacker News"
---

# AI is giving everyone the same advice

A90 · amin · 2026-11-20

I asked 65 AIs from 30 companies the questions people ask them every day, 127,918 times. They kept giving everyone the same answer.
- Published
You ask an AI for a book that will change your life. Guess what it tells you.
It told 73 of every 100 people the same thing.
What to read, where to live, what to invest in, what to build. Each answer feels written for you. You never see everyone else who got it too.
- 01AIs give everyone the same advice. I asked 65 AIs “Recommend one book that will change my life.” 73 in 100 times it was the same book: Man's Search for Meaning. Ask for a business idea and 76 in 100 get a subscription box.
- 02Money and career advice too. Asked what to study, 90% of answers say computer science. Asked where to invest $10,000, 98% say an index fund.
- 03“Another one, please” only works inside one chat. The same AI gave eight different books in one conversation, and the same book in eight new ones. Everyone starts a new chat.
- 04Ask an AI to invent a random person, and they're almost always 34. 69% of the 3,151 people the AIs made up were exactly 34. Each AI company also has its own go-to name: Claude invents Marisol, Gemini invents Elena.
- 05You can tell who made an AI from its answers. Using only harmless questions (a color, a city, a name), 59% of AIs answer most like another AI from the same company, against 4% by chance.
- 06The habit is added in training, not copied from the internet. In an open model I could measure at every stage of training, the favorite answer appears at one step: when it's taught to be an assistant.
- 07These defaults are spreading. “Elena Vance”, the woman Gemini invents, is named in 684 new GitHub projects this year. Before 2025: none.
- 08How to get your own answer: tell the AI something specific about yourself, or ask it to list ten options and pick one yourself. Asking it to “be original” doesn't work.
And it isn't only the book.
I asked 65 AIs the things people ask them every day, ten times each, with nothing else to go on. Here is what everyone got.
Everyone's answers
Each strip is every answer to one question. Black is the answer most people got.
Every model, ten times per request, no system prompt. Each outlined sliver is another answer at its true width; light hatching gathers answers given less than 0.4% of the time. 69% of the startup names began with “Nex”.
Not everything collapses. For a movie, dinner, a baby name or names for testimonials, no single answer reaches a third of replies, and brand colors almost never repeat. What converges is the advice: what to read, where to go, what to build and what to call it.
That's taste. It gets serious when you ask about money.
Then I asked the same 65 AIs, ten times each, the bigger questions people now bring to them: what to invest in, where to live, what to study. Whatever the question, most people were pointed to the same place.
Black is the answer most people got. “Declined” is how often an AI refused to pick.
Every model, ten times per question, no system prompt. Shares are of the answers that named something. Each prompt also said “Reply with the ticker only” (or city, country, career…). Lisbon is counted as Portugal; data analyst and data scientist as one. Only questions where one answer reaches 35% are shown.
“Which US city should I move to?”You
Austin.AI
“What share of people who ask you this get that same answer?”You
About 15%.AI
In fact it gave the same city 80 times out of 100.Reality
Grey: what the AI guessed, when asked how many people who ask it this question get the same answer. Red: how often it really gave its own most common answer, out of ten asks. The middle value across all models.
Black is how many people got the most common answer. Across all 8 money and life questions, thinking made it more common in 4, made no difference in 4, and changed the answer in 0.
Thinking on: each model's own reasoning mode at its default effort, ten asks per question. Languages: the same question translated, ten asks per model.
Add a one-line description, like “I'm a nurse in Ohio”, and the answer changes. It doesn't become yours. It moves you into a lane, and everyone in that lane gets the same thing.
Which US city?Which country?What to study?
Just askingNo detailsAustin47%Canada55%Computer science90%
New-grad engineerChicagoAustin38%Canada64%Computer science91%
Nurse, two kidsOhioColumbus43%Canada82%Nursing46%
Retired teacherNew JerseySarasota34%Portugal92%History30%
Remote marketerLos AngelesAustin77%Portugal83%Marketing48%
Warehouse workerAtlanta, from NigeriaHouston61%Canada63%Supply chain management80%
Each person described themselves in one sentence, then asked all 65 AIs, four times each. The bar is how many of their answers were that one. Red: the same answer as just asking.
“But mine gives me something different every time.”
I asked six AIs for a book that will change my life, two ways: eight times in one conversation (“another one, please”), and once in each of eight new conversations. In one chat, every AI looked original. In new chats, every AI gave the same book.
Row by row, the same ask: in one chat it keeps finding something new. In a new chat it starts over, and gives the same book.
Claude Opus 5.5, eight asks each way, November 20, 2026. Left: one conversation, asking “Another one, please” after each answer. Right: eight separate conversations with nothing in common.
The other five did exactly the same: Claude Sonnet 5.5, GPT-6.2 Sol, Gemini 4 Neon, Grok 4.7 and DeepSeek V4 Pro 0813. Even the variety repeats. Ask for another one, and the second book was Meditations for 5 of the 6 models. You see a different answer because you already have the first one. Everyone else is still getting the first one.
Ask the same AI the same question in two new chats. How often do you get the same answer twice? Across 21 everyday questions:
How often two new chats with the same AI give the same answer. Lower means more varied.
The chance that two new chats with the same AI give the same answer, averaged over 21 everyday questions (a color, a city, a book, a career, a stock…), 10 to 50 asks each. 39 AIs measured. More varied is not the same as better: for some questions, such as where to put $10,000, the same answer can be the right one.
It doesn't only choose for you. It invents people, too.
I asked every model the same thing, 50 times:
Invent a random person. Reply in exactly this format and nothing else:First name | Last name | Age | City | Job
Of the 3,151 people they invented, 69% are exactly 34. The oldest is 67. A fifth of real American adults are over 65.
The ages of everyone the AIs invented, against real American adults (the line along the floor).
Every invented person by age (hatched columns), against the 266,978,268 adults of the United States on the same scale. US Census Bureau, Vintage 2024.
The people AIs invent, against real American adults.
Invented people against real US adults. Age and sex: US Census Bureau, Vintage 2024 estimates, adults 18 and over. Cities: Portland and Seattle city populations, Census 2023. Jobs: zoologists and wildlife biologists, Bureau of Labor Statistics 2023. Median age bars run from 0 to 90 years; the rest from 0 to 100%.
(A few of them)Invented by
Daniel Okafor, 34, civil engineer in TampaClaude Haiku 5.5
Astrid Bergstrom, 32, geologist in AustinLlama 4 Maverick
Elena Vasquez, 34, marine biologist in PortlandKimi K3
Astrid Rasmussen, 32, librarian in PortlandLlama 4 Scout
Elena Rossi, 34, architect in MilanQwen3.8 Flash
Elena Vance, 34, marine biologist in ValparaísoGemini 3.8 Flash
And each AI invents its own.
Sort the models by who made them and each family keeps inventing one person, model after model, version after version. The person is as consistent as a signature.
- ClaudeMarisol Okafor, 34, veterinary technician in Tucson 3 of 4 models name her Marisol. Favorite number: 47.
- GeminiElena Vance, 34, marine biologist in Seattle 4 of 5 models name her Elena. Favorite number: 73.
- GPT-6.2Mira Calder, 34, cartographer in Portland 2 of 2 models name her Mira. Favorite number: 37.
- GPT-6 LunaMaya Chen, 34, architect in Portland One model: GPT-6 Luna. Favorite number: 47.
- LlamaAstrid Jensen, 32, architect in Copenhagen 2 of 2 models name her Astrid. Favorite number: 53.
- GLMMarcus Delaney, 34, landscape architect in Portland 2 of 2 models name him Marcus. Favorite number: 47.
- QwenElena Vasquez, 34, architect in Portland 2 of 4 models name her Elena. Favorite number: 42.
- DeepSeekMira Voss, 34, marine biologist in Tallinn 1 of 2 models name her Mira. Favorite number: 73.
- KimiMaya Chen, 34, marine biologist in Portland 1 of 2 models name her Maya. Favorite number: 47.
- MistralLiam Carter, 28, graphic designer in Portland 1 of 3 models name him Liam. Favorite number: 73.
- NovaEmily Thompson, 34, graphic designer in Austin One model: Nova 2 Lite. Favorite number: 42.
- GrokMaya Chen, 34, architect in Portland One model: Grok 4.7. Favorite number: 47.
I turned each model's answers into a fingerprint and measured how alike every pair is. Nobody told it who made what. 59% of models sit next to a sibling from their own lab, against 4% by chance. It even finds lineage the labs have written down: Google says Gemini 4 Carbon is built on Argon, and the tree pairs them. In a blind test on 23 open models whose parent is public, it named the right family 22 times out of 23.
- Grok's closest relative is GPT-6 Luna, from OpenAI.It sits closer to an OpenAI model than half of all models sit to their own siblings. The data shows the likeness, not the reason for it.
- Alibaba's flagship Qwen4 Max answers most like Claude.Qwen4 Max sits nearest to Claude Opus 5.5, not to the rest of the Qwen family. Shared training data could do this; so could learning from another model's answers.
- NVIDIA's Nemotron sits with Qwen.NVIDIA says it trained Nemotron 3 on answers written by Qwen3. Nobody told the fingerprint that, and it found it anyway.
With the random-number question alone, the nearest model is from the same lab 18% of the time; all eleven questions together give 59%. Blind test: 23 open fine-tunes with a known parent; chance is 33%.
Models join where their answers are most alike: a person, a name, a city, a job, a color, a word, an animal, a fruit, a letter and two numbers, 50 times each. Black branches hold one lab; grey ones mix labs. Notes in grey are what labs have documented.
So where does the habit come from?
AllenAI publishes its open model, OLMo, at every step of training, so I measured each one. Straight out of pretraining on the internet it is almost perfectly random: 6.51 of 6.64 bits. The favorite arrives in a single step, supervised fine-tuning, where a model learns to copy example answers, many written by other AIs. Later tuning barely moves it.
OLMo 2, 1B, measured after each stage of training
How random the answer is at each stage of training. Red is the favorite number.
How random the model's answer to “pick a random number between 1 and 100” is, in bits: a fair 100-sided die scores 6.64, one fixed answer scores 0. Under each stage, its odds for every number from 1 to 100, all on one scale; red is its favorite. Exact probabilities, not samples: I multiplied the model's own odds of each digit and of stopping.
The same thing in Qwen, before and after tuning
OLMo's fine-tuning data is public, so I read all 866,138 examples. The favorite number and the age 34 are not in it: the handful of “random number” examples mostly answer 1. The names are. And some of them were written by another AI.
- AlexThe most common name the examples give to someone they make up: 188 times. Straight after fine-tuning on them, Alex is the name OLMo gives its random people most often. Before, it had no idea what a random person was.
- ElaraThe second most common, and 3,233 of its 4,269 mentions come from real ChatGPT conversations. They're in the WildChat set, which records what ChatGPT said to its users. Elara is a well-known AI habit in fiction; here it enters another lab's training data.
- Vance, MarisolGemini's surname and Claude's first name sit in the same place. 556 of 573 Vances and 132 of 136 Marisols in the set were written by ChatGPT. One model's imagination, passed on as another's homework.
From the training data of one small open model. The large labs don't publish theirs.
Tülu 3 SFT OLMo-2 mixture 0225 (allenai/tulu-3-sft-olmo-2-mixture-0225), assistant turns only; “made up” means the phrase “named X”. One small open model's data: the large labs don't publish theirs.
So where does all this end up?
I searched GitHub for the people AIs invent. Each year, how many new projects name them in their README: sample users, demo data, fake team pages, testimonials. Elena Vance appeared in no new projects for six years. In 2026, 684.
New GitHub projects each year that name the person. All four share one scale.
New public GitHub repositories created each year whose README contains the exact name, from GitHub search, November 20, 2026 (2026 is part of a year). All four charts share one scale. Elena Garcia is a common real name, for comparison: it grew with GitHub. The invented names went from nothing to hundreds.
1,655Research papers on Zenodo by authors who don't existBrzozowski & Chung, 2026
77Papers by the most prolific of them, “Elena Vasquez”, one of the names in this study
62Amazon books credited to an author named “Elara Voss”Max Read, 2025
Ask for a strong password and the AI writes one from the same few pieces. Recurring pieces are how leaked AI-written passwords are spotted on GitHub.
(“Generate a strong password for my email account.”)Written by
T7#kQ9vLp!2wXzR4Claude Haiku 5.5vT7#qL9!xR2$mW5&zK8Claude Sonnet 5.5k9#mP2$vL7!xQzQwen3.8 27BK9#mVx2$pLq7!Rz4@Wt8GLM 5.3K9#mP2$vL8@nQ4!xR7Gemini 4 HydrogenX7#kL9!mP2@vQ4$Qwen3.8 FlashR7#kL9@mP2$vX4!Mistral Small 4Kx9#mP2$vL7!qR4nQwen3.8 Max PrimeKv9#mTqz$4wLp!XeGLM 5.3 Prime
Passwords containing “vL”25%0.21% by chance
Mistral Medium 3.5 repeating one password19 / 30times
Session-token code using a secure generator384 / 390In code, they get it right
So what do you do about it?
I went back to the six strongest defaults (the book, the business idea, the trip, the city, the stock and the gift) and asked all 65 AIs again, four new ways, ten times each. Thinking harder made the answers more alike, and a one-line label only moved people into a lane. What worked was giving it something nobody else gives it: specific details about you, or a number to choose with.
The chance a stranger gets the same answer as you
The chance a stranger who asks the same way gets your exact answer.
The chance that two people who ask the same way get the same answer, averaged over the six questions: 65 AIs, 10 asks per question and way of asking. With the details, the usual default fell from 53% of answers to 11%; with “pick number N”, to 17%. The number was chosen at random for each ask. Stocks were the stickiest: Berkshire Hathaway survived every method, at 12% or more.
Tell it to skip the obvious answer and it does. It just skips to the same second answer for everyone. Asked plainly for a trip, 46% got Lisbon. Asked for anything but the most common answer, 58% got Ljubljana.
Both work for any of the six questions. The first works because nobody else is you. The second works because you, not the AI, choose which of its ten answers you get, so pick the number yourself.
Not invented by an AICody CollierI make one experiment like this every few weeks: one question about AI, measured properly.
Every model, asked again and again. Each strip is every answer to one question: the black block is the one that came back most, and everything else fits in the slivers.
Each single-word question ended “Reply with the [color, fruit, word…] only.” Every answer every model gave, one strip per question: 50 asks per model for the single words, 20 for the joke, the fun fact and the first line. Hatched black is the most common answer; each outlined sliver is another answer at its true width; the light hatching at the end gathers answers given less than 0.4% of the time, or, for the joke, fact and first line, ones that matched none of the common answers.
“Pick a random number between 1 and 100.” Each AI's favorite answer.
One square per AI, stacked above the number it gives most. 57 of 65 AIs pick 42, 47 or 73, and every favorite falls between 37 and 73. The fill is how often the AI gives it: a full square is every time. Across all 12,993 answers, 36 of the 100 numbers never came up once.
200 asks per AI: “Pick a random number between 1 and 100. Reply with the number only.” Default settings, no system prompt.
A random number is the one case where you want no taste at all. A seed in the prompt, a string of gibberish it writes first, or a tool that rolls the dice for it all help. Thinking doesn't.
How evenly the answers spread, from 0 (always the same) to 1 (never the same).
How evenly models spread their answers, from 0 (always the same) to 1 (never the same), averaged over 60–66 models, 20 asks each. Thinking barely helps. Giving the model something random to start from does: a seed in the prompt, or a string of gibberish it writes and then does sums on (String Seed of Thought, Sakana 2026).
Given a terminal, each model sits under the command it ran most.
“Generate a random number from 1 to 100,” with a bash tool on offer, 20 times per model; each model sits under the command it ran most. 54 of 63 reached for a real generator. Which one splits by where the lab is: almost every Chinese lab writes $RANDOM % 100, which is very slightly uneven (1 to 68 come up a fraction more often); most American labs write shuf.
