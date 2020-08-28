---
title: "Using Pipeline Templates"
chapter: false
weight: 1
---

## Create a Job from Pipeline Template Catalog
In this lab you will create a new Multibranch Pipeline job from the **VueJS** template provided by the Pipeline Template Catalog you added above - just by filling in a few parameters.

1. On your CloudBees CI managed controller (Jenkins instance) navigate into the **template-jobs** folder.
2. Click on the New Item link in the left navigation menu.
3. Enter ***simple-maven-app*** as the Item Name, select **Maven Pipeline Template** as the item type and then click the **OK** button. ![New Maven Job](create-maven-job.png?width=60pc)
4. **Enter an item name** as ***[GitHub username]-frontend***, select **VueJS**  and click the **OK** button. <p><img src="item_form.png" width=800/>
5. Fill out the template parameters:
   1. **Repository Owner**: the GitHub Organization your created for the CloudBees CI workshop
   2. **Repository**: The name of your forked repository, *microblog-frontend*
   3. **GitHub Credential ID**: select the *username/password* credential created for you by the **workshop-setup** job and CloudBees CI CasC - it will show up as - [GitHub username]/******
   4. Click the **Save** button<p><img src="template_parameters.png" width=800/>
6. After the initial scan you will see one Jenkins Pipeline job funder the **Pull Requests** tab of the Pipeline Mulitbranch project that was just created for your fork of the **microblog-frontend** repository - **PR-1**. <p><img src="one_job.png" width=800/>
7. Now, in **GitHub**, navigate to the **Add marker file** pull request (#1) in your fork of the **microblog-frontend** repository. <p><img src="pr-navigate.png" width=800/>
8. Click on the pull request, scroll down to the pull request checks and you will see the stage level status of the Pipeline. Here you see that the **VueJS Tests** `stage` has started. <p><img src="pr-stage-status-pending.png" width=800/>
9. Once the Pipeline finishes you will see that all the checks failed on the pull request in GitHub. Clicking on the **Details** link of the **ci/cloudbees/error** check will take you directly to the build logs with the error in your CloudBees CI managed controller (Jenkins instance). <p><img src="pr-stage-status-failed.png" width=800/>
10. The logs show us that a test in `tests/unit/Posts.spec.js` failed - a typo where the word **function** was mis-typed as **funcion**. <p><img src="pr-failed-test-log.png" width=800/>
11. In GitHub, navigate back to the **Add marker file** pull request for your forked **microblog-frontend** repository, click on the **Files changed** tab and then click on the context menu for the `tests/unit/Posts.spec.js` file and select **Edit file**. <p><img src="pr-file-context-edit.png" width=800/>
12. In the GitHub editor for the `tests/unit/Posts.spec.js` file fix the typo changing **funcion** to **function**, and then click the **Commit changes** button to commit the changes to the **marker-file** branch of your forked **microblog-frontend** repository. <p><img src="pr-edit-fix-typo.png" width=800/>
13. Finally, on the pull request page for your **Add marker file** pull request click on the **Conversation** tab and scroll down to the pull request checks. After the **PR-1** pipeline job completes you will see that all the checks are now successful, scroll to the bottom and click the green **Merge pull request** button and then the **Confirm merge** button to merge the pull request to your **master** branch.<p><img src="pr-checks-success.png" width=800/>