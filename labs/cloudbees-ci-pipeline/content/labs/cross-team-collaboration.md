---
title: "CloudBees Cross Team Collaboration"
chapter: false
weight: 8
--- 

In this lab we will explore the [CloudBees CI Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration). Cross Team Collaboration simplifies the cumbersome and complicated tasks of triggering downstream jobs by eliminating the need to identify and maintain the full path for every downstream job. Simply put, this proprietary CloudBees CI feature connects pipelines, increasing automation and collaboration. Prior to this feature, the details of every downstream job (Jenkins instance ID, full job name, Git branch name) all had to be meticulously specified in the upstream job. If the job name changed, the upstream job had to be refactored, creating a maintenance burden and discouraging the adoption of event-based triggers.

## Cross Team Collaboration Events

The [Cross Team Collaboration feature](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration) is designed to greatly improve team collaboration by connecting team Pipelines across any number of CloudBees CI controllers. It essentially allows a Pipeline to publish a notification event which will be trigger other Pipelines (across controllers) that are listening for that event. It consists of a **[Publishing Event](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-publishers)** and a **[Trigger Condition](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-triggers)**. 

The Cross Team Collaboration feature has a configurable router for routing events and it needs to be configured on your Managed Controllers before you will be able to receive the event published by another Managed Controller. CloudBees CI CasC was used to pre-configure this for everyone, but you can still review the configuration by going to the top-level of your Managed Controller and click on the **Manage Jenkins** left menu link and then click on **Configure Notification**. ![Configure Notification Link](config-notification-link.png?width=50pc)

 You should see the following configuration: ![Notification Configuration](notification-config.png?width=50pc)


1. To use Cross Team Collaboration we will need to update the `Jenkinsfile` in the `/templates/container-build-push` folder in your copy of the `pipeline-template-catalog` repository, to listen for a notification event to be published by the upstream, or event publishing, job. We will do that by adding a [trigger directive](https://www.jenkins.io/doc/book/pipeline/syntax/#triggers) to then template **Jenkinsfile** Pipeline script.
2. Navigate to your copy of the `pipeline-template-catalog` repository in your workshop GitHub Organization, click on the **Pull requests** link and click on the **Add Cross Team Collaboration Trigger** pull request. ![PR link](pr-link.png?width=50pc)  
Open the GitHub editor for the `/templates/container-build-push/Jenkinsfile` file in the **main** branch of your copy of the `pipeline-template-catalog` repository.
3. Click on the **Files changed** tab to review the requested configuration changes. Note that we have added a `triggers` block with an `eventTrigger` and we have updated the `when` condition to include `triggeredBy 'EventTriggerCause'`: ![PR Files Changed](pr-files-changed.png?width=50pc)
4. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Add Cross Team Collaboration Trigger** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
5. Navigate to the open **PR** job of your **insurance-frontend-build-deploy** project on your Managed Controller and click the **Build Now** link in the left menu. Then view the configuration for that job by clicking the **View Configuration** link.
6. Click on the **Build Triggers** tab on the job configuration page for the **PR-1**  job and you will see that the **Build whenever the specified event is seen** trigger is checked and configured with a **Jmespath Query** as specified in the template above.

{{% notice note %}}
After first adding a new `trigger` you must run the job at least once so that the `trigger` is saved to the Jenkins job configuration on the controller (similar to setting the `buildDiscarder` `option`).
{{% /notice %}}

7. Next, your instructor will set up a Pipeline project with the following **[JSON event](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/cross-team-collaboration#cross-team-event-types)**: 

```groovy
publishEvent event:jsonEvent("""
          {
            'image':{'name':'nginx','action':'update','tag':'1.22.0'}
          }
        """), verbose: true
```

The entire Jenkins Pipeline containing the publishing event:
```groovy
pipeline {
  agent none
  stages {
    stage('Update Docker Image') {
      steps {
        echo 'updated docker image nginx'
        publishEvent event:jsonEvent("""
          {
            'image':{'name':'nginx','action':'update','tag':'1.22.0'}
          }
        """), verbose: true
      }
    }
  }
}
```

That event will be published **across all Managed Controllers in the Workshop cluster** via the CloudBees CI Cloud Operations Center event router triggering everyones' **insurance-frontend-build-deploy** Pipelines to run. 

8. Now, once that change is committed, and the job with the `publishEvent` runs, everyone will see the open **PR** branch of their **insurance-frontend-build-deploy** job triggered by the `deploy-event` JSON event.


