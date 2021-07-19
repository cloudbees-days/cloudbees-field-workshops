---
title: "Configuring RBAC and Folders with CloudBees CI CasC"
chapter: false
weight: 6
--- 

CloudBees CI CasC provides support for managing the configuration of CloudBees CI Role Based Access Control (RBAC) and folders.

In this lab we will explore updating configuration bundle of your dev controller to manage RBAC.

>NOTE: Using CasC for RBAC requires that you allow Managed Controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the Managed Controller will not inherit roles or groups from Operations Center but will still authenticate through Operations Center. As noted in the previous lab, your dev controller was provisioned with the setting already configured to opt out of inheriting the Operations Center authorization strategy.

In addition to using CasC to configure RBAC for your dev controller, we will also utilize the Jenkins **Overall/Manage** and **Overall/SystemRead** permissions to limit the amount of configuration that your CloudBees CI user is able to make via the UI. The **Overall/Manage** permission will still allow your user to reload updated configuration bundles but the actual configuration changes must be committed to your `dev-controller` repository.

## Configure controller RBAC with a Configuration Bundle

1. Navigate to your workshop GitHub Organization click on the link for your copy of the **dev-controller** repository. ![dev-controller repo link](github-dev-controller-repo-link.png?width=50pc)
2. At the top level of your `dev-controller` repository in your workshop GitHub Organization, click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
```yaml
removeStrategy:
  rbac: SYNC
roles:
- name: authenticated
  filterable: 'true'
  permissions:
  - hudson.model.Hudson.Read
  - hudson.model.Item.Read
  - hudson.model.View.Read
- name: administrator
  permissions:
  - hudson.model.Hudson.Administer
- name: manager
  filterable: 'true'
  permissions:
  - hudson.model.Hudson.SystemRead
  - hudson.model.Hudson.Manage
  - com.cloudbees.plugins.credentials.CredentialsProvider.View
  - com.cloudbees.pipeline.governance.templates.catalog.TemplateCatalogAction.ViewCatalogs
  - com.cloudbees.jenkins.plugin.metrics.views.Alerter.View
  - nectar.plugins.rbac.groups.Group.View
  - nectar.plugins.rbac.roles.Role.View
groups:
- name: Administrators
  members:
    users:
    - admin
    - team-admin
    - "REPLACE_GITHUB_USERNAME-admin"
  roles:
  - name: administrator
    grantedAt: current
- name: Managers
  members:
    users:
    - "REPLACE_GITHUB_USERNAME"
  roles:
  - name: manager
    grantedAt: current
```
3. Name the new file `rbac.yaml`, copy the `rbac` configuration from above and paste it into the GitHub file editor. **Important**: replace the two `REPLACE_GITHUB_USERNAME` placeholders with your GitHub username. Then select the option to **"Create a new branch for this commit and start a pull request"**, name the branch `add-rbac` and then click the **Propose changes** button. ![Create rbac.yaml](github-commit-rbac-yaml.png?width=50pc)
4. On the next screen click the **Create pull request** button to create a pull request to merge to the `main` branch when you are done updating your `ops-controller` configuration bundle. ![Create RBAC pull request](github-create-rbac-pr.png?width=50pc)
5. Navigating back to the top level of your `dev-controller` repository and ensuring that you are on the ` add-rbac` branch, click on the `bundle.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. 
11. Update the bundle `version` to **2** and add the following `rbac` section:
```yaml
apiVersion: "1"
version: "2"
id: "cbci-casc-workshop-dev-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop dev-controller Controller"
parent: "base"
rbac:
  - "rbac.yaml"
```
12. After you have made the changes, ensure that you are committing to the `add-rbac` branch and then click the **Commit changes** button. ![Commit bundle.yaml with rbac](github-commit-rbac-bundle-yaml.png?width=50pc)
13. Now that we have added the `rbac.yaml` and updated the `bundle.yaml`,  we can now merge the pull request to the `main` branch. In GitHub, click on the **Pull requests** tab and then click on the link for the **Create rbac.yaml** pull request. ![rbac pull request link](github-rbac-pr-link.png?width=50pc)
14. On the **Create rbac.yaml #1** pull request page, click the **Merge pull request** button, then click the **Confirm merge** button and then click the **Delete branch** button.
15. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project on your Ops controller. ![dev-controller Mulitbranch](dev-controller-multibranch-jcasc.png?width=50pc)
16. After the the `main` branch job has completed successfully, navigate to the top level of your dev controller, click on the **Manage Jenkins** link in the left menu, and then click on the **CloudBees Configuration as Code bundle** **System Configuration** item. ![CasC Configuration link](dev-casc-config-link.png?width=50pc) 
17. On the **CloudBees Configuration as Code bundle** click on the **Bundle update** tab and you should see that there is a bundle update available. ![CasC bundle update](casc-bundle-update.png?width=50pc)
18. Click on the **Reload Configuration** button and then on the next screen click the **Yes** button to apply the bundle update. ![CasC bundle apply](casc-bundle-apply.png?width=50pc)
19. Once the bundle has finished reloading you will see a *Manage Jenkins* page with fewer items and the left navigation will have fewer items. Also, many of the configuration items that are still available are view only. ![After Delegating Admin](after-delegating-admin.png?width=85pc)
20. Click on **Manage Plugins**, click on the **Available** tab and search for *CloudBees*.  Note that you can see what plugins are available but you cannot install plugins. In order to install or update plugins (or other configuration) you will need to update and reload the CasC bundle for your Managed Controller. ![View Only Plugin Management](plugins-view-only.png?width=60pc)

## Adding a Folder with RBAC to a Configuration Bundle




