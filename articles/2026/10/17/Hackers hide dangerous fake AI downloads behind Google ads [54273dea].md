---
id: "54273dea8f8c624e"
title: "Hackers hide dangerous fake AI downloads behind Google ads"
url: "https://foxnews.com/tech/hackers-hide-dangerous-fake-ai-downloads-behind-google-ads"
link: "https://foxnews.com/tech/hackers-hide-dangerous-fake-ai-downloads-behind-google-ads"
source: "Fox News"
domain: "foxnews.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-17T13:20:23Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Kurt Knutsson", "CyberGuy Report"]
language: "en"
summary: "You search Google for Claude, the popular AI assistant, and spot a sponsored result. The link points to Bing, Microsoft's search engine. Nothing immediately screams scam.  However, that click could send you through several websites before landing on a convincing fake Claude download page designed to trick you into running a dangerous command on your Mac. Security researchers at Push Security…"
tags: ["88e83672-3101-5f01-94e0-f50cb39d6b4d", "fnc", "Fox News", "fox-news/tech/topics/cybercrime", "fox-news/tech/topics/virus", "fox-news/culture", "fox-news/tech", "article"]
orgs: ["Anthropic", "Google", "Microsoft"]
topics: ["search & media"]
content_source: "fulltext"
word_count: 2120
paywalled: false
image: "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/10/931/523/AI-Hackers-Photo-1.jpg?ve=1&tl=1"
discussion_url: null
score: null
comments: null
community: null
---

# Hackers hide dangerous fake AI downloads behind Google ads

Fox News · Kurt Knutsson, CyberGuy Report · 2026-10-17

You search Google for Claude, the popular AI assistant, and spot a sponsored result. The link points to Bing, Microsoft's search engine. Nothing immediately screams scam.
However, that click could send you through several websites before landing on a convincing fake Claude download page designed to trick you into running a dangerous command on your Mac.
Security researchers at Push Security uncovered a clever attack that uses legitimate search engine links to hide a malicious installer. The technique, which researchers jokingly call "Adception," takes advantage of how Google ads and Bing redirects work.
Even more concerning, the fake installer shows one command on the screen while secretly copying another. Here's how the scam works and what you should know before downloading AI software.
ANTI-SCAM SETTINGS ON IPHONE, PIXEL AND GALAXY YOU SHOULD CHECK
Join our upcoming CyberGuy LIVE class: 5 Ways to Travel Smarter and Save Money
In this free live online class, Kurt "CyberGuy" Knutsson will share five practical ways to protect your trip and your wallet this holiday travel season. You’ll learn how to secure your phone and personal information, find better travel deals, avoid common scams, save money on bookings and use technology to make your travels easier and less stressful. No technical experience is needed.
Join us Saturday, Oct. 31, at 11 a.m. ET/8 a.m. PT. Register free now at CyberGuyLive.com.
How a fake AI download scam starts with Google
The attack begins with a Google search for "Claude Mac." According to Push Security, researchers discovered a sponsored search result that displayed bing.com as its destination. That address might seem reassuring because Bing belongs to Microsoft.
However, clicking the advertisement sends users through a series of redirects. First, Google's advertising system processes the click. Next, Bing's legitimate click-tracking service forwards the browser to a compromised WordPress website belonging to a South American retailer. Finally, that website sends the visitor to a fake Claude download page.
The final website, claude-desk-code[.]com, imitates the real Claude download experience. It presents what appears to be a legitimate macOS installation option. By the time someone reaches the page, they may have little reason to suspect the journey began with a malicious advertisement.
Researchers say the attackers deliberately used a real Bing search result for a compromised website. This allowed the attackers to display Bing's legitimate domain in the Google advertisement while using Bing's click-tracking redirect to send visitors toward the malicious destination.
Why the fake Claude installer is difficult to spot
The scammers added another layer of deception to make their operation harder to detect. The compromised retailer's website checks whether visitors arrived through Bing and whether their browsers send certain information. Meanwhile, the fake Claude website checks whether visitors came from Google or Bing.
Someone who visits the malicious website directly may see a 404 error page instead of the fake installer. That behavior can make it harder for security scanners to investigate the attack because they may never encounter the page that victims actually see.
Push Security calls this technique cloaking. Attackers use it to control who reaches their malicious content while showing something harmless to other visitors. In this case, the researchers observed two separate checks designed to protect the attack from unwanted attention. The result is a carefully constructed path that makes a dangerous destination appear more trustworthy than it really is.
The fake Claude download button hides a dangerous command
Here's where the attack gets particularly sneaky. The fake Claude page displays an installation command that appears to come directly from Anthropic, the company behind Claude. The command references Claude's legitimate website and looks like something a technically confident Mac user might recognize. However, the page's Copy button places a completely different command on the clipboard.
According to Push Security, the substituted command uses Base64 encoding to conceal an attacker-controlled website. When someone runs the pasted command in Mac Terminal, it first displays a reassuring message claiming that Claude is being downloaded from its official website.
Behind the scenes, the command decodes the hidden address, downloads a remote script and sends it directly to the Mac's Z shell for execution. That means the person running the command sees references to Claude's legitimate website even though the Mac is executing code from an unrelated server.
This attack follows a technique known as InstallFix, a variation of ClickFix. These scams convince people to execute malicious commands themselves, often by disguising the instructions as a software installation or troubleshooting step.
Push Security identified several additional websites associated with the same malicious toolkit, which it tracks internally as AcSig. The researchers found matching installation commands and similar fake installer interfaces across those sites.
What happens if someone runs the fake Claude installer?
The research confirms that the malicious command is designed to download a remote script from an attacker-controlled server and pass it directly to the Mac's Z shell for execution. However, Push Security's published findings do not identify the final payload or establish what the downloaded script does after execution.
That uncertainty is important. Running an untrusted Terminal command can give malicious code an opportunity to operate with the permissions of the person executing it. Depending on the script, an attacker could potentially steal information, modify files or install additional software. The researchers have not confirmed those specific outcomes in this campaign.
The bigger concern is how easily the attack can persuade someone to bypass their own caution. The user voluntarily pastes the command, believing it came from a legitimate software provider. Meanwhile, the actual destination stays hidden inside encoded text.
Push Security reports that four out of five ClickFix attacks it detects reach victims through search engines. That figure comes from the company's own detection data rather than a measurement of all attacks worldwide. Still, it shows why malicious search advertisements deserve attention.
Google suspends accounts behind malicious ads
Google confirms it has taken action against the advertiser accounts associated with the reported campaign.
"We've suspended the advertiser accounts running the reported campaign. Using ads to distribute malware is an egregious violation of our policies, and we consistently update our detection systems to stay ahead of bad actors' evolving tactics," a Google spokesperson told CyberGuy.
Google also says attackers use cloaking to show its advertising review systems different content from what people actually see. The company says it continues monitoring attempts to evade its protections and updating its detection systems.
Microsoft responds to malicious AI download campaign
Microsoft also responded to CyberGuy's request for comment, confirming that its security protections identify the malicious indicators described in the research.
"We take reports of malicious online activity seriously and continuously work to help protect customers from evolving threats," a Microsoft spokesperson told CyberGuy.
"Microsoft Defender protections detect and block the malicious indicators identified in the report."
We also reached out to Anthropic for comment on the findings but did not hear back before our deadline.
How to protect your Mac from fake AI downloads
You don't need to understand every line of computer code to avoid this scam. A few precautions can help you recognize suspicious downloads before they put your Mac at risk.
1. Download Claude directly from Anthropic
Instead of searching for a download and clicking the first sponsored result, go directly to Claude's official download page. Anthropic provides a macOS download there, so you can install the desktop application without relying on an unfamiliar website. You can also access Claude through your browser at claude.ai.
2. Treat unexpected Terminal instructions as a warning
Be especially careful when a website tells you to copy a command into your Mac's Terminal. Terminal commands can download software, change system settings and execute scripts. Even legitimate-looking instructions can become dangerous when they come from an untrusted source. For the regular Claude desktop app, Anthropic provides a downloadable installer. You don't need to paste a command from a search advertisement to get started.
3. Check what a website actually copies
A website's Copy button can place different text on your clipboard than what appears on the page. Before running an unfamiliar command, paste it into a plain-text editor and compare it with the instructions. Watch for unexplained web addresses, encoded strings or commands that download and immediately execute remote scripts. However, even a command that looks harmless may contain hidden risks. When in doubt, stop and verify the instructions with the software developer.
4. Keep your Mac updated and use strong antivirus protection
Install macOS security updates and keep your browser current. Additionally, use strong antivirus software that offers real-time protection against malicious downloads and suspicious activity. Security software may help detect harmful scripts or their effects, although no antivirus product can guarantee protection against every attack. Get my picks for the best 2026 antivirus protection winners for your Windows, Mac, Android and iOS devices at Cyberguy.com
5. Be skeptical of sponsored search results
A sponsored placement means someone paid to promote a link. It does not guarantee that the destination is safe. Before clicking, check the advertiser by selecting the three dots next to a Google search ad. You can review who paid for it and check the advertiser's verification status.
Google's Ads Transparency Center at adstransparency.google.com offers another way to research advertisers. Always confirm you're visiting the software developer's official website before downloading anything. If an ad looks suspicious, use its three-dot menu to select "Report this ad."
What to do if you already ran the fake Claude command
If you pasted an installation command from a suspicious Claude website into Terminal and pressed Return, treat your Mac as potentially compromised. The researchers have not established what the final payload does, so don't assume everything is safe simply because nothing unusual appears on your screen.
- Disconnect your Mac from the internet. Turn off Wi-Fi and unplug any Ethernet connection to help prevent potential communication with an attacker.
- Run a security scan. Use strong antivirus software to check for malicious files or suspicious activity. Keep in mind that a clean scan cannot guarantee your Mac is safe.
- Change important passwords. From another trusted device, use a password manager to create strong, unique passwords for sensitive accounts, especially those you accessed after running the command. Prioritize your email and financial accounts, and change your password manager's master password if you suspect it was exposed. Enable two-factor authentication (2FA) wherever possible.
- Check for suspicious apps and permissions. Look for unfamiliar applications in your Applications folder and review System Settings > General > Login Items & Extensions for unexpected items. Also check System Settings > Privacy & Security for unfamiliar apps with sensitive permissions.
- Consider professional help. If your Mac contains sensitive personal or financial information, have a qualified technician or security professional examine it before reconnecting to the internet.
- Contact your IT department. If you use a work computer, notify your IT or security team immediately. They can investigate what the command executed and determine whether additional steps are necessary.
WHY VERIFIED SOCIAL MEDIA ACCOUNTS CAN STILL LEAD YOU INTO A SCAM
Kurt's key takeaways
What concerns me most about this attack is how much effort the scammers put into making everything look familiar. You start with Google, pass through a legitimate Microsoft service and eventually arrive at a page that looks like it belongs to a popular AI company. Then, with one click of a Copy button, the website quietly substitutes a command that could put your Mac at risk. I've always encouraged people to pay attention to website addresses before downloading software.
That's still important, but this case shows why checking the address alone may not be enough. The attackers used trusted services to disguise where their link was taking people. My advice is to go straight to the software developer's official website, especially when installing AI tools.
And whenever a download page asks you to run something in Terminal, make sure you understand exactly what you're authorizing. A few extra seconds of caution could save you from a much bigger headache.
Would you trust a software download if it appeared in a Google ad and showed a familiar Microsoft link, or has this kind of scam made you question whether search results can be trusted at all? Let us know by writing to us at Cyberguy.com
Sign up for my FREE CyberGuy Newsletter
- Get my best tech tips, urgent security alerts and exclusive deals delivered straight to your inbox.
- For simple, real-world ways to spot scams early and stay protected, visit CyberGuy.com - trusted by millions who watch CyberGuy on TV daily.
- Plus, you'll get instant access to my Ultimate Scam Survival Guide free when you join.
CLICK HERE TO DOWNLOAD THE FOX NEWS APP
Copyright 2026 CyberGuy.com. All rights reserved.
