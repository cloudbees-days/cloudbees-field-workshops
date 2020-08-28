---
title: "Configuration as Code"
chapter: false
weight: 2
---

In this lab we will setup [GitOps](https://www.gitops.tech/) for [CloudBees CI Configuration as Code (CasC) ](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any CloudBeees CI configuration changes you make in source control will automatically be updated in your CloudBees CI ***managed controller*** (Jenkins instance). 

## GitOps for CloudBees CI CasC

In this lab you will:
* Create a job from a Pipeline template on your CloudBees CI managed controller to automatically update the [CloudBees CI configuration bundle](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/ci-casc-modern#_creating_a_configuration_bundle) for your CloudBees CI managed controller. 
* Update the CloudBees CI configuration bundle in your forked `cloudbees-ci-config-bundle` repository and then commit the changes to the **master** branch of your **cloudbees-ci-config-bundle** repository that will in turn tigger the Pipeline template job.

1. Navigation into the **template-jobs** folder on your ***managed controller***.
2. Click on the **New Item** link in the left navigation menu.
3. Enter ***update-config-bundle*** as the **Item Name**, select **CloudBees CI Configuration Bundle** as the item type and then click the **OK** button. ![New Update Bundle](new-bundle-template-job.png?width=50pc)
4. On the next screen, fill in the **GitHub Organization** template parameters (all the other default values should be correct) and then click the **Save** button. ![Config Bundle Template Parameters](bundle-template-params.png?width=50pc) 
5.  After you click the **Save** button the Multibranch Pipeline project created by the template will scan your fork of the `cloubees-ci-config-bunlde` repository, creating a Pipeline job for each branch where there is a marker file that matched `bundle.yaml` (or in this case, just the `PR-1` Pull Request). Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan. ![Scan Log](bundle-scan-log.png?width=50pc) 
6.  Next, click on the **update-config-bundle** link in the menu at the top of page and you should see a Pipeline job for the `master` branch of your `cloudbees-ci-config-bundle` repository fork.
7.  You will see that there are no jobs for **Branches** and 2 jobs for **Pull Requests**.  Click on the **Pull Requests** tab. ![Scan Log](bundle-no-branch-jobs.png?width=50pc) 
8.  In the **Pull Requests** view of your Multibranch project click on the link for **PR-1**. ![PR-1 Link](pr-link.png?width=50pc)
9.  On the build screen for **PR-1** click on the **GitHub** link in the left navigation menu that will take you to the pull request page in GitHub. ![PR-1 GitHub Link](pr-github-link.png?width=50pc)
10. To quickly review the changes that will be made to your CloudBees CI configuration bundle for your CloudBees CI managed controller, click on the **Files changed** tab and scroll down to see the differences. 
    - The `version` of the `bundle.yaml` file was updated to **2**, this is required to trigger a reload of the configuration bundle from CloudBees CI Operations Center to your ***managed controller***.
    - The `cloudbees-pipeline-policies` plugin was added to the `plugins.yaml` file. ![Scan Log](pr-files-changed.png?width=50pc)
11. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. ![Merge PR](merge-pr.png?width=50pc)
12. Navigate back to your CloudBees CI managed controller and then to the **update-config-bundle** Multibranch Pipeline project under the **template-jobs** folder. ![Scan Log](nav-to-core-config-bundle-job.png?width=50pc)
13. You will now have a Pipeline job for the `master` branch of your fork of the `cloudbees-ci-config-bundle` repository. Shortly after the Pipeline job completes you will see a new **monitor** warning. Click on the **monitor** link of your CloudBees CI managed controller and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. NOTE: If you do not see the **Reload Configuration** button then click the **Safe Restart** button. ![Scan Log](reload-config.png?width=50pc)
14. Among other configuration changes, you will now see a link for **Pipeline Polices** in the left navigation menu, an updated system message and [CloudBees CI Hibernation for Managed Controllers](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) has been configured for your CloudBees CI managed controller. ![Scan Log](casc-update-applied.png?width=50pc)
>NOTE: The **Build strategies** configuration for Pipeline Organization Folder and Multibranch projects are provided by the [Basic Branch Build Strategies plugin](https://github.com/jenkinsci/basic-branch-build-strategies-plugin/blob/master/docs/user.adoc) and by selecting the *Skip initial build on first branch indexing* strategy we avoid an unnecessary build when we first create the Organization Folder project above.

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#26)**
