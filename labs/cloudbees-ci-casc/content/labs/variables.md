---
title: "Simplifying Controller Bundles with Variables"
chapter: false
weight: 7
--- 

The `variables.yaml` is one of the optional CasC bundle file types. It allows you to define variables to be replaced in the jcasc, items and rbac yaml files.

In addition to `variables` bundle files, variables may also be defined as controller system properties and as [JCasC secrets](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc).

In this lab we will use variables to templatize the `rbac.yaml` file and update the parent bundle of your `dev-controller` bundle to the `rbac-base` bundle that includes that templatized version. This allows you to centrally manage standard RBAC strategies across many controllers.

1. Navigate to your workshop GitHub Organization click on the link for your copy of the **dev-controller** repository, click on the **Pull requests** tab and then click on the link for the **Using Variables** pull request.
2. On the next screen, click on the **Files changed** tab to review the files being removed and updated in your `dev-controller` repository.
3. Note that we incremented the `bundle.yaml` `version` to 4, removed the `rbac` entry and added the `bundle/variables.yaml` file.  ![bundle.yaml changes](bundle-variables-changes.png?width=50pc)
4. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Using Variables** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
5. Navigate to the `main` branch job of the `dev-controller` Multibranch pipeline project on your Ops controller.
6. After the the `main` branch job has completes successfully, navigate to the top level of your **dev controller**, click on your username at the top left and then click **Log Out**. ![log out](log-out.png?width=50pc)
7. On the login screen, login as your admin user - which is your lowercased GitHub username with a **-admin** suffix and the password is the same as before. For example: `beedemo-dev-admin`.
8. Once you are logged in, navigate to the top level of your **dev-controller**, click on the **Manage Jenkins** link in the left menu and then click on the **CloudBees Configuration as Code export and update** *System Configuration* item.
9. On the **CloudBees Configuration as Code export and update** click on the **Original Bundle** tab. Notice that the `rbac` files is named `01-rbac-base.rbac.yaml` signifying that it is coming from the `rbac-base` parent bundle. ![rbac from parent](rbac-parent-file.png?width=50pc)
10. Note the `${admin-user}` and `${manager-user}` placeholders in the `rbac-base` `rbac.yaml` file below (available in GitHub [here](https://github.com/cloudbees-days/workshop-casc-bundles/blob/main/rbac-base/rbac.yaml)):

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
    - "${admin-user}"
  roles:
  - name: administrator
    grantedAt: current
- name: Managers
  members:
    users:
    - "${manager-user}"
  roles:
  - name: manager
    grantedAt: current
```

This allows us to use the same `rbac` configuration for everyone's controllers and it could actually be part of a parent bundle.

