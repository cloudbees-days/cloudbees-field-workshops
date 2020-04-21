# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - GitOps for Core CasC

In this lab we will setup [GitOps](https://www.gitops.tech/) for [Configuration as Code (CasC) for CloudBees Core](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any Jenkins configuration changes you make in source control will automatically be updated in your Core Team Master. 

* You will create a Jenkins Pipeline job on your Team Master to automatically update the Core configuration bundle for your Team Master.
* You will add some new configuration to the `jenkins.yaml` JCasC configuration in your **core-config-bundle** repository and commit the changes to the **master** branch of your **core-config-bundle** repository that will then tigger the Jenkins Pipeline to update your Core configuration bundle.

1. If you are in the Blue Ocean UI then switch to the classic UI by clicking on the ***Go to classic*** button next to the ***Logout*** button in Blue Ocean navigation bar.<p><img src="images/go-to-classic.png" width=600/>
2. Once in the classic UI on your Team Master, ensure that you are in the folder with the same name as your Team Master - you should see the `workshop-setup` Pipeline job. This is important if you want to use Blue Ocean to visualize the Pipeline runs of Pipeline jobs you add to your Team Master, because only jobs under this folder will show up in Blue Ocean.<p><img src="images/blue-steel-folder.png" width=600/>
3. Click on the **New Item** link in the left navigation menu - again, make sure that you are in the folder with the same name as your Team Master, and not at the root of your Team Master.
4. Enter the name of the GitHub Organization you created for this workshop as the **Item Name**, select **GitHub Organization** as the item type and then click the **OK** button.<p><img src="images/github-organization-item.png" width=600/>
5. Select the **Credentials** with the ***GitHub PAT from JCasC - username/password*** description created for you with Core CasC, note the value of the **Owner** field is already filled in and matched the **Item Name** you entered above - ensure that it matches the name of the GitHub Organization you created for this workshop. Then click the **Build strategies** **Add** button and select ***Skip initial build on first branch indexing*** from the drop-down. Finally, click the **Save** button.<p><img src="images/organization-folder-save.png" width=800/>
6. After you click the **Save** button the Organization Folder Pipeline project will scan every branch of every repository of your GitHub Organization creating a Pipeline job for each branch where there is a `Jenkinsfile` and creating a [Pipeline Multibranch project](https://jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) for each repository where there is at least one branch containing a `Jenkinsfile`. Once the scan is complete, click on the breadcrumb link that matches your GitHub Organization name - just to the left of **Scan Organization**.<p><img src="images/click-org-folder-link.png" width=600/>
7. Click on the link of the Jenkins Multibranch Pipeline project for your fork of the **core-config-bundle** repository.<p><img src="images/core-config-bundle-multibranch.png" width=600/>
8. Next, in GitHub, navigate to your fork of the 
9. Now we will use the GitHub file editor to add some configuration to the `jenkins.yaml` file in your forked **core-config-bundle** repository. Navigate to the `jenkins.yaml` file of your forked repository and then click on the pencil icon in the upper right to edit that file. <p><img src="images/edit-jenkins-yaml.png" width=600/>
10. Next add the following hibernating master configuration just above the `kube` entry:
```yaml
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 240
kube:
...
```
10.  Next, update the `systemMessage` entry under the `jenkins` category so it starts with **v2** instead of **v1**.<p><img src="images/update-system-message.png" width=600/>
11.  Scroll to the bottom of the page, enter a commit message and click the **Commit changes** button to commit the configuration updates to a new branch of your fork of the **core-config-bundle** repository.<p><img src="images/commit-to-new-branch.png" width=600/>
12.  Open the `plugin-catalog.yaml` file with the GitHub file editor and add the following YAML snippet to the bottom of that configuration file:
```yaml
    cloudbees-pipeline-policies:
      version: "0.8"
    managed-master-hibernation:
      version: "0.3-alpha"
```
13.   Scroll to the bottom of the page, enter a commit message and click the **Commit changes** button to commit the configuration updates to the same branch you committed to above.
14.   Next, open the `plugin.yaml` with the GitHub file editor. We will be adding the CloudBees Pipeline Policy plugin and the CloudBees Managed Master Hibernation plugin by adding the following YAML snippet to the end of that file:
```yaml
- id: "cloudbees-pipeline-policies"
- id: "managed-master-hibernation"
```
15.   Scroll to the bottom of the page, enter a commit message and click the **Commit changes** button to commit the configuration updates to the same branch you committed to above.
16.   Next, open the `bundle.yaml` with the GitHub file editor and update the `version` entry to **2** and then commit the changes to the **master** branch of your fork of the **core-config-bundle** repository.
17.   Create a **Pull Request** between the new branch and the **master** branch of your fork of the **core-config-bundle** repository and then merge those changes to your **master** branch.
18.   Now navigate to the **master** branch Pipeline job of the **core-config-bundle** Multibranch Pipeline project on your Team Master.
19.   After a couple of minutes you will see an addition **monitors** warning. Click on the **monitor** link of your Team Master and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle.
20.   You will now see a link for **Pipeline Polices** and Core Master Hibernation has been configured for your Team Master.

>NOTE: The **Build strategies** configuration for Pipeline Organization Folder and Multibranch projects are provided by the [Basic Branch Build Strategies plugin](https://github.com/jenkinsci/basic-branch-build-strategies-plugin/blob/master/docs/user.adoc) and by selecting the *Skip initial build on first branch indexing* strategy we avoid an unnecessary build when we first create the Organization Folder project above.

You may proceed to the next lab: [*Hibernating Masters*](../hibernating-masters/hibernating-masters.md) or choose another lab on the [main page](../../README.md#workshop-labs).
