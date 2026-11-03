---
id: "d1a41b63cf9b054f"
title: "The Letter Company Releases Letterpress-1: A Coding Agent Built for Growth Engineering"
url: "https://marktechpost.com/2026/11/02/letter-letterpress-1-growth-engineering-coding-agent"
link: "https://marktechpost.com/2026/11/02/letter-letterpress-1-growth-engineering-coding-agent"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T00:43:03Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Michal Sutter"]
language: "en"
summary: "The Letter Company has released the beta of Letterpress-1 , a coding agent, harness and IDE for growth engineering. The Letterpress-1 coding agent reads a website and its market, then decides what should exist. It builds the change in a sandbox and opens a pull request with a live preview. \n\n TL;DR \n\n Size: Letter team says it combines frontier models with fine-tuned small models; names and…"
tags: ["Agentic AI", "AI Agents", "Context Engineering", "Editors Pick", "For Devs", "Harness", "New Releases", "Software Engineering", "Staff", "Tech News"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "products & launches", "models & research", "chips & infrastructure"]
content_source: "summary"
word_count: 1814
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The Letter Company Releases Letterpress-1: A Coding Agent Built for Growth Engineering

MarkTechPost · Michal Sutter · 2026-11-03

The Letter Company has released the beta of Letterpress-1 , a coding agent, harness and IDE for growth engineering. The Letterpress-1 coding agent reads a website and its market, then decides what should exist. It builds the change in a sandbox and opens a pull request with a live preview. 

 TL;DR 

 Size: Letter team says it combines frontier models with fine-tuned small models; names and sizes are not disclosed. 

 Runs on: Letter’s hosted platform against your git repository. No local GPU needed. Setup takes under 5 minutes, per Letter. 

 Performance: No public benchmark. Letter shows 1 self-reported, side-by-side page build against Codex. 

 Best: 760 tools exposed through 1 registry over MCP, REST and CLI. 

 Worst: No measurable eval; entry plan is $100/month with overage at 5x the list rate. 

 What is Letterpress-1? 

 Letterpress-1 is a growth engineering agent from The Letter Company. It turns site and market signals into pull requests. The letter company team argues that websites, unlike apps, react to outside forces. These include agent behavior, Google rankings, human visits and competitor activity . General coding agents were built to scale codebases, not to act on those signals. 

 The agent is aimed at teams that host their marketing site in git. It is proactive: it suggests the next thing to build. Examples include de-anonymization, landing pages, warmed emails, blog automation and agent telemetry. 

 How does Letterpress-1 work? 

 Letterpress-1 runs in 3 modes : 

 Build: create a page or feature from a prompt, with brand copy and visuals kept consistent. 

 Plan: pick a goal and get a build plan of growth actions. 

 Fix: find site issues and dispatch pull requests to fix them. 

 Every change follows the same loop. The agent reads the site, plans and builds in a sandbox. It reviews its own change, then opens a pull request. Each change returns a preview link of your own site . Nothing lands until you choose a preview, a pull request, or a merge after checks pass. 

 Letter team lists 6 surfaces. These are the web platform, a Slack app, the letterpress CLI and a website portal. A standalone app and your own agent round out the list. The in-site IDE works on a live page. Press ⌘L, edit text where you see it, and a pull request follows. Showcase examples also cover A/B tests from live edits. 

 For developers, agents.md documents an MCP server at app.letterstory.com/api/mcp with OAuth. The MCP manifest, OpenAPI spec and API reference form 1 registry of 760 tools. Claude Code, Codex or any MCP-capable agent can call the same functions the app uses. 

 What are Proofs, Simulations, Benches and Phantoms? 

 The launch post highlights 4 primitives aimed at winning over AI agents as buyers: 

 Proofs: signed evidence of customer success, built from telemetry and billing data, for agent visitors. 

 Simulations: mirror versions of your API or MCP with simulated data, so agents can try before buying. 

 Benches: self-hosted, reproducible benchmark apps with open-source code and independent governance. 

 Phantoms: independent, autonomous blogs used to sandbox growth strategies. 

 The site adds more: Kernels, Letterbases, Visitors and Mailers. Then it watches competitor sitemaps and flag new pages. Letter team positions these as replacements for tools like G2, Semrush, Profound, RB2B and Instantly. 

 Play the loop</button>
 <button class="btn" id="prev">← Back</button>
 <button class="btn" id="next">Next →</button>
 </div>
 </section>

 <section class="panel" id="p-modes" role="tabpanel">
 <div class="modes" id="modes"></div>
 <div class="card mdetail"><span class="tag" id="mtag"></span><p id="mbody" style="margin:6px 0 0"></p></div>
 <div style="margin-top:16px"><span class="tag">Where it runs</span>
 <div class="chips" id="surf"></div>
 <p class="note">Plus ⌘L in-site editing: change text on your live page and a pull request follows. 760 tools are exposed over MCP, REST and CLI.</p>
 </div>
 </section>

 <section class="panel" id="p-prims" role="tabpanel">
 <div class="filters" id="flt"></div>
 <div class="prims" id="prims"></div>
 <div class="card" style="margin-top:12px"><span class="tag" id="ptag">Tap a primitive</span><h3 id="ptitle">Pre-built growth infrastructure</h3><p id="pbody" style="color:var(--muted);margin:0">Each primitive is its own endpoint. The launch post spotlights Proofs, Simulations, Benches and Phantoms.</p></div>
 </section>

 <section class="panel" id="p-calc" role="tabpanel">
 <div class="calc">
 <div>
 <div class="row"><label>Pull requests per month <span class="v" id="vpr"></span></label><input type="range" id="pr" min="0" max="200" value="20"></div>
 <div class="row"><label>Tokens per pull request (Letter cites 150 to 900)</label>
 <div class="seg" id="tpr"><button class="btn" data-v="150" aria-pressed="false">150</button><button class="btn" data-v="500" aria-pressed="true">500</button><button class="btn" data-v="900" aria-pressed="false">900</button></div></div>
 <div class="row"><label>Articles published per month (1,030 tokens each) <span class="v" id="var"></span></label><input type="range" id="ar" min="0" max="60" value="8"></div>
 <div class="row"><label>Phantom sites live (300 tokens a month each) <span class="v" id="vph"></span></label><input type="range" id="ph" min="0" max="10" value="2"></div>
 <div class="row"><label>AI visibility answers (12 tokens each) <span class="v" id="vai"></span></label><input type="range" id="ai" min="0" max="3000" step="50" value="600"></div>
 <div class="row"><label>Identified visitors (25 tokens each) <span class="v" id="vvi"></span></label><input type="range" id="vi" min="0" max="2000" step="25" value="100"></div>
 </div>
 <div class="card">
 <span class="tag">Your month</span>
 <div class="total" id="tok"></div>
 <div style="color:var(--muted);font-size:13px" id="list"></div>
 <div id="bars" style="margin-top:10px"></div>
 <p class="note">1 token = 1 cent at list. Overage on each plan is 5x its own per-token rate. Defaults match Letter's own pricing example. Rates from letter.dev/pricing.</p>
 </div>
 </div>
 </section>

 <div class="ft"><span>Sources: <a href="https://letter.dev/" target="_blank" rel="noopener">letter.dev</a> · <a href="https://letter.dev/pricing" target="_blank" rel="noopener">pricing</a> · <a href="https://letter.dev/agents.md" target="_blank" rel="noopener">agents.md</a></span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
 var R=document.getElementById('lp1x');
 function $(id){return document.getElementById(id)}
 function post(){try{parent.postMessage({lp1xHeight:R.offsetHeight+40},'*')}catch(e){}}
 // tabs
 var tabs=R.querySelectorAll('.tab');
 tabs.forEach(function(t){t.addEventListener('click',function(){
 tabs.forEach(function(x){x.setAttribute('aria-selected',x===t?'true':'false')});
 R.querySelectorAll('.panel').forEach(function(p){p.classList.toggle('on',p.id==='p-'+t.dataset.t)});
 if(t.dataset.t==='calc')calc(); if(t.dataset.t==='modes')renderSurf();
 setTimeout(post,60);
 })});
 // loop
 var S=[
 ['Signals','Read the site and the market','The agent maps your pages and watches outside signals: AI agent visits, Google rankings, human traffic and competitor pages.',['<span class="p">›</span> what should we build for growth?','<span class="dim">reading the site · checking competitor pages</span>']],
 ['Plan','Propose what should exist','In Plan mode it picks a goal and drafts a build plan. You approve the picks you want before anything is built.',['<span class="dim">plan · 4 actions proposed</span>','<span class="dim">waiting on approve</span>']],
 ['Build','Build in a sandbox','The change is written inside an isolated sandbox. Letter says it is tuned to keep brand copy and visuals consistent.',['<span class="dim">building in a sandbox</span>','<span class="dim">changed 3 files</span>']],
 ['Review','Self-review the change','The agent reviews its own diff and fixes what the review finds before handing it over.',['<span class="dim">reviewing the change</span>','<span class="ok">fixed what the review found</span>']],
 ['PR','Open a pull request with a preview','Every change returns as a pull request plus a live preview link of your own site.',['<span class="ok">✓ pull request opened · preview is up</span>']],
 ['You','You decide what lands','Keep it as a preview, leave the pull request open, or merge once checks pass. Nothing lands until you say.',['<span class="p">›</span> merge when checks pass','<span class="ok">✓ queued for merge</span>']]
 ];
 var cur=0,timer=null,typeT=null,lines=[];
 var pipe=$('pipe');
 S.forEach(function(s,i){var b=document.createElement('button');b.className='node';b.innerHTML='<b>'+(i+1)+'</b>'+s[0];b.onclick=function(){stop();go(i)};pipe.appendChild(b)});
 function go(i){
 cur=i;var nodes=pipe.querySelectorAll('.node');
 nodes.forEach(function(n,k){n.classList.toggle('done',k<i);n.classList.toggle('cur',k===i)});
 $('rail').style.width=(i/(S.length-1)*100)+'%';
 $('stag').textContent='Step '+(i+1)+' of 6';$('stitle').textContent=S[i][1];$('sbody').textContent=S[i][2];
 if(i===0)lines=['<span class="dim">~/website $</span> letterpress'];
 type(S[i][3]);
 }
 function type(add){
 clearTimeout(typeT);var k=0,term=$('term');
 function step(){if(k<add.length){lines.push(add[k++]);if(lines.length>7)lines=lines.slice(-7);term.innerHTML=lines.join('<br>')+'<br><span class="cur"></span>';typeT=setTimeout(step,420)}}
 step();
 }
 function stop(){clearInterval(timer);timer=null;$('play').textContent=' Play the loop'}
 $('play').onclick=function(){if(timer){stop();return}if(cur===S.length-1)go(0);$('play').textContent='❚❚ Pause';timer=setInterval(function(){if(cur<S.length-1)go(cur+1);else stop()},1900)};
 $('next').onclick=function(){stop();go(Math.min(cur+1,S.length-1))};
 $('prev').onclick=function(){stop();go(Math.max(cur-1,0))};
 go(0);
 // modes
 var M=[['01','Build','Build anything from a prompt','Create pages and features from plain words. Letter says the agent is fine-tuned to write brand-ready copy and keep brand visuals.'],
 ['02','Plan','Pick a goal, get a plan','Name a goal and Letterpress-1 proposes growth strategies to build straight into your repository, with no extra tools.'],
 ['03','Fix','Find what is broken and fix it','Dispatch pull requests that fix common issues across a marketing site, most severe first.']];
 var mw=$('modes');
 M.forEach(function(m,i){var b=document.createElement('button');b.className='mode';b.innerHTML='<div class="n">'+m[0]+'</div><h3>'+m[1]+'</h3><div style="color:var(--muted);font-size:13px">'+m[2]+'</div>';b.onclick=function(){selM(i)};mw.appendChild(b)});
 function selM(i){mw.querySelectorAll('.mode').forEach(function(x,k){x.classList.toggle('on',k===i)});$('mtag').textContent=M[i][1]+' mode';$('mbody').textContent=M[i][3];post()}
 selM(0);
 var SU=['Letter platform','Slack app','Letterpress CLI','Website portal','Letterpress App','Your own agent via MCP'];
 function renderSurf(){var c=$('surf');c.innerHTML='';SU.forEach(function(s,i){var d=document.createElement('span');d.className='chip';d.style.animationDelay=(i*90)+'ms';d.textContent=s;c.appendChild(d)})}
 renderSurf();
 // primitives
 var P=[
 ['Proofs','conv','Signed proof of customer success','Connect telemetry and billing. Letter issues a third-party verified proof that AI agents can review. You choose what is public.'],
 ['Simulations','conv','Agents try before buying','Mirror versions of your API or MCP with simulated data, so agents can test without touching your database.'],
 ['Benches','conv','Self-governed benchmarks','Describe a benchmark; the app deploys itself, re-runs on a schedule and open-sources its code. The site calls these Benchmarks.'],
 ['Phantoms','geo','Independent sandbox blogs','Launch autonomous publications that write and publish, so you can test growth strategies away from your main site.'],
 ['Letterbases','geo','Native content database','An optional store for content collections that the agent refines without a pull request.'],
 ['Kernels','geo','Writing kernels','Drafting endpoints for content. A kernel draft costs 161 tokens.'],
 ['Visitors','in','Visitor identification','A script that tracks human and AI agent visits per page and de-anonymizes traffic. 25 tokens per identified visitor.'],
 ['Mailers','in','Warmed mailboxes and sequences','Outbound email sequences installed natively. A mailbox costs 300 tokens a month.'],
 ['Seers','watch','Competitor watching','Seers read competitor sitemaps on a schedule and flag new pages for a build to answer.']
 ];
 var G={all:'All',conv:'Agentic conviction',geo:'GEO / SEO',in:'Inbound conversion',watch:'Watching'};
 var RP={conv:'Letter positions these against G2 and Trustpilot.',geo:'Letter positions these against Semrush, Sanity and Profound.',in:'Letter positions these against RB2B and Instantly.',watch:'Listed in agents.md.'};
 var fw=$('flt'),pw=$('prims');
 Object.keys(G).forEach(function(k){var b=document.createElement('button');b.className='btn flt';b.textContent=G[k];b.setAttribute('aria-pressed',k==='all');b.onclick=function(){fw.querySelectorAll('.flt').forEach(function(x){x.setAttribute('aria-pressed',x===b)});pw.querySelectorAll('.prim').forEach(function(p){p.classList.toggle('dim',k!=='all'&&p.dataset.g!==k)})};fw.appendChild(b)});
 P.forEach(function(p,i){var b=document.createElement('button');b.className='prim';b.dataset.g=p[1];b.innerHTML='<small>'+G[p[1]]+'</small><b>'+p[0]+'</b>';b.onclick=function(){pw.querySelectorAll('.prim').forEach(function(x){x.classList.toggle('on',x===b)});$('ptag').textContent=G[p[1]];$('ptitle').textContent=p[0]+': '+p[2];$('pbody').textContent=p[3]+' '+RP[p[1]];post()};pw.appendChild(b)});
 // calculator
 var PL=[['Basic',100,10000,50],['Starter',500,50000,50],['Growth',1000,130000,38.46],['Scale',2500,400000,31.25]];
 var tpr=500;
 $('tpr').querySelectorAll('button').forEach(function(b){b.onclick=function(){tpr=+b.dataset.v;$('tpr').querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});calc()}});
 ['pr','ar','ph','ai','vi'].forEach(function(id){$(id).addEventListener('input',calc)});
 function f(n){return n.toLocaleString('en-US')}
 function calc(){
 var pr=+$('pr').value,ar=+$('ar').value,ph=+$('ph').value,ai=+$('ai').value,vi=+$('vi').value;
 $('vpr').textContent=pr;$('var').textContent=ar;$('vph').textContent=ph;$('vai').textContent=f(ai);$('vvi').textContent=f(vi);
 var t=pr*tpr+ar*1030+ph*300+ai*12+vi*25;
 $('tok').textContent=f(t)+' tokens';$('list').textContent='$'+f(Math.round(t/100))+' at list price';
 var costs=PL.map(function(p){return p[1]+Math.max(0,t-p[2])*p[3]/1000});
 var min=Math.min.apply(null,costs),max=Math.max.apply(null,costs),bi=costs.indexOf(min);
 var h='';PL.forEach(function(p,i){h+='<div class="bar'+(i===bi?' best':'')+'"><div class="lbl"><span>'+p[0]+' · $'+f(p[1])+'/mo, '+f(p[2])+' tokens</span><b>$'+f(Math.round(costs[i]))+(i===bi?' ✓':'')+'</b></div><div class="trk"><i data-w="'+(costs[i]/max*100).toFixed(1)+'"></i></div></div>'});
 $('bars').innerHTML=h;
 requestAnimationFrame(function(){requestAnimationFrame(function(){$('bars').querySelectorAll('i').forEach(function(i){i.style.width=i.dataset.w+'%'})})});
 post();
 }
 calc();
 window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);setTimeout(post,1200);
})();
</script>
</body></html>
"> 

(function(){var f=document.getElementById('lp1x-frame');window.addEventListener('message',function(e){if(e.source===f.contentWindow&&e.data&&e.data.lp1xHeight){f.style.height=Math.ceil(e.data.lp1xHeight)+'px';}});})();

 How does Letterpress-1 compare with Codex, Claude Code and Cursor? 

 Feature Letterpress-1 OpenAI Codex Claude Code Cursor Built for Growth engineering on git-hosted sites General coding General coding General coding (editor and agents) Entry paid plan $100/month, 10,000 tokens Go $8/month; Plus $20/month Pro $20/month ($17 annual) Plus $8/month (Grok models only) Free access 5,000 one-time tokens (6,000 with work email) Free plan, $0 Not in Free plan Free plan, limited agent requests Billing Token pool; agent runs at model cost + 20% Plan limits, credits or API key Shared plan usage or API credits Weekly pool; third-party models at API list price Models Frontier plus fine-tuned small models (not named) GPT-6.1 Sol, GPT-6 Luna and others Opus, Sonnet, Haiku; Fable via credits Grok models; third-party at API price Built-in growth primitives Proofs, Simulations, Benches, Phantoms, Visitors, Mailers, Seers None listed None listed None listed 

 How much does Letterpress-1 cost? 

 Letter bills 1 shared token pool . A token equals 1 cent at list price. Plans are Basic ($100, 10,000 tokens), Starter ($500, 50,000), Growth ($1,000, 130,000) and Scale ($2,500, 400,000). Enterprise starts at 2 million tokens a month at half the list rate. 

 Agent runs cost model spend plus 20%, typically 150 to 900 tokens per pull request. That is $1.50 to $9 at list. A published article costs 1,030 tokens. Overage on Basic and Starter is $50 per 1,000 tokens, 5x the list rate. Unused tokens do not roll over. 

 Key Takeaways 

 Letterpress-1 is a coding agent, harness and IDE built for growth engineering. 

 Every change ships as a sandboxed pull request with a preview link. 

 760 tools are exposed over MCP, REST and CLI for external agents. 

 Pricing starts at $100/month; agent runs cost model spend plus 20%. 

 No public benchmark yet; quality claims are self-reported. 

 Check out the product page , pricing , showcase , agents.md and the launch post on X . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post The Letter Company Releases Letterpress-1: A Coding Agent Built for Growth Engineering appeared first on MarkTechPost .
