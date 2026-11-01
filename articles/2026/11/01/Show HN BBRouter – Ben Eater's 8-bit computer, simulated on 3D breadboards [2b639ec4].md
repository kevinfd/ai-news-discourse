---
id: "2b639ec43620655e"
title: "Show HN: BBRouter – Ben Eater's 8-bit computer, simulated on 3D breadboards"
url: "https://bbrouter.com/bbrouter/ben-eater-sap-1"
link: "https://bbrouter.com/bbrouter/ben-eater-sap-1"
source: "BBRouter"
domain: "bbrouter.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-01T00:10:30Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["creack"]
language: "en"
summary: "Hi HN, I kept wiring Ben Eater's 8-bit computer wrong, so I built a realistic virtual breadboard editor. Some of the nice features are side-by-side diff, scope, schematics auto-sync, auto-router (BBRouter stands for breadboard router), and my favorites: upload from the real Arduino IDE and connect to your AI with MCP, let Claude & co build it or help you troubleshoot. The link is the SAP-1…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 565
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50321522"
score: 38
comments: 8
community: "Hacker News"
---

# Show HN: BBRouter – Ben Eater's 8-bit computer, simulated on 3D breadboards

BBRouter · creack · 2026-11-01

BBRouter
Starting…
- ⌘K
- Find an action, part, project or jumper
- P
- Add a part or board (the library)
- ?
- These shortcuts
- ⌘Z
- Undo
- ⌘U · ⇧⌘Z
- Redo
- Esc
- Cancel, deselect, close
- V
- Select and move
- W
- Draw wires
- N
- Pin notes
- Right-drag
- Orbit
- Middle-drag
- Pan
- ⇧ right-drag
- Pan
- Mouse wheel
- Zoom
- Two fingers
- Pan
- ⌥ two fingers
- Orbit
- Pinch
- Zoom
- ⇧-click
- Add to or take from the selection
- ⇧-drag
- Select everything in a box
- ⌘A
- Select everything
- R · ⇧R
- Rotate (⇧: the other way)
- ⌥-drag
- Move a part, its leads kept in their holes
- ⌘C · ⌘V
- Copy, paste
- ⌘D
- Duplicate
- H
- Hide what's selected (or show it again)
- ⌫
- Delete
- Click a hole
- Start, then finish, a wire
- ⇧-click · right-click
- Turn the wire there
- ⌫
- Undo the last turn
- V · W · L
- Select, wires, net labels
- P · A
- Power labels, add a symbol
- R · ⇧R
- Rotate counter-clockwise (⇧: clockwise)
- X · Y
- Flip left to right, top to bottom
- E · double-click
- Its details
- D
- Its datasheet
- /
- While drawing: the corner the other way
- `
- Then a click: light that net
- Right-click
- What can be done with what's under it
- F
- Fit it all in view (the Home key too)
- ⌘F
- Find a net or a part
- G
- Grid on or off
- S · H · ⌘L
- A sheet, a hierarchical label, a global label
- T · I
- A text, a divider (a click a corner; Enter ends it)
- ⌘H
- The sheets, to go to one
- ⇟ · ⇞
- The next sheet, the previous one (Page Down, Page Up)
- ⌥⌫
- Back up to the sheet it's in
Claude, or another AI app, can open, change and run your projects with you, through BBRouter’s MCP server. Connect it once: it asks you to sign in, then works as you, on your projects only.
Then type /mcp in Claude Code, pick bbrouter and choose Authenticate to sign in.
Settings → Connectors → Add custom connector: name it BBRouter, paste the address and click Add, then Connect and sign in.
Any app that takes a remote MCP server (HTTP, with OAuth sign-in): give it the address.
Click a button, a part or a hole to point this step at
Create a layout, or open one saved on the server.
Nothing to control yet: variable jumpers, hole groups, warnings and the simulation show here.
Click anything to pin a note to it.
    Name sticker
    
    
  
    Type
    
      
      
    
  
    Jumper
    
      
      
    
    Fixed: part of the circuit; carries the net from one end to the other. Variable: moved by hand (a probe, a control line); breaks the net, so each end stays its own.
    States
    
  
    Gauge
    
    
  
    Colour
    
  
    Height
    
      
      
      
    
    
  
    Crossings
    
      
      
    
    
    Sections
    
    
  
On the schematicNot on the schematic yetTaken off the schematic
Its owner stopped sharing the project, or the link isn’t whole. Ask them for a new one.
