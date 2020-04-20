name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Configuration as Code (CasC) 
## for CloudBees Core

---
name: core-casc-overview

# CasC for Core Overview

.no-bullet[
* Configuration as Code (CasC) for CloudBees Core simplifies the management of a CloudBees Core cluster by capturing the configuration of Core Masters in human-readable declarative configuration files which can then be applied in a reproducible way. 
* By capturing the configuration in files, it can be treated as a first class revision-controlled artifact - versioned, tested, validated, and then applied to Masters while being centrally managed from CloudBees Core Operations Center.
]

---
name: core-casc-overview

# Core Configuration Bundle

CasC for CloudBees Core consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. `bundle.yaml` - This file describes the bundle, and references the other files in the bundle.
2. `jenkins.yaml` - This file contains the Jenkins configuration as defined by the OSS [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin) and supported CloudBees plugins.
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
name: config-bundle-details-yaml

# JCasC YAML

.no-bullet[
* The `jenkins.yaml` file provides all of the Jenkins system and plugin configuration - that is currently supported and primarily relies on the [OSS Jenkins Configuration as Code (JCasC) plugin](https://github.com/jenkinsci/configuration-as-code-plugin) for the OSS system and plugin configuration that is supported. Also note that some, but not all, CloudBees Core plugins support JCasC based configuration. The following is an example of Jenkins credentials configuration via JCasC:
]

```yaml
credentials:
  system:
    - credentials:
      - string:
          description: "GitHub PAT from JCasC - secret text"
          id: "cbdays-github-token-secret"
          scope: GLOBAL
          secret: "{AQAAABAAAAAwhY0iqxnrlWCCLvk+2TLChLxlT}"
```
???
NOTE: It is completely safe to include the actual secret here as it has been encrypted by the Jenkins instance this particular credentials is targeted for and we will discuss JCasC credentials in further detail in the next slide.
---
name: config-bundle-details-credentials

# JCasC Credentials

Core CasC was used to create two user specific Jenkins credentials for use in the rest of this workshop.

.no-bullet[
* [JCasC Secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc) for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system. For secrets that you want to share across Team Masters you can mount the same [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to every Master.
  2. As Jenkins encrypted values using the Jenkins-internal secret key allowing the encrypted strings to be used directly in the  `jenkins.yaml` configuration as we are doing in this workshop. The Jenkins-internal secret key used for encryption is unique for to Jenkins instance and means that the credentials are not portable between Team Masters.
* The `workshop-setup` job used Jenkins to encrypt the GitHub Personal Access Token that you provided so it can only be decrypted by your Team Master and then replaced the `REPLACE_WITH_JENKINS_ENCODED_PAT` placeholders in your copy of the `jenkins.yaml` file with the Jenkins encrypted value of your GitHub Personal Access Token. 
]

---
name: config-bundle-details-additional
class: compact

# Additional JCasC Configuration

#### Pipeline Shared Library

.no-bullet[
* JCasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide the same Pipeline Shared Libraries across multiple teams - as we have done for this workshop. The Core Pipeline Shared Library was configured at the Jenkins global configuration level so that it will be available for all the Jenkins Pipeline that you run on your Team Master.
]

#### Master Level Kubernetes Agent Templates

.no-bullet[
* The CloudBees Kube Management plugin allows you to [configure Kubernetes Pod Templates for agents at the Team/Master level](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/agents#_editing_pod_templates_per_team_using_masters) but still manage the Kubernetes cluster configuration for Kuberentes based agents at the Core Operations Center level.
]

---
name: gitops-for-casc

# GitOps for Core CasC

.no-bullet[
* One of the main reasons to manage configuration as code is to take advantage of features provided by source control tools - like GitHub webhooks for example. You don't want to have to execute any manual steps when you commit approved changes to your Core configuration. 
* In the following lab we will setup a Jenkins Pipeline job - or more specifically, a [Pipeline Organization Folder](https://jenkins.io/doc/book/pipeline/multibranch/#organization-folders) - on your Team Master that will be triggered whenever you commit any approved changes to the `**master**` branch of your Core configuration bundle repository.
]

---
name: core-casc-lab-link
# Lab - CloudBees Core - GitOps for Core CasC

The lab is available at the following URL: 
[https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md)

---
name: core-casc-lab-review

# CloudBees Core - Configuration as Code Lab Review

You added configuration and reload the Core configuration bundle for your Team Master.