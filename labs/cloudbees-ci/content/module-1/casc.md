---
title: "Configuration as Code"
chapter: false
weight: 2
---

In this lab we will setup [GitOps](https://www.gitops.tech/) for [Configuration as Code (CasC) for CloudBees CI](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any CloudBeees CI configuration changes you make in source control will automatically be updated in your CloudBees CI managed controller (Jenkins instance). 

## GitOps for CloudBees CI CasC

In this lab you will:
* Create a Pipeline template job on your CloudBees CI managed controller to automatically update the [CloudBees CI configuration bundle](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/ci-casc-modern#_creating_a_configuration_bundle) for your CloudBees CI managed controller.
* Update the CloudBees CI configuration bundle in your forked **cloudbees-ci-config-bundle** repository and then commit the changes to the **master** branch of your **cloudbees-ci-config-bundle** repository that will in turn tigger the Pipeline template job.

1. Click on the **New Item** link in the left navigation menu.
2. Enter ***update-config-bundle** as the **Item Name**, select **CloudBees CI Configuration Bundle** as the item type and then click the **OK** button.<p><img src="github-organization-item.png" width=600/>
3. On the next screen, select the **Credentials** with the ***GitHub PAT from JCasC - username/password*** description and displaying your GitHub username - this credential was created with the CloudBees CI CasC bundle applied to your CloudBees CI managed controller by the **cloudbees-ci-workshop-setup** job.
4. The value of the **Owner** field is already filled in and matching the **Item Name** you entered above - ensure that it matches the name of the GitHub Organization you created for this workshop.
5. Next, under the **Behaviors** section, click the **Add** button, select **Filter by name (with wildcards)** under **- Within repository -** and then enter ***master*** as an **Include** so that will be the only branch that gets scanned and built. **IMPORTANT** - make sure you select the **Filter by name (with wildcards)** option **UNDERNEATH** the **- Within repository -** section of the **Behaviors** select list. <p><img src="behaviors-filter-branch-by-name.png" width=900/>
6. Click the **Build strategies** **Add** button and select ***Skip initial build on first branch indexing*** from the drop-down. 
7. Finally, click the **Save** button.<p><img src="organization-folder-save.png" width=900/>
8.  After you click the **Save** button the Organization Folder Pipeline project will scan every branch of every repository of your GitHub Organization creating a Pipeline job for each branch where there is a `Jenkinsfile` (or in this case, just the **master** branch) and creating a [Pipeline Multibranch project](https://jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) for each repository where there is at least one branch containing a `Jenkinsfile`. Once the scan is complete, click on the breadcrumb link that matches your GitHub Organization name - just to the left of **Scan Organization**.<p><img src="click-org-folder-link.png" width=600/>
9.  Click on the link of the Jenkins Multibranch Pipeline project for your fork of the **cloudbees-ci-config-bundle** repository.<p><img src="core-config-bundle-multibranch.png" width=700/>
10. Next, navigate to your fork of the **cloudbees-ci-config-bundle** repository on GitHub by clicking on the **GitHub** link in the left navigation menu. <p><img src="casc-github-link.png" width=700/>
11. In GitHub, click on the **Pull requests** tab and then click on the **GitOps lab updates** pull request. <p><img src="gitops-lab-pr.png" width=700/>
12. To quickly review the changes that will be made to your CloudBees CI configuration bundle for your CloudBees CI managed controller, click on the **Files changed** tab and scroll down to see the differences. <p><img src="pr-files-changed.png" width=800/>
13. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. <p><img src="merge-pr.png" width=800/>
14. Now navigate to the **master** branch Pipeline job of the **cloudbees-ci-config-bundle** Multibranch Pipeline project on your CloudBees CI managed controller. <p><img src="nav-to-core-config-bundle-job.png" width=800/>
15. As the job to update your CloudBees CI CasC bundle is running, let's explore the configuration changes in more detail. Navigate back to your fork of the **cloudbees-ci-config-bundle** repository on GitHub and open the `jenkins.yaml` file.
16. Navigate back to your CloudBees CI CloudBees CI managed controller. Shortly after the Pipeline job completes you will see a new **monitor** warning. Click on the **monitor** link of your CloudBees CI managed controller and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. NOTE: If you do not see the **Reload Configuration** button then click the **Safe Restart** button. <p><img src="reload-config.png" width=800/>
17. Among other configuration changes, you will now see a link for **Pipeline Polices** in the left navigation menu, an updated system message and [CloudBees CI Hibernation for Managed Controllers](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) has been configured for your CloudBees CI managed controller. <p><img src="casc-update-applied.png" width=800/>

>NOTE: The **Build strategies** configuration for Pipeline Organization Folder and Multibranch projects are provided by the [Basic Branch Build Strategies plugin](https://github.com/jenkinsci/basic-branch-build-strategies-plugin/blob/master/docs/user.adoc) and by selecting the *Skip initial build on first branch indexing* strategy we avoid an unnecessary build when we first create the Organization Folder project above.

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#26)**
