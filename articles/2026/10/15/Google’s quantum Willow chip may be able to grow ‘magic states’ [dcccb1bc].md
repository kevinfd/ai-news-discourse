---
id: "dcccb1bc9a866531"
title: "Google’s quantum Willow chip may be able to grow ‘magic states’"
url: "https://scientificamerican.com/article/googles-quantum-willow-chip-may-be-able-to-grow-magic-states"
link: "https://scientificamerican.com/article/googles-quantum-willow-chip-may-be-able-to-grow-magic-states"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T18:00:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Jacek Krywko"]
language: "en"
summary: "The work could help improve quantum computers’ accuracy in complex calculations"
tags: []
orgs: ["Google"]
topics: ["business & funding", "chips & infrastructure", "health & science", "models & research"]
content_source: "fulltext"
word_count: 635
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google’s quantum Willow chip may be able to grow ‘magic states’

Scientific American · Jacek Krywko · 2026-10-15

Quantum computers promise exponential computational power by processing many possibilities simultaneously. But the machines we have today are still far from this ideal. For one, their bits, called qubits, are prone to frequent errors, and as a result, quantum computers are limited for now. To overcome errors, the machines need to tap into so-called magic states—and scientists at Google Research think their quantum chip could help get them there. In a new study published today in Science, the researchers show how to supply magic states more cheaply using a gardening-inspired technique called cultivation.
Traditional computers build every calculation from a few simple logic gates, such as AND, OR and NOT. By contrast, “quantum computers have their own analogy of these operations called the Clifford gates,” explains Emma Rosenfeld, a researcher at Google Quantum AI and the study’s lead author. Clifford gates, however, can be imitated by a normal computer. “But there is one particular gate that unlocks the quantum computer’s power,” Rosenfeld says. “Physicists call it a non-Clifford gate, most often a T gate.” This extra gate is produced using a magic state.
A quibit in a magic state is prepared in a very specific blend of the states 0 and 1 (occupying a mixture of states is a specialty of quantum computers). Fed into a calculation, it is used up to perform the extra gate, and any flaw in the state becomes a flaw in the gate. “It has to be made very, very precisely,” Rosenfeld says.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
The standard recipe to make magic states is called distillation, and it creates fewer, more accurate quantum states from many imperfect ones. “You can have up to 95 percent of your quantum computer being spent just generating these high-fidelity magic states,” Rosenfeld says. To bypass this bottleneck, in 2024 her colleagues at Google Research proposed an alternative technique called cultivation, which works on a single state.
Using Google’s Willow chip, Rosenfeld’s team encoded a rough magic state in a few qubits and then measured it. Measuring a quantum state typically collapses it, forcing it into one of two possible answers. So instead of asking the question, “Are you 0 or 1?” which collapses the quantum state to either of those two options, the team asked, “Are you the right magic state: yes or no?”
States that pass this test are then spread across more qubits for stronger protection, hence the gardening name: the state starts small, gets checked and then grows. Without cultivation, about four attempts in 1,000 produced a faulty state. With it, errors fell by roughly 40-fold. The experiment used 54 physical qubits out of Willow’s 105.
“The Google experiment shows that cultivation works in practice,” says Kenneth Brown, director of the Duke Quantum Center at Duke University, who was not involved in the study. He notes, however, that the technique relies on a quality assurance step that rejects low-quality states, discarding 92 percent of attempts.
The result is still far from what practical applications demand. For example, using a quantum computer to break the current RSA-2048 encryption employed in website security, banking and electronic ID cards would require magic states that would fail only once in 10 billion tries. To simulate molecules, a use Rosenfeld says is more attainable, we would need such states with only one error in a million to one in 100 million. Right now the team stands at roughly one error in 10,000 attempts. Still, the new work represents a step in the right direction, she says.
“We’re more galvanized than ever to get to these near-term scientific applications,” Rosenfeld says.
