---
id: "41b9d660ec27f386"
title: "OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures"
url: "https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures"
link: "https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-13T21:53:40Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Malav Shastri"]
language: "en"
summary: "You can deploy OpenFold3-preview from Amazon SageMaker JumpStart . The OpenFold Consortium and the AlQuraishi Lab at Columbia University developed OpenFold3 as an open source biomolecular structure prediction model. With a few lines of code, you can typically deploy OpenFold3 into your own AWS account. You can then predict the 3D structures of proteins, DNA, RNA, small-molecule ligands, and the…"
tags: ["Advanced (300)", "Amazon SageMaker AI", "Amazon SageMaker JumpStart", "Technical How-to"]
orgs: ["Amazon"]
topics: ["models & research", "health & science", "chips & infrastructure", "jobs & society"]
content_source: "fulltext"
word_count: 2943
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures

AWS Machine Learning Blog · Malav Shastri · 2026-11-13

Artificial Intelligence
OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures
You can deploy OpenFold3-preview from Amazon SageMaker JumpStart. The OpenFold Consortium and the AlQuraishi Lab at Columbia University developed OpenFold3 as an open source biomolecular structure prediction model. With a few lines of code, you can typically deploy OpenFold3 into your own AWS account. You can then predict the 3D structures of proteins, DNA, RNA, small-molecule ligands, and the complexes they form. The endpoint runs with network isolation, which you can use to help keep your sequences within your AWS account.
Computational drug discovery teams now use structure prediction as a core part of their work. Teams use it in target identification, antibody and protein engineering, and structure-based virtual screening. Teams have found running these models challenging. You need GPU infrastructure, a working CUDA and PyTorch stack, large model checkpoints, and a serving layer that handles requests that take minutes rather than milliseconds. SageMaker JumpStart can handle much of that work for you. OpenFold3 runs in an AWS-maintained container on a managed Amazon SageMaker AI endpoint. The endpoint is designed to handle request queuing and GPU warmup, and you can add autoscaling.
In this post, we show you how to:
- Deploy OpenFold3-preview on a SageMaker asynchronous inference endpoint.
- Submit structure prediction jobs and interpret the results, including predicted structures and confidence scores.
- Run several predictions in parallel on multi-GPU instances.
- Supply your own multiple sequence alignments (MSAs) to improve prediction accuracy while helping keep your sequences private.
- Help reduce costs by scaling your endpoint to zero when it’s idle.
Overview of OpenFold3
OpenFold3 is an all-atom structure prediction model. It predicts the joint 3D structure of a set of molecules from their sequences. It isn’t limited to single protein chains: It can fold multi-chain protein complexes, protein–nucleic acid assemblies, and protein–ligand complexes in one prediction.
The OpenFold3 developers release its code and model weights under the Apache 2.0 license, and they publish the training data and methods. Research organizations and pharmaceutical companies can inspect the model, fine-tune it, and build on it under the terms of that license. The developers describe OpenFold3-preview as a research preview.
Use cases
- Target and complex structure prediction – Predict structures for targets that have no experimental structure, including multi-chain assemblies and protein–nucleic acid complexes.
- Protein–ligand co-folding – Fold a protein together with a small molecule supplied as SMILES to generate binding-pose hypotheses for structure-based design.
- Antibody and protein engineering – Evaluate designed variants by predicting their structures and comparing confidence across candidates.
- High-throughput screening pipelines – Queue large batches of prediction jobs against an autoscaling endpoint and process the results directly from Amazon Simple Storage Service (Amazon S3).
Why OpenFold3 uses asynchronous inference
Most JumpStart models, such as large language models and embedding models, deploy to real-time endpoints. A real-time endpoint returns its response within a single request, and that request is capped at 60 seconds. Structure prediction works differently. Folding time grows with the number and length of the chains in a query, and real-world proteins and complexes often take several minutes.
For this reason, OpenFold3 on JumpStart runs on SageMaker Asynchronous Inference:
- You upload the request to Amazon S3 and call InvokeEndpointAsync, which returns immediately.
- The endpoint queues the request and processes it, with an invocation timeout of up to 1 hour.
- The endpoint writes the result, or the error details, to an S3 location you choose. You can poll for it or get a notification through Amazon Simple Notification Service (Amazon SNS).
Two properties of asynchronous endpoints suit scientific workloads especially well. First, they queue bursts of requests internally, so you can submit a large batch of sequences without building your own job queue. Second, they can scale to zero instances when the queue is empty, which helps you avoid paying for idle instances between experiments.
Prerequisites
To follow this walkthrough, you need:
- An AWS account, and a SageMaker AI execution role for the endpoint. Following least privilege, this AWS Identity and Access Management (IAM) role needs read and write access only to the S3 prefix that you use for requests and results. For more information, see How to use SageMaker AI execution roles.
- IAM permissions for the identity that runs the code: to create, describe, invoke, and delete the model, endpoint configuration, and endpoint, plus iam:PassRole for the execution role. For the optional scale-to-zero section, it also needs AWS Application Auto Scaling and Amazon CloudWatch alarm permissions. In production, scope these permissions to your resources rather than using broad managed policies such as AmazonSageMakerFullAccess. For more information, see Complete the prerequisites for asynchronous inference.
- Access to Amazon SageMaker Studio, a SageMaker notebook instance, or a local IDE.
- The SageMaker Python SDK v3 and py3Dmol, which you can install with pip install "sagemaker>=3,<4" py3Dmol.
- Service quota for at least one ml.g6.4xlarge endpoint instance in your AWS Region. You also need quota for ml.g6.12xlarge if you follow the multi-GPU section. You can check your quotas and request increases in the Service Quotas console under Amazon SageMaker.
        Important: SageMaker endpoints are billed per instance-hour while they’re running, including while they’re idle. To avoid unexpected charges, follow the Clean up section, or configure scale-to-zero as described later in this post. For pricing details, see Amazon SageMaker AI pricing.
Discover OpenFold3 in SageMaker JumpStart
- Open SageMaker Studio and choose JumpStart in the navigation pane.
- Search for OpenFold3.
- Open the model card to review the model description, license, and supported instance types.
- Open the example notebook from the model card. It contains the complete asynchronous deployment walkthrough shown in this post.
Deploy OpenFold3 with the SageMaker Python SDK
First, build the model from its JumpStart configuration and define an AsyncInferenceConfig. The output and failure paths are the S3 locations where the endpoint writes results and error details.
Setting accept_eula=True confirms that you’ve reviewed and accepted the model’s license terms, which is required to deploy this model. If you run this code outside SageMaker Studio, also pass your SageMaker execution role to ModelBuilder.from_jumpstart_config with role_arn="<role-arn>".
The endpoint stores your requests and results in Amazon S3, and they contain your sequences and predicted structures. For proprietary sequences, consider using a dedicated S3 bucket or prefix with server-side encryption using an AWS Key Management Service (AWS KMS) key that you manage. To encrypt results with your key, pass its ARN to AsyncInferenceConfig as kms_key_id. Restrict access with a bucket policy that allows only the roles that run this workflow, and add an S3 Lifecycle rule to expire request and result objects that you don’t need to keep. For more information, see Security best practices for Amazon S3.
Deployment typically completes within minutes. This includes a warmup step in which the container runs a short prediction on each GPU, so that the GPUs are warmed up when the endpoint reaches InService.
        Tip: G6 capacity can be limited in some Regions. If a deployment fails with InsufficientInstanceCapacity, retry later, choose a different supported instance size, or deploy in another AWS Region where the model is available.
Run a structure prediction
A request is a JSON document with one or more named queries, and each query lists its chains. All chains in a query are folded together as one complex. Separate queries are folded independently.
Each chain has these fields:
- molecule_type – protein, dna, rna, or ligand.
- chain_ids – a list of chain identifiers, such as ["A"]. To specify identical copies, such as a homodimer, use ["A", "B"].
- sequence – the residue sequence, for protein, DNA, and RNA chains.
- smiles – a SMILES string, used for ligand chains instead of sequence.
The following example folds human ubiquitin, a well-characterized 76-residue protein:
Then poll S3 for either the result or a failure record:
A request with invalid input, such as a malformed chain or an unsupported MSA name, still produces a result object, but with "status": "error" and an error message instead of structures. The last check surfaces that message.
Prediction time grows with the size of the input. In our tests on ml.g6.4xlarge, smaller proteins completed more quickly than larger proteins.
Interpret the results
The response contains a status, a list of predicted structures in mmCIF format, and their matching confidences. By default, OpenFold3 generates five diffusion samples per query, so each query returns five candidate structures. Each sample comes with two confidence files: a detailed one (*_confidences.json) and a summary (*_confidences_aggregated.json). The summary includes a sample_ranking_score that you can use to pick the best sample.
You can open the .cif files in any structure viewer, such as PyMOL, ChimeraX, or Mol*. To view a structure inline in a notebook, use py3Dmol:
The prediction shows ubiquitin’s compact fold: a mixed beta-sheet packed against a single alpha-helix. Most of the structure is blue (high confidence). Only the flexible C-terminal tail, at the top of the image, shifts toward yellow and red, which matches the tail’s known flexibility in experimental structures.
The confidence metrics tell you how much to trust each prediction:
- pLDDT (predicted local distance difference test) – Per-atom confidence in the local structure, on a scale of 0–100. Higher is better, and values above about 70 generally indicate a reliable local structure. The summary file reports the average as avg_plddt.
- pTM and ipTM (predicted TM-score and interface pTM) – Overall confidence in the fold, and in how chains and ligands are positioned relative to each other, on a scale of 0–1. For complexes, ipTM is the key number. The summary file also reports chain_pair_iptm for each pair of chains.
- PAE (predicted aligned error) and PDE (predicted distance error) – Per-residue-pair error estimates, in the detailed confidence file. Use them to judge the relative placement of domains and chains.
Fold a complex
To predict a complex, list several chains in the same query. The following example co-folds human carbonic anhydrase II with its catalytic zinc ion and the drug acetazolamide. This is a well-studied complex with experimental structures in the Protein Data Bank (for example, PDB 3HS4):
Protein sequences in these examples are from UniProt (P0CG48, P00918). You submit and read this request the same way as the ubiquitin example. For complexes like this one, prediction quality depends heavily on providing an MSA, as the next sections show.
Run predictions in parallel on multi-GPU instances
A single OpenFold3 prediction runs on one GPU, so a multi-GPU instance doesn’t make an individual prediction faster. Instead, you can run several predictions at once. On a multi-GPU instance such as ml.g6.12xlarge, which has four GPUs, the container assigns each concurrent request its own GPU. To use all the GPUs, set max_concurrent_invocations_per_instance to the number of GPUs on the instance (four, for ml.g6.12xlarge):
This creates a second endpoint, so remember to delete it as well when you’re done (see Clean up).
In our tests, four concurrent predictions each ran on a separate GPU, with throughput gains that grew with protein size. For larger proteins, the cost per prediction that we measured on ml.g6.12xlarge, based on On-Demand instance pricing, was close to that of ml.g6.4xlarge. Your results depend on your inputs and Region. For pricing, see Amazon SageMaker AI pricing.
        Note: ml.g6.12xlarge capacity can be limited. If it isn’t available in your Region, you can increase throughput by scaling out across several ml.g6.4xlarge instances with the autoscaling configuration described later in this post.
Use the following table to choose an instance:
Improve prediction accuracy with your own MSAs
OpenFold3 can take a multiple sequence alignment (MSA) as an additional input for each protein chain. An MSA is a set of evolutionarily related sequences aligned to your query. Co-variation across those sequences signals which residues are likely to be in contact, so MSAs can substantially improve accuracy for many proteins and complexes.
To help keep your sequences within your AWS account, the JumpStart endpoint runs with network isolation and doesn’t call external MSA servers. Instead, it accepts precomputed MSAs in the request. You generate alignments with the pipeline and sequence databases you already use, on infrastructure you control, and pass them to the endpoint. This design can help drug discovery programs that need to keep proprietary sequences private.
If you don’t supply an MSA, the endpoint predicts from the sequence alone. That can work well for small, well-characterized proteins such as ubiquitin. For most real-world targets and complexes, include an MSA. The rest of this section shows how, and how much it improves results.
Bring your own MSA
Each protein chain accepts a precomputed_msa field: a list of alignments, each with a name and the alignment content in A3M or Stockholm format. For a single merged alignment, such as the output of a ColabFold MMseqs2 search, use the name colabfold_main:
This example has one protein chain. If a query has several different protein chains, compute an MSA for each one and attach it to that chain’s precomputed_msa field. Identical copies listed together under one chain_ids entry, such as a homodimer, share a single MSA.
The endpoint also accepts other alignment names, such as uniref90_hits, mgnify_hits, and bfd_uniclust_hits, if you generate MSAs with a different pipeline. Because the request is staged in S3, you can send large alignments. In our tests, alignments of several megabytes worked.
You can generate MSAs with tools such as ColabFold (MMseqs2) or HHblits or JackHMMER. To help keep proprietary sequences inside your environment, run the search on your own AWS infrastructure against locally hosted sequence databases, rather than sending sequences to a public server. For example, ColabFold’s colabfold_batch command uses the public ColabFold MSA server by default, so for proprietary sequences, use colabfold_search with locally hosted databases instead.
How much difference does an MSA make?
We folded the carbonic anhydrase II, zinc, and acetazolamide complex from the previous section twice on the same endpoint: once in single-sequence mode, and once with an MSA from a ColabFold MMseqs2 search.
With the MSA, OpenFold3 recovers the known binding mode. The zinc ion is coordinated by the three active-site histidines, and the acetazolamide sulfonamide nitrogen binds directly to the zinc, matching the experimental structure. Without the MSA, the protein fold has low confidence and the binding site isn’t formed. Adding the MSA didn’t noticeably change prediction time.
Superimposed on the crystal structure, the MSA-based prediction matches it closely: the protein backbone deviates by 0.2 Å (Cα RMSD), the zinc ion by less than 0.1 Å, and the acetazolamide heavy atoms by 0.4 Å RMSD. The single-sequence prediction is misfolded, with a Cα RMSD of 22 Å.
Carbonic anhydrase II with acetazolamide is one of the most extensively studied complexes in the Protein Data Bank, and closely related structures are likely part of OpenFold3’s training data. Treat this example as a demonstration of the workflow and of how much an MSA matters, not as a benchmark of accuracy on novel targets.
When you compare OpenFold3 results against other tools or published benchmarks, compare like with like: single-sequence results with single-sequence results, and MSA-based results with MSA-based results.
Help reduce cost: Scale to zero when idle
Asynchronous endpoints can scale down to zero instances when no requests are queued, and scale back up when new requests arrive. This pattern suits structure prediction work, which often runs in bursts.
Target tracking scales the endpoint down to zero after the queue has been empty for a while. In our tests, that took about 15–20 minutes. However, target tracking doesn’t scale the endpoint back up from zero. To start an instance when a request arrives and no instances are running, add a step-scaling policy that’s triggered by the HasBacklogWithoutCapacity metric:
When a request arrives at an endpoint with zero instances, it waits in the queue while an instance starts. The first request after scaling from zero will take longer to complete as it includes time for the alarm to trigger, the instance to start, plus the prediction itself. Later requests in the same burst run at normal speed. This trade-off can work well for batch workloads. For interactive use, set MinCapacity=1 to keep one instance warm. For more details, see Autoscale an asynchronous endpoint.
Clean up
To stop incurring charges, delete the resources you created when you’re finished. If you configured autoscaling, remove it first: delete the Amazon CloudWatch alarm, then deregister the scalable target. Then delete each endpoint, its endpoint configuration, and its model, including the multi-GPU endpoint if you deployed it:
If you no longer need the request and result objects, you can also delete them from s3://<bucket>/openfold3-async/.
Conclusion
With OpenFold3 on SageMaker JumpStart, research and drug discovery teams can deploy an open, inspectable structure prediction model into their own AWS account with a few lines of code. Asynchronous inference handles long-running folds and bursty batch workloads, and multi-GPU instances run predictions in parallel. Network isolation helps you keep proprietary sequences private, and because you can bring your own MSAs, you can benefit from MSAs without sending sequences to an external server. With scale-to-zero, you stop paying for endpoint instances after the queue has been empty long enough for the endpoint to scale in. Other charges, such as for Amazon S3 storage, still apply.
The code in this post is sample code for experimentation. Before you use it with proprietary or regulated data, work with your security and legal teams to meet your organization’s security, regulatory, and compliance requirements.
To get started, search for OpenFold3 in SageMaker JumpStart, or open the example notebook from the model card. To learn more about the features used in this post, see Asynchronous inference and Autoscale an asynchronous endpoint. To discuss your structural biology workloads, contact your AWS account team.
