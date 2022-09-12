---
title: "Environment Variables and Credentials"
chapter: false
weight: 5
--- 

The Declarative Pipeline syntax provides an [environment directive](https://www.jenkins.io/doc/book/pipeline/syntax/#environment) that allows specifying key-value pairs at the Pipeline global or `stage` level. In addition to providing environment variables, the `environment` directive also [integrates with Jenkins credentials](https://www.jenkins.io/doc/book/pipeline/syntax/#supported-credentials-type) to provide a simpler way of securely injecting credentials into your Jenkins Pipeline. In this lab we will explore both types of Declarative Pipeline environment variables.

## Global and Stage Pipeline Environment Variables

1. We will add a global environment variable that will be accessible by all the `stages` of the Jenkins Pipeline. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the **main** branch of your **insurance-frontend** repository.  ![Edit Jenkinsfile](edit-jenksinfile.png?width=50pc) 
2. Next, at the global `pipeline` level, add the following `environment` block under the `agent none` directive:
```groovy
  environment {
    FAVORITE_COLOR = 'RED'
  }
```
3. Add the following `echo` step right before the existing `echo` step in the **Build and Push Container Image** stage.
```
          echo "FAVORITE_COLOR is $FAVORITE_COLOR"
```

5. Next, we will override the `FAVORITE_COLOR` variable for the **Test** stage and add an `echo` step. Replace the entire **Test** stage with the following:
```groovy
        stage('Test') {
          environment {
            FAVORITE_COLOR = 'BLUE'
          }
          steps {
            echo "TODO - test $FAVORITE_COLOR"
          }
        }
```

The updated Pipeline should match the following:
```groovy
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          environment {
            FAVORITE_COLOR = 'BLUE'
          }
          steps {
            echo "TODO - test $FAVORITE_COLOR"
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

6. At the bottom of the screen enter a commit message, rename the new branch **add-env-var** and click the **Propose changes** button. 
7. On the next screen, click the **Create pull request** button.
8. Navigate to the active **Pull Requests** job of the **insurance-frontend** project on your managed controller. The job should be running or queued to run. Once it completes you should see the value for the **FAVORITE_COLOR** variable printed out in the logs twice - with a value of **red** for the **Build and Push Container Image** `stage` and the with a value of **blue** for the **Test** `stage`.


## Credentials as Environment Variables

In this lab we will use the `environment` directive to inject a username/password credential into your Jenkins Pipeline. We will also explore the enforcement of some best practices around injecting sensitive environmental variables into a Jenkins Pipeline.

{{% notice note %}}
You may also use the `withCredentials` block directive to inject Jenkins credentials into a pipeline job. It works the same way as the `credentials()` helper we use below, but is much more verbose.
{{% /notice %}}

1. Navigate to and open the GitHub editor for the `Jenkinsfile` file in the `add-env-vars` branch of your **insurance-frontend** repository and click the pencil icon to edit the file.
2. We will add another environment variable to the `environment` directive of the **Test** stage, but this time we will use the special helper method `credentials()` to create an environment variable from a username/password credential and we will then update the `echo` step to print out the values of the variable. Replace the entire **Test** stage with the following:
```groovy
        stage('Test') {
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            echo "TODO - test $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW"
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
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            echo "TODO - test $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW"
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
{{% /expand%}}

{{% notice tip %}}
The `credentials` helper automatically creates two environment variables use the variable name we provided as a prefix and appends `_USR` for the credential username and `_PSW` for the credential password. The credential variable without either suffix will provide the value in the format `username:password`.
{{% /notice %}}

3. At the bottom of the screen enter a commit message, leave **Commit directly to the `add-env-vars` branch** selected and click the **Commit new file** button.
4. Navigate to the active **Pull Requests** job of the **insurance-frontend** project on your managed controller. The job should be running or queued to run. Once it completes, review the **Console Output** and you should see the following error:

```log
[Pipeline] End of Pipeline
ERROR: Error: A secret was passed to "echo" using Groovy String interpolation, which is insecure.
		 Affected argument(s) used the following variable(s): [SERVICE_CREDS_PSW]
		 See https://jenkins.io/redirect/groovy-string-interpolation for details.

GitHub has been notified of this commit’s build result

Policies were not applied to this pipeline
Finished: FAILURE
```

{{% notice note %}}
There is an error regarding *Groovy String interpolation* for the **SERVICE_CREDS** environment variable. This is referring to the fact that the the sensitive environment variable will be interpolated during Groovy evaluation and the value could be made available earlier than intended, resulting in sensitive data leaking in various contexts.
{{% /notice %}}

5. To fix this insecure syntax, navigate back to and open the GitHub editor for the `Jenkinsfile` file in the `add-env-vars` branch of your **insurance-frontend** repository.
6. We will update the `echo` step of the **Test** stage so it does not use Groovy String interpolation to inject the username/password credential variables. Replace the entire **Test** stage with the following:
```groovy
        stage('Test') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            sh 'echo TODO - test $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
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
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            sh 'echo TODO - test $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
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
{{% /expand%}}

We were able to remove Groovy String interpolation on the controller by replacing the `echo` step with an `sh` step that executes **echo** on the agent and replacing the double-quotes with single-quotes so there is no Groovy String interpolation - the pipeline environment variable is used as an environment variable on the agent and is therefore not accessible by any Groovy scripting in the Pipeline. We also had to add an `agent` to the **Test** `stage` because the `sh` step requires an agent (it requires a [non flyweight executor also referred to as a heavyweight executor](https://support.cloudbees.com/hc/en-us/articles/360012808951-Pipeline-Difference-between-flyweight-and-heavyweight-Executors)).

7. At the bottom of the screen enter a commit message, leave **Commit directly to the `add-env-vars` branch** selected and click the **Commit new file** button.
8. Navigate to the active **Pull Requests** job of the **insurance-frontend** project on your managed controller. The job should be running or queued to run. Once it completes, review the logs for the **Test** stage. ![Test Stage Logs No Secret Warning](test-logs-no-secret-warning.png?width=50pc) 

There should no longer be an error regarding *Groovy String interpolation*.

{{% notice tip %}}
By default, the use of unsafe Groovy string interpolation in a Jenkins pipeline will result in a warning. However, we have configured your controller with a system property to override the default warning and to fail any job that uses unsafe Groovy interpolation. To configure these warnings set `org.jenkinsci.plugins.workflow.cps.DSL.UNSAFE_GROOVY_INTERPOLATION` to one of the following values: 
  1) `ignore`: no warnings will be displayed on the log or build page. 
  2) `fail`: build failure when the build encounters the first interpolated groovy string that contains a secret.
{{% /notice %}}

### Finished Jenkinsfile for the *Environment Variables and Credentials* Lab
```groovy
pipeline {
  agent none
  environment {
    FAVORITE_COLOR = 'RED'
  }
  stages {
    stage('Pull Request') {
      when {
        beforeAgent true
        branch 'pr-*'
      }
      stages {
        stage('Build and Push Container Image') {
          steps {
            echo "FAVORITE_COLOR is $FAVORITE_COLOR"
            echo "TODO - Build and Push Container Image"
          }
        }
        stage('Test') {
          agent any
          environment {
            FAVORITE_COLOR = 'BLUE'
            SERVICE_CREDS = credentials('example-service-username-password')
          }
          steps {
            sh 'echo TODO - test $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
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
