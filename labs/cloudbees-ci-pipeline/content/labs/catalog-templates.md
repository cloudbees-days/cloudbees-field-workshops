---
title: "CloudBees Pipeline Template Catalogs"
chapter: false
weight: 5
--- 

Up to this point, the `Jenksfile` that we have created does not do a whole lot. We will quickly change that by using a template from a [Pipeline Template Catalog](https://docs.cloudbees.com/docs/admin-resources/latest/pipeline-templates-user-guide/setting-up-a-pipeline-template-catalog).

Pipeline Template Catalogs provide version controlled, parameterized templates for Multibranch and stand-alone Pipeline jobs. In this lab we will use a template from a Pipeline Template Catalog to create another Multibranch Pipeline project for your copy of the **insurance-fronted** repository. All you will need to do is fill in a few simple parameters and you will end up with a complete end-to-end CI/CD Pipeline for the **insurance-fronted** application - and it won't be using the Jenkinsfile from your repository.

1. Navigate to the top-level of your CloudBees CI managed controller click into the **pipelines** folder and then click on **New Item** in the left menu. Make sure you are in the **pipelines** folder. ![New Item](new-item.png?width=50pc)
2. Enter ***insurance-frontend-build-deploy*** as the **Item Name** and select **Container Build and Deploy** as the item type and click the **OK** button.  ![Create template job](create-template-job.png?width=50pc)
3. On the next screen, all of the pre-configured values should be correct. So all you have to do is click the **Save** button. ![Docker template Parameters](docker-template-params.png?width=50pc)

{{% notice note %}}
The **Repository Owner** parameter will match the GitHub Organization that you are using for the workshop; not what is in the screenshot above. 
{{% /notice %}}

4. After you click the **Save** button the Multibranch Pipeline project (created by the template) will scan your `insurance-frontend` repository, creating a Pipeline job for each branch where there is a marker file that matches `Dockerfile` (or in this case, the `main` and `development` branches). However, notice that none of the `stages` are executed for either of those branches.
5. The marker file and parameters of a catalog template are defined in a `template.yaml` file that is stored alongside a `Jenkinsfile` within a subfolder of a required top-level `templates` folder. The name of the subfolder will be used as an internal identifier of the template so it is recommended to keep it all lowercase with no spaces. Navigate to the `template.yaml` file under `/templates/container-build-push` in your copy of the `pipeline-template-catalog` repository and you will see a file similar to the one below:

```yaml
version: 1
type: pipeline-template
name: Container Build and Deploy
templateType: MULTIBRANCH
description: Builds a top-level Dockerfile from the specified repository and deploys it using a Helm chart from the same repository. 
parameters:
  - name: repoOwner
    type: string
    displayName: Repository Owner
    defaultValue: REPLACE_GITHUB_ORG
  - name: repository
    type: string
    displayName: Repository
    defaultValue: insurance-frontend
  - name: githubCredentialId
    displayName: GitHub Credential ID
    type: CREDENTIALS
    defaultValue: cloudbees-ci-pipeline-workshop-github-app
multibranch:
  branchSource:
    github:
      id: container-image-build-deploy
      credentialsId: ${githubCredentialId}
      repoOwner: ${repoOwner}
      repository: ${repository}
      traits:
        - gitHubPullRequestDiscovery:
            strategyId: 2
  markerFile: Dockerfile
```

6. The `REPLACE_GITHUB_ORG` `defaultValue` for the `repoOwner` parameter has been replaced with the name of your workshop GitHub Organization in your copy of the `template.yaml` file for your `container-build-deploy` template. Note also that the `templateType` is `MULTIBRANCH` and there is a `markerFile` configured with the value of `Dockerfile`.
7. Next, navigate to the `Jenkinsfile` in the same `container-build-deploy` subfolder (under the `templates` folder) of your copy of the `pipeline-template-catalog` repository. The contents should match the screenshot below: ![container-build-deploy template Jenkinsfile](template-jenkinsfile.png?width=60pc)
Some of the highlights include:
    - On **line 1** we are importing a [Pipeline Shared Library](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) that allows us to share custom steps between multiple pipeline definitions - templates or not.
    - One **line 3** we declare `agent none` as we don't want to spin up an agent if the `when` conditions are not satisfied.
    - On **line 7** the `skipDefaultCheckout` option is set to `true` to disable the automatic checkout of source code in very Declarative Pipeline `stage` since we only need to checkout the source code for one `stage`. 
    - On **line 10** we define global environment variables. These will be available in all subsequent `stages` of the pipeline.
    - On **line 17** a `when` condition is defined that will only execute the **Staging PR** nested `stages` when the `branch` be processed is a GitHub pull request.
    - On **line 28** we are calling the `containerBuildPushGeneric` Pipeline Shared Library global variable that provides a common repeatable method for building and pushing Docker images. In this case we are building and pushing with a tool called [Kaniko](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/using-kaniko) which allows building and pushing container images from a Kubernetes `pod` without Docker installed.
    - On **line 29** `checkout scm` is called so the `containerBuildPushGeneric` global variable step will have access to the `Dockerfile` and application code of your `insurance-frontend` repository.
    - On **line 31**, the `stash` command is used to copy the Helm `chart` files for use in a later stage. This will alleviate the need to checkout the entire `insurance-frontend` repository again.
    - On **line 38**, we call the `helmDeploy` global variable step.
    - On **line 39**, we use the `unstash` step to make the Helm `chart` files available to the `helmDeploy` step.
8. 


