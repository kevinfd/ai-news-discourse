---
id: "75559b28fb32de68"
title: "Huawei Atlas AI Accelerator Latest Comparison Overview"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc9oje/huawei_atlas_ai_accelerator_latest_comparison"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc9oje/huawei_atlas_ai_accelerator_latest_comparison"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T05:08:49Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["matteiuspi"]
language: "en"
summary: "https://preview.redd.it/hwwhtgar5ywh1.png?width=1688&format=png&auto=webp&s=1aabdbd2bead7b89baece7308d4daf2463885712 Hey, your friendly neighborhood Atlas advocate here, here with an update--just got off the call with our Silver rated Huawei partner who has given us new information on the latest Atlas card lineup. Some of you were asking about the 950 series and after finally getting the info, I…"
tags: ["r/LocalLLaMA"]
orgs: ["China", "Meta"]
topics: ["products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 625
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc9oje/huawei_atlas_ai_accelerator_latest_comparison/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Huawei Atlas AI Accelerator Latest Comparison Overview

Reddit · matteiuspi · 2026-10-22

https://preview.redd.it/hwwhtgar5ywh1.png?width=1688&format=png&auto=webp&s=1aabdbd2bead7b89baece7308d4daf2463885712 Hey, your friendly neighborhood Atlas advocate here, here with an update--just got off the call with our Silver rated Huawei partner who has given us new information on the latest Atlas card lineup. Some of you were asking about the 950 series and after finally getting the info, I agree, I am compelled to want the other Atlas cards as well. The information on the 150 was only available in Chinese so I did have to translate it to make the above English copy. If you recall to my earlier posts on the topic, I have a system with 3 Atlas 300I duos and have done a ton of work to get QFN working well on one, two or three cards. I've been busy applying more recent optimizations to QFN to my vllm-fork and have been exploring further GLM5.3-flash, deepseek models, as well as have spent this past week on Meta Muse -- started with a REAP run to reduce the experts so it would fit on my three card Atlas 300I duo configuration. Muse and GLM are not fast enough for me on these Atlas 300I duo cards yet, but I will continue working on it, we'll see: https://preview.redd.it/ako373i69ywh1.png?width=2484&format=png&auto=webp&s=ebc307a319f0b65386c79410f6fee7a5213624c8 My friend Josh across the country, also picked up one of the 300I duos, and we have collaborated, I've played with qwen video models for describing security camera feeds, and he is using them to generate images, like this one: https://preview.redd.it/aqrqwiej6ywh1.png?width=1920&format=png&auto=webp&s=82573bc49e6b9d9084a3abdaa9f36912b02aebb3 After spending a couple years working on Ingenic security camera device hardware hacking, I have a special interest in this kind of tech. I think it will take global competition to see the pricing and implementation efficiencies of modern ML/LLMs normalize, and these offerings from Huawei are going to be the top competition out of China. I am working to get more information on the possibility to purchase as well the higher end Atlas Cards -- the Atlas 150 is pretty much brand new and uses the 950 Ascend cores, and if I get that far, I'll be providing more updates on how the cards compare IRL. Fnally, I have now a fourth Atlas 300I Duo card arrived, the one I promised in another post that I'd put to sale here it in the US market: https://opensensor.io/store/products/atlas-300i-duo-96gb Not a solicitation, do reach out with questions about the card if you were actually intrerested. I hope to be able to try out the higher end Atlas cards in the futrue. Current points: Passive cooled cards, and everyone case situation are different--I've designed a handful of shrouds now that takes fans to know--we've done some revisions depending on the enclosure and number of cards and type of fan. Requires an additional PCIe 12V CPU power (not pci-e) -- for Corsair type4 modular supplies, I do have the correct additional cables. Linux/programming knowledge absolutely required. Be aware that so far we have not found a way to modify the embedded Euler OS which actually passes signature verification (think secureboot) -- its not really an issue, but would be interesting if we could could sign our own firmware for getting into the lowest level details of the hardware cores. There is such a thing as getting a customer cert from Huawei for the purpose of signing your own firmware, but so far we haven't proven this out end to end larger with due to how to get the cert. Doesn't effect writing custom kernels or code that run on the NPUs, but does matter if you're a firmware nut. Post references: [1] Huawei Duo specifications https://e.huawei.com/cn/products/computing/ascend/atlas-300i-duo [2] Huawei A2 specifications A2 brochure https://e.huawei.com/cn/products/computing/ascend/atlas-300i-a2 https://e-file.huawei.com/marketingcloud/pep/asset/20000001/Material/799a9236e96a48b7aa126b10f3d7be97/M3T1A590N1195067466974908517/%E6%98%87%E8%85%BEAtlas%20300I%20A2%20%E6%8E%A8%E7%90%86%E5%8D%A1%E4%BA%A7%E5%93%81%E5%BD%A9%E9%A1%B5.pdf [4] llama.cpp chip identification [3] Supplied Atlas 150 hardware brochure. Atlas 150 compute figures may differ by 1% in measurement, per that brochur
