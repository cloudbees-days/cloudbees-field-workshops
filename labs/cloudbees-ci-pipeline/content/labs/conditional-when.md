---
title: "Conditional Execution Using the when Directive"
chapter: false
weight: 4
--- 

## Conditional Stages Using the When Directive

In this lab we will edit the `Jenkinsfile` file in your **insurance-frontend** repository with conditional execution using the [when directive](https://jenkins.io/doc/book/pipeline/syntax/#when). We will accomplish this by adding a branch specific `stage` to the `Jenkinsfile` in your **insurance-frontend** repository.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **add-jenkinsfile** branch of your **insurance-frontend** repository.
2. Insert the ***Deploy*** stage after the existing **Test** stage.
```
      stage('Deploy') {
        when {
          beforeAgent true
          branch 'main'
        }
        steps {
          echo "TODO - deploy"
        }
      }
```

Note the `beforeAgent true` option - this setting will result in the `when` condition being evaluated before acquiring and using a `stage` specific `agent`. The `branch` condition is a built-in condition that allows executing stages only for specific branches - in this case the ***Deploy*** `stage` will only execute for the **main** branch. The entire Pipeline should match what is below:

  ```
  pipeline {
    agent none
    stages {    
      stage('Test') {
        agent {
          kubernetes {
            yamlFile 'nodejs-pod.yaml'
          }
        }
        steps {
          container('nodejs') {
            echo 'Hello World!'   
            sh 'node --version'
          }
        }
      }
      stage('Deploy') {
        when {
          beforeAgent true
          branch 'main'
        }
        steps {
          echo "TODO - deploy"
        }
      }
    }
  }
  ```

3. Commit the changes directly to your `add-jenkinsfile` branch and then navigate to the **insurance-frontend** job on your Managed Controller and the job for the **add-jenkinsfile** branch should be running or queued to run. Note that the ***Deploy*** `stage` was skipped. ![Conditional Stage Skipped](conditional-skipped-stage.png?width=50pc) 
4. Now we will create a [Pull Request](https://help.github.com/en/articles/creating-a-pull-request) between the **add-jenkinsfile** branch and **main** branch of your **insurance-frontend** repository. Navigate to your **insurance-frontend** repository in GitHub, make sure you are on the `add-jenkinsfile` branch. Click on the **Compare & pull request** button at the top; if you don't see that then click the **Contribute** link and then click the **Open pull request** button. ![Create Pull request link](create-pr-link.png?width=50pc) 
5. Make sure that the **base** branch is the **main** branch of your **insurance-frontend** repository and that the **compare** branch is the **add-jenkinsfile** branch, add a comment and then click the **Create pull request** button. ![Create Pull request](create-pr.png?width=50pc) 
6. A job will be created for the pull request and once it has completed you will notice that it cannot be merged because the required ***stage/Pull Request/Build and Push Container Image*** check has not passed and that check is required before you can merge to the `main` branch.

{{% notice tip %}}
We have configured your copy of the **insurance-frontend** repository with [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging). This allows integrating with [checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) provided by CloudBees CI, to include the requirement that certain pipeline stages complete successfully before GitHub will allow for a pull request to be merged to the protected branch - in this case, the `main` branch. In addition to using pipeline `stages` as checks, you may also use a number of checks provided by the [Warnings NG plugin](https://github.com/jenkinsci/warnings-ng-plugin/blob/master/doc/Documentation.md).
{{% /notice %}}

{{% notice note %}}
A Jenkins Pipeline job was automatically created for the pull request (which is really just a special type of GitHub branch) by the Multibranch Pipeline project when the `Jenkisfile` was added to that branch and the **add-jenkinsfile** branch job was removed as it really is just a duplicate of the **PR** job.
{{% /notice %}}

## Using the When Directive with Nested Stages

In this lab we will learn how you can combine nested `stages` with the `when` directive so that you don't have repeat a `when` condition for every `stage` it applies. We will also add a set of pull request specific stages to include the **Build and Push Container Image** stage that is a required status check for merging pull requests to the `main` branch of you **insurance-frontend** repository.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **insurance-frontend** repository.

{{% notice tip %}}
You may also edit files in GitHub from the **Files changed** tab of the pull request view.
{{% /notice %}}

2. Replace the entire pipeline with the following:
```
pipeline {
  agent none
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          agent {
            kubernetes {
              yamlFile 'nodejs-pod.yaml'
            }
          }
          steps {
            container('nodejs') {
              echo 'Hello World!'   
              sh 'node --version'
            }
          }
        }
      }
    }
    stage('Main Branch Stages') {
      when {
        beforeAgent true
        branch 'main'
      }
      stages {
        stage('Push Image to Prod Registry') {
          steps {
            echo "TODO - push image"
          }
        }
        stage('Deploy') {
          steps {
            echo "TODO - deploy"
          }
        }
      }
    }
  }
}
```

By wrapping the ***Push Image to Prod Registry*** and ***Deploy*** `stages` in the ***Main Branch Stages***, the `when` directive for the `main` branch only has to be specified once. We are also using the `pr-*`wildcard `branch` `when` condition so the nested ***Build and Push Container Image*** and ***Test*** `stages` will be executed for all pull request branches but not for any other branch. Once we build and test a container image, there is no reason we can't use it when the pull request is merged to the `main` branch.

3. Commit the changes directly to the `add-jenkinsfile` branch and navigate back to the **Conversation** tab of the **Add jenkinsfile** pull request. Once the required ***stage/Pull Request/Build and Push Container Image*** stage has completed, click the **Merge pull request** button and **Confirm merge** button. ![Finished required check](finished-required-check.png?width=50pc)
4. Navigate to the **insurance-frontend** job on your managed controller. The job for the **main** branch should be running or queued to run. Once the run completes you will see that the nested ***Build and Push Container Image*** and ***Test*** `stages` will be skipped but the **Main Branch Stages** were not. ![Conditional Nested Stage](conditional-nested-stage.png?width=50pc) 

{{% notice tip %}}
In addition to using GitHub branch protection to protect the `main` branch, we have also configured your copy of the **insurance-frontend** repository to automatically delete branches after they are merged into the `main` branch. This allows us to reduce the possibility of long-lived branches in the repository.
{{% /notice %}}

## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **main** branch of your copy of the **insurance-frontend** repository matches the one from below:

### Finished Jenkinsfile for *Conditional Execution using the `when` directive* lab
```groovy
pipeline {
  agent none
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          agent {
            kubernetes {
              yamlFile 'nodejs-pod.yaml'
            }
          }
          steps {
            container('nodejs') {
              echo 'Hello World!'   
              sh 'node --version'
            }
          }
        }
      }
    }
    stage('Main Branch Stages') {
      when {
        beforeAgent true
        branch 'main'
      }
      stages {
        stage('Push Image to Prod Registry') {
          steps {
            echo "TODO - push image"
          }
        }
        stage('Deploy') {
          steps {
            echo "TODO - deploy"
          }
        }
      }
    }
  }
}
```
