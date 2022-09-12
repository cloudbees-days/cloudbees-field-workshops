---
title: "CloudBees Pipeline Template Catalogs"
chapter: false
weight: 7
--- 

Up to this point, the `Jenkinsfile` that we have created has grown and provides an overview of some important declarative pipeline concepts, but it does not do a whole lot. In this lab we will explore how pipeline templates, provided by the CloudBees CI [Pipeline Template Catalog](https://docs.cloudbees.com/docs/admin-resources/latest/pipeline-templates-user-guide/setting-up-a-pipeline-template-catalog) feature, are able to accelerate your continuous integration by providing ready-to-go, full featured pipelines.

Pipeline Template Catalogs provide version controlled, parameterized templates for Multibranch and stand-alone Pipeline jobs. In this lab we will use a template from a Pipeline Template Catalog to create another Multibranch Pipeline project for your copy of the `insurance-frontend` repository. However, the `Jenkinsfile` will be pulled from your `pipeline-template-catalog` repository instead of from your `insurance-frontend` repository. But the source code that the pipeline template executes upon will still be checked out from your `insurance-frontend` repository. 

## Creating Pipeline Jobs from Pipeline Templates

Creating a new job from a catalog template is as simple as filling in a few template specific parameters or by adding a simple yaml based job configuration to your controller's configuration as code bundle. After that, you will have an organization tested Pipeline for the **insurance-frontend** application with all the same benefits as a non-templatized Multibranch pipeline project. Also, note, that although everyone is using a template from their copy of the `pipeline-template-catalog` repository, we could just as easily have everyone use a template from the same repository. 

1. Navigate to the top-level of your CloudBees CI managed controller and click into the **pipelines** folder, and then click on **New Item** in the left menu. Make sure you are in the **pipelines** folder. ![New Item](new-item.png?width=50pc)
2. Enter ***insurance-frontend-container-build*** as the **Item Name** and select **Container Build** as the item type and click the **OK** button.  ![Create template job](create-template-job.png?width=50pc)
3. On the next screen, all of the pre-configured values should be correct. So all you have to do is click the **Save** button. ![Docker template Parameters](docker-template-params.png?width=50pc)

{{% notice note %}}
The **Repository Owner** parameter will match the GitHub Organization that you are using for the workshop; not what is in the screenshot above. 
{{% /notice %}}

4. After you click the **Save** button, the Multibranch Pipeline project (created by the template) will scan your `insurance-frontend` repository, creating a Pipeline job for each branch where there is a marker file that matches `Dockerfile` (or in this case, the `main`  branch). ![Docker template main branch job](docker-template-main-branch-job.png?width=50pc)
5. The marker file and parameters of a catalog template are defined in a `template.yaml` file that is stored alongside a `Jenkinsfile` within a subfolder of the Pipeline Template Catalog required top-level `templates` folder. The name of the subfolder will be used as an internal identifier of the template so it is recommended to keep it all lowercase with no spaces. Navigate to the `template.yaml` file under `/templates/container-build` in your copy of the `pipeline-template-catalog` repository and you will see a file similar to the one below:

```yaml
version: 1
type: pipeline-template
name: Container Build
templateType: MULTIBRANCH
description: Builds a top-level Dockerfile from the specified repository.
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
      id: container-image-build
      credentialsId: ${githubCredentialId}
      repoOwner: ${repoOwner}
      repository: ${repository}
      traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - gitHubPullRequestDiscovery:
            strategyId: 1
  markerFile: Dockerfile
```

6. The `REPLACE_GITHUB_ORG` `defaultValue` for the `repoOwner` parameter has been replaced with the name of your workshop GitHub Organization in your copy of the `template.yaml` file for your `container-build` template. Note also that the `templateType` is `MULTIBRANCH` and there is a `markerFile` configured with the value of `Dockerfile`.
7. You may have noticed that none of the `stages` are executed for the `main` branch job. Navigate to the `Jenkinsfile` in the same `container-build` subfolder (under the `templates` folder) of your copy of the `pipeline-template-catalog` repository, and you will discover why. The contents should match the screenshot below: ![container-build template Jenkinsfile](template-jenkinsfile.png?width=60pc)
Some of the highlights include:
    - On **line 1** we are importing a [Pipeline Shared Library](https://www.jenkins.io/doc/book/pipeline/shared-libraries/) that allows us to share custom steps between multiple pipeline definitions - templates or not.
    - On **line 3** we declare `agent none` as we don't want to spin up an agent if the `when` conditions are not satisfied.
    - On **line 7** the `skipDefaultCheckout` option is set to `true` to disable the automatic checkout of source code in every Declarative Pipeline `stage`, since we only need to checkout the source code in one `stage`. 
    - On **line 10** we define global environment variables. These will be available in all subsequent `stages` of the pipeline, even nested `stages`.
    - On **line 17** a `when` condition is defined that will only allow the **Staging PR** nested `stages` to be executed when the `branch` being processed is a GitHub pull request. This is why no `stages` were executed for the `main` branch.
    - On **line 28** we are calling the `containerBuildPushGeneric` Pipeline Shared Library global variable that provides a common, repeatable method for building and pushing Docker images. (In this case we are building and pushing container images with a tool called [Kaniko](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/using-kaniko) which allows building and pushing container images from a Kubernetes `pod` without Docker installed.)
    - On **line 29** `checkout scm` is called so the `containerBuildPushGeneric` global variable step will have access to the `Dockerfile` and application code of your `insurance-frontend` repository. We must explicitly call this as we disabled the Declarative Pipeline default checkout in the global `options` block above.
8. Now we will create a pull request in your copy of the `insurance-frontend` repository. Navigate to the `main` branch of your copy of the `insurance-frontend` repository and click on the `Jenkinsfile`. 
9. We are going to delete this `Jenkinsfile` since we will now be using the `Jenkinsfile` from the ***Container Build*** catalog template. Click on the trashcan icon at the top of the file, again ensuring that you are on the `main` branch. ![delete Jenkinsfile](delete-jenkinsfile.png?width=60pc)
10. On the next screen, make sure that ***Create a new branch for this commit and start a pull request.***, name the new branch **delete-jenkinsfile** and click the **Propose changes** button. ![propose changes](propose-changes.png?width=60pc)
11. On the next screen, click the **Create pull request** button. ![create pr](create-pr.png?width=60pc)
12. Navigate to the **insurance-frontend-container-build** job on your controller and you will see that there is a new **Pull Requests** job (you may need to refresh the page). ![pr job](pr-job.png?width=60pc)
13. Click on the **Pull Requests** tab and you should see a ***PR*** job running.
14. It will take the job a few minutes to complete as it is utilizing a [multistage Docker build](https://docs.docker.com/develop/develop-images/multistage-build/) in the `Dockerfile` that will build the `insurance-frontend` application from the source code checked out from your copy of the `insurance-frontend` repository and then creates a runtime container image that is pushed to a Google Cloud Artifact Registry via the `containerBuildPushGeneric` Pipeline Shared Library global variable step.

## Ephemeral Deployment Environments for Pull Requests

In this section we are going to provide a brief overview of [CloudBees Previews](). Although this is not Jenkins pipeline specific, it does allows us to easily provide preview environments for a GitHub pull request without any additional pipeline code. In previous versions of this workshop we used the following Jenkins pipeline shared library step to providing a staging environment for GitHub pull requests:

```groovy
def call(String name, 
         String imageTag, 
         String namespace = "staging",
         Closure body) {
  def label = "helm-${UUID.randomUUID().toString()}"
  def podYaml = libraryResource 'podtemplates/helm.yml'
  podTemplate(name: 'helm', inheritFrom: 'default-jnlp', label: label, yaml: podYaml, podRetention: never(), activeDeadlineSeconds:1) {
    node(label) {
      body()
      stagingUrl = "https://${name}.${env.DEPLOYMENT_ENV}.workshop.cb-sa.io"
      gitHubDeploy(REPO_OWNER, REPO_NAME, "", "staging", GITHUB_CREDENTIAL_ID, "true", "false")
      env.NAME=name
      env.IMAGE_TAG=imageTag
      env.NAMESPACE=namespace
      container('helm') {
        withCredentials([string(credentialsId: 'fm-key', variable: 'FM_KEY')]) {
          sh '''
            helm upgrade --install -f ./chart/values.yaml --set image.tag=$IMAGE_TAG --set fmToken=$FM_KEY --namespace=$NAMESPACE  $NAME ./chart
          '''
        }
      }
      gitHubDeployStatus(REPO_OWNER, REPO_NAME, stagingUrl, 'success', GITHUB_CREDENTIAL_ID)
      //only add comment for PRs - CHANGE_ID isn't populated for commits to regular branches
      if (env.CHANGE_ID) {
        def config = [message:"${env.DEPLOYMENT_ENV} environment deloyed by CloudBees CI and is available at: ${stagingUrl}"]
        gitHubComment(config)
      }
    }
  }
}
```

In addition to the additional pipeline code, we also had to manage the configuration and cleanup of environments in the Kubernetes cluster we are using for the workshop. CloudBees Previews eliminates the need for both.

1. Once the ***PR*** job has completed, navigate to the corresponding open pull request in your copy of the `insurance-frontend` repository. Make sure you are on the **Conversation** tab, scroll down to the comments, enter ***/preview*** and click the **Comment** button.
2. you should see a notice that you have requested a deployment under your comment and that it is **In progress**. ![deployment requests](deployment-requested.png?width=60pc)
3. After a minute or so you should see a message stating: "This branch was successfully deployed". Click on the **Show environments** link in that block and then click on the **View deployment** button. ![environment deployed](env-deployed.png?width=60pc)
4. Navigate back to the **Delete Jenkinsfile** pull request in your copy of the **insurance-frontend** GitHub repository. Ensure that you are on the **Conversation** tab and scroll down, click the **Merge pull request** button and then the **Confirm merge** button. Once the merge is complete, you should see the deployment block update to **No deployments**. ![no deployments](no-deployments.png?width=60pc)
5. Refresh the tab with your pull request preview environment and it should be gone. As soon as a pull request is closed, CloudBees Previews will destroy all environments associated with that pull request.


