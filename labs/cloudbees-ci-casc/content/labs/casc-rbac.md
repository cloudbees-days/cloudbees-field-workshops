---
title: "Configuring RBAC and Folders with CloudBees CI CasC"
chapter: false
weight: 6
--- 

CloudBees CI CasC provides support for managing the configuration of CloudBees CI Role Based Access Control (RBAC) for controllers and folders on controllers.

In this lab we will explore updating the configuration bundle of your dev controller to manage RBAC with its CasC bundle.

{{% notice note %}}
Using CasC for RBAC requires that you allow Managed Controllers to opt-out of inheriting the Operations Center authorization strategy, meaning that the managed controller will not inherit roles or groups from Operations Center but will still authenticate through Operations Center. As noted in the previous lab, your dev controller was provisioned with the setting already configured to opt out of inheriting the Operations Center authorization strategy.
{{% /notice %}}

The configuration from the `dev-controller` `controller.yaml` that allows configuring RBAC with CasC for controllers:

```yaml
    - optOutProperty:
        securityEnforcerOptOutMode:
          authorizationOptOutMode: {
            }
```


In addition to using CasC to configure RBAC for your dev controller, we will also utilize the Jenkins **Overall/Manage** and **Overall/SystemRead** permissions to limit the amount of configuration that your CloudBees CI user is able to make via the UI. The **Overall/Manage** permission will still allow your user to reload updated configuration bundles but the actual configuration changes must be committed to your `dev-controller` repository.

## Configure controller RBAC with a Configuration Bundle

1. Navigate to your workshop GitHub Organization click on the link for your copy of the **dev-controller** repository, click on the **Pull requests** tab and then click on the link for the **Controller RBAC** pull request.
2. On the next screen, click on the **Files changed** tab to review the files being updated and added to your `dev-controller` repository.
3. Note that we incremented the `bundle.yaml` `version` to 2, added an `rbac` entry and added the `bundle/rbac.yaml` file.  ![bundle.yaml changes](bundel-yaml-changes.png?width=50pc)
4. Click on the `rbac.yaml` file. Note that we are adding two roles, `administrator` and `manager`; and creating two groups using those roles with your regular user being added as a member of the `Managers` group and your admin user being added to the `Administrators` group.  ![rbac.yaml changes](rbac-yaml-changes.png?width=50pc)
5. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Controller RBAC** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
6. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project on your Ops controller. ![dev-controller Mulitbranch](dev-controller-multibranch-jcasc.png?width=50pc)
7. After the the `main` branch job has completed successfully, navigate to the top level of your **dev controller**, click on the **Manage Jenkins** link in the left menu.
8. You will see a *Manage Jenkins* page with fewer items and the left navigation will have fewer items. Also, many of the configuration items that are still available are view only. ![After Delegating Admin](after-delegating-admin.png?width=85pc)
9. Click on **Manage Plugins**, click on the **Available** tab and search for *CloudBees*.  Note that you can see what plugins are available but you cannot install plugins. In order to install or update plugins (or other configuration) you will need to update and reload the CasC bundle for your Managed Controller. ![View Only Plugin Management](plugins-view-only.png?width=60pc)
10. Finally, navigate to the top level of your dev controller and you will see that you cannot create any items (jobs). In the next section we will create a folder with RBAC that allows you to create jobs in that folder.

## Adding a Folder with RBAC to a Configuration Bundle

1. Navigate to your workshop GitHub Organization click on the link for your copy of the **dev-controller** repository, click on the **Pull requests** tab and then click on the link for the **Folder RBAC** pull request. 
2. On the next screen, click on the **Files changed** tab to review the files being updated and added to your `dev-controller` repository.
3. Note that we incremented the `bundle.yaml` `version` to 3, added an `items` entry and added the `bundle/folder.yaml` file. ![folder bundle.yaml changes](folder-bundle-yaml-changes.png?width=50pc)
4. Next, click on the `folder.yaml` file and notice that we are creating a `controller-jobs` folder with a `Job Managers` group. ![folder.yaml](folder-yaml.png?width=50pc)
5. Finally, click on the `rbac.yaml` file. Note that we are adding the `job-manager` role being used in the `folder.yaml` file above.  ![folder rbac.yaml changes](folder rbac-yaml-changes.png?width=50pc)
6. Now that we have reviewed the new `folders.yaml`, and the changes to the `rbac.yaml` and `bundle.yaml` files,  click on the **Conversation** tab of the **Folder RBAC** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
7. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project **on your Ops controller**. ![dev-controller Mulitbranch](dev-controller-multibranch-jcasc.png?width=50pc)
8. After the the `main` branch job has completed successfully, navigate to the top level of your **dev controller** and there will be a new **controller-jobs** folder. ![New folder](new-jobs-folder.png?width=50pc)
9. Click on the **controller-jobs** folder and you will see that you are able to create new jobs in that folder. ![Create jobs](create-job.png?width=50pc)
