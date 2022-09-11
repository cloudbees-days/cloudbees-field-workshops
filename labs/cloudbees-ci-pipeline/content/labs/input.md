---
title: "Declarative Pipelines with Interactive Input"
chapter: false
weight: 6
--- 

In this lab, we will see how you can capture interactive input in your Jenkins Pipeline while it is running by using the [input directive](https://www.jenkins.io/doc/book/pipeline/syntax/#input) and we will explore some pitfalls you will want to avoid when using the `input` directive.

1. Use the GitHub file editor to update the **Jenkinsfile** file in the **main** branch of your copy of the **insurance-frontend** repository and update the **Deploy** `stage` by adding the following between `environment` directive and `steps` block:

```
          input {
            message "Should we continue with deployment?"
          }
```

{{%expand "expand for complete updated Jenkinsfile" %}}
```groovy
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }
  stages {
    stage('Test') {
      when {
        beforeAgent true
        not { branch 'main' }
      }
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        container('nodejs') { 
          sh 'node --version'
        }
      }
    }
    stage('Main Branch Stages') {
      when {
        beforeAgent true
        branch 'main'
      }
      stages {
        stage('Build and Push Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"  
            echo "TODO - build and push image"
          }
        }
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }          
          input {
            message "Should we continue with deployment?"
          }
          
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
      }
    }
  }
}
```
{{% /expand%}}

{{% notice note %}}
We added an `input` directive instead of an `input` step in the `steps` block. This ensures that the `input` will prompt a user for input before the agent is used.
{{% /notice %}}

2. Commit the changes and then navigate to the **main** branch of your **insurance-frontend** project on your Managed Controller.
3. There will be an `input` prompt for the `Deploy` stage (*the `input` prompt is also available in the Console log*). ![Configure Notification Link](input-prompt.png?width=50pc) Go ahead and click the **Proceed** button and an agent will be provisioned and the `Deploy` stage will run.
4. If you don't click on either the **Proceed** or **Abort** button in the `input` prompt, the job would have waited indefinitely for an `input` response. Let's fix that by setting a timeout for the **Deploy** stage. We will add a `timeout` `option` for the **Deploy** `stage` using the [stage options directive](https://jenkins.io/doc/book/pipeline/syntax/#stage-options) (we will also remove the `when` block). Update the **Deploy** `stage` to match the following in the **main** branch and then commit the changes:

```groovy
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          options {
            timeout(time: 10, unit: 'SECONDS') 
          }
          input {
            message "Should we continue with deployment?"
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
```

{{%expand "expand for complete updated Jenkinsfile" %}}
```groovy
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }
  stages {
    stage('Test') {
      when {
        beforeAgent true
        not { branch 'main' }
      }
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        container('nodejs') { 
          sh 'node --version'
        }
      }
    }
    stage('Main Branch Stages') {
      when {
        beforeAgent true
        branch 'main'
      }
      stages {
        stage('Build and Push Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"  
            echo "TODO - build and push image"
          }
        }
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }          
          options {
            timeout(time: 10, unit: 'SECONDS') 
          }
          input {
            message "Should we continue with deployment?"
          }
          
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
      }
    }
  }
}
```
{{% /expand%}}

5. Navigate to the **main** branch of your **insurance-frontend** project on your Managed Controller and wait a little more than 10 seconds after the 'Deploy' `stage` starts. Your pipeline will be automatically **aborted** 10 seconds after the 'Deploy' `stage` starts. ![Input Timeout](input-timeout.png?width=50pc)

### Finished Jenkinsfile for *Declarative Pipelines with Interactive Input* Lab
```groovy
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }  
  stages {
    stage('Test') {
      when {
        beforeAgent true
        not { branch 'main' }
      }
      agent {
        kubernetes {
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        container('nodejs') { 
          sh 'node --version'
        }
      }
    }
    stage('Main Branch Stages') {
      when {
        beforeAgent true
        branch 'main'
      }
      stages {
        stage('Build and Push Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"  
            echo "TODO - build and push image"
          }
        }
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          options {
            timeout(time: 10, unit: 'SECONDS') 
          }
          input {
            message "Should we continue with deployment?"
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
      }
    }
  }
}
```
