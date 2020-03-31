# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Configuration as Code

In this lab we are going to explore [Configuration as Code (CasC) for CloudBees Core](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) and then we will setup GitOps for Core CasC so that any configuration changes you make in source control will automatically be updated in your Team Master. 

CasC for CloudBees Core consists of a collection of YAML files referred to as a configuration bundle (or CasC bundle) that includes four files:

1. bundle.yaml - This file is an index file that describes the bundle, and references the other files in the bundle.
2. jenkins.yaml - This file contains the Jenkins configuration as defined by the [Jenkins CasC plugin](https://github.com/jenkinsci/configuration-as-code-plugin).
3. plugin-catalog.yaml - This file provides a list of plugins that are not already part of the Core plugin envelope and makes those plugins available to be installed on a Managed Master.
4. plugins.yaml - This file contains a list of all plugin to be installed on a Managed Master by the Core CasC capability.

## Enabling CasC for a Core Managed/Team Master
The `workshop-setup` job copied the YAML configuration files from your forked **core-config-bundle** repository to a sub-directory with the same name as your Team Master inside a special directory in the Jenkins home of the Core Operations Center from which you created your Team Master. When the Core Operations Center is provisioning a Team/Managed Master it will check to see if there is a matching configuration for the name of the Team/Managed Master being provisioned.

## Configuration Components

### jenkins.yaml
The `jenkins.yaml` is 
#### Credentials
Secrets for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system.
  2. As Jenkins encrypted values used directly in the JCasC yaml configuration.

The `workshop-setup` job encrypted the GitHub Personal Access Token that you provided so it can only be decrypted by your Team Master and then replaced placeholders in your copy of the `jenkins.yaml` file. Other placeholders that were replaced were: `REPLACE_GITHUB_ORG` and `REPLACE_WITH_YOUR_GITHUB_USERNAME`. 

#### Pipeline Shared Library
CasC allows auto-configuring Pipeline Shared Libraries so it is very easy to provide shared libraries across many teams.

#### Master Level Kubernetes Agent Templates
The CloudBees Kube Management plugin provides...

## GitOps for Core CasC
One of the main reasons to manage configurations as code is to allow it to be managed in source control. In this exercise we will setup a Jenkins Pipeline job - a [Pipeline Organization Folder](https://jenkins.io/doc/book/pipeline/multibranch/#organization-folders) - on your Team Master that will be triggered whenever you commit any changes to the **master** branch of that repository.

* Create a Jenkins Pipeline job on your Team Master to automatically update the Core configuration bundle for your Team Master.
* Add some configuration to the `jenkins.yaml` JCasC configuration in your **core-config-bundle** repository and commit the changes to tigger an update.

1. If you are in the Blue Ocean UI then switch to the classic UI by clicking on the ***Go to classic*** button next to the ***Logout*** button in Blue Ocean navigation bar.<p><img src="images/go-to-classic.png" width=600/>
2. Once in the classic UI on your Team Master, ensure that you are in the folder with the same name as your Team Master - you should see the `workshop-setup` Pipeline job. This is important if you want to use Blue Ocean to visualize the Pipeline runs, because only jobs under this folder will show up in Blue Ocean.<p><img src="images/blue-steel-folder.png" width=600/>
3. Click on **New Item** link in the left navigation menu - make sure that you are in the folder with the same name as your team, and not at the root of your Team Master.
4. Enter the name of the GitHub Organization you created for this workshop as the **Item Name**, select **GitHub Organization** as the item type and then click the **OK** button.<p><img src="images/github-organization-item.png" width=600/>
5. Select the **Credentials** with the ***GitHub PAT from JCasC - username/password*** description created for you with Core CasC, note the value of the **Owner** field is already filled in and matched the **Item Name** you entered above - ensure that it matches the name of the GitHub Organization you created for this workshop. Then click the **Build strategies** **Add** button and select ***Skip initial build on first branch indexing*** from the drop-down. Finally, click the **Save** button.<p><img src="images/organization-folder-save.png" width=600/>
6. After you click the **Save** button the Organization Folder Pipeline project will scan every branch of every repository of your GitHub Organization creating a Pipeline job for each branch where there is a `Jenkinsfile` and creating a [Pipeline Multibranch project](https://jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline) for each repository where there is at least one branch containing a `Jenkinsfile`. Once the scan is complete, click on the breadcrumb link that matches your GitHub Organization name - just to the left of **Scan Organization**.
7. Click on the link of the Jenkins Multibranch Pipeline project for your fork of the **core-config-bundle** repository.<p><img src="images/core-config-bundle-multibranch.png" width=600/>
8. Now we will use the GitHub file editor to add some configuration to the `jenkins.yaml` file in your forked **core-config-bundle** repository. Navigate to the `jenkins.yaml` file of your forked repository and then click on the pencil icon in the upper right to edit that file. <p><img src="images/edit-jenkins-yaml.png" width=600/>
9. Add the following notification configuration - that enables Cross Team Collaboration - above the `jenkins` entry - **NOTE** that indentation is very important for YAML:
```yaml
notificationConfiguration:
  enabled: true
  router: "operationsCenter"
jenkins:
...
```
10. Next add the following hibernating master configuration just above the `kube` entry:
```yaml
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 600
kube:
...
```
11.  Next, update the `systemMessage` entry under the `jenkins` category so it starts with **v2** instead of **v1**.<p><img src="images/update-system-message.png" width=600/>
12.  Scroll to the bottom of the page, enter a commit message and click the **Commit changes** button to commit the configuration updates to the **master** branch of your fork of the **core-config-bundle** repository.
13.  Next, open the `bundle.yaml` with the GitHub file editor and update the `version` entry to **2** and then commit the changes to the **master** branch of your fork of the **core-config-bundle** repository.
14.  Now navigate to the **master** branch Pipeline job on your Team Master.
15.  After a couple of minutes you will see an addition **monitors** warning. Click on the **monitors** link and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle.

>NOTE: The **Build strategies** configuration for Pipeline Organization Folder and Multibranch projects is provided by the [Basic Branch Build Strategies plugin](https://github.com/jenkinsci/basic-branch-build-strategies-plugin/blob/master/docs/user.adoc) and by selecting the *Skip initial build on first branch indexing* strategy we avoid an unnecessary build when we first create the Organization Folder project above.

You may proceed to the next lab: [*Pipeline Template Catalogs*](../pipeline-template-catalog/pipeline-template-catalog.md) or choose another lab on the [main page](../../README.md#workshop-labs).




