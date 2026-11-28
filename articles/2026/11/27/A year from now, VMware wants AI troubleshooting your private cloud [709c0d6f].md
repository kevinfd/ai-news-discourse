---
id: "709c0d6fb04dc170"
title: "A year from now, VMware wants AI troubleshooting your private cloud"
url: "https://thenewstack.io/vmware-private-cloud-kubernetes"
link: "https://thenewstack.io/vmware-private-cloud-kubernetes"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-27T16:07:11Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "A developer who needs two containers to test a change or modification has a different problem from a platform engineer running an application across several Kubernetes clusters. \n\n Both need infrastructure, preferably before the ticket asking for it becomes old enough to have a birthday. Broadcom’s pitch for VMware Cloud Foundation is that the same private cloud can serve both teams, along with…"
tags: ["Containers", "Kubernetes", "Platform Engineering", "Podcast", "sponsor-broadcom", "Sponsored", "sponsored-podcast", "Video"]
orgs: []
topics: ["chips & infrastructure", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 679
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A year from now, VMware wants AI troubleshooting your private cloud

The New Stack · Chris J. Preimesberger · 2026-11-27

A developer who needs two containers to test a change or modification has a different problem from a platform engineer running an application across several Kubernetes clusters. 

 Both need infrastructure, preferably before the ticket asking for it becomes old enough to have a birthday. Broadcom’s pitch for VMware Cloud Foundation is that the same private cloud can serve both teams, along with the people who still need virtual machines. 

 In an interview recorded recently at KubeCon + CloudNativeCon 2026 in Salt Lake City, The New Stack’s Nick Lucchesi asked Mark Chuang , senior director of product marketing for VMware Cloud Foundation at Broadcom, what developers and operators notice when they mix a cocktail of VMs, containers, and AI workloads onto one platform.  

 “They get a public cloud-like experience when it comes to self-service.” 

 “They get a public cloud-like experience when it comes to self-service,” Chuang told TNS, starting with the experience of asking for resources. “Platform teams still set the policies that govern those resources.”  

 This indeed matters when an AI application depends on services running in both containers and VMs. Operators can apply common security policies, manage the lifecycle of those workloads, and decide where they run. Developers can use self-service to get the infrastructure they need and continue working with their existing CI/CD tools, Chuang said. 

 How much orchestration do you need? 

 Chuang describes direct container deployment as an option for lightweight edge applications or quick developer checks. Kubernetes makes sense when an application needs automated orchestration across clusters. For a team testing a small change, spinning up a couple of containers directly can save setup work. For a platform team, both approaches fit into the same operating environment. 

 Lucchesi also asks what Broadcom means when it says a partner application has been validated for vSphere Kubernetes Service (VKS) . Chuang explains that Broadcom provides test environments and automated tools, while the software vendors define the tests appropriate to their applications. 

 “We’re just trying to lighten some of the load that’s on the plate of our customers.” 

 The checks can cover initial deployment, recovery from failure, security, and even a clean uninstall. Broadcom reviews the results, and partners use them to produce reference architectures and technical guidance. 

 “We’re just trying to lighten some of the load that’s on the plate of our customers,” Chuang said. 

 What if an update breaks a partner application anyway? Chuang says customers can contact either Broadcom or the software vendor. If they call Broadcom, its support team starts by trying to determine whether the problem came from the platform or the application update. That’s a practical detail for a developer who knows exactly when something stopped working and has several plausible explanations. 

 The tools teams already reach for 

 Broadcom also packages frequently used tools such as Prometheus, Argo CD and Harbor as VKS add-ons. Chuang says the company looks at usage and customer feedback when deciding what to include. Handling installation and updates through VKS takes work off teams that would otherwise have to maintain those integrations themselves. 

 The conversation touches on a change Chuang has noticed among customers. Some are increasingly willing to accept a curated set of tools if it gets them to a working environment faster. 

 “Is it a storage issue? Is it a network issue? Is it a CPU contention issue?” 

 TNS also asked Chuang which job a private cloud might take off an operator’s hands a year from now. Chuang’s answer starts with a familiar complaint about a slow application. 

 “Is it a storage issue? Is it a network issue? Is it a CPU contention issue?” Chuang asked, rhetorically. A year from now, Chuang expects AI to do more of the diagnostic work across those layers. 

 Watch the full interview on The New Stack’s YouTube channel for his take on what that could look like, what partner validation actually buys a developer, and why the quickest path to testing a container sometimes starts with a smaller deployment. 
 The post A year from now, VMware wants AI troubleshooting your private cloud appeared first on The New Stack .
