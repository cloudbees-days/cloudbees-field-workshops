# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Cross Team Collaboration

## Enable Cross Team Collaboration Notifications

1. Navigate to the top-level of your Team Master and click on **Manage Jenkins** in the left menu. <p><img src="images/manage-jenkins.png" width=800/>
2. On the **Manage Jenkins** page scroll down and click on the **Configure Notification** link. <p><img src="images/configure-notification-link.png" width=800/>
3. Check the **Enabled** checkbox, select **Local Only** as the **Notification Router Implementation** and click the **Save** button. <p><img src="images/enable-notification-local.png" width=600/>

## Adding an event trigger

1. In GitHub, navigate to the **Add event trigger** pull request (#1) in your fork of the **pipeline-template-catalog** repository. <p><img src="images/collab-pr-navigate.png" width=800/>
2. To see the changes that will be made to your copy of the **VueJS** template, click on the **Files changed** tab and scroll down to see the differences. <p><img src="images/collab-pr-files-changed.png" width=800/>
3. We are adding the `eventTrigger` using `jmespathQuery` and adding a new `stage` where we are using the `getImageBuildEventPayload` Pipeline Shared Library step to extract the event payload. 
4. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button.
5. Next, to ensure that we are using the updated **VueJS** template, we will **re-import** the Pipeline Template Catalog you just updated. Navigate to the top-level of your Team Master and click on **Pipeline Template Catalogs** in the left menu and then click the **workshopCatalog** link. <p><img src="images/workshop-catalog-link.png" width=800/>
6. Finally, in order to enable the trigger on your **microblog-frontend** Pipeline jobs you need to run the job once - so navigate to the **master** branch job for the **microblog-frontend** Mutlibranch project and click the **Build Now** link in the left menu.
7. After the **VueJS** template is loaded the job configuration for your **master** branch job will be updated to reflect the addition of the event trigger. <p><img src="images/job-build-trigger.png" width=800/>

## Create a Pipeline to publish an event

Now that you have an `eventTrigger` added to your **VueJS** template we need to create a job that will publish an event that will trigger it. Each of you will create a simple Pipeline job that will publish an event to imitate the real world scenario where a new `node` base image would be built and pushed - typically by another team on a different Team Master.

1. On your Team Master and ensure that you are in the folder with the same name as your Team Master - you should see the `workshop-setup` Pipeline job.
2. Click on the **New Item** link in the left navigation menu - again, make sure that you are in the **folder** with the same name as your Team Master, and not at the root of your Team Master.
3. Enter an item name - say **publish-event** - then select **Pipeline** as the item type and then click the **OK** button. <p><img src="images/collab-publish-event-item.png" width=800/>
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
                publishEvent event: jsonEvent('{"event":"imagePush","name":"node","tag":"14.0.0-alpine3.11"}')
            }
        }
    }
}
```
<p><img src="images/collab-publish-event-copy-script.png" width=800/>

5. Click the **Build Now** link in the left menu. <p><img src="images/collab-publish-event-build.png" width=800/>
6. Once the **publish-event** Pipeline job completes successfully you will see your job for the **microblog-frontend** Mutlibranch project triggered.
7. Once the **master** branch job completes successfully you can see in the logs: `Resolved base name $NODE_IMAGE to node:14.0.0-alpine3.11` as specified by the event you published above. <p><img src="images/collab-trigger-success-logs.png" width=800/>

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#44).**

You may proceed to the next lab: [*Preview Environments with Core*](../core-preview-environment/preview-environment.md) or choose another lab on the [main page](../../README.md#workshop-labs).