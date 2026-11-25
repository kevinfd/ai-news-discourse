---
id: "2c3ac5a2eb659524"
title: "9/UX: a Macintosh-inspired desktop for 9front"
url: "https://progrium.github.io/9ux"
link: "https://progrium.github.io/9ux"
source: "Lobsters"
domain: "progrium.github.io"
source_type: "community"
collector: "rss"
date: "2026-11-24T18:37:29Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["progrium.github.io via lproven"]
language: "en"
summary: "I have written a story about this on the Register, but of course I can't post that here. \n I think this is a quite astonishing effort and could make 9front considerably more usable... but it's bot-assisted, so I don't think they'll take it. \n Comments"
tags: ["ai", "osdev"]
orgs: ["Apple"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 506
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 9/UX: a Macintosh-inspired desktop for 9front

Lobsters · progrium.github.io via lproven · 2026-11-24

9/UX brings the classic Mac and A/UX desktop (a spatial desktop, a global menu bar, consistent controls and dialogs, icons, and resource-driven presentation) to 9front, built the Plan 9 way: rio and libdraw draw the screen, 9P exposes every application's UI state and commands as files, namespaces define the working environment, the plumber opens documents, and ndb holds human-editable metadata.
Keep the Macintosh's direct-manipulation desktop,
but make every meaningful object, action, and resource visible as a Plan 9 file.
It is not an emulator, a Macintosh ABI, or an A/UX reimplementation. Native 9front programs stay first-class, and existing rio programs (acme, sam, rc windows, nested rio) keep working unchanged beside 9/UX apps.
The pieces:
- rio fork (rio -u): a desktop layer, a global menu bar that follows the focused app, title-bar chrome, and a drag broker, all under /dev/ux. With 9/UX mode off it's stock rio.
- Desktop: volume icons, spatial folder windows, rename, duplicate, Get Info, Trash, remembered layout, and double-click to open documents through the plumber. A remote 9P server works as a volume.
- libux, the Toolbox: windows, menus, dialogs, alerts, and controls, each app serving its control tree over 9P, so echo activate >.../ctl presses a button.
- uxd gathers every app's tree at /mnt/ux with per-app policy; uxmeta keeps associations, volumes and layout in ndb files; resfs serves classic ICN#, icl8, menu, dialog and string resources at /mnt/res; clipd is a typed clipboard kept in step with rio's snarf.
These are real frames, not mockups. The GUI tests embed h9 with a headless screen, inject mouse and keyboard input, and drive the 9P files at the same time.
Macintosh structure, Plan 9 colour: butter title bars from rio's selection yellow, acme's cream and olive, and rio's greygreen for the desktop, so 9/UX windows and legacy rio windows sit together on one screen. Everything reads in one bit, uses a sixteen-colour palette, and is drawn in whole pixels. Every graphic is original to 9/UX; it ships no Apple resources. The mockups below are generated from the same palette and metrics files as the code.
The design document describes 9/UX and its v0.1 acceptance criteria; release.md has where each one stands, the end-to-end demo, and the open issues. Every interface between components is a file protocol in docs/protocols, and the visual design covers the palette, fonts, metrics, chrome, icons and cursors.
The source is on GitHub, under the MIT license. Development runs on h9, which runs 9front's own compilers, mk and rio directly from the host shell, without booting a VM. scripts/h9.sh clones and builds the pinned h9 on its first run:
git clone https://github.com/progrium/9ux
cd 9ux
scripts/h9.sh --rc 'mk'
scripts/h9.sh --gfx rio/7.out -u
scripts/test.sh
Use rio/6.out on amd64. development.md and testing.md have the details.
9/UX is at v0.1 and under active development. Interfaces and behaviour change without notice.
Please report bugs and send questions through GitHub issues.
The 9/UX mark in the menu bar is a pixel-art Glenda by Dan Fessler. Glenda, the Plan 9 bunny, was created by Renée French.
