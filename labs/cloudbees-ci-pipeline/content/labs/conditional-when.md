---
title: "Conditional Execution Using the when Directive"
chapter: false
weight: 4
--- 

## Conditional Stages Using the When Directive

In this lab we will edit the `Jenkinsfile` file in your **insurance-frontend** repository with conditional execution using the [when directive](https://jenkins.io/doc/book/pipeline/syntax/#when). We will accomplish this by adding a branch specific `stage` to the `Jenkinsfile` in your **insurance-frontend** repository.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **development** branch of your **insurance-frontend** repository.
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

3. Commit the changes directly to your `development` branch and then navigate to the **insurance-frontend** job on your Managed Controller and the job for the **development** branch should be running or queued to run. Note that the ***Deploy*** `stage` was skipped. ![Conditional Stage Skipped](conditional-skipped-stage.png?width=50pc) 
4. Now we will create a [Pull Request](https://help.github.com/en/articles/creating-a-pull-request) between the **development** branch and **main** branch of your **insurance-frontend** repository. Navigate to your **insurance-frontend** repository in GitHub, make sure you are on the `development` branch. Click on the **Compare & pull request** button at the top; if you don't see that then click the **Contribute** link and then click the **Open pull request** button. ![Create Pull request link](create-pr-link.png?width=50pc) 
5. Make sure that the **base repository** is the **main** branch of your **insurance-frontend** repository, add a comment and then click the **Create pull request** button. ![Create Pull request](create-pr.png?width=50pc) 
6. A job will be created for the pull request and once it has completed successfully your pull request will show that **All checks have passed**. Go ahead and click the **Merge pull request** button and then click the **Confirm merge** button.

![Merge Pull request](merge-pr.png?width=50pc)

7. Navigate to the **insurance-frontend** job on your CloudBees CI Managed Controller and the job for the **main** branch should be running or queued to run. Click on the run and after it has completed notice that the ***Deploy*** stage was not skipped. ![Stage Not Skipped](stage-not-skipped.png?width=50pc)

{{% notice note %}}
A Jenkins Pipeline job was automatically created for the pull request (which is really just a special type of GitHub branch) and the `main` branch by the Multibranch Pipeline project when the `Jenkisfile` was added to those branches.
{{% /notice %}}

## Using the When Directive with Nested Stages

In this lab we will learn how you can combine nested `stages` with the `when` directive so that you don't have repeat a `when` condition for every `stage` it applies. We will also update the ***Test*** `stage` so it will only execute when the condition is false.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **insurance-frontend** repository.
2. Replace the entire pipeline with the following:
```
pipeline {
  agent none
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'PR-*'
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

By wrapping the ***Push Image to Prod Registry*** and ***Deploy*** `stages` in the ***Main Branch Stages***, the `when` directive for the `main` branch only has to be specified once. Also, by using the `not` `when` condition, the nested ***Build and Push Container Image*** and ***Test*** `stages` will only be executed when the branch being processed is **not** the `main` branch.

3. Click the **Propose changes** button and on the next screen click the **Create Pull Request** button. Once the required ***stage/Build and Push Container Image*** stage has completed, click the **Merge pull request** button and **Confirm merge** button. 
4. Navigate to the **insurance-frontend** job on your managed controller. The job for the **main** branch should be running or queued to run. Once the run completes you will see that the nested ***Build and Push Container Image*** and ***Test*** `stages` will be skipped but the **Main Branch Stages** were not. ![Conditional Nested Stage](conditional-nested-stage.png?width=50pc) 

## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **main** branch of your copy of the **insurance-frontend** repository matches the one from below:

### Finished Jenkinsfile for *Conditional Execution using the `when` directive* lab
```
pipeline {
  agent none
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'PR-*'
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
