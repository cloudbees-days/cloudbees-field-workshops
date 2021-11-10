---
title: "Configuring RBAC and Folders with CloudBees CI CasC"
chapter: false
weight: 6
--- 

CloudBees CI CasC provides support for managing the configuration of CloudBees CI Role Based Access Control (RBAC) and folders.

In this lab we will explore updating configuration bundle of your dev controller to manage RBAC.

{{% notice note %}}
Using CasC for RBAC requires that you allow Managed Controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the Managed Controller will not inherit roles or groups from Operations Center but will still authenticate through Operations Center. As noted in the previous lab, your dev controller was provisioned with the setting already configured to opt out of inheriting the Operations Center authorization strategy.
{{% /notice %}}

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
4. On the next screen click the **Create pull request** button to create a pull request to merge to the `main` branch when you are done updating your `dev-controller` configuration bundle. ![Create RBAC pull request](github-create-rbac-pr.png?width=50pc)
5. Navigating back to the top level of your `dev-controller` repository and ensuring that you are on the ` add-rbac` branch, click on the `bundle.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. 
6. Update the bundle `version` to **2** and add the following `rbac` section:
```yaml
rbac:
  - "rbac.yaml"
```

{{%expand "expand for complete bundle.yaml file" %}}
```yaml
apiVersion: "1"
version: "2"
id: "cbci-casc-workshop-dev-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop dev-controller Controller"
parent: "base"
rbac:
  - "rbac.yaml"
  ```
{{% /expand%}}

7. After you have made the changes, ensure that you are committing to the `add-rbac` branch and then click the **Commit changes** button. ![Commit bundle.yaml with rbac](github-commit-rbac-bundle-yaml.png?width=50pc)
8. Now that we have added the `rbac.yaml` and updated the `bundle.yaml`,  we can now merge the pull request to the `main` branch. In GitHub, click on the **Pull requests** tab and then click on the link for the **Create rbac.yaml** pull request. ![rbac pull request link](github-rbac-pr-link.png?width=50pc)
9. On the **Create rbac.yaml #1** pull request page, click the **Merge pull request** button, then click the **Confirm merge** button and then click the **Delete branch** button.
10. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project on your Ops controller. ![dev-controller Mulitbranch](dev-controller-multibranch-jcasc.png?width=50pc)
11. After the the `main` branch job has completed successfully, navigate to the top level of your **dev controller**, click on the **Manage Jenkins** link in the left menu.
14. You will see a *Manage Jenkins* page with fewer items and the left navigation will have fewer items. Also, many of the configuration items that are still available are view only. ![After Delegating Admin](after-delegating-admin.png?width=85pc)
15. Click on **Manage Plugins**, click on the **Available** tab and search for *CloudBees*.  Note that you can see what plugins are available but you cannot install plugins. In order to install or update plugins (or other configuration) you will need to update and reload the CasC bundle for your Managed Controller. ![View Only Plugin Management](plugins-view-only.png?width=60pc)
16. Finally, navigate to the top level of your dev controller and you will see that you cannot create any items (or jobs). We will fix that in the next section by creating a folder with RBAC that allows you to create jobs in that folder.

## Adding a Folder with RBAC to a Configuration Bundle

1. Navigate to the top level of your `dev-controller` repository in your workshop GitHub Organization and click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
```yaml
removeStrategy:
 items: "none"
 rbac: "sync"

items:
 - kind: "folder"
   name: "controller-jobs"
   description: "Base controller folder for all jobs."
   groups:
     - name: "Job Managers"
       members:
         users:
           - "Managers"
       roles:
         - name: "job-manager"
           grantedAt: "current"
           propagates: "true"
```
2. Name the new file `folders.yaml`, copy the `items` configuration from above and paste it into the GitHub file editor. Then select the option to **"Create a new branch for this commit and start a pull request"**, name the branch `add-folder` and then click the **Propose changes** button. ![Create folders.yaml](github-commit-folders-yaml.png?width=50pc)
3. On the next screen click the **Create pull request** button to create a pull request to merge to the `main` branch when you are done updating your `dev-controller` configuration bundle. ![Create folder pull request](github-create-folder-pr.png?width=50pc)
4. Now we must add the new `job-manager` role to your `rbac.yaml`. Navigate back to the top level of your `dev-controller` repository and ensuring that you are on the ` add-folder` branch, click on the `rbac.yaml` file and then click on the ***Edit this file*** pencil button to edit the file.
5. Add the following `job-manager` section after the current `manager` role:
```yaml
- name: job-manager
  filterable: 'true'
  permissions:
  - hudson.model.Item.Read
  - hudson.model.Item.Create
  - hudson.model.Item.Configure
  - hudson.model.Item.Build
```

{{%expand "expand for complete rbac.yaml file - IMPORTANT: REPLACE_GITHUB_USERNAME must be replaced with your GitHub username" %}}
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
- name: job-manager
  filterable: 'true'
  permissions:
  - hudson.model.Item.Read
  - hudson.model.Item.Create
  - hudson.model.Item.Configure
  - hudson.model.Item.Build
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
{{% /expand%}}

6. After you have made the changes, ensure that you are committing to the `add-folder` branch and then click the **Commit changes** button. ![Commit rbac.yaml with job-manager role](github-commit-rbac-yaml-job-manager.png?width=50pc)
7. Navigating back to the top level of your `dev-controller` repository and ensuring that you are on the ` add-folder` branch, click on the `bundle.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. 
8. Update the bundle `version` to **3** and add the following `items` section after the `rbac` section:
```yaml
items:
  - "folders.yaml"
```

{{%expand "expand for complete bundle.yaml file" %}}
```yaml
apiVersion: "1"
version: "3"
id: "cbci-casc-workshop-dev-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop dev-controller Controller"
parent: "base"
rbac:
  - "rbac.yaml"
items:
  - "folders.yaml"
  ```
{{% /expand%}}

9. After you have made the changes, ensure that you are committing to the `add-folder` branch and then click the **Commit changes** button. ![Commit bundle.yaml with items](github-commit-items-bundle-yaml.png?width=50pc)
8. Now that we have added the `folders.yaml`, and updated the `rbac.yaml` and `bundle.yaml` files,  we can now merge the pull request to the `main` branch. In GitHub, click on the **Pull requests** tab and then click on the link for the **Create folders.yaml** pull request. ![folders pull request link](github-folders-pr-link.png?width=50pc)
9. On the **Create folders.yaml #2** pull request page, click the **Merge pull request** button, then click the **Confirm merge** button and then click the **Delete branch** button.
10. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project **on your Ops controller**. ![dev-controller Mulitbranch](dev-controller-multibranch-jcasc.png?width=50pc)
11. After the the `main` branch job has completed successfully, navigate to the top level of your **dev controller** and there will be a new **controller-jobs** folder. ![New folder](new-jobs-folder.png?width=50pc)
15. Click on the **controller-jobs** folder and you will see that you are able to create new jobs in that folder. ![Create jobs](create-job.png?width=50pc)
