---
title: "CloudBees CI Configuration Bundle Inheritance and Advanced File Structure"
chapter: false
weight: 4
--- 

This lab will explore more advanced aspects of bundle composition to include bundle inheritance and using folders with multiple files. Both of which make it easier to manage configuration bundles at scale.

## Organizing Configuration Bundles with Sub-folders and Multiple Files

CloudBees CI Configuration as Code (CasC) for Controllers bundles allows managing bundles files in folders and allows the use of multiple files for certain bundle type files. In this lab we will split your JCasC configuration into two files and put those files in a `jcasc` folder in order to make the configuration files easier to manage.

1. Navigate to the `ops-controller` repository in your workshop GitHub Organization and click on the `jenkins.yaml` file. 
2. Copy the entire `credentials` section from the `jenkins.yaml` file, navigate back to the top level of the repository and then click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
3. Name the new file `jcasc/credentials.yaml`, paste the copied `credentials` section content from the `jenkins.yaml` and select the option to **"Create a new branch for this commit and start a pull request"**, name the branch `jcasc-subfolder` and then click the **Propose changes** button. . ![Create credentials.yaml in jcasc folder](github-commit-credentials-yaml.png?width=50pc)
4. On the next screen click the **Create pull request** button to create a pull request to merge to the `main` branch when are done updating your `ops-controller` configuration bundle. ![Create sub-folder pull request](github-create-subfolder-pr.png?width=50pc)
5. Next, navigate to the **Code** of your `ops-controller` repository and select the `jcasc-subfolder` branch from the branch drop down. ![Select jcasc-subfolder branch](github-select-jcasc-subfolder-branch.png?width=50pc)
6. Once again, click on the `jenkins.yaml` file, copy the `jenkins` and `unclassified` sections, delete the `jenkins.yaml` file and on the next screen click the **Commit changes** button. ![Delete jenkins.yaml file](github-delete-jenkins-yaml.png?width=50pc)
7. Back at the top level of your `ops-controller` repository, click on the `jcasc` folder and then click on the **Add file** button and then select **Create new file**. ![Create new unclassified in GitHub](github-create-unclassified-file.png?width=50pc)
8. Name the file `jenkins.yaml` and paste the contents from the `jenkins` and `unclassified` sections of the `jenkins.yaml` file into the editor. The new `jenkins.yaml` contents should match the following:
```yaml
unclassified:
  globallibraries:
    libraries:
    - defaultVersion: "main"
      name: "pipeline-library"
      retriever:
        modernSCM:
          scm:
            github:
              credentialsId: "cloudbees-ci-casc-workshop-github-app"
              repoOwner: "REPLACE_GITHUB_ORG"
              repository: "pipeline-library"
```
9. After you have pasted `unclassified` section of the `jenkins.yaml` file into the editor, ensure that you are committing to the `jcasc-subfolder` branch and then click the **Commit changes** button. ![Commit unclassified.yaml](github-commit-unclassified-yaml.png?width=50pc)
10. The contents of your `jcasc` folder in the `jcasc-subfolder` branch should now match the following: ![Commit jcasc-subfolder contents](github-jcasc-subfolder-contents.png?width=50pc)
11. Navigating back to the top level of your `ops-controller` repository and ensuring that you are on the `add-parent-bundle` branch, click on the `bundle.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. 
12. Change the bundle `version` to **4** and update the `jcasc` section to match the following:
```yaml
apiVersion: "1"
version: "4"
id: "cbci-casc-workshop-ops-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop ops-controller Controller"
parent: "base"
jcasc:
  - "jcasc/credentials.yaml"
  - "jcasc/unclassified.yaml"
plugins:
  - "plugins.yaml"
items:
 - "items.yaml"
```
13. After you have made the changes, ensure that you are committing to the `jcasc-subfolder` branch and then click the **Commit changes** button. ![Commit jcasc folder bundle.yaml](github-commit-jcasc-folder-bundle-yaml.png?width=50pc)
14. We have now made all the necessary changes and can now merge the pull request to the `main` branch. In GitHub, click on the **Pull requests** tab and then click on the link for the **Create credentials.yaml** pull request. ![jcasc pull request link](github-jcasc-pr-link.png?width=50pc)
15. On the **Create credentials.yaml #2** pull request page, click the **Merge pull request** button, then click the **Confirm merge** button and then click the **Delete branch** button.
16. Navigate to the `ops-controller` Multibranch pipeline project on your Ops controller. ![ops-controller Mulitbranch](ops-controller-multibranch-jcasc.png?width=50pc)
17. After the the `main` branch job has completed successfully, navigate to the top level of your Ops controller, click on the **Manage Jenkins** link in the left menu, and then click on the **CloudBees Configuration as Code bundle** **System Configuration** item. ![CasC Configuration link](casc-config-link.png?width=50pc) 
18. On the **CloudBees Configuration as Code bundle** click on the **Bundle update** tab and you should see that there is a bundle update available. ![CasC bundle update](casc-bundle-update.png?width=50pc)
19. Click on the **Reload Configuration** button and then on the next screen click the **Yes** button to apply the bundle update. ![CasC bundle apply](casc-bundle-apply.png?width=50pc)
20. After the updated configuration bundle is finished being applied return to the **CloudBees Configuration as Code bundle** configuration page and click on the **Original Bundle** tab. 

## Bundle Inheritance

Bundle inheritance allows you to easily share common configuration across numerous controllers. In this lab we will update your Ops controller bundle to extend a parent bundle providing common configuration and plugins to be shared across all of your organizations controllers. First we will review the contents of the parent `base` bundle that has already and then we will update your Ops controller bundle to use the `base` bundle as a parent bundle. The `base` bundle will include Jenkins configuration that enforces best practices across all of the controllers in the CloudBees CI cluster and a common set of plugins to be used across all controllers.

1. First we will take a look at the `bundle.yaml` for the `base` bundle (also available on GitHub at https://github.com/cloudbees-days/parent-configuration-bundle/blob/main/bundle.yaml):
```yaml
apiVersion: "1"
id: "base"
version: "1"
description: "Workshop Parent Configuration Bundle"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
catalog:
  - "plugin-catalog.yaml"
```
2. Next we will review the content and the `jenkins.yaml` (also available on GitHub at https://github.com/cloudbees-days/parent-configuration-bundle/blob/main/jenkins.yaml):
```yaml
jenkins:
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
3. In addition to providing a common Jenkins pipeline shared library across all controllers, the parent `jenkins.yaml` enforces best practices to include: 
    - Setting the number of executors to 0 on controllers, as you should never execute jobs directly on controller, rather you should always use agents.
    - Enforcing a project naming strategy.
    - Setting the quite period to 0 to maximize speed of builds and utilization of ephemeral Kubernetes agents.
    - Configuring a global build discard policy to reduce controller disk usage. Read more about [best strategies for disk space management](https://support.cloudbees.com/hc/en-us/articles/215549798-Best-Strategy-for-Disk-Space-Management-Clean-Up-Old-Builds).
    - Enabling CloudBees SCM Reporting notifications.
    - Setting Pipeline performance.
    - Enforcing the use of the CloudBees Assurance Plugins.
    - Enabling [controller hibernation](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) to reduce infrastructure costs - controllers will only run when they need to.
    - Enabling [Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration) notifications to allow controllers to send and receive pipeline events.

4. Finally, let's review the `plugins.yaml` that will provide a base set of plugins for all the controllers in our CloudBees CI cluster:
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
5. Now that we have reviewed the contents of the `base` bundle we will update your Ops controller bundle to use it as a parent bundle. However, before we do that it is important to understand how JCasC files are processed. All JCasC configuration **MUST** be supplementary, meaning that a child bundle cannot overwrite any of the parent configuration values. Otherwise there will be a `ConfiguratorException` and the controller will not startup. Therefore, before we update the `ops-controller` configuration bundle we must ensure that it does not overwrite any of the parent bundle’s configuration elements. Navigate to the `ops-controller` repository in your workshop GitHub Organization. Anything that may need to be unique between different controllers should be configured at the controller level; at least until other [JCasC YAML merge strategies become available](https://github.com/jenkinsci/configuration-as-code-plugin/pull/1218).
6. Click on the `jenkins.yaml` file and then click on the ***Edit this file*** pencil button. ![Edit jenkins.yaml](github-edit-jenkins-yaml.png?width=50pc)
7. Now we will delete all the configuration that will be provided by the parent bundle:
   - Delete the entire `jenkins` section.
   - Under the `unclassified` section delete everything except for the `globallibraries` section.
   - Leave the entire `credentials` section.
8. Next, because we have other changes we need to make before we trigger a bundle update, select the option to **"Create a new branch for this commit and start a pull request"**, name the branch `add-parent-bundle` and then click the **Propose changes** button. ![Commit jenkins.yaml](github-commit-jenkins-yaml.png?width=50pc)
9. On the next screen click the **Create pull request** button to create a pull request to merge to the `main` branch when are done updating your `ops-controller` configuration bundle. ![Create pull request](github-create-pr.png?width=50pc)
10. Next, navigate to the **Code** of your `ops-controller` repository and select the `add-parent-bundle` branch from the branch drop down. ![Select add-parent-bundle branch](github-select-branch.png?width=50pc)
11. Click on the `plugin-catalog.yaml` file, again ensuring that you are on the `add-parent-bundle` branch, and then click the **Delete this file** button. ![Delete plugin-catalog.yaml](github-delete-plugin-catalog.png?width=50pc)
12. On the next screen, ensure that **Commit directly to the add-parent-bundle branch** is selected and click the **Commit changes** to commit the deletion to the `add-parent-bundle` branch. ![Commit delete plugin-catalog.yaml](github-commit-delete-plugin-catalog.png?width=50pc)
13. Next, again ensuring that you are on the `add-parent-bundle` branch, click on the `plugins.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. ![Edit plugin.yaml](github-edit-plugin-yaml.png?width=50pc)
14. Remove every single plugin entry except for the `pipeline-utility-steps` plugin. All of the plugins we are deleting will be provided by the parent bundle. After you have made the changes, ensure that you are committing to the `add-parent-bundle` branch and then click the **Commit changes** button. ![Commit plugin.yaml](github-commit-plugin-yaml.png?width=50pc)
15. Ensuring that you are on the `add-parent-bundle` branch, click on the `bundle.yaml` file and then click on the ***Edit this file*** pencil button to edit the file. 
16. Change the bundle `version` to **3**, then below the the description property add `parent: "base"` and finally delete the entry for the `catalog`. Your `bundle.yaml` should match the following:
```yaml
apiVersion: "1"
version: "3"
id: "cbci-casc-workshop-ops-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop ops-controller Controller"
parent: "base"
jcasc:
  - "jenkins.yaml"
plugins:
  - "plugins.yaml"
items:
 - "items.yaml"
```
17. After you have made the changes, ensure that you are committing to the `add-parent-bundle` branch and then click the **Commit changes** button. ![Commit bundle.yaml](github-commit-bundle-yaml.png?width=50pc)
18. We have now made all the necessary changes and can now merge the pull request to the `main` branch. In GitHub, click on the **Pull requests** tab and then click on the link for the **Update jenkins.yaml** pull request. ![pull request link](github-pr-link.png?width=50pc)
19. On the **Update jenkins.yaml #1** pull request page, click the **Merge pull request** button, then click the **Confirm merge** button and then click the **Delete branch** button. ![merge pull request](github-merge-pr.png?width=50pc)
20. Navigate to the `ops-controller` Multibranch pipeline project on your Ops controller. ![ops-controller Mulitbranch](ops-controller-multibranch.png?width=50pc)
21. After the the `main` branch job has completed successfully, navigate to the top level of your Ops controller, click on the **Manage Jenkins** link in the left menu, and then click on the **CloudBees Configuration as Code bundle** **System Configuration** item. ![CasC Configuration link](casc-config-link.png?width=50pc) 
22. On the **CloudBees Configuration as Code bundle** click on the **Bundle update** tab and you should see that there is a bundle update available. ![CasC bundle update](casc-bundle-update.png?width=50pc)
23. Click on the **Reload Configuration** button and then on the next screen click the **Yes** button to apply the bundle update. ![CasC bundle apply](casc-bundle-apply.png?width=50pc)
24. After your Ops Controller has finished restarting navigate back to the **CloudBees Configuration as Code bundle** configuration page and click on the **Original Bundle** tab. Notice that there are two `jcasc` files: `jcasc/base.jenkins.yaml` and `jcasc/cbci-casc-workshop-ops-controller.jenkins.yaml`. CloudBees CI Configuration as Code (CasC) for Controllers automatically renames all JCasC files by prefixing them with the bundle id and placing them in a `jcasc` directory. However, in the case of the `plugins.yaml`, multiple files are merged into one. ![Original Bundle](original-bundle.png?width=50pc) 


