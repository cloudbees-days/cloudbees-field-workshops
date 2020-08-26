# <img src="https://mms.businesswire.com/media/20191204005250/en/760213/23/Logo_-_Stacked_-_Full_Color%402x.jpg" width="100" align="top"> CloudBees Field Workshops
These workshop labs demonstrate how to  effectively use CI/CD practices, manage feature flags, and orchestrating releases with CloudBees CI, CloudBees Feature Flags, and CloudBees CD products.

# Workshop Prerequisites

* Internet access to include access to https://github.com and to include the ability to access and use the [GitHub File Editor](https://help.github.com/articles/editing-files-in-your-repository).
* Access to https://app.slack.com
* An account on https://github.com and a basic understanding of how to use GitHub to do things like fork a repository, edit files in the web UI, and create pull requests.
* A basic understanding of Docker: https://docs.docker.com/get-started/
* A basic understanding of Kubernetes: https://kubernetes.io/docs/tutorials/kubernetes-basics/
* A basic understanding of Jenkins Pipelines: https://jenkins.io/doc/book/pipeline/getting-started/
* A basic understanding of feature flags: https://rollout.io/blog/ultimate-feature-flag-guide/
* Finally, we highly recommend using the Google Chrome browser to work through the lab content.

# Workshop Labs & Slides

[Workshop Setup for all workshops](labs/workshop-setup/workshop-setup.md)


## CloudBees CI:

The CloudBees CI workshop is composed of two distinct sets of labs. The first is focused on product capabilities that make it easy to manage continuous integration at scale and the second is focused on features that provide a developer centric experience for software delivery. 

### Manage Continuous Integration at Scale
These labs will provide hands-on examples that will show you how CloudBees CI enables shared services teams and Jenkins admins to provide highly scalable and easily manageable continuous integration for all of your software delivery teams. You will learn how CloudBees CI provides comprehensive centralized team management with features to manage Jenkins configuration as code, create and share templates for Jenkins pipelines, enforce pipeline policies and simplify collaboration across disparate development teams.

### A Developer Centric Experience
These labs will provide hands-on examples that will show you how CloudBees CI enables developers to spend less time on admin tasks and more time coding. These labs will explore how the CloudBee CI developer centric features provide contextual Jenkins pipeline feedback, in tools such as GitHub and Slack, resulting in less context-switching. These labs will also explore how the scalability and central management of CloudBees CI allows developers to focus on writing and delivering software without being slowed down by their continuous integration tools and processes.

### Slides
https://cloudbees-days.github.io/core-rollout-flow-workshop/core/

### Labs
https://cloudbees-ci.labs.cb-sa.io/

>NOTE: If you are returning to the workshop cluster to complete a lab please review this lab on [**Un-hibernating a Managed Controller**](labs/hibernating/hibernating.md#un-hibernate-a-managed-jenkins-instance).

## CloudBees Feature Flags:

### Slides
https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/

If you did not attend the CloudBees CI Workshop or go through the above labs, please follow [these instructions](labs/rolloutPreReqs/rolloutPreReqs.md) before proceeding to Lab 1 below.

### Labs
 * [Lab 1 - CloudBees Feature Flags Workshop Setup](labs/cloudbees-feature-flags/setup/setup.md)
 * [Lab 2 - Gating Code with CloudBees Feature Flags](labs/cloudbees-feature-flags/feature/feature.md)
 * [Lab 3 - Controlling the Value of a Feature Flag](labs/cloudbees-feature-flags/experiment/experiment.md)
 * [Lab 4 - User Targeting](labs/cloudbees-feature-flags/targeting/targeting.md)
 * [Lab 5 - CloudBees Feature Flags Configuration as Code](labs/cloudbees-feature-flags/cac/cac.md)
 * [Lab 6 - CloudBees Feature Flags and Analytics](labs/cloudbees-feature-flags/analytics/analytics.md)




## CloudBees CD:
Coming soon...
 * Lab 1 - Create release pipeline from a service catalog
 * Lab 2 - Add gates to the release pipeline
 * Lab 3 - Merge into master and run through release pipeline
 * Lab 4 - Check out the live app, close the ticket, observe CloudBees CD Dashboard
