name: contextual-feedback-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI Contextual Feedback for Pipelines

---
name: agenda-setup
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. .blue-bold[Contextual Feedback for Pipelines]
8. Cross Team Collaboration
9. Hibernating Managed Controllers

### CloudBees SCM Reporting for GitHub 

* The CloudBees GitHub Reporting plugin provides more detailed Jenkins Pipeline events as corresponding GitHub statuses.
* As the build runs, CloudBees CI will surface actionable build information directly in GitHub, in real-time, alleviating the need to switch over to your CloudBees CI managed controller to get an overview.

---
name: pipeline-template-catalog-slack

# CloudBees Slack Plugin 

.img-left[
![CloudBees Slack Message](img/cloudbees-slack-post.png)
]

.img-right[
* Similar to the CloudBees SCM Reporting plugin, the CloudBees Slack plugin provides actionable build information inside of Slack.
* After a build runs, the CloudBees Slack plugin will surface results about the build directly in Slack, alleviating the need to switch over to Jenkins to get an overview.
* The Slack messages are sent directly to individual users based on who committed the code that triggered the CloudBees CI job.
]

---
name: contextual-feedback-lab-link
class: compact

# Lab - Configuring and Interacting with Contextual Feedback

* In the following lab you will configure and interact with contextual Pipeline feedback for GitHub and Slack.
* The *Configuring and Interacting with Contextual Feedback* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/contextual-pipeline-feedback/