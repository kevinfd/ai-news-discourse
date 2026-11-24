---
id: "796c738a590ef673"
title: "Investigation of Polymarket Insider Trading on the Reinstatement of Jensen Huang"
url: "https://deucalionn.vercel.app/polymarket-delit-initie-jensen-huang-nvidia"
link: "https://deucalionn.vercel.app/polymarket-delit-initie-jensen-huang-nvidia"
source: "deucalionn.vercel.app"
domain: "deucalionn.vercel.app"
source_type: "community"
collector: "hackernews"
date: "2026-11-24T11:13:55Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["oska"]
language: "en"
summary: "Polymarket : Autopsie d'un délit d'initié sur la réintégration de Jensen Huang chez NVIDIA\n[!NOTE] Pourquoi cet article et cette analyse ?\nDepuis quelque temps, je constate que Polymarket devient un véritable terrain de jeu pour les délits d’initiés, et le climat politique autour de la nouvelle administration Trump rend ce type d’asymétrie d’information encore plus propice. J’ai donc développé…"
tags: []
orgs: ["Nvidia"]
topics: ["chips & infrastructure"]
content_source: "fulltext"
word_count: 1457
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50626578"
score: 259
comments: 137
community: "Hacker News"
---

# Investigation of Polymarket Insider Trading on the Reinstatement of Jensen Huang

deucalionn.vercel.app · oska · 2026-11-24

Polymarket : Autopsie d'un délit d'initié sur la réintégration de Jensen Huang chez NVIDIA
[!NOTE] Pourquoi cet article et cette analyse ?
Depuis quelque temps, je constate que Polymarket devient un véritable terrain de jeu pour les délits d’initiés, et le climat politique autour de la nouvelle administration Trump rend ce type d’asymétrie d’information encore plus propice. J’ai donc développé un algorithme qui surveille en permanence les marchés les plus sensibles : chaque transaction y est analysée par des modèles statistiques et des outils de traçage de flux on-chain.
J’ai finalisé l’algo il y a deux jours à peine. Dans la nuit même, en voyant l’alerte se déclencher, j’ai mené une première analyse à chaud sur les transactions… avant de voir tomber quelques heures plus tard le tweet de Donald Trump confirmant l’asymétrie. Et vous allez voir que le communiqué officiel de NVIDIA n’était que la cerise sur le gâteau.
Cette enquête documente, à la minute et au hash près, un cas assez probant de délit d’initié sur Polymarket détecté en temps réel.
Question principale
Y a-t-il eu un délit d’initié sur le marché « Will Jensen Huang rejoin NVIDIA by December 31, 2026? » ?
- Le timing : Une accumulation de liquidité achevée en pleine nuit Transactions Polygon, exactement 89 minutes avant la prise de position publique de Donald Trump sur Truth Social ;
- L’asymétrie de gain : 4 648 USDC engagés sur une probabilité marginale de 6,5 %, dénoués en 71 518 USDC suite à la confirmation unanime du Conseil d’Administration de NVIDIA sur Polymarket ;
- Le profil du portefeuille : Un compte jetable Gnosis Safe Proxy créé 81 heures auparavant, dont l’activité est 100 % monothématique.
Question secondaire : En quoi les marchés de prédiction décentralisés constituent-ils désormais le sismographe le plus implacable pour révéler publiquement des délits d’initiés invisibles sur les bourses traditionnelles ?
Réponse courte (avant d’entrer dans le détail)
Sur le strict plan des données on-chain, l’hypothèse du hasard est statistiquement disqualifiée. L’acheteur anonyme opérant sous le pseudonyme ljhggk a méthodiquement balayé le carnet d’ordres jusqu’à 0,065 $, verrouillé sa position avant toute réaction de marché, puis encaissé passivement les deux catalyseurs successifs pour réaliser un gain net de +66 869,34 USDC (+1 438,5 % de ROI).
flowchart TB
  subgraph Chronologie ["Reconstitution temporelle (Heure française CET)"]
    direction TB
    A["<b>23/11 · 02:19 - 03:28 CET</b><br/>Rafle OTM discrète<br/>4 ordres · 4 648 $ à 6,5 ¢"] --> B["<b>23/11 · 04:57 CET</b> (+89 min)<br/>Catalyseur 1 : Post Trump<br/>« I hope the Board rehires Jensen »"]
    B --> C["<b>23/11 · 14:30 CET</b> (+11h)<br/>Catalyseur 2 : PR NVIDIA (Wall St)<br/>Réintégration immédiate du CEO"]
    C --> D["<b>23/11 · 15:40 CET</b><br/>Résolution à 1,00 $<br/>Encaissement : 71 518 USDC"]
  end
  D --> R["<b>Bilan Forensic</b><br/>Profit net : +66 869 USDC<br/>Multiplicateur : 15,38x"]
1 · L’Anatomie du trade : 71 518 parts OTM raflées en pleine nuit
Entre 02:19:11 et 03:28:20 CET (01:19 - 02:28 UTC) dans la nuit du dimanche au lundi 23 novembre 2026, le carnet d’ordres du marché Will Jensen Huang rejoin NVIDIA by December 31, 2026? était totalement assoupi. La probabilité implicite stagnait à 6,5 %, reflétant un consensus quasi-unanime : suite à sa démission du 12 novembre, un retour de Huang avant la fin de l’année paraissait exclu.
C’est à cet instant précis qu’un acteur unique déploie une stratégie d’absorption agressive, découpée en 4 ordres limités successifs :
Le relevé des 4 transactions sur Polygon
Chaque transaction a été retracée. Les 4 transactions ont été incluses dans les blocs sans rejet Registre complet :
[!NOTE] Verdict technique de l’exécution : L’opérateur n’a pas étalé ses achats sur 24 heures pour moyenner son coût. Il a exécuté un achat massif et concentré en pleine nuit européenne/américaine, absorbant 34 % de toute la liquidité vendeuse disponible sur le contrat, ce qui pourrait montrer qu’il a eu l’info quelques heures avant et qu’il n’a pas spécialement eu le temps de l’étaler davantage. Dès son dernier ordre complété à 03:28:20 CET, il s’est totalement arrêté de négocier.
À noter : le compte s’était déjà positionné sur de petits montants sur ce pari dès sa création, mais sans jamais approcher de volumes comparables à ce qui a levé l’alerte cette nuit-là. Cette montée soudaine en conviction renforce encore la suspicion.
2 · La Reconstitution temporelle : 89 minutes d’avance sur le monde réel
Le cœur du dossier réside dans la corrélation temporelle entre la clôture de l’accumulation on-chain et la chaîne des déclarations publiques.
02:19 CET ─── 03:28 CET ──────── 04:57 CET ────────────────────── 14:30 CET ─── 15:40 CET
[Achats]      [Fin Accum.]      [Post Trump]                     [PR NVIDIA]     [Résolution]
  4 648 $       Verrouillé        « I hope the Board... »          Officiel        1.00 $
               71 518 parts       Truth Social                     Wall Street     71 518 $
                     ▲                  │                               │
                     └──── +89 min ─────┘                               │
                     └────────────────────── +11h 02min ────────────────┘
1. Le catalyseur politique : La publication de Donald Trump (+89 min)
À 04:57:00 CET (22:57:00 EST le 22 novembre), Donald Trump publie sur son réseau Truth Social :
« I hope the Board of Nvidia rehires Jensen Huang. It would be the best thing for the Company, and also, for the U.S.A. »
Il ne s’agit pas d’une injonction légale, mais le poids politique est massif : la mise à l’écart de Huang reposait sur des craintes de sécurité nationale. Le soutien explicite de Trump lève immédiatement le principal verrou psychologique. Le contrat bondit instantanément de 0,065 $ à 0,14 $ dans les échanges de la nuit.
2. Le catalyseur corporate : Le Conseil d’Administration de NVIDIA (+11h)
À 14:30:00 CET (08:30:00 EST), exactement une heure avant l’ouverture de Wall Street, NVIDIA diffuse son Communiqué officiel de réintégration. Le Conseil d’Administration confirme avoir voté à l’unanimité la réintégration immédiate de Jensen Huang au poste de CEO et Board Member, précisant avoir reçu l’assurance des plus hauts échelons du gouvernement américain quant à l’absence de risque sécuritaire.
Le contrat binaire explose vers 0,985 $, avant d’être résolu et encaissé à 1,00 $.
3 · L’Empreinte on-chain : Ce que révèle le profil du wallet
Dans le cadre d’un audit de délit d’initié (insider trading), l’analyse on-chain permet d’isoler des critères objectifs d’intentionnalité. Le compte ljhggk coche l’intégralité des marqueurs d’un portefeuille jetable (burner proxy) :
flowchart LR
  EOA["<b>Portefeuille personnel (EOA)</b><br/><code>0x3e0f9ada318fa8...</code><br/>Adresse signataire directe"] -->|Déploiement Safe| Proxy["<b>Gnosis Safe Proxy</b><br/><code>0xdf8616e18da2ad...</code><br/>Âge : 81h · Pseudo : ljhggk"]
  Proxy -->|100% Capital| Trade["<b>Marché Unique : NVIDIA</b><br/>4 648 USDC sur YES @ 6,5 ¢<br/>Zéro diversification"]
  Trade -->|Dénouement| Cashout["<b>Position Résolue</b><br/>71 518 USDC (+1 438%)"]
4 · D’où viennent les fonds ?
En inspectant l’adresse à l’origine de la création du compte Polymarket (0x3e0f9ada318fa8...) sur Polygonscan, on fait un constat surprenant : son historique affiche 0 transaction. Le wallet est totalement vierge et n’a jamais interagi directement avec le réseau Polygon.
Ce n’est donc pas ce wallet qui a directement fourni ou transféré les fonds on-chain.
Le rôle du pUSD et du bridge Polymarket
Sur Polymarket, le fonctionnement des soldes et des ordres repose sur une certaine mécanique :
- Aucun besoin de gaz sur le wallet personnel : L’utilisateur signe ses ordres d’achat hors-chaîne depuis son navigateur. C’est le relais officiel de Polymarket (Relayer) qui diffuse les transactions sur la blockchain et règle les frais de réseau à sa place.
- Le concept de pUSD (Polymarket USD) : Pour négocier sur le carnet d’ordres, la plateforme utilise son propre jeton interne indexé sur le dollar : le pUSD. Ce jeton n’est pas envoyé par un particulier, mais émis automatiquement par le protocole lors d’un dépôt.
- Le contrat de bridge / séquestre : Quand un utilisateur approvisionne son compte, les USDC réels sont déposés dans le coffre de séquestre de Polymarket (Collateral Vault). En contrepartie, le bridge de Polymarket crée (mint) les pUSD équivalents directement sur le contrat proxy unique de l’utilisateur (0xdf8616e1...).
- L’origine des capitaux : Les fonds engagés proviennent très probablement d’un retrait direct depuis une plateforme d’échange centralisée (comme Binance, Kraken ou Coinbase) vers l’adresse de dépôt assignée par Polymarket, d’un autre portefeuille externe via une passerelle cross-chain, ou d’un paiement bancaire direct via le partenaire d’intégration fiat (MoonPay).
Ce montage montre que l’acheteur a utilisé une adresse totalement vierge pour signer les ordres sans laisser d’antécédents directs, en faisant transiter sa liquidité directement par les infrastructures de dépôt de Polymarket.
Conclusion
Le délit d’initié sur Polymarket présente une rupture majeure par rapport aux marchés financiers traditionnels : toutes les traces sont publiques, horodatées et infalsifiables dès la première seconde.
Sources
- Fiche de marché Polymarket — Réintégration Jensen Huang
- Polygonscan — Contrat Proxy du portefeuille suspect 0xdf8616…
- Polygonscan — Registre des 4 transactions d’accumulation
- Truth Social — Déclaration publique de Donald Trump sur Jensen Huang
- NVIDIA Newsroom — Communiqué officiel de réintégration par le Conseil d’Administration
