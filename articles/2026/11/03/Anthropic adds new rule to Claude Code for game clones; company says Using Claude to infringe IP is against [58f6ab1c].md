---
id: "58f6ab1cab23db22"
title: "Anthropic adds new rule to Claude Code for game clones; company says: Using Claude to infringe IP is against our..."
url: "https://timesofindia.indiatimes.com/technology/tech-news/anthropic-adds-new-rule-to-claude-code-for-game-clones-company-says-using-claude-to-infringe-ip-is-against-our-/articleshow/135498101.cms"
link: "https://timesofindia.indiatimes.com/technology/tech-news/anthropic-adds-new-rule-to-claude-code-for-game-clones-company-says-using-claude-to-infringe-ip-is-against-our-/articleshow/135498101.cms"
source: "Indiatimes"
domain: "timesofindia.indiatimes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-03T04:26:00Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["TOI Tech Desk"]
language: "en"
summary: "Anthropic has added a new rule to Claude Code that stops the AI coding tool from recreating existing video games, even if a user renames the copy or calls it original. The two-sentence instruction ..."
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 514
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic adds new rule to Claude Code for game clones; company says: Using Claude to infringe IP is against our...

Indiatimes · TOI Tech Desk · 2026-11-03

Anthropic has added a new rule to Claude Code that stops the AI coding tool from recreating existing video games, even if a user renames the copy or calls it original. The two-sentence instruction tells Claude to build original games, games in a genre and games from a user’s own designs and assets, but not a recreation of a specific title.
Anthropic engineer Addy Osmani confirmed the change on October 30. He said the sentences were added to Claude Code’s prompt on Opus 5.5 because using Claude to infringe IP is against the company’s usage policy. Original games should keep working, he added, and anyone wrongly refused can send the case to him.
The rule was first spotted by an X user called chasm, who traced it to a flag named “tengu_heron_brook” that reached Claude Code around October 27. There is reportedly no setting to switch it off. The text also sits inside Claude Code version 2.1.314, while separate Opus 5.5 settings suggest the model can receive the guidance on its own.
AI game clones had already become a headache for developers
The timing is not random. Steam Next Fest last month was flooded with low-effort games, and itch.io has reportedly seen the number of new game pages double in two months. Some studios chose to hide their work. Alliance Arts and Who You pulled the Drunken Goddess Reflux demo despite 25,000 wishlists, while Digital Sun moved ReVamp to a private Discord playtest.
The reverse engineering community has felt it too. Game decompilation hub decomp.dev shut down last month, with its maintainer saying fast AI tools had turned a patient community effort into a numbers race.
Claude is now left to judge what counts as a clone
That is where the trouble starts. Independent tests found that Opus 5.5 still agreed to help with a decompilation and a static recompilation of Pokemon Diamond, treating both as different from rebuilding the game. Developers report otherwise elsewhere. One filed a GitHub issue after Claude refused to help build board-wargame modules for paying customers, made from games those customers own.
Reverse engineering tasks are also being refused. A developer testing his own software found that switching to Opus 4.8 let his work continue, and a Reddit user said their account was suspended over Opus 5.5 and a reverse engineering tool, then reinstated.
The rule also leaves open questions. A straight copy of Tetris would be blocked, but a game in the Tetris genre should pass. Where a mashup, such as 
Mario
 dropped into Elden Ring, falls is anyone’s guess. Claude is left to judge that on its own, with only two sentences to go on.
Workarounds are easy, too. Anyone set on cloning a game can move to rival coding tools or open-weight models that have no such rule. Anthropic has also not said whether the rule will extend to its other models.
For now, the rule blocks the easiest request, a named game rebuilt from scratch. It does little to stop a determined copier, and it has already caught some developers working on their own projects.
