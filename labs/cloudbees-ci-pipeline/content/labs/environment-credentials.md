---
title: "Environment Variables and Credentials"
chapter: false
weight: 5
--- 

The Declarative Pipeline syntax provides an [environment directive](https://www.jenkins.io/doc/book/pipeline/syntax/#environment) that allows specifying key-value pairs at the global Pipeline or `stage` level. In addition to providing environment variables, the `environment` directive also [integrates with Jenkins credentials](https://www.jenkins.io/doc/book/pipeline/syntax/#supported-credentials-type) to provide a simpler way of securely injecting credentials into your Jenkins Pipeline. In this lab we will explore both types of Pipeline environment variables.

## Global and Stage Pipeline Environment Variables

1. We will add a global environment variable that will be accessible by all the stages of our Jenkins Pipeline. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **development** branch of your **helloworld-nodejs** repository.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
2. First we will update the `development` branch Jenksinfile to match the `main` branch Jenkinsfile by replacing the entire `development` branch Jenksinfile with the following:
```
pipeline {
  agent none
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
          echo 'Hello World!'   
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
            echo "TODO - build and push image"
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

3. Next, at the global `pipeline` level, add the following `environment` block under the `agent none` directive:
```
  environment {
    DEPLOYMENT_ENVIRONMENT = 'PREVIEW'
  }
```

3. Next, we will override the `DEPLOYMENT_ENVIRONMENT` variable.
3. At the bottom of the screen enter a commit message, leave **Commit directly to the `main` branch** selected and click the **Commit new file** button.
4. 

