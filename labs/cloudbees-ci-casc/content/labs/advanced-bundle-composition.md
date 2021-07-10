---
title: "Advanced CloudBees CI Configuration Bundle Composition"
chapter: false
weight: 4
--- 

This lab will explore more advanced aspects of bundle composition to include bundle inheritance and using folders with multiple files.

- Then update to use inheritance, make UI based changes to Ops controller and create new ops controller specific bundle. And use multiple files for JCASC files.

## Bundle Inheritance

Bundle inheritance allows you to easily share common configuration across numerous controllers. In this lab we will update your Ops controller bundle to extend a parent bundle with common configuration and plugins to be shared across all of your organizations controllers. First we will review the contents of the parent `base` bundle that has already been created and then we will update your Ops controller bundle to use the `base` bundle as a parent bundle. The `base` bundle will include Jenkins configuration that enforces best practices across all of the controllers in the CloudBees CI cluster and a common set of plugins to be used across all controllers.

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
    - defaultVersion: "master"
      name: "pipeline-library"
      retriever:
        modernSCM:
          scm:
            github:
              credentialsId: "cloudbees-ci-workshop-github-app"
              repoOwner: "cbci-casc-workshop"
              repository: "pipeline-library"
  hibernationConfiguration:
    activities:
    - "build"
    - "web"
    enabled: true
    gracePeriod: 2400
```
3. Finally, let's review the `plugins.yaml` that will provide a base set of plugins for all the controllers in our CloudBees CI cluster:
```yaml

```
4. Now that we have reviewed the contents of the `base` bundle we will update your Ops controller bundle to use it as a parent bundle. First 

## Organizing Configuration Bundles with Folder and Multiple Files

CloudBees CI Configuration as Code (CasC) for Controllers bundles allows managing bundles files in folders and allows the use of multiple files for certain bundle type files.

