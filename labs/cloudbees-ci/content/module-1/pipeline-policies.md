---
title: "Pipeline Policies"
chapter: false
weight: 3
---

## Create a Pipeline Policy

In this lab you will create a [Pipeline Policy](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) to ensure that all Pipeline jobs that run on your CloudBees CI ***managed controller*** (Jenkins instance) have a 30 minute global `timeout` set.

1. Navigate to the top-level of your CloudBees CI managed controller and click on **Pipeline Policies** in the left menu. ![Pipeline Policies Link](policies-click.png?width=50pc) 
2. Click on **New Policy** ![New Policy](new-policy-click.png?width=50pc) 
3. Fill out the Pipeline Policy parameters:
   1. **Name**: Timeout policy
   2. **Action**: Fail
   3. Click on **Add Rule** button: 
      1. Select **Pipeline Timeout**
      2. **Timeout**: 30 MINUTES
   4. Click the **Save** button <p><img src="policy-timeout-form.png" width=800/>
4. Navigate back to the **update-config-bundle** Mutlibranch project in the **template-jobs** folder, click on the **master** branch job and then click the **Build Now** link in the left menu. ![Build with Policy](build-with-policy.png?width=50pc) 
5. Navigate to the logs for that build and you will see that the build failed due to **Validation Errors** ![Policy Error](pipeline-policy-error.png?width=50pc) 
6. To fix this we will have to update the `Jenkinsfile` of the **CloudBees CI Configuration Bundle** template in your forked copy of the `pipeline-template-catalog` repository - remember, even though we are building from the `cloudbees-ci-config-bundle` repository, the `Jenkinsfile` is actually coming from the **CloudBees CI Configuration Bundle** template. Navigate to that `Jenkinsfile` and the click the **pencil icon** to open it in the GitHub file editor. ![Edit Timeout](pipeline-policy-open-jenkinsfile.png?width=50pc) 
7. In the GitHub file editor, change the `time` value of the `timeout` pipeline `option`  from `60` to `30` and then click the **Commit changes** button to commit the updated `Jenkinsfile` to your **master** branch. ![Fix Timeout](pipeline-policy-fix-commit-jenkinsfile.png?width=50pc) 
{{%expand "***Expand to copy complete updated `Jenkinsfile`***" %}}
```groovy
@Library('pipeline-library@master') _
pipeline {
  agent none
  options {
    buildDiscarder(logRotator(numToKeepStr: '2'))
    skipDefaultCheckout true
    timeout(time: 30, unit: 'MINUTES')
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

8. Next, to ensure that we are using the updated **CloudBees CI Configuration Bundle** template, we will **re-import** the Pipeline Template Catalog you just updated. Navigate to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **Pipeline Template Catalogs** in the left menu and then click the **workshopCatalog** link. ![workshop Catalog link](workshop-catalog-link.png?width=50pc) 
9.  On the next screen, click the **Run Catalog Import Now** link. ![Import Now](click-import-link.png?width=50pc)
10.  After the import is complete, navigate back to the **master** branch job in the **update-config-bundle** Mutlibranch project in the **template-jobs** folder and click the **Build Now** link in the left menu. The build will complete successfully and the logs for that build will show that the Pipeline policy validated successfully. ![Policy Success](pipeline-policy-success.png?width=50pc)

**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#36).**
