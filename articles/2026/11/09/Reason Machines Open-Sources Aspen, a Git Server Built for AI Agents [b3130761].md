---
id: "b3130761a518cd1f"
title: "Reason Machines Open-Sources Aspen, a Git Server Built for AI Agents"
url: "https://marktechpost.com/2026/11/09/reason-machines-aspen-open-source-git-server-ai-agents"
link: "https://marktechpost.com/2026/11/09/reason-machines-aspen-open-source-git-server-ai-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T08:20:20Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Reason Machines has released Aspen , an open-source Git server for AI agent traffic. It targets repositories that hundreds of agents push to at once. Aspen independently implements the design OpenAI described for Pando. \n\n TL;DR \n\n Size: One Rust binary. Branches live in PostgreSQL (or SQLite), packs live in object storage. \n\n Runs on: A laptop ( aspen dev ), one host via Docker Compose, or Helm…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Machine Learning", "Open Source"]
orgs: ["OpenAI", "Cursor"]
topics: ["agents & coding", "models & research", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 1735
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Reason Machines Open-Sources Aspen, a Git Server Built for AI Agents

MarkTechPost · Asif Razzaq · 2026-11-09

Reason Machines has released Aspen , an open-source Git server for AI agent traffic. It targets repositories that hundreds of agents push to at once. Aspen independently implements the design OpenAI described for Pando. 

 TL;DR 

 Size: One Rust binary. Branches live in PostgreSQL (or SQLite), packs live in object storage. 

 Runs on: A laptop ( aspen dev ), one host via Docker Compose, or Helm and Terraform clouds. 

 Performance: Pushes to different branches never wait on each other, and fetches reuse stored packs. 

 Best: 567 pushes per second sustained for 5 minutes on one 8-core server (self-reported). 

 Worst: Landing on main runs at about 4 per second, and the project is pre-alpha. 

 Bottom line: Best: per-branch writes remove the per-repository push ceiling. Worst: no releases, no web UI, and the 24-hour durability gate is not met. 

 What is Aspen? 

 Aspen is a self-hostable Git server from Reason Machines that scales writes per branch, not per repository. It speaks plain Git over HTTPS and SSH. Packs go to S3-compatible object storage; branch history goes to PostgreSQL. 

 Why do classic Git servers struggle with AI agents? 

 An agent pushes every few minutes, and CI fetches after each push. Per Reason Machines , a classic server queues every push to a repository together. It also builds a fresh pack for every fetch. Server work grows with clients, not with new code. 

 OpenAI hit this wall and built Pando. It cut median push latency by nearly 5x and serves nearly a petabyte daily. 

 How does Aspen work? 

 Aspen follows Pando and drops 2 claims most Git servers keep. 

 Per-branch compare-and-swap 

 Each branch is a chain of versions in one Postgres row. A push uploads its pack, then moves the branch with one compare-and-swap. Pushes to different branches never wait for each other. If 2 pushes race on one branch, one wins. The other gets Git’s usual “fetch first” error. The cost: branches may be read at slightly different moments. 

 Stored packs instead of per-client packs 

 Aspen never unpacks a push. It checks the pack, completes missing bases and stores it as-is. A fetch streams stored packs the client lacks, recompressing nothing. Signed URLs can serve packs from a CDN. 

 Trunk-only advertisement and compaction 

 A push sees only the trunk branch, so negotiation stays small with a million branches. Background compaction merges packs 16 at a time, in levels like a log-structured merge tree. A client far behind gets a few dozen packs, not thousands. Depth-1 CI fetches get a tip pack built once and served to every job. 

 Auto play</button></div>
 <svg viewBox="0 0 820 250" aria-label="Aspen push and fetch flow">
 <defs><marker id="aspA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#7cb8f5"/></marker></defs>
 <g font-family="Inter,sans-serif" font-size="13">
 <rect x="20" y="40" width="150" height="60" rx="10" fill="#1d1a12" stroke="#3a3526"/><text x="95" y="66" fill="#f3efe3" text-anchor="middle" font-weight="700">Agent</text><text x="95" y="85" fill="#a59f8c" text-anchor="middle" font-size="11">git push</text>
 <rect x="20" y="150" width="150" height="60" rx="10" fill="#1d1a12" stroke="#3a3526"/><text x="95" y="176" fill="#f3efe3" text-anchor="middle" font-weight="700">CI job</text><text x="95" y="195" fill="#a59f8c" text-anchor="middle" font-size="11">git fetch</text>
 <rect x="320" y="85" width="170" height="80" rx="12" fill="#1d1a12" stroke="#3690ea" stroke-width="1.5"/><text x="405" y="120" fill="#f3efe3" text-anchor="middle" font-weight="800">Aspen</text><text x="405" y="140" fill="#a59f8c" text-anchor="middle" font-size="11">stateless server</text>
 <rect x="640" y="30" width="160" height="70" rx="10" fill="#1d1a12" stroke="#3a3526"/><text x="720" y="60" fill="#f3efe3" text-anchor="middle" font-weight="700">Postgres</text><text x="720" y="80" fill="#a59f8c" text-anchor="middle" font-size="11">1 row per branch</text>
 <rect x="640" y="150" width="160" height="70" rx="10" fill="#1d1a12" stroke="#3a3526"/><text x="720" y="180" fill="#f3efe3" text-anchor="middle" font-weight="700">Object storage</text><text x="720" y="200" fill="#a59f8c" text-anchor="middle" font-size="11">packs as pushed</text>
 <path id="aspE0" d="M170 70 L320 110" stroke="#3a3526" stroke-width="2" fill="none"/>
 <path id="aspE1" d="M490 140 L640 180" stroke="#3a3526" stroke-width="2" fill="none"/>
 <path id="aspE2" d="M490 110 L640 70" stroke="#3a3526" stroke-width="2" fill="none"/>
 <path id="aspE3" d="M320 140 L170 180" stroke="#3a3526" stroke-width="2" fill="none"/>
 <circle id="aspPk" r="7" fill="#3690ea"><animateMotion id="aspMo" dur="1.2s" repeatCount="indefinite"><mpath href="#aspE0"/></animateMotion></circle>
 </g></svg>
 <p class="cap" id="aspCap"></p>
 </div>

 <div class="pane" id="p-race">
 <div class="btns"><button class="b" id="aspRun"> Run 128 writers</button><button class="b" id="aspReset">Reset</button></div>
 <div class="race">
 <div class="rc"><h4>Classic server: one queue per repo</h4><div class="dots" id="aspD1"></div><div class="ct" id="aspC1">0 / 128 done</div></div>
 <div class="rc"><h4>Aspen: one CAS per branch</h4><div class="dots" id="aspD2"></div><div class="ct" id="aspC2">0 / 128 done</div></div>
 </div>
 <p class="note">Toy model, not a benchmark. Amber = waiting, blue = done. Mirrors the illustrative simulation in the Reason Machines launch post.</p>
 </div>

 <div class="pane" id="p-bench">
 <div class="btns"><span class="sub">Pushes per second to one repository, each durable before acknowledgement</span></div>
 <div class="bar"><div class="bl"><span>Cursor Origin, S3 Standard (published)</span><span>120</span></div><div class="tr"><div class="fl" data-w="21.2" style="background:#6d6650"></div></div></div>
 <div class="bar"><div class="bl"><span>Cursor Origin, S3 Express One Zone (published)</span><span>300+</span></div><div class="tr"><div class="fl" data-w="52.9" style="background:#8a8064"></div></div></div>
 <div class="bar"><div class="bl"><span>Aspen, S3 Standard (self-reported)</span><span>567</span></div><div class="tr"><div class="fl" data-w="100" style="background:linear-gradient(90deg,#3690ea,#7cb8f5)"></div></div></div>
 <div class="grid"><div class="st"><div class="n">208 ms</div><div class="l">median push</div></div><div class="st"><div class="n">314 ms</div><div class="l">p99 push</div></div><div class="st"><div class="n">30 ms</div><div class="l">median time to visible</div></div><div class="st"><div class="n">~4/s</div><div class="l">landings on main</div></div><div class="st"><div class="n">1.029x</div><div class="l">depth-1 bytes vs stock git</div></div><div class="st"><div class="n">5 min</div><div class="l">sustained, 0 errors</div></div></div>
 <p class="note">Aspen: 1 x 8-core server, S3 Standard, 4-core Postgres, git.git (~4,500 files, 75k commits), branch-scoped URL. Cursor: replicated cluster on its own monorepo. Setups differ; OpenAI published no Pando push rate.</p>
 </div>

 <div class="pane" id="p-comp">
 <div class="bl"><span>Client is behind trunk by</span><span id="aspBeh">2,000 versions</span></div>
 <input type="range" id="aspSl" min="1" max="4" step="1" value="3">
 <svg viewBox="0 0 820 120" id="aspCS"></svg>
 <p class="cap" id="aspCC"></p>
 </div>

 <div class="pane" id="p-lim">
 <div class="lim">
 <div class="li"><div class="t"> Pre-alpha, no releases</div><div class="d">Build from source. Storage formats may change. The 24-hour chaos run stopped after 11.59 clean hours.</div></div>
 <div class="li"><div class="t"> Landing on main ~4/s</div><div class="d">Separate landings run one at a time, limited by round trips. The merge queue rate is not measured yet.</div></div>
 <div class="li"><div class="t"> Missing Git features</div><div class="d">No partial clones, SHA-256 repositories, web UI or RSA SSH keys (Ed25519 and ECDSA only).</div></div>
 <div class="li"><div class="t"> Force push needs -o force</div><div class="d">Because a push only sees trunk, --force and --delete need an extra -o force, a lease or the branch URL.</div></div>
 <div class="li"><div class="t"> Large monorepos</div><div class="d">Each push still costs more as a repository grows, so very large monorepos see lower rates today.</div></div>
 <div class="li"><div class="t"> Storage support conflict</div><div class="d">The launch post lists Azure Blob; the README says Azure Blob is not supported yet and GCS works via its S3 API.</div></div>
 </div>
 <p class="note">Tap a card to expand.</p>
 </div>

 <div class="ft"><span>Sources: <a href="https://reasonmachines.com/blog/aspen" target="_blank" rel="noopener">launch post</a> · <a href="https://github.com/reason-machines/aspen" target="_blank" rel="noopener">GitHub</a> · <a href="https://cursor.com/blog/git-at-any-scale" target="_blank" rel="noopener">Cursor</a></span><span class="brand">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-aspen');
function post(){try{parent.postMessage({mtpH:R.offsetHeight+40,id:'mtp-aspen'},'*')}catch(e){}}
var tabs=R.querySelectorAll('.tab');
tabs.forEach(function(t){t.onclick=function(){tabs.forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 R.querySelectorAll('.pane').forEach(function(p){p.classList.remove('on')});R.querySelector('#p-'+t.dataset.t).classList.add('on');
 if(t.dataset.t==='bench'){R.querySelectorAll('.fl').forEach(function(f){f.style.width='0';setTimeout(function(){f.style.width=f.dataset.w+'%'},60)})}
 setTimeout(post,80);setTimeout(post,500)}});
/* flow */
var caps=['<b>Push.</b> The agent sends a pack. Aspen checks it, completes missing bases and stores it in object storage exactly as it arrived.',
'<b>Compare-and-swap.</b> One row update: move this branch from A to B only if it still points at A. Other branches never wait.',
'<b>Plan.</b> On fetch, Aspen reads the branch row and works out which stored packs cover what the client is missing.',
'<b>Stream.</b> Stored packs go back stitched into one pack, or as URLs for a CDN. Nothing is recompressed.'];
var edges=['aspE0','aspE2','aspE2','aspE3'],live=['aspE0','aspE1'];
var sb=R.querySelectorAll('#p-flow .b[data-s]'),cur=0,timer=null;
function step(i){cur=i;sb.forEach(function(b){b.classList.toggle('on',+b.dataset.s===i)});
 ['aspE0','aspE1','aspE2','aspE3'].forEach(function(e){R.querySelector('#'+e).setAttribute('stroke','#3a3526')});
 var on=i===0?['aspE0','aspE1']:i===1?['aspE2']:i===2?['aspE2']:['aspE1','aspE3'];
 on.forEach(function(e){R.querySelector('#'+e).setAttribute('stroke','#3690ea')});
 var mp=R.querySelector('#aspMo mpath');mp.setAttribute('href','#'+(i===0?'aspE0':i===3?'aspE3':'aspE2'));
 R.querySelector('#aspCap').innerHTML=caps[i]}
sb.forEach(function(b){b.onclick=function(){clearInterval(timer);timer=null;R.querySelector('#aspAuto').textContent=' Auto play';step(+b.dataset.s)}});
R.querySelector('#aspAuto').onclick=function(){if(timer){clearInterval(timer);timer=null;this.textContent=' Auto play';return}
 this.textContent='❚❚ Pause';timer=setInterval(function(){step((cur+1)%4)},2200)};
step(0);
/* race */
var N=128,d1=R.querySelector('#aspD1'),d2=R.querySelector('#aspD2'),rt=null;
function build(){d1.innerHTML='';d2.innerHTML='';for(var i=0;i<N;i++){d1.insertAdjacentHTML('beforeend','<div class="dot"></div>');d2.insertAdjacentHTML('beforeend','<div class="dot"></div>')}
 R.querySelector('#aspC1').textContent='0 / '+N+' done';R.querySelector('#aspC2').textContent='0 / '+N+' done'}
build();
R.querySelector('#aspReset').onclick=function(){clearInterval(rt);build()};
R.querySelector('#aspRun').onclick=function(){clearInterval(rt);build();var a=d1.children,b=d2.children,k=0,q=0,t=0;
 for(var i=0;i<N;i++){a[i].className='dot w';b[i].className='dot w'}
 rt=setInterval(function(){t++;
 if(q<N){a[q].className='dot d';q++;R.querySelector('#aspC1').textContent=q+' / '+N+' done'}
 for(var j=0;j<10&&k<N;j++){b[k].className='dot d';k++}R.querySelector('#aspC2').textContent=k+' / '+N+' done';
 if(q>=N)clearInterval(rt)},45)};
/* compaction */
var lv={1:20,2:200,3:2000,4:20000};
function plan(n){var out=[];[4096,256,16,1].forEach(function(s){while(n>=s){out.push(s);n-=s}});return out}
function comp(){var n=lv[R.querySelector('#aspSl').value],ps=plan(n),s=R.querySelector('#aspCS'),x=10,h='';
 var tot=ps.reduce(function(a,b){return a+Math.log2(b)+1.5},0);
 ps.forEach(function(p,i){var w=(Math.log2(p)+1.5)/tot*800;h+='<rect x="'+x+'" y="30" width="'+Math.max(w-3,2)+'" height="50" rx="4" fill="'+(p>=4096?'#7cb8f5':p>=256?'#3690ea':p>=16?'#2f6fb3':'#5a5440')+'"><animate attributeName="opacity" from="0" to="1" dur=".35s" begin="'+(i*0.04)+'s" fill="freeze"/></rect>';x+=w});
 h+='<text x="10" y="105" fill="#a59f8c" font-family="Inter" font-size="11">client</text><text x="810" y="105" fill="#a59f8c" font-family="Inter" font-size="11" text-anchor="end">trunk</text>';
 s.innerHTML=h;R.querySelector('#aspBeh').textContent=n.toLocaleString()+' versions';
 R.querySelector('#aspCC').innerHTML='Illustrative plan: <b>'+ps.length+' packs</b> instead of '+n.toLocaleString()+'. Packs merge 16 at a time into 4 sizes (1, 16, 256, 4,096 here), and a fetch takes the largest pack that fits at each step.'}
R.querySelector('#aspSl').oninput=comp;comp();
/* limits */
R.querySelectorAll('.li').forEach(function(l){l.onclick=function(){l.classList.toggle('open');setTimeout(post,400)}});
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body></html>
"> 

window.addEventListener("message",function(e){if(e.data&&e.data.id==="mtp-aspen"&&e.data.mtpH){var f=document.getElementById("mtp-aspen-frame");if(f)f.style.height=e.data.mtpH+"px";}});
 
 #mtp-aspen-wrap p:empty,#mtp-aspen-wrap hr,#mtp-aspen-wrap del,#mtp-aspen-wrap s{display:none!important} 

 How fast is Aspen? 

 The test used one 8-core server, S3 Standard and a 4-core Postgres. The target was a copy of git.git, about 4,500 files and 75,000 commits. Aspen sustained 567 pushes per second for 5 minutes with no errors. Each push reached S3 and Postgres before Git printed “ok.” 

 Median push latency: 208 ms; 99th percentile: 314 ms. 

 Another client saw each push 30 ms after acknowledgement, at the median. 

 Depth-1 fetch storm: 1.029x the bytes of stock git upload-pack on git.git. 

 Cursor reports up to 120 pushes per second for Origin on S3 Standard. On S3 Express One Zone it exceeds 300. That is a replicated cluster on Cursor’s monorepo, so setups differ. The README calls Aspen’s figures indicative, not performance claims. 

 How does Aspen compare with other agent-scale Git backends? 

 Feature Aspen Cursor Origin OpenAI Pando GitHub Spokes Availability Open source, self-hosted Commercial Cursor platform Internal to OpenAI Internal to GitHub License Apache 2.0 Not disclosed Not disclosed Not disclosed Push ordering Per branch (compare-and-swap) Per repository (write-ahead log in S3) Per branch Three-phase commit across replicas Ref storage PostgreSQL or SQLite WAL index in S3, no relational DB Metadata store Git repos on NVMe Fetch serving Stored packs, stitched or via URIs Local Git repo cache on NVMe Reused stored packs Git repo replicas Published push rate 567/s, S3 Standard, 1 server (self-reported) 120/s S3 Standard; 300+/s S3 Express Not disclosed Not disclosed Other published result p99 push 314 ms Linear read scaling to 100 replicas Median push latency cut nearly 5x Not disclosed 

 How do you deploy Aspen? 

 You build from source with Rust. aspen dev runs everything with SQLite and a local directory. Teams get Docker Compose with PostgreSQL and MinIO, plus a Helm chart. Terraform covers AWS, Google Cloud, Azure and Hetzner. Mirror mode fronts GitHub or GitLab, so you can trial it without migrating. 

 The live demo is a 64 x 64 pixel canvas where each click is one pushed commit. Per the company, one Reason agent built Aspen from first commit to public in 4 days. That took 151 merged PRs. 

 Key Takeaways 

 Aspen is an Apache 2.0 Git server built for agent-scale push traffic. 

 It is an independent, open implementation of OpenAI’s Pando design. 

 Self-reported: 567 pushes per second on one 8-core server, p99 314 ms. 

 Clients need no changes; stock git works over HTTPS and SSH. 

 Check out the GitHub repo and the launch post . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Reason Machines Open-Sources Aspen, a Git Server Built for AI Agents appeared first on MarkTechPost .
