---
title: "Hibernation for Managed Controllers"
chapter: false
weight: 6
---

The [CloudBees CI hibernation for Managed Controllers](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) feature takes advantage of running CloudBees CI on Kubernetes by automatically shutting down or hibernating CloudBees CI managed controller after a specified amount of time of inactivity. This feature will also automatically un-hibernate a ***managed controller*** for certain events such as GitHub webhooks.

## Configure Hibernation
Hibernation for CloudBees CI managed controller is managed at the global Jenkins configuration level and was configured in the `jenkins.yaml` file in the CloudBees CI CasC lab.

## Hibernation Proxy for Webhooks

>NOTE: For this workshop, the GitHub webhook used by all attendees has been configured at the GitHub App level and we are using [Smee.io](https://smee.io/) to forward those webhook deliveries to everyones' CloudBees CI ***managed controllers***. 

The hibernating monitor service provides a `POST` proxy for things like GitHub webhooks. In this lab we will add a GitHub webhook to your `simple-java-maven-app` repository that includes the [CloudBees CI hibernation POST queue infix](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/managing-masters#post-queue-github).

1. First, we will update the hibernation grace period of your ***managed controller*** so we don't have to wait 2 hours for it to hibernate. Navigate to the top-level of your ***managed controller***, click on the **Mange Jenkins** link in the left menu and then click **Configure System**. ![Manage Jenkins](manage-jenkins.png?width=50pc)
2. Scroll down to the **Automatic hibernation** configuration and update the **Grace period** from *7200* seconds (configured via CasC) to *60* seconds and then click the **Save** button. By the time we are finished with the rest of the steps in this lab your ***managed controller*** should be hibernating. ![Grace period](grace-period.png?width=50pc)
3. Navigate to your `simple-java-maven-app` repository and click on the **Settings** link. ![GitHub Settings link](settings-link.png?width=50pc)
4. In the **Settings** left menu click on the **Webhooks** link and then click on the **Add webhook** button. ![Add webhook button](add-webhook-button.png?width=50pc)
5. For the **Payload URL** enter the URL for your ***managed controller*** preceded by `hibernation/queue/` - in this example we are setting it for a GitHub Organization name of **bee-ci** so the payload URL would be `https://workshop.cb-sa.io/hibernation/queue/teams-bee-ci/github-webhook/`, select `application/json` as the **Content type**, enter `hmC913x+92vc+XmFvIm8Klmca2rUIyGWI4OEb+LZUaY=` as the value for the **Secret** and then click the **Add webhook** button. ![Configure webhook](configure-webhook.png?width=50pc)
6. Navigate to https://workshop.cb-sa.io/cjoc/ in your browser. **IMPORTANT - DO NOT CLICK ON THE LINK FOR YOU MANAGED CONTROLLER!** You should see that your ***managed controller*** is now hibernating - if it is not hibernated yet then wait a minute and then refresh the page. ![managed controller hibernating](controller-hibernating.png?width=50pc)
7. Navigate to the `src/main/java/com/mycompany/app/App.java` file in your `simple-java-maven-app` repository and click on the pencil icon to edit it. ![App.java](app-java-file.png?width=50pc)
8. We will fix the checkstyle warning by moving the `}` on line 10, column 17 to be alone on a line. Make the change and then click the **Commit changes** button to commit directly to the `main` branch. ![Update and commit](update-commit.png?width=50pc)
9.  After a few minutes your ***managed controller*** will no longer be hibernated and you will see that the **main** branch job for your **simple-maven-app** was triggered by the **Push event to branch main**. ![Job triggered](job-triggered.png?width=50pc)

>NOTE: If you review the **Automatic hibernation** configuration for your ***managed controller*** after it is awoken, then you will see that the hibernation **Grace period** has been reconfigured to a value of ***7200*** seconds or 2 hours based on the value configured in the CloudBees CI configuration bundle for your ***managed controller***.

## Un-hibernate a Managed Controllers via the Operations Center UI

1. Navigate to the classic UI of Operations Center and find your CloudBees CI ***managed controller*** (Jenkins instance) in the list of CloudBees CI ***managed controller***. 
2. If there is a light blue **pause** icon next to your CloudBees CI ***managed controller*** then it is hibernating. Just click on the link for your ***managed controller*** to **un-hibernate** it. Note that in this list of **managed controllers**, 4 are hibernating. ![Hibernating managed controllers](hibernating-controllers.png?width=50pc)
3. Once you click on your CloudBees CI ***managed controller*** link from the classic UI of Operations Center you will see a screen that shows that it is "getting ready to work". ![Un-hibernate](unhibernate.png?width=50pc)
4. After a couple of minutes, your CloudBees CI ***managed controller*** will be ready to use and in the same state as it was when it was hibernated.


