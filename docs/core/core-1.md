name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Core Workshop Setup

---
name: core-setup-overview
# Core Workshop Setup

Setup fo this workshop will include:

* Creating a CloudBees Core Jenkins instance referred to as a [Team Master](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/cje-ux).
* Setting up a GitHub.com user account that will be used throughout the workshop. If you have an existing GitHub.com account you will be able to use that account if you are comfortable using that account to create a GitHub Organization and a GitHub Personal Access Token for use in this workshop.
* Creating a Github Personal Access Token that you will use within your Team Masters (Jenkins instance) to connect Pipelines, Multibranch Pipelines, and Github Organization Projects to your Github organization and repositories created for this workshop.
* Creating a GitHub organization to use for this workshop.

---
name: core-setup-lab
# Lab - Core Workshop Setup

* Today's URL for the CloudBees Core Workshop cluster is:
  * https://workshop.cb-sa.io/cjoc/
* The *Workshop Setup* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-workshop-setup/workshop-setup.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/core-workshop-setup/workshop-setup.md)

---
name: core-setup-review
class: compact

# Core Workshop Setup Review

While your Team Master is restarting, let's explore the results of the `workshop-setup` Pipeline:

.no-bullet[
* In the GitHub Organization that you created for this workshop you will notice that you now have 5 repositories. The following repositories were [forked](https://guides.github.com/activities/forking/) from the [CloudBees Days GitHub Organization](https://github.com/cloudbees-days) by the `workshop-setup` job you just ran on your Team Master:
   1. **core-config-bundle** - this repository provides a base CasC configuration for everyones' Team Master.
   2. **pipeline-library** - a Jenkins Pipeline Shared Library that will be used by the Jenkins Pipelines you create during this workshop.
   3. **pipeline-template-catalog** - a set of templated Pipelines that you will use to create Jenkins Pipeline jobs for this workshop.
   4. **microblog-frontend** - a vue.js sample application to be used for this workshop.
   5. **microblog-backend** - a Python sample application to be used in conjunction with the **microblog-frontend** application to be used with this workshop.
* Your Core Team Master was also setup to use Core configuration as code.
]
