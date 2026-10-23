---
id: "111f1c3f741e5c41"
title: "Show HN: OnKey – I'm a bad singer, so I built an app to show where I'm off-key"
url: "https://github.com/dsmurrell/onkey"
link: "https://github.com/dsmurrell/onkey"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-22T14:04:44Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["dsmurrell"]
language: "en"
summary: "Hi all I was pretty terrible at singing, now I’d say I’m bad but not terrible. This is because I’ve been using a singing app (won’t name it here) that scores me on my pitch and timing throughout the song so that I can improve. Lately however, the app I’ve been using has flooded their song list with songs that aren’t originals. I didn’t like this at all as for me, it’s easier to try to improve…"
tags: []
orgs: ["Apple", "Anthropic", "Meta"]
topics: ["products & launches", "search & media", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 842
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50195488"
score: 75
comments: 43
community: "Hacker News"
---

# Show HN: OnKey – I'm a bad singer, so I built an app to show where I'm off-key

GitHub · dsmurrell · 2026-10-22

Learn to sing the songs you love. · singonkey.app
Saving shower singers from themselves since 2026.
  
  
Me singing along to a song OnKey learned from one play. The full demo, with sound.
OnKey is a free, open-source singing trainer for the Mac. Play a song in Spotify, Apple Music, or YouTube in a browser, and sing along. The first time, you get the lyrics, and OnKey learns the singer's melody when the song ends. After that, the notes scroll towards you, your pitch is drawn over them, and you get a score with a report on every line.
OnKey doesn't provide, stream or download music. Your own music app plays it.
You need a Mac with Apple Silicon (M1 or later) and macOS 14.2 or later.
Download OnKey.dmg (from the latest release), open it and drag OnKey to Applications.
Setup asks for the microphone, to hear you, and for system audio recording, to hear the music app. It also asks whether OnKey may follow Spotify and Apple Music: choose Listen only and it follows songs by their sound alone. Getting started walks through it, and the FAQ answers the usual questions.
When a song ends, OnKey learns it on your Mac: a model separates the lead vocal from the music, CREPE tracks the singer's pitch, and the GAME note model turns it into one bar per syllable. On later plays it finds its place from the music itself and tracks your voice live. Singing an octave down counts, and being a touch late isn't punished. How it works and Scoring have the details.
OnKey never saves the music it listens to. It analyses the sound in memory as it plays. Your recordings and the songs it learns stay on your Mac (a take sung over speakers can contain some of the music). There's no account, no analytics and no crash reporting.
These requests do go out:
- Shazam (Apple): a short signature of the music app's sound, not the audio and never your mic, to name a song OnKey hasn't learned when the music app doesn't say what's playing.
- LRCLIB: the song's artist, title, album and length, to fetch lyrics.
- iTunes Search and Lookup (Apple): an artist and title, or the ID Shazam returned, for covers and the song's length. The cover images come from Spotify's, Apple's or YouTube's image hosts.
- GitHub: a check for a new version a minute after launch and once a day, and its download.
Settings has a switch for Shazam, for lyrics and for the update check. Privacy lists everything OnKey keeps and sends, and scripts/release-hosts.txt lists every web address in a release.
OnKey is for practising at home, with music you're entitled to play. Please:
- Keep what it learns to yourself. Its transcription of each song's melody is for your practice, so don't share or publish it.
- To share a take, use Share on its page. It makes a short video of your voice and your pitch line, with no music, and you can add the song from Instagram's own music library, which is licensed for this. Headphone takes are best: sung on speakers, some of the song is in your recording. Don't post screen recordings with the music playing.
- Use a licensed karaoke service for a bar or an event. OnKey's lyrics come from a free community database.
- Don't modify OnKey to save the music.
Rights holders can reach me at hello@singonkey.app (LEGAL.md).
Use Report a problem in the app (Settings, the Help menu, or a take's page). It saves a zip of numbers and logs on your Mac, with no audio and no recordings of you, for you to attach to an issue if you want to. Troubleshooting covers the common problems. Questions, or a song that's out of step? Ask in OnKey's Discord, or email hello@singonkey.app.
If you'd rather not trust my build, you can build your own. You need an Apple Silicon Mac with the Xcode command line tools, Rust, Node, and Python 3:
git clone https://github.com/dsmurrell/onkey && cd onkey
npm install && npm --prefix ui install
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-models.txt
PYTHON=.venv/bin/python scripts/fetch-models.sh   # downloads the models and checks them by SHA-256
npx tauri build
Your build runs on your own Mac. The one thing it can't do is ask Shazam to name a new song, which needs my Apple
signature. Spotify and Apple Music say what's playing themselves, so that only affects YouTube and Listen only. CONTRIBUTING.md has the details, the tests, and how to check a release's checksums. My
releases are signed with my Apple Developer ID and notarised by Apple (spctl -a -vv /Applications/OnKey.app
shows who signed it).
MIT. See LICENSE. Modified versions can't be called OnKey or use its icon. If you build on OnKey's code, a credit linking back here is appreciated.
OnKey learns songs with CREPE, GAME, wav2vec 2.0 and UVR's MDX-Net Karaoke 2. The credits list each one, and THIRD_PARTY_NOTICES.md has the full notices and licence texts.
OnKey is made by Daniel Murrell.
