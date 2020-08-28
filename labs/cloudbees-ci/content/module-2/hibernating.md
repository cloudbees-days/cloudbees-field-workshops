---
title: "Hibernation for Managed Controllers"
chapter: false
weight: 5
---

The [CloudBees CI hibernation for Managed Controllers](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) feature takes advantage of running CloudBees CI on Kubernetes by automatically shutting down or hibernating CloudBees CI managed controller after a specified amount of time of inactivity.

## Configure Hibernation
Hibernation for CloudBees CI managed controller is managed at the global Jenkins configuration level and was configured in the `jenkins.yaml` file in the CloudBees CI CasC lab.

## Un-hibernate a Managed Controllers

1. Navigate to the classic UI of Operations Center and find your CloudBees CI ***managed controller*** (Jenkins instance) in the list of CloudBees CI managed controller. 
2. If there is a light blue **pause** icon next to your CloudBees CI ***managed controller*** then it is hibernating. Just click on the link for your ***managed controller*** to **un-hibernate** it. <p><img src="images/hibernating-master.png" width=800/>
3. Once you click on your CloudBees CI ***managed controller*** link from the classic UI of Operations Center you will see a screen that shows that it is "getting ready to work". <p><img src="images/unhibernate.png" width=800/>
4. After a couple of minutes, your CloudBees CI ***managed controller*** will be ready to use and in the same state as it was when it hibernated.

## Hibernation Proxy for Webhooks
The hibernating monitor service provides a post proxy for things like GitHub webhooks.

Navigate to the GitHub Organization you created for this workshop and click on the **Settings** link. 

In the **Organization settings** menu click on the **Webhooks** link. 

Click on the **Edit** button next to the webhook that was created for your CloudBees CI ***managed controller***.

Update the **Payload URL** by inserting `/hibernation/queue` in front of `/github-webhook/`.

Scroll down and click on the **Update webhook** button.
