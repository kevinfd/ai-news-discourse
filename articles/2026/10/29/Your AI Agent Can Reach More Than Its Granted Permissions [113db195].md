---
id: "113db19553c1e2f4"
title: "Your AI Agent Can Reach More Than Its Granted Permissions"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/29/your-ai-agent-can-reach-more-than-its-granted-permissions"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/29/your-ai-agent-can-reach-more-than-its-granted-permissions"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-29T10:30:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Kiran Elengickal, Forbes Councils Member"]
language: "en"
summary: "Memory compounds the problem. If an agent caches what it fetched into its own memory, that data outlives the access check that let it in."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["US government", "Microsoft"]
topics: ["agents & coding", "products & launches", "safety & ethics"]
content_source: "fulltext"
word_count: 1046
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6adf9a140418747148c7e2c0/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Agent Can Reach More Than Its Granted Permissions

Forbes · Kiran Elengickal, Forbes Councils Member · 2026-10-29

Kiran Elengickal | Vice President at Siemba | AI, Cybersecurity, GTM Expert | Strategic Growth | Alliances | Innovation Leader.
An AI agent’s access list records what it was granted. For AI agent security, the number that matters is what the agent can get other systems to do for it.
Consider an analytics agent approved for two sales datasets and nothing else. Its approval list is short and easy to defend. Elsewhere in the same environment runs a shared data-movement service, built so that nobody had to configure each integration individually, which executes requests under a privileged service account. The agent needs no elevated rights of its own. It needs to find that service and word a request the service will accept. Hidden text in a document will do it, as will a misread instruction or a misconfigured pipeline.
I call this borrowed authority. Security engineers know it as the confused deputy problem, which is decades old. What agents change is volume and improvisation. They chain calls in sequences no engineer scripted, and software that writes software defaults to the flexible shared service because it is the fastest route to a passing test. Nobody schedules its removal.
Where The Platforms Stand
Each major data platform offers a way to enforce access controls closer to the user’s identity. Databricks explains in its documentation that when an app accesses resources through its own service principal, all users share that principal’s permissions, preventing the platform from automatically enforcing fine-grained policies based on individual user identities. With user authorization, Unity Catalog’s row filters and column masks can instead enforce the user’s existing permissions.
Snowflake stored procedures run with their owner’s privileges by default, which can create risks when an agent’s actions need to be limited to the caller’s permissions. Microsoft’s on-behalf-of flow provides a way for a middle-tier API to obtain a token representing the user and pass delegated identity and permissions to a downstream service.
Masking salaries or limiting rows by region only works if the platform knows who is asking. Send the request through a shared identity and those controls keep running, against the wrong party. The audit log shares the blind spot: It shows an agent read the customer table, not who sent it there.
Memory compounds the problem. If an agent caches what it fetched into its own memory, that data outlives the access check that let it in. Another agent, or a user with lower rights, can retrieve it later without going near the privileged service. OWASP flags this in its guidance on vector and embedding weaknesses and recommends memory stores that enforce who may retrieve what.
Acting as the requester is the right default, but it falls short on its own. Users often have more permissions than a particular task requires, and prompt injection can manipulate an agent into misusing those permissions. The agent’s effective access should therefore be narrower than the user’s wherever possible.
Databricks supports this approach through API scopes that limit what an app can do on a user’s behalf, alongside the user’s existing data permissions. More generally, a short-lived, narrowly scoped credential for each task can limit exposure. Standards such as OAuth token exchange support issuing tokens for specific downstream services and narrower scopes, although their lifetime and permissions depend on the implementation. For high-impact or irreversible actions, require explicit human approval, consistent with OWASP’s guidance on excessive agency.
There are limits to this approach. Some integrations only support shared credentials. Scheduled agents need a workload identity rather than an interactive user’s identity, with permissions restricted to the job’s requirements. User-context execution can also reveal overly broad permissions that existing access controls have allowed to persist. Databricks, for example, limits its forwarded user token to the workspace where the app runs.
Who Is Accountable
In many companies, security owns identity, the data team owns the platform and whoever builds the agent owns the shortcuts. No one owns the path from an agent’s request to the data it ends up touching. That makes it a governance gap more than a configuration error, and reviewing configurations will not close it.
NIST’s AI Risk Management Framework assigns accountability to leadership: Executive leadership takes responsibility for risks associated with AI development and deployment.
The SEC’s 2023 rules also require covered public companies to describe board oversight of cybersecurity risk and management’s role. Material cybersecurity incidents generally must be reported within four business days of the materiality determination. Without an audit trail showing who initiated an action, making that determination can be harder. Whether agent data access creates additional disclosure obligations is a question for counsel, and one best asked before an incident.
Name one executive for the whole path, and have security or internal audit do the measuring, so the team building the agents is not grading itself.
Four requirements follow:
1. Map what each agent can reach rather than what it was granted, because whatever it can call is, in practice, within its reach.
2. Make acting as the requester the default for sensitive data and attach a named owner to every exception.
3. Treat any shared service that executes whatever it is told as a finding until proven otherwise.
4. Put an expiry date on everything agents create, including temporary tokens and test pipelines.
The measure I would put in front of the board is a single number. Of the actions agents take on sensitive data, what share can name the person who asked and show that the access applied was no wider than the request required? A sample of last month’s agent actions is enough to set a baseline. Treat any vendor-quoted industry benchmark with suspicion, because the measure is too new for one to mean much.
Gartner predicts that “over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls.” Borrowed authority falls under the third. A company that can produce the number above can point its agents at customer and employee data. One that cannot will keep them on safe, low-value data.
Vendors will tell you they have this covered. Ask whose name shows up in the log.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
