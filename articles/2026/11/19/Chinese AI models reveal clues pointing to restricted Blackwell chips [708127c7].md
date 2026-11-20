---
id: "708127c7ecc657fd"
title: "Chinese AI models reveal clues pointing to restricted Blackwell chips"
url: "https://scientificamerican.com/article/chinese-ai-models-reveal-clues-pointing-to-restricted-blackwell-chips"
link: "https://scientificamerican.com/article/chinese-ai-models-reveal-clues-pointing-to-restricted-blackwell-chips"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T18:20:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Peter Hall"]
language: "en"
summary: "The clues are hidden in the random numbers that form an AI model’s starting point—and hint at a new way to trace its origins"
tags: []
orgs: ["China", "Nvidia", "Alibaba", "OpenAI", "Meta", "DeepSeek", "UK"]
topics: ["chips & infrastructure", "models & research", "business & funding", "health & science"]
content_source: "fulltext"
word_count: 990
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Chinese AI models reveal clues pointing to restricted Blackwell chips

Scientific American · Peter Hall · 2026-11-19

The world of artificial intelligence hardware is becoming a noir movie. The plot already has a suspected spy, and now it has a forensics scene. In a report released on November 12, independent researcher Will DePue carefully dusted the weights of top Chinese AI models for prints—and found ones that he says were most likely left behind by banned hardware.
The report lays out evidence that six recent models from four Chinese AI companies—DeepSeek, Moonshot AI (maker of the Kimi models), MiniMax and Ant Group—got their start on Nvidia’s Blackwell chips, which the U.S. bars from export to China. Earlier models from those companies and newer ones from rivals such as Alibaba’s Qwen instead bear the marks of Nvidia’s previous Hopper generation of chips, versions of which Chinese companies have, at times, been allowed to buy.
DePue, who worked at OpenAI until earlier this year, calls his technique forensic. “Every single little processor has its own type, a small, different signature,” he says. By knowing which kinds of chips write which signatures into a model, he could tell which models were likely built on banned chips—and he believes careful analysis can reveal even more about where a model comes from.
On supporting science journalism
The suspected spy craft surfaced in late October, when the New York Times reported that U.S. intelligence officials believed an executive at a Singapore company that had bought billions of dollars’ worth of Nvidia hardware was spying for Beijing. She also reportedly had a close relationship with the chipmaker’s then CEO Jensen Huang. (Officials did not think he knew of any spying.) Huang has since acknowledged the affair with the alleged spy and resigned as CEO of Nvidia.
American chip exports to China are supposed to be tightly regulated. Cutting-edge chips such as Blackwell are off-limits, based on the theory that labs without access to the best hardware can’t build the best AI. Officials have accused Chinese companies of getting the chips anyway, though they have not offered much evidence yet. If DePue’s analysis holds up, it would confirm that the wall around the U.S.’s best hardware has a side door, and some of China’s top labs have found the way in.
The detective work is possible because of a quirk in the way a model gets its weights, the billions of numbers that collectively decide how to respond to any given prompt. Before a model sees any data at all, its weights start out as seemingly random numbers. Training slowly nudges these values toward their final form, which miraculously encodes the information and writing patterns in the data. Not all weights are nudged the same, though. “There are some specific weights in a language model that actually don’t change that much at all throughout training,” says Rohith Kuditipudi, a recent Ph.D. graduate in computer science from Stanford University.
“The model doesn’t have to go that far in this crazy dimensional space to get to the final model that speaks English,” DePue says. “Because it’s not moving that far, that initialization is still stuck in the weights.”
Those starting numbers aren’t truly random. Training software begins with a single number, called a seed, and feeds it to an algorithm that spins out a long string of random-looking values, one for each of the billions of weights. For efficiency, the work of generating them is split across the chip’s many processors. It just so happens that the way this work is split depends on the specific chip used.
A graphics processing unit, or GPU, the kind of chip used to train and run AI models, is made up of many processors that can all work at once. But “the hardware itself can’t run a million things,” says Tor Aamodt, a computer engineering professor at the University of British Columbia, who consults for Nvidia. Here the million things are random numbers, each headed for its own slot in the model-to-be. The question for the GPU, he says, becomes “How do you take the million and run it on something that has much less?”
Different generations of hardware have slightly different definitions of “much less,” though. The specific Hopper chips in question have 132 of these processors, which Nvidia calls streaming multiprocessors; the Blackwell chips have 148 or 152, depending on the version. Feed each the same seed, and the same random numbers land in different places depending on the chip type. By sifting through some six trillion combinations of seed and chip layout, DePue found the ones that reproduced the barely moved weights in each model he could read, revealing which kind of chip most likely laid down its starting point. The same hardware probably did the training, too, though the fingerprint alone can’t prove that. Nor can it say how the four Chinese labs gained access to Blackwell chips or where the chips sat—in a server room in China or a rented rack abroad—and DePue is careful not to claim proof of lawbreaking. But by his rough estimate, building these models took thousands of the chips.
DePue’s research has not been peer-reviewed—he self-published it—but Kuditipudi is sold. “I find the evidence pretty convincing,” he says. Aamodt finds the approach feasible at a glance but wants more evidence. “I would have liked to see the technical details on how that works,” he says. DePue says he sat on his findings for a while, until he was almost certain of them.
Since DePue released his report, these initial tracks have already been covered. PyTorch, a popular open-source tool kit for building and training AI models, is already in the process of removing this type of fingerprinting, according to an engineer at Meta who has been working on the program. “Unfortunately, it is pretty easy to erase these fingerprints,” DePue says, and he believes the open weights have more to tell. “The seed tracking example is just so immediate,” he says. “There’s a lot of forensic analysis we can do.”
