---
id: "f2d66d96cdd79a6b"
title: "Your AI Test Data Is Too Clean"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/24/your-ai-test-data-is-too-clean"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/24/your-ai-test-data-is-too-clean"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-24T12:30:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Shrey Srivastava, Forbes Councils Member"]
language: "en"
summary: "Organizations spend months choosing a model, then judge it against data far tidier than the world it will work in. Here's what to do instead."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["models & research", "agents & coding", "jobs & society", "products & launches"]
content_source: "fulltext"
word_count: 866
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6b0475f31b639d04d3bd6005/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Test Data Is Too Clean

Forbes · Shrey Srivastava, Forbes Councils Member · 2026-11-24

Shrey Srivastava, AI Data Foundry Head at Wipro, builds the data and test environments frontier AI labs use to train and evaluate models.
A healthcare company built a customer-support agent to answer questions about its policies. Every test it passed was a well-formed policy question, and it answered those well. And when my team asked it to write a JavaScript app, it wrote one.
An agent that will do any job a stranger hands it is running up compute bills and legal exposure that nobody signed off on.
I lead an AI data foundry, where my team builds evaluation data and red-teams models for AI labs and enterprises. The gap I see most often is the one in that agent’s tests: Organizations spend months choosing a model, then judge it against data far tidier than the world it will work in.
The fix is an evaluation set, a collection of real cases with the answers or behavior you expect, that every model has to pass before it touches customers. Models are replaced often; a good test carries over to the next one.
Build that test before you pick the model. Here’s how.
Put The Mess Back In
Many teams test on datasets cleaned to perfection, with every field filled and every answer correct. That cleanliness is a bias. A test built only from tidy inputs tells you nothing about what the model does when a scanned form arrives sideways or a customer types half an account number.
Gartner applies the same standard to AI data in general. In a February 2025 release, it said data is ready for AI only when it represents every pattern in the use case, errors and outliers included. In its July 2024 survey of 1,203 data management leaders, 63% of organizations either lacked the right data practices for AI or weren’t sure they had them. Gartner predicted organizations would abandon 60% of AI projects without AI-ready data through 2026, a window that closes in a few weeks.
So, pull test cases from raw inputs before your cleaning pipeline touches them, and keep the contradictory and half-finished records you’d normally discard. Then label the wrong answers as carefully as the right ones. A test that never shows the model a wrong answer can’t tell you whether it recognizes one.
Borrow Cases You Haven’t Seen
Your own data describes only what has already happened to you. A hospital’s records reflect its own patients and its own coding habits, so a test drawn from them misses the case that walks in next year.
You can close much of that gap in-house. Borrow anonymized records from another business unit or region, add public datasets from your industry, and ask your own specialists to write inputs designed to trip the model up. A lawyer told to break a contract-review tool will write clauses no archive contains.
Check The Basics Before The Domain
Out-of-scope requests belong in the test set, too. Red teams, mine included, tend to go straight for the hard domain risks, such as a wrong dosage or a leaked record. Those deserve the attention, but an agent that writes software on request is cheaper to catch and just as embarrassing to explain.
Before the domain tests, check scope:
• Ask the agent to do jobs outside its role, from writing code to drafting a resignation letter.
• Ask it to act as a different system or user, and see whether it plays along.
• List the tools and data it can reach. The OWASP Top 10 for LLM Applications recommends giving an agent only the functions and permissions its job needs.
• Write down what it must refuse, and run every item on that list after each change.
Keep The Test When The Model Changes
The value of the evaluation set shows up the second time you use it. In one project, an agent that read email through a connector kept citing the wrong message: Asked about an email from United Airlines, it quoted a USPS notice instead. We turned that failure into test cases, trained the model on them in a sandboxed environment, then ran the same cases again. On the use cases we had defined, its score went from 40% to 80%. That before-and-after number existed only because the test came first.
The same rerun protects you when a change makes things worse. A new model version, a reworded system prompt or a fresh batch of fine-tuning data can each undo behavior you’d already checked. That is why the set needs an owner. Without one, it goes stale the first time the team is busy, and the next model ships against whatever test someone writes that week.
Treat the set as part of your AI supply chain, alongside the data you train and prompt with. Add a case every time something goes wrong in production, so the test grows from your own failures. When a vendor pitches a better model, hand them your test instead of watching their demo.
Name the owner before your next model decision. Then let the models compete on your cases.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
