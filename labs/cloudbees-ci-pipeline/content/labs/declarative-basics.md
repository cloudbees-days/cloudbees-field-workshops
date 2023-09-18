---
title: "Introduction to Declarative Pipelines with CloudBees CI"
chapter: false
weight: 2
--- 

Jenkins Pipelines may be categorized by the syntax used to write the pipeline and the type of Jenkins job used to execute the pipeline. 

The two syntaxes are:

1. **Scripted Pipeline**: Scripted Pipeline provides a fully-featured Groovy based programming environment. 
2. **Declarative Pipeline**: Declarative Pipeline provides a simpler and more opinionated syntax with a more strict and pre-defined structure.

There are three main Jenkins job types for managing Jenkins Pipelines:

1. **Pipeline**: The original Pipeline job type, it allows defining the Jenkins Pipeline (Scripted or Declarative) inline where it is stored in the Jenkins home directory or to load a Jenkins Pipeline from source control.
2. **Multibranch Pipeline**: The Jenkins Pipeline must be defined in source control, and Jenkins will automatically discover, manage and execute the Jenkins Pipeline for branches which contain a Jenkinsfile in source control.
3. **Organization Folder (Pipeline)**: Enables Jenkins to monitor an entire GitHub Organization, Bitbucket Team/Project, GitLab Organization, or Gitea organization and automatically creates new Multibranch Pipeline project for repositories that contain a Jenkinsfile in at least one branch (including pull/merge requests).

In this first lab we will [create a Multibranch Pipeline project](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/github-branch-source-plugin) and get an overview of the [basic fundamentals of the Declarative Pipeline syntax](#basic-declarative-syntax-structure). 

{{% notice note %}}
There are numerous advantages to managing your Jenkins Pipelines as code that are explained in detail in *[Understanding and implementing Pipeline as Code](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-as-code)*.
{{% /notice %}}

## Create a GitHub Multibranch Pipeline Project

In this exercise we are going to create a special type of Jenkins Pipeline project referred to as a **[Multibranch Pipeline](https://jenkins.io/doc/book/pipeline/multibranch/)** (this type of project is also [available for Bitbucket](https://plugins.jenkins.io/cloudbees-bitbucket-branch-source) and [GitLab](https://github.com/jenkinsci/gitlab-branch-source-plugin)). The Jenkins *Multibranch Pipeline* project for GitHub will scan a GitHub repository to discover the branches, automatically creating **managed** Pipeline jobs for any branch containing a *Jenkins Pipeline project recognizer* - typically **Jenkinsfile**. We will use the **insurance-frontend** repository in the GitHub Organization that you created in **[Setup - Create a GitHub Organization](/getting-started/pre-workshop-setup/#create-a-github-organization)**. We will also utilize a GitHub Organization level ***webhook*** to automatically manage Jenkins jobs associated with a branch (this includes pull requests) so when a branch is deleted from or added to the **insurance-frontend** repository, the corresponding Pipeline job will automatically be deleted or added to your controller.

1. Navigate to the top-level of the CloudBees CI Operations Center - **Dashboard** - and click on the link for your ***managed controller*** (in the folder with the same name as your workshop GitHub Organization). ![Managed Controller link](managed-controller-link.png?width=60pc)
2. At the top-level of your CloudBees CI managed controller click into the **pipelines** folder and then click on **New Item** in the left menu. Make sure you are in the **pipelines** folder. ![New Item](new-item.png?width=50pc) 

{{% notice note %}}
It is considered a best practice to create and manage all of your CloudBees CI jobs in folders. Furthermore, we are leveraging the CloudBees Folders Plus plugin to limit the types of jobs that may be created in the folder to just three job types to include a Pipeline Catalog template based job that we will explore later in this workshop.
{{% /notice %}}

3. Enter ***insurance-frontend*** as the **Item Name** and select **Multibranch Pipeline** as the item type and click the **OK** button - again, make sure you are in your **pipelines** folder. ![New GitHub Multibranch Pipeline](github-multibranch-item.png?width=50pc) 
4. On the Multibranch Pipeline configuration page scroll down to **Branch Sources**, click the **Add source** button and then select **GitHub** from the dropdown. ![Set Branch Source](branch-source.png?width=50pc) 
5. Next, select the **CloudBees CI Pipeline Workshop GitHub App** credential from the **Credentials** drop down and enter the URL for your workshop copy of the **insurance-frontend** GitHub repository as the value for the **Repository HTTPS URL** - ***https:\//github.com/{YOUR_GITHUB_ORGANIZATION}/insurance-frontend.git***.
6. The rest of the default values are sufficient so click the **Validate** button and then click the **Save** button. ![Configure and Save Multibranch Pipeline](configure-save-multibranch-item.png?width=50pc) 
7. After the repository scan completes, click on the bread-crumb link to go back to your **Multibranch Pipeline** folder that is synced with your workshop copy of the **insurance-frontend** repository. When the scan is complete your **Multibranch Pipeline** project should be **empty**! ![Empty GitHub Organization Folder](empty-multibranch-project.png?width=50pc) 
9. The reason why the scan did not find any repositories is because there were no branches in your copy of the **insurance-frontend** repository with a `Jenkinsfile` in it, so let's fix that. Navigate to your copy of the **insurance-frontend** repository in your workshop GitHub Organization and click on the **Add file** button towards the top right of the screen and then select **Create new file**. Make sure that you don't commit the file to the `main` branch. ![Create Jenkinsfile](create-jenkinsfile.png?width=50pc) 
10. Name the file `Jenkinsfile` and add the following content:
```
pipeline {

}
``` 
![Jenkinsfile in GitHub Editor](jenkinsfile-github-editor.png?width=50pc) 
11. At the bottom of the screen enter a commit message, such as ***adding Jenkinsfile***. Notice the message regarding the `main` branch: *You can’t commit to main because it is a protected branch.* We will learn more about GitHub protected branches later in the workshop, so for now, create a new branch and give it a descriptive name such as **add-jenkinsfile** and click the **Propose new file** button. **IMPORTANT: Do Not Create a Pull Request on the next screen after saving**. ![Commit Jenkinsfile](commit-jenkinsfile.png?width=50pc) 
12. Navigate back to your new Jenkins Multibranch Pipeline project folder on your CloudBees CI Managed Controller and refresh your browser.  You should now have a new failed job for the **add-jenkinsfile** branch that you just added the `Jenkinsfile`. Don't worry that it failed, that is expected and something we will fix in the next lab. ![Job Failed](job-failed.png?width=50pc) 

{{% notice tip %}}
If you do not have a new **add-jenkinsfile** pipeline job then click on the **Scan Repository Now** link in the left menu and then refresh your browser.
{{% /notice %}}

## Basic Declarative Syntax Structure

In the previous lesson your Pipeline ran and will have failed.

In this exercise we will update the Jenkinsfile Declarative Pipeline in your copy of the **insurance-frontend** repository using the GitHub file editor so the Pipeline job will complete successfully, as opposed to resulting in the following syntax errors:

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

1. We will use the GitHub file editor to update the `Jenkinsfile` file in your copy of the **insurance-frontend** repository. Navigate to the `Jenkinsfile` file in the **add-jenkinsfile** branch of your **insurance-frontend** repository and then click on the pencil icon in the upper right to edit that file. 

{{% notice warning %}}
Make sure you are editing the `Jenkinsfile` on your **`add-jenkinsfile` branch** and **NOT the `main` branch**.
{{% /notice %}}

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

3. Add a commit description and then click the **Commit Changes** button with the default selection of *Commit directly to the `add-jenkinsfile` branch* selected.
4. Navigate back to the **insurance-frontend** *add-jenkinsfile* branch job on your CloudBees CI Managed Controller and the job will complete successfully. Note some things from the log:
  
   i. The `Jenkinsfile` is being pulled from the **add-jenkinsfile** branch of your forked **insurance-frontend** repository.
   
   ii. The agent is being provisioned from a Kubernetes Pod Template (more on this in the next lesson):

  ```
  ...
  Agent default-jnlp-sx8fz is provisioned from template default-jnlp
  ...
  ```

   iii. Your copy of the **insurance-frontend** repository is being checked out, even though you did not put any steps in the `Jenkinsfile` to do so:

  ```
  ...
  Cloning repository https://github.com/cbci-pipeline/insurance-frontend.git
  ...
  ```

   iv. The agent has a Java version of `11.0.15`:

```
...
[Pipeline] sh
+ java -version
openjdk version "11.0.15" 2022-04-19 LTS
OpenJDK Runtime Environment 18.9 (build 11.0.15+10-LTS)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.15+10-LTS, mixed mode, sharing)
...
```

{{% notice note %}}
You may have noticed that your Pipeline GitHub repository is being checked out even though you didn't specify that in your Jenkinsfile. Declarative Pipeline checks out source code by default without the need to explicitly include the `checkout scm` step. Furthermore, this automatic checkout will occur in every `stage` that uses a different agent.
{{% /notice %}}

## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **add-jenkinsfile** branch of your copy **insurance-frontend** repository matches the one from below.


### Finished Jenkinsfile for *Introduction to Declarative Pipelines with CloudBees CI*
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
