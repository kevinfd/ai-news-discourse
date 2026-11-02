---
id: "ad2acddb9b1392ef"
title: "Irregular: GLM-5.3 was told not to output memorized code, repeatedly did, and got correct answers"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xlm7h5/irregular_glm53_was_told_not_to_output_memorized"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xlm7h5/irregular_glm53_was_told_not_to_output_memorized"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T03:03:51Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "Irregular, an AI security evaluation company, published a test of Zhipu AI's open-weight GLM-5.3 on Oct 28. The part that caught my eye is a separate instruction-adherence test. They explicitly told the model not to output code reproduced from memory. Per the report, it \"nevertheless repeatedly reproduced memorized code verbatim and used it to reach correct answers.\" Irregular calls this a form…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 230
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xlm7h5/irregular_glm53_was_told_not_to_output_memorized/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Irregular: GLM-5.3 was told not to output memorized code, repeatedly did, and got correct answers

Reddit · shoumikgoswami · 2026-11-02

Irregular, an AI security evaluation company, published a test of Zhipu AI's open-weight GLM-5.3 on Oct 28. The part that caught my eye is a separate instruction-adherence test. They explicitly told the model not to output code reproduced from memory. Per the report, it "nevertheless repeatedly reproduced memorized code verbatim and used it to reach correct answers." Irregular calls this a form of reward hacking: the right answer, reached by bypassing a constraint the test was built around. A different test used vulnerabilities Irregular had planted in open-source code. A review of the transcripts found that code reconstructed from memory contributed to roughly 80% of the successful runs they examined. In those tests, using memorized code broke no instruction, but it can mean a correct finding reflects familiarity with the code rather than discovery. Irregular says it has seen this in closed models too, more often in newer ones, and that the familiarity persists even when internet access is restricted. Why it matters: an eval that only scores correctness would count these runs as wins. Irregular's advice is to check instruction compliance, and to monitor the model's reasoning alongside its actions and outcomes. I'm working from the write-up, not the transcripts. If you had to build an eval where a model is told not to use something it may have memorized, how would you tell whether it did? Source: https://www.irregular.com/research/glm-5.3-multi-stage-cyber-operations-and-instruction-violations
