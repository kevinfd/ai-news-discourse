---
id: "c84d78ab9d51b339"
title: "Show HN: Free open source Adobe Lightroom alternative, completely local with AI"
url: "https://github.com/thesnarkitecht/rembrandt"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T21:00:55Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["thesnarkitecht"]
language: "en"
summary: "Stop paying for Adobe. Flush the incrapification.\nA free photo editor for macOS, Windows and Linux.\nNo account needed, no subscription, no “we’ve updated our terms” emails.\nDownload · Quick facts · Self-host · Features · Compare · Build\nAll files and checksums: Releases. Builds aren't code-signed yet: on macOS use System Settings → Privacy & Security → Open Anyway; on Windows More info → Run…"
tags: []
orgs: ["Google", "Apple"]
topics: ["chips & infrastructure", "products & launches", "models & research"]
content_source: "fulltext"
word_count: 1249
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50012199"
score: 47
comments: 64
community: "Hacker News"
---

# Show HN: Free open source Adobe Lightroom alternative, completely local with AI

GitHub · thesnarkitecht · 2026-10-08

Stop paying for Adobe. Flush the incrapification.
A free photo editor for macOS, Windows and Linux.
No account needed, no subscription, no “we’ve updated our terms” emails.
Download · Quick facts · Self-host · Features · Compare · Build
All files and checksums: Releases. Builds aren't code-signed yet: on macOS use System Settings → Privacy & Security → Open Anyway; on Windows More info → Run anyway.
Serve Rembrandt from the computer that holds your photos and edit them in any browser:
curl -fsSL https://raw.githubusercontent.com/thesnarkitecht/rembrandt/main/install.sh | bash -s -- --server
It asks which photo folder to use, starts at login, and prints a private link. Edits are saved next
to each photo as XMP; the photos themselves are never changed. Add --lan to reach it from other
devices on your network. Linux and macOS; one small dependency-free binary (server/).
To update, press Update in the browser (Settings › About); it installs the latest release,
checks it against the published SHA-256 sums, and restarts the server.
- Ask in words: type “warmer and a bit brighter”, “down exposure by ten points”, “shadows +25” or “paste the edits from the previous photo” (Ctrl/⌘ K), or say it: press the microphone in the side panel and say “bring lens blur down”. A small Rembrandt in dots thinks it over, then makes each change while you watch the sliders move. It runs on your device: a vocabulary, not a language model.
- Edit the photo itself: drag up or down on any part of the picture to lighten or darken that tone, left or right to change that colour; the sliders follow.
- AI looks: Enhance, Relight, Sky, Atmosphere, Sunrays, Skin, Motion and Lens Blur with aperture shapes, from on-device depth and subject maps.
- Refocus: brings back detail in out-of-focus photos, even heavy defocus (regularised deconvolution on the GPU), on the subject or the whole picture.
- Super Resolution: 2× and 4× with real detail, or Restore at the same size for soft photos; runs on the GPU (Metal on Apple silicon).
- AI Denoise: clean high-ISO shots into a new DNG with the same edits, on the GPU.
- Background work that stays out of the way: AI Denoise, Super Resolution and merges run in small GPU slices that pause while you edit, or when you're away, or overnight in a night window you set (Settings › Performance). The queue survives restarts.
- Merge: HDR from brackets, panoramas and focus stacks, each to a RAW-like DNG.
- RAW from 1,000+ cameras, developed on the GPU: tone, colour, curves, grading, dehaze, detail.
- Masks: brush, gradients, colour and tone ranges, AI subject, background, object and depth, and People: face skin, body skin, hair, eyebrows, eye whites, irises, lips, teeth and clothes.
- Remove: heal and clone spots and strokes; Rembrandt picks a matching source for you. Remove blemishes finds and heals them on portraits in one click and keeps moles and beauty marks.
- Pick the best: select a shoot and Rembrandt groups the bursts, picks the sharpest frame with open eyes in each and rejects the blurry and eyes-closed ones. Your own flags are kept; one Undo.
- Lens corrections: the camera's built-in profile from Fujifilm and Sony RAWs, or one of 1,500 lens profiles from Lensfun (distortion, vignetting, chromatic aberration), plus manual distortion and vignetting for any photo. Auto straighten levels horizons.
- On-device AI: Refocus, background replacement. Nothing is uploaded.
- Library: albums, ratings, flags, colour labels, keywords, virtual copies, search, Find similar, sorting, keyboard shortcuts (or Lightroom's), one-click delete with Undo.
- Batch: copy and paste edits to hundreds of photos, batch export, and presets that fit each photo's exposure. Imports Lightroom presets (.xmp, .lrtemplate and zip packs). Watch a folder to apply a preset and album to new photos as they arrive.
- Share how: a before/after page with a slider, a replay video of the edit, or the recipe inside the exported file so anyone can see (and reuse) how it was edited.
- Bring your photos: folders, Lightroom Classic (edits, keywords, labels, virtual copies, collections, with a report of anything that can't come over) and Lightroom, Google Photos, Google Drive, Dropbox, OneDrive (setup). Export back to them too.
- Open formats: edits are standard XMP, readable by Lightroom and others. Exports keep the camera details and date taken, add your name and copyright, and embed an sRGB profile; location is never written.
- Cloud sync (optional, paid): turn it on in Settings to sync edits, albums and photos between your computers, the web and your phone. It's the only thing that needs an account, and the only thing that costs money; everything else stays free.
- Lightroom: the everyday editing and library work is here: RAW development, masks (including AI subject, depth and object), healing, presets, lens corrections, HDR and panorama merges, denoise, batch editing, and catalog import. Not here yet: Print, Book, Slideshow, Web and Map modules, face recognition, Adobe's camera profiles, tethered capture (a watched folder covers most tethering apps), and a plugin ecosystem.
- darktable: Rembrandt borrows darktable's central idea, a scene-referred pipeline (edits work on linear light before a tone curve maps it to the screen), which is why highlights recover cleanly. darktable has far more modules and control; Rembrandt aims to be usable in five minutes, with fewer, broader controls and on-device AI. The engine is an independent implementation (see Credits).
- RawTherapee / ART: similar ground to darktable; Rembrandt trades depth of control for speed of use.
- GIMP / Photoshop: different kind of tool. Those are pixel editors for compositing and painting; Rembrandt is a non-destructive RAW developer and library, like Lightroom.
Rembrandt never moves or rewrites your originals. Edits are saved as standard XMP sidecars next to your photos, which Lightroom, darktable and others can read, and Settings › Data & privacy exports a backup of all your edits. If Rembrandt disappeared tomorrow, your library and your edits would still be yours, in open formats.
JavaScript with WebGL2 and WebGPU shaders for the editing engine and on-device AI, in a small Rust (Tauri) desktop app. RAW files are decoded by LibRaw (C++, compiled to WebAssembly). Every release is built by GitHub Actions from this repository, with checksums and signed build provenance (SECURITY.md).
- darktable: the scene-referred workflow Rembrandt's engine is modelled on. An early prototype ported darktable's algorithms; it was replaced by an independent implementation of the published methods (listed in NOTICE.md) before the code was released.
- LibRaw (RAW decoding), Lensfun (lens profiles), RAWmakase (lens tables, heal and clone), Real-ESRGAN (Super Resolution), KAIR / FFDNet (AI Denoise), MediaPipe (subject, depth and object models). Licences and notices in NOTICE.md.
Rembrandt is free and stays free. Star the repo, tell a photographer, report a bug or send a fix.
npm ci && npx http-server -c-1 .   # web app
npm run tauri dev                  # desktop app (Rust + Tauri prerequisites)
Details in docs/building.md. Contributions welcome: CONTRIBUTING.md.
Free software under the GNU General Public License v3.0 or later, the same licence as darktable. Use it, study it, change it and share it; if you distribute a modified version, share its source under the same terms. It may also be distributed through app stores (an additional permission under the GPL; see NOTICE.md, which also lists the third-party parts).
Screenshot photos from the scikit-image sample data: espresso by Rachel Michetti and cat by Stefan van der Walt (CC0), rocket launch by SpaceX and Hubble eXtreme Deep Field by NASA (public domain).
