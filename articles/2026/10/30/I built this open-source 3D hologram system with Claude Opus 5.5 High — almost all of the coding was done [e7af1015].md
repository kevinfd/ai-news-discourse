---
id: "e7af10157538e302"
title: "I built this open-source 3D/hologram system with Claude Opus 5.5 High — almost all of the coding was done autonomously"
url: "https://reddit.com/r/ClaudeAI/comments/1xj544y/i_built_this_opensource_3dhologram_system_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xj544y/i_built_this_opensource_3dhologram_system_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T03:45:05Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["SignificanceLanky988"]
language: "en"
summary: "I've been building an open-source project called Construct, and since the whole thing was implemented with Claude Opus 5.5 (high effort) in Claude Code, I thought this subreddit might appreciate both the result and how we got there. Construct lets you name a real object—a specific car, cathedral, camera, synthesizer, etc.—and an agent researches it and describes it as structured data: parts,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 709
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj544y/i_built_this_opensource_3dhologram_system_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built this open-source 3D/hologram system with Claude Opus 5.5 High — almost all of the coding was done autonomously

Reddit · SignificanceLanky988 · 2026-10-30

I've been building an open-source project called Construct, and since the whole thing was implemented with Claude Opus 5.5 (high effort) in Claude Code, I thought this subreddit might appreciate both the result and how we got there. Construct lets you name a real object—a specific car, cathedral, camera, synthesizer, etc.—and an agent researches it and describes it as structured data: parts, dimensions, joints, facts and their sources. Construct then checks that description for things like floating parts or dimensions claimed more precisely than the source actually supports, and builds it deterministically. The AI writes data, never a mesh or graphics code. It also keeps track of what it actually knows. Every fact and part is marked as verified, user-supplied, inferred or decorative, and provenance mode shows the distinction visually. So if an agent had to reconstruct something from reference photos rather than a measured source, Construct doesn't pretend that part is equally certain. The same scene can become an interactive Measured Light hologram, a proper 3D model with named parts and working joints, a Blender scene, glTF for game engines, a film sequence that assembles to music, or even an entire NetLogo agent-based simulation run represented as a 3D construct. Construct itself is also a Claude Code skill. Load it with claude --plugin-dir dist/claude-code/construct and ask for something like “a masterpiece of the Sainte-Chapelle.” That's how the cathedral in the video was made: 183 parts, 21 facts and 6 sources, refined over 15 critic rounds in that experiment. The video is basically a tour of what the project has turned into. How I actually built it with Claude I designed and directed the project, but essentially all of the code was written by Claude. It was mostly one long Claude Code session. I let Claude implement things fairly autonomously, including running tests and debugging its own work. The main session also started separate sessions to build and test different constructs and experiments in parallel. My role was mostly at the checkpoints. I reviewed everything that actually came out, decided what wasn't working, proposed design changes and new experiments, and then let Claude implement and test the next version. That distinction mattered a lot because Claude could optimize things that were perfectly reasonable technically but weren't actually what I wanted visually. One example is the quality critic. In the higher-quality mode, a separate agent reviews each iteration against the sources and reference images. At first we used numerical scores to decide whether a new round was better. It didn't work. The scores were noisy, and eventually I realized we were optimizing the critic's metric rather than the thing I actually cared about. One experiment produced a Land Cruiser that scored well but looked like a cardboard mockup to me. So I changed the design: no more scores. A fresh critic now sees the new version and the current best side by side, blind, and simply decides which it prefers. Only the winner survives. I still do the final evaluations myself through blind A/B comparisons. That loop is basically how the whole project developed: Claude implements autonomously, I judge what actually came out, we find something weird or broken, I change the design or propose another test, and Claude implements it again. I spent surprisingly little time micromanaging code. From the original idea to the current version took about a month and a half, but the active development of Construct itself was well under a week. I already had a proof of concept and had spent another 3–4 days getting the holographic visual language where I wanted it, which gave us a pretty big head start. I tried to make the finished thing useful beyond just being a cool hologram: game developers can use it for props and blockouts with real proportions and working parts, 3D artists can use the models as starting points to work over, educators and researchers can visualize things and simulations, and museums or archives can use the provenance system to distinguish what is actually known from what had to be reconstructed. It's completely free and open source (Apache-2.0; the Blender add-on is GPL): https://github.com/rtmandreyev/construct Live examples: https://rtmandreyev.github.io/construct/ If you try it, let me know what you think—and definitely show me what you build with it.
