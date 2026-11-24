---
id: "073594fd111e60b0"
title: "OpenClaw at one: its chief architect on a year of explosive growth, wooing the enterprise, and being Meta’s muse"
url: "https://thenewstack.io/openclaw-vincent-koc-interview"
link: "https://thenewstack.io/openclaw-vincent-koc-interview"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T12:39:32Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Paul Sawers"]
language: "en"
summary: "It’s been a whirlwind 12 months for OpenClaw , the open source personal AI agent used for everything from managing calendars and email to booking flights and restaurants. \n\n On Nov. 24, 2025 — exactly a year ago today — Austrian software developer Peter Steinberger made the first commit for Warelay, a small WhatsApp relay designed to let users trigger actions on their computer through WhatsApp.…"
tags: ["AI", "AI Agents", "AI Infrastructure", "Open Source"]
orgs: ["Meta", "OpenAI", "Anthropic", "Nvidia"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "summary"
word_count: 2486
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenClaw at one: its chief architect on a year of explosive growth, wooing the enterprise, and being Meta’s muse

The New Stack · Paul Sawers · 2026-11-24

It’s been a whirlwind 12 months for OpenClaw , the open source personal AI agent used for everything from managing calendars and email to booking flights and restaurants. 

 On Nov. 24, 2025 — exactly a year ago today — Austrian software developer Peter Steinberger made the first commit for Warelay, a small WhatsApp relay designed to let users trigger actions on their computer through WhatsApp. It briefly became Clawd, a play on Claude and its lobster mascot, before Anthropic’s legal team “politely” asked Steinberger to reconsider the name. After another short-lived stint as Moltbot, the project finally settled on OpenClaw at the end of January, 2026. 

 OpenClaw has become one of the most closely watched open source projects in AI. That excitement ultimately led OpenAI to hire Steinberger in February, with the project eventually moving into an independent foundation backed by companies including OpenAI itself, GitHub, and Nvidia. 

 Meanwhile, the Foundation has also stepped up its enterprise push, while the arrival of OpenClaw 2.0 focused heavily on making the project easier to install and use. 

 Ahead of the one-year anniversary, The New Stack caught up with Vincent Koc to chat all things OpenClaw, including how the project has matured, its growing enterprise ambitions, and how it has influenced projects from some of the biggest names in technology. 

 OpenClaw grows up… and becomes Meta’s muse 

 As an open source project available under an MIT license, anyone is able to take OpenClaw and do more or less as they please with it — including building their own products and services around it. However, its influence also extends into the broader agentic AI realm, as evidenced in September when Meta launched Muse , described as the “world’s first personal AI agent built for everyone.” 

 Meta’s Muse in action 

 Like OpenClaw, Muse is designed to act on a user’s behalf across apps, retain personal context, and carry out tasks through a browser. But when Muse hit the market in September, Ansh Nanda , co-founder and CEO of Vibecode , noted that the similarities went considerably further, calling it “LITERALLY Openclaw for normies,” adding that “it’s actually just openclaw.” 

 To support that assertion, Nanda shared a screenshot in which Muse compared its own system files with the OpenClaw GitHub repository. It reported the same set of workspace file names — including SOUL.md , MEMORY.md , USER.md , IDENTITY.md , TOOLS.md , HEARTBEAT.md , AGENTS.md and BOOTSTRAP.md — and said parts of its SOUL.md closely matched OpenClaw’s. 

 we built muse from scratch, but it is definitely heavily inspired as a product by openclaw. After I used openclaw in january I bought hundreds of mac minis for the MSL team and lots of us fell in love with using openclaw (and other personal agents). @steipete is a genius and his… — Nat Friedman (@natfriedman) September 21, 2026 

 Nat Friedman , ex-GitHub CEO who’s now heading up Meta’s AI products and applied research unit, didn’t shy away from the influence. He said the company had developed Muse “from scratch,” but added: “…it is definitely heavily inspired as a product by openclaw.” 

 Indeed, Friedman said that Meta’s goal was to make an OpenClaw-like experience secure and easy enough for a much broader audience. When pressed on why Muse was sailing so close to the exact file names, Friedman replied : “We thought that Peter [Steinberger] got those things exactly right!” 

 Meta, of course, wasn’t the only company influenced by OpenClaw. And in some respects, the intense hype that surrounded the project earlier in the year has moved elsewhere as a growing number of companies have launched agents of their own. 

 “From our perspective, I think it’s nice that the hype has died down, the spotlight’s off of us, and we can get focused on actually building a good product without everyone having ‘lobster fever’.” 

 “There’s always going to be hype in the zeitgeist, and there’s going to be the new shiny object that everyone gravitates towards,” Koc tells The New Stack . “From our perspective, I think it’s nice that the hype has died down, the spotlight’s off of us, and we can get focused on actually building a good product without everyone having ‘lobster fever’.” 

 Getting hooked on OpenClaw 

 Koc himself first encountered OpenClaw before most of that attention arrived. At the time, he was working at AI evaluation and observability company Comet , and started to notice the project cropping up repeatedly online around the tail end of 2025. 

 He installed it out of curiosity and, despite encountering plenty of bugs, spent the next four or five days using it almost continuously. What caught his attention was the way it could change its own code in response to instructions, but also how different the interaction felt compared with the AI chatbots he had been using. 

 “It was like you’re talking to a mate on WhatsApp or iMessage. It felt very personal.” 

 “There was ChatGPT and Claude, but they felt somewhat robotic — it felt like I was still talking to an agent,” Koc explains. “Whereas with this [OpenClaw], it was just this continual chat thread, it was like you’re talking to a mate on WhatsApp or iMessage. It felt very personal.” 

 Koc soon began contributing himself, initially concentrating on security vulnerabilities as a way of getting Steinberger’s attention. That led to him becoming a security maintainer, before his remit expanded into the project’s wider architecture. By the time the pair discussed Koc working on OpenClaw full time, he says he had become its second-largest code contributor. 

 The project’s future became a more pressing question in February, however, when OpenAI hired Steinberger. “Yes, I could totally see how OpenClaw could become a huge company,” he wrote at the time. “And no, it’s not really exciting for me. I’m a builder at heart.” 

 Instead, Steinberger said the project would remain open and independent under a foundation, with OpenAI sponsoring it and enabling him to continue working on it. That foundation was formally established in July , bringing in its first full-time team, including Koc as chief architect. Steinberger remains heavily involved in the project’s engineering direction, Koc says, even as a larger team has assumed responsibility for the Foundation’s day-to-day work. 

 “He was the founder of this project, he was there from day one,” Koc says. “His vision and his involvement matters deeply, but beyond that, we have a large team that’s looking at everything from our corporate relationships to marketing and events.” 

 And the list of companies now involved extends well beyond OpenAI. Alongside sponsors including GitHub and Nvidia, OpenClaw has maintainers from Microsoft, Tencent, Atlassian and others. And Koc says the Foundation is working with labs, as well as technology companies across Asia and Europe. 

 Koc says those companies have different motivations for getting involved, but OpenClaw’s independence is ultimately a big part of the attraction. 

 “Different companies have joined for different reasons,” Koc says. “I think individuals in these companies saw the potential, saw we are independent, we are open source, but also we’re not venture backed. So it creates this really interesting thing, where they can see us like another Linux or Mozilla — something that’s going to live longer.” 

 “It creates this really interesting thing, where they can see us like another Linux or Mozilla — something that’s going to live longer.” 

 Microsoft offers one of the clearest example of where that involvement can lead. In June, it unveiled Scout , an always-on personal agent for Microsoft 365 powered by OpenClaw. Microsoft corporate vice president Omar Shahine said at the time that the company had added the identity, credential, access and security controls needed to make it suitable for enterprise use. 

 Microsoft Scout has since been rebranded as Autopilot 

 Microsoft also contributed policy-conformance work directly upstream to OpenClaw, allowing organizations to check deployments against their security and compliance requirements and produce an audit-ready result. 

 Nvidia has taken a similar route with NemoClaw , which builds on OpenClaw while adding its own security , privacy and policy controls through the company’s OpenShell runtime. 

 Scout was renamed Autopilot in September as part of Microsoft’s revamped Copilot lineup, but the OpenClaw connection remains. And with both Microsoft and Nvidia building products around OpenClaw, the Foundation itself has also turned its attention to making the project more suitable for large organizations. 

 Claw courts the enterprise 

 The growing corporate involvement comes as OpenClaw itself makes a concerted push into the enterprise. In September, the Foundation launched OpenClaw Enterprise , an open source , self-hostable, vendor-neutral platform designed to give companies a central way to deploy, govern and isolate persistent agents. 

 The project remains “pre-1.0,” and is currently intended for internal pilots, but its remit is clear: give IT teams control over who can deploy agents, what those agents can access, and how their activity is audited. The OpenClaw Control Plane adds multi-tenancy, permissions and security boundaries while letting companies choose their own models, harnesses and infrastructure. 

 Part of that work has also involved reducing what gets installed by default. OpenClaw moved integrations including Slack, WhatsApp, Matrix and Amazon Bedrock out of its core dependency path, meaning their dependencies only arrive when those capabilities are actually installed. 

 “We’ve carved out the code into plugins,” Koc says. “If you’re not using something, it doesn’t get installed.” 

 The Foundation has also worked with technology companies on scanning and auditing OpenClaw skills . In June, Koc and researchers from OpenClaw and Nvidia published a study covering tens of thousands of public skill versions, comparing results from VirusTotal, OpenClaw’s own static analysis and Nvidia’s SkillSpector. 

 The three approaches frequently identified different risks. Just 0.69% of skills were flagged by all three, while 81.9% of those flagged were picked up by only one. OpenClaw subsequently combined those signals through ClawScan , alongside provenance, metadata and moderation history, and released the underlying dataset for outside researchers. 

 “There’s not one way to make everything absolutely safe and secure,” Koc said. “Security is going to be this evolving thing — there’s no one-size-fits-all.” 

 Koc also says that this kind of work is beginning to change the conversation with large organizations. He compared the initial response to OpenClaw with the early corporate reaction to ChatGPT and Claude, when security concerns prompted some companies to pull the plug. 

 “Everyone in enterprise were like, ‘shut it down. This is dangerous,’” Koc says. “I feel like there’s an element of that here now.” 

 But, he suggests, that response is easing as companies better understand how OpenClaw works and the security risks involved. He also says that it is being used by Fortune 100 companies, other large enterprises and governments, including across teams and projects and, in some cases, with individual employees running their own instances. 

 Larger deployments also raise a new set of questions. If employees eventually have separate personal and work agents, for example, OpenClaw will have to determine how those agents communicate, what information they can share, and how they coordinate things such as calendars without crossing organizational boundaries. 

 “What I personally don’t want to see is this world where we have all these different agents and none of them can collaborate or work together.” 

 More broadly, Koc is thinking about what happens as more companies build agents of their own. 

 “What I personally don’t want to see is this world where we have all these different agents and none of them can collaborate or work together, and it becomes like you have to buy into some ecosystem to make things work,” Koc says. 

 What’s next for OpenClaw 

 Released at the end of August, much of OpenClaw 2.0 was ultimately about removing friction . The release began as an effort to simplify installation and rebuild the browser experience, before expanding into a much broader overhaul spanning memory, skills, native apps, plugins, security and other parts of the project. 

 That push has continued since. OpenClaw has introduced simpler native installers and onboarding, with Koc saying the goal is eventually to get as close as possible to a click-and-go experience — install OpenClaw, configure it, set up a local model where appropriate, and have it ready to use without requiring people to spend time configuring servers or dependencies. 

 Koc himself is also willing to push OpenClaw further in his own life than many users might be comfortable with. In some instances, he gives it access to his email, phone, computer and other personal data, acknowledging that doing so carries some risk but arguing that he needs to experience this himself if he is helping build the product. 

 “I know there’s some risk attached to that, but I feel like if I’m working on the edge and creating a product like this, I need to embrace the unknown a little bit more than everyone else,” Koc says. “There needs to be an element of me dogfooding this and understanding how it works.” 

 All of this raises an obvious question, particularly given the comparison with Meta’s personal AI agent: does this all ultimately lead to OpenClaw ultimately becoming the same kind of polished consumer product? 

 “Probably not in the vein of Muse, but we are looking at how we simplify the experience as much as possible,” Koc says. “As much as an open source project can, one that doesn’t want to handle infrastructure, and still let you run it the way you want to run it.” 

 So while there are clear similarities between OpenClaw and products such as Muse, they are ultimately different propositions. Meta can manage the underlying infrastructure and hide much of the complexity from the user; OpenClaw is trying to make things easier while preserving the ability to choose where it runs, which models it uses and how much control the user retains. 

 Beyond ease of use, multiplayer is also emerging as another significant part of what comes next. OpenClaw Multiplayer lets multiple people work with and steer the same agent while retaining the same context, an idea that grew out of the Foundation’s own experiments with shared agent sessions. It says around 50 people at the Foundation are already using the same shared environment. 

 “We’re trying to reinvent how we work as a team and improve the way we work with agents, and then whatever that ends up becoming is what we end up shipping to the community,” Koc says. 

 As for what OpenClaw 3.0 might look like, Koc says the team is still working that out. But the same principle appears likely to shape it: its direction, he suggests, will be determined largely by the problems OpenClaw’s own developers encounter while using the project. 

 “Whatever’s slowing us down, whatever’s making it harder for us to build OpenClaw, that is what we’re going to solve next, and we’re going to give that back to the community,” Koc says. 
 The post OpenClaw at one: its chief architect on a year of explosive growth, wooing the enterprise, and being Meta’s muse appeared first on The New Stack .
