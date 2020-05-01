name: rollout-cac-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Rollout Configuration as Code

---
name: rollout-cac-overview
# Rollout Configuration as Code

Configuration as Code (CasC) allows the entire configuration of Rollout’s state to be stored as source code.

* The Rollout integration with Git code management service includes a bi-directional connection with your repository.
* If you make changes in your repository and push it to the remote origin branch, Rollout will pick these updates and update the dashboard accordingly.
* If you make changes in the dashboard, Rollout will push commits into your branches.

---
name: rollout-cac-advantages
# Advantages of Configuration as Code

Versioning and Traceability of changes
* You can store CasC in a version control system, such as Git, to see who changed what and when in your production environment. You can use tags to mark specific version. You can use branches to isolate changes to rollback in time and to work in parallel streams without affecting your production/Staging environment.
* You can track which changes have been applied to your production environment. Analyzing configuration differences (e.g. via git diff) is quite often more convenient and efficient than reading audit logs in Rollout dashboard.

Smooth promotion of changes from test to production
* CloudBees Rollout uses a git branch for each environment e.g. production, staging, development. Promoting changes from these environments using git native merging or GitHub pull request is simpler than clicking through many UI pages, testing that everything works and next tediously repeating the same steps on the production instance. With configuration as code you can simply deploy plans to a test instance, verify changes and then deploy to the production instance just by merging back the code.

---
name: rollout-cac-lab
# Lab - Configuration as Code

* The *Rollout Configuration as Code* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rollout-cac/rollout-cac.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rollout-cac/rollout-cac.md)

---
name: rollout-cac-review
# Configuration as Code Overview

* Created a new GitHub repository and connected your Rollout app to the repo.
* Copied the sidebar experiment from the Development environment to the Production environment.
* Modified experiment via Rollout dashboard in Development environment and noted the change in GitHub `Development` branch.
* Merged `Development` branch with `Master` and noted the updated experiment in the production environment.

With Configuration as Code set up, you can now lock down the Production environment in Rollout so that no one can make changes via dashboard. Instead, Production can only be modified by pull request which allows you to use GitOps to its full potential. 
