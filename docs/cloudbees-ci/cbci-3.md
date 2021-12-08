name: casc-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Configuration as Code (CasC) 

---
name: agenda-setup
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. .blue-bold[Configuration as Code (CasC) with CloudBees CI]
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. <a class="no-style" href="#rbac-casc-title">Delegating Administration with RBAC</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: core-casc-overview

# CasC for CloudBees CI Overview

.no-bullet[
* 
* Configuration as Code (CasC) for CloudBees CI simplifies the management of a CloudBees CI cluster by capturing the configuration of CloudBees CI Operations Center and ***managed controllers*** (Jenkins instances) in human-readable declarative configuration files which can then be applied in a reproducible way and managed as code. 
* By capturing the configuration in files, it can be treated as a first class revision-controlled artifact - versioned, tested, validated, and then applied to a *managed controller* while being centrally managed from CloudBees CI Operations Center.
* The configuration of a CloudBees CI *managed controller* is defined in a collection of YAML files referred to as a *configuration bundle*.
* CasC for CloudBees CI expands on what is offered by OSS Jenkins CasC by enabling the management of **CasC at scale** across many *managed controllers* and including the **ability to manage plugins** and **job configuration** for all of your team specific *managed controllers*.
]

???
A good question to ask is if anyone is already using Jenkins Config-as-Code?

---
name: core-casc-overview
class: compact

# CloudBees CI Configuration Bundle

CasC for CloudBees CI consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes six files:

1. `bundle.yaml` - provides a version for the bundle and references the other files in the bundle.
2. `jenkins.yaml` - contains the Jenkins configuration as defined by the OSS [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin) and supported CloudBees plugins.
3. `plugin-catalog.yaml` *optional* - provides a list of plugins that are **ALLOWED** to be installed on your *managed controllers* that are not already included as part of the CloudBees Assurance Program (CAP) Core plugins.
4. `plugins.yaml` *optional* - contains a list of all plugins that will be **INSTALLED/UPDATED** on the configured *managed controllers* - but plugins can only be installed if included via the `plugin-catalog.yaml` or if they are already included as CloudBees CAP plugins.
5. `rbac.yaml` *optional* - contains RBAC configuration for individual managed controllers.
6. `items.yaml` *optional* - contains configuration for items to be created on managed controller.

---
name: enable-casc
class: compact

# Enabling CasC for a CloudBees CI Managed Controllers (Jenkins instance)

* After you installed the CloudBees CI Workshop GitHub App into your workshop GitHub Organization a customized configuration bundle was created in your copy of the **cloudbees-ci-config-bundle** repository was copied to a special sub-directory (`jcasc-bundles-store`) on CloudBees CI Operations Center with a **bundle name** configured to be available for your *managed controller*. 
* When the CloudBees CI Operations Center is provisioning a *managed controller* it will check to see if there is a bundle available and configured for the *managed controller* being provisioned to use and copy a CloudBees CI configuration bundle link YAML file to `/var/casc-bundle/bundle-link.yaml` on your *managed controller* and set the value of the `core.casc.config.bundle` system property to match that file path.
* Your *managed controller* uses that protected link to download the CloudBees CI configuration bundle to your *managed controller*. The `jenkins.yaml` (and other bundler yaml files) file were downloaded from the CloudBees CI Operations Center to the `/var/jenkins_home/core-casc-bundle/` directory and the `casc.jenkins.config` system property was set to the `jenkins.yaml` file path.

---
name: config-bundle-details-yaml

# JCasC YAML

.no-bullet[
* The `jenkins.yaml` file provides Jenkins system and plugin configuration - as defined by the [OSS Jenkins Configuration as Code (JCasC) plugin](https://github.com/jenkinsci/configuration-as-code-plugin). Also note that most CloudBees CI plugins support JCasC based configuration. 
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
  1. As properties files in the Managed Jenkins file system. For secrets that you want to share across ***managed controller*** you can mount the same [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to every *managed controller*.
  2. As Jenkins encrypted values using the Jenkins-internal secret key allowing the encrypted strings to be used directly in the  `jenkins.yaml` configuration as we are doing in this workshop. The Jenkins-internal secret key used for encryption is unique to a Jenkins instance and means that the credentials are not portable between Jenkins instances.
* For the CloudBees CI Workshop we have mounted Kubernetes `Secrets` to each of your *managed controller* for use with the GitHub, Slack and cross team collaboration integrations.
]

---
name: config-bundle-details-additional

# Additional JCasC Configuration
#### Pipeline Shared Library
.no-bullet[
* JCasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide the same Pipeline Shared Libraries across multiple teams - as we have done for this workshop. The CloudBees CI Pipeline Shared Library was configured at the Jenkins global configuration level so that it will be available for all the Jenkins Pipeline jobs that you run on your *managed controller* for this workshop.
]
#### Other Configuration
* Applied a **System Message** to your *managed controller* so you could see that the CloudBees CI CasC bundle was applied
* Created a *managed controller* level Kubernetes Pod Template for use in a later lab.
* Installed several plugins to be used in the rest of the workshop.

---
name: core-casc-lab-link

# Lab - GitOps for CloudBees CI CasC

.no-bullet[
* 
* One of the main reasons to manage configuration as code is to take advantage of features provided by source control tools - like GitHub webhooks for example. You don't want to have to execute any manual steps when you commit approved changes to your CloudBees CI configuration. 
]

* In the following lab we will update a Jenkins Pipeline job - or more specifically, a **Pipeline Template** based job on your ***managed controller*** that will be triggered whenever you commit any approved changes to the **`main`** branch of your CloudBees CI configuration bundle repository.
* The *GitOps for CloudBees CI CasC* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-1/casc/
  
???

If you show off the Kubernetes pod templates view, talk about our kube agent plugin which brings enhancements to the open source plugin.

---
name: casc-lab-review

# CloudBees CI - GitOps for CloudBees CI CasC Lab Review

* You created a Pipeline job, via a GitHub Organization Folder project, that will update your ***managed controller*** configuration bundle whenever you commit any changes to the **`master`** branch of your fork of the **`cloudbees-ci-config-bundle`** repository. This is GitOps for Jenkins configuration.
* Then, via the GitHub Pull Request, you merged the CloudBees CI CasC bundle for your *managed controller*, and finally you applied an update that included several new plugins and configuration for some of those plugins.
* In the next sections and labs we will be exploring the functionality of those plugins and other features - to include:
  * CloudBees CI *managed controller* specific Pod Templates for Kubernetes based agents
  * Pipeline Template Catalogs
  * Pipeline Policies
  * CloudBees SCM Reporting for GitHub
  * Cross Team Collaboration
  * Hibernating Managed Controllers

