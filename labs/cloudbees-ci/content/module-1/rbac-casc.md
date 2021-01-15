---
title: "Delegating Administration with CloudBees CI RBAC"
chapter: false
weight: 4
---

Role-Based Access Control (RBAC) for CloudBees CI provides the ability to restrict access and delegate administration. When combined with CloudBees CI CasC you have a complete audit history of any changes to access control (and other configuration changes) captured by your source control tool, such as Git.

In addition to using CloudBees CI CasC to configure RBAC for your managed controller, we will be using the new experimental *Overall/Manage* and *Overall/SystemRead* permissions to limit UI based configuration for your user but still allow you to reload updated CasC bundles.

>NOTE: Using CasC for RBAC requires that you allow managed controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the managed controller will not inherit roles or groups from Operations Center.

1. To opt out of the Operations Center authorization strategy click on the **Teams** breadcrumb link in the top navigation.
2. In the **Teams** folder, expand the contextual menu for your managed controller and click the **Configure** link. ![Configure controllers](configure-controller.png?width=50pc) 
3. On the **Configure** screen scroll down to the **Security Setting Enforcement**, select the ***Enforce Authentication only*** value from the **Opt-out** select list and then click the **Save** button. ![Auth Only](auth-only.png?width=50pc) 
4. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. 
5. Click on the **RBAC lab updates** pull request in GitHub and then click on the **Files changed** tab to review the requested configuration changes.
6. Note the new `rbac.yaml` file that we are adding. We are adding two roles and two groups using those roles. ![RBAC YAML](rbac-yaml.png?width=50pc) 
7. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
8. On the next screen click the **Delete branch** button.
5. Navigate to the **config-bundle-ops** job under the **template-jobs** folder on your CloudBees CI managed controller.
6. Shortly after the **master** branch job completes successfully, navigate to the top-level of your managed controller.
7. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code bundle** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
8. On the next screen, click on the **Bundle Update** link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. *Note: If you don't see the new version available then click the **Check for Updates** button.* ![Bundle Update](new-bundle-available.png?width=50pc)
9. Once the bundle has finished reloading you will see a *Manage Jenkins* page with fewer items and the left navigation will have fewer items. Also, many of the configuration items that are still available are view only. ![Before and After Delegating Admin](before-after-delegating-admin.png?width=75pc)
10. Click on **Manage Plugins**, click on the **Available** tab and search for *CloudBees*.  Note that you can see what plugins are available but you cannot install plugins. In order to install or update plugins (or other configuration) you will need to update and reload the CasC bundle for your managed controller. ![View Only Plugin Management](plugins-view-only.png?width=50pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#pipeline-policies-overview">return to the workshop slides</a>**