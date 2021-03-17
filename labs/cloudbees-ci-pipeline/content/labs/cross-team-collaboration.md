---
title: "CloudBees Cross Team Collaboration"
chapter: false
weight: 6
--- 

In this lab we will explore the [CloudBees Core Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration). Cross Team Collaboration simplifies the cumbersome and complicated tasks of triggering downstream jobs by eliminating the need to identify and maintain the full path for every downstream job. Simply put it, this proprietary feature connects pipelines, increasing automation and collaboration. Prior to this feature, the details of every downstream job (Jenkins instance ID, full job name, Git branch name) all had to be meticulously specified in the upstream job. If the job name changed, the upstream job had to be refactored, creating a maintenance burden and discouraging the adoption of event-based triggers.

## Cross Team Collaboration Events

The [Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration) is designed to greatly improve team collaboration by connecting team Pipelines to deliver software faster. It essentially allows a Pipeline to create a notification event which will be consumed by other Pipelines waiting on it. It consists of a [**Publishing Event**](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-publishers) and a [**Trigger Condition**](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-triggers).

The Cross Team Collaboration feature has a configurable router for routing events and it needs to be configured on your Managed Controllers before you will be able to receive the event published by another Managed Controller. Once again, CasC was used to pre-configure this for everyone, but you can still review the configuration by going to the top-level of your Managed Controller in the classic UI andclicking on **Manage Jenkins** and then click on **Configure Notification**. ![Configure Notification Link](config-notification-link.png?width=50pc)

 You should see the following configuration: ![Notification Configuration](notification-config.png?width=50pc)


1. Now our pipeline must must be updated to listen for a notification event to be published by the upstream job. We will do that by adding a `trigger` to your **Jenkinsfile** Pipeline script.
2. Open the GitHub editor for the **Jenkinsfile** file in the **main** branch of your copy of the **helloworld-nodejs** repository.
3. Add the following `trigger` block just above the top-level `stages` block:

```groovy
  triggers {
    eventTrigger simpleMatch('hello-api-deploy-event')
  }
```

4. Commit the changes and then navigate to the **main** branch of your **helloworld-nodejs** job on your Managed Controller and view the c. 

>**NOTE:**After first adding a new `trigger` you must run the job at least once so that the `trigger` is saved to the Jenkins job configuration (similar to what was necessary for the `buildDiscarder` `option` earlier). <p><img src="img/cross-team/cross_team_trigger_configured.png" width=850/>

Next, your instructor will set up a Multibranch Pipeline project for the https://github.com/cloudbees-days/helloworld-api repository and add the following [simple event](https://go.cloudbees.com/docs/cloudbees-core/cloud-admin-guide/cross-team-collaboration/#cross-team-event-types) to the **Deploy** stage of the **helloworld-api** `Jenkinsfile` : 

```
publishEvent simpleEvent('hello-api-deploy-event')
```

That event will be published **across all Managed Controllers in the Workshop cluster** via the CloudBees Operations Center event router triggering everyones' **helloworld-nodejs** Pipelines to run. 

Now, once that change is committed, and the **helloworld-api** job runs, everyone will see the **main** branch of their **helloworld-nodejs** job triggered. <p><img src="img/cross-team/cross_team_triggered_by_event.png" width=850/>


## Next Lesson

Before moving on to the next lesson make sure that your **Jenkinsfile** Pipeline script on the **main** branch of your forked **helloworld-nodejs** repository matches the one from [below](#finished-jenkinsfile-for-pipeline-pod-templates-and-cross-team-collaboration).

### Finished Jenkinsfile for *Pipeline Pod Templates and Cross Team Collaboration*
```
pipeline {
  agent none
  options { 
    buildDiscarder(logRotator(numToKeepStr: '2'))
    skipDefaultCheckout true
  }
  triggers {
    eventTrigger simpleMatch('hello-api-deploy-event')
  }
  stages {
    stage('Test') {
      agent {
        kubernetes {
          label 'nodejs-app-pod'
          yamlFile 'nodejs-pod.yaml'
        }
      }
      steps {
        checkout scm
        container('nodejs') {
          echo 'Hello World!'   
          sh 'node --version'
        }
      }
    }
    stage('Build and Push Image') {
      when {
        beforeAgent true
        branch 'main'
      }
      steps {
        echo "TODO - build and push image"
      }
    }
  }
}
```
