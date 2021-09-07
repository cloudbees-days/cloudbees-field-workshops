---
title: "Managing Job Configuration with CloudBees CI Configuration Bundles"
chapter: false
weight: 4
--- 

In addition to folders, the CloudBees CI CasC provides support for [managing the configuration of certain Jenkins job types](https://docs.cloudbees.com/docs/cloudbees-ci/latest/casc-controller/items#_supported_items_using_casc) (or items) to include:

- Freestyle jobs
- Pipeline jobs
- Multibranch Pipeline jobs
- GitHub Organization folders
- Bitbucket Team/Project folders

In this lab we will export the configuration for the GitHub Organization Folder project you created in the previous lab and then add it to your configuration bundle with some minor modifications to including removing redundant default fields and updating to only run for the `main` branch.

## Adding Job Configuration to the Configuration Bundle

1. Navigate back to the top-level of your Ops controller and you should see the new **controller-jobs** folder. Click on the **Manage Jenkins** link in the left menu. ![Folder created](folder-created.png?width=50pc) 
2. On the **Manage Jenkins** page click on **CloudBees Configuration as Code bundle** under the **System Configuration** section. ![CloudBees CasC link](cloudbees-casc-link.png?width=50pc) 
3. Next click on the *visualize* link for the `items.yaml` **Filename**. ![Items visualize link](items-visualize-link.png?width=50pc) 
4. A new browser page will open in a new tab or window with the auto-generated `items.yaml` with content very similar to the following:

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
    SCMSources:
    - github:
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - gitHubPullRequestDiscovery:
            strategyId: 1
        - gitHubForkDiscovery:
            trust:
              gitHubTrustPermissions: {}
            strategyId: 1
        repoOwner: cbci-casc-workshop
        credentialsId: cloudbees-ci-casc-workshop-github-app
        id: org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator::https://api.github.com::cbci-casc-workshop::ops-controller
        repository: ops-controller
        configuredByUrl: false
        repositoryUrl: https://github.com/cbci-casc-workshop/ops-controller
    kind: organizationFolder
    displayName: cbci-casc-workshop
    name: cbci-casc-workshop
    description: ''
    navigators:
    - github:
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - gitHubPullRequestDiscovery:
            strategyId: 1
        - gitHubForkDiscovery:
            trust:
              gitHubTrustPermissions: {}
            strategyId: 1
        repoOwner: cbci-casc-workshop
        credentialsId: cloudbees-ci-casc-workshop-github-app
    projectFactories:
    - customMultiBranchProjectFactory:
        factory:
          customBranchProjectFactory:
            marker: bundle.yaml
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
    - organizationChildHealthMetricsProperty:
        templates:
        - worstChildHealthMetric:
            recursive: true
        - averageChildHealthMetric: {}
        - jobStatusHealthMetric:
            unstable: true
            countVirginJobs: false
            failure: true
            success: true
            unbuilt: true
        - projectEnabledHealthMetric: {}
    - organizationChildOrphanedItemsProperty:
        strategy:
          inherit: {}
    - organizationChildTriggersProperty:
        templates:
        - periodicFolderTrigger:
            interval: 1d
    - {}
    - kubernetesFolderProperty: {}
    - noTriggerOrganizationFolderProperty:
        branches: .*
  properties:
  - envVars:
      vars:
        GITHUB_ORGANIZATION: ${GITHUB_ORGANIZATION}
  - kubernetesFolderProperty: {}
  - itemRestrictions:
      allowedTypes:
      - org.jenkinsci.plugins.workflow.job.WorkflowJob
      - jenkins.branch.OrganizationFolder
      - org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject
      - jenkins.branch.OrganizationFolder.org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator
      filter: true
```

5. Rather than copy it as is, we have provided a minimized version that eliminates unneeded configuration and modifies the GitHub Organization Folder to only run for the `main` branch of a repository:

```yaml
removeStrategy:
  rbac: SYNC
  items: NONE
items:
- kind: folder
  displayName: controller-jobs
  name: controller-jobs
  properties:
  - envVars:
      vars:
        GITHUB_ORGANIZATION: ${GITHUB_ORGANIZATION}
  - itemRestrictions:
      allowedTypes:
      - org.jenkinsci.plugins.workflow.job.WorkflowJob
      - org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject
      - jenkins.branch.OrganizationFolder.org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator
      - jenkins.branch.OrganizationFolder
      filter: true
  items:
  - kind: organizationFolder
    name: cbci-casc-workshop
    navigators:
    - github:
        traits:
        - headWildcardFilter:
            includes: main
        repoOwner: cbci-casc-workshop
        credentialsId: cloudbees-ci-casc-workshop-github-app
    projectFactories:
    - customMultiBranchProjectFactory:
        factory:
          customBranchProjectFactory:
            marker: bundle.yaml
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
```

6. Copy the provided `items.yaml` and navigate to the top level of your copy of the `ops-controller` repository in your workshop GitHub Organization.
7. 