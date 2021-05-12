---
title: "Introduction to Declarative Pipelines with CloudBees CI"
chapter: false
weight: 2
--- 

In this first lab we will [create a Multibranch Pipeline project](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/github-branch-source-plugin) and get an overview of the [basic fundamentals of the Declarative Pipeline syntax](#basic-declarative-syntax-structure). 

## Create a GitHub Multibranch Pipeline Project

In this exercise we are going to create a special type of Jenkins Pipeline project referred to as a **[Multibranch Pipeline](https://jenkins.io/doc/book/pipeline/multibranch/)** (this type of project is also [available for Bitbucket](https://plugins.jenkins.io/cloudbees-bitbucket-branch-source) and [GitLab](https://github.com/jenkinsci/gitlab-branch-source-plugin)). The Jenkins *Multibranch Pipeline* project for GitHub will scan a GitHub Repository to discover the branches, automatically creating **managed** Pipeline jobs for any branch containing a *Jenkins Pipeline project recognizer* - typically **Jenkinsfile**. We will use the **helloworld-nodejs** repository in the GitHub Organization that you created in **[Setup - Create a GitHub Organization](/getting-started/pre-workshop-setup/#create-a-github-organization)**. We will also utilize a GitHub Organization level ***webhook*** to automatically manage Jenkins jobs associated with a branch (this includes pull requests) so when a branch is deleted from or added to the **helloworld-nodejs** the corresponding Pipeline job will be deleted from your controller.

1. Navigate to the top-level of the CloudBees CI Operations Center - **Dashboard** - and click on the link for your ***Managed Controller*** (it will have the same names as your workshop GitHub Organization). ![Managed Controller link](managed-controller-link.png?width=60pc)
2. At the top-level of your CloudBees CI Managed Controller click into the **pipelines** folder and then click on **New Item** in the left menu. Make sure you are in the **pipelines** folder and note that it is considered a best practice to create and manage all of your CloudBees CI jobs in folders.  ![New Item](new-item.png?width=50pc) 
3. Enter **helloworld-nodejs** as the **Item Name** and select **Multibranch Pipeline** as the item type and click the **OK** button - again, make sure you are in your **pipelines** folder. ![New GitHub Multibranch Pipeline](github-multibranch-item.png?width=50pc) 
4. On the Multibranch Pipeline configuration page scroll down to **Branch Sources**, click the **Add source** button and then select **GitHub** from the dropdown. ![Set Branch Source](branch-source.png?width=50pc) 
5. Next, select the **CloudBees CI Pipeline Workshop GitHub App** credential from the **Credentials** drop down and enter the URL for your workshop copy of the **helloworld-nodejs** GitHub repository as the value for the **Repository HTTPS URL** - ***https:\//github.com/{YOUR_GITHUB_ORGANIZATION}/helloworld-nodejs.git***.
6. The rest of the default values are sufficient so click the **Validate** button and then click the **Save** button. ![Configure and Save Multibranch Pipeline](configure-save-multibranch-item.png?width=50pc) 
7. After the repository scan completes, click on the bread-crumb link to go back to your **Multibranch Pipeline** folder that is synced with your workshop copy of the **helloworld-nodejs** repository. When the scan is complete your **Multibranch Pipeline** project should be **empty**! ![Empty GitHub Organization Folder](empty-multibranch-project.png?width=50pc) 
8. CloudBees configuration-as-code (CasC) was used to create a GitHub Organization webhook for your workshop GitHub Organization. We need to verify that the webhook was created in Github by checking the **Webhooks** within your GitHub Organization **Settings**. *NOTE: This webhook will be used to automatically create new branch and Pull Request Pipeline jobs, and trigger those jobs on new commits.* ![GitHub Organization Webhook](github-org-webhook.png?width=50pc) 
9. The reason why the scan did not find any repositories is because there were no branches in the **helloworld-nodejs** repository with a `Jenkinsfile` in it, so let's fix that. Navigate to your copy of the **helloworld-nodejs** repository in your workshop GitHub Organization and click on the **Add file** button towards the top right of the screen and then select **Create new file**. ![Create Jenkinsfile](create-jenkinsfile.png?width=50pc) 
10. Name the file `Jenkinsfile` and add the following content:
```
pipeline {

}
``` 
![Jenkinsfile in GitHub Editor](jenkinsfile-github-editor.png?width=50pc) 
11. At the bottom of the screen enter a commit message, such as ***initial Jenkinsfile***, select the **Create a new branch for this commit and start a pull request**, name the branch **development** and click the **Propose new file** button. **IMPORTANT: Do Not Create a Pull Request on the next screen after saving**. ![Commit Jenkinsfile](commit-jenkinsfile.png?width=50pc) 
12. Navigate back to your new Jenkins Multibranch Pipeline project folder on your CloudBees CI Managed Controller and refresh your browser.  You should now have a new failed job for the **development** branch you just added the `Jenkinsfile`. Don't worry that it failed, that is expected and something we will fix in the next lab. *NOTE: If you do not have a new **development** pipeline job then click on the **Scan Repository Now** link in the left menu and then refresh your browser.*![Job Failed](job-failed.png?width=50pc) 

## Basic Declarative Syntax Structure

In the previous lesson your Pipeline ran and will have failed.

In this exercise we will update the Jenkinsfile Declarative Pipeline in your copy of the **helloworld-nodejs** repository using the GitHub file editor so the Pipeline job will complete successfully, as opposed to resulting in the following syntax errors:

```
WorkflowScript: 1: Missing required section "stages" @ line 1, column 1.
   pipeline {
   ^

WorkflowScript: 1: Missing required section "agent" @ line 1, column 1.
   pipeline {
   ^

2 errors
```

[Declarative Pipelines](https://jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline) must be enclosed within a `pipeline` block - which we have. But Declarative Pipelines must also contain a top-level `agent` declaration, and must contain exactly one `stages` block at the top level. The `stages` block must have at least one `stage` block but can have an unlimited number of additional `stage` blocks. Each `stage` block must have exactly one `steps` block. 

1. We will use the GitHub file editor to update the `Jenkinsfile` file in your copy of the **helloworld-nodejs** repository. Navigate to the `Jenkinsfile` file in the **development** branch of your **helloworld-nodejs** repository and then click on the pencil icon in the upper right to edit that file. **IMPORTANT:** Make sure you are editing the `Jenkinsfile` on your `development` branch** and **NOT the `main` branch**. ![Edit Basic Syntax](github-edit-basic-syntax.png?width=50pc) 
2. Replace the contents of that file with the following Declarative Pipeline:

```groovy
pipeline {
  agent any
  stages {
    stage('Say Hello') {
      steps {
        echo 'Hello World!'   
        sh 'java -version'
      }
    }
  }
}
```
![Basic Syntax Commit](basic-syntax-commit.png?width=50pc) 

3. Add a commit description and then click the **Commit Changes** button with the default selection of *Commit directly to the `development` branch* selected.
4. Navigate back to the **helloworld-nodejs** *development* branch job on your CloudBees CI Managed Controller and the job will complete successfully. Note some things from the log:
  
   i. The `Jenkinsfile` is being pulled from the **development** branch of your forked **helloworld-nodejs** repository.
   
   ii. The agent is being provisioned from a Kubernetes Pod Template (more on this in the next lesson):

  ```
  ...
  Agent default-jnlp-sx8fz is provisioned from template default-jnlp
  ...
  ```

   iii. Your copy of the **helloworld-nodejs** repository is being checked out, even though you did not put any steps in the `Jenkinsfile` to do so:

  ```
  ...
  Cloning repository https://github.com/cbci-pipeline/helloworld-nodejs.git
  ...
  ```

   iv. The agent has a Java version of `1.8.0_191`:

```
...
[Pipeline] sh
+ java -version
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (IcedTea 3.10.0) (Alpine 8.191.12-r0)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
...
```
  
> **NOTE:** You may have noticed that your Pipeline GitHub repository is being checked out even though you didn't specify that in your Jenkinsfile. Declarative Pipeline checks out source code by default without the need to explicitly include the `checkout scm` step. Furthermore, this automatic checkout will occur in every `stage` that uses a different agent.

## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **development** branch of your copy **helloworld-nodejs** repository matches the one from below.


### Finished Jenkinsfile for *Introduction to Pipelines with CloudBees Core*
```
pipeline {
  agent any
  stages {
    stage('Say Hello') {
      steps {
        echo 'Hello World!'   
        sh 'java -version'
      }
    }
  }
}
```
