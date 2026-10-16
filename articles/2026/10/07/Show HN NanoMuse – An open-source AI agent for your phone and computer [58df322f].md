---
id: "58df322f46a9de9b"
title: "Show HN: NanoMuse – An open-source AI agent for your phone and computer"
url: "https://github.com/nano-muse/nanoMuse"
link: "https://github.com/nano-muse/nanoMuse"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T03:30:44Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["ilreb"]
language: "en"
summary: "English | 简体中文 | 繁體中文 | Español | Français | Bahasa Indonesia | 日本語 | 한국어 | Русский | Tiếng Việt\nnanoMuse is an open-source personal agent for every device you own. One agent with a name and a look of its own, in the style of Meta's Muse: it does things instead of answering questions, keeps working while the app is closed, remembers you, and stops to ask before anything you could not undo.\nnano…"
tags: []
orgs: ["Meta", "DeepSeek", "Hugging Face", "ByteDance", "China"]
topics: ["products & launches", "agents & coding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 847
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49987765"
score: 68
comments: 21
community: "Hacker News"
---

# Show HN: NanoMuse – An open-source AI agent for your phone and computer

GitHub · ilreb · 2026-10-07

English | 简体中文 | 繁體中文 | Español | Français | Bahasa Indonesia | 日本語 | 한국어 | Русский | Tiếng Việt
nanoMuse is an open-source personal agent for every device you own. One agent with a name and a look of its own, in the style of Meta's Muse: it does things instead of answering questions, keeps working while the app is closed, remembers you, and stops to ask before anything you could not undo.
nano means the whole set, small enough to run and deploy yourself: the phone app, the desktop app, the web console and the relay that joins them are all in this repository, under GPL-3.0-or-later. Free, open source, non-profit. Let's build it together. Sign in and you get a free allowance of model use on the community relay (the developer pays for it); when it is gone, use your own key. The same relay runs on a server of yours, so nothing has to leave your house. Latest: 1.0.5 Lookout, release notes · try it in the browser.
Note
nanoMuse keeps evolving
A personal agent should not live only in someone else's cloud, so nanoMuse is the open-source, low-cost alternative: on your own devices, with a model you choose and a relay you can host yourself. We want to build it with developers and users everywhere, so that each person truly owns a personal agent. Open an issue or send a pull request; either one helps nanoMuse get better.
nanomuse-film-en-web.mp4
English · 中文 · nanomuse.cn
- 2026-10-13 ⭐ 1,000 stars on GitHub, eighteen days after the first release, with four days on GitHub Trending's Swift list on the way (Trendshift: seventh on October 7, fourth on October 10). Thank you for every try, every report and every pull request. We keep going: a version every few days, and the roadmap says what comes next.
- 2026-10-09 🚀 Version 1.0.0 Keel is out, for the phone, the desktop and the browser; it installs over the version before and keeps your data, and its release notes list every change.
- 2026-10-08 🤗 Our paper is on Hugging Face Daily Papers, ranked third on the list for October 8; questions and comments are welcome on the paper page.
- 2026-10-07 📄 Our paper is available on arXiv: nanoMuse: An Open-Source Personal Agent for Every Device You Own, by Guangyi Liu, Yong Liu and Jiangning Zhang (Zhejiang University); the citation is at the end of this page.
- 2026-09-25 🎉 nanoMuse is released on GitHub under GPL-3.0-or-later: an Android app built on OpenMinis 1.13; the relay, the desktop app and the iPhone app came in the days after.
Every version: releases.
All downloads come from the latest release; the same files are on nanomuse.cn/dl when GitHub is slow where you are. Open the app, sign in with an e-mail or a mainland-China phone number, and it has a model to think with. The phone, the desktop and the web share one account and show the same conversations.
Each device runs its own agent: the phone inside the APK (Alpine Linux under proot, a shell, a browser, MCP), the computer inside nanoMuse Desktop (DeepSeek Harness with the Python runtime for the hands). Signed in, they meet on the relay and can ask each other for things; the text of the conversations travels through it, files and screenshots stay where they were made.
docs/every-device.md explains the devices, docs/hub.md the frames, docs/cloud.md the relay, docs/privacy.md what it keeps.
nanomuse.cn/docs: install per platform, every device, hands, connectors, memory, self-hosting, the protocols. The sources are in docs/; what changed in each version is in the CHANGELOG and docs/releases/.
One VPS, one hour: docs/self-hosting.md. Three ways: no server at all with your own key, your own relay with scripts/self-host.sh, or a runtime of your own for the web app.
Use it for a real task, report what broke, then pick something focused: CONTRIBUTING.md has the setup and the conventions, AGENTS.md the rules a coding agent follows in this tree, and the roadmap says where to start. Issues · Discussions · Discord.
Everyone whose change has landed on main, from GitHub's contributors list.
If you find nanoMuse useful, please cite the paper.
@misc{liu2026nanomuseopensourcepersonalagent,
      title={nanoMuse: An Open-Source Personal Agent for Every Device You Own}, 
      author={Guangyi Liu and Yong Liu and Jiangning Zhang},
      year={2026},
      eprint={2610.08699},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2610.08699}, 
}
nanoMuse stands on other people's work; THIRD_PARTY_NOTICES.md has the terms.
- OpenMinis: the on-device agent the phone app is built on, with proot and Alpine Linux for the sandbox.
- DeepSeek Harness: the agent harness the desktop app is a plugin of.
- UI-TARS-desktop (ByteDance): the desktop hands' operator is a port of theirs, and the stage's markers follow their ScreenMarker.
- MobileGym, MemGUI-Bench, PhoneHarness, CopilotKit/OpenMuse, Open-AutoGLM, ClawGUI: the phone operator, the traces and the product ideas.
nanoMuse is an independent community project, not affiliated with or endorsed by Meta Platforms, Inc.; Muse is their trademark. The dragon is the project's own.
GPL-3.0-or-later. The phone app is based on OpenMinis 1.13 (GPL-3.0), modified since 2026-09-24; see NOTICE. Earlier versions of the Python line were MIT (tag pre-openminis).
