---
id: "f97ab91cc2a05fc5"
title: "Saw Adam.new and got curious if plain Claude could do real hardware. A week later I have an open source Pocket recorder designed down to CNC drawings"
url: "https://reddit.com/r/ClaudeAI/comments/1x9nvo8/saw_adamnew_and_got_curious_if_plain_claude_could"
link: "https://reddit.com/r/ClaudeAI/comments/1x9nvo8/saw_adamnew_and_got_curious_if_plain_claude_could"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T04:56:25Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["DounderShtyc"]
language: "en"
summary: "So I saw adam (the AI CAD thing) a while ago, and it made me wonder... do you even need a dedicated tool for this, or can a normal Claude agent with a few tools just do it? I needed something real to test it on. I’d seen the Pocket (heypocket.com), the little recorder you stick on the back of your phone, and it looked like a good target. Small, not too complicated, but still real hardware. So…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "business & funding"]
content_source: "post"
word_count: 682
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9nvo8/saw_adamnew_and_got_curious_if_plain_claude_could/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Saw Adam.new and got curious if plain Claude could do real hardware. A week later I have an open source Pocket recorder designed down to CNC drawings

Reddit · DounderShtyc · 2026-10-19

So I saw adam (the AI CAD thing) a while ago, and it made me wonder... do you even need a dedicated tool for this, or can a normal Claude agent with a few tools just do it? I needed something real to test it on. I’d seen the Pocket (heypocket.com), the little recorder you stick on the back of your phone, and it looked like a good target. Small, not too complicated, but still real hardware. So the goal: an open source DIY version. ESP32, two mics, battery, aluminium case. My first prompt was basically “install whatever skills, MCP servers, packages and integrations you need and do as much of this as you can on your own”. Then I mostly just made decisions and let it go. Roughly what happened: It set up its own toolchain: CadQuery (python CAD), OpenSCAD for previews, matplotlib for drawings, and it downloaded the real STEP models of the XIAO ESP32S3 and the mic boards. It did some research first and found pocket-libre, a reverse engineered Pocket protocol. It suggested making the firmware compatible so the existing desktop app (local whisper, summaries etc) just works. Good call, I wouldn’t have thought of it. It wrote the whole enclosure as one parametric script, and every build runs an interference check between all the parts, so it can’t just eyeball it and say “looks fine”. First version was 15mm thick. I said thinner, it got to 12.2. Then I said I want it all metal, so now it’s an aluminium shell + lid (80x48x12.6mm) with a printed tray inside. It caught stuff I’d probably have missed on a first proto: the USB-C receptacle has to sit within ~0.4mm of the outer face or the plug doesn’t fully mate, and it put a translucent window in the lid so the antenna works through the metal (the status LED shines through it too). It did a DFM review of its own design and found real problems: mics hanging 1mm below their recess, nothing behind the button so it would just get pushed in, countersinks breaking out through the lid corner. It made machining drawings with tolerances, threads and finish, STEP files, wiring diagram and a BOM with suppliers and stock. Parts: this was the part that surprised me the most. It hooked up a parts sourcing MCP server (nexteverything.io), pushed pushed the BOM through it and got live stock + prices from JLCPCB, Mouser and Digi-Key, with obsolete parts flagged. The first pass was a bit messy: it matched a LiPo size code to a $49 industrial part lol, and a vibration motor search returned buzzers. Claude fixed it by switching to exact part numbers, and the second pass priced everything. And it turns out the MCP can also place the order. I let it send a test order for the electronics for 2 units, about $65. Last step was the renders. It scripted a Blender scene (materials, studio lights, 4 colours) and rendered it on a cloud machine. Those are the pics. For context, I’m a hardware engineer, I’ve built a few projects like this myself, and honestly the design looks good. It’s not “AI slop CAD”, it’s stuff I’d send to a machine shop with maybe a few tweaks. What it didn’t do (yet): nothing is built. no metal cut, firmware is a spec not code I made all the product calls (thickness, all metal, colours). It’s not one prompt and walk away, more like a really fast engineer who still needs someone to decide things a real machinist will definitely have opinions My main takeaway: code-based CAD fits an LLM really well, because it can check its own geometry instead of guessing. And the weakest part is always the physical world, parts and ordering. With the MCP in the loop it went from “here’s a BOM” to “here’s a priced order” which I didn’t expect at all. Repo (STEP, STL, drawings, BOM, assembly guide, all open source): https://github.com/TanskiSzymon/open-pocket Next up: quotes for the aluminium parts and building unit #1. Happy to answer questions or share the prompts.
