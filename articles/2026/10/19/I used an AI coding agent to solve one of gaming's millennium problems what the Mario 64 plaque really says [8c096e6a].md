---
id: "8c096e6a6268dc81"
title: "I used an AI coding agent to solve one of gaming's \"millennium problems\": what the Mario 64 plaque really says"
url: "https://reddit.com/r/singularity/comments/1x9x7gw/i_used_an_ai_coding_agent_to_solve_one_of_gamings"
link: "https://reddit.com/r/singularity/comments/1x9x7gw/i_used_an_ai_coding_agent_to_solve_one_of_gamings"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T13:41:33Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["decorator"]
language: "en"
summary: "Each hobby has some problems that can never be solved, and one of these for Nintendo fans is the plaque on the castle fountain in Super Mario 64, which has been the subject of debate since 1996 and has never reached a conclusion. It is essentially the gaming world's equivalent of a Millennium Prize problem. It is well known that the plaque says \"L is real 2401\", and this is allegedly an…"
tags: ["r/singularity"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 447
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1x9x7gw/i_used_an_ai_coding_agent_to_solve_one_of_gamings/"
score: null
comments: null
community: "r/singularity"
---

# I used an AI coding agent to solve one of gaming's "millennium problems": what the Mario 64 plaque really says

Reddit · decorator · 2026-10-19

Each hobby has some problems that can never be solved, and one of these for Nintendo fans is the plaque on the castle fountain in Super Mario 64, which has been the subject of debate since 1996 and has never reached a conclusion. It is essentially the gaming world's equivalent of a Millennium Prize problem. It is well known that the plaque says "L is real 2401", and this is allegedly an indication that Luigi is concealed in the game. However, no one has ever been able to verify what it states since the entire plaque is a 32 by 32 pixel texture and the letters are 3 to 5 pixels high. I worked on this using Claude as a coding agent. It wasn't used for image generation or for upscaling since those methods merely invent letters. Instead, we developed a forward model: we would enter a candidate text in the fonts typical of that era, reduce it exactly as a designer would have done in 1996, and then compare it with the actual pixels from the ROM. The most impressive aspect was the font. We looked at 470 fonts that a Nintendo artist might have had access to between 1993 and 1996, together with 4,583 modern fonts as a control group. The winning font was Palatino Bold Italic, specifically the original 1990 Adobe version. This wasn't by chance. Mario 64 was developed on SGI workstations, and SGI's system software was configured precisely for this Adobe Palatino. The Adobe font disc that it installs comes with the exact same letter metrics, byte for byte. Therefore, we didn't just discover the text; we identified the actual font file that the artist most likely used when typing it. The agent did some heavy lifting: Writing up the pipeline and research assistant rewrote the code so it can run on GPU Searching the web for thousands of old fonts and contemporary fonts set up blind tests against itself to make sure it wasn't fooling itself Result: "Eternal Star / We hope so". The phrase "L is real 2401" matches about twice as poorly on the first line by itself. The part that I prefer most was this: in order to make sure it wasn't simply picking out the word I had wanted, we had 50 secret words hidden in fake versions of the plaque and it managed to decode all of them correctly. All the components are open source, with a public challenge offering to beat the score: https://github.com/supermochi64/sm64-plaque-decode more details: https://github.com/supermochi64/sm64-plaque-decode/tree/main/press A year ago such a project would have taken a team several months; I carried it out in a couple of weeks with the help of an agent.
