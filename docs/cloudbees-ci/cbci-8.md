name: contextual-feedback-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Contextual Feedback for Pipelines

---
name: agenda-setup
class: compact

# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. A Developer Centric Experience
8. Using Pipeline Templates
9. Configuration as Code (CasC) for Developers
10. .blue-bold[Contextual Feedback for Pipelines]
11. Cross Team Collaboration
12. Hibernating Managed Controllers

---
name: contextual-feedback-overview
class: compact

### CloudBees SCM Reporting for GitHub 

* The CloudBees SCM Reporting plugin supports detailed commit statuses for GitHub and BitBucket. 
* As the build runs, CloudBees CI will surface actionable build information directly in your source control tool, in real-time, alleviating the need to switch over to your CloudBees CI ***managed controller*** to get an overview.

---
name: pipeline-template-catalog-slack

# CloudBees Slack Plugin 

.img-left[
![CloudBees Slack Message](img/cloudbees-slack-post.png)
]

.img-right[
* Similar to the CloudBees SCM Reporting plugin, the CloudBees Slack plugin provides actionable build information as Slack messages.
* After a build runs *for a GitHub Pull Request*, the CloudBees Slack plugin will surface results about the build directly in Slack, alleviating the need to switch over to your CloudBees CI ***managed controller*** (Jenkins instance) to get an overview.
* The Slack messages are sent directly to individual users based on who committed the code that triggered the CloudBees CI job.
]

.footnote[.bold[*] CloudBees recently released a preview version of our new CloudBees CI Microsoft Teams plugin.]

---
name: contextual-feedback-lab-link
class: compact

# Lab - Configuring and Interacting with Contextual Feedback

* In the following lab you will configure and interact with contextual Pipeline feedback for GitHub and Slack.
* The *Configuring and Interacting with Contextual Feedback* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/contextual-pipeline-feedback/