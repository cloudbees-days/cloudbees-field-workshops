---
title: "CloudBees CI Configuration Bundle Inheritance and Advanced Structure"
chapter: false
weight: 4
--- 

This lab will explore more advanced aspects of bundle composition to include bundle inheritance and using folders with multiple files.

- Then update to use inheritance, make UI based changes to Ops controller and create new ops controller specific bundle. And use multiple files for JCASC files.

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
  globallibraries:
    libraries:
    - defaultVersion: "main"
      name: "pipeline-library"
      retriever:
        modernSCM:
          scm:
            github:
              credentialsId: "cloudbees-ci-workshop-github-app"
              repoOwner: "cbci-casc-workshop"
              repository: "pipeline-library"
cloudbees-pipeline-policies:
  config:
    policies:
    - action: "fail"
      name: "Timeout policy"
      rules:
      - entirePipelineTimeoutRule:
          maxTime: 30
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 2400
```
3. In addition to providing a common Jenkins pipeline shared library across all controllers, the parent `jenkins.yaml` enforces best practices to include: 
    - Setting the number of executors to 0 on controllers, as you should never execute jobs directly on controller, rather you should always use agents.
    - Enforcing a project naming strategy.
    - Setting the quite period to 0 to maximize speed of builds and utilization of ephemeral Kubernetes agents.
    - Configuring a global build discard policy to reduce controller disk usage. Read more about [best strategies for disk space management](https://support.cloudbees.com/hc/en-us/articles/215549798-Best-Strategy-for-Disk-Space-Management-Clean-Up-Old-Builds).
    - Enabling CloudBees SCM Reporting notifications.
    - Setting Pipeline performance.
    - Providing a standard Pipeline shared library across all controllers.
    - Enforcing a standard global Pipeline timeout using [CloudBees Pipeline Policies](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-policies).
    - Enabling [controller hibernation](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) to reduce infrastructure costs - controllers will only run when they need to.

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
5. Now that we have reviewed the contents of the `base` bundle we will update your Ops controller bundle to use it as a parent bundle. However, there is currently one major limitation with inheritance for the JCasC configuration file (typically `jenkins.yaml` as above). All JCasC configuration **MUST** be supplementary, meaning that a child bundle cannot overwrite any of the parent configuration values. Otherwise there will be a `ConfiguratorException` and the controller will not startup. Therefore, before we update the `ops-controller` configuration bundle we must ensure that it does not overwrite any of the parent bundle’s configuration elements. Navigate to the `ops-controller` repository in your workshop GitHub Organization.
6. Click on the `jenkins.yaml` file and then click on the ***Edit this file*** pencil button. 

## Organizing Configuration Bundles with Folder and Multiple Files

CloudBees CI Configuration as Code (CasC) for Controllers bundles allows managing bundles files in folders and allows the use of multiple files for certain bundle type files.

