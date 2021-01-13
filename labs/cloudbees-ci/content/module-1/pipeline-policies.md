---
title: "Pipeline Policies"
chapter: false
weight: 3
---

Pipeline Policies are runtime validations that work for both scripted and declarative pipelines and provide administrators a way to include warnings for or block the execution of pipelines that do not comply with the policies applied to your ***managed controller***.

## Create a Pipeline Policy

In this lab you will use CloudBees CI CasC for controllers to create a [Pipeline Policy](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) to ensure that all Pipeline jobs that run on your CloudBees CI ***managed controller*** (Jenkins instance) have a maximum 30 minute global `timeout` set.

1. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. ![PR link](pr-link.png?width=50pc) 
2. 
Navigate to the top-level of your CloudBees CI ***managed controller*** and click on **Pipeline Policies** in the left menu. ![Pipeline Policies Link](policies-click.png?width=50pc) 
2. Next, on the **Pipeline Policies** screen, you will see a policy with the following settings - matching the CasC:
   1. **Name**: ***Timeout policy***
   2. **Action**: ***Fail***
   3. Click on **Add Rule** button: 
      1. Select **Pipeline Timeout**
      2. **Timeout**: 30 MINUTES
   4. Click the **Save** button ![Create Policy](policy-timeout-form.png?width=50pc) 
4. Navigate to the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder, click on the **master** branch job and then click the **Build Now** link in the left menu. ![Build with Policy](build-with-policy.png?width=50pc) 
5. Navigate to the logs for that build and you will see that the build failed due to **Validation Errors** ![Policy Error](pipeline-policy-error.png?width=50pc) 
6. To fix this we will have to update the `Jenkinsfile` of the **CloudBees CI Configuration Bundle** template in your forked copy of the `pipeline-template-catalog` repository - remember, even though we are building from the `cloudbees-ci-config-bundle` repository, the `Jenkinsfile` is actually coming from the **CloudBees CI Configuration Bundle** template. Navigate to that `Jenkinsfile` and click the **pencil icon** to open it in the GitHub file editor. ![Edit Timeout](pipeline-policy-open-jenkinsfile.png?width=50pc) 
7. In the GitHub file editor, change the `time` value of the `timeout` pipeline `option`  from `60` to `10` (it needs to be 30 minutes or less to validate against the ***Timeout policy***) and then click the **Commit changes** *(directly to the `master` branch)* button to commit the updated `Jenkinsfile` to your **master** branch. ![Fix Timeout](pipeline-policy-fix-commit-jenkinsfile.png?width=50pc) 
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

8. Next, to ensure that we are using the updated **CloudBees CI Configuration Bundle** template, we will check the Pipeline Template Catalog **Import Log**. Navigate to the top-level of your CloudBees CI ***managed controller*** and click on **Pipeline Template Catalogs** link in the left menu and then click the **workshopCatalog** link. 
   - ***NOTE:*** *Because the **pipeline-catalog-ops** project is a Multibranch pipeline it will be triggered via a GitHub webhook on all code commits resulting in a re-import of the Pipeline Template Catalog.* ![workshop Catalog link](workshop-catalog-link.png?width=50pc) 
9.  On the next screen, click the **Import Log** link to ensure the catalog was imported successfully and recently. ![Import Now](click-import-log-link.png?width=50pc)
10.    After the import is complete, navigate back to the **master** branch job in the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder and click the **Build Now** link in the left menu. The build will complete successfully and the logs for that build will show that the Pipeline policy validated successfully. ![Policy Success](pipeline-policy-success.png?width=50pc)


**For instructor led workshops please return to the workshop slides: https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#36**
