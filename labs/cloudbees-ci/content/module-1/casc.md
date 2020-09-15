---
title: "Configuration as Code"
chapter: false
weight: 2
---

In this lab we will setup [GitOps](https://www.gitops.tech/) for [CloudBees CI Configuration as Code (CasC) ](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any CloudBeees CI configuration changes you make in source control will automatically be updated in your CloudBees CI ***managed controller*** (Jenkins instance). 

## GitOps for CloudBees CI CasC

In this lab you will:
* Create a job from a Pipeline template on your CloudBees CI ***managed controller*** to automatically update the [CloudBees CI configuration bundle](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/ci-casc-modern#_creating_a_configuration_bundle) for your CloudBees CI ***managed controller***. 
* Update the CloudBees CI configuration bundle in your forked `cloudbees-ci-config-bundle` repository and then commit the changes to the **master** branch of your `cloudbees-ci-config-bundle` repository that will in turn tigger the Pipeline template job.

1. Navigation into the **template-jobs** folder on your ***managed controller***.
2. Click on the **New Item** link in the left navigation menu.
3. Enter ***config-bundle-ops*** as the **Item Name**, select **CloudBees CI Configuration Bundle** as the item type and then click the **OK** button. ![New Update Bundle](new-bundle-template-job.png?width=50pc)
4. On the next screen, fill in the **GitHub Organization** template parameter with the name of the GitHub Organization you created for this workshop (all the other default values should be correct) and then click the **Save** button. ![Config Bundle Template Parameters](bundle-template-params.png?width=50pc) 
5.  After you click the **Save** button the Multibranch Pipeline project (created by the template) will scan your fork of the `cloubees-ci-config-bunlde` repository, creating a Pipeline job for each branch where there is a marker file that matched `bundle.yaml` (or in this case, just the `PR-1` Pull Request). Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan. ![Scan Log](bundle-scan-log.png?width=50pc) 
6.  Next, click on the **config-bundle-ops** link in the menu at the top of page and you will see that there are no jobs for **Branches** and 4 jobs for **Pull Requests**.  Click on the **Pull Requests** tab. ![Scan Log](bundle-no-branch-jobs.png?width=50pc) 
7.  In the **Pull Requests** view of your Multibranch project click on the link for **PR-1**. ![PR-1 Link](pr-link.png?width=50pc)
8.  On the build screen for **PR-1** click on the **GitHub** link in the left navigation menu that will take you to the pull request page in GitHub. ![PR-1 GitHub Link](pr-github-link.png?width=50pc)
9.  To review the changes that will be made to your CloudBees CI configuration bundle for your CloudBees CI ***managed controller***, click on the **Files changed** tab and scroll down to see the differences. 
    - The `version` of the `bundle.yaml` file was updated to **2**, **it is important to note that this is required to trigger a reload of the configuration bundle from CloudBees CI Operations Center to your** ***managed controller***.
    - The `cloudbees-pipeline-policies` plugin, that we will need for the next lab, was added to the `plugins.yaml` file. ![Scan Log](pr-files-changed.png?width=50pc)
10. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. ![Merge PR](merge-pr.png?width=50pc)
11. On the next screen click the **Delete branch** button.
12. Navigate back to your CloudBees CI ***managed controller*** by clicking on the **Code** tab of your `cloudbees-ci-config-bundle` repository, click on the commit status (a small orange dot or green check), and then click on the **Details** link for the **continuous-integration/jenkins/branch** check. ![Commit Check link](commit-check-link.png?width=50pc)
13. You will now have a Pipeline job for the `master` branch of your fork of the `cloudbees-ci-config-bundle` repository. Shortly after the Pipeline job completes navigate to the top-level of your ***managed controller***. ![Config Update Complete](config-update-complete.png?width=50pc)
14. Click on the **monitor** link of your CloudBees CI ***managed controller*** (if you don't see a monitor alert then refresh your browser as it may take a minute or two for it to appear) and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. NOTE: If you do not see the **Reload Configuration** button then click the **Safe Restart** button. ![Reload CasC](reload-config.png?width=50pc)
15. Navigate back to the top-level of your ***managed controller***. Among other configuration changes, you will now see a link for **Pipeline Polices** in the left navigation menu and an updated system message for your CloudBees CI ***managed controller***. ![New CasC applied](casc-update-applied.png?width=50pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#31">return to the workshop slides</a>**
