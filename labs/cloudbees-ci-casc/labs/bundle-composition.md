---
title: "CloudBees CI Configuration Bundle Composition"
chapter: false
weight: 2
--- 

The YAML based configuration of a controller is described in a collection of files referred to as a Configuration as Code (CasC) for Controllers bundle that we will refer to as just ***configuration bundle*** for the rest of this workshop. The CloudBees CI Operations Center can store as many different configuration bundles as needed to represent any unique requirements between different controllers.

This lab will explore the composition of a CloudBees CI configuration bundle to include the manual updating of a configuration bundle and creating a configuration bundle from the bundle export of a *template* controller.

## Configuration Bundle Composition Overview

A configuration bundle may consist of the following YAML file types:

- **bundle** (required) - This file is an index file that describes the bundle, references the other files in the bundle and must be named `bundle.yaml`. Any files not listed in this file will not be included in the controller bundle.
- **jcasc** (optional) - This file contains the Jenkins configuration (global configuration, credentials), as defined by the Jenkins [Configuration as Code plugin](https://github.com/jenkinsci/configuration-as-code-plugin).
- **plugins** (optional) - This file contains a list of all the plugins that should be installed on the controller. Plugins that are not in the CloudBees Assurance Program (CAP) should be added via a Plugin Catalog.
- **catalog** (optional) - This file defines the catalog of versioned plugins outside of the CloudBees Assurance Program (CAP) that are available for installation on the controller. An optional location can also be specified for plugins that are not available in the standard update centers.
- **rbac** (optional) - This file defines the RBAC groups and roles at the root level of a controller. 
- **items** (optional) - This file defines items to be created on the controller. Currently, only folders can be managed and only a subset of fields are supported. 

>NOTE: You may have noticed that all the file types except for the **bundle** file are optional and wonder if it would make sense to have a configuration bundle that only had a **bundle** file.

- Create bare bones bundle from scratch
- Then use pre-configured controller to create bundle files from export.

In this lab we will explore the configuration bundle assigned to your Ops controller when it was dynamically provisioned.

1. Navigate to the `configuration-bundles` repository in your workshop GitHub Organization.
2. Select the GitHub branch with the name matching the initial CloudBees CI Controller that was provisioned for you - it will be the name of your workshop GitHub Organization prefixed with **ops**. ![Select Ops Controller Branch](select-ops-controller-branch.png?width=50pc) 
3. After switching to your Ops controller specific branch, click on the `bundle.yaml` file. Its contents will mostly match the following (the `id` and `description` will include your unique Ops controller name):
```yaml
apiVersion: "1"
version: "1"
id: "cloudbees-ci-casc-ops-cbci-casc-workshop"
description: "CloudBees CI configuration bundle for the CloudBees CI CasC Workshop ops-cbci-casc-workshop Controller"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
``` 
>NOTE: It is important that the bundle file is named exactly `bundle.yaml` otherwise the bundle will not be useable.
4. Return to the top level of your Ops controller branch and click on the `jenkins.yaml` file. The name of this file must match the file name listed under `jcasc` in the `bundle.yaml` file. Its contents will mostly match the following, except for the `repoOwner` field for the **pipeline-library** which will match your workshop GitHub Organization name, as will the `owner` field for the `gitHubApp` credential:
```yaml
jenkins:
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
    - defaultVersion: "master"
      name: "pipeline-library"
      retriever:
        modernSCM:
          scm:
            github:
              credentialsId: "cloudbees-ci-workshop-github-app"
              repoOwner: "cbci-casc-workshop"
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
          appID: "${gitHubAppId}"
          description: "CloudBees CI Workshop GitHub App credential"
          id: "cloudbees-ci-workshop-github-app"
          owner: "cbci-casc-workshop"
          privateKey: "${gitHubAppPrivateKey}"
```
>NOTE: Setting up an initial Ops controller is a bit like the chicken and the egg conundrum. There will typically be some required manual steps to bootstrap the initial automation. In the case of this workshop, we have our own Ops controller that is used to dynamically provision each attendees Ops controller with a dynamically generated configuration bundle when you installed the CloudBees CI CasC Workshop GitHub App into your workshop GitHub Organization.
5. As mentioned above, the `gitHubApp` credential is unique to your workshop GitHub Organization. But also notice the variable substitution for the `privateKey` field of that credential - the value in the `jenkins.yaml` file is `${gitHubAppPrivateKey}`. Of course you wouldn't want to store a secure secret directly in a JCasC yaml file, especially if it is to be store in source control. Luckily JCasC supports several ways to [pass secrets more securely](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc). For this workshop we are passing secrets through variables using the [Kubernetes Secrets Store CSI driver](https://secrets-store-csi-driver.sigs.k8s.io/introduction.html) with the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). This allows us to manage secrets with the Google Secret Manager in GCP and to mount those secrets as files in the directory on your controller configured for JCasC to read secret variables from with the file name being the variable name and the file contents being the value.
6. Return again to the top level of your Ops controller branch and click on the `plugins.yaml` file. The name of this file must match the file name listed under `plugins` in the `bundle.yaml` file. Its contents will match the following:
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
```
## Creating a Configuration Bundle from a Bundle Export
As you can see from composition overview above, the YAML in the different configuration files can be somewhat complicated, and that is only with a few of the bundle file types and a fairly simple set of configurations. Luckily, the CloudBees CI CasC supports an export capability that allows you export the current configuration from an existing controller. In this lab you will make configurations changes on your Ops controller and then use the export feature to copy new or updated configuration to the files in the Ops controller branch of your `configuration-bundles` repository.

1. Navigate to the top-level of your Ops controller - it will be in the Operations Center **operations** folder and have the same name as your workshop GitHub Organization name (lower-cased) and prefixed with **ops-**.
2. At the top-level of your Ops controller, click on the **Mange Jenkins** link in the left menu. ![Manage Jenkins link](manage-jenkins-link.png?width=50pc) 
3. On the **Manage Jenkins** page click on **Manage Plugins** under the **System Configuration** section. ![Manage Plugins link](manage-plugins-link.png?width=50pc) 
4. On the **Plugin Manager** screen, click on the **Available** tab and enter ***Pipeline Util*** into the search box. Then check the **Install** checkbox for the **Pipeline Utility Steps** plugin and then click the the **Install without restart** button. ![Search for Pipeline Util](search-pipeline-util.png?width=50pc) 
5. Once the **Pipeline Utility Steps** plugin is successfully installed return to the top-level of your Ops controller. ![Install plugin](install-plugin.png?width=50pc) 
6. At the top-level of your Ops controller, click on **Create a job** link.  ![Create a job](create-job-link.png?width=50pc) 
7. On the job creation screen, enter ***controller-automation*** as the name, select **Folder** as the type and then click the **OK** button. ![Create folder](create-folder.png?width=50pc) 
8. On the next screen click the **Save** button to create the **controller-automation** folder and then navigate back to the top-level of your Ops controller. ![Folder created](folder-created.png?width=50pc) 
9. On the **Manage Jenkins** page click on **CloudBees Configuration as Code bundle** under the **System Configuration** section. ![CloudBees CasC link](cloudbees-casc-link.png?width=50pc) 
10. Next, on the **CloudBees Configuration as Code bundle** page, click on the *visualize* link for the `plugin-catalog.yaml` **Filename**. A [plugin catalog](https://docs.cloudbees.com/docs/admin-resources/latest/plugin-management/configuring-plugin-catalogs) is used to widen the acceptable scope of plugins beyond those defined by the CloudBees Assurance Program (CAP) and since the **Pipeline Utility Steps** is not in CAP we must create a plugin catalog that includes that plugin so we may install it on our controller. ![Plugin Catalog visualize link](plugin-catalog-visualize-link.png?width=50pc) 
11. A new browser page will open in a new tab or window with the auto-generated contents of a Plugin Catalog with the following contents:
```yaml
type: plugin-catalog
version: '1'
name: ops-cbci-casc-workshop
displayName: Autogenerated catalog from ops-cbci-casc-workshop
configurations:
- description: Exported plugins
  includePlugins:
    pipeline-utility-steps: {version: 2.8.0}
```
12. Copy the contents of the auto-generated `plugin-catalog.yaml` and then navigate to the `configuration-bundles` repository in your workshop GitHub Organization.
13. Click on the branch selector and switch to the branch with the same name as your Ops controller. ![Select Ops Controller Branch](select-ops-controller-branch.png?width=50pc) 
14. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
15. On the next screen, name the new file `plugin-catalog.yaml`, enter the contents from the `plugin-catalog.yaml` export (same as above) and then commit directly to your Ops controller branch. ![Commit plugin-catalog.yaml](commit-plugin-catalog.png?width=50pc)
16. Plugins in the `plugin-catalog.yaml` are not actually installed on a controller, rather they just extend what can be installed outside of CAP. In order for a plugin to be installed via a configuration bundle you must add it to the `plugins.yaml`. On the branch with the same name as your Ops controller click on the `plugins.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit plugins file GitHub](github-edit-plugins-file.png?width=50pc)
17. In the GitHub file editor, add `- id: pipeline-utility-steps` under the line containing the content `- id: pipeline-stage-view`, and then commit directly to your Ops controller branch. ![Commit plugins.yaml](commit-plugins.png?width=50pc)
18. Next, back on the **CloudBees Configuration as Code bundle** page of your Ops controller, click on the *visualize* link for the `items.yaml` **Filename**. ![Items visualize link](items-visualize-link.png?width=50pc) 
19. A new browser page will open in a new tab or window with the auto-generated `items.yaml` with the following contents:
```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  name: controller-automation
  description: ''
  properties:
  - {}
```
>NOTE: Currently only folder items are supported and only some folder properties are supported. 
20. Copy the contents of the auto-generated `items.yaml` and then navigate to the top-level of the branch with the same name as your Ops controller in the `configuration-bundles` repository in your workshop GitHub Organization.
21. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
22. On the next screen, name the new file `items.yaml`, enter the contents from the `items.yaml` export (same as above) and then commit directly to your Ops controller branch. ![Commit items.yaml](commit-items.png?width=50pc)
23. So in addition to updating the `plugins.yaml`, we also added two new files: `plugin-catalog.yaml` and `items.yaml`. However, those files are not listed in the `bundles.yaml`. In order to include those files in the controller bundle we need to add them to the `bundle.yaml` file, so c lick on the `bundles.yaml` file and then click on the ***Edit this file*** pencil button.
24. In the GitHub file editor, add the following configuration to the end of the `bundle.yaml` file:
```yaml
catalog:
  - "plugin-catalog.yaml"
items:
 - "items.yaml"
```
25. Commit the `bundle.yaml` file directly to your Ops controller branch. ![Commit bundle.yaml](commit-bundle.png?width=50pc)

So now we have an updated configuration bundle based on a bundle export from our Ops controller. In the next lab we will set up a job to actually update