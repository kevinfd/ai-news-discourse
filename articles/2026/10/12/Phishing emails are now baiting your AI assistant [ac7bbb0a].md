---
id: "ac7bbb0a0ac1770d"
title: "Phishing emails are now baiting your AI assistant"
url: "https://malwarebytes.com/blog/ai/2026/10/phishing-emails-are-baiting-your-ai-assistant"
source: "Malwarebytes"
domain: "malwarebytes.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-12T19:35:02Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Apollo_R"]
language: "en"
summary: "You ignored the suspicious email. You didn’t open the attachment, click the link, or reply to the sender.\nThen you asked your AI assistant to summarize your inbox.\nCould the message you wisely avoided find its way back onto your to-do list—only this time presented as an urgent recommendation from a tool you trust?\nThat’s the risk behind phishing emails containing hidden instructions aimed at AI…"
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 762
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50061773"
score: 11
comments: 0
community: "Hacker News"
---

# Phishing emails are now baiting your AI assistant

Malwarebytes · Apollo_R · 2026-10-12

You ignored the suspicious email. You didn’t open the attachment, click the link, or reply to the sender.
Then you asked your AI assistant to summarize your inbox.
Could the message you wisely avoided find its way back onto your to-do list—only this time presented as an urgent recommendation from a tool you trust?
That’s the risk behind phishing emails containing hidden instructions aimed at AI assistants. Instead of relying only on persuading you, attackers are also trying to influence the software that reads your messages. Recent research from Barracuda describes emails designed to target both audiences at once.
For the human recipient, there was a password-protected attachment, with the password supplied in the email. For an AI assistant processing the message, there were hidden instructions intended to influence how it summarized or handled the content.
By including a prompt injection, attackers give themselves another way to reach you. The malicious instructions could try to make the assistant describe the email as legitimate or urgent, encouraging you to revisit it.
In another example, a hidden block instructed a summarizing AI to add a fake priority action: Change a vendor’s payment details. That could result in an employee sending money to an attacker’s account.
The attacker isn’t simply asking the AI to repeat a fraudulent request. They’re trying to turn that request into the assistant’s recommendation.
How prompt injection works
Prompt injection means planting instructions in material an AI system is supposed to read, hoping it will follow those instructions instead of treating them as part of the material. When the instructions arrive through an outside source, such as an email or webpage, it’s often called indirect prompt injection.
The malicious instructions don’t have to appear as ordinary, readable paragraphs. Barracuda identified concealment techniques including comments in the email’s underlying HTML code, text made invisible through styling, encoded content, and invisible “zero-width” characters. These can obscure instructions from a person viewing the message while leaving content available for an AI system to process. Whether that content actually reaches the model depends on how the particular tool extracts and prepares the email.
That means this problem cannot be solved simply by asking people to look more carefully at their emails. Part of the defense must sit inside the tools handling those messages.
Apollo Raines, developer of the AI code review service ShipItClean, explains:
“The real flaw is that the model can’t tell the difference between text it’s supposed to read and instructions it’s supposed to follow. Stripping hidden content before it reaches the model is worth doing, and every vendor should do it. But it’s an arms race. Each new encoding trick is a new hole.”
He adds:
“People have learned to distrust the email. They haven’t learned to distrust their AI assistant. So, the defense has to live inside the tools. I’d go one step further: some of it has to live inside the model itself. Wrappers, filters, sandboxing and human sign-off on payments are all necessary.”
Before taking action
An assistant that summarizes messages could mislead you about which email deserves attention or what action it requires.
An assistant with additional permissions could create a more serious problem. Depending on its capabilities and safeguards, malicious instructions might try to make it carry out unauthorized actions or disclose sensitive information.
You don’t need to abandon AI tools that help with email. But you do need to consider what you trust them to do and what permissions you give them.
The familiar phishing advice still applies. When an assistant reads your inbox on your behalf, check its recommendations before acting:
- Check the original message before acting on a recommendation involving money or sensitive information. If a summary tells you to pay an invoice, change account details, or share sensitive information, don’t treat the summary itself as verification.
- Always verify payment changes through a separate, established channel. Contact the person or organization using details you already trust, rather than relying on information supplied in the suspicious message.
- Keep your AI assistant’s permissions limited to what you need and, at work, what your organization allows. An assistant used to summarize emails should not need broad authority to carry out unrelated actions. Limiting access can reduce the consequences if it follows malicious instructions.
- Require human approval for high-impact actions like payments and changes to vendor payment details. Approval should include checking the underlying request, not simply accepting the assistant’s recommendation.
From reporting threats to removing them.
Cybersecurity risks should never spread beyond a headline. Keep threats off your devices by downloading Malwarebytes today.
