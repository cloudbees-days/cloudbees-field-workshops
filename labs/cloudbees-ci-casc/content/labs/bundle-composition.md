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

{{% notice note %}}
You may have noticed that all the file types except for the **bundle** file are optional and wonder if it would make sense to have a configuration bundle that only had a **bundle** file.
{{% /notice %}}

- Create bare bones bundle from scratch
- Then use pre-configured controller to create bundle files from export.

In this lab we will explore the configuration bundle assigned to your Ops controller when it was dynamically provisioned.

1. Navigate to the `ops-controller` repository in your workshop GitHub Organization. ![ops-controller repository](ops-controller-repo.png?width=50pc) 
2. Click on the `bundle.yaml` file. Its contents will mostly match the following (the `id` and `description` will include your workshop GitHub Organization name):
```yaml
apiVersion: "1"
version: "1"
id: "cbci-casc-workshop-ops-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop ops-controller Controller"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
``` 
>NOTE: It is important that the bundle file is named exactly `bundle.yaml` otherwise the bundle will not be useable.
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
>NOTE: Setting up an initial Ops controller is a bit like the chicken and the egg conundrum. There will typically be some required manual steps to bootstrap the initial automation. In the case of this workshop, we have our own Ops controller that is used to dynamically provision each attendees Ops controller with a dynamically generated configuration bundle when you installed the CloudBees CI CasC Workshop GitHub App into your workshop GitHub Organization.
4. As mentioned above, the `gitHubApp` credential is unique to your workshop GitHub Organization. But also notice the variable substitution for the `privateKey` field of that credential - the value in the `jenkins.yaml` file is the `${gitHubAppPrivateKey}` variable. Of course you wouldn't want to store a secure secret directly in a JCasC yaml file, especially if it is to be store in source control. Luckily JCasC supports several ways to [pass secrets more securely](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc). For this workshop we are passing secrets through variables using the [Kubernetes Secrets Store CSI driver](https://secrets-store-csi-driver.sigs.k8s.io/introduction.html) with the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). This allows us to manage secrets with the Google Secret Manager in GCP and to mount those secrets as files in the directory on your controller configured for JCasC to read secret variables with the file name being the variable name and the file contents being the secret value.
5. Return to the top level of your `ops-controller` repository and click on the `plugins.yaml` file. The name of this file must match the file name listed under `plugins` in the `bundle.yaml` file. Its contents will match the following:
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
## Creating/Updating a Configuration Bundle from a Bundle Export
As you can see from the composition overview above, the YAML in the different configuration files can be somewhat complicated, and that is only with a few of the bundle file types and a fairly simple set of configurations. Luckily, CloudBees CI Configuration as Code (CasC) for Controllers supports an export capability that allows you to export the current configuration from an existing controller. In this lab you will make configurations changes on your Ops controller and then use the export feature to copy new or updated configuration to the files in the Ops controller branch of your `ops-controller` repository.

1. Navigate to the top level of your Ops controller - it will be in the folder with the same name as your workshop GitHub Organization name (lower-cased).
2. At the top level of your Ops controller, click on the **Mange Jenkins** link in the left menu. ![Manage Jenkins link](manage-jenkins-link.png?width=50pc) 
3. On the **Manage Jenkins** page click on **Manage Plugins** under the **System Configuration** section. ![Manage Plugins link](manage-plugins-link.png?width=50pc) 
4. On the **Plugin Manager** screen, click on the **Available** tab and enter ***Pipeline Util*** into the search box. Then check the **Install** checkbox for the **Pipeline Utility Steps** plugin and then click the the **Install without restart** button. ![Search for Pipeline Util](search-pipeline-util.png?width=50pc) 
5. Once the **Pipeline Utility Steps** plugin is successfully installed return to the top-level of your Ops controller. ![Install plugin](install-plugin.png?width=50pc) 
6. At the top level of your Ops controller, click on **Create a job** link.  ![Create a job](create-job-link.png?width=50pc) 
7. On the item creation screen, enter ***controller-jobs*** as the name, select **Folder** as the type and then click the **OK** button. ![Create folder](create-folder.png?width=50pc) 
8. On the next screen click on the **Properties** tab, then enter `GITHUB_ORGANIZATION=${GITHUB_ORGANIZATION}` in the **Environment Variables** text area, and then click the **Save** button. ![Configure folder](configure-folder.png?width=50pc) 
9. Navigate back to the top-level of your Ops controller and you should see the new **controller-jobs** folder. Click on the **Manage Jenkins** link in the left menu. ![Folder created](folder-created.png?width=50pc) 
10. On the **Manage Jenkins** page click on **CloudBees Configuration as Code export and update** under the **System Configuration** section. ![CloudBees CasC link](cloudbees-casc-link.png?width=50pc) 
11. Next, on the **CloudBees Configuration as Code bundle** page under the **Current configuration** tab, click on the *visualize* link for the `plugin-catalog.yaml` **Filename**. A [plugin catalog](https://docs.cloudbees.com/docs/admin-resources/latest/plugin-management/configuring-plugin-catalogs) is used to include plugins that are not in the CloudBees Assurance Program (CAP); tested and used by your software delivery workloads. Since the **Pipeline Utility Steps** is not in CAP we must create a plugin catalog that includes that plugin so we may install it on a controller. ![Plugin Catalog visualize link](plugin-catalog-visualize-link.png?width=50pc) 
12. A new browser page will open in a new tab or window with the auto-generated contents of a Plugin Catalog with the following contents (except the export does not put single quotes around the plugin version as we see below, this is needed to keep the `.0` from being stripped off):
```yaml
type: plugin-catalog
version: '1'
name: ops-cbci-casc-workshop
displayName: Autogenerated catalog from ops-cbci-casc-workshop
configurations:
- description: Exported plugins
  includePlugins:
    pipeline-utility-steps: {version: '2.8.0'}
```
13. Copy the contents of the auto-generated `plugin-catalog.yaml` and then navigate to the `ops-controller` repository in your workshop GitHub Organization.
14. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
15. On the next screen, name the new file `plugin-catalog.yaml`, enter the contents from the `plugin-catalog.yaml` export but **make sure your put single quotes around the plugin version**. Then commit directly to the `main` branch. ![Commit plugin-catalog.yaml](commit-plugin-catalog.png?width=50pc)
16. Plugins in the `plugin-catalog.yaml` are not actually installed on a controller, rather they just extend what can be installed outside of CAP. In order for a plugin to be installed via a configuration bundle you must add it to the `plugins.yaml`. Click on the `plugins.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit plugins file GitHub](github-edit-plugins-file.png?width=50pc)
17. In the GitHub file editor, add `- id: pipeline-utility-steps` under the line containing the content `- id: pipeline-stage-view`, and then commit directly to the `main` branch. ![Commit plugins.yaml](commit-plugins.png?width=50pc)

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
- id: pipeline-utility-steps
- id: warnings-ng
- id: workflow-aggregator
- id: workflow-cps-checkpoint
```
{{% /expand%}}

18. Next, back on the **CloudBees Configuration as Code bundle** page of your Ops controller, click on the *visualize* link for the `items.yaml` **Filename**. ![Items visualize link](items-visualize-link.png?width=50pc) 
19. A new browser page will open in a new tab or window with the auto-generated `items.yaml` with the following contents:
```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  name: controller-jobs
  description: ''
  properties:
  - kind: envVars
    vars:
      GITHUB_ORGANIZATION: '${GITHUB_ORGANIZATION}'
```
>NOTE: Currently only folder items are supported and only `envVars` folder properties are supported. 
20. Copy the contents of the auto-generated `items.yaml` and then navigate to the top level of your copy of the `ops-controller` repository in your workshop GitHub Organization.
21. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
22. On the next screen, name the new file `items.yaml`, enter the contents from the `items.yaml` export (same as above) and then commit directly to the `main` branch. ![Commit items.yaml](commit-items.png?width=50pc)
23. In addition to updating the `plugins.yaml`, we also added two new files: `plugin-catalog.yaml` and `items.yaml`. However, those files are not listed in the `bundles.yaml`. In order to include those files in the configuration bundle we need to add them to the `bundle.yaml` file, so click on the `bundles.yaml` file and then click on the ***Edit this file*** pencil button.
24. In the GitHub file editor for the `bundle.yaml` file, update the `version` field to **2** and add the following configuration to the end of the `bundle.yaml` file:
```yaml
catalog:
  - "plugin-catalog.yaml"
items:
  - "items.yaml"
```

{{%expand "expand for complete bundle.yaml file" %}}
```yaml
apiVersion: "1"
version: "2"
id: "cbci-casc-workshop-ops-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop ops-controller Controller"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
catalog:
  - "plugin-catalog.yaml"
items:
  - "items.yaml"
```
{{% /expand%}}

{{% notice note %}}
In previous versions of CloudBees CI Configuration as Code (CasC) for Controllers the `version` field of the `bundle.yaml` file had to be modified in order for an update to be triggered for controllers using that bundle. This is no longer required as any change in any file in a bundle will trigger a bundle update for any controllers using the updated bundle. However, it is still considered a best practice to increment the bundle version.
{{% /notice %}}

25. Commit the `bundle.yaml` file directly to the `main` branch of your `ops-controller` repository. ![Commit bundle.yaml](commit-bundle.png?width=50pc)
26. The contents of your copy of the `ops-controller` repository in your workshop GitHub Organization should match the following screenshot: ![Repository contents](repository-contents.png?width=50pc)
27. Finally, navigate back to the top level of your Ops controller, click on the **controller-jobs** folder and then click **Delete Folder** in the left menu. When the updated configuration bundle is applied to your Ops controller it will add the `controller-jobs` folder back. ![Delete folder](delete-folder.png?width=50pc)

So now we have an updated configuration bundle based on a bundle export from our Ops controller but the bundle hasn't actually been applied to the controller. In the next lab we will set up a job to actually update the bundle files on Operations Center, that will in turn trigger an available update on your controller, any time there is a commit to the `main` branch of your `ops-controller` repository.
