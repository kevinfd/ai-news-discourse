---
id: "5e77f6da5f9012e2"
title: "Fake AI event invites target Microsoft and Google logins"
url: "https://foxnews.com/tech/fake-ai-event-invites-target-microsoft-google-logins"
link: "https://foxnews.com/tech/fake-ai-event-invites-target-microsoft-google-logins"
source: "Fox News"
domain: "foxnews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-15T15:51:15Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Kurt Knutsson", "CyberGuy Report"]
language: "en"
summary: "An invitation to an exclusive OpenAI event lands in your inbox. It promises a look at the latest AI tools and even offers three months of ChatGPT Pro for free. All you have to do is register using your work account. Sounds like a pretty good deal, right? Well, before you click that registration button, there's something you should know. Cybercriminals are using fake AI event invitations to trick…"
tags: ["f55ddc46-7a36-5d62-bc7d-c9dff7dd5ea3", "fnc", "Fox News", "fox-news/tech/topics/cybercrime", "fox-news/tech/topics/security", "fox-news/tech/topics/hackers", "fox-news/tech/artificial-intelligence", "fox-news/tech/companies/microsoft", "fox-news/tech/companies/google", "fox-news/tech", "article"]
orgs: ["Microsoft", "OpenAI", "Google", "Anthropic", "Amazon", "xAI"]
topics: ["business & funding", "search & media"]
content_source: "fulltext"
word_count: 2427
paywalled: false
image: "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/03/931/523/tech-giants-anti-scam-accord-1.jpg?ve=1&tl=1"
discussion_url: null
score: null
comments: null
community: null
---

# Fake AI event invites target Microsoft and Google logins

Fox News · Kurt Knutsson, CyberGuy Report · 2026-11-15

An invitation to an exclusive OpenAI event lands in your inbox. It promises a look at the latest AI tools and even offers three months of ChatGPT Pro for free. All you have to do is register using your work account. Sounds like a pretty good deal, right? Well, before you click that registration button, there's something you should know. Cybercriminals are using fake AI event invitations to trick employees into giving them access to their Microsoft and Google accounts. And some of these attacks can get past the extra security checks many of us rely on.
According to a new report from Push Security, attackers have created convincing event registration pages impersonating OpenAI, SpaceX and Anthropic. Push Security says it detected and blocked visits to the malicious event registration pages on its customers' browsers in late October 2026. The concerning part is how easily an invitation that appears legitimate can lead to someone handing over access to their work account. Here's what researchers discovered and how to protect yourself.
Missed CyberGuy LIVE? Watch the replay and discover 5 ways to travel smarter and save money.
Our free CyberGuy LIVE class, 5 Ways to Travel Smarter and Save Money, has ended, but you can still watch the full replay. Kurt "CyberGuy" Knutsson walks you through five practical ways to protect your phone and personal information, avoid common travel scams, find better deals, save money on bookings and use technology to make your travels easier and less stressful. No technical experience is needed.
Watch the free replay + downloadable checklist now at CyberGuyLive.com.
FAKE CHATGPT BILLING EMAILS CAN STEAL YOUR LOGIN
Fake AI event invites promise free access to premium tools
The attackers are taking advantage of the growing interest in artificial intelligence. After all, plenty of employees want to learn how AI can make their jobs easier. A free premium subscription could be enough to get someone's attention. The phishing pages discovered by Push Security promote events that appear to come from recognizable technology companies. One fake OpenAI event advertised a November 4 livestream called "ChatGPT for Social & Digital Marketing Teams." The registration page promised three months of ChatGPT Pro to participants. Another page promoted an invitation-only SpaceX briefing scheduled for November 12. Visitors could supposedly choose between three months of Grok Heavy or a "SpaceX share."
Researchers also identified a phishing page impersonating an Anthropic event at AWS re 2026. That page was no longer active when they investigated it. These pages impersonated legitimate technology companies, and the advertised rewards were part of the phishing scheme. Push Security did not suggest that OpenAI, SpaceX or Anthropic operated these fraudulent events. And here's where things get especially concerning. The fake websites tell visitors they must sign in using their corporate Microsoft or Google accounts to complete registration and claim the promised rewards. That request opens the door to the phishing attack.
How fake AI event invitations trick employees
The criminals have put considerable effort into making these invitations appear credible. Rather than sending people directly to an obvious phishing website, they use familiar online services to help disguise where the links lead. Push Security found that the campaign routed visitors through shortened links associated with Google and Zapier. Earlier related attacks also used legitimate Zoom event pages and GoTo Webinar's email infrastructure. As a result, someone checking an invitation might see a familiar service before reaching the malicious registration page. Researchers have not confirmed the initial delivery method for every invitation in the newer campaign.
Once someone reaches the suspicious site, another familiar feature appears. A Cloudflare security challenge asks visitors to confirm they are human. You have probably encountered similar checks while shopping or visiting legitimate websites. However, criminals can use them too. In this campaign, the challenge also made it harder for automated security scanners to examine the malicious pages. After completing the check, visitors arrive at what looks like a professional event registration website. They're presented with two familiar buttons: "Continue with Microsoft" and "Continue with Google." Depending on which button someone selects, the attackers launch a different method designed to capture access to that account.
How hackers target Microsoft accounts without a password
This is where the attack gets clever. If someone selects "Continue with Microsoft," the phishing website connects to a service called Kali365. It's a phishing-as-a-service platform that criminals can use to carry out account attacks. Kali365 generates a Microsoft device authentication code. The fake registration page then instructs the visitor to copy that code and enter it on Microsoft's legitimate sign-in website.
Now, here's why that can fool someone. Microsoft's device authentication process is real. You may have used something similar when connecting a streaming device to an account. However, the attacker started this authentication request. When the victim enters the supplied code and approves the sign-in, Microsoft can issue authentication tokens to the attacker's session.
Those tokens may provide access to Microsoft 365 resources without the attacker needing the account password. And the attack may continue from there. Push Security found that the campaign redirects Microsoft users to another phishing service called VoidProxy after the device code step. That second stage attempts to capture their password and authenticated session cookie. A successful compromise could expose company email or documents stored in Microsoft 365. Other connected workplace applications may also be at risk, depending on the permissions and access associated with the compromised account.
How the Google phishing attack steals login sessions
The Google option takes another approach. When visitors click "Continue with Google," the phishing page opens a pop-up that appears to contain Google's familiar sign-in screen. However, that login process runs through VoidProxy, which acts as an intermediary between the person signing in and Google's actual authentication service.
As someone enters their credentials, the phishing service can capture the information. It can also intercept certain multifactor authentication responses and steal session cookies. So, what exactly is a session cookie? Think of it as a digital pass that helps a website remember you've already signed in. Once your identity has been verified, that cookie can allow you to continue using your account without entering your password on every page.
If a criminal obtains a usable session cookie, they may be able to reuse that authenticated session and gain access without completing the usual login process again. That's why these attacks are particularly dangerous for people who believe that enabling multifactor authentication automatically protects them from every account takeover attempt. It's important to note that Push Security documented the malicious infrastructure and blocked visits to the phishing pages. Its report did not establish how many accounts, if any, were successfully compromised through this campaign.
HACKERS HIDE DANGEROUS FAKE AI DOWNLOADS BEHIND GOOGLE ADS
Why these fake AI event scams are difficult to spot
The attackers are combining two phishing services behind the same registration pages. Kali365 targets Microsoft's device authentication process, while VoidProxy targets authenticated login sessions. Meanwhile, the fake event websites borrow the appearance of familiar brands. The criminals can also change their websites and event themes as older pages get discovered. Researchers also discovered that the fraudulent registration pages could automatically display content in a visitor's language. That allowed the attackers to adapt the same phishing campaign for people in different regions without creating entirely new websites. Push Security identified two phishing kits used to create the fake event pages. The researchers call them ZoomMock and MSDRoot. They found evidence suggesting the same operators were responsible for both kits, although the connection was not conclusively established.
Researchers also found no evidence linking the developers of Kali365 and VoidProxy. Instead, they believe the attackers behind the event campaign are customers of both phishing services. The result is an attack that can appear credible at several points. A shortened link may use a recognized service. A security challenge can look legitimate. Even the Microsoft authentication page can be genuine. For employees who regularly attend virtual meetings or participate in industry webinars, that familiarity could make the scam harder to recognize.
In response to our request for comment, a Microsoft spokesperson said, "We take reports of malicious online activity seriously and continuously work to help protect our customers from evolving threats. Microsoft Defender includes detections to block the threats identified in the report."
We also reached out to Google, OpenAI, Anthropic and SpaceX for comment but did not receive responses before our deadline.
How to protect yourself from fake AI event phishing scams
A few careful habits can significantly reduce your chances of falling for these attacks. Here's how to protect yourself.
1) Verify event invitations before registering
If you receive an unexpected invitation from OpenAI, SpaceX or another technology company, take a moment to check whether the event actually exists. Open a new browser tab and visit the organization's official website yourself. Look for the event through its verified channels. If necessary, contact the organizer using information obtained independently of the invitation. Be especially careful when an unfamiliar event requests your corporate account credentials.
2) Be skeptical of free AI subscriptions and exclusive rewards
An invitation promising premium AI access may sound appealing, especially when the offer appears to come from a respected technology company. However, the promise of something valuable can encourage people to act before checking the details. If registration requires you to sign in with a work account to receive a reward, verify the offer independently before proceeding.
3) Never enter a Microsoft device code you didn't request
This is one of the most important lessons from the campaign. If a website asks you to copy a device authentication code and enter it on a Microsoft page, consider whether you initiated a legitimate device sign-in. If you were simply registering for a webinar, that unexpected device code request should raise concerns. Even a legitimate Microsoft authentication webpage can become part of a phishing attack when criminals trick you into approving their request. Pay attention to any Microsoft sign-in prompt asking you to approve access. Even if the website address is legitimate, you could be authorizing a session started by a criminal.
THE BEST DEFENSE AGAINST HIGH-TECH AI SCAMS IS LOW-TECH SKEPTICISM, EXPERT WARNS
4) Check where you're signing in
Before entering account credentials, examine the website address and consider how you arrived there. A page displaying familiar branding may still belong to a criminal. Shortened links can also conceal the final destination. Whenever possible, open Microsoft or Google directly through a trusted bookmark or the official website. Remember that a padlock icon and HTTPS connection do not guarantee that a website is trustworthy.
5) Keep strong account security enabled
Continue using multifactor authentication, even though some phishing attacks can defeat certain forms of it. For stronger protection, consider phishing-resistant authentication, such as FIDO2 security keys or supported passkeys. These methods can help prevent attackers from stealing credentials through fraudulent login websites. While these methods offer stronger protection against phishing, they cannot guarantee protection if an attacker obtains a valid authenticated session through another method. However, no single security measure stops every possible attack. Organizations should also consider additional controls to protect authenticated sessions and reduce the risk of stolen tokens being reused. Microsoft recommends restricting device code authentication wherever it isn't necessary. IT administrators can apply those restrictions through Microsoft Entra Conditional Access policies after reviewing legitimate business needs.
6) Use security software with phishing protection
Strong antivirus software and browser protections can help identify suspicious links and dangerous websites before you interact with them. Look for protection that helps detect phishing pages and malicious downloads. Keep your browser and security tools updated so they can benefit from the latest available protections. However, remember that attackers frequently create new websites to evade detection. Security software can reduce your exposure, but it cannot guarantee that every fraudulent invitation will be blocked. Get my picks for the best 2026 antivirus protection winners for your Windows, Mac, Android & iOS devices at Cyberguy.com
What to do if you already clicked a fake AI event invitation
If you've already clicked on a suspicious event invitation, don't panic. What you do next depends on how far you got in the sign-in process. Here are the steps to take to protect your accounts.
- Close the suspicious page. If you clicked the invitation but did not enter account details or approve a sign-in, close the website. Report the invitation through your organization's security reporting process.
- Contact your IT or security team immediately. If you entered your work credentials or approved a Microsoft device code, let your company's security team know right away.
- Explain exactly what happened. Tell your security team whether you entered a device code, submitted your password or completed a Google sign-in. These details can help them identify the attack.
- Secure your accounts. Your IT team may need to reset your password, revoke active sessions and authentication tokens, and investigate suspicious access to connected applications.
- Don't assume changing your password fixes everything. Attackers may already have a valid authentication token or session cookie. Even after sessions are revoked, some access tokens may remain valid until they expire.
The sooner you report suspicious activity, the better the chances of stopping unauthorized access before more damage occurs.
Kurt's key takeaways
Criminals know people are eager to keep up with AI, and they're using that interest to make their scams more convincing. An invitation offering free ChatGPT Pro or access to an exclusive event sounds pretty tempting. But what really concerns me is that you can land on Microsoft's actual sign-in page and still give a hacker access to your account. Think about that. Even checking the website address may not be enough to protect you. So before you sign up for that next AI event, take a minute to make sure it's legitimate. I'd rather miss out on a free offer than hand a criminal access to my work account.
CLICK HERE TO DOWNLOAD THE FOX NEWS APP
Have you ever received an invitation to an online event that seemed too good to be true? What made you suspicious? Let us know by writing to us at Cyberguy.com
Sign up for my FREE CyberGuy Newsletter
- Get my best tech tips, urgent security alerts and exclusive deals delivered straight to your inbox.
- For simple, real-world ways to spot scams early and stay protected, visit CyberGuy.com - trusted by millions who watch CyberGuy on TV daily.
- Plus, you'll get instant access to my Ultimate Scam Survival Guide free when you join.
Copyright 2026 CyberGuy.com. All rights reserved.
