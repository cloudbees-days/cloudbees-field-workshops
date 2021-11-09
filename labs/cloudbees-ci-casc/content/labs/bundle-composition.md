---
title: "CloudBees CI Configuration Bundle Composition"
chapter: false
weight: 2
--- 

The YAML based configuration of a controller is described in a collection of files referred to as a Configuration as Code (CasC) for Controllers bundle that we will refer to as just ***configuration bundle*** for most of this workshop. The CloudBees CI Operations Center can store as many different configuration bundles as needed to represent any unique requirements between different controllers.

This lab will explore the composition of a CloudBees CI configuration bundle, to include the manual updating of a configuration bundle and creating a configuration bundle from the bundle export of an existing controller.

## Configuration Bundle Composition Overview

A configuration bundle may consist of the following YAML file types:

- **bundle** (required) - This file is an index file that describes the bundle, references the other files in the bundle and must be named `bundle.yaml`. Any files not listed in this file will not be included in the controller bundle. It also (optionally) allows you to specify an `availabilityPattern` which is the full path to the controllers that can use the bundle defined as a regular expression.
- **jcasc** (optional) - This file contains the Jenkins configuration (global configuration, credentials), as defined by the Jenkins [Configuration as Code plugin](https://github.com/jenkinsci/configuration-as-code-plugin).
- **plugins** (optional) - This file contains a list of all the plugins to be installed on the controller. Plugins that are not in the [CloudBees Assurance Program (CAP)](https://docs.cloudbees.com/docs/admin-resources/latest/assurance-program/) have to be added with a Plugin Catalog and to this file.
- **catalog** (optional) - This file defines the catalog of versioned plugins outside of the CloudBees Assurance Program (CAP) that are available for installation on the controller. An optional location can also be specified for plugins that are not available in the standard update centers. Adding plugins to a catalog only makes them available to install and they still must be added to the plugins file above.
- **rbac** (optional) - This file defines the RBAC groups and roles at the root level of a controller. 
- **items** (optional) - This file defines items to be created on the controller. Currently, only folders and a subset of fields are fully supported. 

{{% notice note %}}
You may have noticed that all the file types except for the **bundle** file are optional and wonder if it would make sense to have a configuration bundle that only had a **bundle** file. We will see in a later lab that it is useful with bundle inheritance.
{{% /notice %}}

In this lab we will explore the configuration bundle assigned to your Ops controller when it was dynamically provisioned.

1. Navigate to the `ops-controller` repository in your workshop GitHub Organization. ![ops-controller repository](ops-controller-repo.png?width=50pc) 
2. Click on the `bundle.yaml` file. Its contents will mostly match the following (the `id`, `description` and `availabilityPattern` will be unique to each attendee):
```yaml
apiVersion: "1"
version: "1"
id: "cbci-casc-workshop-ops-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop ops-controller Controller"
availabilityPattern: "{GitHub Org}/{controller name}"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
items:
  - "items.yaml"
``` 

{{% notice note %}}
It is important that the bundle file is named exactly `bundle.yaml` otherwise the bundle will not be useable.
{{% /notice %}}

3. Return to the top level of your `ops-controller` repository and click on the `jenkins.yaml` file. The name of this file must match the file name listed under `jcasc` in the `bundle.yaml` file. Its contents will  match the following:
```yaml
jenkins:
  globalNodeProperties:
  - envVars:
      env:
      - key: GITHUB_ORGANIZATION
        value: "${GITHUB_ORGANIZATION}"
      - key: GITHUB_REPOSITORY
        value: ops-controller
  quietPeriod: 0
  systemMessage: 'Jenkins configured using CloudBees CI CasC'
unclassified:
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 1500
  gitHubConfiguration:
    apiRateLimitChecker: ThrottleForNormalize
  gitHubPluginConfig:
    hookSecretConfigs:
    - credentialsId: "cloudbees-ci-workshop-github-webhook-secret"
  globalDefaultFlowDurabilityLevel:
    durabilityHint: PERFORMANCE_OPTIMIZED
  globallibraries:
    libraries:
    - defaultVersion: "main"
      name: "pipeline-library"
      retriever:
        modernSCM:
          scm:
            github:
              credentialsId: "cloudbees-ci-workshop-github-app"
              repoOwner: "${GITHUB_ORGANIZATION}"
              repository: "pipeline-library"
credentials:
  system:
    domainCredentials:
    - credentials:
      - string:
          description: "Webhook secret for CloudBees CI Workshop GitHub App"
          id: "cloudbees-ci-workshop-github-webhook-secret"
          scope: SYSTEM
          secret: "${gitHubWebhookSecret}"
      - gitHubApp:
          apiUri: "https://api.github.com"
          appID: "${cbciCascWorkshopGitHubAppId}"
          description: "CloudBees CI CasC Workshop GitHub App credential"
          id: "cloudbees-ci-casc-workshop-github-app"
          owner: "${GITHUB_ORGANIZATION}"
          privateKey: "${cbciCascWorkshopGitHubAppPrivateKey}"
```

{{% notice note %}}
Setting up an initial Ops controller is a bit like the chicken and the egg conundrum. There will typically be some required manual steps to bootstrap the initial automation. In the case of this workshop, we have our own Ops controller that is used to dynamically provision each attendees Ops controller with a dynamically generated configuration bundle when you installed the CloudBees CI CasC Workshop GitHub App into your workshop GitHub Organization. Another alternative is to use CloudBees CI CasC for Operations Center that allows you to define managed controllers as `items` in the Operations Center CasC bundle (but it does not support automatically provisioning those controllers at this time, so there is still am manual step to actually start the managed controller).
{{% /notice %}}

4. As mentioned above, the `gitHubApp` credential is unique to your workshop GitHub Organization. But also notice the variable substitution for the `privateKey` field of that credential - the value in the `jenkins.yaml` file is the `${gitHubAppPrivateKey}` variable. Of course you wouldn't want to store a secure secret directly in a JCasC yaml file, especially if it is to be store in source control. However, JCasC supports several ways to [pass secrets more securely](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc). For this workshop we are passing secrets through variables using the [Kubernetes Secrets Store CSI driver](https://secrets-store-csi-driver.sigs.k8s.io/introduction.html) with the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). This allows us to manage secrets with the Google Secret Manager in GCP and to mount those secrets as files in the directory on your controller configured for JCasC to read secret variables with the file name being the variable name and the file contents being the secret value.
5. Return to the top level of your `ops-controller` repository and click on the `plugins.yaml` file. The name of this file must match the file name listed under `plugins` in the `bundle.yaml` file. Its contents will match the following:

```yaml
plugins:
- id: antisamy-markup-formatter
- id: cloudbees-casc-api
- id: cloudbees-github-reporting
- id: cloudbees-groovy-view
- id: cloudbees-monitoring
- id: cloudbees-pipeline-policies
- id: cloudbees-slack
- id: cloudbees-template
- id: cloudbees-view-creation-filter
- id: cloudbees-workflow-template
- id: cloudbees-workflow-ui
- id: configuration-as-code
- id: git
- id: github-branch-source
- id: managed-master-hibernation
- id: notification-api
- id: operations-center-cloud
- id: operations-center-notification
- id: pipeline-event-step
- id: pipeline-model-extensions
- id: pipeline-stage-view
- id: warnings-ng
- id: workflow-aggregator
- id: workflow-cps-checkpoint
# non-cap plugins
```
6. Finally, return to the top level of your `ops-controller` repository and click on the `items.yaml` file. The name of this file must match the file name listed under `items` in the `bundle.yaml` file. Its contents will match the following (except for the `REPLACE_GITHUB_ORG` placeholders):

```yml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  displayName: controller-jobs
  name: controller-jobs
  items:
  - kind: organizationFolder
    displayName: cbci-casc-automation
    name: cbci-casc-automation
    orphanedItemStrategy:
      defaultOrphanedItemStrategy:
        pruneDeadBranches: true
        daysToKeep: -1
        numToKeep: -1
    SCMSources:
    - github:
        apiUri: https://api.github.com
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - headWildcardFilter:
            includes: main
        repoOwner: REPLACE_GITHUB_ORG
        credentialsId: cloudbees-ci-casc-workshop-github-app
        id: org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator::https://api.github.com::REPLACE_GITHUB_ORG::ops-controller
        repository: ops-controller
        configuredByUrl: false
        repositoryUrl: https://github.com/REPLACE_GITHUB_ORG/ops-controller
    navigators:
    - github:
        apiUri: https://api.github.com
        repoOwner: REPLACE_GITHUB_ORG
        credentialsId: cloudbees-ci-casc-workshop-github-app
    projectFactories:
    - customMultiBranchProjectFactory:
        factory:
          customBranchProjectFactory:
            marker: Jenkinsfile
            definition:
              cpsScmFlowDefinition:
                scriptPath: controller-casc-automation
                scm:
                  gitSCM:
                    userRemoteConfigs:
                    - userRemoteConfig:
                        credentialsId: cloudbees-ci-casc-workshop-github-app
                        url: https://github.com/REPLACE_GITHUB_ORG/ops-controller.git
                    branches:
                    - branchSpec:
                        name: '*/main'
                lightweight: true
```

## Creating/Updating a Configuration Bundle from a Bundle Export
As you can see from the composition overview above, the YAML in the different configuration files can be somewhat complicated, and that is only with a few of the bundle file types and a fairly simple set of configurations. Luckily, CloudBees CI Configuration as Code (CasC) for Controllers supports an export capability that allows you to export the current configuration from an existing controller. In this lab you will make configurations changes on your Ops controller and then use the export feature to copy new or updated configuration to the files in the Ops controller branch of your `ops-controller` repository.

1. Navigate to the top level of your Ops controller - it will be in the folder with the same name as your workshop GitHub Organization name (lower-cased).
2. You will see a folder named `controller-jobs` and within that folder there will be a GitHub Organization job named `cbci-casc-automation` which we will take a deeper look at in the next lab.
2. At the top level of your Ops controller, click on the **Mange Jenkins** link in the left menu. ![Manage Jenkins link](manage-jenkins-link.png?width=50pc) 
3. On the **Manage Jenkins** page click on **Manage Plugins** under the **System Configuration** section. ![Manage Plugins link](manage-plugins-link.png?width=50pc) 
4. On the **Plugin Manager** screen, click on the **Available** tab and enter ***CloudBees Restrict*** into the search box. Then check the **Install** checkbox for the **CloudBees Restricted Credentials Plugin** and then click the the **Install without restart** button. ![Search for Plugin](search-plugin.png?width=50pc) 
5. Once the **CloudBees Restricted Credentials Plugin** is successfully installed, return to the top-level of your Ops controller and click on the **Mange Jenkins** link in the left menu. ![Install plugin](install-plugin.png?width=50pc) 
6. On the **Manage Jenkins** page click on **CloudBees Configuration as Code export and update** under the **System Configuration** section. ![CloudBees CasC link](cloudbees-casc-link.png?width=50pc) 
7. Next, on the **CloudBees Configuration as Code export and update** page under the **Current configuration** tab, click on the *visualize* link for the `plugin-catalog.yaml` **Filename**. A [plugin catalog](https://docs.cloudbees.com/docs/admin-resources/latest/plugin-management/configuring-plugin-catalogs) is used to include plugins that are not in the CloudBees Assurance Program (CAP); tested and used by your software delivery workloads. Since the **CloudBees Restricted Credentials Plugin** is not in CAP we must create a plugin catalog that includes that plugin so we may install it on a controller with CasC. ![Plugin Catalog visualize link](plugin-catalog-visualize-link.png?width=50pc) 
8. A new browser page will open in a new tab or window with the auto-generated contents of a Plugin Catalog with the following contents:
```yaml
type: plugin-catalog
version: '1'
name: ops-controller
displayName: Autogenerated catalog from ops-controller
configurations:
- description: Exported plugins
  includePlugins:
    cloudbees-restricted-credentials: {version: '0.1'}
```

9. Copy the contents of the `plugin-catalog.yaml` from above and then navigate to the `ops-controller` repository in your workshop GitHub Organization.
10. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
11. On the next screen, name the new file `plugin-catalog.yaml`, enter the contents from the `plugin-catalog.yaml` export. Then commit directly to the `main` branch. ![Commit plugin-catalog.yaml](commit-plugin-catalog.png?width=50pc)
12. Plugins in the `plugin-catalog.yaml` are not actually installed on a controller, rather they just extend what can be installed outside of CAP. In order for a plugin to be installed via a configuration bundle you must add it to the `plugins.yaml`. Click on the `plugins.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit plugins file GitHub](github-edit-plugins-file.png?width=50pc)
13. In the GitHub file editor, add `- id: cloudbees-restricted-credentials` under the `# non-cap plugins` comment, and then commit directly to the `main` branch. ![Commit plugins.yaml](commit-plugins.png?width=50pc)

{{%expand "expand for complete updated plugins.yaml file" %}}
```yaml
plugins:
- id: antisamy-markup-formatter
- id: cloudbees-casc-api
- id: cloudbees-github-reporting
- id: cloudbees-groovy-view
- id: cloudbees-monitoring
- id: cloudbees-pipeline-policies
- id: cloudbees-prometheus
- id: cloudbees-slack
- id: cloudbees-template
- id: cloudbees-view-creation-filter
- id: cloudbees-workflow-template
- id: cloudbees-workflow-ui
- id: configuration-as-code
- id: git
- id: github-branch-source
- id: managed-master-hibernation
- id: notification-api
- id: operations-center-cloud
- id: operations-center-notification
- id: pipeline-event-step
- id: pipeline-model-extensions
- id: pipeline-stage-view
- id: warnings-ng
- id: workflow-aggregator
- id: workflow-cps-checkpoint
# non-cap plugins
- id: cloudbees-restricted-credentials
```
{{% /expand%}}
14. In addition to updating the `plugins.yaml`, we also added the`plugin-catalog.yaml` file. But it is not listed in the `bundles.yaml`. In order to have that file used by configuration bundle on our controller, we need to add it to the `bundle.yaml` file, so click on the `bundles.yaml` file and then click on the ***Edit this file*** pencil button.
15. In the GitHub file editor for the `bundle.yaml` file, update the `version` field to **2** and add the following configuration to the end of the `bundle.yaml` file:
```yaml
catalog:
  - "plugin-catalog.yaml"
```

{{% notice note %}}
In previous versions of CloudBees CI Configuration as Code (CasC) for Controllers the `version` field of the `bundle.yaml` file had to be modified in order for an update to be triggered for controllers using that bundle. This is no longer required as any change in any file in a bundle will trigger a bundle update for any controllers using the updated bundle once those changes are copied to the JCasC bundle directory on Operations Center. However, it is still considered a best practice to increment the bundle version.
{{% /notice %}}

16. Commit the `bundle.yaml` file directly to the `main` branch of your `ops-controller` repository. ![Commit bundle.yaml](commit-bundle.png?width=50pc)
17. Navigate back to the top level of your Ops controller, click on the **controller-jobs** folder.  ![Controller jobs](controller-jobs-folder.png?width=50pc) 
18. On the **controller-jobs** folder click on the **Configure** left menu item. ![Configure folder](configure-folder-link.png?width=50pc) 
19. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **Pipeline**, **Multibranch Pipeline** and **Organization Folder** so only Jenkins Pipeline type jobs are allowed to be created in the folder; and then hit the **Save** button. ![Configure folder](configure-folder.png?width=50pc) 
20. Navigate back to the top-level of your Ops controller and click on the **Manage Jenkins** link in the left menu. ![Folder updated](folder-created.png?width=50pc) 
21. Next, On the **Manage Jenkins** page click on **CloudBees Configuration as Code export and update** under the **System Configuration** section.
22. On the **CloudBees Configuration as Code export and update** page of your Ops controller, instead of clicking the *visualize* link, click the *Copy content* link for the `items.yaml` **Filename**. ![Items copy content link](items-copy-content-link.png?width=50pc) 
23. Navigate to the top level of your copy of the `ops-controller` and click on the `items.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit items.yaml](edit-items.png?width=50pc)
24. Replace the entire contents of the file with the contents you copied from the `items.yaml` export and then commit directly to the `main` branch. ![Commit items.yaml](commit-items.png?width=50pc)

{{%expand "expand for complete updated items.yaml file" %}}
```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  displayName: controller-jobs
  name: controller-jobs
  description: ''
  items:
  - orphanedItemStrategy:
      defaultOrphanedItemStrategy:
        pruneDeadBranches: true
        daysToKeep: -1
        numToKeep: -1
    kind: organizationFolder
    displayName: cbci-casc-automation
    name: cbci-casc-automation
    navigators:
    - github:
        apiUri: https://api.github.com
        repoOwner: cbci-casc-workshop
        credentialsId: cloudbees-ci-casc-workshop-github-app
    projectFactories:
    - customMultiBranchProjectFactory:
        factory:
          customBranchProjectFactory:
            marker: Jenkinsfile
            definition:
              cpsScmFlowDefinition:
                scriptPath: controller-casc-automation
                scm:
                  gitSCM:
                    userRemoteConfigs:
                    - userRemoteConfig:
                        credentialsId: cloudbees-ci-casc-workshop-github-app
                        url: https://github.com/cbci-casc-workshop/ops-controller.git
                    branches:
                    - branchSpec:
                        name: '*/main'
                lightweight: true
    trigger:
      periodicFolderTrigger:
        interval: 1d
    strategy:
      allBranchesSame: {}
  properties:
  - envVars: {}
  - kubernetesFolderProperty: {}
  - itemRestrictions:
      allowedTypes:
      - org.jenkinsci.plugins.workflow.job.WorkflowJob
      - jenkins.branch.OrganizationFolder
      - org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject
      filter: true
```
{{% /expand%}}

25. The contents of your copy of the `ops-controller` repository in your workshop GitHub Organization should match the following screenshot: ![Repository contents](repository-contents.png?width=50pc)

So now we have an updated configuration bundle based on a bundle export from our Ops controller but the bundle hasn't actually been applied to the controller. In the next lab we will update the `cbci-casc-automation` job to actually update the bundle files on Operations Center, that will in turn trigger an available update on your controller, any time there is a commit to the `main` branch of your `ops-controller` repository.
