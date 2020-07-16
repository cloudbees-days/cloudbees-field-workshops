name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Pipeline Template Catalogs

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Configuration as Code (CasC) with CloudBees CI
5. .blue-bold[Pipeline Manageability & Governance with Templates] and Policies
6. Cross Team Collaboration
7. Hibernating Masters

---
name: pipeline-template-catalog

# Pipeline Template Catalogs

Pipeline Template Catalogs provide version controlled parameterized templates for Multibranch and stand-alone Pipeline jobs, and help ensure that Pipeline jobs conform to organizational standards.

Benefits of using Pipeline Template Catalogs include:

* Providing developers with a simplified and directed experience for configuring Pipeline in “domain specific” terms that make sense for an organization. This allows developers to focus on shipping software.
* Organizing Pipelines per projects and/or teams. Similar-looking jobs that only differ in a few aspects can be easily parameterized on a per job basis. When you change a template, all the jobs created from that template get updated automatically.

When combined with Pipeline Shared Libraries, Pipeline Template Catalogs provide an easy way to make your organization's Pipelines reusable — boosting cross-team collaboration, saving time and reducing errors.

???
Pipeline Template Catalogs help ensure that Pipeline jobs conform to organizational standards and when used in combination with Shared Libraries provide reusable Pipelines — boosting cross-team collaborations, saving time and reducing errors.

Pipeline Shared Libraries and Pipeline Template Catalogs can 'live' in the same source code repository.

---
name: pipeline-template-catalog-lab-link

# Lab - Pipeline Template Catalog

* In this lab you will import a Pipeline Template Catalog from a repository that was forked in by the setup job and then create a job from one of the templates in that catalog.
* The *Pipeline Template Catalog* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-template-catalog/pipeline-template-catalog.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-template-catalog/pipeline-template-catalog.md)

---
name: pipeline-template-catalog-overview

# Pipeline Template Catalog Overview

* Imported a Pipeline Template Catalog from a GitHub repository
* Used a CloudBees Folders Plus feature to restrict what type of jobs can be created in a folder
* Leveraged CloudBees SCM Reporting for GitHub to find and fix an error

### CloudBees SCM Reporting for GitHub .badge-red[PRE-RELEASE]

* Whereas OSS github-branch-source plugin displays only build-level statuses, the CloudBees GitHub Reporting plugin provides more detailed Jenkins Pipeline events as corresponding GitHub statuses.
* As the build runs, CloudBees CI will surface status information about the build directly in GitHub, in real-time, alleviating the need to switch over to Jenkins to get an overview.

---
name: pipeline-template-catalog-slack

# CloudBees Slack Plugin .badge-red[PRE-RELEASE]

.img-left[
![CloudBees Slack Message](img/cloudbees-slack-post.png)
]

.img-right[
* Similar to the CloudBees SCM Reporting plugin, the CloudBees Slack plugin provides actionable build information inside of Slack.
* After a build runs, the CloudBees Slack plugin will surface results about the build directly in Slack, alleviating the need to switch over to Jenkins to get an overview.
* The Slack messages are sent directly to individual users based on who committed the code that triggered the CloudBees CI job.
]