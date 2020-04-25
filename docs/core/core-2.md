name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Configuration as Code (CasC) for CloudBees Core

---
name: core-casc-overview

# CasC for Core Overview .badge-red[PREVIEW]

.no-bullet[
* 
* Configuration as Code (CasC) for CloudBees Core simplifies the management of a CloudBees Core cluster by capturing the configuration of Core Masters in human-readable declarative configuration files which can then be applied in a reproducible way. 
* By capturing the configuration in files, it can be treated as a first class revision-controlled artifact - versioned, tested, validated, and then applied to Masters while being centrally managed from CloudBees Core Operations Center.
* The configuration of a Core Master is defined in a collection of YAML files referred to as a *configuration bundle*.
* CasC for CloudBees Core expands on what is offered by OSS Jenkins CasC by enabling the management of **CasC at scale** across many Masters and including the **ability to manage plugins** for those Masters.
]

???
Make sure that attendees are aware that Core CasC is currently a preview feature.

A good question to ask is if anyone is already using Jenkins Config-as-Code?

---
name: core-casc-overview

# Core Configuration Bundle

CasC for CloudBees Core consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. `bundle.yaml` - provides a version for the bundle (which must be incremented for bundle updates), and references the other files in the bundle.
2. `jenkins.yaml` - contains the Jenkins configuration as defined by the OSS [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin) and supported CloudBees plugins.
3. `plugin-catalog.yaml` - provides a list of plugins that are **ALLOWED** to be installed on your Managed Master that are not already included as part of the CloudBees Assurance Program (CAP) Core plugins.
4. `plugins.yaml` - contains a list of all plugins that will be **INSTALLED/UPDATED** on the configured Managed Master - but plugins can only be installed if included via the `plugin-catalog.yaml` or if they are already included as CloudBees CAP plugins.

---
name: enable-casc
class: compact

# Enabling CasC for a Core Managed/Team Master

* The `workshop-setup` job that you ran in the *Core Workshop Setup* lab updated your forked copy of the `jenkins.yaml` file with your GitHub information and then copied the Core configuration bundle YAML files from your forked **core-config-bundle** repository to a sub-directory with the same name as your Team Master inside a special directory - the `jcasc-bundles-store` directory - in the Jenkins home of the Core Operations Center from which you created your Team Master. 
* Your Team Master was then *re-provisioned* in order for the Core configuration bundle to take effect.
* When the Core Operations Center is provisioning a Team Master it will check to see if there is a matching configuration for the name of the Team Master being provisioned and copy a Core configuration bundle link YAML file to `/var/casc-bundle/bundle-link.yaml` on your Team Master and set the value of the `core.casc.config.bundle` system property to match that file path.
* Your Team Master will then use that protected link to download the Core configuration bundle to your Team Master. The `jenkins.yaml` file will be downloaded from the OC to `/var/jenkins_home/core-casc-bundle/jenkins.yaml` and the `casc.jenkins.config` system property will be set to that file path.

---
name: config-bundle-details-yaml

# JCasC YAML

.no-bullet[
* The `jenkins.yaml` file provides Jenkins system and plugin configuration - as defined by the [OSS Jenkins Configuration as Code (JCasC) plugin](https://github.com/jenkinsci/configuration-as-code-plugin). Also note that many, but not all, CloudBees Core plugins support JCasC based configuration. 
* The following is an example of Jenkins credentials configuration via JCasC:
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
It is completely safe to include the actual secret here as it has been encrypted by the Jenkins instance and we will discuss JCasC credentials in further detail in the next slide.

---
name: config-bundle-details-credentials

# JCasC Credentials

Core CasC was used to create two user specific Jenkins credentials for use in the rest of this workshop.

.no-bullet[
* [JCasC Secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc) for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system. For secrets that you want to share across Team Masters you can mount the same [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to every Master.
  2. As Jenkins encrypted values using the Jenkins-internal secret key allowing the encrypted strings to be used directly in the  `jenkins.yaml` configuration as we are doing in this workshop. The Jenkins-internal secret key used for encryption is unique to a Jenkins instance and means that the credentials are not portable between Masters.
* The `workshop-setup` job used your Team Master Jenkins instance to encrypt your GitHub Personal Access Token that you provided and then updated your copy of the `jenkins.yaml` file with the encrypted value. This is perfectly secure as it can only be decrypted by your Team Master. 
]

---
name: config-bundle-details-additional
class: compact

# Additional JCasC Configuration
#### Pipeline Shared Library
.no-bullet[
* JCasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide the same Pipeline Shared Libraries across multiple teams - as we have done for this workshop. The Core Pipeline Shared Library was configured at the Jenkins global configuration level so that it will be available for all the Jenkins Pipeline jobs that you run on your Team Master for this workshop.
]
#### Other Configuration
* Installed the `antisamy-markup-formatter` plugin and configured your Team Master to use **Safe HTML** as the **Markup Formatter**
* Applied a **System Message** to your Team Master so you could see that the Core CasC bundle was applied
* Configured the GitHub plugin to manage webhooks for you using the `cbdays-github-token-secret` credential created
* Installed the `basic-branch-build-strategies` and `pipeline-utility-steps` that will be used in the next lab

---
name: core-casc-lab-link

# Lab - GitOps for Core CasC

.no-bullet[
* 
* One of the main reasons to manage configuration as code is to take advantage of features provided by source control tools - like GitHub webhooks for example. You don't want to have to execute any manual steps when you commit approved changes to your Core configuration. 
]

* In the following lab we will setup a Jenkins Pipeline job - or more specifically, a [Pipeline Organization Folder](https://jenkins.io/doc/book/pipeline/multibranch/#organization-folders) - on your Team Master that will be triggered whenever you commit any approved changes to the `**master**` branch of your Core configuration bundle repository.
* The GitOps for Core CasC lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md)

---
name: core-casc-lab-review

# CloudBees Core - Configuration as Code Lab Review

* You created a Pipeline job, via a GitHub Organization Folder project, that will update your Team Master configuration bundle whenever you commit any changes to the **master** branch of your fork of the **core-config-bundle** repository. This is GitOps for Jenkins configuration.
* Then, via the GitHub Pull Request you created and merged, your Team Master was updated with several plugins and configuration for some of those plugins.
* In the next sections and labs we will be exploring the functionality of those plugins and other features - to include:
  * Master specific Pod Templates for Kubernetes based agents
  * Pipeline Template Catalogs
  * Pipeline Policies
  * CloudBees GitHub Reporting
  * Cross Team Collaboration
  * Hibernating Masters

