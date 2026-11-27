---
id: "00d37b844ee38851"
title: "It Wasn't Your Imagination: Reaching ChatGPT Limits Way Too Quickly Was Real"
url: "https://note.com/ai_arai_ally/n/ne32653bd30cf?hl=en"
link: "https://note.com/ai_arai_ally/n/ne32653bd30cf?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-27T02:31:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-27T13:04:05Z"
authors: ["アライ｜Ai思考実験とデータ分析"]
language: "en"
summary: "Over the past few days, even though you've been doing the same tasks, you hit the usage limit much sooner than before. If that's what you were feeling, it wasn't just in your head📉On November 26, ..."
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2359
paywalled: false
image: "http://www.bing.com/th?id=ONUT.7wam6CRD82Sw1_opZTAPyA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# It Wasn't Your Imagination: Reaching ChatGPT Limits Way Too Quickly Was Real

note · アライ｜Ai思考実験とデータ分析 · 2026-11-27

It Wasn't Your Imagination: Reaching ChatGPT Limits Way Too Quickly Was Real
Over the past few days, even though you've been doing the same tasks, you hit the usage limit much sooner than before. If that's what you were feeling, it wasn't just in your head📉
On November 26, 2026, Thibault Sottiaux, who leads Codex and ChatGPT at OpenAI, posted on X. According to the post, when GPT-6.2 Astra and Sol were launched, there was a billing calculation error that mistakenly discounted usage for most users by undercounting it. Because this has now been fixed, he was reported as saying that the exact same work will now consume more of your plan's usage allowance.
The numbers are 40% and 25%. Rather than lingering on what happened, figuring out what changes you should make going forward comes first, so let's cover that first🧮
📋 What you'll learn in this article
- ✅ What became 40% faster and what hasn't changed
- ✅ How to claim the one-time limit reset token and its expiration conditions
- ✅ The official baseline figures for "how many messages every 5 hours"
- ✅ Actual measurements on my end for balancing tasks based on remaining allowance
- ✅ What is confirmed and what remains unverified about merging ChatGPT and Codex allowances in December
📉 Limits Weren't Decreased; the Counting Method Was Fixed
First, let's clarify what happened. It is not that the limit itself was reduced.
According to reports, there was a mistake at launch where usage was undercounted, and this fix merely restored the intended calculation method. Consequently, doing the same work as last week will cause you to reach your limit 40% faster on Astra and 25% faster on Sol. This applies strictly to these two models; it does not mean the overall ChatGPT limit is reached 40% faster across the board. Other models are unaffected. It is also reported that OpenAI will not retroactively bill users for the excess usage accumulated in the past💸
11/26 の前と後（報じられた内容）
  変わった    GPT-6.2 Astra / Sol の使用量の数え方（割引きをやめた）
  変わらない  他のモデル / 上限そのものの大きさ / 過去分の請求
  体感        同じ作業で上限に当たるのが Astra 40%早く・Sol 25%早く
One mathematical caution is in order. Hitting the limit 40% faster is not the same as the limit being reduced by 40%. If you consume allowance at the same rate, your usable amount becomes 1 ÷ 1.4, or about 71%, meaning the actual reduction is roughly 29%🧮 Additionally, the post did not mention whether message limits in the Chat tab will change (this remains unconfirmed).
Note that I have not been able to access the original text of this post directly. The X page could not be retrieved (HTTP 402), so this article relies on multiple news reports citing the exact same figures and quotes. The official text has not been independently retrieved📝
🎟️ A One-Time Limit Reset Token Has Been Quietly Granted
As compensation, it has been reported that Go, Plus, Pro, and Business accounts were each granted one "banked reset"🎟️ This is a token that lets you restore your usage allowance to full just once. It is not applied automatically and will be saved until you claim it. Since this token is not listed on the official pricing page, reports remain the sole source for this information.
Here is the critical point: if you leave it alone, it will eventually expire. The expiration date is displayed on screen before you confirm its use.
バンクされたリセット（1回・報じられた内容）
  対象       Go / Plus / Pro / Business（Enterprise は言及なし）
  場所       Web の使用量設定、またはデスクトップアプリの 設定 > Usage & billing
  出ない所   モバイルアプリ
  条件       対象の枠のどれかが残り80%未満の時だけ使える
  戻る量     Plus は5時間枠と週の枠を100%へ / Go は月の枠を100%へ
  注意       有効期限あり。使わないまま過ぎると消える
Therefore, claiming it right away puts you at a disadvantage. Because it cannot be used unless your remaining allowance drops below 80%, it is better to save the token for an exceptionally demanding day. The biggest waste would be letting it expire without ever realizing it was there😇
📐 The official figures are "6 to 50 messages" and "17 to 180 messages"
Looking only at a rate of change like 40% didn't give me a clear sense of things, so I pulled the figures from the official pricing page. It lists the estimated number of messages per 5 hours for Plus and Standard Business📐
5時間あたりの目安メッセージ数（公式の料金ページ・Plus と Standard Business）
  GPT-6.2 Astra   6〜50通
  GPT-6.2 Sol     17〜180通
  Pro             現時点で5時間の上限なし（通数は未掲載）
  公式の注記      これらは固定のメッセージ上限ではない
The reason there is an 8x spread is that the amount consumed per message varies depending on the content. The official page states that it changes based on the model, task content, context size, reasoning, tool usage, and caching. Pasting long documents significantly reduces your allowance in a single message, while asking short questions results in smaller consumption. That is why trying to manage it by message count will miss the mark🎯
The same page also clearly stated the details for Codex. Messages run locally and cloud chats share the same usage quota of the plan. Weekly limits may also apply. There is also a note stating that cloud tasks may consume more quota than local messages.
The unit price for paying overages with credits is also listed: it is 3x standard until February 28, 2027, and becomes 6x from March 1, 2027 (PT). The option to make up for shortfalls by buying extra credits will double in price next March💰
🔀 Checking the remaining quota and routing work to the other side
From here, it's about what I do on my end. If the limit comes early, there are only two things you can do: reduce the amount used per message, or reroute to another quota. I have automated the latter with a machine🔀
What I'm doing is simple: just dividing the remaining quota by the time until reset. If you only look at what percentage remains, you end up needlessly preserving the side that resets sooner. Dividing it by time tells you how much you can actually spend today.
2026-11-27 07時台に測った、自分の週の枠
  Claude  24.0% 使用  リセットまで 81.9時間  1時間あたり 0.93% 使える
  Codex   10.0% 使用  リセットまで 118.5時間 1時間あたり 0.76% 使える
  → この時点の判定は Claude（1時間あたり多く使える側）
Even though Codex has more remaining, Claude comes out ahead on a per-hour basis because its reset is closer. When I only looked at the remaining amount, I would route tasks to the side with more left on days like this, only to end up with surplus right before the reset📉 Note that these figures are from a day after the counting method was revised, and I haven't compared them against data from before November 26 (unmeasured).
The same mindset works even for people who only use a single tool. Concentrate heavy tasks in the morning to use up one 5-hour quota, and then run lighter tasks after the quota replenishes. Viewing your quota not as savings, but as a faucet per unit of time, will reduce the number of times you hit the limit🚰
🗓️ In December, the quotas for ChatGPT and Codex will merge into one
Another change that will take effect soon has been reported. It is said that for Plus, Pro, and Business, ChatGPT and Codex will begin sharing a single token-based usage quota🗓️
12月の変更（報道。公式ヘルプの文面は未取得）
  対象        Plus / Pro / Business（Enterprise・Edu は言及なし）
  変わる所    ChatGPT と Codex が1つのトークン基準の枠を共有する
  枠の外      Instant モデルとの会話。枠が尽きても使える
  未公表      枠の大きさ。これまでの別枠の合計と同じかどうか
  担当者の話  ほとんどの人はリセットの頻度は増えないが、ごく一部の重い利用者は早く当たるかも
This part needs to be read carefully. All I was able to confirm is that news reports are conveying the official help explanation as such. I haven't been able to retrieve the original text of the official help, nor has the quota size been disclosed. If the total stays the same, it's a win since you gain freedom in how you allocate it internally, but if it shrinks, it will be an effective price hike. Which one it is remains unconfirmed📝
Building on that, to share my projection, I believe workflows predicated on using only one quota will fall apart in December (speculation). My read is that people who pack code-writing and text-writing into the same day will start hitting limits on both in a single day. Whether that actually happens depends on the quota size, so it's not yet clear (unconfirmed).
💼 From a contractor's perspective, what hurts is not the cost, but the deadline
Looking at this from the perspective of freelance or client work, what hurts is not the cost, but the delivery deadline. Since the quota is designed to recover over time, waiting allows work to proceed. However, the waiting time varies depending on whether you were stopped by the 5-hour quota or the weekly quota, so it cannot be generalized as taking a fixed number of hours (unconfirmed). But if you promised delivery by this evening, your progress halts right there⏳
Here is my guess (this is speculation, not based on an actual order I received). Tasks that feed long documents into a single prompt—such as summarizing key points from meeting recordings, transcribing quantities from PDFs, or extracting tables from images—are the ones that heavily consume your limit with just one message. Conversely, jobs where you give short instructions over and over deplete the limit much less, even if message counts are high. That is why when taking on work, estimating based on character counts per job rather than number of messages yields far more accurate results📄
What clients pay for is not the cost of your usage limit, but the hassle of transcribing and verifying that they find too tedious to do themselves. If I were to specify who would actually pay, I have three targets in mind: solo or two-person professional service firms (like lawyers or accountants) that need recordings of consultations and meetings turned into written records every week; small construction contractors or equipment companies that need quantities transcribed from quotation PDFs and blueprints into spreadsheets; and solo instructors who need to extract key points for teaching materials from video recordings📋 All of these are tasks that would take the client hours, while all we use is our current subscription plan's quota. That part has not changed. What did change is simply the upper limit on how many jobs you can promise in a single day.
🛠️ Things to Do Today (3 Lines)
1️⃣ Pick one task that someone might ask you to do and create just one sample. For example, taking a one-hour meeting recording from transcription all the way to a 10-line summary. It only takes 20 to 30 minutes and the usage limit from your current plan, with zero extra payments required. 2️⃣ Note down the remaining % shown in your usage settings before and after running that one job. The difference is the limit used per job, which reveals how many jobs you can commit to within a 5-hour window. This becomes your unit for estimates. 3️⃣ Also check the same screen to see if you have one banked reset available. Even if you do, don't use it now—save it for a day when you drop below 80% remaining (you can't use it unless you are below 80%). If you have two tools available, divide the remaining % by the time left until reset and route the heavier tasks to the larger one.
🌟 Summary
It isn't that the limits were reduced, but rather that a counting error present at launch was fixed, with reports indicating that hitting the limit for the same workload now occurs 40% faster on Astra and 25% faster on Sol. This only affects these two models. It has also been reported that a one-time compensation credit was issued, which will expire if you do not claim it🎟️
The official guideline is 6 to 50 messages per 5 hours for Astra, and 17 to 180 messages for Sol, which is an eightfold spread. If you manage by message count, your estimates will be off, so tracking the volume entered per job will be much more accurate. Furthermore, it has been reported that ChatGPT and Codex quotas will be merged into one in December, though the exact size of the quota has not yet been announced.
Stop counting your quota like a savings account, and look at it as a faucet flowing over time. That is the only thing I changed today🚰
When you hit the limit, do you stop working for the day, or do you switch over to another tool?
Liking this post encourages me to write the next one🌟
👀 Here is what we do in the membership
💻 On Discord, I share everything: Markdown files and code from my own computer, along with methods for coding side hustles.
What we're working on this month includes records of things tested and decisions made, daily logs for LINE stickers, a system for posting on note every day, and anonymous surveys📋 I will also share the exact mechanism used behind the scenes for this article, which decides where to route tasks based on remaining % and time until reset.
🎁 In the membership (the member-only Discord "Side Hustle Kit Depot"), I directly distribute the original tools I actually run for my AI side hustle (Python scripts, prompts, JSON ledgers), along with 24-hour scheduled harnesses and ZIP archives of graphic assets. 
📦 Immediately upon joining, you can download all ZIP files at no additional cost (¥0), including an 8-panel one-click extraction tool for LINE stickers, a 24-hour harness & checkpoint kit, and 20 speech bubble & arrow graphic assets. 
The first 10 members get in for ¥980/month permanently (no free first month).
💡 I run a membership program. It is a small community capped at 10 people.
🔗 Related Articles
I have written about usage limits before: the story of how my quota melted away even after dialing back the effort level, and the story of the week rate limits were first introduced as a feature.
📚 Sources
- Official ChatGPT Pricing Page (Estimated limits per 5 hours and unit price for overages; retrieved on 2026-11-27)
- ChatGPT users hit limits up to 40% sooner after OpenAI billing fix (Notebookcheck coverage of a post on 2026-11-26)
- ChatGPT users hit GPT-6.2 Astra limits 40 percent faster after billing fix (datastudios coverage of December's shared quota)
- Post by OpenAI's Thibault Sottiaux on 2026-11-26 (body text not retrieved due to HTTP 402)
#AI #ChatGPT #OpenAI #GPT62 #Codex #AISideHustle #GenerativeAI #Usage #Subscription #BusinessEfficiency
