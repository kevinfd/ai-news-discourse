---
id: "448d198a6d06442b"
title: "Using NVIDIA Run:ai GPU Fractioning on Amazon EKS"
url: "https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks"
link: "https://aws.amazon.com/blogs/machine-learning/using-nvidia-runai-gpu-fractioning-on-amazon-eks"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-19T16:13:51Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Muru Bhaskaran"]
language: "en"
summary: "GPU sharing is not new: Multi-Instance GPU (MIG), time-slicing, and Multi-Process Service (MPS) address different isolation and utilization needs. NVIDIA Run:ai GPU Fractioning builds on MPS with Kubernetes-integrated scheduling, per-Pod memory contracts, enforcement, and metrics. \n NVIDIA Run:ai is AI workload orchestration software for Kubernetes. Its GPU Fractioning Operator can help several…"
tags: ["Advanced (300)", "Amazon Elastic Kubernetes Service", "Technical How-to"]
orgs: ["Amazon", "Nvidia"]
topics: ["chips & infrastructure", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 2698
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Using NVIDIA Run:ai GPU Fractioning on Amazon EKS

AWS Machine Learning Blog · Muru Bhaskaran · 2026-11-19

Artificial Intelligence
Using NVIDIA Run:ai GPU Fractioning on Amazon EKS
GPU sharing is not new: Multi-Instance GPU (MIG), time-slicing, and Multi-Process Service (MPS) address different isolation and utilization needs. NVIDIA Run:ai GPU Fractioning builds on MPS with Kubernetes-integrated scheduling, per-Pod memory contracts, enforcement, and metrics.
NVIDIA Run:ai is AI workload orchestration software for Kubernetes. Its GPU Fractioning Operator can help several teams share one or two GPUs on Amazon Elastic Kubernetes Service (Amazon EKS). Notebooks, model evaluations, and small inference services can leave teams waiting even when GPU memory remains available. In this walkthrough’s baseline, the NVIDIA device plugin exposes the single GPU as one nvidia.com/gpu resource, with GPU sharing disabled. Two Pods each requesting nvidia.com/gpu: 1 cannot run concurrently on that node, even when their combined GPU-memory demand fits.
NVIDIA Run:ai GPU Fractioning adds Kubernetes scheduling integration, enforced GPU-memory limits, and per-Pod metrics to software-based sharing. The approach applies to NVIDIA GPUs that meet the GPU Fractioning Operator’s hardware and software requirements, including GPUs without MIG. We use one Amazon Elastic Compute Cloud (Amazon EC2) g5.xlarge instance with an NVIDIA A10G Tensor Core GPU as the validated example. Other configurations require compatibility checks and validation.
NVIDIA announced the open source release of NVIDIA Run:ai on October 13, 2026. This example uses two of its four modular components: KAI Scheduler and GPU Fractioning Operator. KAI Resource Management and Workload Map address organizational governance and additional workload types, outside this walkthrough’s scope.
In this post, we show how to build a custom Amazon Linux 2023 (AL2023) image and configure GPU-memory sharing on Amazon EKS. In the validated G5/A10G example, you establish a whole-GPU baseline, give each Pod an 8 GiB memory contract, and verify 6 GiB allocations. You then inspect per-Pod metrics, test rejection of a 9 GiB allocation, and clean up the disposable environment.
Choose a GPU sharing approach
MIG provides hardware partitions on supported GPUs. Device-plugin time-slicing shares a GPU without replica memory or fault isolation. MPS permits concurrent CUDA processes. Fault containment depends on configuration. NVIDIA Run:ai GPU Fractioning adds enforced per-container memory limits and supports time-slicing (default) or sm-sharing compute modes. NVIDIA documents separate workload error domains for its default mode and a shared error domain for sm-sharing. These are not security guarantees. This walkthrough tests memory limits, not fault containment or compute performance. A memory limit does not reserve proportional compute.
Amazon EKS documents several GPU sharing options: MIG, time-slicing with the NVIDIA device plugin, and time-slicing with the NVIDIA DRA driver and Karpenter. For guidance on choosing among them, see the GPU sharing guidance in the Amazon EKS Best Practices Guide. Choose GPU fractioning when you need enforced per-Pod GPU-memory limits on GPUs without MIG and can run fixed-size GPU node groups.
Dynamic Resource Allocation (DRA) provides Kubernetes APIs for requesting and allocating devices. GPU sharing and isolation depend on the device driver’s implementation and enabled features. KAI Scheduler and GPU Operator support DRA. This walkthrough uses NvFractions annotations, not DRA.
GPU fractioning can help interactive notebooks with idle periods, short evaluation jobs, GPU compatibility tests, and small inference services. Choose each GPU-memory request from measured peak usage plus overhead, then test latency under concurrent load. The demonstrated density improvement does not establish a throughput gain or a universal cost reduction.
Solution overview
The following diagram shows the validated single-GPU environment in the US East (Ohio) Region (us-east-2). You use the AWS Command Line Interface (AWS CLI), eksctl, Helm, and Packer to build and operate it. The Amazon EKS control plane runs Kubernetes version 1.36 in an AWS managed Amazon Virtual Private Cloud (Amazon VPC), separate from the customer VPC. It connects to EC2 workers in private subnets of the customer VPC.
An m7i.large system node hosts the operator controllers and KAI Scheduler. KAI Scheduler places both Pods on a tainted g5.xlarge with one A10G containing 23,028 MiB of GPU memory.
Each Pod has an 8 GiB GPU-memory limit and allocates 6 GiB of GPU memory. The GPU worker uses custom AL2023 with the NVIDIA R615 driver branch, NVIDIA Container Toolkit, and containerd. It runs fractiond with Node Resource Interface (NRI) integration and MPS for sharing. The metricsd daemon exports per-Pod GPU-memory metrics.
Implementation walkthrough
The walkthrough uses the AWS Samples repository. Confirm the prerequisites and validated component versions, then complete Steps 1 through 10.
Prerequisites
Use an AWS account with permissions for Amazon EKS, AWS CloudFormation, Amazon VPC, Amazon EC2, Amazon Elastic Block Store (Amazon EBS), AWS Identity and Access Management (IAM), and AWS Systems Manager for Amazon Machine Image (AMI) discovery. Confirm quota and capacity for g5.xlarge, the system node, and a temporary m5.xlarge image builder. Install AWS CLI v2, eksctl, kubectl, Helm, Packer, Git, jq, and curl.
Use your normal AWS credential provider: a named profile, AWS IAM Identity Center, an assumed role, or access-key environment variables. Prefer temporary credentials. AWS_SESSION_TOKEN is required when using temporary access keys. The examples use us-east-2. Another Region must support the selected Amazon EKS version and instance types.
Before choosing another GPU, check NVIDIA’s GPU Operator hardware list, the selected driver’s hardware support, and the GPU Fractioning Operator prerequisites. Hardware support alone does not establish fractioning compatibility. This walkthrough validates the G5/A10G configuration only. The AMI build targets x86_64. Check CUDA compatibility and memory headroom: The two 8 GiB contracts require room for both contracts and runtime overhead. Smaller devices need smaller contracts and adjusted probes.
The walkthrough creates billable resources, including an Amazon EKS control plane, a NAT gateway, instances, volumes, and an AMI snapshot. Use a disposable environment and complete cleanup when validation finishes.
Use the validated AL2023 stack
At the time of validation, the EKS-optimized AL2023 NVIDIA image provided R580 and R595 driver branches. GPU Fractioning Operator v0.1.7 requires R615 or newer. R615 is short-lived and is not the GPU Operator default. This example builds a custom standard Amazon EKS 1.36 AL2023 image with AMI-owned driver and toolkit. It does not use an operator-managed driver container on another OS. The table records lab validation, not vendor support certification.
We validated this walkthrough on October 22, 2026, using NVIDIA driver 615.71.10. On November 18, 2026, after updating the GPU node taint, we repeated every step except the Step 3 image build, using an image with the same driver. The results matched. The table lists the tested component versions, not a permanent support matrix. Recheck the Amazon EKS AMI documentation and NVIDIA prerequisites before changing any component.
Step 1: Clone and configure
Clone the repository, then create a local configuration file from the provided example and restrict its permissions:
After cloning, use walkthrough.env for configuration and run.sh for each stage. Generated files and kubeconfig stay in the ignored .state directory. GPU_INSTANCE_TYPE selects the instance type. Changing it alone does not establish compatibility.
Defaults and optional authentication settings in walkthrough.env
Never commit credentials. The local configuration file is ignored by Git. Confirm the active identity before provisioning:
Run stages separately to inspect results, or use ./run.sh walkthrough to run through the memory-limit test. Cleanup is always a separate action.
Step 2: Create the disposable cluster
Run the following command to create the disposable Amazon EKS cluster and its system node:
The command provisions an Amazon EKS cluster running Kubernetes version 1.36, a dedicated VPC with one NAT gateway, OpenID Connect (OIDC) integration, and a private m7i.large managed node.
Selected fields from config/eksctl-cluster.yaml.tpl
Step 3: Build the custom AL2023 image
Run the following command to build the custom AL2023 image with the R615 driver branch:
The script discovers a public builder subnet and the recommended standard Amazon EKS AMI for Kubernetes 1.36 on AL2023. Packer installs the current patch release from the R615 driver branch and the toolkit, configures the NVIDIA runtime, checks package state, and creates an encrypted image. The Region-specific AMI ID is stored in .state/ami-id.
NVIDIA_DRIVER_VERSION selects the R615 branch. It is not an exact patch pin. The workflow records the discovered driver version with the AMI ID and uses that version in AMI and node-group tags. Read .state/installed-driver-version for the version observed in your build. For production, pin exact packages and the base image in your own build and validate a supported driver-branch upgrade.
You need this step only because the EKS-optimized AL2023 NVIDIA AMI did not include the R615 driver branch at the time of validation. Prefer an EKS-optimized NVIDIA AMI once the driver that it selects for your GPU and the remaining host prerequisites meet the GPU Fractioning Operator requirements. Check the driver versions in the Amazon EKS AMI releases on GitHub. The sample’s scripts currently require the R615 driver and metadata from the image build, so using a stock AMI also requires script changes.
Relevant Packer settings from ami/eks-al2023-r615.pkr.hcl
SOURCE_AMI_ID and PACKER_SUBNET_ID are optional overrides for an approved base image or builder subnet. Rebuild and test images when the operating system or GPU stack changes.
Step 4: Add the GPU worker
Run the following command to add a GPU managed node group that uses the custom image:
By default, the managed node group uses the custom image and stays at one On-Demand g5.xlarge, the validated GPU worker. A GPU taint excludes ordinary workloads. The script disables eksctl’s NVIDIA device-plugin installation because GPU Operator manages that component.
Selected fields from config/eksctl-gpu-nodegroup.yaml.tpl
Step 5: Install GPU Operator and inspect the host
Run the following command to install GPU Operator and inspect the GPU worker’s host configuration:
GPU Operator 26.7.1 supplies the device plugin and Kubernetes integrations. Its configuration preserves the image-owned driver and toolkit:
The same command runs a temporary privileged inspection Pod on the GPU worker, prints the host configuration, and removes the Pod. The validated node reports:
Observed host configuration
On this AL2023 node, /var/run is a symbolic link to /run. Both paths identify the same socket. Limit privileged inspection to the disposable environment and confirm the Pod is removed.
Step 6: Establish the whole-GPU baseline
Run the following command to test whole-GPU scheduling before fractioning is installed:
Each baseline Pod requests and limits nvidia.com/gpu to 1. The test assumes one available physical GPU with sharing disabled: One Pod runs and the other remains Pending. This demonstrates the whole-device scheduling constraint before fractioning is installed. On multi-GPU nodes, adapt this baseline and verify that both fractional workloads use the same GPU.
Measured baseline result
The script checks this state and removes both baseline Pods.
Step 7: Install KAI Scheduler and GPU Fractioning Operator
Run the following command to install KAI Scheduler, which includes GPU Fractioning Operator:
The pinned KAI Scheduler 0.18.5 chart includes GPU Fractioning Operator 0.1.7. The values turn on NvFractions and per-Pod metrics while retaining GPU-stack version checks. The optional nvidia.com/container.<name>.gpu-compute.mode annotation selects compute mode. These workloads leave the default unchanged.
Relevant fields from helm/kai-values.yaml
In the validation, FractiondReady, MpsdReady, and Ready are True. DriverUpgradeInProgress is False with reason NoDriverUpgrade, consistent with the AMI retaining driver ownership.
Step 8: Run the positive sharing test
Run the following command to deploy two Pods with 8 GiB GPU-memory contracts:
Each Pod requests and limits memory to 8 GiB and selects kai-scheduler. Neither requests a whole nvidia.com/gpu resource. The repository applies these scheduling fields and runs a CUDA probe that allocates 6 GiB:
Essential fields from kubernetes/fraction-8gi-pods.yaml
Measured positive result
The script verifies matching node names and GPU UUIDs. In the validation, both Pods see 8,192 MiB and report allocation_succeeded_mib=6144. Those checks establish placement on one physical GPU, the bounded device view, and successful allocations within each contract.
Measured allocation output from each Pod
Observe memory while both Pods remain active
The gpu_fractioning_gpu_memory_used_bytes metric attributes memory by Pod and GPU UUID. The observed 6,394 MiB (about 6.24 GiB) per Pod exceeds the probe’s 6,144 MiB allocation by 250 MiB. Metrics can include CUDA context and runtime overhead. This experiment does not measure that breakdown. Retain workload identity and request, limit, and usage values together when monitoring the shared device.
Measured per-Pod metric series
Step 9: Verify rejection above the limit
Run the following command to test an allocation that exceeds the 8 GiB contract:
This command removes the positive-test Pods and creates one Pod with an 8 GiB contract that attempts a 9 GiB allocation. The probe reports:
Measured over-limit result
Measured negative-test Pod status
Here, cudaMalloc returns an out-of-memory error, which the probe handles before exiting with code 0. Completed is expected, not OOMKilled. This demonstrates allocation rejection, not container termination or general fault isolation.
Step 10: Clean up
Capture the VPC ID before deleting the cluster. The independent checks that follow use the default cluster name and Region. Substitute your configured values if you changed them.
Capture the VPC ID
Remove the disposable environment
Standard cleanup removes the test namespace, Helm releases, and disposable cluster while preserving the custom AMI and its Amazon EBS snapshot.
Verify resource deletion
Expect explicit resource-not-found responses for deleted resources. Authentication or permission errors do not establish deletion. Also inspect remaining node groups and cluster-tagged instances. If cleanup fails, inspect CloudFormation events and resolve owned dependencies before retrying. An absent Amazon EKS endpoint does not prove that its VPC is gone.
Use ./run.sh cleanup-all only when the custom AMI and its Amazon EBS snapshot are no longer needed. If image deletion is refused, confirm the AMI ID and sample ownership tag. Do not bypass the safeguard.
Production considerations
Treat this as a behavior validation. Use trusted workloads and apply least-privilege IAM, namespace controls, approved images, and admission rules for fraction requests. Choose whole GPUs or MIG on supported hardware when stronger isolation is required.
The pinned fractioning daemons use privileged containers, host PID access, and NRI/MPS host mounts. Restrict their deployment and configuration to trusted administrators.
Allow headroom for CUDA contexts, caches, batching, and runtime overhead. Measure latency and throughput under concurrent load. Monitor allocation failures, MPS health, NRI connectivity, and GPU errors. Pin the base AMI, driver, toolkit, device plugin, operator, scheduler, and workload images as one tested combination. Rebuild images and test rollback before rollout.
This walkthrough requires pre-provisioned GPU capacity. It does not configure or validate GPU-fraction-aware autoscaling. The fractional Pods select kai-scheduler, request no nvidia.com/gpu resource, and use a nodeSelector that targets a node group fixed at one node. Karpenter support for secondary schedulers is an open feature request (issue #742 on GitHub). The custom image cannot run on Amazon EKS Auto Mode-managed nodes, because Auto Mode selects and manages their AMI. A cluster can mix Auto Mode-managed nodes with managed node groups, but we did not validate this walkthrough in such a cluster.
Teams that use Karpenter can reference the same custom AMI by ID in an EC2NodeClass. The autoscaling limit still applies. We did not validate this path.
KAI Scheduler is a second scheduler. It handles queueing and placement for Pods that select it. If you already use Kueue, decide which component owns queueing for GPU workloads before you adopt KAI Scheduler.
We recommend running the Amazon EKS node monitoring agent on GPU nodes. In a November 18, 2026 regression run, the agent ran on the custom R615 image with MPS sharing active and reported healthy GPU conditions throughout the sharing and limit tests. That run did not test fault detection. Because GPU Operator already runs a Data Center GPU Manager (DCGM) host engine, configure the agent to use that host engine instead of its bundled one.
Conclusion
In this post, we showed how to configure GPU-memory fractioning on Amazon EKS with a custom AL2023 image, using G5/A10G as the validated example. The approach extends to compatible NVIDIA GPUs after checking prerequisites and validating the selected configuration. You established the whole-GPU baseline, ran two bounded workloads on the same GPU, inspected per-Pod memory usage, and verified rejection of an allocation above the limit. Fractioning can improve access to existing capacity when workload memory fits. Production adoption also requires isolation controls and performance testing.
To repeat the experiment, clone the AWS Samples repository and compare your results with its validated evidence. Explore the GPU Fractioning Operator documentation and the Amazon EKS accelerated AMI guidance before adapting the example to your workloads.
The content and opinions in this post are those of the third-party author and AWS is not responsible for the content or accuracy of this post.
