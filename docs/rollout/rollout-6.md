name: rollout-cac-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Rollout Configuration as Code

---
name: rollout-cac
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
