---
id: "8479763fd3434d1e"
title: "Latest Windows update disables key security setting – but there’s a workaround"
url: "https://zdnet.com/tech/microsoft-october-windows-update-disables-security-setting-workaround"
link: "https://zdnet.com/tech/microsoft-october-windows-update-disables-security-setting-workaround"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T14:26:05Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Lance Whitney"]
language: "en"
summary: "A bug in Microsoft’s October Windows update prevents you from turning on a security setting that blocks malicious or suspicious apps. A Registry hack fixes the glitch."
tags: ["Windows 11"]
orgs: ["Microsoft"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 491
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/mshq2GettyImages-1408775753.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Latest Windows update disables key security setting – but there’s a workaround

ZDNet · Lance Whitney · 2026-10-20

ZDNET’s key takeaways
- The October Windows update disables Smart App Control.
- You’re unable to turn on the feature if it’s turned off.
- You can temporarily squash the bug through a Registry hack.
Microsoft’s monthly Windows updates always seem to sneak in some new bug that impacts an important feature or setting. And that’s the case with this month’s update.
Also: 5 apps I always install on new Windows PCs – and most are free
Rolled out on October 13, the latest Patch Tuesday update for Windows 11 has a glitch that disables a security setting for Smart App Control. Added to Windows 11 in 2022, Smart App Control blocks potentially malicious or suspicious apps and files from infecting your computer. Stronger and stricter than some of the other built-in security settings, this is designed to protect you against new and emerging threats.
More from ZDNET
How to check if you’re affected
Microsoft says that it’s working on a fix for this bug and will provide an update in a future release. In the meantime, you can get past the glitch by adding two keys to the Windows Registry. Microsoft has provided the steps for doing that.
Also: This free Windows 11 tool can rescue your PC when things go wrong
First, though, you’ll want to see if you’re affected. Go to Settings, select Privacy & security, and then click Windows Security. In the section for Protection areas, select the one for App & browser control. In the new window that pops up, click the link for Smart App Control settings. If the option is currently set to Off and the one for On is grayed out, then you’ve been hit by the bug.
To get past this, type cmd in the Search box to open a command prompt window. But choose the option to run as administrator; otherwise, you won’t be able to modify the Registry.
At the command prompt, type the following commands one after the other:
reg add “HKLM\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides” /v 2883193997 /t REG_DWORD /d 1 /f
reg add “HKLM\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides” /v 2850574478 /t REG_DWORD /d 1 /f
After each command, you should receive a confirmation that the operation completed successfully. In that case, close the command prompt and reboot your PC. Log back in and head to the same Smart App Control settings screen. You should now see that the On option is once again available, allowing you to activate the feature.
Also: My 5 favorite Windows Insider features
In general, I think it’s a good idea to enable Smart App Control to defend you from potentially malicious apps and files. The only downside is that it can get in your way if you download or install a lot of files from unfamiliar sources. In that case, you can always turn it off. But try it for a while to see if you can live with it, as it can prevent unknown malware from infecting your system.
