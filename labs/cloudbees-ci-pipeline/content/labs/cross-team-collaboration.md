---
title: "CloudBees Cross Team Collaboration"
chapter: false
weight: 6
--- 

In this lab we will explore the [CloudBees CI Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration). Cross Team Collaboration simplifies the cumbersome and complicated tasks of triggering downstream jobs by eliminating the need to identify and maintain the full path for every downstream job. Simply put, this proprietary CloudBees CI feature connects pipelines, increasing automation and collaboration. Prior to this feature, the details of every downstream job (Jenkins instance ID, full job name, Git branch name) all had to be meticulously specified in the upstream job. If the job name changed, the upstream job had to be refactored, creating a maintenance burden and discouraging the adoption of event-based triggers.

## Cross Team Collaboration Events

The [Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration) is designed to greatly improve team collaboration by connecting team Pipelines to deliver software faster. It essentially allows a Pipeline to create a notification event which will be consumed by other Pipelines waiting on it. It consists of a **[Publishing Event](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-publishers)** and a **[Trigger Condition](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-triggers)**.

The Cross Team Collaboration feature has a configurable router for routing events and it needs to be configured on your Managed Controllers before you will be able to receive the event published by another Managed Controller. Once again, CasC was used to pre-configure this for everyone, but you can still review the configuration by going to the top-level of your Managed Controller and click on the **Manage Jenkins** left menu link and then click on **Configure Notification**. ![Configure Notification Link](config-notification-link.png?width=50pc)

 You should see the following configuration: ![Notification Configuration](notification-config.png?width=50pc)


1. To use Cross Team Collaboration we will need to update the **helloworld-nodejs** Jenkinsfile to listen for a notification event to be published by the upstream, or publishing, job. We will do that by adding a [`trigger` directive](https://www.jenkins.io/doc/book/pipeline/syntax/#triggers) to your **Jenkinsfile** Pipeline script.
2. Open the GitHub editor for the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository.
3. Add the following `trigger` directive just above the top-level `stages` block:

```groovy
  triggers {
    eventTrigger simpleMatch('hello-api-deploy-event')
  }
```

4. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** project on your Managed Controller and view the configuration for that job by click the **View Configuration** link on the **Branch main** job page. ![View Configuration Link](view-config-link.png?width=50pc)
5. Click on the **Build Triggers** tab on the job configuration page for the **main** branch job and you will the **Build whenever the specified event is seen** trigger is checked and configured with a **Simple Event**. ![View Configuration Link](event-trigger-config.png?width=50pc)

{{% notice note %}}
After first adding a new `trigger` you must run the job at least once so that the `trigger` is saved to the Jenkins job configuration (similar to setting the `buildDiscarder` `option`).
{{% /notice %}}

6. Next, your instructor will set up a Pipeline project with the following **[simple event](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-types)**: 

```
publishEvent simpleEvent('hello-api-deploy-event')
```

The entire Jenkins Pipeline containing the publishing event:
```
pipeline {
  agent none
  stages {
    stage('Build') {
      steps {
        echo 'build'
      }
    }
    stage('Deploy') {
      steps {
        echo 'deploy'
        publishEvent simpleEvent('hello-api-deploy-event')
      }
    }
  }
}
```

That event will be published **across all Managed Controllers in the Workshop cluster** via the CloudBees CI Cloud Operations Center event router triggering everyones' **helloworld-nodejs** Pipelines to run. 

7. Now, once that change is committed, and the **helloworld-api** job runs, everyone will see the **main** branch of their **helloworld-nodejs** job triggered by the `hello-api-deploy-event` simple event. ![View Configuration Link](triggered-by-event.png?width=50pc)


## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **main** branch of your forked **helloworld-nodejs** repository matches the one from [below](#finished-jenkinsfile-for-pipeline-pod-templates-and-cross-team-collaboration).

### Finished Jenkinsfile for *Pipeline Pod Templates and Cross Team Collaboration* Lab
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
          steps {
            sh 'echo TODO - deploy to $FAVORITE_COLOR with SERVICE_CREDS: username=$SERVICE_CREDS_USR password=$SERVICE_CREDS_PSW'
          }
        }
      }
    }
  }
}
```
