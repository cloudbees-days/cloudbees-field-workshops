---
title: "CloudBees Pipeline Template Catalogs"
chapter: false
weight: 5
--- 

Pipeline Template Catalogs provide version controlled paramaterized templates for Multibranch and stand-alone Pipeline jobs. In this exercise we will use [Pipeline Template Catalogs](https://github.com/cloudbees-days/pipeline-template-catalog/tree/master/templates/nodejs-app) to create a templatized Multibranch Pipeline project of your workshop copy of the **helloworld-nodejs** repository. All you will need to do is fill in a few simple parameters and you will end up with a complete end-to-end CI/CD Pipeline for the **helloworld-nodejs** application - and it won't be using the `Jenkinsfile` from your repository.

## Create a Multibranch Project from a Pipeline Template Catalog
[Jenkins Configurations as Code](https://wiki.jenkins.io/display/JENKINS/Configuration+as+Code+Plugin) (JCasC) was used to pre-configure a Pipeline Template Catalog on everyone's Managed Controller and there is a **template-jobs** folder on your Managed Controller that has been configured with [CloudBees Folders Plus folder item filtering](https://go.cloudbees.com/docs/plugins/folders-plus/#folders-plus-sect-restrict) to only allow the creation of certain job types. Now we will create a templatized end-to-end CI/CD Pipeline Multibranch project for your copy of the **helloworld-nodejs** repository.

1. On your CloudBees CI Managed Controller navigate to the **template-jobs** folder and then lick on the ***New Node.js App Multibranch Pipeline*** link in the left menu. ![Create Job from Template](create-template-job-link.png?width=50pc)
2. Enter an item name of your **[GitHub username]-hello**, select **Node.js App Multibranch Pipeline**  and click the **OK** button. ![New Item Form](new-item-form.png?width=50pc)
3. Fill out the template parameters:
   1. **Repository Owner**: the GitHub Organization your created for the CloudBees CI Pipeline Workshop.
   2. Use the default values for the rest of the parameters.
   3. Click the **Save** button. ![Template Parameters](template-parameters.png?width=50pc)
4. The initial scan won't find any branches because you have to add the [custom markerfile](https://go.cloudbees.com/docs/cloudbees-core/cloud-admin-guide/pipeline/#_multibranch_pipeline_options_in_template_yaml) `.nodejs-app` to any branch that you want a job to be created. The [template we are using has a `markerFile` parameter set to `.nodejs-app`](https://github.com/cloudbees-days/pipeline-template-catalog/blob/master/templates/nodejs-app/template.yaml#L29), so we need to add that file to at least one branch of your copy of the **helloworld-nodejs** repository.
5. Make sure you are on the **development** branch and click on the **Create new  file** button towards the top right of the screen. 
6. Name the file `.nodejs-app` and commit the empty file to your **development** branch.
7. You may need to refresh the Multibranch job screen, but you should eventually have **one** job - for the **development** branch. ![One Job](one-job.png?width=50pc)

## Web Browser Tests with Testcafe

Executing [Testcafe](http://devexpress.github.io/testcafe/) driven browser tests for the **helloworld-nodejs** app in our Pipeline.

1. After you add the custom marker file, your **development** branch job will run and it will fail. On the job details screen for the failed run we can see that there was a test failure. Click on the **Test Result** link to see the specific test error. ![Job Details Failed Test](job-details-failed-test.png?width=50pc)
2. On the **Test Result** page, expand the **Initial page.Check message header** test and then expand the **Stack Trace** and you will see that there is a slight typo in the **helloworld-nodejs** app. ![Test Results Failure](test-results-failure.png?width=50pc)
3. In GitHub, open editor for the `hello.js` file on the **development** branch of your forked copy of the **helloworld-nodejs** repository, fix the misspelling of **Worlld** to **World** and then commit the changes. ![Fix Error](fix-error.png?width=50pc)
4. Navigate to the **development** branch of your **helloworld-nodejs** job on your Managed Controller and your job should already be running as a GitHub webhook triggered it when you commited the changes for the `hello.js` file in the **helloworld-nodejs** repository. The tests should pass and the job should complete successfully. ![Test Passed](test-passed.png?width=50pc)

## Deploy to Staging
Now that you have fixed the small bug in the **helloworld-nodejs** application, we will create a Pull Request and merge the change to the **master** branch of your forked copy of the **helloworld-nodejs** repository.

1. Navigate to your forked **helloworld-nodejs** repository in GitHub - click on the **New pull request** button <p><img src="img/intro/conditional_new_pull_request.png" width=800/>
2. Change the **base repository** to the **master** branch of your forked **helloworld-nodejs** repository (not the **cloudbees-days** repository), add a comment and then click the **Create pull request** button
3. A job will be created for the pull request and once it has completed successfully your pull request will show that **All checks have passed**. Go ahead and click the **Merge pull request** button and then click the **Confirm merge** button but **DO NOT DELETE** the **development** branch
4. Navigate to the **helloworld-nodejs** Pipeline Template Catalog job in Blue Ocean on your Team Master and the job for the **master** branch should be running or queued to run
5. The templated job will build a Docker image for your **helloworld-nodejs** application, push the image to the Google Container Registry (GCR), and then deploy your containerized application to a staging environment in Kubernetes - a link to your application will be available in the logs of your job. 

### GitOps with Core v2
As part of the deployment to *staging* the Pipeline Template Catalog job will create a new **environment-staging** repository in your workshop GitHub Organization with the generated Kubernetes deployment yaml used for the deployment to the K8s *staging* environment.

~~### Cross Team Collaboration
In addition to deploying to the *staging* environment, the Pipeline Template will also pubslish a Cross Team Collaboration event `containerImagePush` that the Core Workshop security team is listening for - anytime that this event is publish a job will be triggered on the **team-sec** Team Master to scan the image you just published with [Anchore](https://anchore.com/). Your application will not be deployed to production unless it passes this scan.~~

You may proceed to the next lab [*Lab 6 - Cross Team Collaboration*](./cross-team-collaboration.md) or head back to the main list of the [**labs**](./README.md#workshop-labs) when you are ready.
