---
id: "2855a6dd0b52b57a"
title: "Show HN: Black Ops II statically recompiled to native ARM64 macOS"
url: "https://github.com/adrbn/bo2-mac"
link: "https://github.com/adrbn/bo2-mac"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T04:56:47Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["adrbn"]
language: "en"
summary: "I grew up with Black Ops 2 and wanted to see if I could make it work on my 2020 MacBook Pro. So I used Claude Opus 5.5 to create a tool that converts your copy of the game (from Steam) to a native ARM64 Mac app, with almost 60fps in all areas. The whole game is statically recompilated ahead-of-time (AOT) and does not use any emulator whatsoever, be it Wine, Crossover or Rosetta. The best thing…"
tags: []
orgs: ["Apple", "Anthropic", "Microsoft"]
topics: ["products & launches", "jobs & society"]
content_source: "fulltext"
word_count: 3358
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50449891"
score: 51
comments: 15
community: "Hacker News"
---

# Show HN: Black Ops II statically recompiled to native ARM64 macOS

GitHub · adrbn · 2026-11-11

Call of Duty: Black Ops II, statically recompiled from 32-bit x86 Windows to native ARM64 macOS.
Campaign, Zombies and multiplayer against bots, built on your Mac from your own Steam copy.
English · 中文
Why · Abstract · Method · Limits · Repository · Legal
Beta, 2026-11-03 · measured on one Apple M1 (4 performance + 4 efficiency cores, 16 GB)
Campaign (Angola), Zombies (Town) and multiplayer (Hijacked, against bots) on an Apple M1, recorded while playing; the number in the top right corner is frames per second, and the screen recording itself costs some, mostly in the campaign. 80-second video (MP4, 20 MB)
Important
This repository contains no game file and no translated game code. It turns your own Steam copy of Black Ops II into an app for your Mac, on your Mac. The game's code ends up inside that app, so nobody can hand you a ready-made one: each player builds their own, and it may not be shared. Unofficial fan project, not affiliated with Activision, Treyarch or Microsoft. To play, buy the game. Beta: read what has and has not been proven.
Black Ops II never came out on Mac. On Apple Silicon the usual way to play it is Wine or CrossOver on top of Rosetta 2, which translate the game while it runs. Here that translation happens once, before the game starts, and what you get is a native ARM64 app. That also means it can be fixed and extended like any Mac app: split-screen, which the PC version never had, is in progress. A side-by-side comparison with CrossOver on the same Mac is not done yet.
bo2-mac takes the three executables of Black Ops II, the campaign (t6sp.exe), Zombies (t6zm.exe) and
multiplayer (t6mp.exe), and turns their x86 machine code into ARM64 machine code ahead of time.
Remill lifts each function to LLVM IR, a chain of our own passes rewrites
that IR, and the result is linked with a Win32 runtime written by hand, whose Direct3D 11 is drawn by Metal. There is
no Wine and no JIT: the game runs as native code, in one process. About 150,000 functions are translated across the
three executables. Only the short sequences that the copy protection hides run in a small x86 interpreter, and so does
any code the translation missed, so a hole is built to cost speed rather than crash the game.
On an Apple M1 the campaign runs at 51–60 frames per second, and every mission loads and hands over to the next
one, down to the end credits. Zombies is played solo on six maps through the game's own menus at 57–60.
Multiplayer is played against bots through its real menus, eleven game modes, at 53–60. One app,
Black Ops II.app, opens the campaign, and the CAMPAIGN / ZOMBIES / MULTIPLAYER entries of each menu switch to the
other game.
Nothing is downloaded from anyone but you: the converter reads the executables of the copy you bought, checks them byte for byte, and builds the app on your machine.
Frame rate counts the drawables really presented to the screen, checked against the screen and the Metal HUD.
What you can play
All three modes: keyboard and mouse, or a DualSense as XInput through GameController.framework; sound on; movement keys follow their position on your keyboard (ZQSD on AZERTY, WASD on QWERTY), unless you bound them yourself in the game's options.
In five steps, all on the player's Mac:
- Check. The converter accepts only the exact Steam build of each executable, checked by SHA-256. The launcher asks the Steam client on your Mac whether the signed-in account owns the game, and refuses otherwise.
- Catalogue and lift. Ghidra lists the functions of your own executable; Remill v6.0.1 lifts each one to LLVM IR. Five patches to the lifter are carried in tools/remill-patches/, among them the x87 rounding mode, and one that forks a running Remill for each function instead of reloading its x86 semantics.
- Fold. Remill's IR is correct but slow: every guest memory access, flag and x87 push is a call or a store
into a State structure. Our passes rewrite it before clang -O2: guest reads and writes are inlined, lock sequences become hardware atomics, the guest ret stays inside the lifted code, and the x87 stack is promoted to
locals.
- Runtime. runtime/ implements the Windows imports the game really calls, with exact stdcall arities (the Steam API ones taken from Valve's public headers). Guest memory is one 4 GiB mapping. Direct3D 11 is a fake-COM layer over Metal; DXBC shaders go through HLSLcc. XAudio2 goes to CoreAudio, and the videos are decoded natively with libvpx.
- Threads. Guest threads start as coroutines on one host thread, which removes most sources of non-determinism and makes a run replayable. The fast configuration moves the server, the render backend, sound mixing and decoding, and the job workers onto real host threads. ARM is not TSO, so this needed real memory barriers.
The copy protection is executed, not bypassed. The game hides integrity checks behind hardware exceptions, single-step traps and code it decrypts into the heap. A small x86 machine built on Unicorn (x86_guest_vm.cpp, heap_code.cpp) runs exactly those sequences and hands control back to the recompiled code. No check result is forced and no key is placed by hand.
A hole in the translation is built to cost speed, not a crash. When the game reaches x86 code that was never lifted, the
same machine runs its original bytes (interp.cpp) and gives control back to the
recompiled code at the next translated block, call or return. Each interpreted address is logged ([INTERP]).
The online service is answered locally. Zombies and multiplayer expect Demonware; a responder written from the game's own requests (dw_local.cpp) answers the lobby, storage and ticket on your Mac. Nothing leaves the machine.
Why not Wine, CrossOver, DXVK or DXMT?
They translate Windows calls at run time and keep the x86 code under Rosetta. Here the x86 code itself is gone: it is ARM64 machine code before the game starts. DXVK and DXMT are PE DLLs that reach their native backend through Wine's unixlib mechanism; this port has no Wine, and its Direct3D 11 is its own layer over 32-bit guest memory. Only shader translation was needed from outside, and HLSLcc, a plain C++ library, covers it.
Each entry is a symptom seen on screen, the cause that was measured, and the effect of the fix.
Thirteen findings, from the x87 rounding mode to a false start inside one instruction
F1 · The lifter ignored the x87 rounding mode. In Zombies the prone view shook. fistp rounded to nearest where
the game had asked for truncation, inside the network codec of the view height. The height received by the client was
wrong on 8 samples out of 8, and on 0 out of 8 after a Remill patch and a re-lift of the codec.
F2 · One reserved bit of the x87 control word. A campaign mission froze in an effects loop, only with real threads. The lifter stored bit 6 of the control word differently from real hardware. A one-line Remill patch and four re-lifted runtime functions fixed it, with no slowdown.
F3 · A CPU feature flag changes the algorithm. Our IsProcessorFeaturePresent answered "no SSE2", so the C
runtime took its x87 ceil, which rounded to nearest under our runtime. An effect then sampled index −1 forever: two
missions froze.
F4 · Our own log caused the stutter. Hitches of 170–430 ms were the render thread blocked in write(): our log,
redirected to a file on a nearly full disk. Sending it through a pipe to a child process took the hitches per run from
12 and 8 to 0 and 0.
F5 · Shader translation moved constants by 4 bytes. HLSLcc placed a float2 after a float at offset 24 where
Direct3D reads it at 20. 31 of 2,664 shaders were affected, among them the eyes and the reticles.
F6 · The protection has to run. The options menu froze 8 times out of 8. An integrity check rewrites its own return address to point at code decrypted into the heap, which the runtime ignored. Running that code, as Windows does, gave 3 out of 3 without a freeze.
F7 · Our own safety guards were the obstacle. One guard of ours stopped the game at 28 seconds of play. The largest gains of the project came from removing our own guards and false sharing, not from clever code.
F8 · An empty API stub looks like a broken service. Two stubs that returned nothing (CryptGenRandom,
StringFromGUID2) looked like a network failure in Zombies.
F9 · Thread priorities are part of the program. SetThreadPriority was a stub. Passing the mixer's request to
macOS cut the short audio buffers of a run from 908–1872 to 7–71, and the sound gaps with them.
F10 · Native skinning, bit for bit. CPU skinning rewritten in NEON gives the same bits as the original x86 and took a heavy scene from 17.8 to 30.3 fps.
F11 · Decals need the game's depth bias. Scorch marks and blood appeared or vanished with a slight turn of the camera. The game asks for a depth bias on decals; our layer left it at zero. Passing the game's values to Metal fixed it.
F12 · The render thread was copying the level's geometry every frame. In multiplayer and Zombies it copied 23–63 MB of vertex data to the GPU per frame, most of it static. Keeping static buffers resident in Metal brought the copies to 3.5–5 MB per frame: multiplayer 51.8 → 60 fps, Zombies 43.1 → 58.2. The same change does nothing in the campaign, where the pace is set by the scheduler thread. A speed-up helps only the mode whose bottleneck it touches.
F13 · A false start inside one instruction cost half the frame rate in combat. In the first conversions from a fresh Steam copy, Zombies fell to 25 fps whenever the player fired. Hot functions were running in the interpreter: the catalogue placed the start of the next function inside the first instruction of a root, so its bounded sweep decoded zero bytes and the root was dropped without a word. Sweeping such roots without the bound, as the one-by-one lifter already did, put them back in the translated code.
Predict, then measure.
- A prediction is written before the result is read: about 1,100 numbered ones by the time of this beta.
- At least three runs per configuration. Run-to-run noise is 30–64%, so a difference under about 40% cannot be seen at n = 3.
- A change must prove it is active: the log has to show it firing.
- A run that never reaches the level is a dead run, not a data point.
- The screen beats the log. When the screen contradicts a probe, the probe is wrong.
Record and replay, retractions, clean room, who does what
Deterministic record and replay. With every guest thread a coroutine on one host thread, most sources of non-determinism are gone; the replay is checked against the recording, not assumed. Three boundaries capture all outside input: the import dispatcher, the window message drain, and the consumed audio buffers. The journal is about 16 MB. It allows the same run twice with exactly one flag changed.
The instrument is the thing that fails. Nearly 200 findings were taken back along the way. The largest share (31%) were an instrument that answered a different question; the next (17%), one that could not answer at all. So every oracle here names its input and refuses to answer when that input is missing.
Clean room for the match rules. Multiplayer and Zombies take their match rules from a daily patch file that Steam no longer ships. The replacement in runtime/match_rules/ was written by a team that never saw the original script: one team wrote a behavioural specification from the game, the other wrote the code from that specification alone, and the two only spoke through written questions and answers, kept with their dates.
Who does what. AI agents supply the throughput: writing the shims, bisecting millions of calls per run, reading tens of thousands of lines. The human supplies the goal, the corrections from what is really on screen, and refuses the flattering conclusion. This is one game, months of work and heavy manual intervention.
- Local only. Multiplayer and Zombies run against the responder on your Mac. There is no online play, no LAN and no co-op yet. League Play is refused.
- Match rules are ours. Written in a clean room (see Method); behaviour may differ from the original in places.
- Heat. The Mac runs very hot during long sessions (111–116 °C reported on the M1). Play plugged in: on battery, macOS throttles the game hard. Plugging in avoids the slowdown, not the heat.
- First game on each map. In Zombies and multiplayer, shaders are translated for Metal while the map loads, so that first load is longer and the first minute can still hitch slightly. In the campaign they are translated when they first appear, so the loading cinematic stays smooth and the first pass through a place can hitch. Everything is cached: the next time, it loads fast and runs smooth.
- Window. The game runs in a 1280×720 window.
- Other Macs. Only one M1 has been measured. M2, M3 and M4 should be faster, but no number is claimed.
- Campaign. Every mission loads and chains; not every one has been played end to end.
- Zombies. Grief and Turned need a second player, and there is no co-op yet.
- macOS audio. When the system's coreaudiod is unhealthy the campaign stalls on its first video. Check that afplay -t 1 /System/Library/Sounds/Tink.aiff takes about 1 s; restarting the Mac fixes it.
You need an Apple silicon Mac, macOS 14 or later, at least 20 GB free (the conversion peaks at about 10 GB and about 4 GB stays), Homebrew, and Steam for Mac signed in to the account that owns the game.
git clone https://github.com/adrbn/bo2-mac.git && cd bo2-mac
brew install llvm@17 cmake ninja libvpx unicorn
pip3 install capstone
scripts/make_app.sh --from-source
Open Black Ops II.app, point it at your game folder and let it convert: about 1 hour 45 on an M1, the campaign first in about 45 minutes. The campaign is
playable as soon as it is converted: play it then, and Zombies and multiplayer are converted when you first pick them
in the game's menu. Otherwise the conversion goes on through all three. If the disk falls under
8 GB free, the conversion stops cleanly and resumes where it was.
Updating, or if the conversion stops. Run git pull && scripts/make_app.sh --from-source in the repository
folder: what is already converted is kept and the conversion resumes. An update redoes only what its changes touch: a
fix to the runtime relinks the three modes in about 3 minutes on an M1 instead of converting again. If it still fails,
open an issue with the log it names.
The converter only accepts the exact Steam build, checked by SHA-256. The Steam executables are encrypted by Valve's
SteamStub wrapper and this repository provides no way to remove it: the converter expects the three decrypted
images in ~/.bo2-native/steam/ (t6sp.exe.unpacked.exe, t6mp.exe.unpacked.exe, t6zm.exe.unpacked.exe). You make
them yourself from the copy you bought, with a separate tool of your choice. Only the wrapper must go: the file names
above and the SHA-256 check tell you at once whether a file is right. Never share these files.
DLC. The launcher asks your Steam client which DLC your account owns, exactly as the game does on Windows. A DLC map plays when you own it and its files are in your game folder.
- This beta: the three modes from a fresh Steam copy, on other Macs than the one that built them. Your reports (Mac model, frame rate, what broke) decide what comes next. First outside report, 2026-11-05: on an M2 Pro (16 GB), the conversion completed and the game started, after three fixes found on the way (#4, #5, #6).
- No Terminal: one app to download and open, then drop the game folder on its window. It carries its tools already built, so nothing is compiled on your Mac but the game itself (macOS 26 or later; macOS 14 and 15 keep the Terminal install).
- Fully translated: the 46 code blocks that still run through the Unicorn interpreter are translated ahead of time, and every translated instruction is checked against the interpreter; any translated function can be sent back to the interpreter, to find a wrong one by halving.
- No shader wait: shaders built before the first match, instead of at launch (about 3 minutes in multiplayer) and during play (freezes when a new effect appears). Started: shaders now compile in batches, and the ones from the last sessions compile in the background at launch. In multiplayer on an M1 without Xcode (a few tries, not a benchmark), shader compiling during the first two minutes of a match went from 18–25 s to 10–14 s on a first launch and about 5 s on the next one; freezes over 300 ms went from 15–22 to 13–15, then 7. The first launch still freezes about as often.
- Shorter conversion: down from about 2.5 hours to 1 hour 45 on an M1 (2026-11-06, measured on all three modes: the preparation reads the executable once, the lift and the fold use every core the memory allows). An update now redoes only what changed (a runtime fix: about 3 minutes). Next: less optimisation for code that rarely runs. The three modes share only 4 % of their functions, so converting shared code once would gain little.
- Faster, without heat: the campaign is bound by the scheduler thread, not by rendering; multiplayer with 11 bots is bound by the server thread. Native rewrites of the hottest functions come next, then frame rates above 60 for 120 Hz screens.
- Controllers: vibration and aim assist.
- Together: real UDP sockets for Zombies co-op, Grief and Turned, and multiplayer over LAN. Then local split screen, which the PC version never had: two copies of the game drawn in one window, one controller each, joined over that LAN.
- Later: MetalFX, post-processing when the frame is presented, and replacement textures loaded from the player's own copy.
For a copy the user owns, on hardware the user owns.
- No engine source and no leaked code are used.
- Neither the input binary nor the recompiled output is distributed. No game file is included: the player needs their own Steam copy of Call of Duty: Black Ops II. The converter only accepts the exact Steam build (SHA-256), and ownership is checked each time the game starts by the player's own Steam client: the game refuses to run when Steam is not signed in or the account does not own it.
- The copy protection is executed as the game wrote it; nothing in it is patched out. This repository provides no way to remove Valve's SteamStub wrapper.
- The online service the game expects is answered by a local responder written from the game's own requests: no Activision server is contacted, there is no online play, and game ownership is still checked by the player's Steam. The match rules were written in a clean room.
- The code written here is licensed under GPL-3.0 (LICENSE).
- Unicorn (GPL-2.0) is linked statically from Homebrew when you build (tools/boot.py). GPL-2.0 and GPL-3.0 code cannot be shipped together in one binary, so the prebuilt tools of roadmap step 2 cannot embed Unicorn as it is linked today. Building from source on your own Mac is not affected.
This is an unofficial fan project. Call of Duty and Black Ops are trademarks of Activision Publishing, Inc. Steam is a trademark of Valve Corporation. This project is not affiliated with, endorsed by or sponsored by Activision, Treyarch, Microsoft or Valve. To play, buy the game.
