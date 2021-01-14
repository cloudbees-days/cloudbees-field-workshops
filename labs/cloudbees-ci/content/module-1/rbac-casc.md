---
title: "Delegating Administration with CloudBees CI RBAC"
chapter: false
weight: 4
---

Role-Based Access Control (RBAC) for CloudBees CI provides the ability to restrict access and delegate administration. And when combined with CloudBees CI CasC you have complete audit history of any changes to access control (and other configuration changes) captured by your source control tool, such as Git.

In addition to using CloudBees CI CasC to configure RBAC for your managed controller, we will also be setting up a custom RBAC role utilizing the *Overall/Manage* permission.

>NOTE: Using CasC for RBAC requires that you allow managed controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the managed controller will not inherit roles or groups from Operations Center.

1. To opt out of the Operations Center authorization strategy click on the **Teams** breadcrumb link in the top navigation.
2. In the **Teams** folder, expand the contextual menu for your managed controller and click the **Configure** link. ![Configure controllers](configure-controller.png?width=50pc) 
3. On the **Configure** screen scroll down to the **Security Setting Enforcement**, select the ***Enforce Authentication only*** value from the **Opt-out** select list and then click the **Save** button. ![Auth Only](auth-only.png?width=50pc) 
4. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. 
5. Click on the **RBAC CasC Lab** pull request in GitHub and then click on the **Files changed** tab to review the requested configuration changes.
6. Note the new `rbac.yaml` file that we are adding. We are adding two roles and two groups using those roles.
7. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
8. On the next screen click the **Delete branch** button.
5. Navigate to the **config-bundle-ops** job under the **template-jobs** folder on your CloudBees CI ***managed controller***.
6. Shortly after the **master** branch job completes successfully navigate to the top-level of your ***managed controller***
7. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code bundle** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)

