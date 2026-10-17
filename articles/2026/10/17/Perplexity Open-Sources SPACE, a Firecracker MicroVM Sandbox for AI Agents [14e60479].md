---
id: "14e6047931133571"
title: "Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents"
url: "https://marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents"
link: "https://marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-17T00:09:12Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Perplexity has open-sourced SPACE , the sandbox platform behind every task in Perplexity Computer. The Perplexity SPACE sandbox gives each agent task its own Firecracker microVM. Credentials and outbound traffic are controlled from outside that VM. The code ships under Apache 2.0 on GitHub . For teams building coding or browsing agents, this is a production-tested isolation layer they can…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Perplexity", "OpenAI", "Anthropic"]
topics: ["agents & coding", "products & launches", "policy & regulation", "jobs & society"]
content_source: "summary"
word_count: 1233
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents

MarkTechPost · Asif Razzaq · 2026-10-17

Perplexity has open-sourced SPACE , the sandbox platform behind every task in Perplexity Computer. The Perplexity SPACE sandbox gives each agent task its own Firecracker microVM. Credentials and outbound traffic are controlled from outside that VM. The code ships under Apache 2.0 on GitHub . For teams building coding or browsing agents, this is a production-tested isolation layer they can self-host. 

 TL;DR 

 Size: Rust codebase, release 0.8.0 , the public baseline. HTTP API plus server-sent events. 

 Runs on: A Linux x86_64 host with KVM , /dev/kvm , btrfs and Docker. Local Kind (Kubernetes) or direct mode. No macOS. 

 Performance: In production, median create latency fell from 185 ms to 60 ms versus Perplexity’s previous provider. 

 Best: 0 of 108 VM-to-host escape attempts succeeded across 9 frontier models. 

 Worst: Before fixes, agents bypassed the egress policy in 11 of 54 partial-network runs. 

 What is Perplexity SPACE? 

 SPACE (Sandboxed Platform for Agentic Code Execution) is Perplexity’s platform for running agent code in isolated microVMs. Applications call its HTTP API to create Linux environments, run commands and stream output. 

 A template supplies the starting filesystem. A sandbox is one instance of that template, with its own VM and writable disk. Many commands can run inside one sandbox. 

 Perplexity’s launch thread explains the design goal. Agents run commands, install packages and call services with root inside the sandbox. The host stays outside the guest’s control. Agent work is long-running, stateful and branching, so it must survive restarts. 

 How does SPACE isolate agents? 

 Each sandbox is a Firecracker microVM with its own guest kernel. A per-sandbox network gateway on the host enforces egress policy on every outbound connection. 

 Secrets never enter the guest. Per Perplexity’s July engineering post , credentials are injected at the network layer. The credential store adds hierarchical scoping, rate limits and audit logging. 

 The architecture guide splits the system into 4 parts. These are a PostgreSQL-backed API, controllers, worker services and a data plane. Worker services manage VMs, networking, volumes, templates and credentials. btrfs copy-on-write creates each root filesystem. 

 How do pause, suspend and restore work? 

 Sandboxes move through 4 states: running, paused, suspended and deleted. 

 Paused: VM memory stays resident on the worker. This is not a durable snapshot. 

 Suspended: VM memory, runtime state and root filesystem are snapshotted. Active resources are released. 

 Idle default: sandboxes suspend after 6 hours without activity. 

 For fast creates, Kubernetes deployments use warm pools of booted sandboxes. Single-node setups use base snapshots instead. 

 In production, the 90th-percentile create latency dropped from 447 ms to 89 ms . Perplexity reports that 100% of Computer sessions run on SPACE. 

 Did SPACE survive a red-team test? 

 Perplexity’s Escaping SPACE: Part I report tested 9 models with root inside the guest. The study ran 216 runs across 2 tasks and 4 settings. 

 Sandbox escape: 0 of 108 runs reached the host-side secret. 

 No-network bypass: 0 of 54 runs succeeded. 

 Partial-network bypass: 11 of 54 runs succeeded before fixes. 4 models found a path. 

 Claude Opus 5.0, GPT-5.6 Sol, GPT-5.6 Cyber and Kimi K3 found bypasses. The attacks used DNS spoofing and shared CDN IP addresses. 

 Perplexity then added source-address validation through nftables. The gateway now terminates TLS and checks both SNI and HTTP host against the allowlist. In the retest, no model produced a verified bypass. 

 The same team tested 10 third-party platforms. 8 showed at least one network-policy bypass. Perplexity disclosed the results to every affected vendor. 

 Back</button><button class="btn" id="psx-next">Next state </button></div>
 </div>

 <div class="pane" data-p="2">
 <div class="bars" id="psx-rt"></div>
 <div class="note">9 models, 216 runs, root inside the guest. Fixes: nftables source-address validation, TLS termination with SNI + Host allowlist checks. Source: Perplexity, Escaping SPACE: Part I (Sep 23, 2026).</div>
 </div>

 <div class="pane" data-p="3">
 <div class="bars" id="psx-lat"></div>
 <div class="note">Production launch-week traffic, SPACE vs Perplexity's previous sandbox provider. Lower is better. Source: Perplexity engineering blog (Jul 15, 2026).</div>
 </div>

 <div class="pane" data-p="4">
 <div class="tw"><table>
 <tr><th>Feature</th><th>SPACE</th><th>E2B Runtime</th><th>microsandbox</th></tr>
 <tr><td>Isolation</td><td>Firecracker microVM</td><td>Firecracker microVM</td><td>libkrun microVM</td></tr>
 <tr><td>License</td><td>Apache 2.0</td><td>Apache 2.0</td><td>Apache 2.0</td></tr>
 <tr><td>Language</td><td>Rust</td><td>Go</td><td>Rust</td></tr>
 <tr><td>Perplexity egress test</td><td>0 bypasses after fix</td><td>HTTPS bypass, mitigation planned</td><td>HTTP + HTTPS bypass, fix in v0.6.18</td></tr>
 </table></div>
 <div class="note">Egress results from Perplexity's tests on Aug 31 to Sep 1, 2026, for the versions tested.</div>
 </div>

 <div class="ft"><span>Sources: github.com/perplexityai/SPACE · perplexity.ai/hub/blog</span><b>© Marktechpost</b></div>
</div>
<script>
(function(){
 var R=document.getElementById('pplx-space-x');
 function post(){try{parent.postMessage({psxHeight:R.offsetHeight+40},'*')}catch(e){}}
 var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
 var D=['<b>Guest microVM.</b> Each task gets its own Firecracker microVM with its own guest kernel. The agent can run commands and install packages as root. The host stays outside its control.',
 '<b>Per-sandbox gateway.</b> All guest egress passes through a host-side gateway. It now terminates TLS and requires both SNI and HTTP Host to be allowlisted and DNS-attributed.',
 '<b>Outside services.</b> Credentials never enter the guest. They are injected at the network layer, with scoping, rate limits and audit logging.'];
 var det=document.getElementById('psx-detail'),boxes=R.querySelectorAll('.box');
 function showD(i){boxes.forEach(function(b,j){b.classList.toggle('act',i==j)});det.innerHTML=D[i];post()}
 boxes.forEach(function(b){b.addEventListener('click',function(){showD(+b.dataset.d)});b.addEventListener('mouseenter',function(){showD(+b.dataset.d)})});
 showD(0);
 var L=['<b>Running.</b> Processes execute. Live VM memory and the writable filesystem are kept.',
 '<b>Paused.</b> Execution stops. VM memory stays resident on the worker. This is not a durable snapshot.',
 '<b>Suspended.</b> VM memory, runtime state and root filesystem are snapshotted. Active VM resources are released. Default: suspend after 6 hours idle.',
 '<b>Deleted.</b> The sandbox is no longer available through the API.'];
 var li=0,sts=R.querySelectorAll('.st'),ld=document.getElementById('psx-life');
 function life(){sts.forEach(function(s,j){s.classList.toggle('on',j==li)});ld.innerHTML=L[li];post()}
 document.getElementById('psx-next').onclick=function(){li=(li+1)%4;life()};
 document.getElementById('psx-prev').onclick=function(){li=(li+3)%4;life()};
 sts.forEach(function(s,j){s.style.cursor='pointer';s.onclick=function(){li=j;life()}});
 life();
 function bars(el,data){el.innerHTML=data.map(function(d){return '<div class="row"><div class="lbl"><span>'+d[0]+'</span><em>'+d[1]+'</em></div><div class="track"><div class="fill" data-w="'+d[2]+'" style="background:'+d[3]+'"></div></div></div>'}).join('')}
 bars(document.getElementById('psx-rt'),[
 ['VM-to-host escape','0 of 108 runs',1.5,'#76B900'],
 ['Network bypass, no network','0 of 54 runs',1.5,'#76B900'],
 ['Network bypass, partial network (before fix)','11 of 54 runs',20.4,'#E5675A'],
 ['Network bypass, after fix','0 verified bypasses',1.5,'#76B900'],
 ['Third-party platforms with a bypass','8 of 10',80,'#1FB8CD']]);
 bars(document.getElementById('psx-lat'),[
 ['Median create, previous provider','185 ms',41.4,'#5E5B66'],
 ['Median create, SPACE','60 ms',13.4,'#20808D'],
 ['p90 create, previous provider','447 ms',100,'#5E5B66'],
 ['p90 create, SPACE','89 ms',19.9,'#20808D']]);
 function anim(p){p.querySelectorAll('.fill').forEach(function(f){f.style.width='0';setTimeout(function(){f.style.width=f.dataset.w+'%'},60)})}
 tabs.forEach(function(t){t.onclick=function(){var i=+t.dataset.t;tabs.forEach(function(x,j){x.classList.toggle('on',j==i)});panes.forEach(function(p,j){p.classList.toggle('on',j==i)});anim(panes[i]);post()}});
 window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body>
</html>
"> 

(function(){var f=document.getElementById('pplx-space-frame');window.addEventListener('message',function(e){if(e.source===f.contentWindow&&e.data&&e.data.psxHeight){f.style.height=e.data.psxHeight+'px';}});})();

 How does SPACE compare with other open sandboxes? 

 Feature Perplexity SPACE E2B Runtime microsandbox Daytona Isolation Firecracker microVM per sandbox Firecracker microVM per sandbox libkrun microVM Dedicated kernel per sandbox License Apache 2.0 Apache 2.0 Apache 2.0 Public repo, unmaintained since June 2026 Language Rust Go Rust Not disclosed Host needs Linux x86_64 + KVM Not disclosed Linux with KVM Not disclosed Egress control Per-sandbox gateway, TLS termination nftables firewall, SNI/Host lists Not disclosed Not disclosed Perplexity egress test 0 bypasses after fix HTTPS bypass, mitigation planned HTTP + HTTPS bypass, fix in v0.6.18 HTTPS bypass, mitigation released E2B SDK support Yes, via ECW wrapper Native Not disclosed Not disclosed 

 How do developers deploy SPACE? 

 The installation guide deploys SPACE into a local Kind cluster. The host needs /dev/kvm , /dev/net/tun , loop devices and btrfs. Running it inside a VM requires nested virtualization. 

 Teams already on E2B can try the E2B Compatibility Wrapper . Its tested baseline is the Python package e2b==2.21.1 . A reference AWS EKS deployment ships in the repository. 

 Key Takeaways 

 SPACE runs each agent task in its own Firecracker microVM. 

 Credentials and egress policy live outside the guest VM. 

 0 of 108 escape attempts reached the host in red-team tests. 

 Egress bypasses hit 11 of 54 runs before fixes, 0 after. 

 Apache 2.0, Rust, needs a Linux x86_64 host with KVM. 

 Check out the GitHub repo , the docs and the red-team report . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents appeared first on MarkTechPost .
