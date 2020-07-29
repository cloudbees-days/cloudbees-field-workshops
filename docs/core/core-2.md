name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Configuration as Code (CasC) for CloudBees CI

---
name: agenda-setup
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. .blue-bold[Configuration as Code (CasC) with CloudBees CI]
5. Pipeline Manageability & Governance with Templates and Policies
6. Cross Team Collaboration
7. Hibernating Managed Jenkins Instances


---
name: core-casc-overview

# CasC for CloudBees CI Overview .badge-red[PREVIEW]

.no-bullet[
* 
* Configuration as Code (CasC) for CloudBees CI simplifies the management of a CloudBees CI cluster by capturing the configuration of CloudBees CI Managed Jenkins instances in human-readable declarative configuration files which can then be applied in a reproducible way. 
* By capturing the configuration in files, it can be treated as a first class revision-controlled artifact - versioned, tested, validated, and then applied to Managed Jenkins instances while being centrally managed from CloudBees CI Operations Center.
* The configuration of a CloudBees CI Managed Jenkins instance is defined in a collection of YAML files referred to as a *configuration bundle*.
* CasC for CloudBees CI expands on what is offered by OSS Jenkins CasC by enabling the management of **CasC at scale** across many Managed Jenkins instances and including the **ability to manage plugins** for those Managed Jenkins instances.
]

???
Make sure that attendees are aware that CloudBees CI CasC is currently a preview feature.

A good question to ask is if anyone is already using Jenkins Config-as-Code?

---
name: core-casc-overview

# CloudBees CI Configuration Bundle

CasC for CloudBees CI consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. `bundle.yaml` - provides a version for the bundle (which must be incremented for bundle updates), and references the other files in the bundle.
2. `jenkins.yaml` - contains the Jenkins configuration as defined by the OSS [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin) and supported CloudBees plugins.
3. `plugin-catalog.yaml` - provides a list of plugins that are **ALLOWED** to be installed on your Managed Jenkins instances that are not already included as part of the CloudBees Assurance Program (CAP) Core plugins.
4. `plugins.yaml` - contains a list of all plugins that will be **INSTALLED/UPDATED** on the configured Managed Jenkins instances - but plugins can only be installed if included via the `plugin-catalog.yaml` or if they are already included as CloudBees CAP plugins.

---
name: enable-casc

# Enabling CasC for a CloudBees CI Managed/Team (Managed Jenkins Instance)

* The `core-workshop-setup` job that you ran in the *CloudBees CI Workshop Setup* lab updated your forked copy of the `jenkins.yaml` file with your GitHub information and then copied the Core configuration bundle YAML files from your forked **core-config-bundle** repository to a sub-directory with the same name as your Team (Jenkins instance) inside a special directory - the `jcasc-bundles-store` directory - in the Jenkins home of the CloudBees CI Operations Center from which you created your Team (Jenkins instance). 
* Your Team (Jenkins instance) was then *re-provisioned* in order for the CloudBees CI configuration bundle to take effect.
* When the CloudBees CI Operations Center is provisioning a Team (Jenkins instance) it will check to see if there is a matching configuration for the name of the Team (Jenkins instance) being provisioned and copy a CloudBees CI configuration bundle link YAML file to `/var/casc-bundle/bundle-link.yaml` on your Team (Jenkins instance) and set the value of the `core.casc.config.bundle` system property to match that file path.
* Your Team (Jenkins instance) will then use that protected link to download the CloudBees CI configuration bundle to your Team (Jenkins instance). The `jenkins.yaml` file will be downloaded from the OC to `/var/jenkins_home/core-casc-bundle/jenkins.yaml` and the `casc.jenkins.config` system property will be set to that file path.

---
name: config-bundle-details-yaml

# JCasC YAML

.no-bullet[
* The `jenkins.yaml` file provides Jenkins system and plugin configuration - as defined by the [OSS Jenkins Configuration as Code (JCasC) plugin](https://github.com/jenkinsci/configuration-as-code-plugin). Also note that many, but not all, CloudBees CI plugins support JCasC based configuration. 
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

CloudBees CI CasC was used to create two user specific Jenkins credentials for use in the rest of this workshop.

.no-bullet[
* [JCasC Secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc) for credentials can be managed in a few different ways:
  1. As properties files in the Managed Jenkins file system. For secrets that you want to share across Team (Jenkins instance) you can mount the same [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to every Managed Jenkins instance.
  2. As Jenkins encrypted values using the Jenkins-internal secret key allowing the encrypted strings to be used directly in the  `jenkins.yaml` configuration as we are doing in this workshop. The Jenkins-internal secret key used for encryption is unique to a Jenkins instance and means that the credentials are not portable between Jenkins instances.
* The `cloudbees-ci-workshop-setup` job used your Team (Jenkins instance) Jenkins instance to encrypt your GitHub Personal Access Token that you provided and then updated your copy of the `jenkins.yaml` file with the encrypted value. This is perfectly secure as it can only be decrypted by your Team (Jenkins instance). 
]

---
name: config-bundle-details-additional

# Additional JCasC Configuration
#### Pipeline Shared Library
.no-bullet[
* JCasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide the same Pipeline Shared Libraries across multiple teams - as we have done for this workshop. The CloudBees CI Pipeline Shared Library was configured at the Jenkins global configuration level so that it will be available for all the Jenkins Pipeline jobs that you run on your Team (Jenkins instance) for this workshop.
]
#### Other Configuration
* Applied a **System Message** to your Team (Jenkins instance) so you could see that the CloudBees CI CasC bundle was applied
* Installed the `basic-branch-build-strategies` and `pipeline-utility-steps` plugins to be used in the next lab

---
name: core-casc-lab-link

# Lab - GitOps for CloudBees CI CasC

.no-bullet[
* 
* One of the main reasons to manage configuration as code is to take advantage of features provided by source control tools - like GitHub webhooks for example. You don't want to have to execute any manual steps when you commit approved changes to your CloudBees CI configuration. 
]

* In the following lab we will setup a Jenkins Pipeline job - or more specifically, a [Pipeline Organization Folder](https://jenkins.io/doc/book/pipeline/multibranch/#organization-folders) - on your Team (Jenkins instance) that will be triggered whenever you commit any approved changes to the **`master`** branch of your CloudBees CI configuration bundle repository.
* The *GitOps for CloudBees CI CasC* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-casc/core-casc.md)
  
???

If you show off the Kubernetes pod templates view, talk about our kube agent plugin which brings enhancements to the open source plugin.

---
name: core-casc-lab-review

# CloudBees CI - GitOps for CloudBees CI CasC Lab Review

* You created a Pipeline job, via a GitHub Organization Folder project, that will update your Team (Jenkins instance) configuration bundle whenever you commit any changes to the **`master`** branch of your fork of the **`cloudbees-ci-config-bundle`** repository. This is GitOps for Jenkins configuration.
* Then, via the GitHub Pull Request, you merged the CloudBees CI CasC bundle for you Team (Jenkins instance) was updated, and finally you applied that update that included several new plugins and configuration for some of those plugins.
* In the next sections and labs we will be exploring the functionality of those plugins and other features - to include:
  * Managed Jenkins instance specific Pod Templates for Kubernetes based agents
  * Pipeline Template Catalogs
  * Pipeline Policies
  * CloudBees SCM Reporting for GitHub
  * Cross Team Collaboration
  * Hibernating Managed Jenkins Instances

