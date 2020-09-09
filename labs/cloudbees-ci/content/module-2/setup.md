---
title: "Setup"
chapter: false
weight: 1
---

For those attendees that did not complete **Module 1** we need to update the configuration of your CloudBees CI ***managed controller*** to match what was completed in **Module 1**.

1. In GitHub, navigate to your copy of the `cloudbees-ci-config-bundle` repository, click on the **Pull requests** tab and then click on the **CloudBees CI Module 2 Setup** pull request. ![Module 2 Pull request](module-2-pull-request.png?width=50pc)
2. On the pull request screen click on the **Merge pull request** button, then click the **Confirm merge** button and finally click the **Delete branch** button. ![Merge PR](merge-pr.png?width=50pc)
3. Navigate back to your CloudBees CI managed controller and click on the monitor link of your CloudBees CI managed controller (if you don’t see a monitor alert than refresh your browser as it may take a minute or two for it to appear). ![Reload CasC](reload-config.png?width=50pc)
4. Navigate back to the top-level of your ***managed controller***. Among other configuration changes, you will now see a **template-jobs** folder and an updated system message for your CloudBees CI ***managed controller*** showing that you are on *v2* of the CloudBees CI CasC bundle. ![Updated config](updated-config.png?width=50pc)


