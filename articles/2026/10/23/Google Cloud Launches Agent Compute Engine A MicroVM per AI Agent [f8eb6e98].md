---
id: "f8eb6e980e5dcd38"
title: "Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent"
url: "https://marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents"
link: "https://marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T06:05:10Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google Cloud has announced Agent Compute Engine , a compute service built specifically for AI agents. Google Agent Compute Engine gives each agent its own hardware-isolated microVM. The sandbox holds zero credentials. The service already powers Gemini as an agent for work tasks. Google unveiled it this week at AGNTCon + MCPCon. Customer preview is targeted for the coming months. The pitch:…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "Harness", "Language Model", "Large Language Model", "Machine Learning"]
orgs: ["Google"]
topics: ["agents & coding", "chips & infrastructure", "models & research"]
content_source: "summary"
word_count: 1871
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent

MarkTechPost · Michal Sutter · 2026-10-23

Google Cloud has announced Agent Compute Engine , a compute service built specifically for AI agents. Google Agent Compute Engine gives each agent its own hardware-isolated microVM. The sandbox holds zero credentials. The service already powers Gemini as an agent for work tasks. Google unveiled it this week at AGNTCon + MCPCon. Customer preview is targeted for the coming months. The pitch: VM-grade isolation with container-like speed and density. 

 TL;DR 

 Unit: One hardware-isolated microVM per agent session, with its own guest kernel, root access and Hyperdisk. 

 Runs on: Google-managed hosts using Titan silicon and the Titanium IPU. Open-source sibling Agent Substrate runs on any Kubernetes cluster. 

 Performance: Idle agents are checkpointed to zero active resources and resumed from snapshots. Google gives no ACE boot or density numbers. 

 Best: Agent Substrate hit 500 activations/s at under 500 ms suspend/resume across 200,000 agents. 

 Worst: No published boot time, density, pricing or preview date for Agent Compute Engine itself. 

 What is Google Agent Compute Engine? 

 Agent Compute Engine is a Google Cloud service that runs each AI agent inside a dedicated microVM. Per the technical post , it powers Gemini, Antigravity, and internal evaluation and RL pipelines. 

 Google splits every agent into 2 parts. The harness, or ‘brain,’ calls the model. The sandbox, or ‘hands,’ runs code, shell commands and browsers. The harness runs fully outside the sandbox and dispatches explicit commands into it. 

 How does the microVM isolation work? 

 Each session runs in a single-tenant microVM behind a Cloud Hypervisor boundary . Hosts are stateless appliances with a read-only root filesystem enforced by dm-verity. Titanium holds attestation keys outside the guest. 

 The networking design is the unusual part: 

 MicroVMs have no standard network interface, no default gateway and no direct VPC access. 

 All traffic crosses a virtio-vsock boundary to a local proxy, then to an external gateway. 

 Guests get only a session-scoped SPIFFE certificate and a short-lived identity token. 

 Agent Gateway swaps in the real backend credential in flight, after policy checks. 

 Google assumes an attacker controls everything inside the sandbox. A prompt-injected agent finds no secrets to steal. 

 What are the Four Agent Identities? 

 Google defines 4 identities for every agent workload: 

 User identity: authenticates the overall task only. 

 Delegated on-behalf-of identity: a scoped grant stored in a central authorization service, never on the node. 

 Agent Workload Identity: a short-lived SPIFFE identity, the only one used for sandbox traffic. 

 Agent Workforce Identity: an agent’s own account and resources. 

 The workload identity is useless for direct API calls if exfiltrated. It only identifies which sandbox sent a packet. 

 How does it keep idle agents cheap? 

 Google team found agents spend most of their time waiting on models or users. So the sandbox signals when a tool call finishes. The host checkpoints the idle microVM to zero active resources. It resumes on the next call. 

 Density comes from copy-on-write memory sharing . Pre-warmed snapshot images are mapped with DAX, so microVMs on a host share base OS and library pages. Only each agent’s modified pages consume private memory. Harnesses also get cloning, snapshot/forking, rewind and rollback. 

 Storage is split 3 ways: disposable scratch overlays, shared read-only volumes, and persistent user workspaces on Hyperdisk . 

 </b>Harness<span class="zone z-out">outside</span></div>
 <div class="node"><b> </b>Sandbox microVM<span class="zone z-in">untrusted</span></div>
 <div class="node"><b> </b>vsock + local proxy<span class="zone z-out">host</span></div>
 <div class="node"><b> </b>Agent Gateway<span class="zone z-out">off-node</span></div>
 <div class="node"><b> </b>Token swap<span class="zone z-out">off-node</span></div>
 <div class="node"><b> </b>Backend<span class="zone z-out">Workspace / VPC</span></div>
 </div>
 <div class="track"><span id="ace-fill"></span><i class="pkt" id="ace-pkt"></i></div>
 <div class="card"><h4 id="ace-st">Step 1</h4><p id="ace-sd"></p></div>
 <div class="ctl">
 <button class="btn" id="ace-prev"> Back</button>
 <button class="btn pri" id="ace-next">Next step </button>
 <button class="btn" id="ace-play"> Auto-play</button>
 </div>
 <p class="note">Source: Google Cloud technical deep dive, Oct 22, 2026.</p>
 </div>

 <div class="pane" data-p="1">
 <div class="life" id="ace-life">
 <div class="st"><div class="lb">State 1</div><div class="nm">Running tool call</div><div class="meter"><span style="width:100%;background:#34A853"></span></div><div class="ds">Code, shell or browser executes inside the microVM.</div></div>
 <div class="st"><div class="lb">State 2</div><div class="nm">"Thinking" signal</div><div class="meter"><span style="width:55%;background:#FBBC04"></span></div><div class="ds">Sandbox reports no commands or background tasks in flight.</div></div>
 <div class="st"><div class="lb">State 3</div><div class="nm">Checkpointed idle</div><div class="meter"><span style="width:0%;background:#4285F4"></span></div><div class="ds">State preserved. Zero active host resources.</div></div>
 <div class="st"><div class="lb">State 4</div><div class="nm">Resume</div><div class="meter"><span style="width:100%;background:#34A853"></span></div><div class="ds">Next tool call restores the microVM from its snapshot.</div></div>
 </div>
 <div class="card">
 <h4>Copy-on-write memory, shared across 6 microVMs</h4>
 <div class="mem" id="ace-mem"></div>
 <div class="shared" id="ace-shared">1 shared copy of base OS, libraries and binaries (DAX + CoW)</div>
 <div class="legend"><span><i style="background:#4285F4"></i>Base image pages</span><span><i style="background:#FBBC04"></i>Private pages the agent modified</span></div>
 <div class="ctl"><button class="btn pri" id="ace-cow">Turn on CoW sharing</button><button class="btn" id="ace-cycle"> Run idle cycle</button></div>
 </div>
 <p class="note">Bar heights are illustrative. Google discloses no per-host density figure for Agent Compute Engine.</p>
 </div>

 <div class="pane" data-p="2">
 <div class="ids">
 <button class="id"><div class="n">ID 1</div><div class="t">User identity</div><div class="w" style="color:#4285F4">Starts the task</div><div class="more">The authenticated user who initiated the request. Used only to authenticate the overall task, never for agentic operations.</div></button>
 <button class="id"><div class="n">ID 2</div><div class="t">Delegated on-behalf-of</div><div class="w" style="color:#FBBC04">Lives in central auth service</div><div class="more">A cryptographically scoped grant proving the user authorized the harness. These long-lived grants never sit on the compute node.</div></button>
 <button class="id key"><span class="badge">Only ID in sandbox</span><div class="n">ID 3</div><div class="t">Agent Workload Identity</div><div class="w" style="color:#34A853">Short-lived SPIFFE ID</div><div class="more">Assigned when the microVM spins up. Identifies which sandbox sent a packet. Useless for direct backend calls if exfiltrated.</div></button>
 <button class="id"><div class="n">ID 4</div><div class="t">Agent Workforce Identity</div><div class="w" style="color:#EA4335">Agent's own account</div><div class="more">Lets an agent act as an assistant with its own identity, account and resources.</div></button>
 </div>
 <p class="note">Tap a card to reveal it. Agent Gateway translates ID 3 into the other identities off-node, after verifying host, user, sandbox, session and policy.</p>
 </div>

 <div class="pane" data-p="3">
 <div class="stats">
 <div class="stat"><div class="v" data-n="200000" data-f=",">0</div><div class="k">agents in benchmark</div></div>
 <div class="stat"><div class="v" data-n="500">0</div><div class="k">activations per second</div></div>
 <div class="stat"><div class="v" data-n="500" data-p="&lt;" data-s=" ms">0</div><div class="k">suspend / resume latency</div></div>
 <div class="stat"><div class="v" data-n="10" data-s="x">0</div><div class="k">higher compute density (up to)</div></div>
 <div class="stat"><div class="v" data-n="1000" data-f="," data-s="+">0</div><div class="k">dormant agents per host</div></div>
 </div>
 <div class="bars">
 <div class="bar"><div class="row"><span>Published resume latency: Agent Substrate</span><b>&lt; 500 ms</b></div><div class="tr"><span data-w="50" style="background:#4285F4"></span></div></div>
 <div class="bar"><div class="row"><span>Published resume time: E2B (docs)</span><b>~1 s</b></div><div class="tr"><span data-w="100" style="background:#9aa4b2"></span></div></div>
 <div class="bar"><div class="row"><span>Agent Compute Engine</span><b>Not disclosed</b></div><div class="tr"><span data-w="0" style="background:#EA4335"></span></div></div>
 </div>
 <p class="note">These figures are for open-source Agent Substrate on GKE, not Agent Compute Engine. Self-reported by Google. Lower latency is better.</p>
 </div>

 <div class="pane" data-p="4">
 <div class="tw"><table>
 <tr><th></th><th>Agent Compute Engine</th><th>AWS AgentCore Runtime</th><th>Azure dynamic sessions</th><th>E2B</th></tr>
 <tr><td>Isolation</td><td class="g">Cloud Hypervisor microVM</td><td>Dedicated microVM per session</td><td>Hyper-V sandbox</td><td>Firecracker microVM</td></tr>
 <tr><td>Idle</td><td class="g">Checkpoint to zero active resources</td><td>CPU billing typically skips I/O wait</td><td>Destroyed after cooldown</td><td>Pause saves files and memory</td></tr>
 <tr><td>Credentials</td><td class="g">None in sandbox</td><td>Managed by AgentCore Identity</td><td>Not disclosed</td><td>Not disclosed</td></tr>
 <tr><td>Max session</td><td class="g">Not disclosed</td><td>8 h microVM, 14 days Instances</td><td>Configurable cooldown</td><td>Not compared</td></tr>
 <tr><td>Status</td><td class="g">Preview in coming months</td><td>Available</td><td>38 listed regions</td><td>Available</td></tr>
 </table></div>
 <p class="note">Sources: Google Cloud blog; AWS, Microsoft Learn and E2B docs. Checked Oct 22, 2026.</p>
 </div>

 <div class="ft"><span>Sources: <a href="https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive" target="_blank" rel="noopener">Google Cloud deep dive</a> · <a href="https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke" target="_blank" rel="noopener">Agent Substrate</a></span><span class="mtp">Built by Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-ace-explainer');
function post(){try{parent.postMessage({mtpAceHeight:R.offsetHeight+40},'*')}catch(e){}}
var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
tabs.forEach(function(t){t.addEventListener('click',function(){var i=+t.dataset.t;tabs.forEach(function(x){x.classList.toggle('on',x===t)});panes.forEach(function(p){p.classList.toggle('on',+p.dataset.p===i)});if(i===3)runStats();setTimeout(post,60);setTimeout(post,500)})});
/* flow */
var S=[["Harness dispatches a command","The harness (the brain) runs outside the sandbox. It decides the next tool call and sends an explicit command into the microVM."],
["Sandbox runs untrusted code","The microVM (the hands) executes code, shell or browser actions. It holds no tokens, no API keys and has no metadata server access."],
["Traffic exits over vsock","There is no standard network card. Outbound requests cross a virtio-vsock boundary to a local proxy, which binds Titanium-backed node attestation."],
["Agent Gateway checks the triad","Off-node, Agent Gateway validates user delegation, agent identity and node identity, then applies egress and data loss prevention policy."],
["In-flight token swap","Only now is the real backend credential inserted on the wire, as the request leaves the gateway. The sandbox never sees it."],
["Backend sees a clean identity","Workspace, a private VPC service or an MCP server receives a verifiable identity, auditable to a specific agent acting for a specific user."]];
var nodes=R.querySelectorAll('#ace-flow .node'),fill=R.querySelector('#ace-fill'),pkt=R.querySelector('#ace-pkt'),st=R.querySelector('#ace-st'),sd=R.querySelector('#ace-sd'),prev=R.querySelector('#ace-prev'),next=R.querySelector('#ace-next'),play=R.querySelector('#ace-play'),k=0,timer=null;
function draw(){nodes.forEach(function(n,i){n.classList.toggle('cur',i===k);n.classList.toggle('done',i<k)});var pct=k/(S.length-1)*100;fill.style.width=pct+'%';pkt.style.left='calc('+pct+'% - '+(pct/100*14)+'px)';st.textContent='Step '+(k+1)+' of 6: '+S[k][0];sd.textContent=S[k][1];prev.disabled=k===0;next.textContent=k===S.length-1?'Restart ↺':'Next step '}
next.onclick=function(){k=k===S.length-1?0:k+1;draw()};prev.onclick=function(){if(k>0){k--;draw()}};
play.onclick=function(){if(timer){clearInterval(timer);timer=null;play.textContent=' Auto-play';return}play.textContent='❚❚ Pause';k=0;draw();timer=setInterval(function(){if(k<S.length-1){k++;draw()}else{clearInterval(timer);timer=null;play.textContent=' Auto-play'}},1800)};
draw();
/* memory */
var mem=R.querySelector('#ace-mem'),cow=false,priv=[14,22,10,18,26,12];
for(var i=0;i<6;i++){var v=document.createElement('div');v.className='vm';v.innerHTML='<small>VM '+(i+1)+'</small><span class="base" style="height:70px"></span><span class="priv" style="height:'+priv[i]+'px"></span>';mem.appendChild(v)}
var cowb=R.querySelector('#ace-cow'),sh=R.querySelector('#ace-shared');
cowb.onclick=function(){cow=!cow;mem.querySelectorAll('.base').forEach(function(b){b.style.height=cow?'0px':'70px';b.style.opacity=cow?0:1});sh.classList.toggle('on',cow);cowb.textContent=cow?'Turn off CoW sharing':'Turn on CoW sharing'};
var lifes=R.querySelectorAll('#ace-life .st'),lt=null;
R.querySelector('#ace-cycle').onclick=function(){if(lt)clearInterval(lt);var j=0;lifes.forEach(function(x){x.classList.remove('on')});lifes[0].classList.add('on');lt=setInterval(function(){lifes[j].classList.remove('on');j++;if(j>=lifes.length){clearInterval(lt);lt=null;return}lifes[j].classList.add('on')},1300)};
/* ids */
R.querySelectorAll('.id').forEach(function(c){c.addEventListener('click',function(){c.classList.toggle('open');setTimeout(post,450)})});
/* stats */
var ran=false;
function runStats(){if(ran)return;ran=true;R.querySelectorAll('.stat .v').forEach(function(el){var n=+el.dataset.n,p=el.dataset.p||'',s=el.dataset.s||'',f=el.dataset.f,t0=null;function step(ts){if(!t0)t0=ts;var q=Math.min(1,(ts-t0)/1200),e=1-Math.pow(1-q,3),v=Math.round(n*e);el.textContent=p+(f?v.toLocaleString('en-US'):v)+s;if(q<1)requestAnimationFrame(step)}requestAnimationFrame(step)});setTimeout(function(){R.querySelectorAll('.bar .tr span').forEach(function(b){b.style.width=b.dataset.w+'%'})},80)}
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body></html>
"> 

(function(){var f=document.getElementById('mtp-ace-frame');window.addEventListener('message',function(e){if(!f||e.source!==f.contentWindow)return;var d=e.data;if(d&&typeof d.mtpAceHeight==='number'&&d.mtpAceHeight>200){f.style.height=Math.ceil(d.mtpAceHeight)+'px';}});})();

 What does Agent Substrate add? 

 Agent Substrate is the open-source, Kubernetes-native counterpart, available on GKE since September 15, 2026. It offers Cloud Hypervisor microVMs or gVisor sandboxes. Google reports these figures: 

 Up to 10x higher compute density than traditional compute. 

 500 activations per second at under 500 ms suspend/resume, in a 200,000-agent benchmark. 

 Over 1,000 dormant agents per host. 

 It works with harnesses including Claude Code, OpenClaw and Hermes. It is open to all GKE customers for non-production use. Production GA is allowlist-only. Source code is at https://github.com/agent-substrate/substrate . 

 How does it compare with other agent sandboxes? 

 Feature Google Agent Compute Engine Google Agent Substrate AWS AgentCore Runtime Azure dynamic sessions E2B Isolation Cloud Hypervisor microVM ( source ) Cloud Hypervisor microVM or gVisor ( source ) Dedicated microVM per session ( source ) Hyper-V sandbox per session ( source ) Firecracker microVM ( source ) Idle handling Checkpoint to zero active resources Snapshot, free CPU and RAM CPU billing typically skips I/O wait Destroyed after cooldown Pause saves filesystem and memory ( source ) Persistence Hyperdisk per microVM Filestore agent volumes (optional) Filesystem persists across stop/resume Ephemeral sessions Snapshot on pause Max session Not disclosed Not disclosed 8 hours (microVMs), 14 days (Instances) Configurable cooldown Not compared Credentials in sandbox None (gateway token swap) Injected by egress proxy Managed by AgentCore Identity Not disclosed Not disclosed Published resume/start figure Not disclosed Under 500 ms resume Not disclosed Millisecond allocation from prewarmed pools About 1 s resume Open source No Yes No No Not compared Availability Preview in coming months GKE non-production; GA via allowlist Available 38 listed regions Available 

 How is Google expanding agent governance? 

 Google is extending Gemini for business agent governance to Agent Runtime, Cloud Run, Agent Sandboxes, GKE and ACE. The stack includes Agent Gateway, Agent Registry, Agent Identity and OpenTelemetry-based observability. 

 New pieces arrive in stages: 

 Preview soon: Envoy-based enforcement points for multicloud and hybrid setups. 

 Preview soon: governance for local coding agents like Claude Code and Antigravity CLI on managed devices. 

 Preview this quarter: token management , model routing, Service Extensions bindings and Express Link for Cloud Run. 

 Preview this quarter: delegated authorization with Ping Identity, SailPoint and Saviynt. 

 Key Takeaways 

 1 hardware-isolated microVM per agent, with zero credentials inside. 

 Idle agents checkpoint to zero active resources, then resume from snapshots. 

 4 separate identities; only a short-lived SPIFFE ID touches the sandbox. 

 Agent Substrate: 500 activations/s, under 500 ms resume, 200,000 agents. 

 No public pricing, boot time or preview date for Agent Compute Engine yet. 

 Check out the launch post , the technical deep dive , and the Agent Substrate announcement . Register interest for the preview here .. All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent appeared first on MarkTechPost .
