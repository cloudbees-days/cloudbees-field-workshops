---
title: "Cross Team Collaboration"
chapter: false
weight: 4
---

## Enable Cross Team Collaboration Notifications

We will utilize CloudBees CI CasC to enable and configure Notifications for Cross Team Collaboration.

1. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. ![PR link](pr-link.png?width=50pc) 
2. On the next screen, click on the **Cross Team Collaboration Lab: Enable Notifications** pull request (#3) and then click on the **Files changed** tab to review the requested configuration changes. As you can see, we are adding `notificationConfiguration` for your CloudBees CI managed controller. ![PR Files Changed](collab-casc-changes.png?width=50pc)
3. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
4. On the next screen click the **Delete branch** button.
5. Navigate to the **config-bundle-ops** job under the **template-jobs** folder on your CloudBees CI managed controller. Shortly after the **master** branch job completes successfully you will see a new **monitor alert** at the top of the screen. ![Monitor alert](monitor-alert.png?width=50pc)
6. Click on the **monitor** link of your CloudBees CI managed controller and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. NOTE: If you do not see the **Reload Configuration** button then click the **Safe Restart** button. ![Reload CasC](reload-config.png?width=50pc)
7. Once your managed controller is finished updating the configuration click on the **Notifications** configuration. ![Notifications config link](notifications-config-link.png?width=50pc)
8. Note that the **Notification Configuration** is **Enabled** and the **Notification Router Implementation** is set to **Local only**. ![Notifications configured](notifications-configured.png?width=50pc)

## Adding an event trigger

Now that we have configured CloudBees CI Notifications for our managed controllers we will add an event trigger to a Pipeline template.

1. In GitHub, navigate to the **Cross Team Collaboration: Add Event Trigger** pull request (#1) in your fork of the **pipeline-template-catalog** repository. ![Notifications configured](notifications-configured.png?width=50pc)
2. To see the changes that will be made to the **Maven Pipeline Template**, click on the **Files changed** tab and scroll down to see the differences. ![Notifications configured](notifications-configured.png?width=50pc)
3. We are adding the `eventTrigger` using `jmespathQuery` and adding a new `stage` where we are using the `getImageBuildEventPayload` Pipeline Shared Library step to extract the event payload. 
4. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button, then the **Confirm merge** button and then delete the branch.
5. Next, to ensure that we are using the updated **Maven Pipeline Template**, we will **re-import** the Pipeline Template Catalog you just updated. Navigate to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **Pipeline Template Catalogs** in the left menu and then click the **workshopCatalog** link. ![Notifications configured](notifications-configured.png?width=50pc)
6. Finally, in order to enable the trigger on your **simple-maven-app** Pipeline jobs you need to run the job once - so navigate to the **master** branch job for the **simple-maven-app** Mutlibranch project and click the **Build Now** link in the left menu.
7. After the **Maven Pipeline Template** is loaded the job configuration for your **master** branch job will be updated to reflect the addition of the event trigger. ![Notifications configured](notifications-configured.png?width=50pc)

## Create a Pipeline to publish an event

Now that you have an `eventTrigger` added to your **VueJS** template we need to create a job that will publish an event that will trigger it. Each of you will create a simple Pipeline job that will publish an event to imitate the real world scenario where a new `node` base image would be built and pushed - typically by another team on a different Team (Jenkins instance).

1. On your CloudBees CI managed controller (Jenkins instance) and ensure that you are in the folder with the same name as your CloudBees CI managed controller (Jenkins instance) - you should see the `cloudbees-ci-workshop-setup` Pipeline job.
2. Click on the **New Item** link in the left navigation menu - again, make sure that you are in the **folder** with the same name as your CloudBees CI managed controller (Jenkins instance), and not at the root of your CloudBees CI managed controller (Jenkins instance).
3. Enter an item name - say **publish-event** - then select **Pipeline** as the item type and then click the **OK** button. ![Notifications configured](notifications-configured.png?width=50pc)
4. Copy the following Pipeline and paste it into the **Script** text area and click the **Save** button:

```groovy
pipeline {
    agent none
    options {
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Publish Event') {
            steps {
                publishEvent event: jsonEvent('{"event":"imagePush","name":"maven","tag":"3.6.3-openjdk-15"}'), verbose: true
            }
        }
    }
}
```
<p><img src="images/collab-publish-event-copy-script.png" width=800/>

5. Click the **Build Now** link in the left menu. <p><img src="images/collab-publish-event-build.png" width=800/>
6. Once the **publish-event** Pipeline job completes successfully you will see your job for the **microblog-frontend** Mutlibranch project triggered.
7. Once the **master** branch job completes successfully you can see in the logs: `Resolved base name $NODE_IMAGE to node:14.0.0-alpine3.11` as specified by the event you published above. <p><img src="images/collab-trigger-success-logs.png" width=800/>

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#44).**
