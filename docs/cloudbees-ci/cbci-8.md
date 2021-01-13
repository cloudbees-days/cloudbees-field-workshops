name: contextual-feedback-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Contextual Feedback for Pipelines

---
name: agenda-setup
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. .blue-bold[Contextual Feedback for Pipelines]
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: contextual-feedback-overview

### CloudBees SCM Reporting for GitHub 

* The CloudBees SCM Reporting plugin supports detailed commit statuses for GitHub and BitBucket. 
* As the build runs, CloudBees CI will surface actionable build information directly in your source control tool, in real-time, alleviating the need to switch over to your CloudBees CI ***managed controller*** to get an overview.
* Integrates with GitHub Checks - as seen below.
<br><br>
.img-center[
![:scale 60%](img/pmd-annotations.png)
]

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