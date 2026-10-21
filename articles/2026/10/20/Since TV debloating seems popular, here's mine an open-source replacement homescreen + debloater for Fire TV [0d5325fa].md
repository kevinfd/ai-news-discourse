---
id: "0d5325fa614782de"
title: "Since TV debloating seems popular, here's mine: an open-source replacement homescreen + debloater for Fire TV (no root required)"
url: "https://reddit.com/r/ClaudeAI/comments/1xb00lj/since_tv_debloating_seems_popular_heres_mine_an"
link: "https://reddit.com/r/ClaudeAI/comments/1xb00lj/since_tv_debloating_seems_popular_heres_mine_an"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T18:26:39Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Sarg338"]
language: "en"
summary: "Repo: https://github.com/Sarg338/Homestead Since debloating TVs is getting a lot of attention lately, figured I'd share the thing I've created and been running on my own TV. It's an app Claude developed and called Homestead. Claude did all of the coding, including it's own testing controlling the TV, and it even made the picture in this post. It's a replacement home screen that drops the…"
tags: ["r/ClaudeAI"]
orgs: ["Amazon", "Anthropic"]
topics: ["products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 590
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xb00lj/since_tv_debloating_seems_popular_heres_mine_an/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Since TV debloating seems popular, here's mine: an open-source replacement homescreen + debloater for Fire TV (no root required)

Reddit · Sarg338 · 2026-10-20

Repo: https://github.com/Sarg338/Homestead Since debloating TVs is getting a lot of attention lately, figured I'd share the thing I've created and been running on my own TV. It's an app Claude developed and called Homestead. Claude did all of the coding, including it's own testing controlling the TV, and it even made the picture in this post. It's a replacement home screen that drops the sponsored banner, the auto-playing trailers, and the promoted rows, so you just get your inputs and your apps. It can also switch off a pile of Amazon's ad and telemetry packages if you want it to. **This honestly wasn't meant to be a public thing, but a few people asked, so I cleaned it up and put it on GitHub. I'm not an app developer, so fair warning going in that it's probably not as polished as some of the other examples going around.** A heads up on the Fire OS quirks, because there are a few: Fire OS won't let any app actually become the default home screen. Amazon locks that down hard. So Homestead doesn't replace it, it just opens itself whenever you hit Home instead of Amazon's screen. Works the same in day to day use, with two catches: 1) You could still see Amazon's home screen flash for a split second on every Home press before Homestead covers it. Can't fully kill that one. Fire OS doesn't tell the app you pressed Home until Amazon's screen is already drawing. 2) If you're already sitting on Amazon's home screen and press Home, nothing happens, because Fire OS sends no signal in that case. Open any app, then press Home, and you're back in Homestead. Setup is a bit more involved than a normal app, also thanks to Fire OS: 1) Fire OS doesn't list accessibility apps in its own Accessibility menu, so there's no switch to just flip for the Home button part. The app turns it on over ADB instead, all from the TV, no computer needed. You turn on ADB debugging and approve a couple of prompts and that's it. 2) One of those prompts is a scary looking VPN notice that says the app can monitor your network traffic. That's just Android's standard warning for anything using a VPN. Homestead only uses it to reach the TV's own debugging service from the TV itself. Nothing leaves your TV, no accounts, no phoning home. --- On the debloat side, it disables packages rather than uninstalling them, so nothing is gone for good and you can turn any of it back on from the app. A handful of Amazon's telemetry packages are protected by Fire OS and can't be disabled by anything short of root, so telemetry gets reduced, not killed. The app tells you which ones are locked. The main caveat is that I've only really tested this on my own TV, an Insignia Fire TV Edition on Fire OS 7. The debloat list was put together by hand on that one TV, so on other models some of it might not line up. If you run it somewhere else and something's off, open an issue with your model, or point your own Claude at the repo and have it sort it out. PRs welcome. Fire OS 8 is completely untested. It's free and open source under GPL. Grab the APK from the releases page and sideload it, or if you've already got Claude talking to your TV you can just point it at the repo and tell it to install.
