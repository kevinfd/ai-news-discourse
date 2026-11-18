---
id: "8bb0f76172359f4c"
title: "Microsoft and Salesforce announce 'Copilotforce', with over 38 sales skills in preview. Clarifying the reality of Copilot integration"
url: "https://note.com/daigo_miyoshi/n/nd2a8b2ac7ad5?hl=en"
link: "https://note.com/daigo_miyoshi/n/nd2a8b2ac7ad5?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-17T21:52:00Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["三好大悟（Daigo Miyoshi）｜リベルクラフト"]
language: "en"
summary: "On November 17, 2026, it was reported that Microsoft and Salesforce announced a partnership called 'Copilotforce' at Microsoft Ignite. This includes 'Salesforce in Copilot,' a plugin featuring over 38 ..."
tags: []
orgs: ["Microsoft", "Salesforce"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 2175
paywalled: false
image: "http://www.bing.com/th?id=ONUT.8eGPUBhsODeTZCYQ-VDHFQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft and Salesforce announce 'Copilotforce', with over 38 sales skills in preview. Clarifying the reality of Copilot integration

note · 三好大悟（Daigo Miyoshi）｜リベルクラフト · 2026-11-17

SYSTEM NOTICE
Microsoft and Salesforce announce 'Copilotforce', with over 38 sales skills in preview. Clarifying the reality of Copilot integration
On November 17, 2026, it was reported that Microsoft and Salesforce announced a partnership called 'Copilotforce' at Microsoft Ignite. This includes 'Salesforce in Copilot,' a plugin featuring over 38 pre-built skills for sales, which is currently available in public preview.
However, expressions such as 'Copilot has become the OS for work' or 'Word, Excel, and PowerPoint have been integrated into Copilot' cannot be found in the materials at hand. It is necessary to read by distinguishing between confirmed facts and what is still unknown.
In this article, I will organize the details of the partnership, the mechanism of data integration, the introduction of Accenture, and the impact on Japanese companies in order. Daigo Miyoshi, who supports AI implementation in practice, will explain from the perspective of what can be tested at the preview stage. Please use this as material for sales, information systems, and corporate planning personnel to judge whether to test it in their own companies.
On November 17, 2026, Microsoft and Salesforce announced the 'Copilotforce' partnership at Ignite.
The announcement was made on November 17, 2026, at Microsoft Ignite. The name of the partnership is 'Copilotforce,' an initiative that combines Microsoft's Copilot with Salesforce.
The core is the 'Salesforce in Copilot' plugin. A plugin is an extension component that adds functionality to Copilot later. This plugin includes over 38 pre-built sales skills. 'Pre-built' means that they are created in advance so that users can use them without having to build them from scratch.
The availability stage is public preview. Public preview refers to a stage that is widely available but precedes the official release. Since specifications may change, it is considered a stage for testing on a small scale to gauge effectiveness rather than making it a prerequisite for production operations. When testing, it is easier to make decisions if you narrow down the target departments and periods.
The names and contents of individual skills are not known from the materials at hand. Since there is no mention of the general availability date or pricing, if you are going to test it in the sales department, you need to plan on the premise that costs and availability dates are not visible.
Microsoft Work IQ, which supports Copilot, provides context from Teams meetings, Outlook emails, and SharePoint and OneDrive documents.
The intelligence layer supporting Copilot is Microsoft Work IQ. The intelligence layer refers to a mechanism that reads and passes the situation from internal company information when AI creates answers or suggestions. The AI does not know the sales situation based solely on the instructions given. By passing background information such as meeting content and email history, it is thought that it will be easier to produce drafts and summaries that fit the situation.
Work IQ is cited as a source of context material from Teams meetings, Outlook emails, and documents on SharePoint and OneDrive. Teams is a service for meetings and chat, Outlook is a service for email, and SharePoint and OneDrive are services for storing documents. The history of business negotiations remains not only on the customer management screen but also in remarks made during meetings, email exchanges, and shared materials.
If the internal exchanges collected by Work IQ are added to Salesforce customer information, it may be possible to reduce the time and effort sales representatives spend checking history before making proposals. However, the materials at hand do not confirm in what situations and how Salesforce in Copilot uses Work IQ. It is considered important to check on the actual screen without having too high expectations.
With bidirectional zero-copy integration between Salesforce Data 360 and Microsoft Fabric, you can query each other without duplicating data.
Salesforce Data 360 and Microsoft Fabric are connected via bidirectional zero-copy integration. Data 360 is a platform for handling data on the Salesforce side, and Fabric is a platform for the Microsoft side. 'Bidirectional' means that you can reference the Microsoft side from Salesforce, and you can reference Salesforce from the Microsoft side. 'Zero-copy' refers to a method of referencing data while it remains in its original location without copying it to another location.
The materials state that this integration allows for mutual querying without duplicating data. A query is an inquiry into data. For example, it is assumed that it will be used to match customer data in Salesforce with other data on the Microsoft side without creating copies.
The advantage of not duplicating data is that it may reduce dual management and synchronization discrepancies. In many Japanese companies, data is often separated by department, and operations that create copies every time integration occurs tend to be a burden. On the other hand, the materials at hand do not contain information on access rights, costs, or integration setup procedures. For companies considering analysis that spans sales data and data from other departments, this is a point that needs to be confirmed.
Microsoft's materials describe Copilot as the 'front door' to business processes, not as an 'OS for work'.
In its materials, Microsoft describes Copilot as the 'front door' to business processes. The term 'front door' is considered to refer to the initial screen or point of contact where work begins. On the other hand, the expression 'OS for work' is not in the materials at hand. Which words are used to position Copilot is a clue to understanding the direction of the product, so it is also the first point to check when verifying primary information.
I will also organize the handling of Word, PowerPoint, and Excel. While there are mentions of Word and PowerPoint, they are not mentioned as being integrated into Copilot, but rather as places where sales representatives create proposals and business cases. There is no mention of Excel in the entire document.
In other words, the summary that 'Copilot has been integrated into Word and Excel' or 'has become the OS for work' is not supported by the materials. It is considered closer to the understanding of the materials to read that sales representatives start their work from Copilot, and Word and PowerPoint are mentioned as places to create proposals, rather than reading it as Copilot entering each application as a function. In AI news, short words in headlines can sometimes convey more than the reality. When sharing within the company, I think it is safe to quote the expressions in the materials as they are.
Accenture will introduce it to its own sales organization as a design and implementation partner and pilot customer.
Accenture is a design and implementation partner for Copilotforce, as well as a pilot customer. A pilot customer refers to a customer that uses the service in advance of a full-scale rollout to verify results. It is stated that Accenture will introduce it to its own sales organization.
The fact that the company responsible for design and implementation is also using it first in its own sales department can be considered material for thinking about how to proceed with the introduction. Since the side supporting the introduction is using it themselves, there is a possibility that issues arising in the field will be easily reflected in the design. However, the scope of the introduction at Accenture, the number of people, the duration, and the results are not mentioned in the materials at hand.
If a Japanese company were to try it, it would be realistic to choose one sales department and first take inventory of where daily business data such as case information, meetings, and emails are located. At the same time, it is also desirable to organize the storage locations and access rights for the data. Companies where information entered into Salesforce is separated from Teams meetings and Outlook emails should find it easier to verify the effects of this integration. Before verification, deciding on metrics to measure success will also make it harder for judgments during the preview to waver. All of these are the author's perspective, not official recommended procedures for the partnership.
GitHub Copilot deprecated models on November 16, 2026, and unconfirmed points remain regarding Copilotforce.
GitHub Copilot is a service that uses AI to assist developers in writing code. On November 16, 2026, GitHub deprecated Claude Opus 4.8, Claude Opus 5, and GPT-5.6 Terra for most GitHub Copilot features. The announcement was made on October 15, 2026. Claude Opus 5 was removed from the model picker (the screen for selecting models), but it remains for fallback rejection during execution. The connection to Ignite cannot be confirmed from the materials.
In the case of GitHub Copilot, it took about one month from the announcement to implementation. It is considered necessary to establish procedures for confirmation and review for AI tools incorporated into business, on the premise that models will be replaced.
There are still things that have not been confirmed. The general availability date and pricing for Copilotforce, the duration and keynote content of Ignite 2026, and other announcements in general are not mentioned in the materials. While a product page for the MAI brand's audio-to-audio model 'MAI Realtime 1' exists, it is unclear whether it was announced at Ignite, and the introduction of a 'new MAI model family' cannot be confirmed either. This article has not confirmed official primary information and is based on the materials at hand.
Summary
In short, 'Copilotforce' announced by Microsoft and Salesforce on November 17, 2026, is a partnership at the stage where plugins with over 38 sales skills can be tried in public preview. Accenture will introduce it in advance within its own sales organization. Copilot is described as the 'gateway to business processes,' and there is no mention in the materials of it being a 'work OS' or the integration of Word and Excel. The next things to confirm are the general availability date and pricing, data integration permissions and settings, and official primary information.
For those who want to move forward with verifying the Copilot integration between Microsoft and Salesforce
Since Copilotforce is in the preview stage and the availability date and pricing are unknown, it is essential to judge how much to try within your own company. In fact, when trying to work on it internally, many people stop at points such as:
- Being unable to decide which department to try the preview-stage integration in and to what extent, so verification does not begin
- Being unable to judge how much AI should be allowed to reference Teams meetings and Outlook emails
- Being unable to solidify the design and permission management for connecting Salesforce and other department data without duplication
There are many people who stop at these points.
I believe there are two main ways to proceed.
If you want to proceed while borrowing outside help
Libercraft supports corporate AI adoption from the practical side through AI development support and data science development support. You can consult with us from any stage, according to your needs, from requirement organization to PoC (small-scale verification), production operation, and internal training. We also provide the Agentic RAG SaaS 'Socrag'.
It is fine to be at the stage where 'nothing is specifically decided yet, but I would like to hear about it once.' We offer free individual consultations.
If you want to learn how to utilize AI integration in sales operations
For those who have read this far and thought, 'I want to be able to build this myself,' I run a course called Craft College. We offer a 'Data Scientist Training Course' for engineers and beginners aiming to become data scientists, a 'PM/Consultant Training Course' for non-engineer managers and project leaders, and an 'Advanced Course' for those already working with these tools in their daily tasks. You can learn how to incorporate AI tools into your business and verify their effectiveness while getting hands-on experience. We also hold regular trial information sessions.
The entry point differs depending on whether you are consulting as a company or learning as an individual, so please take a look at the one that suits you best.
About LiberCraft Inc.
<Company Overview>
If you are interested, please take a look at our company website!
<Recruitment Information>
We are also strengthening our recruitment activities. If you are interested, please feel free to contact us. I would be happy to have a casual conversation first.
<SNS Presence>
We also share information on various social media platforms. Please take a look.
- X: https://x.com/libercraft1202
- Instagram: https://www.instagram.com/k.k.libercraft/
- Youtube: https://youtube.com/channel/UCKbBfTER3_NF1sYhZijQX7Q/
- Spotify: https://open.spotify.com/show/76V9rKvukhx63uyRDoY5vc
- peatix: https://libercraft.peatix.com/
Author Introduction: Daigo Miyoshi
Representative Director of LiberCraft Inc. Focusing on AI/data utilization consulting and contract development (B2B), he supports AI implementation projects for various industries including JAXA, the Ministry of Defense, and MISUMI. He operates Craft College (a data science and AI practical school), supporting career changes and skill acquisition for working professionals aiming to become data scientists or AI project managers.
- Main areas of support: RAG, AI agents, machine learning, contract development, data scientist training
- X (Personal): https://x.com/daigomiyoshi_ai
- YouTube: https://youtube.com/channel/UCKbBfTER3_NF1sYhZijQX7Q/
