---
id: "772f4d70ca2a8f96"
title: "Lost or stolen Windows laptop? IT can lock it down without wiping it now"
url: "https://zdnet.com/tech/microsoft-preview-remote-lock-intune-windows-devices"
link: "https://zdnet.com/tech/microsoft-preview-remote-lock-intune-windows-devices"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T16:08:03Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Taylor Clemons"]
language: "en"
summary: "The Intune-enabled feature will allow admins to remotely lock down any compromised Windows device."
tags: ["Windows 11"]
orgs: ["Microsoft"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 403
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/windowslock-GettyImages-2239565222.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Lost or stolen Windows laptop? IT can lock it down without wiping it now

ZDNet · Taylor Clemons · 2026-11-16

ZDNET’s key takeaways
- The new remote lock feature is designed for IT administrators.
- The lock will persist across restarts until an admin removes it.
- The lock won’t affect your Microsoft account, so you can still sign in to other devices.
Microsoft is testing a new feature that lets IT admins instantly lock down your lost or stolen device via remote connection, protecting your work projects and personal data from theft and unauthorized access.
Also: Windows 11 can run better on PCs with 8GB now
How Microsoft’s new remote lock works
Once a device is reported missing or stolen, an admin can disable login access from anywhere without having to fully wipe the laptop or smartphone. Microsoft reports that the lockdown will persist across restarts, even if the device is disconnected from Wi-Fi networks, and can only be lifted by an admin. This means that thieves can’t use your passwords, PINs, or biometric data to circumvent the lock.
While the new feature allows IT admins to respond quickly when a laptop or phone is reported missing, there are still security gaps that other Windows controls must address. The new lock feature doesn’t erase your data or wipe your device if it can’t be recovered, nor does it isolate the missing device from corporate networks. Therefore, IT admins will still need to access those controls via the Intune and Microsoft Entra dashboards.
Also: You can now restore Windows 11 even if it can’t boot up
The remote lock feature also doesn’t change your Microsoft account credentials, so you can use your log-ins on other devices to recover your data, change passwords, and temporarily disable permissions. Finally, Remote lock doesn’t block the device from being booted in Safe Mode, from a USB, in Windows Recovery Mode, or if the storage drive is reimaged; Microsoft highly recommends keeping BitLocker enabled until the device can be wiped or recovered.
Setting up the remote lock is a straightforward process: Log into the Intune management center, then go to Devices > Windows > Configuration > Create > New Policy > Windows 10 and later > Templates > Custom. This lets admins create a profile for each network-connected device and a device group reserved for lockdown. Locking down a device is as simple as adding it to the group. To unlock, create a second profile and device group, and move the locked device to the new unlock category.
