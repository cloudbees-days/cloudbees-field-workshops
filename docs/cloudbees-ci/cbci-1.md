name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI Workshop Setup

---
name: agenda-setup
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. .blue-bold[Setup for Labs]
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. Contextual Feedback for Pipelines
8. Cross Team Collaboration
9. Hibernating Managed Controllers

---
name: core-setup-overview
# CloudBees CI Workshop Setup

The pre-setup for this workshop consisted of:
* Setting up a GitHub.com user account that will be used throughout the workshop. If you have an existing GitHub.com account you will be able to use that account if you are comfortable using that account to create a GitHub Organization and a GitHub Personal Access Token for use in this workshop.
* Creating a GitHub organization to use for this workshop.
* Install the CloudBees CI Workshop GitHub App into your workshop GitHub Organization.

Each of you  will now provision your own (team specific) CloudBees CI managed Jenkins instance we refer to as a [***managed controller***](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters).

---
name: core-setup-lab
# Lab - CloudBees CI Setup
In this lab you will create a CloudBees CI account and then provision a CloudBees CI managed controller.

* Today's URL for the CloudBees CI Workshop cluster will be provided by your instructor.
* The *CloudBees CI Workshop Setup* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/getting-started/provision-controller/

---
name: core-setup-review
class: compact

# CloudBees CI Workshop Setup Review

While your ***managed controller*** is restarting, let's explore the results of the workshop setup:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 4 repositories. The following repositories were [forked](https://guides.github.com/activities/forking/) from the [CloudBees Days GitHub Organization](https://github.com/cloudbees-days) when you installed the **CloudBees CI Workshop** GitHub App into your workshop GitHub Organization:
   1. **cloudbees-ci-config-bundle** - this repository provides a base CasC configuration for everyones' ***managed controller***.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   4. **simple-java-maven-app** - a simple Java project using Maven, used to highlight contextual Pipeline feedback.
* Your CloudBees CI ***managed controller*** was also setup to use CloudBees CI configuration as code as we will explore after the next section on Pipeline Template Catalogs.
]
