---
id: "e0489ed045c5aea9"
title: "AI Can Get Smarter Without Getting More Authority"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/06/ai-can-get-smarter-without-getting-more-authority"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/06/ai-can-get-smarter-without-getting-more-authority"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-06T11:15:00Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Binny Gill, Forbes Councils Member"]
language: "en"
summary: "Human control does not require understanding every decision a model makes. It requires ensuring that AI cannot decide the extent of its own authority.​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "Hugging Face"]
topics: ["models & research", "safety & ethics", "agents & coding", "health & science"]
content_source: "fulltext"
word_count: 878
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6aeb927f45eff33db7f1f994/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI Can Get Smarter Without Getting More Authority

Forbes · Binny Gill, Forbes Councils Member · 2026-11-06

Kognitos Founder & CEO Binny Gill holds nearly 100 patents in computer science.
We all saw something unusual happen in AI as some of the people building the world’s most capable systems began arguing that the technology may be advancing faster than our ability to control it.
Anthropic CEO Dario Amodei called for the industry to “pace the frontier,” warning that AI capabilities could advance faster than our ability to control them. Other AI leaders echoed this, and Anthropic began measuring how much AI contributes to developing future AI systems.
I take those concerns seriously, but I think they also expose an assumption that deserves more scrutiny. We often talk as though greater intelligence must inevitably bring greater autonomy, when the two are separate engineering decisions.
Control Should Sit Outside The Model
Much of the frontier safety debate focuses on models themselves. Researchers want to understand model behavior and whether systems continue to follow human intent as their capabilities increase. But control can sit where the model’s reasoning meets the outside world.
Imagine an AI model concludes that a customer should receive a $20,000 refund. Whether that refund actually happens isn’t the model’s call. The business defines the rules: Refunds under $500 are issued automatically, anything over $5,000 requires a manager’s approval, and some actions are never permitted without a human. So the model recommends, and the execution layer applies those rules and routes this one for sign-off.
This is the value of keeping the execution layer deterministic. Generative AI reasons probabilistically; that’s inherent to how it works. But the rules governing what it can do can be explicit, predictable and enforceable.
Human Control Cannot Mean Approving Every Action
If someone has to click “approve” 10,000 times a day, we have re-created manual work under a different name. Keeping people in control is less about making humans approve everything and more about making humans responsible for the boundaries.
Low-risk actions might execute automatically, while changes involving money, sensitive data or binding customer commitments require approval. Some operations may remain completely outside the AI system’s permissions.
Businesses already work this way. They establish permissions, approval thresholds, SOPs and separation of duties, then build systems that enforce them consistently.
AI needs an equivalent approach to authority. For an enterprise deploying agents, this produces much more useful questions than whether a model can simply be “trusted.” What can it change? When does somebody need to intervene? If something goes wrong six months from now, can we reconstruct what the model proposed, what rules applied and why an action was permitted?
More Intelligence Makes Boundaries More Important
As models become more capable, it is tempting to give them broader access because additional permission makes the system appear more useful. The danger is that authority expands almost accidentally, one integration and one exception at a time.
A model that becomes much better at reasoning may eventually reach conclusions that its users cannot easily follow. That creates a genuine interpretability challenge, but it does not follow that the same system must also be free to act on those conclusions without constraint.
Remaining in control does not require people to stay more intelligent than the AI systems they use; it requires organizations to decide where those systems’ authority begins and ends.
None of this removes AI risk. People can define bad policies, permissions can be misconfigured, and humans can approve the wrong action. But those failures happen at identifiable boundaries within the systems that can be tested, audited and improved.
Build For The Intelligence That Is Coming
The recent Hugging Face incident is a good example; in this case, the guardrails didn’t fail the way people expected. The team believed the permissions were tight enough, and they were in testing. What broke them was the agent inventing a sequence of steps at runtime that nobody anticipated. This is a flaw in controlling an agent only through access: A sufficiently capable model will find a path through whatever access it has, and no permission set can enumerate every path in advance. 
I favor separating planning from execution. A neurosymbolic architecture lets the model do what it is good at: reasoning about an ambiguous goal and producing a plan in plain English that a human can read and approve, then handing that plan to a symbolic engine that executes it exactly as written. The model cannot improvise new steps at runtime because it is no longer the thing running.
Over time, approved plans become a library of safe building blocks the AI can compose to reach new goals, and composing vetted parts is a very different risk than open-ended invention. If novelty is throttled at the plan level, the system can keep broad capabilities like internet access while doing only what was reviewed. Organizations already work this way: A hospital or bank approves standard operating procedures rather than vetting every decision. The AI equivalent is a reviewed plan, executed deterministically, with any deviation requiring new approval.
The debate over AI safety and how quickly models should advance will continue, but enterprises can already build systems that keep increasingly capable AI within defined limits. Human control does not require understanding every decision a model makes. It requires ensuring that AI cannot decide the extent of its own authority.
