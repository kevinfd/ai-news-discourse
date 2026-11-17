---
id: "23f76b8c1b11f7f2"
title: "I built an app that puts your face in a birthday video from one selfie. What I learned about prompting video with a real person in it"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xxyk2v/i_built_an_app_that_puts_your_face_in_a_birthday"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xxyk2v/i_built_an_app_that_puts_your_face_in_a_birthday"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T19:24:53Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["pvdyck"]
language: "en"
summary: "Solo builder here. hehehe.AI turns one live selfie into a short vertical birthday video with your own face. In some scenes you record a line, and the person in the card says it in your voice. Every card is free; credits only buy extras. Demo (no sign-up): https://hehehe.ai How it works, briefly: - The selfie is processed on your phone. We never upload the raw photo, only the face pictures the…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI", "Anthropic"]
topics: []
content_source: "post"
word_count: 344
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xxyk2v/i_built_an_app_that_puts_your_face_in_a_birthday/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# I built an app that puts your face in a birthday video from one selfie. What I learned about prompting video with a real person in it

Reddit · pvdyck · 2026-11-16

Solo builder here. hehehe.AI turns one live selfie into a short vertical birthday video with your own face. In some scenes you record a line, and the person in the card says it in your voice. Every card is free; credits only buy extras. Demo (no sign-up): https://hehehe.ai How it works, briefly: - The selfie is processed on your phone. We never upload the raw photo, only the face pictures the scene needs. - Each card is one "scene": a structured prompt with the face as a reference. - A card can only show your own face. You can't make one of someone else. What I learned, mostly the hard way: One person, one moment, one payoff. Every scene that tried to tell a story failed. A cake pushed at the lens works. A plot doesn't. Real-looking places keep the person; cartoon worlds eat them. Put someone in a toy town and the style wins: the face melts into it. Photographic sets kept the likeness every time. Describing someone's look did nothing visible. I tested adding hair, glasses and age words to the prompt. No visible effect. The reference face does the work, and extra words only risk fighting it. Never tell the person to "turn to the camera". Frame them facing the lens from the first frame. Any cue to turn or look up makes the AI invent a move, and the face drifts. Keep the camera calm while someone speaks. A push-in during the line looks great in the edit and terrible on the lips. Phones are the real battlefield. One popular phone GPU failed on every frame of the face step, so we fall back to the CPU there. And all on-device ML has to free its memory the moment it's done, or the next step crashes on cheaper phones. Next: I'm opening scene writing to other people. They write scenes by talking to their own AI (Claude or ChatGPT) through a connector, and test them on 24 synthetic faces, never their own. Happy to go deeper on any of this.
