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
3. Add the following `echo` righ before the existing `echo` step in the **Build and Push Image** stage.
```
          echo "FAVORITE_COLOR is $FAVORITE_COLOR"
```

5. Next, we will override the `FAVORITE_COLOR` variable for the **Deploy** stage and adding an `echo` step. Replace the entire **Deploy** stage with the following:
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

In this lab we will use the `environment` directive to inject a username/password credential into are Jenkins Pipeline. We will also explore some best practices around injecting sensitive envrionmental variables into a Jenkins Pipeline.

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **helloworld-nodejs** repository.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
2. We will add another environment variable to the `environment` directive of the **Deploy** stage, but this time we will use the special helper method `credentials()` to create an environment variable from a username/password credential and we will then update the `echo` step to print out the values of the variable. Replace the entire **Deploy** stage with the following:
```
        stage('Deploy') {
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            echo "TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS = $SERVICE_CREDS"
          }
        }
```

3. At the bottom of the screen enter a commit message, leave **Commit directly to the `main` branch** selected and click the **Commit new file** button.
4. Navigate to the **main** branch job of the **helloworld-nodejs** project on your Managed Controller and the job should be running or queued to run. Once it completes, review the logs for the **Deploy** stage. ![Deploy Stage Logs with Secret Warning](deploy-logs-secret-warning.png?width=50pc) 
Note that there is a warning regarding *Groovy String interpolation* for the **SERVICE_CREDS** environment variable. 
5. 

