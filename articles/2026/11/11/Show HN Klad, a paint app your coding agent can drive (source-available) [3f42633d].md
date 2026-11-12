---
id: "3f42633dc5b5e54d"
title: "Show HN: Klad, a paint app your coding agent can drive (source-available)"
url: "https://github.com/klad-app/klad"
link: "https://github.com/klad-app/klad"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T16:00:50Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["ambewas"]
language: "en"
summary: "I've been developing applications for a long time and have turned to game development as well lately. One of the things that frustrated me the most was that using AI agents for game development is very annoying in the art department. Your only options right now are to either use an image genAI model and roll the dice every time you want to make an edit, or have your agent draw with something…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 2002
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50454951"
score: 79
comments: 31
community: "Hacker News"
---

# Show HN: Klad, a paint app your coding agent can drive (source-available)

GitHub · ambewas · 2026-11-11

Give your agent real brushes. klad is a 2D painting and animation app you share with a coding agent. You paint in the editor with a pen. The agent paints through the klad command line, with the same brushes, on the same drawing, and each of you sees the other's strokes instantly.
don't want to build it? Sign up for the pre-built app release at klad.studio
There is no image model in klad. Your agent (Claude Code, Codex, anything that can run commands) decides what to paint; klad gives it brushes, layers and a timeline. Whatever either of you puts down stays what it was: a stroke with its path, pressure, brush and colour, a shape with its points, a fill with its region. So there's no rerolling and hoping for the best: if one leaf looks off, you fix that leaf.
Asked for "a little sprout creature for my game", the agent paints 4,344 strokes and fills. You change them: recolour the leaves, bend the mouth, move a smudge, blend the blush. Then the agent animates it: the creature's parts go into five groups, 205 keys move them, and no frame is painted again.
Drawings made with Claude Fable 5.2: the creature, the scene and the prop kit were painted stroke by stroke through the klad command line.
- Site and guides: klad.studio, with these drawings replayed stroke by stroke.
- Licence: source-available, not open source. Free to build and use for yourself, and inside a company with less than 500,000 euros a year in revenue. See Licence.
- Runs on: macOS (pen pressure and tilt). It also builds and passes its tests on Linux and Windows, checked on every change; the editor starts on Linux with the mouse for now, and nobody has drawn with it on Windows yet.
- Status: early. This is the first public version, and you build it yourself: see From source.
An image generator hands you pixels, and the only edit left is another roll of the dice. klad keeps every stroke and every fill as data: where it went, how hard it was pressed, its brush and its colour. Pick any of them hours later, yours or the agent's, and recolour it, bend it, move it or delete it.
- It's paint, not just vectors. A stroke keeps its path and pressure like a vector does, and still lands as paint. Loaded oil leaves ridges that catch the light, and smudge drags the paint already on the layer. The smudge stays a stroke too: move it later and klad blends it again where it lands.
- It can also do just vectors. Shapes with editable points, gradients, glows and real text in about fifty open fonts that come with it, for posters, covers and cards.
- It's a full painting and animation app. Two dozen brushes and a brush editor, layers, masks, clipping, effects, a timeline with onion skins and clips, in-betweens made from your key drawings, bones with IK, and exports as PNGs, sprite sheets or straight into Godot.
- Your drawings stay yours. A drawing is a folder of plain files on your computer, and klad needs no account. It only looks for a new version once a day, and you can turn that off. An edit changes only the files of what it edits, so drawings live well in git.
- Ask. Tell your agent what the drawing needs, in plain words: a lantern for the inn, lit from the left, on its own layer.
- Watch. It paints through the klad command line, and its strokes show up in your editor about a second later.
- Point. Pin a note on the canvas or select the part you mean ("more moss on this side"). The agent reads both.
- Take over. Repaint whatever you like by hand, the agent's strokes as much as your own. Its strokes are marked as its own and every change is one step in a shared history, so you can undo any of it.
The prompt to start with is under Try it. klad skill prints the agent skill in docs/skill/SKILL.md: how to look at a drawing, change it and check the result. A second one, klad skill drawing (docs/skill/drawing/SKILL.md), teaches the craft: planning a picture, light on form, values, edges, colour, materials and how to judge the result. A third, klad skill pixel (docs/skill/pixel/SKILL.md), does the same for pixel art. All are MIT, so use them with any agent and any tool. Open the drawing to watch and draw along:
What an agent paints depends on the agent and on how much you steer it. The skills teach it the tool and some craft; the pen in your hand does the rest.
Everything you can do in the editor has a klad command too, so a script or an agent works on the same drawing you have open. It reads strokes as JSON, changes any of them by its address and applies batches of edits as JSON ops.
The file format is documented down to the byte under the MIT licence (docs/format.md), so other apps and engines can read and write klad drawings with or without klad.
Props, characters, backgrounds and frame-by-frame animation. Draw the key poses and klad makes the drawings in between, part by part; it checks the arcs (a foot that slides, a part that sinks under the ground), colours every drawing from the first one, and exports sprite sheets or a Godot SpriteFrames scene with each clip's timing.
klad inbetween creature.klad --layers lines,colour --from 3 --to 5 --spacing in-out
klad arcs creature.klad --track 'lines:near leg' --clip walk --check
klad export creature.klad --godot ../game/artgit clone https://github.com/klad-app/klad && cd klad
just compile                  # about ten minutes the first time
target/release/klad open      # on Linux: target/linux/release/klad open
- Put klad on your path, for you and for your agent: target/release/klad install (on Linux target/linux/release/klad install; on a Mac it may ask for your password).
- Start your coding agent (Claude Code, Codex, or anything else that can run commands) in the folder where the drawing should go, and paste: Run klad skill and klad skill drawing and read what they print. Then make scene.klad and paint a night scene: a hooded traveller holding a lantern out to a ruined arch, a small creature following, flat shaded and lit by the lantern.
- Once it has made scene.klad, open it in another terminal to watch the strokes land, and draw along: klad open scene.klad.
- Then steer it. Press N to pin a note on the canvas ("more moss on this side") and tell the agent to read your notes, or pick any stroke with S and change it yourself.
Every build holds the klad command line tool, the editor, the fonts, the licences, the agent skill and six sample drawings to look at and draw on (the start window shows them; klad samples lists them and copies one out). The first start offers first steps: draw a shape, fill it and hand the drawing to an agent. The guides in docs/guide/ show how to paint, select, fill, animate, rig and export in the editor, one recipe at a time, starting with Getting started.
Building takes about ten minutes the first time.
- Install Rust with rustup and just (brew install just, or cargo install just). On Linux also pkg-config, libfreetype-dev, libfontconfig1-dev, libxkbcommon-dev and libwayland-dev.
- git clone https://github.com/klad-app/klad && cd klad, then just compile makes klad and klad-editor for the machine you are on, in target/release/ (on Linux in target/linux/release/). What you build is for your own use, or your company's if it had less than 500,000 euros in revenue last year (see Licence).
- target/release/klad open starts the editor on its start window: make a drawing and start painting, or take first steps (Help > First steps in the editor).
- target/release/klad install puts klad on your terminal's path, for you and for agents (the editor's document menu has the same as "install the klad command").
- just samples builds the sample drawings in samples/ (a lantern, a walking creature, a running courier, an underground ruin, an inn sign, a tree, a meadow, painted solids, a bowl of lemons and the same painted over with brushwork, a bouncing ball, ink examples, a pixel art character and a tileset); open one with target/release/klad open samples/lantern/lantern.klad. The eight listed in samples/shipped.json show in the start window and go into every build (packaging/samples.sh).
- On a Mac, just app makes klad.app and a disk image in dist/; just dist packs this machine's build as an archive. Each machine builds for itself: a Mac builds the Mac version, Linux the Linux one.
- You build it yourself. There are no installers yet. Signed builds for macOS, Windows and Linux are planned, under the same licence as the source; leave your email on klad.studio to hear when they are ready.
- The editor is made on a Mac. On Linux it starts and you draw with the mouse: tablets give no pressure there yet. On Windows it builds and its tests pass, but nobody has drawn with it there, so tell us what you see.
- Some illustration basics are missing: selecting several shapes at once, align and distribute, snapping, a grid, and SVG import and export.
- Bones are a preview: their commands may still change.
- Drawings keep opening as klad changes: a new format version comes with a migration.
- docs/format.md: the file format of a drawing, enough to read and write one from any program.
- docs/cli.md: every command with its options (klad <command> --help prints the same).
- crates/client: klad-client, a small Rust crate that runs klad commands, applies edits as JSON ops and reads drawings back.
- docs/DESIGN.md: how klad is built: the CLI, the brush engine, rendering, the editor, the dependencies.
- CONTRIBUTING.md: building, testing, the code rules and how to send a change.
- samples/: generators that make drawings from scratch, the best place to see the ops in use.
just compile    # release build of the klad CLI and the editor (plain `just` does the same)
just test       # every test, and the drawkit check
just lint       # rustfmt and clippy, warnings as errors
just audit      # licences, RustSec advisories, sources, and the notices are current
just samples    # build the sample drawings
klad is source-available, not open source, copyright Indicode BV.
- The app, meaning everything not listed in the next point, is under the PolyForm Internal Use License 1.0.0 with three additional permissions and one limit (LICENSE): you may use it for your own personal purposes, building it from source free of charge, as well as inside your company; you may send changes to Indicode BV to propose them as contributions; and the drawings you make with it are yours to share, with the brush settings and pictures klad copies into them. The limit: a company (counted with the companies it controls or is controlled by) that had 500,000 euros or more in revenue in its last tax year needs a bought licence for each person who uses klad for it. You may build it and change it for those uses; you may not distribute it, from source or as a build.
- Buying a build, on itch.io, Steam or from Indicode BV, gets you that bought licence, and the build is licensed under these same terms: one licence for the source and the builds, with no separate end-user licence.
- These files are under the MIT License (LICENSE-MIT), so any program or agent can work with klad drawings: docs/format.md (the file format), docs/cli.md (the command reference), docs/skill/ (the agent skills) and crates/client/ (the klad-client crate).
- Contributions are licensed to Indicode BV for inclusion in klad and in its sold builds, under the contributor licence agreement (CLA.md); see CONTRIBUTING.md.
klad is built on open source libraries, fonts and Skia; their licences are in THIRD-PARTY-NOTICES.md, also shown by klad licences and in the editor's About window.
