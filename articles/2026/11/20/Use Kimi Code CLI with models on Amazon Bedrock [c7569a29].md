---
id: "c7569a295cb76304"
title: "Use Kimi Code CLI with models on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-20T00:33:30Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Alex Thewsey"]
language: "en"
summary: "Kimi Code CLI is an open source coding agent from Moonshot AI, the creator of the Kimi series of open-weight foundation models. Previously, using Kimi Code with models on Amazon Bedrock meant configuring a generic connection “provider” with an Amazon Bedrock API key. For many AWS customers, this meant introducing an extra credential to obtain and protect. \n With v2.7.0, Moonshot AI adds a native…"
tags: ["Amazon Bedrock", "Announcements", "Intermediate (200)"]
orgs: ["Amazon", "OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 2133
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Use Kimi Code CLI with models on Amazon Bedrock

AWS Machine Learning Blog · Alex Thewsey · 2026-11-20

Artificial Intelligence
Use Kimi Code CLI with models on Amazon Bedrock
Kimi Code CLI is an open source coding agent from Moonshot AI, the creator of the Kimi series of open-weight foundation models. Previously, using Kimi Code with models on Amazon Bedrock meant configuring a generic connection “provider” with an Amazon Bedrock API key. For many AWS customers, this meant introducing an extra credential to obtain and protect.
With v2.7.0, Moonshot AI adds a native bedrock provider to the CLI. You can now configure the agent to use your standard AWS credential chain, including named profiles and single sign-on (SSO), instead of creating and managing a separate API key.
In this post, we show you how to connect Kimi Code CLI to models on Amazon Bedrock using your existing AWS credentials. We use Kimi K3.1 Pro Highspeed as an example, which supports streaming, configurable reasoning, image input, and client-side tool calling.
What’s new
Amazon Bedrock provides pay-per-token inference for a range of open and proprietary models from leading providers, available through standard APIs. Processing stays within the AWS data boundary, as detailed in the Data protection section of the User Guide. The model cards detail which APIs and features are supported for each model.
In older versions of the Kimi Code CLI, you could connect to Amazon Bedrock through a provider with type = "openai" or type = "openai_responses". These use the OpenAI-compatible Chat Completions or Responses APIs, respectively. This approach required you to set the regional base_url and provide an Amazon Bedrock API key. The key could be short-term or long-term, but it was a separate credential for you to obtain and manage.
The native provider changes that setup:
- Use your existing AWS authentication workflow. The bedrock provider can resolve temporary credentials through the standard AWS Command Line Interface (AWS CLI) credential chain. You can use the default chain or select a named profile, including a profile backed by SSO.
- Override the protocol for each model, if needed. The provider infers an API format and regional endpoint from the model ID, but you can change them as detailed in the “Override endpoint URL and protocol” section of this post.
AWS recommends short-term credentials over long-term credentials. This new path reduces reliance on manually managed API keys, but it doesn’t change your responsibility to protect AWS credentials and scope permissions appropriately.
How it works
The native provider handles authentication and request routing in four steps:
- Resolve AWS credentials. Unless you configure an Amazon Bedrock API key, the bedrock provider uses the standard AWS credential chain in your environment. You can set AWS_PROFILE to select a specific named profile.
- Generate a short-lived bearer token. The provider uses @aws/bedrock-token-generator to create a short-term Amazon Bedrock API key, and renews it when necessary. You don’t need to place any AWS access key or manually generated Amazon Bedrock key in the Kimi Code config.toml. However, an explicit key given through api_key or api_key_env takes precedence if you provide it.
- Build the regional endpoint. The provider resolves AWS_REGION or AWS_DEFAULT_REGION and constructs the appropriate bedrock-runtime endpoint for the model’s inferred API. For Kimi models, this resolves to the recommended OpenAI-compatible Chat Completions path.
- Call the selected inference profile. The model alias maps to an Amazon Bedrock model or inference profile ID. This example uses the global inference profile global.moonshotai.kimi-k3.1. The global. prefix selects the profile, while AWS_REGION determines the regional endpoint that receives your request.
The CLI then streams the model response and can use the model’s client-side tool-calling support during coding tasks. Authentication, authorization, model access, and network connectivity must all succeed for a request to complete. The ephemeral API keys generated by the provider are valid for up to 12 hours or your AWS session length, whichever is shorter.
Prerequisites
For this walkthrough, we use Kimi K3.1 Pro Highspeed as an example model, accessed through global cross-Region inference for broadest availability and lowest cost. Review the Amazon Bedrock pricing to understand expected costs before using the model.
To follow along, you need:
- An AWS account with access to the target model and inference profile in a supported source AWS Region. Check the Kimi K3.1 Pro Highspeed model card for current Region and inference-profile support.
- Kimi Code CLI v2.7.0 or later. Follow the Kimi Code CLI installation guide and run kimi --version to check your installation.
- The AWS CLI, to follow the profile and identity-check commands in this post. The optional aws login workflow requires AWS CLI v2.32.0 or later.
- An AWS Identity and Access Management (IAM) identity (user or assumed role) with permissions to invoke the target model and inference profile in your chosen AWS Region.
The following example IAM policy grants the permissions used by this walkthrough, for the Kimi K3.1 Pro Highspeed model and global inference profile only. Replace ${AWS_REGION} with your source Region (for example, us-west-2 for US West Oregon) and ${AWS_ACCOUNT_ID} with your 12-digit AWS account ID:
The foundation-model ARN without a Region or account ID is intentional and required for global cross-Region routing. The BedrockInvokeKimiK31DefaultProject statement is only required if using the openai_responses protocol, not with the default openai (Chat Completions).
Security of your AWS environment is a shared responsibility. Review and grant IAM permissions according to the principle of least privilege, particularly for production environments. Consider using a dedicated IAM role for Kimi Code CLI, separate from your regular AWS activities.
Get started with the bedrock provider
After your prerequisites are ready, follow these steps to configure AWS authentication, add the provider and model, and send a test request.
Step 1: Configure AWS credentials
There are different ways to authenticate with the AWS CLI, depending on your organization’s setup. With Named profiles, you can configure multiple AWS contexts and switch between them.
For example:
- If you use SSO through AWS IAM Identity Center, run aws configure sso --profile YOUR_PROFILE_NAME to set up a profile, then run aws sso login --profile YOUR_PROFILE_NAME to authenticate.
- To use AWS Management Console credentials with AWS CLI v2.32.0 or later, run aws login --profile YOUR_PROFILE_NAME. The console-credential login guide also describes a credential_process configuration for tools that don’t support the cached login session directly.
- Omit the --profile arguments to use your default AWS profile instead of a named one.
Whichever approach you choose, your session resolves to an IAM identity (user or role) that needs the Amazon Bedrock permissions from the prerequisites. A Region configured in an AWS CLI profile applies to AWS CLI commands, but you must still set the Region explicitly for Kimi Code in Step 2.
Verify that the AWS CLI resolves your intended identity. Omit --profile YOUR_PROFILE_NAME if you use the default profile:
Step 2: Add the provider and model
- Open or create ~/.kimi-code/config.toml in a text editor. If you set KIMI_CODE_HOME, use $KIMI_CODE_HOME/config.toml instead. If you have an existing file, back it up and merge these entries with your current settings rather than overwriting unrelated providers or models.
- Replace YOUR_SOURCE_REGION with your supported source Region (for example, us-west-2). To use a named profile, replace YOUR_PROFILE_NAME and uncomment the AWS_PROFILE line: The model alias bedrock-kimi-k3-1 is a local name used by Kimi Code CLI. The model value is the Amazon Bedrock global inference-profile ID. The example declares a 1-million-token context window and explicit reasoning, image-input, and tool-use capabilities. It omits api_key, api_key_env, and AWS_BEARER_TOKEN_BEDROCK, so the provider uses ambient AWS credentials. A configured Amazon Bedrock key would take precedence.
- Save the file. The [providers.bedrock.env] table supplies configuration to the provider. It doesn’t export variables into your shell.
Step 3: Send a request and start a coding session
- Run a small non-interactive coding request:
- Confirm that the CLI streams a response without an authentication, authorization, Region, model-access, or network error. This request provides a more meaningful connectivity check than a provider status indicator.
- Start an interactive session in a project directory: 
         
         Because you set default_model, the session selects bedrock-kimi-k3-1 automatically. Ask the agent to explain the repository or propose a small change. Review its proposed file modifications and shell commands before approving them.
Configuration best practices
At the time of writing, the native bedrock provider has several configuration considerations. These practices help you avoid ambiguous status information and mismatched settings.
Use the configuration file to set up the provider
At the time of writing, Kimi Code’s desktop and web provider-creation interfaces don’t expose all the provider environment fields used by this credential-chain setup. Edit config.toml directly to set up the Amazon Bedrock provider. For further details, refer to Model providers in the Kimi Code documentation.
Declare model capabilities explicitly
Kimi Code doesn’t auto-detect the capabilities of most models on Amazon Bedrock, including Kimi models. Check the Amazon Bedrock model card for each target model and explicitly declare its capabilities to let Kimi Code make use of them.
For example, Kimi K3.1 Pro Highspeed supports always_thinking, thinking, image_in, and tool_use, but not audio_in or video_in, as reflected in the config.toml example shown earlier.
These declarations describe client behavior. You should only include capabilities that are supported for each target model and Amazon Bedrock API endpoint. Validate tool and image workflows for your application rather than relying on the capability labels alone.
Keep Region settings consistent and prefer cross-Region inference where possible
The bedrock provider requires an explicit AWS_REGION or AWS_DEFAULT_REGION in Kimi Code’s config.toml or the shell environment. It can’t infer a Region configured only in ~/.aws/config or through aws configure.
When you use cross-Region inference profiles (with prefixes such as global., us., or in.), the configured Kimi Code Region controls the source Region that receives your requests. For more information, refer to cross-Region inference in the Amazon Bedrock User Guide.
For workloads without data-residency requirements, start with the global inference profile. This model, like many others, is priced 10% lower for global inference than through geographic profiles. Review Amazon Bedrock pricing for current rates and geographic alternatives.
Override endpoint URL and protocol where needed
In some cases, the provider’s auto-detection might mistake the API protocol or target URL you want to use for a particular model. For example, you will need to set a different URL to use Amazon Bedrock through a VPC endpoint or the Mantle endpoints.
In the Kimi Code config.toml, you can:
- Set the protocol field to openai (Chat Completions), openai_responses, or anthropic (Messages) to configure a model to use a particular supported wire protocol. See the model cards for which models support which APIs.
- Set the base_url field to change the target URL, which must include any attached API path like /openai/v1 or /anthropic.
In the following example, we show a configuration to connect to the same model but using the OpenAI Responses API through an Amazon Bedrock VPC endpoint you’ve set up:
Treat connectivity status as a configuration indicator
In the Kimi Code desktop and web apps, the provider list can show connected for a bedrock provider. That status doesn’t validate the configured AWS credentials, IAM permissions, Region, model access, or network path. Don’t treat it as proof of a successful model request. Use the non-interactive prompt to test the complete path, and diagnose the actual response if it fails.
Cleanup
If you created a new AWS IAM identity or assigned new permissions to experiment with Kimi K3.1 Pro on Amazon Bedrock, remember to delete them when you’re finished testing.
You might also want to revert any local Kimi Code CLI provider configurations or AWS CLI profiles you set up. You can even uninstall the CLIs altogether if they’re no longer required. See the uninstall guides for Kimi Code and AWS CLI for details. Remember that deleting the local AWS configuration or CLI doesn’t by itself revoke IAM permissions or an active AWS session.
Amazon Bedrock inference for the models we showed is charged on a per-token basis, so there’s no persistent cloud infrastructure deployment to clean up.
Conclusion
We showed how Moonshot AI’s native bedrock provider in Kimi Code CLI v2.7.0 connects to Kimi K3.1 Pro Highspeed on Amazon Bedrock through the standard AWS credential chain. You no longer need a separately managed Amazon Bedrock API key.
Amazon Bedrock gives you access to open and proprietary AI models from leading providers, through standard APIs. Its governance controls and compliance validation programs can support even strictly regulated workloads.
If you’re already using Kimi Code CLI and want to run inference on AWS, upgrade today and give the new streamlined authentication a try.
For more information about Kimi K3.1 Pro on Amazon Bedrock, see our launch blog post and the Moonshot AI on AWS samples repository. To explore supported APIs and features by model, see the model cards in the Amazon Bedrock User Guide. To discuss your use case with the Amazon Bedrock team, connect with us.
