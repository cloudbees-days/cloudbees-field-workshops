name: rbac-casc-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Delegating Administration with RBAC

---
name: agenda-templates
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. .blue-bold[Delegating Administration with RBAC]
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: rbac-casc

# Delegating Administration with CloudBees CI RBAC

* [Delegating administration with CloudBees CI RBAC](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/delegating-administration-modern) allows organizations to delegate the level of administration avaialbe through the UI. Two new permissions were introduced in Jenkins v2.222 to allow for a more granual control of permissions allowing different levels of administration versus the previous `Overall/Administration` permission that enabled all permissions.
* The two new permissions include:
  * **Overall/Manage:** safely grant a user the ability to manage a subset of CloudBees CI configuration options.
  * **Overall/SystemRead:** grant a user the ability to view most of CloudBees CI configuration options, but in read only mode.
* These new permissions are currently *Experimental* and disabled by default. They can be [enabled via corresponding system properties or with corresponding dedicated plugins](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/delegating-administration-modern#_enabling_the_new_permissions). We recommend using the system properties as you never want to install additional plugins if not necessary. 

---
name: rbac-casc-lab-link
class: compact

# Labs - Delegating Administration with CloudBees CI RBAC

* In the following labs:
  * You will use CasC to create an RBAC configuration that will reduce the administrative permissions of your user in the UI - delegating you to a *manager* role.
  * The permission will still allow your user to approve/reload updated configuration bundles.
* The *Delegating Administration with CloudBees CI RBAC* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-1/rbac-casc/


---
name: rbac-casc-overview

# Delegating Administration with CloudBees CI RBAC Overview

* CasC was used to create an RBAC configuration for your managed controller that delegated you to a *manager* role that enforces the use of CasC from source control for managing the configuration of your managed controller.
