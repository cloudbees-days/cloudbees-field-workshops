---
title: "Environment Variables and Credentials"
chapter: false
weight: 5
--- 

The Declarative Pipeline syntax provides an [environment directive](https://www.jenkins.io/doc/book/pipeline/syntax/#environment) that allows specifying key-value pairs at the global Pipeline or `stage` level. In addition to providing environment variables, the `environment` directive also [integrates with Jenkins credentials](https://www.jenkins.io/doc/book/pipeline/syntax/#supported-credentials-type) to provide a simpler way of securely injecting credentials into your Jenkins Pipeline. In this lab we will explore both types of Pipeline environment variables.

## Global and Stage Pipeline Environment Variables

1. We will add a global environment variable that will be accessible by all the stages of our Jenkins Pipeline. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **helloworld-nodejs** repository.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
2. Next, at the global `pipeline` level, add the following `environment` block under the `agent none` directive:
```
  environment {
    FAVORITE_COLOR = 'RED'
  }
```
3. Add the following `echo` step right before the existing `echo` step in the **Build and Push Image** stage.
```
          echo "FAVORITE_COLOR is $FAVORITE_COLOR"
```

5. Next, we will override the `FAVORITE_COLOR` variable for the **Deploy** stage and add an `echo` step. Replace the entire **Deploy** stage with the following:
```
        stage('Deploy') {
          environment {
            FAVORITE_COLOR = 'BLUE'
          }
          steps {
            echo "TODO - deploy to $FAVORITE_COLOR"
          }
        }
```

The complete Pipeline should match the following:
```
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
          environment {
            FAVORITE_COLOR = 'BLUE'
          }
          steps {
            echo "TODO - deploy to $FAVORITE_COLOR"
          }
        }
      }
    }
  }
}
```

6. At the bottom of the screen enter a commit message, leave **Commit directly to the `main` branch** selected and click the **Commit new file** button.
7. Navigate to the **main** branch job of the **helloworld-nodejs** project on your Managed Controller and the job should be running or queued to run. Once it completes you should see the value for the **FAVORITE_COLOR** variable printed out in the logs and it should have a different value. ![Variable in Test Stage](favorite-color-red-or-blue.png?width=50pc) 


## Credentials as Environment Variables

In this lab we will use the `environment` directive to inject a username/password credential into your Jenkins Pipeline. We will also explore some best practices around injecting sensitive environmental variables into a Jenkins Pipeline.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **helloworld-nodejs** repository and click the pencil icon to edit the file.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
2. We will add another environment variable to the `environment` directive of the **Deploy** stage, but this time we will use the special helper method `credentials()` to create an environment variable from a username/password credential and we will then update the `echo` step to print out the values of the variable. Replace the entire **Deploy** stage with the following:
```
        stage('Deploy') {
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            echo "TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW"
          }
        }
```

{{% notice note %}}
Note that the `credentials` helper automatically creates two environment variables use the variable name we provided as a prefix and add `_USR` for the credential username and `_PSW` for the credential password. The credential variable without either suffix will provide the value in the format `username:password`.
{{% /notice %}}

3. At the bottom of the screen enter a commit message, leave **Commit directly to the `main` branch** selected and click the **Commit new file** button.
4. Navigate to the **main** branch job of the **helloworld-nodejs** project on your Managed Controller and the job should be running or queued to run. Once it completes, review the logs for the **Deploy** stage. ![Deploy Stage Logs with Secret Warning](deploy-logs-secret-warning.png?width=50pc) 

{{% notice note %}}
There is a warning regarding *Groovy String interpolation* for the **SERVICE_CREDS** environment variable. This is referring to the fact that the the sensitive environment variable will be interpolated during Groovy evaluation and the value could be made available earlier than intended, resulting in sensitive data leaking in various contexts.
{{% /notice %}}

5. To fix this, navigate back to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **helloworld-nodejs** repository.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
6. We will update the `echo` step of the **Deploy** stage so it does not use Groovy String interpolation to inject the username/password credential. Replace the entire **Deploy** stage with the following:
```
        stage('Deploy') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
```

We were able to remove Groovy String interpolation on the controller by replacing the `echo` step with an `sh` step that executes **echo** on the agent and replacing the double-quotes with single-quotes so there is no Groovy String interpolation - the pipeline environment variable is used as an environment variable on the agent. We also had to add an `agent` because the `sh` step requires an agent to run on.

7. At the bottom of the screen enter a commit message, leave **Commit directly to the `main` branch** selected and click the **Commit new file** button.
8. Navigate to the **main** branch job of the **helloworld-nodejs** project on your Managed Controller and the job should be running or queued to run. Once it completes, review the logs for the **Deploy** stage. ![Deploy Stage Logs No Secret Warning](deploy-logs-no-secret-warning.png?width=50pc) 

There should no longer be a warning regarding *Groovy String interpolation*.

{{% notice tip %}}
By default warnings are configured to be displayed on the build and log pages when there might be insecure interpolation. To configure these warnings set `org.jenkinsci.plugins.workflow.cps.DSL.UNSAFE_GROOVY_INTERPOLATION` to the following values: 
>1) `ignore`: no warnings will be displayed on the log or build page. 
>2) `fail`: build failure when the build encounters the first interpolated groovy string that contains a secret.
{{% /notice %}}

### Finished Jenkinsfile for the *Environment Variables and Credentials* Lab
```
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
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
      }
    }
  }
}
```
