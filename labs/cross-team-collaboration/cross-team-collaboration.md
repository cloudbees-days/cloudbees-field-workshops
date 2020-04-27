# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Cross Team Collaboration

# WORK IN PROGRESS

## Enable Cross Team Collaboration Notifications

1. Navigate to the top-level of your Team Master and click on **Manage Jenkins** in the left menu. <p><img src="images/manage-jenkins.png" width=800/>
2. On the **Manage Jenkins** page scroll down and click on the **Configure Notification** link. <p><img src="images/configure-notification-link.png" width=800/>
3. Check the **Enabled** checkbox, select **Local Only** as the **Notification Router Implementation** and click the **Save** button. <p><img src="images/enable-notification-local.png" width=600/>

## Adding an event trigger

1. In GitHub, navigate to the **Add event trigger** pull request (#1) in your fork of the **pipeline-template-catalog** repository. <p><img src="images/collab-pr-navigate.png" width=800/>
2. To see the changes that will be made to your copy of the **VueJS** template, click on the **Files changed** tab and scroll down to see the differences. <p><img src="images/collab-pr-files-changed.png" width=800/>
3. We are adding the `eventTrigger` using `jmespathQuery` and adding a new `stage` where we are using the `getImageBuildEventPayload` Pipeline Shared Library step to extract the event payload. 
4. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. <p><img src="images/collab-merge-pr.png" width=800/> 

## Create a Pipeline to publish an event

Now that you have an `eventTrigger` added to your **VueJS** template we need to create a job that will publish an event that will trigger it. Each of you will create a simple Pipeline job that will publish an event to imitate the real world scenario where a new `node` base image would be built and pushed - typically by another team on a different Team Master.

1. On your Team Master and ensure that you are in the folder with the same name as your Team Master - you should see the `workshop-setup` Pipeline job.
2. Click on the **New Item** link in the left navigation menu - again, make sure that you are in the **folder** with the same name as your Team Master, and not at the root of your Team Master.
3. Enter an item name - say **publish-event** - then select **Pipeline** as the item type and then click the **OK** button. <p><img src="images/collab-publish-item.png" width=600/>
4. 


For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#33).

You may proceed to the next lab: [*Preview Environments with Core*](../core-preview-environment/catalog-templates.md) or choose another lab on the [main page](../../README.md#workshop-labs).