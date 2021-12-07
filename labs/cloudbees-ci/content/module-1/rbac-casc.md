---
title: "Delegating Administration with CloudBees CI RBAC"
chapter: false
weight: 4
---

Role-Based Access Control (RBAC) for CloudBees CI provides the ability to restrict access and delegate administration. When combined with CloudBees CI CasC, you have a complete audit history of any changes to access control (and other configuration changes) captured by your source control tool, such as Git.

In addition to using CloudBees CI CasC to configure RBAC for your managed controller, we will be using the *Overall/Manage* and *Overall/SystemRead* permissions (as described [here](https://www.jenkins.io/doc/book/security/access-control/permissions/#optional-permissions)) to limit UI based configuration for your user, but still allow you to reload updated CasC bundles.

{{% notice note %}}
Using CasC for RBAC requires that you allow Managed Controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the Managed Controller will not inherit roles or groups from Operations Center.
{{% /notice %}}

1. To opt out of the Operations Center authorization strategy navigate to the folder with the same name as your workshop GitHub Organization, expand the contextual menu for your managed controller and click the **Configure** link. ![Configure controllers](configure-controller.png?width=50pc) 
2. On the **Configure** screen scroll down to the **Security Setting Enforcement**, select the ***Enforce Authentication only*** value from the **Opt-out** select list and then click the **Save** button. ![Auth Only](auth-only.png?width=50pc) 
3. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. 
4. Click on the **RBAC lab updates** pull request in GitHub and then click on the **Files changed** tab to review the requested configuration changes.
5. Note the new `rbac.yaml` file that we are adding. We are adding two roles and two groups using those roles. ![RBAC YAML](rbac-yaml.png?width=50pc) 
6. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
7. On the next screen click the **Delete branch** button.
8. Navigate to the **config-bundle-ops** job under the **template-jobs** folder on your CloudBees CI managed controller.
9. Shortly after the **main** branch job completes successfully, navigate to the top-level of your managed controller.
10. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code export and update** link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
11. On the next screen, click on the Bundle Update link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. 

{{% notice note %}}
If you don't see the new version available then click the **Check for Updates** button.
{{% /notice %}}
![Bundle Update](new-bundle-available.png?width=50pc)

12. Once the bundle has finished reloading you will see a *Manage Jenkins* page with fewer items and the left navigation will have fewer items - including no longer having the ability to create a **New Item** at the root of your controller. Also, many of the configuration items that are still available are view only. ![Before and After Delegating Admin](before-after-delegating-admin.png?width=85pc)
13. Click on **Manage Plugins**, click on the **Available** tab and search for *CloudBees*.  Note that you can see what plugins are available but you cannot install plugins. In order to install or update plugins (or other configuration) you will need to update and reload the CasC bundle for your managed controller. ![View Only Plugin Management](plugins-view-only.png?width=60pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#prbac-casc-overview">return to the workshop slides</a>**