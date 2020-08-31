---
title: "CloudBees CI Configuration as Code for Developers"
chapter: false
weight: 2
---

As a developer you typically (and shouldn't) have access to makes configuration changes to your team's CloudBees CI ***managed controller*** (Jenkins instance). However, developers can take advantage of the GitOps approach to manage CloudBees CI CasC to request configuration changes via a GitHub pull request.

In this lab you will act as developer and CloudBees CI admin, where you will review a pull request to your `cloudbees-ci-config-bundle` repository.

1. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. ![PR link](pr-link.png?width=50pc) 
2. On the next screen, click on the **CasC for Devs lab updates** pull request (#2) and then click on the **Files changed** tab to review the requested configuration changes. As you can see, we are adding the `cloudbees-slack` plugin and `cloudbees-slack-integration` configuration for your CloudBees CI user - make sure the `slack` parameter matches the email you used to sign up to the CloudBees Workshops Slack workspace. ![PR Files Changed](dev-casc-changes.png?width=50pc)
3. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
4. On the next screen click the **Delete branch** button.
5. Navigate to the **config-bundle-ops** job under the **template-jobs** folder on your CloudBees CI managed controller. Shortly after the **master** branch job completes successfully you will see a new **monitor alert** at the top of the screen. ![Monitor alert](monitor-alert.png?width=50pc)
6. Click on the **monitor** link of your CloudBees CI managed controller and you will see that a new version of the configuration bundle is available - click on the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. NOTE: If you do not see the **Reload Configuration** button then click the **Safe Restart** button. ![Reload CasC](reload-config.png?width=50pc)
7. Your CloudBees CI managed controller will install the `cloudbees-slack` plugin and update the configuration to match what is in the `master` branch of you `cloudbees-ci-config-bundle` repository. Once the screen of your CloudBees CI managed controller has reload you will see the **Managed Jenkins** screen with the **CloudBees Slack Integration**. ![Slack Config Added](slack-config-added.png?width=50pc)
8. There is one final step to enable the CloudBees Slack integration for your user. Click your CloudBees CI user name at the top of the screen.
9. On the next screen, click on the **Slack Integration** link in the left menu. ![Slack Integration link](slack-integration-link.png?width=50pc)
10. On the **User Settings** screen for the CloudBees Slack Integration, click on the **Send Test Message** button and you should see the message ***"Message sent successfully, please check Slack"***. Finally, click on the ![Slack Send Test Message](slack-send-test-msg.png?width=50pc)
11. Navigate to the [CloudBees Workshops Slack workspace](https://app.slack.com/client/T010A455W77/) and you should see a direct message from the **Slackbot**. ![Slack Test Message](slack-test-msg.png?width=50pc)

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#37).**