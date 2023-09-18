---
title: "CloudBees CI Configuration Bundle Inheritance and Advanced File Structure"
chapter: false
weight: 4
--- 

This lab will explore more advanced aspects of bundle composition to include bundle inheritance and using folders with multiple files. These features make it easier to manage configuration bundles at scale across many controllers.

## Organizing Configuration Bundles with Sub-folders and Multiple Files

CloudBees CI Configuration as Code (CasC) for Controllers allows managing bundle files in folders and allows the use of multiple files for certain bundle file types. In this lab we will split your JCasC configuration (the `jenkins.yaml` file) into two files and put those files in a `jcasc` folder to make the configuration files easier to manage.

{{% notice tip %}}
The `items` CasC configuration also supports managing multiple files in folders (and sub-folders) which may be very useful when managing many controller items with CloudBees CI CasC. Also, if you are managing items within sub-folders you may want to take advantage of the `items` `root` property that allows you to define the root path for item creation as part of individual `items` yaml files (of course you must ensure the root path exists on the controller).
{{% /notice %}}

1. Navigate to your `ops-controller` repository in your workshop GitHub Organization, click on the **Pull requests** link and click on the **Bundle Folders** pull request. ![PR link](pr-link.png?width=50pc) 
2. Click on the **Files changed** tab to review the requested configuration changes. ![PR Files Changed](pr-files-changed.png?width=50pc)
3. We have updated the `bundle.yaml` file to use all files in the new `jcasc` folder as `jcasc` configuration files, added the `credentials.yaml` file to the new `jcasc` folder and moved an updated version of the `jenkins.yaml` to the new `jcasc` folder.
4. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Bundle Folders** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
5. Navigate to the `main` branch job of the `ops-controller` Multibranch pipeline project on your Ops controller.
6. After the the `main` branch job has completed successfully, navigate to the top level of your Ops controller and refresh the page until you see the bundle version change in the system message (remember we updated the `controller-casc-update` job to auto-reload the bundle). ![Bundle Version Updated](bundle-version-updated.png?width=50pc) 
7. After the bundle has finished loading, click on the **Manage Jenkins** link in the left menu and then click on the **CloudBees Configuration as Code export and update** **System Configuration** item again and then click on the **Original Bundle** tab. ![Original bundle with folder](original-bundle-folder.png?width=50pc)
8. The **Original Bundle** view will show you what configuration is being managed by the configuration bundle assigned to your controller. Notice that there are now two *Jenkins configuration as defined by OSS CasC* files - `jcasc/01-cbci-casc-workshop-ops-controller.jcasc.credentials.yaml` and `jcasc/01-cbci-casc-workshop-ops-controller.jcasc.jenkins.yaml`; and both prefixed with `01`, the `id` of your bundle and include the name of the folder the configurations files are in. This is done to support including configuration files in folders and sub-folders, and to support bundle inheritance as we will see in the next section.

## Bundle Inheritance

Bundle inheritance allows you to easily share common configuration across numerous controllers. In this lab we will update your Ops controller bundle to extend a parent bundle, providing common configuration and plugins to be shared across all of your organizations' controllers. First, we will review the contents of the parent `base` bundle that has already been set-up on Operations Center (and is also the default bundle), and then we will update your Ops controller bundle to use the `base` bundle as a parent bundle. The `base` bundle will include Jenkins configuration that enforces best practices across all of the controllers in the CloudBees CI cluster and include a common set of plugins to be used across all controllers.

1. First we will take a look at the `bundle.yaml` for the `base` bundle (also available in GitHub [here](https://github.com/cloudbees-days/workshop-casc-bundles/blob/main/base/bundle.yaml) ):
```yaml
apiVersion: "1"
id: "base"
version: "1"
description: "Workshop Parent Configuration Bundle"
availabilityPattern: ".*"
jcascMergeStrategy: "override"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
catalog:
  - "plugin-catalog.yaml"
```
2. Note that the `jcascMergeStrategy` is set to `override`. [JCasC configuration](https://github.com/jenkinsci/configuration-as-code-plugin) supports different [merge strategies](https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/mergeStrategy.md), currently limited to `errorOnConflict` and `override`. Here, we are specifying that everyones' controllers use the `override` merge strategy.
  - `errorOnConflict` is what existed before merge strategies were added to JCasC and will result in a Jenkins exception when loading a bundle with conflicting configuration; meaning that a child bundle cannot overwrite any of the parent configuration values
  - `override` allows for JCasC configuration in a child bundle to override that of the parent bundle.

{{% notice note %}}
Your may also specify the JCasC merge strategy via the `-Dcasc.merge.strategy=override` system property.
{{% /notice %}}

3. Next let's take a detailed look at the `base` bundle `jenkins.yaml` (also available on GitHub [here](https://github.com/cloudbees-days/workshop-casc-bundles/blob/main/base/jenkins.yaml) ):
```yaml
jenkins:
  authorizationStrategy: "cloudBeesRoleBasedAccessControl"
  markupFormatter:
    rawHtml:
      disableSyntaxHighlighting: false
  numExecutors: 0
  projectNamingStrategy:
    pattern:
      description: "All project (job) names must be alphanumeric, lower case, may contain dashes/underscores and contain\
        \ no spaces with a limit of 30 characters and a minimum of 4 characters."
      forceExistingJobs: false
      namePattern: "^[a-z0-9-_]{4,30}$"
  quietPeriod: 0
  systemMessage: "Controller configured using CloudBees CI Base Configuration Bundle"
unclassified:
  buildDiscarders:
    configuredBuildDiscarders:
    - "jobBuildDiscarder"
    - simpleBuildDiscarder:
        discarder:
          logRotator:
            numToKeepStr: "5"
  cloudBeesSCMReporting:
    enabled: true
  gitHubConfiguration:
    apiRateLimitChecker: ThrottleOnOver
  globalDefaultFlowDurabilityLevel:
    durabilityHint: PERFORMANCE_OPTIMIZED
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 2400
beekeeper:
  enabled: true
  securityWarnings:
    enabledForCore: true
    enabledForPlugins: true
  upgrades:
    autoDowngradePlugins: false
    autoUpgradePlugins: false
notificationConfiguration:
  enabled: true
  router: "operationsCenter"
```
4. The parent `jenkins.yaml` enforces a number of best practices across all managed controllers to include: 
    - Setting the number of executors to 0 on controllers, as you should never execute jobs directly on a controller, rather you should always distribute jobs across agents.
    - Enforcing a project naming strategy to maintain clean job URLs and directory paths in the Jenkins home.
    - Setting the quite period to 0 to maximize speed of builds and utilization of ephemeral Kubernetes agents.
    - Configuring a global build discard policy to reduce controller disk usage. Read more about [best strategies for disk space management](https://support.cloudbees.com/hc/en-us/articles/215549798-Best-Strategy-for-Disk-Space-Management-Clean-Up-Old-Builds).
    - Enabling CloudBees SCM Reporting notifications.
    - Setting Pipeline performance.
    - Enforcing the use of the CloudBees Assurance Plugins.
    - Enabling [controller hibernation](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) to reduce infrastructure costs - controllers will only run when they need to.
    - Enabling [Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration) notifications to allow controllers to send and receive pipeline events.

5. Next, let's review the `plugins.yaml` that will provide a base set of plugins for all the controllers in our CloudBees CI cluster:
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
```
6. Finally, let's review the `plugin-catalog.yaml` that will extend CAP plugins and allow individual controllers to opt-in to their usage. 
```yaml
displayName: CloudBees CI Workshop Plugin Catalog
name: cbci-workshop-catalog
type: plugin-catalog
version: '1'
configurations:
- description: Workshop Additional Plugins
  includePlugins:
    pipeline-utility-steps: 
      version: 2.13.0
```
7. Now that we have reviewed the `base` bundle, navigate to your `ops-controller` repository in your workshop GitHub Organization, click on the **Pull requests** link and click on the **Bundle Inheritance** pull request. ![Inheritance PR link](inheritance-pr-link.png?width=50pc) 
8. Next, click on the **Files changed** tab to review the configuration changes. For the `bundle.yaml` note that we added `parent: base` and removed the `catalog` entry. ![Inheritance PR Files Changed](inheritance-pr-files-changed.png?width=50pc)
9. Click on the `jenkins.yaml` file link and you will see that much of the configuration has been removed since it will be provided by the parent bundle:
   - Deleted the `quietPeriod` under `jenkins`.
   - Updated the `systemMessage` to `'Jenkins configured using CloudBees CI CasC with controller overrides'`.
   - Under the `unclassified` section deleted everything except for the `globallibraries` section.
   - Update the `headerLabel` `text` to **v4**.
![jenkins.yaml changes](jenkins-yaml-changes.png?width=50pc)
10. Next, click on the `plugins.yaml` file link. The `plugin-catalog.yaml` has been deleted. Also, all of the plugins have been removed from the `plugins.yaml` file except for the non-CAP `pipeline-utility-steps` plugin made available to install via the parent bundle `plugin-catalog.yaml` configuration. Plugin files are merged so the majority of your controller plugins will now come from the parent defined standard list of plugins. Plugin catalog files are not merged, so we are relying on the parent bundle to defined the available non-CAP plugins. ![plugins.yaml changes](plugins-yaml-changes.png?width=50pc)
11. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Bundle Inheritance** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
12. Navigate to the `main` branch job of your `ops-controller` Multibranch pipeline project on your Ops controller.
13. After the the `main` branch job has completed successfully, navigate to the top level of your Ops controller, the ***system message*** should read - "Jenkins configured using CloudBees CI CasC with controller overrides" signifying that the `base` bundle has been overridden by your controller specific bundle. ![Overridden systemMessage](overridden-system-message.png?width=50pc) 

{{% notice note %}}
It takes a minute or two for the bundle files to be checked out, copied, updated and reloaded.
{{% /notice %}}

14. Next, click on the **Manage Jenkins** link in the left menu, and then click on the **CloudBees Configuration as Code export and update** *System Configuration* item.
15. On the **CloudBees Configuration as Code export and update** click on the **Original Bundle** tab. Notice that there are now three `jcasc` files: `jcasc/01-base.jenkins.yaml`, `jcasc/02-cbci-casc-workshop-ops-controller.jcasc.credentials.yaml` and `jcasc/02-cbci-casc-workshop-ops-controller.jcasc.jenkins.yaml`. CloudBees CI Configuration as Code (CasC) for Controllers automatically renames all JCasC files by prefixing them with the level of inheritance, the bundle id and their folder structure and then copies them into the `jcasc` directory. However, in the case of the `plugins.yaml`, multiple files are merged into one. Also note that the `items.yaml` file is prefixed and placed in an `items` folder. ![Original Bundle](original-bundle-base.png?width=50pc) 

