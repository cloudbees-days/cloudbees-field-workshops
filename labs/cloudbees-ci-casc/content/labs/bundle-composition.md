---
title: "CloudBees CI Configuration Bundle Composition"
chapter: false
weight: 2
--- 

The YAML based configuration of a controller is described in a collection of files referred to as a Configuration as Code (CasC) for Controllers bundle that we will refer to as just ***configuration bundle*** for most of this workshop. The CloudBees CI Operations Center can store as many different configuration bundles as needed to represent any unique requirements between different controllers.

This lab will explore the composition of a CloudBees CI configuration bundle, to include the manual updating of a configuration bundle and creating a configuration bundle from the bundle export of an existing controller.

## Configuration Bundle Composition Overview

A configuration bundle may consist of the following YAML file types:

- **bundle** (required) - This file is an index file that describes the bundle, references the other files in the bundle and must be named `bundle.yaml`. Any files not listed in this file will not be included in the controller bundle (even if it is in the bundle's directory). It also (optionally) allows you to specify an `availabilityPattern` which a regular expression that controls what controllers can use the bundle based on their location on Operations Center.
- **jcasc** (optional) - This file contains the Jenkins configuration (global configuration, credentials, plugin configuration, etc), as defined by the Jenkins [Configuration as Code plugin](https://github.com/jenkinsci/configuration-as-code-plugin).
- **plugins** (optional) - This file contains a list of all the plugins to be installed on the controller. Plugins that are not in the [CloudBees Assurance Program (CAP)](https://docs.cloudbees.com/docs/admin-resources/latest/assurance-program/) have to be added with a Plugin Catalog and to this file.
- **catalog** (optional) - This file defines the catalog of versioned plugins outside of the CloudBees Assurance Program (CAP) that are available for installation on the controller. An optional location can also be specified for plugins that are not available in the standard update centers. Adding plugins to a catalog only makes them available to install and they still must be added to the plugins file above.
- **rbac** (optional) - This file defines the RBAC groups and roles at the root level of a controller. 
- **items** (optional) - This file defines items (folders, jobs, etc) to be created on the controller.

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
availabilityPattern: "cloudbees-ci-casc-workshop/cbci-casc-workshop/ops-controller"
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
      - key: "GITHUB_ORGANIZATION"
        value: "${GITHUB_ORGANIZATION}"
      - key: "GITHUB_REPOSITORY"
        value: "ops-controller"
      - key: "BUNDLE_ID"
        value: "${CASC_BUNDLE_ID}"
  quietPeriod: 0
  systemMessage: 'Jenkins configured using CloudBees CI CasC v1'
notificationConfiguration:
  enabled: true
  router: "operationsCenter"
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
              credentialsId: "cloudbees-ci-casc-workshop-github-app"
              repoOwner: "${GITHUB_ORGANIZATION}"
              repository: "pipeline-library"
  headerLabel:
    text: "${GITHUB_APP}-bundle-v1"
credentials:
  system:
    domainCredentials:
    - credentials:
      - string:
          description: "CasC Update Secret"
          id: "casc-update-secret"
          scope: GLOBAL
          secret: "${cbciCascWorkshopControllerProvisionSecret}"
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

4. The `gitHubApp` credential is unique to your workshop GitHub Organization. But also notice the variable substitution for the `privateKey` field of that credential - the value in the `jenkins.yaml` file is the `${gitHubAppPrivateKey}` variable. Of course you wouldn't want to store a secure secret directly in a JCasC yaml file, especially if it is to be stored in source control. However, JCasC supports several ways to [pass secrets more securely](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc). For this workshop we are passing secrets by mounting secret volumes using the [Kubernetes Secrets Store CSI driver](https://secrets-store-csi-driver.sigs.k8s.io/introduction.html) with the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). This allows us to manage secrets with the Google Secret Manager in GCP and to mount those secrets as files in the directory on your controller configured for JCasC to read secret variables, with the file name being the variable name and the file contents being the secret value.

{{% notice tip %}}
There are also Kubernetes Secrets Store CSI providers for [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_csi_driver.html), [Azure Key Vault](https://docs.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) and [HashiCorp Vault](https://www.vaultproject.io/docs/platform/k8s/csi).
{{% /notice %}}

5. Return to the top level of your `ops-controller` repository and click on the `plugins.yaml` file. The name of this file must match the file name listed under `plugins` in the `bundle.yaml` file. Its contents will match the following:

```yaml
plugins:
- id: antisamy-markup-formatter
- id: cloudbees-casc-client
- id: cloudbees-casc-items-api
- id: cloudbees-casc-items-commons
- id: cloudbees-casc-items-controller
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
6. Return to the top level of your `ops-controller` repository and click on the `items.yaml` file. The name of this file must match the file name listed under `items` in the `bundle.yaml` file. Its contents will match the following (except for the `REPLACE_GITHUB_ORG` placeholders). Also note the `removeStrategy` configuration at the top, this specifies the strategy to handle existing configuration when a new configuration is applied, and is required for all `items` files (`NONE` is currently the only strategy available for `items`):

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
    displayName: controller-casc-update
    name: controller-casc-update
    orphanedItemStrategy:
      defaultOrphanedItemStrategy:
        pruneDeadBranches: true
        daysToKeep: -1
        numToKeep: -1
    SCMSources:
    navigators:
    - github:
        apiUri: https://api.github.com
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - headWildcardFilter:
            excludes: ''
            includes: main
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

7. There is one more configuration file in your `ops-controller` repository, but it is not part of the `bundle`. The `controller.yaml` file represents the CloudBees CI **managed controller** that was provisioned for you as part of the workshop setup. It has the same format as the `items.yaml` we reviewed above. However, it is applied to Operations Center with the [CloudBees CI CasC HTTP API](https://docs.cloudbees.com/docs/cloudbees-ci-api/latest/bundle-management-api) instead of being applied to your managed controller. Its contents will match the following (except for the `REPLACE_...` placeholders):

```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  name: cbci-casc-workshop
  groups:
  - members:
      users:
      - beedemo-dev
      - beedemo-dev-admin
    roles:
    - name: browse
      grantedAt: current
    - name: workshop-admin
      grantedAt: child
    name: Team Administrators
  filteredRoles:
  - workshop-admin
  - browse
  items:
  - kind: managedController
    name: ops-controller
    properties:
    - healthReporting:
        enabled: true
    - configurationAsCode:
        bundle: cbci-casc-workshop-ops-controller
    configuration:
      kubernetes:
        memory: 4000
        cpus: 1.0
        clusterEndpointId: default
        disk: 10
        storageClassName: premium-rwo
        domain: cbci-casc-workshop-ops-controller
        namespace: controllers
        yaml: |
          kind: "StatefulSet"
          spec:
            template:
              metadata:
                labels:
                  networking/allow-internet-access: "true"
              spec:
                containers:
                - name: "jenkins"
                  env:
                  - name: "SECRETS"
                    value: "/var/jenkins_home/jcasc_secrets"
                  - name: "GITHUB_ORGANIZATION"
                    value: "cbci-casc-workshop"
                  - name: "GITHUB_USER"
                    value: "beedemo-dev"
                  - name: "GITHUB_APP"
                    value: "cloudbees-ci-casc-workshop"
                  - name: "CONTROLLER_SUBDOMAIN"
                    value: "cbci-casc-workshop-ops-controller"
                  - name: "CASC_BUNDLE_ID"
                    value: "cbci-casc-workshop-ops-controller"
                  volumeMounts:
                  - name: "jcasc-secrets"
                    mountPath: "/var/jenkins_home/jcasc_secrets"
                volumes:
                - name: "jcasc-secrets"
                  secret:
                    secretName: cbci-mc-secret
```

## Creating/Updating a Configuration Bundle from a Bundle Export
As you can see from the composition overview above, the YAML in the different configuration files can be somewhat complicated, and that is with only a some of the bundle file types and a fairly simple set of configurations. Luckily, CloudBees CI Configuration as Code (CasC) for Controllers supports an export capability that allows you to export the current configuration from an existing controller. In this lab you will make configurations changes on your Ops controller using the UI and then use the export feature to copy new or updated configuration to the files in your `ops-controller` repository. First, we will add a new, non-CAP plugin and then we will add some properties to a folder - and we will use the CasC export functionality to copy the YAML for those updates to apply to the your bundle in your `ops-controller` repository.

1. Navigate to the top level of your Ops controller - it will be in the folder with the same name as your workshop GitHub Organization name (lower-cased), and you will see a folder named `controller-jobs`.
2. At the top level of your Ops controller, click on the **Mange Jenkins** link in the left menu. ![Manage Jenkins link](manage-jenkins-link.png?width=50pc) 
3. On the **Manage Jenkins** page click on **Manage Plugins** under the **System Configuration** section. ![Manage Plugins link](manage-plugins-link.png?width=50pc) 
4. On the **Plugin Manager** screen, click on the **Available** tab and enter ***CloudBees Restrict*** into the search box. Then check the **Install** checkbox for the **CloudBees Restricted Credentials Plugin** and then click the the **Install without restart** button. ![Search for Plugin](search-plugin.png?width=50pc) 
5. Once the **CloudBees Restricted Credentials Plugin** is successfully installed, click on the **Mange Jenkins** link in the left menu. ![Install plugin](install-plugin.png?width=50pc) 
6. On the **Manage Jenkins** page click on **CloudBees Configuration as Code export and update** under the **System Configuration** section. ![CloudBees CasC link](cloudbees-casc-link.png?width=50pc) 
7. Next, on the **CloudBees Configuration as Code export and update** page, under the **Current configuration** tab, click on the **Copy content** link for the `plugin-catalog.yaml` **Filename**. A [plugin catalog](https://docs.cloudbees.com/docs/admin-resources/latest/plugin-management/configuring-plugin-catalogs) is used to include plugins that are not in the CloudBees Assurance Program (CAP); tested and used by your software delivery workloads. Since the **CloudBees Restricted Credentials Plugin** is not in CAP we must add a plugin catalog to our bundle that includes that plugin, so we may install it on our controllers with CasC. ![Plugin Catalog copy link](plugin-catalog-copy-link.png?width=50pc) 
8. Navigate to the `ops-controller` repository in your workshop GitHub Organization and click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
9. On the next screen, name the new file `plugin-catalog.yaml`, paste the contents from the `plugin-catalog.yaml` export, and then commit directly to the `main` branch. ![Commit plugin-catalog.yaml](commit-plugin-catalog.png?width=50pc)
10. Again, plugins in the `plugin-catalog.yaml` are not actually installed on a controller, rather they just extend what can be installed outside of CAP. In order for a plugin to be installed via a configuration bundle you must add it to the `plugins.yaml`. Click on the `plugins.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit plugins file GitHub](github-edit-plugins-file.png?width=50pc)
11. In the GitHub file editor, add `- id: cloudbees-restricted-credentials` under the `# non-cap plugins` comment, and then commit directly to the `main` branch. ![Commit plugins.yaml](commit-plugins.png?width=50pc)

{{%expand "expand for complete updated plugins.yaml file" %}}
```yaml
plugins:
plugins:
- id: antisamy-markup-formatter
- id: cloudbees-casc-client
- id: cloudbees-casc-items-api
- id: cloudbees-casc-items-commons
- id: cloudbees-casc-items-controller
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
- id: cloudbees-restricted-credentials
```
{{% /expand%}}

12. In addition to updating the `plugins.yaml`, we also added the`plugin-catalog.yaml` file. But it is not listed in the `bundles.yaml`. In order to have that file used by the configuration bundle assigned to our controller, we need to add it to the `bundle.yaml` file. So click on the `bundles.yaml` file and then click on the ***Edit this file*** pencil button.
13. In the GitHub file editor for the `bundle.yaml` file, update the `version` field to **2** and add the following configuration to the end of the `bundle.yaml` file:

```yaml

catalog:
  - "plugin-catalog.yaml"
```

{{% notice note %}}
In previous versions of CloudBees CI Configuration as Code (CasC) for Controllers the `version` field of the `bundle.yaml` file had to be modified in order for an update to be triggered for controllers using that bundle. This is no longer required, as any change in any file in a bundle will trigger a bundle update for any controllers using the updated bundle once those changes are copied to the JCasC bundle directory on Operations Center. However, it is still considered a best practice to increment the bundle version.
{{% /notice %}}

14. Commit the `bundle.yaml` file directly to the `main` branch of your `ops-controller` repository. ![Commit bundle.yaml](commit-bundle.png?width=50pc)
15. Navigate back to the top level of your Ops controller, click on the **controller-jobs** folder.
16. On the **controller-jobs** folder screen, click on the **Configure** left menu item. ![Configure folder](configure-folder-link.png?width=50pc) 
17. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **Freestyle project**, **Pipeline**, **Multibranch Pipeline** and **Organization Folder** so only Jenkins Pipeline type jobs are allowed to be created in the folder; and then hit the **Save** button. ![Configure folder](configure-folder.png?width=50pc) 
18. After the updated **controller-jobs** folder configuration has been saved, click on the **Export CasC item** link in the left menu. ![Folder updated](export-casc-item-link.png?width=50pc) 
19. On the **Export CasC item** page, scroll down to the `properties` section at the bottom (as highlighted below). This is the only fragment we need to add to the `items.yaml` file in the `ops-controller` repository. ![Copy folder properties](copy-folder-properties.png?width=50pc)
20. Navigate to the top level of your copy of the `ops-controller` repository and click on the `items.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit items.yaml](edit-items.png?width=50pc)
21. Paste the `properties` fragment you copied from the `items.yaml` export right below `name: controller-jobs` and indent it two spaces to align with `name:controller-jobs` as seen below. Delete the `hudson.model.FreeStyleProject` entry (we decided we don't want anyone creating Freestyle jobs in that folder), and then commit directly to the `main` branch. ![Commit items.yaml](commit-items.png?width=50pc)

{{%expand "expand for complete updated items.yaml file" %}}
```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  displayName: controller-jobs
  name: controller-jobs
  properties:
  - envVars: {
      }
  - kubernetesFolderProperty: {
      }
  - itemRestrictions:
      allowedTypes:
      - org.jenkinsci.plugins.workflow.job.WorkflowJob
      - jenkins.branch.OrganizationFolder
      - org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject
      filter: true
  items:
  - kind: organizationFolder
    displayName: controller-casc-update
    name: controller-casc-update
    orphanedItemStrategy:
      defaultOrphanedItemStrategy:
        pruneDeadBranches: true
        daysToKeep: -1
        numToKeep: -1
    SCMSources:
    navigators:
    - github:
        apiUri: https://api.github.com
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - headWildcardFilter:
            excludes: ''
            includes: main
        repoOwner: cbci-casc-workshop
        credentialsId: cloudbees-ci-casc-workshop-github-app
    projectFactories:
    - customMultiBranchProjectFactory:
        factory:
          customBranchProjectFactory:
            marker: Jenkinsfile
            definition:
              cpsScmFlowDefinition:
                scriptPath: controller-casc-update
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
```
{{% /expand%}}
22. Finally, navigate back to the top level of your copy of the `ops-controller` repository and click on the `jenkins.yaml` file and then click on the ***Edit this file*** pencil button.
23. Update the `systemMessage` to `'Jenkins configured using CloudBees CI CasC v2'`, update `headerLabel` `text` to `"${GITHUB_APP}-bundle-v2"`, and then commit directly to the `main` branch.

{{%expand "expand for complete updated items.yaml file" %}}
jenkins:
  globalNodeProperties:
  - envVars:
      env:
      - key: "GITHUB_ORGANIZATION"
        value: "${GITHUB_ORGANIZATION}"
      - key: "GITHUB_REPOSITORY"
        value: "ops-controller"
      - key: "BUNDLE_ID"
        value: "${CASC_BUNDLE_ID}"
  quietPeriod: 0
  systemMessage: 'Jenkins configured using CloudBees CI CasC v2'
notificationConfiguration:
  enabled: true
  router: "operationsCenter"
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
              credentialsId: "cloudbees-ci-casc-workshop-github-app"
              repoOwner: "${GITHUB_ORGANIZATION}"
              repository: "pipeline-library"
  headerLabel:
    text: "${GITHUB_APP}-bundle-v2"
credentials:
  system:
    domainCredentials:
    - credentials:
      - string:
          description: "CasC Update Secret"
          id: "casc-update-secret"
          scope: GLOBAL
          secret: "${cbciCascWorkshopControllerProvisionSecret}"
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
{{% /expand%}}

So now we have an updated configuration bundle based on bundle exports from our Ops controller. However, the updated bundle hasn't actually been applied to your controller. In the next lab we will update the `controller-casc-update` job configuration so it will actually update the bundle files on Operations Center, that will in turn trigger an available update on your controller. After that, any time there is a commit to the `main` branch of your `ops-controller` repository, it will automatically be updated on your CloudBees CI controller.
