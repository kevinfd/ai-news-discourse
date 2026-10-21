---
id: "99ae24e773f80392"
title: "Announcing SimReady Central: An Open Library of Simulation-Ready 3D Assets for Robotics and AI Factories"
url: "https://huggingface.co/blog/nvidia/simready-central-assets-robotics-ai-factories"
link: "https://huggingface.co/blog/nvidia/simready-central-assets-robotics-ai-factories"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "company_blog"
collector: "rss"
date: "2026-10-21T10:59:42Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["John Kosnik", "Frank DeLise", "Pomi Lee"]
language: "en"
summary: "SimReady Central USD Search\nSearch SimReady assets and retrieve building component data\nEnterprise + Article Published\n\t\t\t\t\tOctober 21, 2026 \nBuilding robotics simulations and high-fidelity AI factory digital twins takes more than 3D models. Developers often need to add properties such as collision geometry, mass, and friction. SimReady assets are 3D models that come prepared with the properties…"
tags: []
orgs: ["Hugging Face", "Nvidia"]
topics: ["robotics & autonomy", "agents & coding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1773
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Announcing SimReady Central: An Open Library of Simulation-Ready 3D Assets for Robotics and AI Factories

Hugging Face · John Kosnik, Frank DeLise, Pomi Lee · 2026-10-21

SimReady Central USD Search
Search SimReady assets and retrieve building component data
Enterprise + Article Published
					October 21, 2026 
Building robotics simulations and high-fidelity AI factory digital twins takes more than 3D models. Developers often need to add properties such as collision geometry, mass, and friction. SimReady assets are 3D models that come prepared with the properties required for simulation workflows, reducing that manual work.
SimReady Central Library brings together more than 2,000 simulation-ready (SimReady) OpenUSD assets on Hugging Face, giving developers a free, ungated starting point for physical AI training environments and AI factory digital twins. The library includes a variety of infrastructure and equipment assets from robot arms and grippers to warehouse equipment, racks, and cooling infrastructure. Developers can check which capabilities each asset supports, then combine assets from different suppliers into a scene.
Equipment manufacturers (OEMs) can now prepare and validate assets against SimReady requirements and use SimReady Central Library to reach developers and allow their end customers to test and simulate scenarios faster and accelerate decision making. This enables industries to build simulations around their products while managing their own Hugging Face datasets.
We’ll cover what makes an asset SimReady and how OEMs contribute to SimReady Central Library, then show how developers can use those assets to build a robotic pick-and-place scenario and compare AI factory layouts.
SimReady assets are OpenUSD assets prepared with the properties required for simulation workflows. A detailed 3D model, such as CAD, is a useful starting point. Simulation requires additional information about how that object should be interpreted and used.
For a robot manipulation task, that might include the object’s mass, collision geometry, and friction properties. For AI factory workflows, it might include equipment geometry and the electrical or thermal metadata required by the application.
OpenUSD is an open, extensible framework for describing and composing 3D scenes. Using those scenes to train and evaluate autonomous machines also requires information about physical behavior, collisions, and sensor interactions.
SimReady Foundation provides specifications, profiles, and validation tools that make these requirements explicit. A profile defines the logical grouping of features and capabilities an asset needs for a particular use case.
Figure 1. SimReady Foundation defines asset representation requirements for specific simulation use cases, while developer libraries help prepare and validate OpenUSD assets against those requirements.
Depending on the asset and profile, those features can include:
For the requirements associated with each simulation use case, see the SimReady Foundation requirements and profiles. Developers should select assets from SimReady Central whose profiles match their workflow needs and compose them into an OpenUSD scene.
OEMs can turn their CAD equipment models into SimReady assets for developers building simulations around their products. SimReady Central Library makes those assets discoverable on Hugging Face, helping manufacturers reach teams building robotics simulations and AI factory digital twins.
For AI factory OEMs like Vertiv, the library provides a path to distribute assets such as warehouse equipment racks, server racks, cooling equipment, and supporting infrastructure for AI factory digital twins. Developers and frontier agents can incorporate these assets into AI factory digital twins reusing the geometry and properties specified by their SimReady profiles.
For robotics OEMs like Comau, FANUC, Franka Robotics, Robotiq, Standard Bots, and Universal Robots, the library makes robot arms and grippers discoverable by teams building training and evaluation environments. Developers can combine these assets with industrial equipment to build warehouse and factory scenarios.
For simulation asset providers like Palatial the library features the NVIDIA Robotics 1K Dataset released in collaboration with NVIDIA Robotics, alongside complex articulated assets generated from text, images, scans, datasheets, and CAD. Developers can build assets and scenes for robot training and evaluation.
For OEMs like LG Electronics (LGE) that develop robots for the home alongside the appliances they work with, the library provides a path to share assets such as refrigerators and dishwashers. Developers can use assets informed by LGE’s experience in both appliances and robotics to build household simulation environments for robot training, evaluation, and synthetic data generation.
For AI-assisted CAD providers like ForgeCAD, the library makes articulated robotics props with high-quality textures available, which developers can use to build environments for robot perception and manipulation training, as well as synthetic data generation.
To contribute, OEMs can use the SimReady Central submission skill to validate assets against the relevant SimReady profiles, package them, and submit them for inclusion in the library.
Figure 2. OEMs prepare and validate OpenUSD assets against SimReady profiles and then submit the asset to SimReady Central. Developers and AI agents discover assets in the library and use them to build simulation environments.
SimReady Central gives robotics and industrial developers a reusable starting point for robot workcells, industrial environments, and AI factory digital twins. Developers and AI agents can find assets in SimReady Central that meet the profiles required by their workflows and compose them into OpenUSD environments.
Developers can use SimReady assets to populate training environments with objects and obstacles, then vary their placement to evaluate robot behaviors. These environments can support projects such as Microduck, an open-source robot from Hugging Face and Pollen Robotics.
Figure 3. Asset datasets connect through SimReady Central on Hugging Face, using its USD search service to support Isaac workflows, SimReady Central library search, and AI agent workflows.
NVIDIA USD Search powers natural-language search in SimReady Central Library, helping developers and AI agents find assets across participating datasets. Hugging Face has also integrated USD Search into their platform search with indexed USD properties and simulation metadata, helping agents discover SimReady assets suited to their physical AI simulation tasks.
AI-assisted authoring adds another way to build with those assets. Developers can use frontier models like OpenAI’s GPT-6 Astra combined with asset search and scene-authoring tools to build environments using SimReady Central Library. Given task requirements and spatial constraints, Astra can help find suitable assets, write code to assemble a scene, and create scenario variations.
OEMs can also use Astra to help prepare and refine OpenUSD assets against SimReady Foundation requirements before validating and submitting them to the library.
For example, a developer building a robotic pick-and-place scenario could start with this prompt:
Using SimReady assets from SimReady Central on Hugging Face, create a basic warehouse pick-and-place scenario in Isaac Sim using PhysX.
Use the nvidia-simready-central.hf.space to find a FANUC robotic arm, a compatible Robotiq gripper, and suitable warehouse assets. Generate the Python code to assemble the scene and configure the pick-and-place task. Render a .mov preview so I can review the results.
Include the scripts, asset versions, and runtime versions so I can reproduce the scenario.
In this workflow, we expect Astra to do the following:
- Query the SimReady Search API to find relevant assets distributed on Hugging Face
- Reference/Payload them into an OpenUSD stage
- Generate Python code to assemble the workcell
- Configure the Pick-and-place task
- Render a preview for user review
Figure 4. A robotic pick-and-place workcell assembled from SimReady assets illustrates how AI-assisted scene authoring can turn developer requirements into a simulation scenario for review and refinement in Isaac Sim.
The same approach can support an ISV (independent software vendor) building an AI factory digital twin. The task shifts from robot interactions to equipment placement: arranging racks, cooling equipment, and supporting infrastructure within specified spatial constraints.
Using SimReady assets from SimReady Central on Hugging Face, create two alternative AI factory layouts with racks and cooling equipment.
Use the supplied equipment dimensions and aisle-clearance requirements. Check for equipment overlaps and clearance violations, and report any issues.
Save each layout as an OpenUSD scene. Include the scene-building scripts, asset versions, and runtime versions so I can reproduce and compare the results.
In this workflow, Astra would assemble the selected SimReady assets into two OpenUSD layouts, followed up by generating scripts to check equipment overlaps and aisle clearances against the supplied requirements. Developers could then inspect the layouts in their simulation application, compare equipment placement and access paths, and review any flagged issues before refining the preferred configuration.
Figure 5. An AI factory layout assembled from SimReady assets illustrates how AI-assisted scene authoring supports equipment placement, aisle-clearance checks, and layout refinement in OpenUSD.
In either example, developers can extend their environments in a few ways:
- Reuse the environment: Keep layout and task-specific changes in separate OpenUSD layers so the same source assets can support multiple experiments.
- Vary the scenarios: Introduce additional assets from the library and vary object placements, equipment configurations, or surrounding infrastructure to evaluate different conditions.
- Build application-specific tests: For robotics, configure training and evaluation tasks in Isaac Lab. For AI factories, connect the scene to the equipment data and simulation tools needed for analyses such as power distribution or cooling performance.
- Carry validated layouts into operations: For AI factories, connect the scene to live BMS and IT telemetry to keep the digital twin synchronized with an AI factory facility.
SimReady Central’s roadmap includes more OEM partners and a growing asset library, expanding the equipment and environments developers can assemble from reusable content.
Community feedback will help identify which additions matter most. Tell us in the comments which assets you need, which runtimes you use, and where you encounter integration gaps.
Submit OEM assets for inclusion in SimReady Central using the asset submission guide.
OEM contributions can broaden the available content, while developer examples can show how assets work in different applications. Share examples of what you build in the comments and open an issue in SimReady Foundation for bugs or SimReady requirements feature requests.
Choose an asset from SimReady Central Library for your next robotics simulation or AI factory digital twin. Use the resources below to find assets, build a scene, or contribute equipment models.
- Find assets for your task: SimReady Central Library on Hugging Face
- Search with natural language: Describe the assets you need through the SimReady Central search endpoint powered by USD Search.
- Build your own asset browser: Explore the index-to-library skills in the SimReady Central GitHub repository.
- Learn to assemble OpenUSD scenes: Follow the free OpenUSD learning path.
- Develop your robotics and digital twin skills: Explore the free physical AI courses.
- Build robotics simulations: Start with the Isaac Sim and Isaac Lab.
- Build AI factories: Start with an agent-assisted digital twin workflow.
- Start the OEM contribution process: Follow the onboarding guide and find FAQ answers in the SimReady Central Library documentation.
- Choose the requirements for your asset: Review the profiles in SimReady Foundation.
- Prepare CAD models for simulation: Use the CAD-to-SimReady skills.
- Validate, package, and submit your assets: Follow the SimReady Central submission skill.
Happy building, we can’t wait to see what you create!
🔎
