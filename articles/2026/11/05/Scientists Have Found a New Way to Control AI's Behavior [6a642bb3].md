---
id: "6a642bb3ee2a2eb4"
title: "Scientists Have Found a New Way to Control AI's Behavior"
url: "https://time.com/article/2026/11/05/ai-cheating-scientists-report-alignment"
link: "https://time.com/article/2026/11/05/ai-cheating-scientists-report-alignment"
source: "TIME"
domain: "time.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-05T15:45:02Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Harry Booth"]
language: "en"
summary: "—Illustration by TIME (Source Images: Narumon Bowonkitwanchai, baona, Vergeles_Andrey—Getty Images) Artificial intelligence models have, in recent months, hacked a multibillion-dollar company, meddled with government data, and even filed a fabricated homicide tip to police, all under the noses of their creators. They did so not in pursuit of world domination, but to maximize their scores on…"
tags: ["Business"]
orgs: ["Anthropic", "Salesforce"]
topics: ["models & research", "business & funding", "safety & ethics", "policy & regulation"]
content_source: "fulltext"
word_count: 1001
paywalled: false
image: "https://static.time.com/v3/assets/bltea6093859af6183b/blt03c771aa668f8304/6aecc6485fb446613bcfb01d/ai-cheating.jpg?branch=production"
discussion_url: null
score: null
comments: null
community: null
---

# Scientists Have Found a New Way to Control AI's Behavior

TIME · Harry Booth · 2026-11-05

Artificial intelligence models have, in recent months, hacked a multibillion-dollar company, meddled with government data, and even filed a fabricated homicide tip to police, all under the noses of their creators. They did so not in pursuit of world domination, but to maximize their scores on tests. In other words, they cheated.
On Nov. 5, AI interpretability startup Goodfire unveiled a technique it says sharply reduces that impulse. In a paper shared exclusively with TIME ahead of publication, researchers use signals from inside models to reward them not just for getting the right answer, but for getting there in the right way. In early tests, the technique could also make models less eager to tell users what they wanted to hear and even discourage medical-image recognition models from relying on misleading clues.
The news lands as existing ways for spotting AI misbehavior have begun to break down. Researchers rely on a model’s “chain of thought,” a trail that doesn't really contain its thoughts at all. It is closer to the scrap paper a math student uses to work through a problem. But when models suspect they are being watched, they can be selective about what goes on paper. Increasingly, they can do the work in their heads.
Goodfire’s technique goes after the thoughts themselves, or at least the ones researchers have already catalogued. So far, it has been tested only on models roughly 1/300th the size of frontier systems. But Goodfire is betting that the larger the model, “the cleaner the representation” of internal concepts, making those signals easier to read, says paper co-author Thomas Fel.
Why AI cheats
After teaching their AIs to predict words, developers put them through a digital obstacle course—ranging from math puzzles to web surfing—and reward them only when they succeed. With each correct solution, the model’s parameters—the strength of connections between digital neurons—update.
Models are rewarded regardless of how they completed their task, incentivizing shortcuts or other questionable impulses, like accruing power.
A version of this problem helps explain why AI is often a suck-up. During training, models are rewarded for answers most likely to receive a “thumbs up” from human graders. Known as “reinforcement learning from human feedback,” or RLHF, the technique was heralded as a safety breakthrough in 2022 for its ability to turn unruly language models into well-mannered chatbots, curbing their tendency to offer racist and misogynistic responses. But it can also make models pathologically agreeable, sometimes indulging and reinforcing users’ delusions.
The underlying riddle is how to train AI to do something without inadvertently teaching it the wrong lesson—known among researchers as the “alignment problem.”
A new way to steer model behavior
Similar to how neuroscientists use real-time magnetic resonance imaging to identify which regions of brain activity correlate with certain states, interpretability researchers have developed tools for recognizing which patterns of digital neuron activations correspond with concepts like “the Golden Gate Bridge” or “reward hacking,” the technical term for AI cheating. A tiny AI model can then be trained to spot these patterns. The result is known as a “probe,” a narrow window into the model, which fires when it “thinks” about a particular concept.
Anthropic already uses probes as guardrails, flagging potential trouble before an answer reaches the user. But Goodfire instead used those signals to specify how a model should solve a task. In one example, Goodfire tasked AIs with a series of math puzzles, gave them a file with the answers, but told them not to open it. The ordinary training rewarded success so effectively that the models learned to peek almost every time. Using a probe to penalize “reward hacking” reduced that to near zero.
Whether the technique will work on the sorts of complex tests frontier models undergo during training remains an open question. But early experiments suggest it works across different tasks. After warming up on the math puzzles, Goodfire then tasked the AIs with chess challenges. The one that had not been penalized for cheating on math peeked at the answer sheet 99% of the time, while the one that had did so less than 1% of the time.
It also seemed to work for curbing AI’s other bad habits. The researchers tried penalizing a model when responses were influenced by its internal concept of "sycophancy,” and it learned to be less excessively agreeable. This approach, Fel hopes, could be used to specify which information an AI should disregard, such as an applicant's gender when screening résumés.
Even a perfectly controllable AI won’t resolve the question of who should control it. But “this could be a breakthrough,” says Naomi Saphra, an assistant professor at Boston University, who has spent almost a decade working on language model interpretability. Its practical application will depend partly on whether the improvements justify the human effort required to identify and interpret the model’s internal patterns, she says.
Penalizing an internal pattern can change its shape, essentially pushing the “thought” elsewhere in the neural network and outside the probe’s narrow view. Dam a stream and the water finds another channel. That risk of losing monitorability has made training on internal signals taboo among some researchers. But a pattern change isn’t necessarily lost, Fel says. In experiments, recalibrating the probe could bring a pattern back into view, and where that fails, more sophisticated statistical tools could recognize combinations of signals simpler probes missed.
Goodfire raised $150 million in a Series B round in February, valuing the company at $1.25 billion. (Investors include Salesforce, where TIME's co-chair and owner Marc Benioff is the CEO.) It publishes its research freely, though it rents its interpretability tools to other AI companies. “The more people are doing interpretability, the more people will use our platform,” says co-founder and CEO Eric Ho.
“If we manage to scale this technology, and overcome any of the possible hurdles with loss of monitorability,” says Tom McGrath, Goodfire’s co-founder and chief scientist, “I think this would be like one of the biggest advances in alignment technology that has happened.”
