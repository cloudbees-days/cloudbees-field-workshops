# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Configuration as Code

In this lab we are going to explore [Configuration as Code (CasC) for CloudBees Core](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) and then we will setup GitOps for Core CasC so that any changes you make in source control will automatically be update in your Team Master. 

CasC for CloudBees Core consists of a colletion of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. bundle.yaml - This file is an index file that describes the bundle, and references the other files in the bundle.

## Enabling CasC for a Core Managed/Team Master
The `workshop-setup` job copied the YAML configuration files from your forked **core-config-bundle** repository to a sub-directory with the same name as your Team Master inside a special directory in the Jenkins home of the Core Operations Center from which you created your Team Master.

## Configuration Components

### Credentials
Secrets for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system.
  2. As Jenkins encrypted values used directly in the JCasC yaml configuration.

The `workshop-setup` job encrypted the GitHub Personal Access Token that you provided so it can only be decrypted by your Team Master and then replaced placeholders in your copy of the `jenkins.yaml` file. Other placeholders that were replaced were: `REPLACE_GITHUB_ORG` and `REPLACE_WITH_YOUR_GITHUB_USERNAME`. 

### Master Level Kubernetes Agent Templates
The CloudBees Kube Management plugin provides...

## GitOps for Core CasC
One of the main reasons to manage configurations as code is to allow it to be managed in source control like GitHub.
* Create a Jenkins Pipeline job on your Team Master to automatically update the Core configuration bundle for your Team Master.
* Add some configuration to the `jenkins.yaml` JCasC configuration in your **core-config-bundle** repository and commit the changes to tigger an update.

You may proceed to the next lab: [*Pipeline Template Catalogs*](../pipeline-template-catalog/pipeline-template-catalog.md) or choose another lab on the [main page](../../README.md#workshop-labs).




