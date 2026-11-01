---
id: "5bba16c16594796f"
title: "Show HN: Vela, a New Linux Desktop Environment"
url: "https://velade.org/blog/vela-0-1"
link: "https://velade.org/blog/vela-0-1"
source: "Vela"
domain: "velade.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-01T00:36:10Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["BrandoDev_it"]
language: "en"
summary: "Hi, take a look at this.\nI didn't like KDE nor KDE Themes, so I made Vela, a new stacking desktop environment, and even though this is not very inspired in terms of aesthetic, this is not the point of Vela (not yet).\nPoint of Vela is mostly architecture: Vulkan 1.4 only, no OpenGL fallback; based on wlroots, but has a custom renderer.\nGPL3 license.\nVela is currently at 0.1.0 beta after one month…"
tags: []
orgs: ["Nvidia", "Intel", "AMD"]
topics: ["chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 863
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50321663"
score: 12
comments: 12
community: "Hacker News"
---

# Show HN: Vela, a New Linux Desktop Environment

Vela · BrandoDev_it · 2026-11-01

I’m really happy to say it: Vela 0.1, the first beta, is out! 🎉 It’s been hard work, sometimes frustrating, but damn good fun.
With 0.1, Vela stops being something to try out in the evening and becomes a desktop to use every day. On a desktop PC, it’s my daily driver, and I recommend it as yours. It’s still a beta, so there are bugs and there will be more, but the foundations are solid, and from here on the work is mostly polish.
What’s in Vela 0.1
0.1 isn’t about a list of new features. It’s the first time the whole desktop comes together under a version number:
- Windows: snap layouts and Snap Assist, snap groups, Task View with virtual desktops, Alt+Tab with live previews, rounded corners and shadows drawn by the compositor.
- The shell: a taskbar with jump lists and hover previews, a launcher, quick settings, a notification center, clipboard history, a snipping tool, desktop icons, light and dark modes.
- Files and Settings, built for Vela: a file manager with tabs, a preview pane, safe copies, archives and drives, and a settings app that covers displays (with an automatic revert if something goes wrong), sound, Bluetooth, power, input, personalization and accessibility.
- Graphics and gaming: Vela’s own Vulkan 1.4 renderer, animations tied to real vblanks, live blur, direct scanout, VRR, tearing control and explicit sync.
- A session you can rely on: if the compositor crashes it restarts and apps reconnect, the screen comes back locked if it was locked, a lost GPU no longer freezes the desktop, and administrator prompts dim the whole desktop.
- English and Italian, switchable on the fly.
New since the last alpha
After the feature freeze, most of the work went into fixes, but a few things arrived that make a real difference:
- The Updates page in Settings. It shows the installed and newest versions, what’s new, and the channel (Beta or Experimental). Vela checks on its own once a day, never on a metered connection, and sends a notification when there’s something new.
- Native Bluetooth pairing. Vela has its own Bluetooth service, and PIN, passkey and confirmation prompts come from the shell. Pairing a device no longer needs BlueDevil or blueman.
- X11 apps at native resolution. X11 apps and games run 1:1 in the monitor’s pixels, even at fractional scales, and fullscreen games go through direct scanout.
- Faster screen capture on NVIDIA. Reading the frame back no longer blocks presentation.
- Recovery from GPU loss. If the Vulkan driver loses the device, the compositor notices, stops and restarts instead of hanging.
- A sharper blurred wallpaper on the lock screen.
- Less and less KDE. Plasma Workspace and the KDE portal are no longer needed. KDE apps remain welcome, and Konsole remains the default terminal.
- Numbered, signed releases, on the two channels I talk about below.
Desktops yes, laptops with a plan B
My main PC has a Radeon RX 9070 XT, and I use Vela on it every day. The GPU test suites also run on an NVIDIA RTX 4070 Laptop. On a desktop PC with a Vulkan 1.4 GPU, you can use Vela as your main session.
On laptops I’m less confident: hybrid GPUs, suspend and resume, and backlight have had far less testing, and touchscreens only arrive with 0.2. Go ahead and use it, but keep another desktop installed that you can pick at the login screen, for the days when something goes wrong.
Ubuntu 26.10 support is the newest: the packages pass the installation tests, but they haven’t seen much real hardware yet.
How to install it
The Beta channel installs the newest numbered release: a prebuilt, signed native package, which vela-update verifies with Cosign before installing it. If verification fails, it installs nothing. Install Cosign (the steps for each distribution are in the installation guide), then:
git clone https://github.com/vela-desktop/vela.git
sh vela/packaging/vela-update --channel beta
Then pick Vela at the login screen. From then on, updates arrive from Settings → System → Updates.
If you already use the Experimental package (vela-git), you can switch to the Beta from the same page, or with vela-update --channel beta. Your settings are kept.
What “beta” means
The alphas were a build for every commit on main. Now there are two channels:
- Beta (vela): numbered v0.x.y releases, built from a protected tag and signed. It’s the one I recommend.
- Experimental (vela-git): follows the latest commit on main and is built on your computer. It gets every change as soon as it lands, and every regression along with it.
Next up is 0.2, which focuses on touch and pen input, Vela’s own on-screen keyboard, and input methods (fcitx5, IBus). The rest is in the roadmap.
If something goes wrong
Run vela-report: it builds a ZIP file with your description of the problem and the diagnostics you choose, shows you every file before exporting it, and uploads nothing anywhere. Then open an issue and attach it. I especially need reports from hardware I don’t have: Intel GPUs, laptops, multi-monitor setups.
Vela is free software, licensed under GPL-3.0-or-later. Try it and let me know how it went!
