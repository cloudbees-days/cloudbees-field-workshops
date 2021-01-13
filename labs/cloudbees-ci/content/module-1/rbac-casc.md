---
title: "Delegating Administration with CloudBees CI RBAC"
chapter: false
weight: 3
---

Role-Based Access Control (RBAC) for CloudBees CI provides the ability to restrict access and delegate administration. And when combined with CloudBees CI CasC you have complete audit history of any changes to access control (and other configuration changes) captured by your source control tool, such as Git.

In addition to using CloudBees CI CasC to configure RBAC for your managed controller, we will also be setting up a custom RBAC role utilizing the *Overall/Manage* permission.

>NOTE: Using CasC for RBAC requires that you allow managed controllers to opt-out of inheriting the Operations Center authorization strategy meaning that the managed controller will not inherit roles or groups from Operations Center.

1. To opt out of the Operations Center authorization strategy click on the **Teams** breadcrumb link in the top navigation.
2. In the **Teams** folder, expand the contextual menu for your managed controller and click the **Configure** link.
3. On the **Configure** screen scroll down to the **Security Setting Enforcement**, select the ***Enforce Authentication only*** value from the **Opt-out** select list and then click the **Save** button.
4. Review `rbac-casc` pull request in GitHub.
   1. 
5. Merge the pull request.
6. After the config bundle job completes, reload the updated configuration bundle.
7. 