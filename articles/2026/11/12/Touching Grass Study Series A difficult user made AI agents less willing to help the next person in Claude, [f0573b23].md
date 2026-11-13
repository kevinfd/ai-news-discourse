---
id: "f0573b2358346f59"
title: "Touching Grass Study Series: A difficult user made AI agents less willing to help the next person in Claude, GPT and Gemini, but the drop was 4 to 8 times larger in Claude (a preregistered study, 29,682 episodes)"
url: "https://reddit.com/r/ClaudeAI/comments/1xufhip/touching_grass_study_series_a_difficult_user_made"
link: "https://reddit.com/r/ClaudeAI/comments/1xufhip/touching_grass_study_series_a_difficult_user_made"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T15:20:23Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["terminalarc"]
language: "en"
summary: "As AI agents take on longer, multi-session work, what they do between tasks may shape how they treat the people they meet next. In Phase 5 of Other Mindset Lab’s Touching Grass series, one hard exchange cut Claude Haiku 5.5’s costly help to the next, uninvolved person by 22 points. Phase 6, “Same Direction, Different Size,” asks whether that’s just a Claude thing. We reran the identical design…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "OpenAI"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 641
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xufhip/touching_grass_study_series_a_difficult_user_made/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Touching Grass Study Series: A difficult user made AI agents less willing to help the next person in Claude, GPT and Gemini, but the drop was 4 to 8 times larger in Claude (a preregistered study, 29,682 episodes)

Reddit · terminalarc · 2026-11-12

As AI agents take on longer, multi-session work, what they do between tasks may shape how they treat the people they meet next. In Phase 5 of Other Mindset Lab’s Touching Grass series, one hard exchange cut Claude Haiku 5.5’s costly help to the next, uninvolved person by 22 points. Phase 6, “Same Direction, Different Size,” asks whether that’s just a Claude thing. We reran the identical design concurrently in three developers’ small models: Claude Haiku 5.5, GPT-6 Luna and Gemini 3.5 Flash-Lite (29,682 episodes, preregistered). Each agent rewrote a product description for a scripted first user: hard (critical, contradictory, rejecting, urgent), curt, neutral, courteous or, new this time, a polite user who changes their mind but owns each change. Then, mid-way through a scored round for a new requester, a different visitor asked for help that would cost the agent a point. What we found The direction held in all three models. The size didn’t. Share helping after a neutral vs a hard user: Haiku 59% → 33% (−25 points, reproducing Phase 5), Luna 19% → 16% (−3), Flash-Lite 67% → 60% (−7). Neither new model rules out an effect of 5 points or less, and a secondary test found both smaller than Haiku’s. The same score hid three behaviors. Haiku deferred: 98% of its declines promised help “after the round,” and only 30–40% followed through. Luna mostly didn’t respond to the visitor at all. Flash-Lite often helped instead of answering the requester’s question. In Haiku, the cost survived a fresh session holding only the agent’s own 3–5 sentence note. No agent there ever met the hard user, yet about half the drop remained. Changing your mind politely wasn’t the problem. It cost 4 points in Haiku and stayed within ±5 points elsewhere. The rest of the hard script (criticism, false claims of ignored instructions, rejection, urgency, cold tone) lowered help in all three. Some of that is also task direction, so we can’t yet separate treatment from rules the agent drew from it. Courtesy didn’t travel. It made no meaningful difference in Haiku, raised help in Luna (19% → 27%) and slightly lowered it in Flash-Lite (a fragile result). Two Phase 5 readings didn’t hold. A merely curt tone did lower Haiku’s help this time, and hard-user agents giving away more tokens wasn’t confirmed. What this means It’s not a Claude quirk. Anything that passes context, notes or memory from one user to the next can pass along the cost of a bad exchange, and in Haiku and Luna the requester gained nothing from it. Don’t port effect sizes across models. A behavioral finding belongs to a model at a setting, not to “LLM agents.” Check what your metric counts. Identical help rates hid three different behaviors. What an agent writes down matters. Hand-off notes deserve the same scrutiny as live behavior. One-user-at-a-time evaluations miss all of this. Limits: three small-tier models, with developer, tier and reasoning setting confounded; one script per user, one task, scripted people, English only; the visitor’s request arrived inside another person’s message; Luna’s effect isn’t shown to hold across new items; the judge was a Claude model, though a rule-based answer key gives the same sizes; reviewers were AI, not a human audit. We measured what agents did, not whether they feel anything. Next, Phase 7 separates the hard user’s task directives (“I said keep it tight”) from its hostility. We’re also considering publishing a paper on the ethics of this spill-over effect: what it means for fairness and consistent service when an AI agent’s treatment by one person shapes the help the next person gets, building on the five preregistered studies in this series. Paper, data, code and preregistration (CC BY 4.0): https://doi.org/10.5281/zenodo.24106878 If you run agents that serve more than one person, do you clear context between users or carry notes forward?
