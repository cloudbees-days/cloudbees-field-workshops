---
title: "Simplifying Controller Bundles with Variables"
chapter: false
weight: 7
--- 

The `variables.yaml` is one of the optional CasC bundle file types. It allows you to define variables to be replaced in the jcasc, items and rbac yaml files.

In addition to `variables` bundle files, variables may also be defined as controller system properties and as [JCasC secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc).

In this lab we will use variables to templatize the `rbac.yaml` file.

1. Navigate to your workshop GitHub Organization click on the link for your copy of the **dev-controller** repository, click on the **Pull requests** tab and then click on the link for the **Using Variables** pull request.
2. On the next screen, click on the **Files changed** tab to review the files being removed and updated in your `dev-controller` repository.
3. Note that we incremented the `bundle.yaml` `version` to 4, removed the `rbac` entry and added the `bundle/variables.yaml` file.  ![bundle.yaml changes](bundle-variables-changes.png?width=50pc)
4. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Using Variables** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
5. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project on your Ops controller.
6. After the the `main` branch job has completed successfully, navigate to the top level of your **dev controller**, click on your username at the top left and then click **Log Out**. ![log out](log-out.png?width=50pc)
7. On the login screen, login as your admin user - which is your lowercased GitHub username with a **-admin** suffix and the password is the same. For example `beedemo-dev-admin`.
8. Once you are logged in, navigate to the top level of your **dev-controller**, click on the **Manage Jenkins** link in the left menu and then click on the **CloudBees Configuration as Code export and update** *System Configuration* item.
9. On the **CloudBees Configuration as Code export and update** click on the **Original Bundle** tab. Notice that the `rbac` files is named `01-rbac-base.rbac.yaml` signifying that it is coming from the `rbac-base` parent bundle. ![rbac from parent](rbac-parent-file.png?width=50pc)


