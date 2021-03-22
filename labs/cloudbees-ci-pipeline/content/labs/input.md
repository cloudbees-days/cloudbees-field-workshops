---
title: "Pipelines with Interactive Input"
chapter: false
weight: 7
--- 

In this lab, we will see how you can capture interactive input in your Jenkins Pipeline while it is running by using the `input` step and some pitfalls you will want to avoid when using the `input` step.

1. Use the GitHub file editor to update the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository and update the **Deploy** `stage` by adding the following between `environment` directive and `steps` block:

```
          when {
            environment name: 'FAVORITE_COLOR', value: 'BLUE'
          }
          input {
            message "Should we continue with deployment?"
          }
```

Note that we added a new `when` condition that will result in the **Deploy** stage being skipped. We also added an `input` directive instead of an `input` step in the `steps` block. This ensures that the `input` will be displayed before the agent is used. *Also note that even though we are setting the `FAVORITE_COLOR` environment variable value to `BLUE` in the **Deploy** stage that does not get executed until after the `when` condition is checked; so the value is still `RED` for the `when` condition.* 

2. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller.
3. There will be an `input` prompt for the `Deploy` stage (*the `input` prompt is also available in the Console log*). ![Configure Notification Link](input-prompt.png?width=50pc) Go ahead and click the **Proceed** button and you will see that the **Deploy** stage is skipped. 
4. Return to the the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository in GitHub and use the GitHub file editor to update the **Deploy** `stage` by adding a special [beforeInput](https://www.jenkins.io/doc/book/pipeline/syntax/#evaluating-when-before-the-input-directive) `when` condition set to `true` after the `environment` condition. The updated `when` directive should match the following:
```
          when {
            environment name: 'FAVORITE_COLOR', value: 'BLUE'
            beforeInput true
          }
```

5. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller. The **Deploy** stage will be skipped before prompting for input.
6. Return to the the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository in GitHub and use the GitHub file editor to update the **Deploy** `stage`. Replace the entire **Deploy** stage with the following:
```
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
```

7. Commit the changes, navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller and you will eventually see a `input` prompt for the `Deploy` stage.
8. If you don't click on either the **Proceed** or **Abort** button in the `input` prompt, the Managed Controller would have waited indefinitely for a user response. Let's fix that by setting a timeout for the **Deploy** stage. We will add a `timeout` `option` for the **Deploy** `stage` using the [stage options directive](https://jenkins.io/doc/book/pipeline/syntax/#stage-options). Update the **Deploy** `stage` to match the following in the **main** branch and then commit the changes:

```
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          options {
            timeout(time: 30, unit: 'SECONDS') 
          }
          input {
            message "Should we continue with deployment?"
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
```

9. Navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller and wait at least 30 seconds after the 'Deploy' `stage` starts. Your pipeline will be automatically **aborted** 30 seconds after the 'Deploy' `stage` starts. ![Input Timeout](input-timeout.png?width=50pc)

### Finished Jenkinsfile for *Pipeline Approvals with Interactive Input* Lab
```
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }  
  triggers {
    eventTrigger simpleMatch('hello-api-deploy-event')
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
            timeout(time: 30, unit: 'SECONDS') 
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
