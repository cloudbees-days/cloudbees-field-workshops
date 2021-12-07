---
title: "Configuration as Code"
chapter: false
weight: 2
---

In this lab we will setup [GitOps](https://www.gitops.tech/) for [CloudBees CI Configuration as Code (CasC) ](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any CloudBeees CI configuration changes you make in source control will be made available to reload in your CloudBees CI ***managed controller*** (Jenkins instance). 

## GitOps for CloudBees CI CasC

In this lab you will:
* Update the CloudBees CI configuration bundle in your copy of the `cloudbees-ci-config-bundle` repository and then commit the changes to the **main** branch of your that will in turn trigger the Pipeline template job.
* Update the ***CloudBees CI Configuration Bundle*** Pipeline Catalog template to use CloudBees CI Cross Team Collaboration feature to trigger a job on another controller, with permissions to use `kubectl` to copy files to the Operations Center `pod`, by publishing a notification event.

1.  After you click the **Save** button, the Multibranch Pipeline project (created by the template) will scan your copy of the `cloubees-ci-config-bunlde` repository, creating a Pipeline job for each branch where there is a marker file that matched `.markerfile` as specified in the `template.yaml` of the ***CloudBees CI Configuration Bundle*** template (just the open Pull Requests have that file and will be scanned in). Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan. ![Scan Log](bundle-scan-log.png?width=50pc) 
2.  Next, click on the **config-bundle-ops** link in the menu at the top of page and you will see that there are no jobs for **Branches** and 5 jobs for **Pull Requests**.  Click on the **Pull Requests** tab. ![Scan Log](bundle-no-branch-jobs.png?width=50pc) 
3.  In the **Pull Requests** view of your Multibranch project click on the link for **PR-1**. ![PR-1 Link](pr-link.png?width=50pc)
4.  On the build screen for **PR-1** click on the **GitHub** link in the left navigation menu that will take you to the pull request page in GitHub. ![PR-1 GitHub Link](pr-github-link.png?width=50pc)
5.  To review the changes that will be made to your CloudBees CI configuration bundle for your CloudBees CI ***managed controller***, click on the **Files changed** tab and scroll down to see the differences. 
    - The `version` of the `bundle.yaml` file was updated to **2**, **it is important to note that this is required to trigger a reload of the configuration bundle from CloudBees CI Operations Center to your** ***managed controller***.
    - The `cloudbees-pipeline-policies` plugin, that we will need for the next lab, was added to the `plugins.yaml` file. ![Scan Log](pr-files-changed.png?width=50pc)
6. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. ![Merge PR](merge-pr.png?width=50pc)
7. On the next screen click the **Delete branch** button.
8. Navigate back to your CloudBees CI ***managed controller*** and then navigate to the ***main*** branch job of your **config-bundle-ops** Multi-branch Project in the **template-jobs** folder.

{{% notice note %}}
A job was created for the `main` branch of your copy of the `cloudbees-ci-config-bundle` repository because when you merged the pull request it added the `.markerfile` to your `main` branch and that triggered the ***config-bundle-ops*** Multibranch Pipeline template to create the job.
{{% /notice %}}

9. The job will fail with the following error:

```
Error from server (Forbidden): pods "cjoc-0" is forbidden: User "system:serviceaccount:controllers:jenkins" cannot get resource "pods" in API group "" in the namespace "cbci"
```
10. The reason you get this error is because your **controller** has been provisioned to a different Kubernetes `namespace` than Operations Center and no agent `pod` in the `controllers` namespace will have the permissions to copy files with `kubectl` to the Operations Center `cjoc-0` `pod`.
11. You will now have a Pipeline job for the `main` branch of your copy of the `cloudbees-ci-config-bundle` repository. After the Pipeline job successfully completes navigate to the top-level of your ***managed controller***. ![Config Update Complete](config-update-complete.png?width=50pc)
14. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code export and update** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
15.  On the next screen, click on the **Bundle Update** link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. 

{{% notice note %}}
If you don't see the new version available then click the **Check for Updates** button. Also, once you click **Yes** it will take a few minutes for the bundle update to reload.
{{% /notice %}}
![Bundle Update](new-bundle-available.png?width=50pc)

16. Navigate back to the top-level of your ***managed controller***. Among other configuration changes, you will now see a link for **Pipeline Polices** in the left navigation menu and an updated system message for your CloudBees CI managed controller. ![New CasC applied](casc-update-applied.png?width=50pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#casc-lab-review">return to the workshop slides</a>**
