name: casc-dev-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Configuration as Code for Developers

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
7. <a class="no-style" href="#rbac-casc-title">Delegating Administration with RBAC</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. .blue-bold[Configuration as Code (CasC) for Developers]
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: dev-casc-overview
class: compact

# Configuration as Code for Developers

.no-bullet[
* 
* Giving all the developers in your organization configuration access to CloudBees CI (Jenkins) is a recipe for chaos and instability of your continuous integration pipelines with unstable and untested plugins being installed and other insecure non-conformant misconfigurations. But with CloudBees CI Configuration as Code (CasC) you can provide an easily manageable Git based workflow for developers to have the CloudBees CI configuration they need.
* 
]
### Changes Through Pull Requests

* Any new configuration requests for a CloudBees CI ***managed controller*** must be done by opening a new pull request (PR). 
* That PR will trigger automated tests and since managed controllers can be treated as ephemeral resources you can easily and quickly spin up a managed controller on your Kubernetes cluster to test those configuration changes before they are allowed to be merged to the `main` branch. 
* Once the PR is merged the targeted managed controller will be updated to reflect the configuration in source control.

---
name: casc-for-devs-lab-link
class: compact

# Labs - CloudBees CI Configuration as Code for Developers

* In the following labs:
  *  You will review and merge a pull requests for your *managed controller* to add configuration that will enable the CloudBees CI Slack notifications for your user.
* The *CloudBees CI Configuration as Code for Developers* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/casc-for-developers/
