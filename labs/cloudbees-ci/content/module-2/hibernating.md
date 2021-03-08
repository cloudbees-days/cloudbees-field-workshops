---
title: "Hibernation for Managed Controllers"
chapter: false
weight: 6
---

The [CloudBees CI hibernation for Managed Controllers](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) feature takes advantage of running CloudBees CI on Kubernetes by automatically shutting down, or hibernating, CloudBees CI Managed Controller after a specified amount of inactivity. This feature will also automatically un-hibernate a Managed controller for certain events such as GitHub webhooks.

## Configure Hibernation
Hibernation for CloudBees CI Managed Controllers is managed at the global Jenkins configuration level and was configured in the `jenkins.yaml` file in the CloudBees CI CasC lab.

## Hibernation Proxy for Webhooks

The hibernating monitor service provides a `POST` proxy for things like GitHub webhooks. In this lab we will add a GitHub webhook to your workshop GitHub Organization that includes the [CloudBees CI hibernation POST queue endpoint](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters#post-queue-github).

1. First, we will update the hibernation grace period of your Managed Controller so we don't have to wait 25 minutes for it to hibernate. To modify the hibernation configuration via the UI you will need to login as an administrator. Click on your CloudBees CI username in the top-right corner of the screen and then select **Log Out** from the drop-down menu. ![Log Out](log-out.png?width=50pc)
2. Log back in, but append **-admin** to the GitHub username you used earlier to login with, the password is the same as before. ![Log In as Admin](log-in-admin.png?width=50pc) 
3. Navigate to the top-level of your Managed Controller, click on the **Mange Jenkins** link in the left menu and then click **Configure System**. ![Manage Jenkins](manage-jenkins.png?width=50pc)
4. Scroll down to the **Automatic hibernation** configuration and update the **Grace period** from *1500* seconds (configured via CasC) to *30* seconds and then click the **Save** button. By the time we are finished with the rest of the steps in this lab your Managed Controller should be hibernating. ![Update Grace period](update-grace-period.png?width=50pc)
5. Navigate back to CloudBees CI Cloud Operations Center by clicking on **Jenkins** in the breadcrumb navigation and then navigate to your workshiop GitHub Organization and click on the **Settings** link. ![GitHub Organization Settings link](github-org-settings-link.png?width=50pc)
6. In the **Account settings** left menu click on the **Webhooks** link and then click on the **Edit** button for the Webhook starting with **https://cbci.workshop.cb-sa.io/**. ![Edit CBCI Webhook](edit-webhook-button.png?width=50pc)
7. Before we update the webhook to use the hibernation proxy, scroll down to **Recent Deliveries**, expand the most recent delivery and click the **Redeliver** button. The *redelivery* will fail. ![Failed Webhook Redelivery](failed-webhook-redelivery.png?width=50pc)
8. We will update the **Payload URL** to send Webhooks to the `hibernation/queue/` - in this example we are setting it for a GitHub Organization with the name **bee-ci** so the payload URL would be `https://cbci.workshop.cb-sa.io/hibernation/ns/sda/queue/teams-bee-ci/github-webhook/` - update your **Payload URL** by replacing `https://cbci.workshop.cb-sa.io/` with `https://cbci.workshop.cb-sa.io/hibernation/ns/sda/queue/` before your Managed Controller specific sub-path and then click the **Update webhook** button. ![Update webhook](update-webhook-url.png?width=50pc)
9. Once again, scroll down to **Recent Deliveries**, expand the most recent delivery (the one that failed) and click the **Redeliver** button. ![Successful Webhook Redelivery](successful-webhook-redelivery.png?width=50pc)
10. Navigate to https://cbci.workshop.cb-sa.io/cjoc/ in your browser. **IMPORTANT - DO NOT CLICK ON THE LINK FOR YOU MANAGED CONTROLLER!** You should see that your Managed Controller is now hibernating. Click on the cog icon next to your Managed Controller. ![managed controller hibernating](controller-hibernating.png?width=50pc)
11.  After a few minutes your Managed Controller will no longer be hibernated and you will see that the **main** branch job for your **simple-maven-app** was triggered by the **Push event to branch main**. ![Job triggered](job-triggered.png?width=50pc)

>NOTE: If you review the **Automatic hibernation** configuration for your Managed Controller after it is awoken, then you will see that the hibernation **Grace period** has been reconfigured to a value of ***1500*** second (25 minutes) based on the value configured in the CloudBees CI configuration bundle for your Managed Controller as the configuration bundle values will always override any UI based changes.

## Un-hibernate a Managed Controllers via the Operations Center UI

1. Navigate to the classic UI of Operations Center and find your CloudBees CI ***managed controller*** (Jenkins instance) in the list of CloudBees CI ***managed controller***. 
2. If there is a light blue **pause** icon next to your CloudBees CI ***managed controller*** then it is hibernating. Just click on the link for your ***managed controller*** to **un-hibernate** it. Note that in this list of **managed controllers**, 4 are hibernating. ![Hibernating managed controllers](hibernating-controllers.png?width=50pc)
3. Once you click on your CloudBees CI ***managed controller*** link from the classic UI of Operations Center you will see a screen that shows that it is "getting ready to work". ![Un-hibernate](unhibernate.png?width=50pc)
4. After a couple of minutes, your CloudBees CI ***managed controller*** will be ready to use and in the same state as it was when it was hibernated.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#cbci-thanks">return to the workshop slides</a>**
