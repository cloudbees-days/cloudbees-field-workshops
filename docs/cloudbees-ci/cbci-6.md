name: contextual-feedback-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Configuration as Code for Developers

---
name: agenda-setup
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. Using Pipeline Templates
8. .blue-bold[Configuration as Code (CasC) for Developers]
9. Contextual Feedback for Pipelines
10. Cross Team Collaboration
11. Hibernating Managed Controllers

---
name: dev-casc-overview
class: compact

# Configuration as Code for Developers

Giving all the developers in your organization configuration access to CloudBees CI (Jenkins) is a recipe for chaos and instability of your continuous integration pipelines with unstable and untested plugins being installed and other insecure non-conformant misconfigurations. But with CloudBees CI Configuration as Code (CasC) you can provide an easily manageable Git based workflow for developers to have the CloudBees CI configuration they need.


### Changes Through Pull Requests

Any new configuration requests for a CloudBees CI ***managed controller*** must be done by opening a new pull request (PR). That PR will trigger automated tests and since ***managed controllers*** can be treated as ephemeral resources you can easily and quickly spin up a ***managed controller*** to test those configuration changes before they are allowed to be merged to the `main` branch. Once the PR is merged the targeted ***managed controller*** will be updated to reflect the configuration in source control.

---
name: casc-for-devs-lab-link
class: compact

# Labs - CloudBees CI Configuration as Code for Developers

* In the following labs:
  *  You will review and merge a pull requests for your ***managed controller*** to add configuration that will enable the CloudBees CI Slack notifications for your user.
* The *CloudBees CI Configuration as Code for Developers* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/casc-for-developers/
