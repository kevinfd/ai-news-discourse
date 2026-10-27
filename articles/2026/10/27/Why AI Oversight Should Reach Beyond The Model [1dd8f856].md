---
id: "1dd8f8560fdbf80d"
title: "Why AI Oversight Should Reach Beyond The Model"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/27/why-ai-oversight-should-reach-beyond-the-model"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/27/why-ai-oversight-should-reach-beyond-the-model"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-27T10:00:00Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Madhu Shashanka, Forbes Councils Member"]
language: "en"
summary: "Many AI failures are happening in the connections between systems that several parties built and one organization joined together."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["OpenAI", "Anthropic", "US government", "xAI", "Tesla"]
topics: ["agents & coding", "policy & regulation", "safety & ethics", "models & research"]
content_source: "fulltext"
word_count: 1037
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/691cdb24af47b8d8b9f8759a/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Why AI Oversight Should Reach Beyond The Model

Forbes · Madhu Shashanka, Forbes Councils Member · 2026-10-27

Madhu Shashanka is the Cofounder, Chief Scientist and CTO at Concentric AI and author of the forthcoming book, Coherence.
In September 2026, Senator Bernie Sanders and former FTC Chair Lina Khan offered different answers to the same AI fear.
Sanders moved to ban “superintelligent” AI outright and temporarily pause advanced development until a federal regulator writes rules.
Khan argued that enforcers can already charge AI companies and their CEOs under existing law for releasing “dangerous, unvetted or defective products” and that debates over new regimes should not distract from doing so.
The model makers have made their moves, too. Anthropic CEO Dario Amodei called for pacing the frontier and committed to giving outside evaluators employee-like access. OpenAI CEO Sam Altman said his company would match that commitment. Elon Musk of xAI also voiced support. Days earlier, OpenAI had asked Congress for mandatory national rules. 
These perspectives differ on what is needed to address AI risks, but they all point oversight at the same place: the models themselves. 
However, many AI failures are happening elsewhere: in the connections between systems that several parties built and one organization joined together.
The Risk Of AI Interconnection
As the co-founder of a company that helps companies manage data security and AI governance, I should note that my work inclines me toward organizational answers, so weigh my argument accordingly.
But consider how earlier this year, according to researchers, thousands of OpenAI agents took over a mostly dormant public wiki page and used it as a message board to coordinate with one another.
Meanwhile, in April, a coding agent working for PocketOS, a small software company, deleted the production database and its backups in nine seconds. The agent came from one vendor, the model from a second and the hosting from a third. In this case, the agent overreached: A token meant for a narrow job carried full permissions, and the backups sat in the same volume as the data.
As the founder wrote on X, “This isn’t a story about one bad agent or one bad API. It’s about an entire industry building AI-agent integrations into production infrastructure faster than it’s building the safety architecture to make those integrations safe.”
Neither of these examples required superintelligence. Ordinary agents with ordinary access were enough. In the wiki case, one company built and ran every agent. In the database case, however, three vendors and the customer each contributed a small flaw, and none was sufficient alone.
The second example is the one that should concern every enterprise. 
When a hospital or a bank joins agents from several vendors and its own teams, and the harm comes from how they were joined, the loss lands on the organization that joined them.
While I have found no public case at that scale yet, the small case shows the risk. Each part’s flaw is local, and no settled standard yet says how the parts should be joined.
The wiring also hardens over time. Companies learn which systems depend on one another only when they try to turn one off.
Why Each Fix Falls Short
Consider the ban first. A hard ceiling on capability answers a real fear. The bill summary defines superintelligence as a system that can “match or exceed human cognitive performance and capabilities across a broad range of domains or tasks.”
While that definition is clear on paper, it is hard to test in practice. Read broadly, it sweeps in today’s tools. Read narrowly, it waits for a threshold that is hard to measure. The bill’s pause on advanced development is a separate measure. It would slow what labs build next, and it would leave the agents already running inside enterprises where they are. It therefore doesn’t address the risk at hand. 
Khan’s proposal may help with oversight in the meantime, but enforcement works best when one company builds and runs the whole system.
The wiki case has a maker, a design and a defendant. But enterprises rarely buy from one maker. The hospital and the bank join agents from many vendors. Logs can show which agent acted. They cannot show a defect when each agent met its own specification. Ten parts from three vendors and your own team, each flawed a little, joined by you, leave one harm that vendor contracts tend to hand back to you.
The step of “pacing the frontier” proposed by the AI frontier labs also only examines the model. An evaluated model can still be joined badly, and no evaluator inside a lab sees how a hospital wires its agents together.
A ban, an enforcement push and the industry’s own pacing all leave the same space untouched.
What Leaders Can Do Now
None of this says a ceiling on the most dangerous systems is wrong; a genuine tail risk may deserve a hard line.
Bringing outside eyes inside the labs can be real progress. Liability can reach a maker whose agent trusts what it should not, an assembler who plainly cut corners or a company that built and ran the whole system.
None of them reaches the harm that exceeds any one party’s fault.
The questions that would catch it are organizational:
• Can you see what you run? Map the handoffs between agents as well as the agents to understand what each system’s output is feeding.
• Does each system have an owner? If not, name one accountable person for every handoff, because the joins are where ownership lapses.
• Can you tell when coordination drifts? Pick one enterprise-level outcome for each chain of agents and review it on a schedule.
• Can you pull a system back? Rehearse switching one agent off, and confirm that its backups and credentials sit outside its reach.
None of these steps requires a particular product, but they do require decisions about who sees, who owns and who can stop.
The same question sits unanswered for the hospital, the bank and the agency assembling these systems today: Can you see what you are running, and can you pull it back?
A ban, an enforcement action and an industry pledge will not answer that for you.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
