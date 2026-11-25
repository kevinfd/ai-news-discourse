---
id: "be935e935382b3ed"
title: "Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Preferences Into Ranking"
url: "https://marktechpost.com/2026/11/24/meta-facebook-your-algorithm-llm-recommendations"
link: "https://marktechpost.com/2026/11/24/meta-facebook-your-algorithm-llm-recommendations"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T23:06:17Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Meta has published an engineering deep dive on Facebook Your Algorithm . Your Algorithm lets people tell Facebook, in plain language, what they want in Feed and Reels. Meta announced the feature on October 13, 2026. The new post shows how large language models (LLMs) sit inside a production recommender. For developers, it is a rare look at explicit preferences wired into an implicit-signal…"
tags: ["Agentic AI", "Editors Pick", "For Devs", "Software Engineering", "Staff"]
orgs: ["Meta"]
topics: ["search & media", "models & research", "agents & coding"]
content_source: "summary"
word_count: 1304
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Preferences Into Ranking

MarkTechPost · Michal Sutter · 2026-11-24

Meta has published an engineering deep dive on Facebook Your Algorithm . Your Algorithm lets people tell Facebook, in plain language, what they want in Feed and Reels. Meta announced the feature on October 13, 2026. The new post shows how large language models (LLMs) sit inside a production recommender. For developers, it is a rare look at explicit preferences wired into an implicit-signal ranking stack. 

 TL;DR 

 What: ‘ Your algorithm is an end-to-end system that addresses the limitations of adaptability and nuance in recommendations’ 

 Runs on: Meta’s server-side ranking stack, plus on-device cache invalidation in the Facebook app. 

 Best: Explicit interests feed 4 retrieval sources and apply across both Feed and Reels. 

 Bottom line: Best: a clear blueprint for LLM-steered ranking 

 What is Facebook Your Algorithm? 

 Your Algorithm is an AI-powered preference page for Facebook Feed and Reels. It has 3 parts, per Meta’s engineering post . A one-sentence “Lately Summary” describes recent viewing. An “Interested In” list is prefilled from past activity. A “Not Interested In” list holds exclusions. Users can type interests, move them between lists, or delete them. Access is through the three-dot menu on posts, according to Meta’s newsroom . 

 Meta’s framing is simple. Implicit engagement signals scale well but adapt slowly and miss nuance. Explicit, stated preferences close that gap. 

 How does the Your Algorithm system work? 

 Meta splits the preference lifecycle into 4 components: 

 Profile generation: An LLM turns regularly refreshed interest signals into readable topic names. It also writes the Lately Summary. 

 Preference management: An LLM checks that a typed phrase is a coherent topic. It detects duplicates and maps the phrase to a clean topic name. This step runs on a smaller, cheaper model. 

 Ranking: Both lists are applied across the ranking funnel. 

 Delivery optimization: Changes reach the feed faster. 

 Validated interests are enriched with an embedding and search keywords. They are saved to a shared store that both Feed and Reels read. A separate component runs integrity and safety checks. 

 How do “Interested In” topics reach the feed? 

 Each interest drives 4 retrieval sources. 2 match content directly: search and clusters of closely related topics. 2 extend reach: the content graph and item-to-item similarity. 

 A relevance check compares the interest’s meaning with each candidate. Passing candidates get a late-stage ranking promotion. A reranking control layer then stops flooding: 

 Repeats of the same interest are spaced out. 

 Each interest’s daily contribution is capped. 

 Retrieval fetches for 1 interest per request. 

 New interests get temporary extra weight. 

 How does “Not Interested In” filtering work? 

 Meta calls this layered filtering at every stage. Ranking uses embedding comparison to remove close matches. Demotion rules push down near matches. A fine-tuned LLM reranker then reviews the final list. 

 Quality requests, such as less AI-generated or sexually suggestive content, take a different path. They map to dedicated demotion signals, not topic matching. Requests naming a creator filter that creator directly. 

 On the client, cache invalidation removes queued items that match a new exclusion before display. 

 Why use a small fine-tuned LLM as the reranker? 

 The reranker is trained to return only the items to remove. Meta says this small fine-tuned model beat a general-purpose model judging each item. It was faster and more reliable. Outputting a short removal list is cheaper than scoring every candidate. 

 Speed comes from a “supplementary tail load.” Adding an interest fires an extra fetch outside the normal cycle. Meta gives no latency figure for it. 

 Back</button><button class="btn" id="ya-next">Next </button></div>
</div>

<div class="pan" data-p="2">
<div class="flow">
<div class="src">
<div class="s"><i>DIRECT</i>Search</div>
<div class="s"><i>DIRECT</i>Related-topic clusters</div>
<div class="s"><i>EXTEND REACH</i>Content graph</div>
<div class="s"><i>EXTEND REACH</i>Item-to-item similarity</div>
</div>
<div class="center"><b id="ya-int">"vintage synthesizers"</b><small>Relevance check, then late-stage promotion</small><div class="btns" style="justify-content:center"><button class="btn" id="ya-run">Run retrieval </button></div></div>
<div class="rules">
<div class="r">Repeats of 1 interest spaced out</div>
<div class="r">Daily contribution per interest capped</div>
<div class="r">1 interest fetched per request</div>
<div class="r">New interests get temporary extra weight</div>
</div>
</div>
<p class="note">Illustrative interest. The 4 sources and 4 controls are from Meta's engineering post.</p>
</div>

<div class="pan" data-p="3">
<div class="layers">
<div class="ly"><span class="nm">Embedding removal</span><div class="bar"><div></div></div><span class="ct">Rank</span></div>
<div class="ly"><span class="nm">Demotion rules</span><div class="bar"><div></div></div><span class="ct">Rank</span></div>
<div class="ly"><span class="nm">LLM reranker</span><div class="bar"><div></div></div><span class="ct">Final</span></div>
<div class="ly"><span class="nm">Cache invalidation</span><div class="bar"><div></div></div><span class="ct">Device</span></div>
</div>
<div class="btns"><button class="btn" id="ya-filter">Animate filter layers </button></div>
<p class="note">Layers show where filtering happens, not measured removal rates. Meta publishes no filtering metrics. The reranker is a small fine-tuned LLM that returns only items to remove.</p>
</div>

<div class="pan" data-p="4">
<div class="scroll"><table>
<tr><th></th><th>Facebook</th><th>Instagram</th><th>Threads</th><th>YouTube</th></tr>
<tr class="hl"><td>Feature</td><td>Your Algorithm</td><td>Your Algorithm</td><td>Dear Algo</td><td>Custom Feeds</td></tr>
<tr><td>Announced</td><td>Oct 13, 2026</td><td>Dec 10, 2025</td><td>Feb 11, 2026</td><td>Sep 23, 2026</td></tr>
<tr><td>Input</td><td>Typed topics, 2 lists</td><td>Add or remove topics</td><td>Public post</td><td>Typed prompt</td></tr>
<tr><td>Duration</td><td>Until edited</td><td>Until edited</td><td>3 days</td><td>30 days inactive</td></tr>
<tr><td>Model named</td><td>Not disclosed</td><td>Not disclosed</td><td>Not disclosed</td><td>Gemini</td></tr>
<tr class="hl"><td>Internals</td><td>Published</td><td>Not disclosed</td><td>Not disclosed</td><td>Not disclosed</td></tr>
</table></div>
<p class="note">TikTok offers slider-based Manage Topics (10+ categories) and an AI-generated content slider.</p>
</div>

<div class="ft"><span>Source: <a href="https://engineering.fb.com/2026/11/10/ml-applications/your-algorithm-giving-people-more-ways-to-personalize-facebook-recommendations/" target="_blank" rel="noopener">Engineering at Meta, Nov 10, 2026</a></span><span class="mtp">Built by Marktechpost</span></div>
<script>
(function(){
var w=document.getElementById('mtp-ya-wrap');
function rs(){try{parent.postMessage({mtpYaHeight:w.offsetHeight+40},'*')}catch(e){}}
var tabs=w.querySelectorAll('.tab'),pans=w.querySelectorAll('.pan');
tabs.forEach(function(t){t.addEventListener('click',function(){tabs.forEach(function(x){x.classList.remove('on')});pans.forEach(function(x){x.classList.remove('on')});t.classList.add('on');w.querySelector('.pan[data-p="'+t.dataset.t+'"]').classList.add('on');if(t.dataset.t==='3')runFilter();setTimeout(rs,60)})});
w.querySelectorAll('.card').forEach(function(c){c.addEventListener('click',function(){c.classList.toggle('open');setTimeout(rs,60)})});
var S=[['Profile generation','An LLM turns regularly refreshed interest signals into readable topic names. It also writes the 1-sentence Lately Summary.'],['Preference management','A smaller, cheaper LLM checks each typed phrase is a coherent topic, detects duplicates and maps it to a clean name. The interest gets an embedding and search keywords, then lands in a shared store read by Feed and Reels. A separate component runs integrity and safety checks.'],['Ranking','Both lists apply across the funnel. Interested In drives 4 retrieval sources and a late-stage promotion. Not Interested In triggers layered filtering, ending in a fine-tuned LLM reranker.'],['Delivery optimization','A supplementary tail load fetches fresh items outside the normal cycle when you add an interest. On-device cache invalidation drops queued items that match a new exclusion.']];
var i=0,box=w.querySelector('#ya-step'),st=w.querySelectorAll('.st');
function draw(){box.innerHTML='<h4>'+S[i][0]+'</h4><p>'+S[i][1]+'</p>';st.forEach(function(s,k){s.className='st'+(k===i?' on':(k<i?' done':''))});box.animate&&box.animate([{opacity:0,transform:'translateX(10px)'},{opacity:1,transform:'none'}],{duration:300});setTimeout(rs,60)}
w.querySelector('#ya-next').onclick=function(){i=(i+1)%4;draw()};
w.querySelector('#ya-prev').onclick=function(){i=(i+3)%4;draw()};
draw();
var ints=['"vintage synthesizers"','"trail running"','"home espresso"'],ii=0;
w.querySelector('#ya-run').onclick=function(){var src=w.querySelectorAll('.s'),rules=w.querySelectorAll('.r');w.querySelector('#ya-int').textContent=ints[ii=(ii+1)%3];rules.forEach(function(r){r.classList.remove('lit')});src.forEach(function(s,k){setTimeout(function(){s.classList.add('pulse')},k*220);setTimeout(function(){s.classList.remove('pulse')},1600+k*220)});rules.forEach(function(r,k){setTimeout(function(){r.classList.add('lit')},900+k*300)})};
function runFilter(){var b=w.querySelectorAll('.bar div');b.forEach(function(x){x.style.width='0'});b.forEach(function(x,k){setTimeout(function(){x.style.width='100%'},150+k*350)})}
w.querySelector('#ya-filter').onclick=runFilter;
window.addEventListener('load',rs);setTimeout(rs,300);
})();
</script>
</div>
</body></html>" style="width:100%;max-width:880px;height:600px;border:0;display:block;margin:0 auto;" loading="lazy" sandbox="allow-scripts allow-popups allow-popups-to-escape-sandbox"> 
 window.addEventListener("message",function(e){if(e.data&&e.data.mtpYaHeight){var f=document.getElementById("mtp-ya-frame");if(f&&e.source===f.contentWindow){f.style.height=e.data.mtpYaHeight+"px";}}}); 

 How does it compare with Instagram, YouTube and TikTok? 

 Feature Facebook Your Algorithm Instagram Your Algorithm Threads Dear Algo YouTube Custom Feeds TikTok Manage Topics Announced Oct 13, 2026 Dec 10, 2025 Feb 11, 2026 Sep 23, 2026 ( TechCrunch ) AIGC slider test: Nov 2025 Input Typed topics, Interested / Not Interested lists View, add or remove topics Public “Dear Algo” post Typed prompt Sliders, 10+ categories Surfaces Feed, Reels Feed, Reels, Explore Threads feed Separate Home tab For You feed Duration Persistent until edited Persistent until edited 3 days ( Engadget ) Expires after 30 days inactive Persistent until edited Model named Not disclosed Not disclosed Not disclosed Gemini Not disclosed Engineering details 4 retrieval sources, LLM reranker, LLM-as-judge Not disclosed Not disclosed Not disclosed Not disclosed Availability Rolling out; regions not disclosed Global, English (June 10, 2026) US, UK, AU, NZ at launch Not disclosed by country Not disclosed by country 

 Source conflict: YouTube’s Help Center says 1 custom feed at a time. TechCrunch reports multiple feeds rolling out from October 2026. 

 Key Takeaways 

 Meta uses LLMs across the full preference lifecycle, from profile to final filter. 

 Each typed interest drives 4 retrieval sources with daily caps. 

 Exclusions pass through embeddings, demotion rules, an LLM reranker and on-device cache. 

 A small fine-tuned reranker beat a general model on speed and reliability. 

 Meta discloses 0 metrics or model names, so claims stay unverified. 

 Check out the Meta engineering post and the Facebook announcement . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Preferences Into Ranking appeared first on MarkTechPost .
