---
id: "d26ae9b2d9ce501c"
title: "Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases ‘medical superintelligence’"
url: "https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence"
link: "https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T18:43:53Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Rebecca Bellan"]
language: "en"
summary: "Microsoft’s new AI diagnostic system beat generalist doctors on hard cases, according to a study in Science. But most of the improvement seems to come from the AI models underneath, not from Microsoft’s system itself."
tags: ["AI", "Biotech & Health", "microsoft AI", "Mustafa Suleyman"]
orgs: ["Microsoft", "Google", "OpenAI", "Anthropic", "Meta", "DeepSeek"]
topics: ["health & science", "models & research", "products & launches", "safety & ethics"]
content_source: "fulltext"
word_count: 1102
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases ‘medical superintelligence’

TechCrunch · Rebecca Bellan · 2026-10-22

Microsoft’s AI diagnostic system correctly diagnosed complex medical cases in a simulation more than twice as often as generalist physicians, according to a study published Thursday in Science. Mustafa Suleyman, Microsoft AI’s CEO, called the result a step toward “medical superintelligence.”
The system, dubbed MAI-DxO (DxO for short), coordinates several AI agents that act like a panel of doctors. They question a patient, order tests, and debate a diagnosis.
In a simulation using complex cases from the New England Journal of Medicine, it was correct 83% of the time. Primary care doctors and general internists, working individually with reference materials, were correct 36% of the time. One note: Cases this complex are usually handled by specialists or physician teams, who weren’t part of the comparison.
“There is something very substantial and exciting here,” Dominic King, vice president of Health at Microsoft AI, told TechCrunch. “The biggest challenge in healthcare delivery at the moment is the growing mismatch between demand and supply of medical expertise.”
In publishing these results, Microsoft joins Google and OpenAI in claiming that its AI can match or outperform doctors.
The study’s own data suggests that much of the improvement comes from more powerful underlying AI models, with Microsoft’s orchestration system adding gains on top.
Microsoft tested MAI-DxO with models from several companies, including OpenAI, Google, Anthropic, Meta, and DeepSeek, but its best results came with OpenAI’s GPT-5 and GPT-5.5.
Microsoft measured DxO on cost as well as accuracy, meaning the estimated cost of running the AI on each case. On its own with a short, basic prompt, GPT-5 scored 78.9% on complex cases at about $8,400 per case. DxO cut that cost by about $3,000 but raised accuracy by only about four points. On emergency department cases, there was little improvement in either accuracy or cost improvement between GPT-5 on its own and with the assist from DxO.
With GPT-5.5, a newer model released in April 2026, the results split. On complex cases, DxO increased GPT-5.5’s accuracy score from 72% to nearly 87% at a slightly cheaper cost. However, the gains once again didn’t show up on emergency department cases. Both (with and without DxO) scored about 85% at a similar cost.
DxO helps most on complex cases and with less capable AI models. Gemini 2.5 Flash, for example, scored 46.4% on its own but nearly 69% with DxO. Even so, the gap between the weaker and stronger models was larger than the boost DxO provided.
Microsoft’s researchers said that accuracy gains naturally shrink as models approach the theoretical maximum. “The DxO orchestration helps with the broader challenge of optimization both accuracy and cost,” a spokesperson added.
Suleyman, who leads Microsoft’s effort to build its own frontier AI, told TechCrunch that the company is working with the Mayo Clinic to train a foundation model for healthcare, with release planned for next year. He believes this model will enable the company to “make really enormous leaps here,” and says DxO is part of the foundational infrastructure Microsoft is building to see real breakthroughs in healthcare.
“I really believe that in 2027, we will be on the verge of a coding style breakthrough for medical records,” Suleyman said. “I think we’re going to be able to stream highly accurate predictions about how a medical record might unfold, and obviously that kind of foresight for a clinician is gold dust.”
Suleyman has spent his career trying to use AI to solve medical issues. He was previously a co-founder of DeepMind, which was acquired by Google in 2014. The following year, Google DeepMind acquired King’s startup Hark, a clinical task management app, and the two of them launched DeepMind Health together. Suleyman joined Microsoft to lead its AI unit in 2024, and King followed a few months later.
“We’re just true believers,” Suleyman said.
He said while the use of generative AI in healthcare is still early, he expects healthcare models to get “an order of magnitude better in capability within the next 24 to 36 months.”
“As we’ve seen multiple times in the last five or six years, the progress happens very quickly once you have a flywheel,” Suleyman said. “A flywheel means we have a model in production which we are iterating with real-world usage in order to identify gaps in the model and then patch them and improve them. That’s what’s happened in coding. It’s what happened in chat before that. And I think next year it’s going to start to happen for medical records and for clinical decision support.”
Through a new partnership with Beth Israel Deaconess Medical Center in Boston, Microsoft will evaluate the clinical reasoning capabilities of DxO across different hospital settings.
“This technology is ready for real-world evaluations, and you can imagine the complexity and diversity of issues that come from a Boston emergency department on a Friday evening,” King said.
He explained how the study will work: Patients will get standard treatment, including triage, time with a specialist, treatments, investigations, and decision on whether it’s safe to discharge. In parallel, those who consent will also engage with DxO. Microsoft and its partners will compare DxO’s recommendations against the human doctors’.
Google published a clinical study alongside Beth Israel in The Lancet this month to evaluate Google’s AMIE conversational diagnostic AI in real-world urgent care visits, while human physicians monitored the interactions in real time.
“We think this will be the biggest study of its kind,” King said. “It will be across not just emergency settings but urgent care environments, and will give us very compelling evidence by the end of the study period around the ability for these systems to be deployed at greater scale in the future.”
Microsoft’s study in Science coincides with a manifesto of sorts around what it will take to build medical superintelligence, defined as “the capacity to surpass the strongest contemporary human-led health systems in medical reasoning and coordination across the full arc of care.” Microsoft hopes to move beyond benchmarking individual tasks — like answering medical exam questions and generating diagnoses — into integrating with clinicians and healthcare systems for better outcomes.
“This is the kind of technology that everybody in the world wants, and that’s why we’re committed to doing everything we can to accelerate its introduction to the world,” Suleyman said, adding that this focus could be a differentiator for Microsoft compared to the other frontier labs.
Microsoft already sells dictation and radiology tools to clinicians and sees DxO as an expansion to those efforts.
“We have to have the absolute number one state-of-the-art medical clinical decision support products over the next few years,” Suleyman said.
