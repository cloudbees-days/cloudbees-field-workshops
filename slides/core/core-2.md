name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Configuration as Code (CasC) 
## for CloudBees Core

---
name: core-casc-overview

# CasC for Core Overview

CasC for CloudBees Core consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. `bundle.yaml` - This file is an index file that describes the bundle, and references the other files in the bundle.
2. `jenkins.yaml` - This file contains the Jenkins configuration as defined by the OSS [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin).
3. `plugin-catalog.yaml` - This file provides a list of plugins that are **ALLOWED** to be installed on your Managed Master that are not already part of the allowed CAP Core plugins.
4. `plugins.yaml` - This file contains a list of all plugins that will be **INSTALLED** on the configured Managed Master - but they can only be installed if allowed via the `plugin-catalog.yaml` or they are allowed CAP plugins.

???
* The `bundle.yaml` basically defines the configuration bundle.
* It is kind of hard to explain the difference between the `plugin-catalog.yaml` and the `plugins.yaml` - basically the `plugin-catalog` is a required component of CAP.
---
name: enable-casc
class: compact

## Enabling CasC for a Core Managed/Team Master

* The `workshop-setup` job that you ran in the *Core Workshop Setup* lab modified the `jenkins.yaml` file and then copied the Core configuration bundle YAML files from your forked **core-config-bundle** repository to a sub-directory with the same name as your Team Master inside a special directory - the `jcasc-bundles-store` directory - in the Jenkins home of the Core Operations Center from which you created your Team Master. 
* Your Team Master was then *re-provisioned* in order for the Core configuration bundle to take effect.
* When the Core Operations Center is provisioning a Team/Managed Master it will check to see if there is a matching configuration for the name of the Team/Managed Master being provisioned and copy that Core configuration bundle link YAML file to `/var/casc-bundle/bundle-link.yaml` on your Team Master and set the value of the `core.casc.config.bundle` system property to match that file path.
* Your Team Master will then use that protected link to download the Core configuration bundle to your Team Master. The `jenkins.yaml` file will be downloaded from the OC to `/var/jenkins_home/core-casc-bundle/jenkins.yaml` and the `casc.jenkins.config` system property will be set to that file path.

---
name: config-bundle-details
## Configuration Bundle Details

### jenkins.yaml
The `jenkins.yaml` provides all of the Jenkins system and plugin configuration - that is currently supported and primarily relies on the [OSS Jenkins Configuration as Code (JCasC) plugin](https://github.com/jenkinsci/configuration-as-code-plugin) for the OSS system and plugin configuration that is supported. Also note that some, but not all, CloudBees Core plugins support JCasC based configuration.

#### Credentials
Core CasC was used to create two user specific Jenkins credentials for use in the rest of this workshop.

[JCasC Secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc) for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system. For secrets that you want to share across Team Masters you can mount the same [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to every Master.
  2. As Jenkins encrypted values using the Jenkins-internal secret key allowing the encrypted strings to be used directly in the  `jenkins.yaml` configuration as we are doing in this workshop. The Jenkins-internal secret key used for encryption is unique for to Jenkins instance and means that the credentials are not portable between Team Masters.

The `workshop-setup` job used Jenkins to encrypt the GitHub Personal Access Token that you provided so it can only be decrypted by your Team Master and then replaced the `REPLACE_WITH_JENKINS_ENCODED_PAT`placeholders in your copy of the `jenkins.yaml` file with the Jenkins encrypted value of your GitHub Personal Access Token. Other placeholders that were replaced were: `REPLACE_GITHUB_ORG` with the GitHub Organization your created for the workshop and `REPLACE_WITH_YOUR_GITHUB_USERNAME` with the GitHub username you are using for this workshop. 

#### Pipeline Shared Library
CasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide the same Pipeline Shared Libraries across multiple teams as we have done in this workshop. The Core Pipeline Shared Library was configured at the global level so that it will be available to all the Jenkins Pipeline that you run on your Team Master.

#### Master Level Kubernetes Agent Templates
The CloudBees Kube Management plugin allows you to [configure Kubernetes Pod Templates for agents at the Team/Master level](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/agents#_editing_pod_templates_per_team_using_masters) but still managed the Kubernetes cluster configuration for Kuberentes based agents at the Core Operations Center level. Several Kubernetes Pod Templates were added to your Team Master via your Core configuration bundle.
---
name: gitops-for-casc

## GitOps for Core CasC
One of the main reasons to manage configurations as code is to allow it to be managed in source control. But you still don't want to have to execute any manual steps when you make approved changes to your configuration. In the following we will setup a Jenkins Pipeline job - or more specifically, a [Pipeline Organization Folder](https://jenkins.io/doc/book/pipeline/multibranch/#organization-folders) - on your Team Master that will be triggered whenever you commit any approved changes to the `**master**` branch of your Core configuration bundle repository.

---
name: core-casc-lab-link
## Lab - CloudBees Core - Configuration as Code

[https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md)