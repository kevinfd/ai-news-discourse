---
id: "d02c093c759860e4"
title: "Built an open-source Cotypist/Granola hybrid: autocomplete on Gemma 4 E2B (~50 ms/suggestion on M4 Max) using your own meeting notes as context"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4x5km/built_an_opensource_cotypistgranola_hybrid"
link: "https://reddit.com/r/LocalLLaMA/comments/1x4x5km/built_an_opensource_cotypistgranola_hybrid"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T13:49:31Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["stevyhacker"]
language: "en"
summary: "I built a desktop app harness that keeps local meeting notes and can use them to autocomplete my typing as well as complement my dictation with additional context via reading my screen or using the previous meetings notes. It's been a bit of a struggle to get it to work well and also to not be too intrusive and laggy. I've finally made it usable in the last few days so I'm sharing it here. I've…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 308
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4x5km/built_an_opensource_cotypistgranola_hybrid/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Built an open-source Cotypist/Granola hybrid: autocomplete on Gemma 4 E2B (~50 ms/suggestion on M4 Max) using your own meeting notes as context

Reddit · stevyhacker · 2026-10-13

I built a desktop app harness that keeps local meeting notes and can use them to autocomplete my typing as well as complement my dictation with additional context via reading my screen or using the previous meetings notes. It's been a bit of a struggle to get it to work well and also to not be too intrusive and laggy. I've finally made it usable in the last few days so I'm sharing it here. I've done a lot of experiments with different models and quants and Gemma 4 E2B base at 6bit is the best balance of quality suggestions and low latency on a regular MacBook. Feature Cotypist Cotabby LokalBot License / price Proprietary, free for 100 words a day, $$ for unlimited AGPL-3.0, free (beta) GPLv3, free, no limits Model Local (Gemma 4 E4B recommended) Local GGUF via llama.cpp, or Apple Intelligence Gemma 4 E2B base Q6_K, in-process llama.cpp Knows what was said in your meetings No No Yes, opt-in: up to two facts from your own notes, when your draft names something distinctive Text above the field Not documented on its site OCR of the window Accessibility text above the field, on by default, never from private windows Also in the app Autocomplete Emoji, macros, autocorrect Meetings, dictation, screen recall, sharing one model RAM budget Head-to-head with Cotabby, 782 next-word checkpoints: Identical inputs, same Gemma 4 E2B weights Exact next word LokalBot 32.7% (256 / 782) Cotabby 30.7% (240 / 782) Difference +2.0 points (95% interval 0.0 to +4.0) It's comparable performance wise to CoTabby, I'm still working on polishing the UX though. GitHub: https://github.com/stevyhacker/lokalbot If you try it I'd love to hear how it writes for you: which language, and how useful are suggestions. And if you know a small base model that beats Gemma 4 E2B at about 50 ms, I'll benchmark it.
