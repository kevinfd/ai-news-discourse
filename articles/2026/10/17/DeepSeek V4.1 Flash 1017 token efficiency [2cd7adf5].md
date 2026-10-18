---
id: "2cd7adf5688c7dcf"
title: "DeepSeek V4.1 Flash 1017 token efficiency"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8dh83/deepseek_v41_flash_1017_token_efficiency"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8dh83/deepseek_v41_flash_1017_token_efficiency"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T15:46:46Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Dany0"]
language: "en"
summary: "https://preview.redd.it/thtq5y7zr1wh1.png?width=3706&format=png&auto=webp&s=e75b7f205d4c7d9bed8b45bf964e9535f3492a72 I only found one sloppy-ass slop channel that published see pic attached. Obviously they celebrate its cost efficiency and their benchmark is some nonsense but jesus fucking christ that's a big indication it's a tokenslopper Is there a better token efficiency benchmark available…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research"]
content_source: "post"
word_count: 178
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8dh83/deepseek_v41_flash_1017_token_efficiency/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# DeepSeek V4.1 Flash 1017 token efficiency

Reddit · Dany0 · 2026-10-17

https://preview.redd.it/thtq5y7zr1wh1.png?width=3706&format=png&auto=webp&s=e75b7f205d4c7d9bed8b45bf964e9535f3492a72 I only found one sloppy-ass slop channel that published see pic attached. Obviously they celebrate its cost efficiency and their benchmark is some nonsense but jesus fucking christ that's a big indication it's a tokenslopper Is there a better token efficiency benchmark available yet? I'm not sure AA will retest this one (I sure hope so though) Mainly I care about whether it's better than previous ckpt, as I know already the previous one was so bad that GLM 5.3 Flash was a better option for me EDIT: For anyone that's interested, I found more numbers but just nothing quite useful. I went ahead and ran my classic set of tests, not all of them, but my preliminary conclusion is: - on max thinking effort, there is no difference in CoT length - on high effort, CoT length is significantly shorter, but not by much - regardless of thinking effort, the CoT quality is much higher, uses less 'fluff', and the end result is that it takes less turns to solve the task So it's worth trying!
