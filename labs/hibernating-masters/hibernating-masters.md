# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Hibernating Masters

The [CloudBees Core Managed Master hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) feature takes advantage of running Core on Kubernetes by automatically shutting down or hibernating Team/Managed Masters after a specified amount of time.

## Configure Hibernation
The Master Hibernation is managed at the global Jenkins configuration level. The configuration 

## Hibernation Proxy for Webhooks
The hibernating monitor service provides a post proxy for things like GitHub webhooks.

Navigate to the GitHub Organization you created for this workshop and click on the **Settings** link. 

In the **Organization settings** menu click on the **Webhooks** link. 

Click on the **Edit** button next to the webhook that was created for your Team Master.

Update the **Payload URL** by inserting `/hibernation/queue` in front of `/github-webhook/`.

Scroll down and click on the **Update webhook** button.



Please return to the [main page](../../README.md#workshop-labs) for other workshops and labs.
