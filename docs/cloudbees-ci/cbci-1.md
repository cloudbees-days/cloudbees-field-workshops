name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Workshop Setup

---
name: agenda-setup
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. .blue-bold[Setup for Labs]
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. <a class="no-style" href="#rbac-casc-title">Delegating Administration with RBAC</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: core-setup-overview
class: compact

# CloudBees CI Workshop Setup

If you haven't already done the pre-workshop setup then do it now: https://cloudbees-ci.labs.cb-sa.io/getting-started/pre-workshop-setup/ 

The pre-workshop setup consisted of:
* Setting up a GitHub.com user account that will be used throughout the workshop. If you have an existing GitHub.com account you will be able to use that account if you are comfortable using that account to create a GitHub Organization for use in this workshop.
* Creating a GitHub Organization to use for this workshop.
* Installing the [CloudBees CI Workshop GitHub App](https://github.com/apps/cloudbees-ci-workshop) into your workshop GitHub Organization triggering a CloudBees CI job that:
  * Installed several repositories into your workshop GitHub Organization.
  * Created a CloudBees CI (Jenkins) account for you.
  * Provisioned a (attendee specific) CloudBees CI managed Jenkins instance we refer to as a [***managed controller***](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters).

---
name: core-setup-lab
# Lab - CloudBees CI Setup
In this lab you will login into your CloudBees CI managed controller (enterprise Jenkins instance).

* If the URL for the CloudBees CI Workshop cluster was not already provided to you, then it will be provided by your instructor.
* The *CloudBees CI Workshop Setup* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/getting-started/cloudbees-ci-login/

---
name: cbci-setup-review
class: compact

# CloudBees CI Workshop Setup Review

Let's explore the results of the workshop setup:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 4 repositories. The following repositories were [copied from templates](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) from the [CloudBees Field Workshops GitHub Organization](https://github.com/cloudbees-days) when you installed the **CloudBees CI Workshop** GitHub App into your workshop GitHub Organization:
   1. **cloudbees-ci-config-bundle** - this repository provides a base CasC configuration for everyones' ***managed controller***.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   4. **simple-java-maven-app** - a simple Java project using Maven, used to highlight contextual Pipeline feedback.
* Your CloudBees CI ***managed controller*** was also setup to use CloudBees CI configuration as code, which we will explore in more detail after the next section on Pipeline Template Catalogs.
]
