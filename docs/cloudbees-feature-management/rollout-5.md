name: rollout-cac-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Feature Management<br>Configuration as Code

---
name: rollout-cac-overview
# CloudBees Feature Management Configuration as Code

Configuration as Code (CasC) allows the entire configuration of CloudBees Feature Management state to be stored as source code.

* The CloudBees Feature Management integration with Git code management service includes a bi-directional connection with your repository.
* If you make changes in your repository and push it to the remote origin branch, CloudBees Feature Management will pick these updates and update the dashboard accordingly.
* If you make changes in the dashboard, CloudBees Feature Management will push commits into your branches.

---
name: rollout-cac-advantages
# Advantages of Configuration as Code

Versioning and traceability of changes
* You can store CasC in a version control system, such as Git, to see who changed what and when in your production environment. You can use tags to mark specific version. You can use branches to isolate changes to rollback in time and to work in parallel streams without affecting your production/staging environment.
* You can track which changes have been applied to your production environment. Analyzing configuration differences (e.g. via git diff) is quite often more convenient and efficient than reading audit logs in the CloudBees Feature Management dashboard.

Smooth promotion of changes from test to production
* CloudBees Feature Management  uses a git branch for each environment e.g. production, staging, development. Promoting changes from these environments using git native merging or GitHub pull request is simpler than clicking through many UI pages, testing that everything works and next tediously repeating the same steps on the production instance. With configuration as code you can simply deploy plans to a test instance, verify changes and then deploy to the production instance just by merging the code back to the `master` branch.

---
name: rollout-cac-architecture
class: middle, center

# Config as Code Architecture Overview
![:scale 75%](img/rollout_cac_arch.jpg)

---
name: rollout-cac-lab
# Lab - Configuration as Code

* The *CloudBees Feature Management Configuration as Code* lab instructions are available at:
  * https://cloudbees-feature-flags.labs.cb-sa.io/labs/cac/ 

---
name: rollout-cac-review
# Configuration as Code Lab Review

* You created a new GitHub repository and connected your CloudBees Feature Management app to the repo.
* In the CloudBees Feature Management dashboard, you disabled the sidebar experiment in Development environment by toggling `Active` to `Killed`.
* Within the Github code editor, you modified `default.sidebar.yml` to re-enable the feature in the CloudBees Feature Management dashboard.
* Finally, you merged `Development` branch with `master` and noted the promotion of the sidebar and title experiments to the production environment.

With Configuration as Code set up, you can now lock down the Production environment in CloudBees Feature Management so that no one can make changes via dashboard. Instead, Production can only be modified by pull request which allows you to use GitOps to its full potential.
