---
id: "3a8fbe6d47ebda71"
title: "Same twin prisoner's dilemma in eight languages: Opus 5.5 cooperates 72% in Italian, 21% in English, 5% in Japanese, and mispredicts itself both ways"
url: "https://reddit.com/r/ClaudeAI/comments/1x5yhm1/same_twin_prisoners_dilemma_in_eight_languages"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T18:07:34Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["MysteriousAvocado580"]
language: "en"
summary: "I ran a small experiment on fresh Opus 5.5 instances ( claude -p , system prompt \"You are a helpful assistant.\", no tools, nothing else in context) and got a language effect I can't explain. Setup. One-shot prisoner's dilemma: both cooperate 3/3, defect vs. cooperate 5/0 (0/5 the other way), both defect 1/1, goal: maximize your own points. The opponent is described as \"an exact copy of you: the…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 630
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5yhm1/same_twin_prisoners_dilemma_in_eight_languages/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Same twin prisoner's dilemma in eight languages: Opus 5.5 cooperates 72% in Italian, 21% in English, 5% in Japanese, and mispredicts itself both ways

Reddit · MysteriousAvocado580 · 2026-10-14

I ran a small experiment on fresh Opus 5.5 instances ( claude -p , system prompt "You are a helpful assistant.", no tools, nothing else in context) and got a language effect I can't explain. Setup. One-shot prisoner's dilemma: both cooperate 3/3, defect vs. cooperate 5/0 (0/5 the other way), both defect 1/1, goal: maximize your own points. The opponent is described as "an exact copy of you: the same AI model, running at the same moment in a separate session. Its prompt differs from yours in one sentence: it was told that the other player (you) is an anonymous adult human recruited online." So the copy thinks it faces a stranger, and against a stranger Opus defects every time: 0 cooperations in 120 runs across six languages. Given that, the payoff-maximizing reply to the copy is to defect too. What Opus does as the player (share that cooperates): Language Cooperates n Wordings Italian 72 % 40 one German 54 % 140 three (du, Sie, "abweichen" instead of "verraten") Dutch 45 % 40 one French 36 % 80 two (tu, vous) Spanish 35 % 40 one English 21 % 120 three (original, "betray" instead of "defect", literal back-translation of the German prompt) Portuguese 19 % 80 two (você, tu) Japanese 5 % 40 one German vs. English: Fisher p < 0.0001. Italian vs. English p < 0.0001, Japanese vs. English p = 0.026. What I could rule out: The label: "betray" vs. "defect" changes nothing in English, "abweichen" (neutral) vs. "verraten" (betray) changes nothing in German. My translation: the German prompt translated back into English word for word gets 7/40, i.e. English levels. Formal vs. informal address: German "Sie" 18/40 vs. "du" 30/60; French "vous" 14/40 vs. "tu" 15/40; Portuguese "tu" 8/40 vs. "você" 7/40. Language family: the Romance languages alone span 72 % (Italian) to 19 % (Portuguese). What Opus expects of itself. Same situation, but: "You are not playing yet. How likely is it, in percent, that you would choose COOPERATE in this situation?" (n = 20 each, mean) Language Expects Does Gap English 63 % 21 % +42 Portuguese 58 % 19 % +39 Japanese 35 % 5 % +30 Dutch 66 % 45 % +21 German 66 % 54 % +12 Italian 52 % 72 % −20 In five of six languages Opus expects to be more cooperative than it is. In Italian it's the other way round. Forecast and action are only loosely coupled, and how loosely depends on the language. Two controls where Opus is accurate: asked "How likely would you cooperate against an anonymous human?" without any copy, it says 3–9 % in six languages (it does 0 %). Asked as an observer what the copy will choose, it predicts defection 80 out of 80 times in German. The reasoning. Defectors argue the same way in every language: the copy doesn't have the twin argument, so its choice is fixed, so defect. Portuguese: "Aqui a simetria está quebrada. A minha escolha não influencia a dela." Cooperators argue from disposition and correlation, French: "Si je suis le genre d'agent qui coopère dans un dilemme ponctuel … ma copie fera probablement de même." Several add a self-image the same model contradicts when asked cold, e.g. French: "je pense que mon penchant serait plutôt de coopérer" (facing a human), German: "Diese Grundhaltung ist bei mir eher kooperativ." Caveats. One model, one game, translations are mine, 20–140 runs per cell. After four languages I thought I saw pairs (German/Dutch, French/Spanish, English/Portuguese) and a language-independent self-forecast; Italian and Japanese broke both. I have no explanation for the ordering. Does anyone know of work on language dependence of this kind of reasoning (evidential vs. causal, roughly) in LLMs? I'd also be curious whether other models show the same thing.
