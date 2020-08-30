---
title: "Using Pipeline Templates"
chapter: false
weight: 1
---

## Create a Job from Pipeline Template Catalog
In this lab you will create a new Multibranch Pipeline job from the **Maven Pipeline Template** template provided by a Pipeline Template Catalog. And just by filling in a few parameters of a Pipeline template you will have a complete continuous integration for your application.

1. On your CloudBees CI ***managed controller*** (Jenkins instance) navigate into the **template-jobs** folder.
2. Click on the **New Item** link in the left navigation menu.
3. Enter ***simple-maven-app*** as the Item Name, select **Maven Pipeline Template** as the item type and then click the **OK** button. ![New Maven Job](create-maven-job.png?width=60pc)
4. On the next screen, fill in the **GitHub Organization** template parameter with the name of the GitHub Organization you create for this workshop (all the other default values should be correct) and then click the **Save** button. ![Maven template Parameters](maven-template-params.png?width=50pc)
5. After you click the **Save** button the Multibranch Pipeline project (created by the template) will scan your fork of the `cloubees-ci-config-bunlde` repository, creating a Pipeline job for each branch where there is a marker file that matched `bundle.yaml` (or in this case, just the `PR-1` Pull Request). Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan. ![Scan Log](bundle-scan-log.png?width=50pc) 
6. Now, in **GitHub**, navigate to the **Add marker file** pull request (#1) in your fork of the **microblog-frontend** repository. <p><img src="pr-navigate.png" width=800/>
7. Click on the pull request, scroll down to the pull request checks and you will see the stage level status of the Pipeline. Here you see that the **VueJS Tests** `stage` has started. <p><img src="pr-stage-status-pending.png" width=800/>
8. Once the Pipeline finishes you will see that all the checks failed on the pull request in GitHub. Clicking on the **Details** link of the **ci/cloudbees/error** check will take you directly to the build logs with the error in your CloudBees CI managed controller (Jenkins instance). <p><img src="pr-stage-status-failed.png" width=800/>
9.  The logs show us that a test in `tests/unit/Posts.spec.js` failed - a typo where the word **function** was mis-typed as **funcion**. <p><img src="pr-failed-test-log.png" width=800/>
10. In GitHub, navigate back to the **Add marker file** pull request for your forked **microblog-frontend** repository, click on the **Files changed** tab and then click on the context menu for the `tests/unit/Posts.spec.js` file and select **Edit file**. <p><img src="pr-file-context-edit.png" width=800/>
11. In the GitHub editor for the `tests/unit/Posts.spec.js` file fix the typo changing **funcion** to **function**, and then click the **Commit changes** button to commit the changes to the **marker-file** branch of your forked **microblog-frontend** repository. <p><img src="pr-edit-fix-typo.png" width=800/>
12. Finally, on the pull request page for your **Add marker file** pull request click on the **Conversation** tab and scroll down to the pull request checks. After the **PR-1** pipeline job completes you will see that all the checks are now successful, scroll to the bottom and click the green **Merge pull request** button and then the **Confirm merge** button to merge the pull request to your **master** branch.<p><img src="pr-checks-success.png" width=800/>

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#36).**
