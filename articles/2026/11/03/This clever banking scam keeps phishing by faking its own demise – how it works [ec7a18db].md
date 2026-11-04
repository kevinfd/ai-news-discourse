---
id: "ec7a18db18106426"
title: "This clever banking scam keeps phishing by faking its own demise – how it works"
url: "https://zdnet.com/tech/bank-phishing-scam-kela"
link: "https://zdnet.com/tech/bank-phishing-scam-kela"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T14:15:36Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Charlie Osborne"]
language: "en"
summary: "You won’t see the ‘suspended’ sign because it’s not meant for you."
tags: ["Security"]
orgs: ["Google", "Meta", "UK"]
topics: ["policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 872
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-2210544722.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# This clever banking scam keeps phishing by faking its own demise – how it works

ZDNet · Charlie Osborne · 2026-11-03

ZDNET’s key takeaways
- Fake banking websites are faking their own suspensions to fly under the radar
- While scanners see a takedown notice, victims don’t.
- Hundreds of fake domains are still active.
KELA researchers have exposed an active financial-scam infrastructure that hosts hundreds of fraudulent websites capable of faking their own suspensions to stay online. As of Oct. 25, 2026, 248 financial scam and phishing domains tied to 189 major US banks and financial services have been linked to the same infrastructure.
According to the cybersecurity firm’s report, published on Tuesday, the “Suspended” infrastructure operation runs websites that have cloned the official domains of victim organizations, with a particular focus on business banking. Many domains use the [keyword]-[bank].com format, slotting in keywords such as “secure,” “disable,” “protect,” and “cancel.”
Also: Beware of Bluetooth sniffers: How your favorite gadgets could be exposing your data
More from ZDNET
Why is this financial phishing campaign different?
This phishing campaign stands out because of how the cybercriminals behind the scam are protecting it: by issuing takedown notices.
When you visit a website and see a message that it has been taken down or suspended, it’s usually because the domain has been associated with malicious or illegal activity, including phishing and scams. Law enforcement agencies, often with help from technology firms, find these websites, obtain the necessary court orders, and seize the infrastructure or accounts behind them to force a suspension through a registrar or hosting provider.
You see the notice, you move on — and this also goes for scanners and security teams.
However, in this case, the scam artists created a mechanism to show it themselves, to avoid being flagged and taken down. But it’s when they show it that matters.
How the false phishing flag works
The false suspension notice appears deceptively simple at first glance. A phishing kit embedded in the domain registers the IP address of each visitor, and on their second visit, they are shown a fake “account suspended” page. The kit is disguised as a challenge page similar to those legitimately used by Cloudflare.
Researchers also detected other decoys, including “Sorry, you’ve been blocked” notices, blank pages, and redirections to Google. Some pages also have reCAPTCHAs, and the researchers detected scripts that block browser developer tools, likely to slow analysis.
Also: Don’t use Muse? Meta’s AI agent can still access your private messages – here’s how
But why show fake suspension notices in the first place? To scanners and cybersecurity teams, it looks like someone else has already dealt with the malicious domain, and they can move on to the next suspicious website.
“That design targets exactly the people who could shut a site down,” KELA says. “A victim typically follows a link once. A scanner, a security team or a takedown provider checks a reported site and then checks it again to confirm, and the second check shows what looks like a completed takedown.”
As shown in the image below, while scanners would detect a suspension notice, victims would still see the cloned website, complete with lures to entice them into entering their information, leading to financial fraud and potentially identity theft. After all, one visit is enough.
How widespread is this phishing campaign?
As of this writing, there are 248 live domains, plus those taken offline after the researchers disclosed their findings to law enforcement; over 300 scam domains have been hosted on the same infrastructure since May this year. Unfortunately, this phishing campaign remains active, with new domains appearing every day.
One lead could reveal the operator: a remote desktop connection to the malicious infrastructure through a standard UK home broadband connection, but it has not been verified.
How do you detect fake banking websites?
Use a phishing link checker to verify whether a URL is trustworthy, and remember that any email or message claiming to be from your bank may be fraudulent.
Typical signs of a bank phishing email include:
- Unusual email addresses: This is a clear giveaway that the message has come from a fraudulent domain. Watch out for small typographical errors and domains you don’t recognize.
- Poor formatting: Spelling errors, poorly written messages, vague and generic content missing specifics — all of these can point to a phishing email. Logos may be copy-pasted into message bodies to make them more convincing, but don’t fall for it.
- Emotive content: Phishing emails succeed most often when they create an emotional reaction, including panic. If an email lands in your inbox demanding payment, late fees, or threatening legal action for problems you weren’t aware of, take a moment to breathe before responding. If you need to verify that a message is legitimate, ring up your bank directly — and don’t use any phone numbers contained in the email, as they may send you to a scam call center.
- Suspicious links and attachments: Malicious links and attachments are often found in the cybercriminal playbook. Links may send you to phishing domains, whereas attachments may contain malware that infects your PC. Be wary of both.
When it comes to organizations, KELA has released a free Bank Phishing Check tool that compares official domains and organizations against the websites uncovered during the firm’s research.
