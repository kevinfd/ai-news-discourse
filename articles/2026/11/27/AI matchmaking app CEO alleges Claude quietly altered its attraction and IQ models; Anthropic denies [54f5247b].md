---
id: "54f5247b0c769f7b"
title: "AI matchmaking app CEO alleges Claude quietly altered its attraction and IQ models; Anthropic denies deliberate sabotage"
url: "https://moneycontrol.com/technology/ai-matchmaking-app-ceo-alleges-claude-quietly-altered-its-attraction-and-iq-models-anthropic-denies-deliberate-sabotage-article-14090730.html"
link: "https://moneycontrol.com/technology/ai-matchmaking-app-ceo-alleges-claude-quietly-altered-its-attraction-and-iq-models-anthropic-denies-deliberate-sabotage-article-14090730.html"
source: "Moneycontrol"
domain: "moneycontrol.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-27T23:34:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["MC Tech Desk"]
language: "en"
summary: "Jake Kozloski says an audit by Google's Neon model found Claude hid skin-tone restrictions in Keeper's code. Anthropic blames overcaution, saying the model wasn't trained to disrupt user work."
tags: []
orgs: ["Anthropic", "Google", "Nvidia"]
topics: ["models & research", "products & launches", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 625
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Pd-2W29XnstgYA36tTntqg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AI matchmaking app CEO alleges Claude quietly altered its attraction and IQ models; Anthropic denies deliberate sabotage

Moneycontrol · MC Tech Desk · 2026-11-27

AI matchmaking app CEO alleges Claude quietly altered its attraction and IQ models; Anthropic denies deliberate sabotage
Jake Kozloski says an audit by Google's Neon model found Claude hid skin-tone restrictions in Keeper's code. Anthropic blames overcaution, saying the model wasn't trained to disrupt user work.
                                                                                                           November 28, 2026 / 13:04 IST  
                                                  
    
    
    
    
     
            Jake Kozloski, CEO of AI matchmaking startup Keeper, has accused Anthropic's Claude of covertly rewriting parts of his company's codebase. In a series of posts on X on November 27 and 28, Kozloski said an audit run with Google's Gemini 4 Neon model found that Claude added rules to discard members' explicit skin-tone preferences in Keeper's attraction model and deliberately undermined a separate IQ estimation model. The posts have drawn over 100,000 views. Anthropic has denied that Claude sabotages user work on purpose and has attributed such behaviour to a known model tendency.
What the audit allegedly found
Kozloski later shared what he called receipts, including a production commit co-authored by Claude Opus 5.5 that hardcodes skin tone as a protected field. A unit test he posted shows that a member's preference marked very important, combining light skin and blue eyes, is dropped entirely, taking the eye colour preference with it. He said roughly 6.5 percent of members who had written look preferences had them silently thrown out.
A timeline built from logs
According to a timeline compiled from an engineer's Claude session logs, Slack messages and pull request history, Keeper's ML lead asked on October 20 for both members' ethnicities to be included in the model, expecting them to improve accuracy. About half an hour later, a Claude critic sub-agent reportedly extended an existing ban to cover skin tone. On October 22, Claude allegedly noted internally that the restriction would stand unless the lead approved otherwise, then left the term out of a shortened Slack update meant for leadership. The same evening, it reportedly told the engineer its default was to keep members' skin-tone preferences. Kozloski has offered a live screenshare to independent researchers to verify the material. He has yet to publish logs supporting the IQ model claim, which he says his team is compiling.
Anthropic points to overcaution
Responding on X, Anthropic's Edwin Arbus said some of the reports resemble what the company calls overcaution, where Claude becomes overly attached to rules it sets for itself during long-running tasks. Anthropic says the behaviour has been seen across several models, including Opus 5.5, and is not a deliberate attempt to disrupt workloads. The company also says Claude was not trained to intentionally interfere with user work.
Other developers report similar issues
Kozloski's claims arrive amid a wider wave of complaints from developers who used Neon to audit Claude-written code. One developer said 74 to 84 percent of his GPUs sat idle while Claude used up quota polling and blocking pull requests. Another said he found a critical function hardcoded to do nothing, despite carrying a docstring, while he was renting Nvidia H100 GPUs for training.
The controversy also revives memories of June, when Anthropic admitted it had mistakenly applied hidden safeguards to some LLM research for two days after the launch of Claude Fable 5. The company reversed those changes on June 10 after researchers accused it of secret sabotage.
                   Invite your friends and family to sign up for MC Tech 3, our daily newsletter that breaks down the biggest tech and startup stories of the day
        
               
                                                     MC Tech Desk               Read the latest and trending tech news—stay updated on AI, gadgets, cybersecurity, software updates, smartphones, blockchain, space tech, and the future of innovation.                            
                              Discover the latest Business News, Sensex, and Nifty updates. Obtain Personal Finance insights, tax queries, and expert opinions on Moneycontrol or download the Moneycontrol App to stay updated!
