---
id: "975377beb2f4474c"
title: "You.com Launches Inference Router: 12 Open-Weight Models With 99.9% Uptime SLA"
url: "https://marktechpost.com/2026/10/22/you-com-inference-router-open-weight-models-uptime-sla"
link: "https://marktechpost.com/2026/10/22/you-com-inference-router-open-weight-models-uptime-sla"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T05:28:21Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "You.com has launched Inference Router , a managed API for running open-weight models in production. The You.com Inference Router is an OpenAI-compatible service that routes requests across 12 live models. It bundles a 99.9% minimum uptime SLA and zero data retention (ZDR). It adds 100% US hosting and server-side web search. It is pay-as-you-go, with no platform fee. \n\n TL;DR \n\n Size: 12 live…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "New Releases", "Software Engineering", "Staff"]
orgs: ["OpenAI", "Alibaba", "Anthropic", "Meta", "DeepSeek"]
topics: ["search & media", "models & research", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 1661
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# You.com Launches Inference Router: 12 Open-Weight Models With 99.9% Uptime SLA

MarkTechPost · Asif Razzaq · 2026-10-23

You.com has launched Inference Router , a managed API for running open-weight models in production. The You.com Inference Router is an OpenAI-compatible service that routes requests across 12 live models. It bundles a 99.9% minimum uptime SLA and zero data retention (ZDR). It adds 100% US hosting and server-side web search. It is pay-as-you-go, with no platform fee. 

 TL;DR 

 Size: 12 live models, from GPT-OSS 120B (125K context) to Kimi K3 and Qwen3.8 Max (1M context). Kimi K3 is a 2.8T-parameter model; Qwen3.8 Max is a 2.4T MoE. 

 Runs on: Fully managed. Requests hit You.com Inference Direct first, then fail over to US-hosted partners. No GPUs to manage. 

 Performance: On You.com’s LiveNewsBench run, open-weight models plus You.com search matched frontier models at lower cost. 

 Best: GLM-5.3 with You.com search scored 86.53%, at $0.0485 per question versus $0.0920 for Claude Sonnet 5.5 (self-reported). 

 Worst: Per-token prices sit near market. Kimi K3 is $2.85/$14.25, only 5% below Together AI’s $3.00/$15.00. 

 What is You.com Inference Router? 

 It is one API for many open-weight models. The endpoint is https://api.you.com , with OpenAI-compatible and Anthropic-compatible routes . Existing SDK code moves over by changing the base URL and key. 

 You.com team frames the problem around stalled migrations. Dev teams test open-weight models on aggregators, then hit security review. Reviewers ask about ZDR, US hosting, access controls and DPAs. Dedicated providers clear those bars, but usually with a large commitment. Inference Router targets that gap. 

 How does the routing and failover work? 

 Every request goes first to You.com Inference Direct , the company’s own inference capacity. If it is down or full, the request fails over to a vetted partner. The official post names Parasail, Wafer, Alibaba Cloud, Meta and Inception, with Prime Intellect coming soon. All are 100% US-hosted and must meet ZDR rules. 

 Failover does not change the bill. Each model has 1 published per-token price. You.com also offers spend caps per API key and daily usage views by model, cost and provider. Accounts run on SOC 2 compliant infrastructure, with a DPA on request. 

 What does zero data retention cover? 

 The ZDR policy states that prompts and outputs are processed in memory and not stored. It covers both model calls and web search requests. You.com keeps only operational metadata, such as token counts, timestamps and account IDs. Prompt hashes, de-identified text and disk-backed prompt caches are explicitly excluded. 

 Which models are available, and what do they cost? 

 The models page lists 12 live models, all US-hosted. Prices are per 1M tokens (input / output): 

 Kimi K3 (Moonshot AI): $2.85 / $14.25, 1M context 

 Qwen3.8 Max (Alibaba): $1.85 / $5.55, 1M context 

 GLM 5.3 (Z.ai): $1.35 / $4.25, 1M context 

 DeepSeek V4 Pro : $1.65 / $3.65, 1M context 

 DeepSeek V4.1 Flash : $0.30 / $1.20, 1M context 

 Mercury 3 (Inception): $0.10 / $0.35, 1M context 

 GPT-OSS 120B (OpenAI): $0.097 / $0.73, 125K context 

 Muse Wonder, Muse Spark 1.3, GLM 5.3 Flash, Qwen3.8 Flash and MiniMax M3 round out the list. 

 How does built-in web search work? 

 Developers declare a web_search or web_extract tool, and the router runs searches for the model. The docs show up to 20 results per search and a default of 30 search rounds. Responses return a web_results object with citations. 

 Search runs on the same server as the model. You.com says internal tests show up to 15% lower latency. 

 Send request</button>
 <button class="btn" id="ydcSearch">＋ With web_search</button>
 <button class="btn" id="ydcFail"> Simulate outage</button>
 <span class="status" id="ydcStat">idle</span>
 </div>
 </div>
 <div class="grid3">
 <div class="stat"><b>≥99.9%</b><span>Uptime SLA with service credits</span></div>
 <div class="stat"><b>0%</b><span>Platform fee (OpenRouter: 5.5%)</span></div>
 <div class="stat"><b>Up to 15%</b><span>Lower latency, server-side search (internal test)</span></div>
 </div>
 <p class="note">Failover partners named in the launch post: Parasail, Wafer, Alibaba Cloud, Meta, Inception; Prime Intellect coming soon. Failover never changes the price.</p>
 </div>

 <!-- 1: models -->
 <div class="pn" data-p="1">
 <div class="seg" id="ydcSeg"><button class="on" data-m="in">Input $/1M</button><button data-m="out">Output $/1M</button></div>
 <div class="rows" id="ydcModels"></div>
 <p class="note">Prices per 1M tokens from you.com/product/inference-router/models, checked Oct 22, 2026. All models US-hosted with ZDR.</p>
 </div>

 <!-- 2: benchmarks -->
 <div class="pn" data-p="2">
 <div class="seg" id="ydcBseg"><button class="on" data-m="acc">Accuracy</button><button data-m="cost">Cost per question</button></div>
 <div class="rows" id="ydcBench"></div>
 <p class="note">LiveNewsBench, 1,329 questions, list prices. Accuracy bars start at 80%. You.com's own Oct 2026 run using Braintrust's open-source search eval (self-reported). Purple = open-weight + You.com search; grey = closed model with built-in search.</p>
 </div>

 <!-- 3: compare -->
 <div class="pn" data-p="3">
 <div class="tw"><table>
 <thead><tr><th></th><th>You.com</th><th>OpenRouter</th><th>Together AI</th><th>Fireworks AI</th></tr></thead>
 <tbody>
 <tr class="hl"><td>Uptime SLA</td><td>≥99.9%, pay-as-you-go</td><td>Not disclosed</td><td>Best-effort; 99% with PTU commit</td><td>Not disclosed</td></tr>
 <tr class="hl"><td>ZDR</td><td>Default, models + search</td><td>No prompt logging default</td><td>Off by default</td><td>On by default (open models)</td></tr>
 <tr class="hl"><td>Platform fee</td><td>0%</td><td>5.5%</td><td>None listed</td><td>None listed</td></tr>
 <tr class="hl"><td>Kimi K3 in/out</td><td>$2.85 / $14.25</td><td>Varies by provider</td><td>$3.00 / $15.00</td><td>$3.00 / $15.00 (US-only $4.50 / $22.50)</td></tr>
 <tr class="hl"><td>US hosting</td><td>100% incl. failover</td><td>Varies</td><td>Not disclosed</td><td>US tier at premium</td></tr>
 </tbody>
 </table></div>
 <p class="note">Sources: openrouter.ai/docs/faq, together.ai/pricing, docs.together.ai, docs.fireworks.ai/serverless/pricing. Checked Oct 22, 2026.</p>
 </div>

 <!-- 4: quickstart -->
 <div class="pn" data-p="4">
 <div class="steps"><button class="btn" data-s="0">1 · Install</button><button class="btn" data-s="1">2 · Change base URL</button><button class="btn" data-s="2">3 · Add search</button></div>
 <pre><code id="ydcCode"></code></pre>
 <p class="stepTxt" id="ydcStep"></p>
 </div>

 <div class="ft"><span>Sources: you.com launch post, model page, docs · Numbers self-reported where noted</span><a href="https://www.marktechpost.com" target="_blank" rel="noopener">© Marktechpost</a></div>
</div>
<script>
(function(){
var R=document.getElementById('ydc-ir');
function post(){try{parent.postMessage({ydcH:R.offsetHeight+40},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.onclick=function(){
 R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 R.querySelectorAll('.pn').forEach(function(p){p.classList.toggle('on',p.dataset.p==t.dataset.t)});
 if(t.dataset.t=='0')layout(); if(t.dataset.t=='1')drawM(); if(t.dataset.t=='2')drawB(); if(t.dataset.t=='4')step(0);
 setTimeout(post,60);}});
/* routing */
var F=document.getElementById('ydcFlow'),W=document.getElementById('ydcWires'),ST=document.getElementById('ydcStat');
var N={app:'n-app',r:'n-r',s:'n-s',d:'n-d',p:'n-p'},down=false,busy=false;
function el(k){return document.getElementById(N[k])}
function layout(){var w=F.clientWidth,h=F.clientHeight,m=w<520;
 var pos=m?{app:[.5,.07],r:[.5,.38],s:[.5,.66],d:[.22,.93],p:[.78,.93]}:{app:[.1,.5],r:[.42,.5],s:[.42,.12],d:[.82,.25],p:[.82,.78]};
 for(var k in pos){var e=el(k);e.style.left=(pos[k][0]*w-e.offsetWidth/2)+'px';e.style.top=(pos[k][1]*h-e.offsetHeight/2)+'px'}
 wires();}
function c(k){var e=el(k);return[e.offsetLeft+e.offsetWidth/2,e.offsetTop+e.offsetHeight/2]}
function wires(){W.querySelectorAll('path').forEach(function(p){p.remove()});
 [['app','r'],['r','s'],['r','d'],['r','p']].forEach(function(pr){var a=c(pr[0]),b=c(pr[1]),p=document.createElementNS('http://www.w3.org/2000/svg','path');
 p.setAttribute('d','M'+a[0]+' '+a[1]+' L'+b[0]+' '+b[1]);p.setAttribute('class','w');p.id='w-'+pr[0]+pr[1];W.appendChild(p)})}
function clear(){R.querySelectorAll('.node').forEach(function(n){n.classList.remove('hot','fo')});W.querySelectorAll('.w').forEach(function(w){w.classList.remove('act')})}
function hot(k,cls){el(k).classList.add(cls||'hot')}
function wire(id){var w=document.getElementById('w-'+id);if(w)w.classList.add('act')}
function run(search){if(busy)return;busy=true;clear();var t=0,seq=[];
 seq.push(function(){hot('app');wire('appr');ST.textContent='request → router'});
 seq.push(function(){hot('r')});
 if(search)seq.push(function(){wire('rs');hot('s');ST.textContent='web_search runs server-side'});
 if(!down)seq.push(function(){wire('rd');hot('d');ST.textContent='served by Inference Direct · ZDR'});
 else{seq.push(function(){ST.textContent='Inference Direct unavailable…'});
 seq.push(function(){wire('rp');hot('p','fo');ST.textContent='auto-failover to US partner · same price'})}
 seq.push(function(){busy=false});
 seq.forEach(function(f){setTimeout(f,t);t+=650})}
document.getElementById('ydcSend').onclick=function(){run(false)};
document.getElementById('ydcSearch').onclick=function(){run(true)};
document.getElementById('ydcFail').onclick=function(){down=!down;el('d').classList.toggle('down',down);this.textContent=down?'✓ Restore capacity':' Simulate outage';ST.textContent=down?'Inference Direct: down':'Inference Direct: up'};
window.addEventListener('resize',function(){layout();post()});
/* models */
var M=[['Kimi K3','Moonshot AI · 1M',2.85,14.25],['Muse Wonder','Meta · 1M',4.00,20.00],['Qwen3.8 Max','Alibaba · 1M',1.85,5.55],['DeepSeek V4 Pro','DeepSeek · 1M',1.65,3.65],['GLM 5.3','Z.ai · 1M',1.35,4.25],['Muse Spark 1.3','Meta · 1M',1.25,4.25],['DeepSeek V4.1 Flash','DeepSeek · 1M',0.30,1.20],['MiniMax M3','MiniMax · 512K',0.29,1.16],['GLM 5.3 Flash','Z.ai · 1M',0.14,0.48],['Qwen3.8 Flash','Alibaba · 1M',0.14,0.43],['Mercury 3','Inception · 1M',0.10,0.35],['GPT-OSS 120B','OpenAI · 125K',0.097,0.73]];
var mode='in',MB=document.getElementById('ydcModels');
function drawM(){var i=mode=='in'?2:3,mx=Math.max.apply(null,M.map(function(r){return r[i]}));
 var s=M.slice().sort(function(a,b){return b[i]-a[i]});
 MB.innerHTML=s.map(function(r){return '<div class="row"><div class="nm">'+r[0]+'<small>'+r[1]+'</small></div><div class="bar"><i data-w="'+(r[i]/mx*100)+'"></i></div><div class="val">$'+r[i].toFixed(r[i]<0.1?3:2)+'</div></div>'}).join('');
 requestAnimationFrame(function(){MB.querySelectorAll('i').forEach(function(x){x.style.width=x.dataset.w+'%'})});post()}
R.querySelectorAll('#ydcSeg button').forEach(function(b){b.onclick=function(){R.querySelectorAll('#ydcSeg button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');mode=b.dataset.m;drawM()}});
/* bench */
var B=[['GPT-6.1 Sol','built-in search',86.53,0.0591,0],['GLM-5.3','+ You.com search',86.53,0.0485,1],['Claude Sonnet 5.5','built-in search',86.38,0.0920,0],['DeepSeek V4.1 Flash','+ You.com search',84.12,0.0215,1]];
var bm='acc',BB=document.getElementById('ydcBench');
function drawB(){BB.innerHTML=B.map(function(r){var v=bm=='acc'?r[2]:r[3],w=bm=='acc'?(r[2]-80)/(90-80)*100:r[3]/0.0920*100;
 return '<div class="row"><div class="nm">'+r[0]+'<small>'+r[1]+'</small></div><div class="bar"><i class="'+(r[4]?'':'alt')+'" data-w="'+w+'"></i></div><div class="val">'+(bm=='acc'?v.toFixed(2)+'%':'$'+v.toFixed(4))+'</div></div>'}).join('');
 requestAnimationFrame(function(){BB.querySelectorAll('i').forEach(function(x){x.style.width=x.dataset.w+'%'})});post()}
R.querySelectorAll('#ydcBseg button').forEach(function(b){b.onclick=function(){R.querySelectorAll('#ydcBseg button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');bm=b.dataset.m;drawB()}});
/* quickstart */
var CODE=[
 '<span class="c"># Use the standard OpenAI SDK</span>\npip install openai',
 '<span class="k">from</span> openai <span class="k">import</span> OpenAI\n\nclient = OpenAI(\n<span class="hlline"> base_url=<span class="s">"https://api.you.com/v1"</span>, <span class="c"># the only line you change</span></span>\n api_key=<span class="s">"YDC_API_KEY"</span>,\n)\n\nresp = client.chat.completions.create(\n model=<span class="s">"kimi-k3"</span>,\n messages=[{<span class="s">"role"</span>: <span class="s">"user"</span>, <span class="s">"content"</span>: <span class="s">"Hello"</span>}],\n)',
 'resp = client.chat.completions.create(\n model=<span class="s">"kimi-k3"</span>,\n messages=[{<span class="s">"role"</span>: <span class="s">"user"</span>,\n <span class="s">"content"</span>: <span class="s">"What changed in the latest Python release?"</span>}],\n<span class="hlline"> tools=[{<span class="s">"type"</span>: <span class="s">"web_search"</span>, <span class="s">"freshness"</span>: <span class="s">"month"</span>, <span class="s">"count"</span>: 5}],</span>\n)\n<span class="c"># answer + citations come back in resp.web_results</span>'];
var TXT=['Inference Router speaks the OpenAI and Anthropic API formats, so existing SDKs work.','Swap the base URL and key. Your existing OpenAI-compatible code now runs on Inference Router.','Declare a web_search tool and the router runs searches server-side, returning sources in web_results.'];
function step(i){document.getElementById('ydcCode').innerHTML=CODE[i];document.getElementById('ydcStep').textContent=TXT[i];
 R.querySelectorAll('.steps .btn').forEach(function(b){b.style.borderColor=b.dataset.s==i?'#7b6cff':''});post()}
R.querySelectorAll('.steps .btn').forEach(function(b){b.onclick=function(){step(+b.dataset.s)}});
layout();setTimeout(function(){layout();post()},300);window.addEventListener('load',post);post();
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(e){if(e.data&&e.data.ydcH){var f=document.getElementById('ydc-ir-frame');if(f&&e.source===f.contentWindow){f.style.height=e.data.ydcH+'px';}}});

 What do the benchmarks show? 

 You.com reports a LiveNewsBench run of 1,329 questions, using Braintrust’s open-source search eval . These numbers are self-reported: 

 Setup Accuracy Mean cost per question GPT-6.1 Sol, built-in search 86.53% $0.0591 GLM-5.3 + You.com search 86.53% $0.0485 Claude Sonnet 5.5, built-in search 86.38% $0.0920 DeepSeek V4.1 Flash + You.com search 84.12% $0.0215 

 DeepSeek V4.1 Flash costs about 77% less per question than Claude Sonnet 5.5. It trails by 2.26 points. 

 Braintrust’s own August study used older models. There, DeepSeek V4 Flash with You.com search hit 80.66% at $0.0163 per question. Claude Sonnet 5 with built-in search scored 78.78% at $0.1148. 

 You.com also cites joint work with NVIDIA and CoreWeave. Post-training Nemotron 3.5 Lightning with You.com search in the loop lifted BrowseComp from 36.97% to 45.45%. Tool calls fell by 30%. 

 How does it compare with OpenRouter, Together AI and Fireworks AI? 

 Metrics You.com Inference Router OpenRouter Together AI (serverless) Fireworks AI (serverless) Model Own capacity first, partner failover Aggregator across third-party providers Own inference cloud Own inference cloud Uptime SLA At least 99.9%, with credits, on pay-as-you-go Not disclosed; automatic fallback Best-effort; 99% request SLA only with provisioned throughput (1-month minimum) Not disclosed Zero data retention Default, models and web search No prompt logging by default; provider policies vary Off by default ; admin enables On by default for open models US hosting 100%, including failover Varies by provider Not disclosed for serverless US-only tier at a premium Platform fee 0% 5.5% on credit purchases ($0.80 minimum) None listed None listed Kimi K3 (in / out per 1M) $2.85 / $14.25 $0.238 / $16 up to $4.50 / $22.50, by provider $3.00 / $15.00 $3.00 / $15.00; US-only $4.50 / $22.50 DeepSeek V4.1 Flash (in / out per 1M) $0.30 / $1.20 Not checked $0.30 / $1.20 $0.30 / $1.20; US-only $0.45 / $1.80 Server-side web search Yes, same server as model Server tool, third-party search Not disclosed Third-party search providers 

 The clearest price win is versus Fireworks’ US-only tier. There, You.com is about 37% cheaper on Kimi K3 input. 

 Key Takeaways 

 12 open-weight models behind 1 OpenAI-compatible base URL. 

 At least 99.9% uptime SLA on pay-as-you-go, with credits. 

 ZDR covers both model calls and web search. 

 0% platform fee versus OpenRouter’s 5.5%. 

 Token prices are near market; the value is in guarantees. 

 Check out the launch post , browse the model list and check the developer docs . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post You.com Launches Inference Router: 12 Open-Weight Models With 99.9% Uptime SLA appeared first on MarkTechPost .
