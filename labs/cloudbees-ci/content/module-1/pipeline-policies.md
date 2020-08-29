---
title: "Pipeline Policies"
chapter: false
weight: 3
---

## Create a Pipeline Policy

In this lab you will create a [Pipeline Policy](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) to ensure that all Pipeline jobs that run on your CloudBees CI ***managed controller*** (Jenkins instance) have a 30 minute global `timeout` set.

1. Navigate to the top-level of your CloudBees CI managed controller and click on **Pipeline Policies** in the left menu. ![Pipeline Policies Link](policies-click.png?width=50pc) 
2. Next, on the **Pipeline Policies** screen, click on the **New Policy** button.
3. Fill out the Pipeline Policy parameters:
   1. **Name**: ***Timeout policy***
   2. **Action**: ***Fail***
   3. Click on **Add Rule** button: 
      1. Select **Pipeline Timeout**
      2. **Timeout**: 30 MINUTES
   4. Click the **Save** button ![Create Policy](policy-timeout-form.png?width=50pc) 
4. Navigate to the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder, click on the **master** branch job and then click the **Build Now** link in the left menu. ![Build with Policy](build-with-policy.png?width=50pc) 
5. Navigate to the logs for that build and you will see that the build failed due to **Validation Errors** ![Policy Error](pipeline-policy-error.png?width=50pc) 
6. To fix this we will have to update the `Jenkinsfile` of the **CloudBees CI Configuration Bundle** template in your forked copy of the `pipeline-template-catalog` repository - remember, even though we are building from the `cloudbees-ci-config-bundle` repository, the `Jenkinsfile` is actually coming from the **CloudBees CI Configuration Bundle** template. Navigate to that `Jenkinsfile` and the click the **pencil icon** to open it in the GitHub file editor. ![Edit Timeout](pipeline-policy-open-jenkinsfile.png?width=50pc) 
7. In the GitHub file editor, change the `time` value of the `timeout` pipeline `option`  from `60` to `10` and then click the **Commit changes** *(directly to the `master` branch)* button to commit the updated `Jenkinsfile` to your **master** branch. ![Fix Timeout](pipeline-policy-fix-commit-jenkinsfile.png?width=50pc) 
{{%expand "expand to copy edited Jenkinsfile" %}}
```groovy
@Library('pipeline-library@master') _
pipeline {
  agent none
  options {
    buildDiscarder(logRotator(numToKeepStr: '2'))
    skipDefaultCheckout true
    timeout(time: 10, unit: 'MINUTES')
  }
  stages {
    stage('Update Config Bundle') {
      when {
        beforeAgent true
        branch 'master'
      }
      steps {
        configBundleUpdate()
      }
    }
  }
}
```
{{% /expand%}}

8. Next, to ensure that we are using the updated **CloudBees CI Configuration Bundle** template, we will check the Pipeline Template Catalog **Import Log**. Navigate to the top-level of your CloudBees CI ***managed controller*** and click on **Pipeline Template Catalogs** link in the left menu and then click the **workshopCatalog** link. ![workshop Catalog link](workshop-catalog-link.png?width=50pc) 
9.  On the next screen, click the **Import Log** link to ensure the catalog was imported successfully and recently. ![Import Now](click-import-log-link.png?width=50pc)
10.    After the import is complete, navigate back to the **master** branch job in the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder and click the **Build Now** link in the left menu. The build will complete successfully and the logs for that build will show that the Pipeline policy validated successfully. ![Policy Success](pipeline-policy-success.png?width=50pc)

## Pipeline Policies as Code

Managing Pipeline Policies across a large number of ***managed controllers*** using the graphical user interface (GUI) is time consuming and prone to human error due to the repetitive nature of the task.

Using the provided CLI commands allows the administrator to automate the management of Pipeline Policies across multiple managed controllers, which reduces efforts and consistency across all development teams. There are two provided CLI commands for working with Pipeline Policies, listing and creating/updating. 

In this lab we leverage a Pipeline Template that uses the CloudBees CI `policies` CLI command to output the policy that you created above to a file and then push that to a new branch on your fork of the `pipeline-policies` repository. We will then update the exported policy file in GitHub to update the policy on your ***managed controller***.

1. Navigate into the **template-jobs** folder on your ***managed controller***.
2. Click on the **New Item** link in the left navigation menu.
3. Enter ***pipeline-policies-ops*** as the **Item Name**, select **Pipeline Policies GitOps** template as the item type and then click the **OK** button. ![New Pipeline Policies GitOps template job](new-policies-template-job.png?width=50pc)
4. On the next screen, fill in the **GitHub Organization** template parameter (all the other default values should be correct) and then click the **Save** button. ![Config Policies template Parameters](policies-template-params.png?width=50pc)
5. Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan and then click on the **pipeline-catalog-ops** link at the top of the page. ![Scan Log](policy-ops-scan-log.png?width=50pc)
6. Shortly after the **master** branch job completes successfully you will see a new **policy-patch** branch job. Click on the **policy-patch** branch job. ![policy-patch job](policy-patch-job.png?width=50pc)
7. Click on the **GitHub** link in the left menu to navigate to that branch in GitHub on your fork of the `pipeline-policies` repository.
8. Notice that there is now a `pipeline-policies.json` file, click on that file. ![pipeline-policies.json link](pipeline-policies-json-link.png?width=50pc)
9. Click on the pencil icon to edit the file, then update the `maxTime` from `30` to `60` and then click the **Commit changes** button at the bottom of the screen. ![edit pipeline-policies.json](edit-pipeline-policies-json.png?width=50pc)
{{%expand "expand to copy edited pipeline-policies.json" %}}
```json
[ {
  "action" : "fail",
  "customMessage" : "",
  "description" : "",
  "filter" : "",
  "name" : "Timeout policy",
  "rules" : [ {
    "$class" : "EntirePipelineTimeoutRule",
    "maxTime" : 60
  } ]
} ]
```
{{% /expand%}}
10. Navigate back to the top level of your `pipeline-policies` repository and click the **Pull request** link. ![create pr](create-policy-pr.png?width=50pc)
11. On the next screen accept the default values and then click the **Create pull request** button.
12. On the next screen click the **Merge pull request** button and then the **Confirm merge** button to merge the changes with the `master` branch of your `pipeline-policies` repository and trigger the ***pipeline-policies-ops*** job on your ***managed controller***. ![merge pr](merge-policy-pr.png?width=50pc)
13. On the next screen click the **Delete branch** button.
14. Navigate to the top-level of your CloudBees CI managed controller and click on **Pipeline Policies** in the left menu.
15. The **Timeout policy** you created in the previous lab will now have a **Timeout** value of `60 MINUTES`. ![updated policy](updated-policy.png?width=50pc)

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#36).**
