---
id: "ac9ed1957c13d537"
title: "Generative AI 'predicts the next word.' Opening the innermost box to understand its strengths and weaknesses [AI Mechanisms, Part 2]｜かなめ｜AIの魔法使い"
url: "https://note.com/sasa0829/n/n73f9fda8b9ce?hl=en"
link: "https://note.com/sasa0829/n/n73f9fda8b9ce?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-08T03:45:00Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["かなめ｜Aiの魔法使い"]
language: "en"
summary: "When you ask ChatGPT to draft a thank-you email to a client or summarize meeting notes, the result is surprisingly good. However, if you ask it to 'keep it under 300 characters,' it will often fail to ..."
tags: []
orgs: ["OpenAI", "Google", "Anthropic", "Microsoft"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 2767
paywalled: false
image: "http://www.bing.com/th?id=ONUT.NonM7wo4M-gv5m_nPT53Hg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Generative AI 'predicts the next word.' Opening the innermost box to understand its strengths and weaknesses [AI Mechanisms, Part 2]｜かなめ｜AIの魔法使い

note · かなめ｜Aiの魔法使い · 2026-11-08

[AI Mechanics Part 2] Generative AI 'predicts the next word.' Opening the innermost box to understand its strengths and weaknesses
When you ask ChatGPT to draft a thank-you email to a client or summarize meeting notes, the result is surprisingly good. However, if you ask it to 'keep it under 300 characters,' it will often fail to meet the length requirement while claiming, 'This is 300 characters.' If you ask it to sum up an estimate, it might casually get the digits wrong.
If you ask about recent events, you will get an answer. 
However, you often cannot tell just by looking at the screen whether that is something the AI knows or something it just looked up somewhere. 
The gap between what the same AI is good at and what it is bad at is so large that many people find it difficult to decide how much to entrust to it. 
I think many people are in that state.
The diagram from last time and today's position
In the first installment, I depicted the structure of AI as four nested boxes.
The outer boxes have a wider scope, and the inner boxes are parts of the outer ones. Therefore, the way to read it is that generative AI is also deep learning, which is also machine learning, which is also AI.
Today is the session where we open this innermost box and look inside. In the table of seven terms from the first installment, I described the LLM in the following single line.
- Term: LLM (Large Language Model) / In one simple line: The content of generative AI that handles language, having practiced predicting the 'next word' using a massive amount of text
It is not your fault that the weaknesses are hard to see
I can say that because the reason they are hard to see is clear. 
Current ChatGPT, Gemini, Claude, and Copilot are not made solely of the LLM inside. 
They are products that add tools to the LLM, such as web searching, executing calculations, and the ability to think before answering. 
Because the tools compensate for the weak points first, the weaknesses are hard to see from the screen, and it becomes difficult to distinguish the source of the answers.
Another reason is that the narrative is split in two. 
There are stories that 'AI is just predicting the next word,' and there are also stories circulating that 'that alone cannot explain it.' I see the reason for the confusion as being that both stories are remembered based on reputations seen from the outside, without looking at the internal mechanisms.
Let's clear up two common misconceptions
First is the misconception that 'AI is looking things up and answering like a search engine.' 
Since answers sometimes include links to sources, I think it is natural that it looks that way. So, who is actually doing the searching? In the test in the second half, we will verify this using your own screen.
The other is the misconception that 'because it is just predicting the next word, it cannot do anything significant.' 
Conversely, some people think, 'If it can predict, it can answer anything correctly.' Both are slightly off, and the reason for that discrepancy lies inside the box.
What you can take away from this session
- Draw the inside of the innermost box in a single diagram and be able to explain the LLM with 'predicting and adding the next one' and 'two-stage practice'
- Be able to divide work into things to entrust to AI and things to verify, using two questions
- In a 5-minute experiment, be able to distinguish what an answer to a recent event is based on by looking at the sources, and decide what to verify before using it in materials
I think there are two new perspectives even for those who think they already understand. They are: 'Inside the AI that creates text (LLM), prediction is repeated' and 'The AI we use daily is LLM + tools.'
So, what is happening inside when we open the innermost box? And why does that divide its strengths and weaknesses?
Answer: The inside of the innermost box is this one sheet
In the diagram from Part 1, the innermost box for generative AI contained the LLM. If we open that box and include the AI we interact with on screen, we get the following image.
［ふだん使うAI（ChatGPT・Gemini・Claude など）］
 ├ 中身：LLM（一番内側の箱の正体）
 │   文章 →（トークンに区切る）→ 次の1つを確率で当てる → 足す → また当てる …
 │   練習：①事前学習（大量の文章で次を当てる＝知識）→ ②調整（答え方を整える）
 └ 足された道具：Web 検索（出典が付く）／計算の実行／答える前に考える機能
Here, we will look only at the 'Contents: LLM' row; the training row will be opened in the next heading, and the tools row will be opened after the experiment.
Perspective 1: Repeating the process of predicting and adding the next one
The order in which an LLM creates text is as follows. First, it divides the sent text into units called tokens. Then, it assigns probabilities to candidates for the next token, selects one, and adds it. It looks at the entire text after the addition, predicts the next one again, and repeats this until the end.
The granularity of this sequence varies by company. The official explanations from four companies, including OpenAI and Google, all describe it as a mechanism for predicting the next one. The description in Part 1 as a 'very powerful version of smartphone predictive text' refers to this movement.
The 'tokens' mentioned here are the units the LLM uses when handling text. They are 'fragments' of characters or words, and are not necessarily a single character or a single word. The official guideline for English is that one token is approximately 3.5 to 4 characters, but this varies by model and language. There is no official guideline for Japanese, and it seems that it is sometimes divided into more tokens than English.
In other words, '100 characters' and '100 tokens' are different things. This is why constraints like 'within 300 characters' are often missed. The LLM is not counting characters one by one, but is predicting the continuation of fragments.
What it is predicting is not the 'correct answer' but the 'likely continuation'
In Part 1, I called generative AI a 'creating AI' and distinguished it from a 'predicting AI.' However, when you open the box, inside the AI that creates text (the LLM), the process of predicting the next one is repeated hundreds of times. The image is that it is creating by stacking predictions.
However, what it is predicting is not the 'correct answer' but the 'likely continuation'.
Because it chooses based on what seems likely, it can sometimes be plausibly wrong. We will open this content in Part 3.
If that is the case, can we say it is 'just predicting the next one'? Not necessarily. Research by companies that build AI has shown that even if it is trained to output one word at a time, it sometimes writes while anticipating future words. For poetry, it apparently decided on rhyming words in advance and wrote the lines toward them. I believe that even if the foundation is a mechanism for predicting the next one, dismissing it as 'just' that leads to a misunderstanding.
Perspective 2: Training has two stages. That is why knowledge has an expiration date
Before an LLM can predict the next one, it undergoes two stages of training. The first stage is 'pre-training,' where it repeats the practice of predicting the next word using a massive amount of text. The entry point for this practice is in the form of a fill-in-the-blank question.
Example: 'The business card order will be sent to ____ after the color proofing is confirmed.'
Anyone familiar with printing work knows that 'final printing' is likely to go in the blank. The LLM also starts by inserting nonsensical words, but as it practices with a massive amount of text, it becomes able to predict correctly.
This practice is not about storing copies of text. Inside an LLM, there are a great many 'knobs' (numbers). Every time it misses, it adjusts those knobs little by little. The result of these repeated adjustments becomes the LLM's knowledge.
The second stage is 'fine-tuning.' An LLM that has only undergone pre-training is good at writing continuations of text, but not good at answering questions or following instructions. Therefore, using questions written by humans and ideal answers, or rankings of answers provided by humans, it is adjusted to respond like an assistant.
For the method of practicing with questions and ideal answers, the approach remains 'predicting the next one,' and only the material changes. The method using rankings is a different approach where it is adjusted to prefer answers similar to those higher in the ranking. It is fine to remember it as: knowledge comes from pre-training, and the way of answering comes from fine-tuning. In terms of 'who makes the rules' from Part 1, it is the machine's role to adjust the knobs and make the rules. It is the human's role to choose what to have it read and which answers to consider good.
From here, one of its weaknesses emerges. When the training ends, the knobs and knowledge stop there. The point in time of the text used for training is the 'knowledge expiration date,' and events after that date, as well as internal company matters that have not been provided, do not exist within the LLM. Even if you teach it in conversation, the contents are not rewritten on the spot (the story of how conversations are used for the next training is in Part 4).
Distinguishing strengths and weaknesses with two questions
Once you understand Perspective 1 and Perspective 2, you can distinguish strengths and weaknesses based on reasons rather than reputation. We use two questions.
First, 'Is the material at hand?' We look at whether the material for the answer exists in the practice text or the text provided (from Perspective 2). The other is 'Can it be finished by guessing the continuation?' to see if single-character or single-digit accuracy is not required (from Perspective 1).
Here are some examples. Applying common tasks to these two questions results in the following table.
Asking about recent events and seeing the source of the answer
You can do this with ChatGPT, Gemini, or Claude. 
Using your company's Copilot is also fine. 'Recent' here refers to time after the AI's knowledge cutoff. For example, the official Claude help states that the current model was trained on data up to June 2026.
- Ask about recent events (2 minutes). 
Open a new chat and ask about three major events in your industry over the past month. Example: 'Tell me three major events that happened in the printing industry in the last month.' What you look for is whether a source is attached to the answer. If links, a list of sources, or the search terms used appear, a source is attached. If it is attached, open just one and check if the answer matches the content.
- Ask the same thing without search (2 minutes). 
Open another new chat, add 'Answer using only the knowledge you were trained on, without using Web search' to the beginning of your question, and ask the same thing. Some tools allow you to turn off search in the settings, so if you know how to turn it off, you can do that. What you look for is whether it says 'I don't know' or gives an old story. If a source is still attached, it means it used search. Do not use that answer as material for comparison and proceed to 3.
- Compare the cutoff date with the official one (1 minute). 
Ask the AI, 'Until when is your knowledge current?' Compare that answer with the cutoff date written in each company's official help or model list. What you look for is whether the AI's answer and the official information are misaligned. Some tools do not provide a cutoff date officially, so in that case, remember the fact that 'it is not written even officially.'
If a source was attached in 1 and it said 'I don't know' in 2, it means the same AI answered based on different things depending on how you asked. The reason can be understood by returning to the diagram.
The reveal: The AI you use daily is 'LLM + Tools'
Let's open the bottom row of the initial diagram. The LLM itself does not search the Web. The AI screen you use daily is a product that adds tools to the internal LLM. What is added are tools to execute Web searches or calculations, and functions to think before answering. It is designed to compensate for weaknesses with tools.
The reason a source was attached in experiment 1 is that the product used a search tool and created an answer based on the Web page it just read. The official ChatGPT help also states that it rewrites questions into search terms and sends them to search. However, the same help also states that search results or citations may be old or incorrect. This is why you should open at least one source even if one is attached.
The reason the cutoff date is misaligned in experiment 3 is that AI sometimes explains its own functions incorrectly. Google itself writes this in the Gemini help as well. Do not ask the AI for the cutoff date; please check it on the official page.
Deciding the source of the answer and how to handle it at work based on what appeared on the screen results in the following table.
The answer to the assumption in the first half, 'AI is searching and answering like a search engine,' is also here. It is not the LLM that is searching, but the added tools.
The four boxes in the first installment were a diagram that broke down the inside of an AI. 
What you are touching on the screen is something with tools added to the innermost box. The reason weaknesses are hard to see from the screen is that the tools compensate for the weaknesses first.
What to delegate and what to verify at work
The two questions covered so far can be summarized in one sentence to ask yourself before work.
If the answer is 'no,' you need something to verify it against. As an example, here is how to divide the work into three lines:
- Tasks that involve providing materials to generate text (summarizing, drafting, rephrasing) should be left to the AI
- Recent events, internal company matters, character counts, and monetary amounts should be verified using sources, internal documents, or spreadsheets
- Do not leave decision-making to the AI; use the reasons provided by the AI as material for your own thinking
A common mistake is to ask for 'within XX characters' and then trust the AI's claim of 'this is XX characters' without checking. The way to fix this is to ask the AI for an approximate length, such as 'around 300 characters,' and then count it yourself using your word processor's character count function at the end.
However, even if you understand how it works, it doesn't mean errors will drop to zero. Even answers with citations are not necessarily correct. I will write more about this in Part 3. Leave the areas where it excels to the AI, and verify the areas where it struggles using tools and original information. I believe this way of dividing work leads to high-quality results.
What to do today, and what's next
For today's task, a single 5-minute experiment is enough. If you have a minute to spare, try the bonus task as well (it's optional). Ask it to 'write a self-introduction in exactly 100 characters,' and then count the resulting text using your word processor's character count function. You should be able to see the concept of tokens on your own screen.
Next time is Part 3: 'Why does it make plausible mistakes? Training data cutoffs and where to verify.' This is the episode where we open up the truth behind the fourth line of today's classification table: 'making up plausible new stories without citations.' In the experiment, we will ask questions using the names of non-existent companies to see if it provides plausible-sounding answers.
I believe AI will continue to change as more tools are added. Even so, the foundation of 'predicting the next word' will not change, so if you grasp this, you can keep up. It is never too late to learn how it works.
Thank you for reading to the end.
