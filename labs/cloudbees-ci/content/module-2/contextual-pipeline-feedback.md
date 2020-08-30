---
title: "Contextual Pipeline Feedback"
chapter: false
weight: 3
---

Developers should use the tools they want and not be required to use tools that slow them down. CloudBees CI contextual feedback for Jenkins Pipelines allows you to focus on your code and not your continuous integration tool.

## Jenkins Pipeline Contextual Feedback
In this lab you will create a PR for your fork of the `simple-java-maven-app` repository that will provide an example of the contextual feedback provided by the CloudBees Slack plugin and the CloudBees SCM Reporting plugin.

1. Navigate to your `simple-java-maven-app` repository in GitHub and then navigate to the `App.java` file. ![App.java](goto-app-java.png?width=50pc)
2. Click on the pencil icon to edit the file, then update the typo changing `Helloo` to `Hello`, then scroll to the bottom of the page and select the option to ***Create a new branch for this commit and start a pull request*** and the click the **Propose changes** button. ![Propose changes](propose-changes.png?width=50pc)
3. On the next screen click the **Create pull request** button. ![Create pull request](create-pr.png?width=50pc)
4. Navigate to the [CloudBees Workshops Slack workspace](https://app.slack.com/client/T010A455W77/) and after the CloudBees CI build finishes you will receive a new Slackbot direct message from the CloudBees CI Bot. ![Slack build message](slack-build-msg.png?width=50pc)
5. Scroll to the top of the Slack message, note that the build failed, and then click on the **PR#1 Update App.java** link to review the GitHub pull request you created above. ![Slack PR link](slack-pr-link.png?width=50pc)
6. Back in GitHub, click on the **Checks** tab. 
7. On the **Checks** screen click on the **error** check under the **CloudBees CI Workshop** check run on the left side of the screen and then expand the **Log** under the **Details**. ![Check error](check-error-log.png?width=50pc)
8. 
