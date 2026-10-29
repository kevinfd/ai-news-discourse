---
id: "d89ca3c9727babfa"
title: "How to make the “Outstanding” Tiny Desk AI videos from photos — workflow and input tips"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xhnmxw/how_to_make_the_outstanding_tiny_desk_ai_videos"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xhnmxw/how_to_make_the_outstanding_tiny_desk_ai_videos"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T13:09:48Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Hungry_Incident1146"]
language: "en"
summary: "If you’ve seen those AI desk concerts where an unexpected lead singer belts out “Outstanding!”, here’s a breakdown of how to approach making one. I’m building Tiny Desk for this format. The workflow separates who’s in the band from how the performance moves, which is a useful way to structure the inputs even if you’re putting it together yourself. 1. Prepare the cast Use one clear photo per…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 339
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xhnmxw/how_to_make_the_outstanding_tiny_desk_ai_videos/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# How to make the “Outstanding” Tiny Desk AI videos from photos — workflow and input tips

Reddit · Hungry_Incident1146 · 2026-10-28

If you’ve seen those AI desk concerts where an unexpected lead singer belts out “Outstanding!”, here’s a breakdown of how to approach making one. I’m building Tiny Desk for this format. The workflow separates who’s in the band from how the performance moves, which is a useful way to structure the inputs even if you’re putting it together yourself. 1. Prepare the cast Use one clear photo per person or pet. For people, a waist-up photo gives you clothing and body references; a separate face crop gives the model a closer look at their features. Avoid group photos, covered faces and heavy filters. Use photos you have permission to use. 2. Assign each reference a specific role Write down the mapping before generating: lead singer, keys, sax, backing vocals. In the prompt, explicitly identify which image belongs to which role. If you’re supplying a face crop and a wider photo of the same person, say that they’re the same subject—not two band members. 3. Separate casting from motion There are two ways to structure this: With a reference clip you have rights to use, keep its camera cuts and performance timing, and describe which cast members should change. Without a reference clip, build a still image of the complete band first, then use that composition to guide the video generation. The second approach gives you a chance to check faces, positions and instruments before spending a video generation on it. 4. Check more than the opening frame Watch for identity changes after cuts, faces hidden behind microphones, hands around instruments, and whether the vocals match the performance. A convincing first frame doesn’t guarantee a convincing full clip. I’ve packaged the workflow into Tiny Desk , with people or pets, up to five cast members, and 15-second output. There are samples you can watch without logging in. Generation is paid, starting at $8.90 for one video. It’s an independent project, not affiliated with NPR. For anyone working on multi-character AI video: how are you keeping identities consistent across camera cuts?
