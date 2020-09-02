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
7. On the **Checks** screen, expand the **CloudBees CI Workshop** check if not already expanded, then click on the **error** check and then expand the **Log** under the **Details** and you will see that there is a `PMD violation` that is causing the build to fail. ![Check error](check-error-log.png?width=50pc)
8. Next, click on the **pmd** check and review the **Annotations**. ![pmd Annotations](pmd-annotations.png?width=50pc)
9. Click on the file icon to see the **UnnecessaryModifier** annotation in the context of the file with the PMD warning. 
10. On the **Files changed** screen you will see the exact line of code that is causing the PMD warning resulting in a failed build. Click on the 3 dots to the right of the file name to edit `src/main/java/com/mycompany/app/App.java`. ![edit file](edit-file.png?width=50pc)
11. In the file editor for `src/main/java/com/mycompany/app/App.java`, remove the `final` modifier from the `getMessage()` method and then scroll to the bottom of the screen and click the **Commit changes** button. ![fix pmd warning](fix-pmd-warning.png?width=50pc)
12. Return to the **Checks** tab and you will see that another build was triggered and GitHub is waiting for the checks information. ![waiting for checks](waiting-for-checks.png?width=50pc)
13. Once the build completes (you may need to refresh your GitHub Checks page), click on the **pmd** check. Next click on the **checkstyle** check and you will see that there is still one issue, but it is not blocking the build. ![build passed with checkstyle issues](build-passed.png?width=50pc)
14. Return the **Conversation** tab. Note that the **Required** checks - **checkstyle** and **pmd** - have all passed and the **Merge pull request** button is enabled. Click the **Merge pull request** button and on the next screen click the **Confirm merge** button. ![All checks passed](checks-passed-merge.png?width=40pc)
15. On the next screen click the **Delete branch** button.
16. The **master** branch job of your **simple-maven-app** Multibranch Pipeline project will now complete successfully. ![simple-maven-app success](simple-maven-app-success.png?width=50pc)

In this lab you saw how CloudBees CI contextual feedback allows you to spend more time in the tools you use for development.

**For instructor led workshops please returns to the workshop slides: https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#48**
