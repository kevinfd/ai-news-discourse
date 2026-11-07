---
id: "0dd0efab7576004d"
title: "Alpine Linux and OpenSSH patch flaw that’s as bad as it can get"
url: "https://zdnet.com/tech/alpine-linux-openssh-patch-flaw"
link: "https://zdnet.com/tech/alpine-linux-openssh-patch-flaw"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-07T00:00:45Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Steven Vaughan-Nichols"]
language: "en"
summary: "This dangerous Linux security hole must be patched as soon as possible."
tags: ["Security"]
orgs: []
topics: ["products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 930
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-879472452.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Alpine Linux and OpenSSH patch flaw that’s as bad as it can get

ZDNet · Steven Vaughan-Nichols · 2026-11-07

ZDNET’s key takeaways
- An ancient bug is affecting Alpine Linux and a few other Linux distros.
- It’s about as bad as it can get.
- You must patch ASAP, and then restart the patched software.
The perfect nightmare scenario for a Linux server is when all an attacker needs to do is reach the server’s Secure Shell (SSH) port, waltz right in, and take it over. That’s what happened to Alpine Linux, the popular, lightweight Linux server. Adding insult to injury, this happened only days after Alpine Linux dodged a security hole-sized bullet to its GitLab implementation.
Also: Linux Mint 27 arrives next month, and I like it already: What to expect
How the attack works
As security engineer Gregory Bryant explained in his LinkedIn post:
Most authentication bypasses come from complex logic chains, but yesterday’s Alpine Linux OpenSSH vulnerability (CVE-2026-123158) comes down to a single character: *.”
If you run Alpine Linux (or another musl-based distro) with the default openssh-server package (no Pluggable Authentication Modules (PAM)) and PasswordAuthentication enabled, an attacker can log into password-disabled, or key-only accounts simply by sending a password between 257 and 1024 bytes long.
That’s it. That’s all.
Alpine Linux isn’t the only operating system that uses musl, a lightweight version of the standard C library (libc). Other operating systems that use musl and are potentially vulnerable include Adélie Linux; Void Linux; Sabotage Linux; OpenWrt, an Android variant, and the Yocto Project, which is used to build embedded Linux distributions.
Also: This clever banking scam keeps phishing by faking its own demise
Wind River, which produces the commercial embedded Linux distro, Wind River Linux, is also looking into the issue. A company representative told me, “Wind River takes security seriously. We are actively reviewing the reported vulnerability and assessing its potential impact. We will take appropriate action as needed.”
Behind the scenes, when OpenSSH is built without PAM, it verifies passwords by hashing the password attempt using the C library’s crypt() function. It then compares the result to the account’s stored password field. So far, so good.
But when a key is longer than 256 bytes, musl’s crypt() function returns the string * as an error indicator. That is also what the password field holds for any account with no password, such as a key-only account. Thus, the “hash” matches and the login succeeds, and the attacker walks in.
Also: The new Cutefish Linux distro might be the best MacOS clone around
To exploit it, an attacker only needs the name of such an account. The attacker also needs at least one other account on the machine with a 5 or 6 password hash, and then to send a password of 257 to 1,024 bytes. According to Alpine, one user with a password is enough to make every passwordless account accessible.
In Linux systems that use glibc’s crypt(), which is almost all of them, the same attempt would return NULL on error, which sshd already rejects, so Debian, Ubuntu, Fedora, etc., aren’t affected.
According to *sshole, the group that uncovered the problem, this is a side effect that has been hiding since 2016.
Who’s exposed
Alpine said every release it checked is affected: 3.21 through 3.24, edge, and the older 3.16 to 3.20 branches. Exposure requires the following:
- The openssh-server package, which is built without PAM, or openssh-server-pam with UsePAM no.
- PasswordAuthentication set to yes, which is the OpenSSH default.
- An account with * as its password field, and another account with a 5 or 6 hash.
Root is not directly exposed in most cases. It has shipped as root:* in the base image since about Alpine 3.16, but OpenSSH’s default PermitRootLogin prohibit-password blocks it. Another account that can become root, for example through doas, still gives an attacker a route to root.
Alpine singled out its official tiny-cloud images, versions 3.18.11 through 3.24.3, as especially vulnerable. These ship with an alpine user with a * password field and passwordless doas. They are safe on first boot but become exploitable once any 6 hash exists on the machine. That can happen when an administrator sets a console password or when user data adds a user with a hashed password, which means, essentially, all of them.
Alpine said these are not affected:
- Containers that do not run sshd.
- Systems with password authentication disabled.
- Systems using openssh-server-pam with UsePAM yes.
- Locked accounts with! in the password field.
- Cloud images configured through cloud-init, which writes PasswordAuthentication no.
The fix
Alpine released 3.21.10, 3.22.8, 3.23.8 and 3.24.4 on Thursday, with the OpenSSH fix among the security changes. It also published fixed packages for each release back to 3.16. Alpine 3.21 reached end of support on Nov. 1.
The just-released OpenSSH 10.6p2 avoids the problem in sshd. Alpine’s stable branches carry a patch for the same problem. You should run apk upgrade -U -a and then restart the daemon with rc-service sshd restart. Alpine stressed that upgrading the package does not replace the running daemon. Anyone who cannot update should set PasswordAuthentication no and restart sshd, after confirming that key login works.
Also: Maze Linux is the best security-focused distro I’ve ever tested
To check for an attack, Alpine told administrators to search /var/log/messages for “Accepted password for” lines that name an account with no password. It also advised reviewing dedicated OpenBSD application subexecutor (doas) use and recently created users, files, and authorized keys. “If you cannot rule out a login, treat the machine as compromised.” Just what you wanted for your weekend, I know, but here we are.
