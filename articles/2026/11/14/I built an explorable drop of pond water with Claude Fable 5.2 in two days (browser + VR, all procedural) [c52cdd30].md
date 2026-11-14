---
id: "c52cdd30b6cb545d"
title: "I built an explorable drop of pond water with Claude Fable 5.2 in two days (browser + VR, all procedural)"
url: "https://reddit.com/r/ClaudeAI/comments/1xvyy70/i_built_an_explorable_drop_of_pond_water_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xvyy70/i_built_an_explorable_drop_of_pond_water_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T10:11:37Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["FelipeReigosa"]
language: "en"
summary: "I wanted to see if Claude could build something like the microscope footage from Journey to the Microcosmos youtube channel, but as a 3D scene you can fly around in. This is the result: https://felipereigosa.com/microcosmos.html Full video here: https://www.youtube.com/watch?v=PqeAH68DkbU Code and the full conversations: https://github.com/felipereigosa/microcosmos Desktop: drag to orbit, scroll…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media", "models & research"]
content_source: "post"
word_count: 374
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvyy70/i_built_an_explorable_drop_of_pond_water_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an explorable drop of pond water with Claude Fable 5.2 in two days (browser + VR, all procedural)

Reddit · FelipeReigosa · 2026-11-14

I wanted to see if Claude could build something like the microscope footage from Journey to the Microcosmos youtube channel, but as a 3D scene you can fly around in. This is the result: https://felipereigosa.com/microcosmos.html Full video here: https://www.youtube.com/watch?v=PqeAH68DkbU Code and the full conversations: https://github.com/felipereigosa/microcosmos Desktop: drag to orbit, scroll to zoom, click an organism to follow it, Esc to let go, Space to pause. VR (Quest): left stick flies, right stick turns and zooms, trigger picks what you point at. What's in it: a Lacrymaria that hunts and swallows its prey with its stretching neck, paramecia, a Vorticella that snaps its stalk into a coil, algae, debris, and a sewing needle for scale. Click an organism to follow it and read about it. Zoom in and the organelles appear. There are no 3D model files or textures. Every organism is code: geometry and shaders built from measurements. The whole page is a single HTML file under 1 MB. Why I think it worked: - Scientific papers. For each organism I gave Claude a paper (or it found an open access one), and it built the model from the published numbers: sizes, the 15 helical pleats on the Lacrymaria, cilia length and spacing, and so on. - Matching real footage. Claude tracked a real Lacrymaria in a microscope clip and used its measurements and timing. When something looked wrong (the debris, the neck motion), the fix was always the same: look at frames of the real thing and match them, instead of inventing. - One thing at a time. I looked at each result and said what was off. Several versions got rejected. The repo has every prompt and reply, including the failures. I also asked for a "VR button" to see if it would run on my Quest 2. It did, and floating among these things at their scale is my favourite part. You can point at an organism to read about it and ride along with it. I have 25 years of experience with software engineering but I wrote none of the code. My part was directing and judging. Credits: music by Kevin MacLeod (CC BY 4.0), footage reference from James Weiss / Journey to the Microcosmos, papers listed in the README.
