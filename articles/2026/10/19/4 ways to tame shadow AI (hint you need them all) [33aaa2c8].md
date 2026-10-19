---
id: "33aaa2c8a33b8469"
title: "4 ways to tame shadow AI (hint: you need them all)"
url: "https://computerworld.com/article/4229136/best-way-to-tame-shadow-ai-is-to-combine-tactics.html"
link: "https://computerworld.com/article/4229136/best-way-to-tame-shadow-ai-is-to-combine-tactics.html"
source: "Computerworld"
domain: "computerworld.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-19T04:58:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Maria Korolov"]
language: "en"
summary: "Unsanctioned AI use is epidemic, and agentic AI expands the risk. Here are four proven tactics that work better together."
tags: []
orgs: ["Anthropic", "DeepSeek", "OpenAI", "Google", "China", "xAI"]
topics: ["agents & coding", "safety & ethics", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 1887
paywalled: false
image: "http://www.bing.com/th?id=ONUT.DbhiYSBrtjNHOTwZXeUFOQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# 4 ways to tame shadow AI (hint: you need them all)

Computerworld · Maria Korolov · 2026-10-19

Unsanctioned AI use is epidemic, and agentic AI expands the risk. Here are four proven tactics that work better together.
In olden days — last year, say — employees using unsanctioned AI tools might copy-and-paste sensitive data that could end up in the AI company’s training data set.
Today, an unsanctioned AI can hack into another company for an employee even if they didn’t explicitly ask it to.
This doesn’t just mean the latest unreleased frontier models undergoing security testing. Claude, ChatGPT, and Gemini have all evolved from being mere chatbots, answering questions and helping people write emails. They now have agentic capabilities and are able to carry out complex tasks on behalf of users.
And they do, sometimes to dangerous effect.
In August, ABC News in Australia interviewed a man identified only as “Andrew” who asked an AI agent to sign him up for a gym class. The agent hacked into the gym’s system and deleted someone else’s wait list reservation.
The AI was Anthropic’s Claude, and the agentic framework was OpenClaw.
Now imagine an employee asking their agentic AI assistant to help them make a sale. The request might inadvertently inspire the agent to hack into the prospect’s company.
To keep this — and other worst-case scenarios — from taking place, enterprises are building guardrails around their AI systems, restricting what data the AI has access to and what tools it’s allowed to use.
But none of those guardrails will work if the employee uses a tool that their company doesn’t know about.
“This is a problem we’ve long had,” says Matt Butkovic, technical director for cyber risk and resilience in the CERT division at Carnegie Mellon University’s Software Engineering Institute. “People will find ways to purchase or get access to things they think are useful, even when an organization says you probably shouldn’t do that.”
Ten years ago it was personal email and unauthorized cloud storage.
“The stakes are higher in some ways now,” adds Butkovic, who also teaches in CMU’s CISO program.
Verizon’s 2026 Data Breach Investigations report, released in May, shows that 67% of employees access AI services through non-corporate accounts on corporate devices. Shadow AI was the third most common non-malicious insider action detected in Verizon’s 2025 data loss prevention dataset.
And a May analysis of 1.9 million AI session minutes conducted by Harmonic Security found that when employees accessed personal accounts, 65% of their activity was related to business. They used personal accounts to write work emails and debug code, and even used it for legal work.
In a separate report, released in July, Harmonic reported that every organization the company monitored in the first half of 2026 had at least one employee sending data to a China-based AI tool. The uploaded data included M&A plans, source code, financial projections, and legal material.
To address this problem, enterprises are taking a fourfold approach:
- Figure out what employees want to use AI for and give them sanctioned, safe alternatives.
- Use security tools to monitor activity and keep employees from sharing sensitive data with unsafe systems, or even accessing them at all.
- Educate employees on the risks of AI and how to use it safely, because you can’t solve this problem with technology alone.
- Hold employees accountable when they violate AI policies.
Blocking DeepSeek at a financial services firm
BitGo, a Fortune 500 financial services firm with over $100 billion in digital assets under custody, uses a combination of strategies to combat unsanctioned AI.
“We have enterprise versions of Grok, ChatGPT, Claude and Gemini,” says Manny Khan, the company’s deputy CISO. “We are an AI-first organization. We encourage all of our people to use AI in their work, to try to automate as much of it as possible while keeping the human in the loop to avoid any slop.”
Unsanctioned AI is an industry-wide concern, he says, and having a sanctioned alternative is key.
“We encourage folks to use what is approved and has guardrails and harnesses and trust boundaries and safety checks,” he says.
To make the sanctioned alternatives easier and more appealing, employees use single sign-on, provided by Okta, to log into systems, and the enterprise-grade models also connect to the company’s MCP servers.
Once employees have a safe AI option to use, the next step is to get a handle on the unsafe ones.
For example, BitGo uses a data loss prevention tool from Cyberhaven. DLP was a useful security tool long before AI came along, but today it also helps ensure that sensitive data isn’t copied-and-pasted into untrusted chatbots.
“All traffic is proxied and analyzed by our security tools to identify anything potentially malicious, shut it down, and not allow the connection if it’s a site known to be malicious,” Khan says.
For example, the company blocks DeepSeek, a Chinese AI model. “We don’t want their models to train on our data,” Khan says.
But there’s only so much technology can do.
“Every site has AI now, and we cannot block every single site,” Khan says. “We might as well block the internet at that point.”
That’s where human awareness and education come in, says Khan.
“We do train people,” he says. “And we have an AI governance policy that we share company-wide and enforce this policy by tracking and measuring against it.”
It’s important for a company to have a single voice on AI use, a central figure with authority and ownership who can provide guidance, he adds. “Otherwise, you’ve got a lot of people who try to figure it out on their own. And that’s what you don’t want.”
Docusign on guard against agentic AI
“We want to educate users to do the right things, but people still want to experiment,” says Shivi Verma, senior manager of engineering at electronic signature firm Docusign.
That’s where it helps to have approved, secure tools for people to use, as well as systems in place to block the insecure ones.
“Some of the websites, like DeepSeek, we have blocked,” he says. “But we want to block in a way that focuses on education and focuses people on the right processes and tooling, which will drive people automatically to use approved tools.”
The company is also working on creating an allow list, he says, focusing on tools that employees can use without any concern.
And the company has network management tools like Zscaler, says Verma. “If people are posting confidential data in an external tool, it will give a popup, like a deterrent.”
Now, personal AI agents like OpenClaw are yet another evolution of the shadow AI problem, he says.
“We do monitor and people are using it, but we want to do it in a way that’s under security policies,” he says.
And with OpenClaw in particular, the danger is too high for just a warning.
“If it’s for personal use, that’s one thing,” Verma says. “But if you’re using it at work, your user has to be stopped immediately.”
Nonprofit builds routing system for approved AI
“Simply blocking AI tools is not a sustainable solution,” says Boris Kolev, global head of technology at JA Worldwide, a global educational nonprofit with almost 5,000 employees that serves more than 20 million people a year.
For JA Worldwide in particular, the problem was exacerbated by the fact that there was no approved solution until three months ago. As a result, employees got into the habit of using personal AI platforms.
“It was totally uncontrolled,” Kolev says. “Everyone who wanted to explore AI was using public models.”
At the beginning, people didn’t worry about what they shared and uploaded. “We tried to implement some policies, like ‘don’t upload corporate information.’ But it was hard to know what people were doing.”
Plus, AI was being embedded everywhere. On Windows. In people’s phones. “A user cannot avoid it,” says Kolev.
Then, earlier this year, the organization built a routing system, with enterprise-safe versions of Claude and ChatGPT running in private environments on AWS and Azure, in addition to some open-source models.
“Our colleagues can choose which model to use,” he says. “And sometimes they do a prompt two different times and choose which one works better.”
The system went into production in June, after a couple of months of testing and development.
“Now, after all the policies and rules are implemented, we have our own closed AI system, hosted on our own servers, so no risk of leaking corporate data,” he says. “But still, some projects are using public models, and we are trying to solve this problem.”
Another hitch: individual employees were often invested in the personal AI tools they’d grown comfortable with and reluctant to change to the corporate tools.
“Employees were saying, ‘I have so much history. It knows me, I cannot just switch,'” Kolev says.
And employees still have all the AI tools that come with their devices.
“This is hard to manage, and it’s getting even harder,” he says. There are monitoring and blocking tools available, but they’re too expensive. “We’re a nonprofit, and for us it’s almost impossible to afford monitoring tools. So we do a lot of educational sessions.”
The organization is also trying to make the sanctioned tools more appealing. That includes a mechanism to import the history and context from other platforms, he says. “And we’re trying to convince them that our tool works better and has more functionality, so we’re adding MCPs.”
MCP — model context protocol — allows an AI system to access data and tools directly. That includes connecting to corporate email and calendars, SharePoint, Monday.com, CRM, and all the other software that employees use for work, he says.
Kolev says that it’s a mistake to assume that employees use shadow AI because they don’t respect IT policies. It’s because IT didn’t move quickly enough to meet their needs.
“They find the AI faster than you can produce tools and governance and rules,” he says. “So my advice is that you start with simple rules that employees can understand, provide sanctioned tools, and continuously adapt governance.”
Holding employees accountable
According to an April survey of more than 1,200 employees conducted by Wakefield Research on behalf of PagerDuty, 66% of employees have used unsanctioned AI tools — and of those, 48% faced formal consequences, such as a warning or disciplinary action.
Holding people accountable is critical to a successful AI use policy, says Carnegie Mellon’s Butkovic. “We have to speak definitely about this in organizations,” he says. “If this behavior cannot be tolerated, then it shouldn’t be tolerated.”
Allowing the use of unsanctioned AI doesn’t just create risks but also opens up an organization to legal liability if the AI agents, acting on behalf of employees, harmed other companies or individuals.
“There could be consequential actions,” he says. Even if the employee responsible gets fired, “external parties that have been affected are still going to sue the company.”
The organization needs to be able to show that it has policies in place and enforces them when employees deliberately circumvent the policies.
“If you as an employee make a good-faith effort to comply with the policy, we’ll show you latitude if you’re not malicious,” Butkovic says. “But if you’re actively circumventing the system of controls in your organizations, that’s the case where there have to be swift and profound consequences.”
