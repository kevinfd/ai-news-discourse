---
id: "d854a311c0288aee"
title: "Week 2 of Migrating From 2D to 3D using Claude with Tripo"
url: "https://reddit.com/r/ClaudeAI/comments/1xa52j3/week_2_of_migrating_from_2d_to_3d_using_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xa52j3/week_2_of_migrating_from_2d_to_3d_using_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T18:36:57Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Dead_Fox_7"]
language: "en"
summary: "I'm going to aim for weekly updates and in week 2, almost all assets (UI) and mechanics have been migrated from the Python version into Unreal, so a week 3 should start focusing on adding new fun things :) Tripo has done an incredible job at getting the needed assets to start making this feel alive. There's still a lot of placeholder assets (I'm looking at you Ugly Road and Mr. Gray Boring…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "xAI"]
topics: ["agents & coding", "models & research", "products & launches", "jobs & society"]
content_source: "post"
word_count: 659
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xa52j3/week_2_of_migrating_from_2d_to_3d_using_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Week 2 of Migrating From 2D to 3D using Claude with Tripo

Reddit · Dead_Fox_7 · 2026-10-19

I'm going to aim for weekly updates and in week 2, almost all assets (UI) and mechanics have been migrated from the Python version into Unreal, so a week 3 should start focusing on adding new fun things :) Tripo has done an incredible job at getting the needed assets to start making this feel alive. There's still a lot of placeholder assets (I'm looking at you Ugly Road and Mr. Gray Boring Vehicle Shed) so it really makes difference when I see what Tripo has created added to the game. This week's big step regarding that was the addition of barns, horses, pigs and the new storage buildings (the smaller blue roofed on and the larger orange silo). All made by Tripo. In addition, grass, flowers and trees and a new sky. Grass and flowers modeled by Claude. Deciduous trees made by Speedtree while the pine trees were purchased on Fab, but Claude took the sprite cards and converted them to meshes and then put together several variations of pines using Nanite Assembler. New animations for the pigs and horses which I'm quite happy with so far. Still using the method of image gen>Tripo model> Blender for a side profile screenshot> Grok using first and last frame to generate>Claude then lines up the skeleton it makes for the model to each frame. The addition for this week is that I colored each leg differently before the video generation to help with separation. Still testing as to whether this genuinely helps Claude or not. The barns in particular were a fun first step in generating the pieces separately and having Claude assemble them before adding them to Unreal. Currently they are made up of separate side walls, front and back with a separated wood framing and doors, the roof and floor. My approach here was to separate them first in an image gen, then show a front and side view (sometimes back as well), then bring those into Tripo, export and let Claude know how they should look based on the initial reference image. This worked quite well and I'm looking forward to improving on this for a very modular housing system. Claude Opus 5.5 took care of all coding and honestly has handled anything I throw at them like a champ. I've yet to see it not be able to transfer what's in my to what's on screen and it still feels like absolute magic. Workflow still remains unchange in week 2. I'll update any changes. Currently what is working very well for me is: Project docs it reads every session. A CLAUDE md points it to a “constitution” (the rules of the project), a code map (where everything lives, plus Unreal lessons learned), a decisions log and one mechanics file per system. That’s how it keeps its context between sessions. Milestones. Each system (inventory, farming, construction and so on) is a milestone with a brief. Claude builds it, I play it, give notes, and accept it. 20 milestones so far and still working well. The game logic is plain C++ with no engine dependencies, so Claude can test it headless. There are 680 automation tests that it runs itself. I'm, uh, actually not sure if this is excessive. It checks its own work visually. When the editor is closed, Claude launches the game off-screen with command-line flags (camera position, time of day, which UI panel to open, scripted mouse clicks) and saves a PNG, which it then looks at. When the editor is open, it works through Unreal’s MCP server instead. Headless tools for the map. It wrote commandlets and .bat scripts that generate the map, bake the walking grid, place buildings and re-seat trees after I sculpt the terrain. Music made by Suno after several remixes. Feel free to ask questions. I still have a lot to learn here, but would happy to share what I've picked up on this journey so far. Hope you enjoy!
