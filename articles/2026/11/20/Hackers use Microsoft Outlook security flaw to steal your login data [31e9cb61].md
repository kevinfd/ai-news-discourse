---
id: "31e9cb61b178ad61"
title: "Hackers use Microsoft Outlook security flaw to steal your login data"
url: "https://foxnews.com/tech/hackers-use-microsoft-outlook-security-flaw-steal-login-data"
link: "https://foxnews.com/tech/hackers-use-microsoft-outlook-security-flaw-steal-login-data"
source: "Fox News"
domain: "foxnews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-20T14:09:17Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Kurt Knutsson", "CyberGuy Report"]
language: "en"
summary: "You probably know better than to enter your password on a suspicious website. But what if hackers could steal information tied to your Windows login without ever asking for your password? That's the concern behind a Microsoft Outlook security flaw that hackers are already exploiting. Attackers can trick someone into opening a malicious Outlook file that quietly exposes Windows authentication…"
tags: ["3b917b46-878d-5432-87f9-a2eead011a53", "fnc", "Fox News", "fox-news/tech/companies/microsoft", "fox-news/tech/topics/cybercrime", "fox-news/tech/topics/hackers", "fox-news/tech/topics/security", "fox-news/tech/technologies/windows-os", "fox-news/tech/technologies/email", "fox-news/tech", "article"]
orgs: ["Microsoft"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 2106
paywalled: false
image: "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/11/931/524/microsoft-outlook-email-client.jpg?ve=1&tl=1"
discussion_url: null
score: null
comments: null
community: null
---

# Hackers use Microsoft Outlook security flaw to steal your login data

Fox News · Kurt Knutsson, CyberGuy Report · 2026-11-20

You probably know better than to enter your password on a suspicious website. But what if hackers could steal information tied to your Windows login without ever asking for your password? That's the concern behind a Microsoft Outlook security flaw that hackers are already exploiting. Attackers can trick someone into opening a malicious Outlook file that quietly exposes Windows authentication information. That information could help a criminal impersonate you and potentially gain access to systems you use.
Microsoft released a fix on Nov. 10. However, the company confirms hackers were exploiting the vulnerability before the update became available. If you use Outlook for work, this is one security update you should check right away.
Missed CyberGuy LIVE? Watch the replay and discover 5 ways to travel smarter and save money.
Our free CyberGuy LIVE class, 5 Ways to Travel Smarter and Save Money, has ended, but you can still watch the full replay. Kurt "CyberGuy" Knutsson walks you through five practical ways to protect your phone and personal information, avoid common travel scams, find better deals, save money on bookings and use technology to make your travels easier and less stressful. No technical experience is needed.
Watch the free replay + downloadable checklist now at CyberGuyLive.com.
FAKE AI EVENT INVITES TARGET MICROSOFT AND GOOGLE LOGINS
How hackers exploit the Microsoft Outlook security flaw
The vulnerability, tracked as CVE-2026-124194, involves how Outlook handles specially crafted message files. An attacker can create a malicious Outlook message file, such as one using the .msg format. The hacker then needs to convince someone to open that file in an affected version of Outlook. Once opened, the malicious file can cause Outlook to connect to a server controlled by the attacker. That connection happens without the usual warning about accessing external content. During the connection, Windows can reveal NTLMv2 authentication information. This data helps Windows verify your identity when connecting to certain network services.
The information differs from your actual password. However, hackers may be able to use it in a follow-up attack to impersonate you. For someone using Outlook at work, that could potentially expose company resources their account can access. The outcome depends on the network's security protections and whether the attacker can successfully misuse the authentication information. Here's what makes this especially concerning. The attack doesn't require you to type your password into a fake login page. Opening the malicious file can be enough if your computer can connect to the attacker's network location. Microsoft says simply viewing the message through Outlook's Preview Pane does not trigger this particular vulnerability. Someone must open the malicious file for the attack to work.
Microsoft confirms hackers are already exploiting the flaw
Microsoft included the Outlook fix in its November Patch Tuesday security updates. The company's core release addressed 1,093 vulnerabilities, including 63 rated critical. Interestingly, Microsoft classified this particular Outlook vulnerability as moderate, giving it a CVSS severity score of 6.5 out of 10. However, that rating tells only part of the story. Microsoft confirms attackers have already exploited the flaw. The Cybersecurity and Infrastructure Security Agency (CISA) also added it to its Known Exploited Vulnerabilities catalog on Nov. 10. In other words, hackers are already taking advantage of this security weakness. Microsoft has not publicly identified who carried out the attacks or disclosed how many people were affected. The company also hasn't provided detailed information about the incidents. With hackers already exploiting the flaw, it's important to install the security update as soon as possible.
FAKE CHATGPT BILLING EMAILS CAN STEAL YOUR LOGIN
Who is affected by the Outlook security vulnerability?
According to Microsoft's security advisory, the affected products include:
- Microsoft 365 Apps for Enterprise: Affected versions of Outlook included with enterprise subscriptions.
- Microsoft Office LTSC 2021: Affected installations of Microsoft's long-term servicing edition.
- Microsoft Office LTSC 2024: Affected installations of the newer long-term servicing edition.
The vulnerability concerns affected desktop Office installations on Windows computers. Microsoft's advisory does not list Outlook.com in a web browser or the Outlook mobile apps as affected products. If your employer manages your Microsoft 365 software, your IT department may handle these updates. However, it's worth confirming that the security fix has been installed. For people who manage their own computers, here's how to check.
How to protect yourself from the Outlook security flaw
The most important thing you can do is update Microsoft Office. However, a few additional precautions can help reduce your exposure to suspicious files and account attacks.
1) Update Microsoft Office immediately
Microsoft has released security updates addressing the vulnerability. You can manually check for updates in supported Windows versions of Office.
- Open Microsoft Word or another installed Office application and create or open a document.
- Click File and select Account. In classic Outlook, the option may appear as Office Account.
- Under Product Information, select Update Options.
- Click Update Now and allow Microsoft to check for available updates.
- If prompted, save your work and allow Office to close any open applications, so the updates can finish installing.
- Wait for the "You're up to date!" or "Updates were installed" confirmation.
If you don't see Update Now, you may need to select Enable Updates first. If the entire Update Options menu is missing, your employer may manage updates centrally. Contact your IT department rather than assuming the software has already been patched. You can also review Microsoft's official Office update instructions.
2) Confirm your Microsoft Office version
After installing the update, you can check which version of Office is running on your computer.
- Open Microsoft Word or another installed Office application.
- Click File and select Account.
- Look under Product Information for the version and build information.
- Select About Word if you need to see the complete build number.
For affected volume-licensed installations, Microsoft's November 10 security release includes these updated builds:
- Office LTSC 2021: Build 14334.21048
- Office LTSC 2024: Build 17932.21140
These build numbers apply to the specified LTSC editions. They shouldn't be used to check other Office versions. If you're using Microsoft 365 Apps for Enterprise, the correct build depends on your organization's update channel. You can check Microsoft's Office security release notes or contact your IT department to confirm the fix.
3) Check for Windows security updates
Although this vulnerability requires an Office fix, keeping Windows updated remains important.
On Windows 11:
- Open Settings.
- Click Windows Update.
- Select Check for updates.
- Install available security updates.
- Restart your computer if prompted.
Next, check whether Windows can receive updates for other Microsoft products.
- From Windows Update, click Advanced options.
- Find Receive updates for other Microsoft products.
- Turn the setting On if available.
This can help Windows deliver updates for supported Microsoft products. However, some Office installations receive updates through separate services or employer-managed systems. Remember that checking Windows Update alone may not confirm you've installed the specific Outlook fix. Check Office separately. It's also smart to back up important files before installing major operating system updates.
4) Be suspicious of unexpected Outlook attachments
A message file from an unfamiliar sender deserves extra caution, especially if you weren't expecting it. Watch for attachments ending in .msg, a common file format for saved Outlook messages. The format itself is legitimate. However, attackers can abuse it to deliver this exploit. If an email claims you need to open an attached message to review an invoice or urgent workplace request, verify it through another trusted channel. Even attachments appearing to come from coworkers deserve a second look when the request seems unusual.
5) Report suspicious emails in Outlook
If something looks suspicious, avoid opening the attachment. Instead, report the message using Outlook's built-in reporting tools when available.
In supported versions of Outlook:
- Select the suspicious email in your inbox without opening its attachment.
- Look for Report or Report phishing in the toolbar.
- Choose Report phishing if that option appears.
- Follow the prompts to submit the report.
The exact menu location depends on your Outlook version and your employer's settings. If you're using a work account and don't see a reporting option, contact your IT department. Avoid forwarding the suspicious attachment to other coworkers.
6) Use strong antivirus protection
Strong antivirus software can help identify suspicious attachments and malicious activity before they cause further damage. Look for protection that includes real-time scanning and behavior-based detection. These features may help catch threats that traditional virus signatures miss. However, antivirus software cannot replace Microsoft's security patch. Installing the Outlook update remains essential for closing this particular vulnerability. Get my picks for the best 2026 antivirus protection winners for your Windows, Mac, Android and iOS devices at CyberGuy.com.
7) Turn on multifactor authentication
Multifactor authentication (MFA) adds another layer of account protection by requiring additional verification when you sign in. Enable it on your Microsoft account and other important services whenever available. Keep in mind that MFA may not stop attacks involving stolen Windows authentication information. That's another reason updating Outlook takes priority.
Know what to do if you opened a suspicious file
If you recently opened an unexpected Outlook message attachment, don't assume everything is fine because nothing unusual appeared on your screen. Here's what to do next.
- Close the suspicious file: Stop interacting with the attachment. Don't reopen it or forward it to anyone else.
- Notify your IT department if it's a work computer: Report what happened right away. Your security team can investigate suspicious authentication activity and determine whether additional action is needed.
- Update Microsoft Office: Install the latest security updates to protect against further attempts to exploit the Outlook vulnerability.
- Run a security scan: Use your antivirus software to check for other suspicious activity or malware. Keep in mind that a clean scan cannot rule out stolen authentication information.
- Check your account activity: Review your Microsoft account for unfamiliar sign-ins or unexpected security changes. However, normal sign-in activity doesn't guarantee your authentication information wasn't exposed.
- Secure your personal accounts: If you suspect unauthorized access, change your password using a trusted device. Make sure multifactor authentication is enabled wherever available.
One important reminder: Changing your password alone may not address every potential exposure from this vulnerability. If you opened the attachment on a work computer, let your IT team determine whether additional security measures are necessary.
Why Microsoft's latest security update deserves attention
Microsoft's November security release covers far more than Outlook. It also fixes weaknesses that could allow attackers to gain additional privileges or remotely execute malicious code. For those of you using a Windows PC every day, the sheer number of vulnerabilities may sound overwhelming. However, not every flaw carries the same immediate risk. In this case, the Outlook weakness deserves your attention because Microsoft has confirmed active exploitation.
The larger concern is how easily a malicious file can take advantage of trusted software. Outlook is part of everyday communication for countless businesses, and opening saved email messages may seem harmless. This vulnerability shows why keeping Office updated deserves the same attention as updating Windows.
Kurt's key takeaways
What concerns me about this Outlook flaw is how little someone has to do to put their information at risk. You could receive what looks like a routine work attachment, open it and unknowingly expose information that helps a hacker impersonate you. There's no obvious warning telling you something went wrong. And by the time you realize it, the damage may already be done. I also find it troubling that Microsoft rated this vulnerability moderate even though attackers were already exploiting it. Most people aren't going to spend their day reviewing security ratings, and they shouldn't have to. They need software that protects them and updates that are easy to install. My advice is simple. If you use Outlook on a Windows computer, check for Office updates today. Don't assume your computer has already taken care of it.
Should Microsoft be doing more to prevent a single malicious Outlook file from exposing your login information, or do you think keeping your software updated is enough protection? Let us know by writing to us at CyberGuy.com.
Sign up for my FREE CyberGuy Newsletter
- Get my best tech tips, urgent security alerts and exclusive deals delivered straight to your inbox.
- For simple, real-world ways to spot scams early and stay protected, visit CyberGuy.com – trusted by millions who watch CyberGuy on TV daily.
- Plus, you'll get instant access to my Ultimate Scam Survival Guide free when you join.
CLICK HERE TO DOWNLOAD THE FOX NEWS APP
Copyright 2026 CyberGuy.com. All rights reserved.
