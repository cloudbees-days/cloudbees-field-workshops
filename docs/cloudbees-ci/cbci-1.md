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

Each of you  will now provision your own (team specific) CloudBees CI managed Jenkins instance referred to as a [***managed controller***](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters).

---
name: core-setup-lab
# Lab - CloudBees CI Workshop Setup

* Today's URL for the CloudBees CI Workshop cluster will be provided by your instructor.
* The *CloudBees CI Workshop Setup* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/getting-started/workshop-setup/ 

---
name: core-setup-review
class: compact

# CloudBees CI Workshop Setup Review

While your ***managed controller*** is restarting, let's explore the results of the **`cloudbees-ci-workshop-setup`** Pipeline:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 5 repositories. The following repositories were [forked](https://guides.github.com/activities/forking/) from the [CloudBees Days GitHub Organization](https://github.com/cloudbees-days) by the `cloudbees-ci-workshop-setup` job you just ran on your ***managed controller***:
   1. **cloudbees-ci-config-bundle** - this repository provides a base CasC configuration for everyones' ***managed controller***.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   4. **simple-java-maven-app** - 
* Your CloudBees CI ***managed controller*** was also setup to use CloudBees CI configuration as code as we will explore next.
]

???
The `cloudbees-ci-workshop-setup` job also created three GitHub pull requests to streamline the labs where they are used.