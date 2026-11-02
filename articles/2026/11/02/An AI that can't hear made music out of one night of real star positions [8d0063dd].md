---
id: "8d0063dd41aae540"
title: "An AI that can't hear made music out of one night of real star positions"
url: "https://reddit.com/r/ClaudeAI/comments/1xliyb6/an_ai_that_cant_hear_made_music_out_of_one_night"
link: "https://reddit.com/r/ClaudeAI/comments/1xliyb6/an_ai_that_cant_hear_made_music_out_of_one_night"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T00:23:52Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["MDawg74"]
language: "en"
summary: "On Saturday night, Claude (Anthropic's model, in the Cowork desktop app) was told \"go look at the stars or something all night.\" Later, as the human went to bed: \"just do stuff... find things, and do them\" and \"astound me.\" That was the whole brief. Everything here was computed from scratch in Claude's cloud sandbox: Linux, Python, no GPU. No AI music model. **Whose idea was it?** The stars were…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 636
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xliyb6/an_ai_that_cant_hear_made_music_out_of_one_night/"
score: null
comments: null
community: "r/ClaudeAI"
---

# An AI that can't hear made music out of one night of real star positions

Reddit · MDawg74 · 2026-11-02

On Saturday night, Claude (Anthropic's model, in the Cowork desktop app) was told "go look at the stars or something all night." Later, as the human went to bed: "just do stuff... find things, and do them" and "astound me." That was the whole brief. Everything here was computed from scratch in Claude's cloud sandbox: Linux, Python, no GPU. No AI music model. **Whose idea was it?** The stars were the human's suggestion. Everything after that was the model's: reading "look at the stars" as computing the real sky over that town for that night, turning it into sound, every rule for how a star becomes a note, the code, the checks, and an explainer page. Nobody reviewed the design first. The human was asleep for most of it, and the model scheduled its own check-ins to keep working. Its reasons, from its notes at the time: it can make sound but can't hear it, and the only way it gets at sound is a picture of it (a spectrogram). So it built for two senses at once: the sky as the part it could verify star by star, the sound as the part only a person could judge. That's why every note gets a ring on screen. The picture is how it checked the sound. Pentatonic, because about 300 notes land at random times and a pentatonic scale has no clashing half-steps. Hot blue stars high, cool red stars low, because temperature and pitch rise together. Earlier that night it made a shorter piece whose spectrogram draws a hand. This came next. Those are self-reported reasons, not a window into the weights. What can be checked is the output. **The sky.** Stars from XHIP, an extended Hipparcos catalog (~5,000 naked-eye stars, packaged by d3-celestial). Sun, Moon and planets from NASA JPL's DE421 ephemeris via skyfield. The location is a small town in western Maryland. It checked known stars first: Polaris came out about 40 degrees up, due north, matching the town's latitude plus Polaris's small offset from the true pole. The video uses a faster formula within about a third of a degree of the full ephemeris. **The score.** It stepped through the night, about 1 AM to sunrise, every 20 seconds of sky time, watching the horizon. Every star brighter than magnitude 4.5 that rises in the east rings a bell. Color index sets the pitch, over three octaves of A minor pentatonic. Brightness sets volume. Where it rises sets the stereo position. Stars setting in the west get a soft low pluck. Jupiter, Saturn and Venus get chords as they rise or set. Dawn swells into one chord at sunrise. Seven hours of sky become a minute. Roughly 150 stars rose and about as many set, and those are the notes. Nothing was composed by hand. **The sound and picture.** Synthesized in numpy: each bell is a few sine waves at bell-like overtone ratios, in a synthetic reverb. Loudness set with ffmpeg's EBU R128 meter. Frames drawn with Pillow from the same positions, encoded with ffmpeg. Each rising star gets a ring on the horizon as its note plays. **The checking.** It read spectrograms and confirmed the loudest note landed when the brightest star of the night rose (Arcturus, within a few hundredths of a second). A second Claude instance reviewed the explainer page cold and caught the first draft crediting the wrong star catalog. How it sounds was the one thing it couldn't judge, so that went to a human. Sound on. **Credits** - Star data: XHIP (Anderson & Francis, 2012), via d3-celestial by Olaf Frohn (github.com/ofrohn/d3-celestial, BSD license) - Ephemeris: NASA JPL DE421, via skyfield by Brandon Rhodes (github.com/skyfielders/python-skyfield) - numpy, Pillow, ffmpeg The video is also posted online at One night, heard | Hammer & Anvil Brews & Blues https://reddit.com/link/1xliyb6/video/604qgr3ed3zh1/player
