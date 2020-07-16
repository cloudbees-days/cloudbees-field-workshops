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
4. Configuration as Code (CasC) with CloudBees CI
5. Pipeline Manageability & Governance with Templates and Policies
6. Cross Team Collaboration
7. Hibernating Masters

---
name: core-setup-overview
# CloudBees CI Workshop Setup

Setup for this workshop will include:

* Creating a CloudBees CI Jenkins instance referred to as a [Team Master](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/cje-ux).
* Setting up a GitHub.com user account that will be used throughout the workshop. If you have an existing GitHub.com account you will be able to use that account if you are comfortable using that account to create a GitHub Organization and a GitHub Personal Access Token for use in this workshop.
* Creating a Github Personal Access Token that you will use within your Team Masters (Jenkins instance) to connect Pipelines, Multibranch Pipelines, and Github Organization Projects to your Github organization and repositories created for this workshop.
* Creating a GitHub organization to use for this workshop.

---
name: core-setup-lab
# Lab - CloudBees CI Workshop Setup

* Today's URL for the CloudBees CI Workshop cluster will be provided by your instructor.
* The *Core Workshop Setup* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/workshop-setup/workshop-setup.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/workshop-setup/workshop-setup.md)

---
name: core-setup-review
class: compact

# CloudBees CI Workshop Setup Review

While your Team Master is restarting, let's explore the results of the **`core-workshop-setup`** Pipeline:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 5 repositories. The following repositories were [forked](https://guides.github.com/activities/forking/) from the [CloudBees Days GitHub Organization](https://github.com/cloudbees-days) by the `core-workshop-setup` job you just ran on your Team Master:
   1. **core-config-bundle** - this repository provides a base CasC configuration for everyones' Team Master.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   4. **microblog-frontend** - a vue.js sample application to be used for this workshop.
   5. **microblog-backend** - a Python sample application to be used in conjunction with the **microblog-frontend** application to be used with this workshop.
* Your CloudBees CI Team Master was also setup to use CloudBees CI configuration as code as we will explore next.
]

???
The `core-workshop-setup` job also created three GitHub pull requests to streamline the labs where they are used.