---
id: "1e3f029d6e47de6b"
title: "I gave Claude my grandfather’s 1945 WWII unit history book. It rebuilt his platoon’s war as an interactive 3D experience, and made all 2,655 men in the book searchable"
url: "https://reddit.com/r/ClaudeAI/comments/1xxtf0m/i_gave_claude_my_grandfathers_1945_wwii_unit"
link: "https://reddit.com/r/ClaudeAI/comments/1xxtf0m/i_gave_claude_my_grandfathers_1945_wwii_unit"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T16:13:17Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Agile_Toe4400"]
language: "en"
summary: "A few days ago someone here posted a tiny procedurally generated world built with Fable, and it motivated me to take action on an idea about a book I’ve had for years. The video is the 2-minute version; links to try it yourself (tap Play, sound on) are below. In 1945, weeks after the war ended, the men of the 106th Cavalry Group printed their own history in Augsburg, Germany. Their road from…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 519
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xxtf0m/i_gave_claude_my_grandfathers_1945_wwii_unit/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude my grandfather’s 1945 WWII unit history book. It rebuilt his platoon’s war as an interactive 3D experience, and made all 2,655 men in the book searchable

Reddit · Agile_Toe4400 · 2026-11-16

A few days ago someone here posted a tiny procedurally generated world built with Fable, and it motivated me to take action on an idea about a book I’ve had for years. The video is the 2-minute version; links to try it yourself (tap Play, sound on) are below. In 1945, weeks after the war ended, the men of the 106th Cavalry Group printed their own history in Augsburg, Germany. Their road from Normandy to Austria, written by the men who fought it, with rosters of nearly everyone in the unit. My grandfather, a lieutenant in B Troop, is named in it twice, both times in a forest attack in Lorraine on 4 October 1944. I never met him. I have his medals and that book, and the stories my relatives have shared with me about him. I wanted to see a taste of what he experienced in action. What I built with Claude: The short version (2½ min, interactive): that 4 October attack, built entirely in code in the browser: his platoon pinned down in the Forêt de Parroy, the tanks pushing in with hatches open, the rush to the road, the push to the crossroads. Then his actual medals. https://claude.ai/artifact/Mnra2RWf4dnY8Gh5F297YB The full journey: his troop’s road from Normandy to Austria, chapter by chapter. Every scene is labeled by what the book supports: “named here” where he appears by name, “his troop was here” everywhere else. The original page scans are one tap away. https://claude.ai/artifact/KKk9TyYir9pkooa7gEsSBY Every man in the book: Claude pulled out the rosters, linked the names in the story to the men, and built a page for each of the 2,655 men, following their own troop’s road. If your family has a 106th Cavalry vet, you can look him up. https://claude.ai/artifact/Uy6VcpjQQbnmuKue12xjjL How it came together: I scanned the book with the Adobe Scan app; Claude read all 368 pages, sorted the story by troop and date, and caught OCR errors and duplicate names. Claude Code built the 3D world with three.js (procedural terrain, forest, weather, figures, gunfire) and tuned the look against screenshots it took itself. The sound is 50 public-domain/CC0 recordings mixed spatially, so a machine gun on your left sounds left. Guardrails I cared about: no invented events or quotes, and nothing claimed beyond the book. A collision check fails the build if anyone clips through a tree; that one came from me spotting my grandfather walking through an oak. It’s not a “finished” work. Excuse my thumbs in the page scans (it was hard to keep the old book open while using the app). The figures are still rough, and a history-buff friend already told me the original pages and maps should be the star, more than the 3D. That’s what I’m working on next: putting the book page first in every scene, a zoom-out map, and real 1944 Army maps. I’d love feedback, especially from anyone who’s tried something like this with family records. If people find this interesting enough, I’ll keep iterating on it, and will also post in a WWII subreddit for anyone who had family in the 106th Cavalry.
