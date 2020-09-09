name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Workshop Setup

---
name: agenda-setup
class: compact

# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. .blue-bold[Setup for Labs]
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. A Developer Centric Experience
8. Using Pipeline Templates
9. Configuration as Code (CasC) for Developers
10. Contextual Feedback for Pipelines
11. Cross Team Collaboration
12. Hibernating Managed Controllers

---
name: core-setup-overview
class: compact

# CloudBees CI Workshop Setup

If you haven't already done the pre-workshop setup then do it now: https://cloudbees-ci.labs.cb-sa.io/getting-started/pre-workshop-setup/ 

The pre-workshop setup consisted of:
* Setting up a GitHub.com user account that will be used throughout the workshop. If you have an existing GitHub.com account you will be able to use that account if you are comfortable using that account to create a GitHub Organization for use in this workshop.
* Creating a GitHub organization to use for this workshop.
* Installing the CloudBees CI Workshop GitHub App into your workshop GitHub Organization which will trigger a CloudBees CI job that will:
  * Install several repositories, to used in the workshop labs, into your workshop GitHub Organization.
  * A CloudBees CI (Jenkins) account was created for you.
  * A (team specific) CloudBees CI managed Jenkins instance we refer to as a [***managed controller***](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters) was provisioned for each of you.

---
name: core-setup-lab
# Lab - CloudBees CI Setup
In this lab you will login into your CloudBees CI managed controller.

* If the URL for the CloudBees CI Workshop cluster has not already been provided then it will be provided by your instructor.
* The *CloudBees CI Workshop Setup* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/getting-started/cloudbees-ci-login/

---
name: core-setup-review
class: compact

# CloudBees CI Workshop Setup Review

While your ***managed controller*** is restarting, let's explore the results of the workshop setup:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 5 repositories. The following repositories were [copied from templates](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) from the [CloudBees Field Workshops GitHub Organization](https://github.com/cloudbees-days) when you installed the **CloudBees CI Workshop** GitHub App into your workshop GitHub Organization:
   1. **cloudbees-ci-config-bundle** - this repository provides a base CasC configuration for everyones' ***managed controller***.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-policies** - used for the Pipeline Policies GitOps lab.
   4. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   5. **simple-java-maven-app** - a simple Java project using Maven, used to highlight contextual Pipeline feedback.
* Your CloudBees CI ***managed controller*** was also setup to use CloudBees CI configuration as code as we will explore after the next section on Pipeline Template Catalogs.
]
