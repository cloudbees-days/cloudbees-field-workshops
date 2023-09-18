---
title: "Setup"
chapter: false
weight: 1
---

{{% notice warning %}}
If you completed **Module 1** then skip this setup.
{{% /notice %}}

For those attendees that did not complete **Module 1** we need to update the configuration of your CloudBees CI ***managed controller*** to match what was completed in **Module 1**. 

1. Once your CloudBees CI *managed controller* is up, navigate to your copy of the `cloudbees-ci-config-bundle` repository in your workshop GitHub Organization, click on the **Pull requests** tab and then click on the **CloudBees CI Module 2 Setup** pull request. ![Module 2 Pull request](module-2-pull-request.png?width=50pc)
2. On the pull request screen click on the **Merge pull request** button, then click the **Confirm merge** button and finally click the **Delete branch** button. ![Merge PR](merge-pr.png?width=50pc)
4. Navigate back to your CloudBees CI ***managed controller***, refresh the page and you should see a **template-jobs** folder and an updated system message for your CloudBees CI managed controller showing that you are on *v2* of the CloudBees CI CasC bundle. ![Updated config](updated-config.png?width=50pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#using-templates-title">return to the workshop slides</a>**
