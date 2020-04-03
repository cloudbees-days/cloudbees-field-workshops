# <img src="https://mms.businesswire.com/media/20191204005250/en/760213/23/Logo_-_Stacked_-_Full_Color%402x.jpg" width="100" align="top"> CloudBees Core-Rollout-Flow Integration Workshop
This workshop serves to demonstrate how to  effectively use CI/CD practices, manage feature flags, and orchestrating releases through a close integration of CloudBees' Core, Rollout, and Flow products, respectively.

The workshop is divided into 2 parts. The first will focus on the use of Core and Rollout with the latter concentrating on Rollout and Flow usage.

# Workshop Prerequisites

* Internet access to include access to https://github.com and to include the ability to access and use the [GitHub File Editor](https://help.github.com/articles/editing-files-in-your-repository).
* Access to https://app.slack.com 
* An account on https://github.com and a basic understanding of how to use GitHub to do things like fork a repository, edit files in the web UI, and create pull requests.
* A basic understanding of Docker: https://docs.docker.com/get-started/
* A basic understanding of Kubernetes: https://kubernetes.io/docs/tutorials/kubernetes-basics/
* A basic understanding of Jenkins Pipelines: https://jenkins.io/doc/book/pipeline/getting-started/
* A basic understanding of feature flags: https://rollout.io/blog/ultimate-feature-flag-guide/

# Workshop Labs
## Core:
 * [Lab 1 - Core Setup](labs/core-workshop-setup/workshop-setup.md)
 * [Lab 2 - Configuration as Code (CasC) for CloudBees Core](labs/core-casc/core-casc.md)
 * [Lab 3 - Pipeline Template Catalogs & Pipeline Policies](labs/pipeline-template-catalog/pipeline-template-catalog.md)
 * [Lab 4 - Hibernating Masters](labs/hibernating-masters/hibernating-masters.md) 
 * [Lab 5 - Cross Team Collaboration](labs/cross-team-collaboration/cross-team-collaboration.md)
 * [Lab 6 - Preview Environment](labs/core-preview-environment/catalog-templates.md)


## Rollout: 
 * [Lab 1 - Setting Up CloudBees Rollout](labs/rolloutSetup/rolloutSetup.md)
 * [Lab 2 - Adding a Sidebar to the Microblog](labs/rolloutFeature/rolloutFeature.md)
 * [Lab 3 - Control the Value of a Feature Flag](labs/rolloutExperiment/rolloutExperiment.md)
 * Lab 4 - User Targeting
 * Lab 5 - Analytics and A/B testing
 * Lab 6 - Feature Flag GitOps



## Flow:
Coming soon...
 * Lab 1 - Create release pipeline from service catalog
 * Lab 2 - Add gates to the release pipeline
 * Lab 3 - Merge into master and run through release pipeline
 * Lab 4 - Check out the live app, close the ticket, observe flow Dashboard
