---
title: "Pipeline Policies"
chapter: false
weight: 3
---

Pipeline Policies are runtime validations that work for both scripted and declarative pipelines, and provide administrators a way to include warnings for or block the execution of pipelines that do not comply with the policies applied to your ***managed controller***.

## Create a Pipeline Policy

In this lab you will use CloudBees CI CasC for controllers to create a [Pipeline Policy](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) to enforce that all Pipeline jobs that run on your CloudBees CI ***managed controller*** (Jenkins instance) have a maximum 30 minute global `timeout` set.

1. Navigate to your `cloudbees-ci-config-bundle` repository in GitHub and click on the **Pull requests** link. ![PR link](pr-link.png?width=50pc) 
2. On the next screen, click on the **Pipeline Policies lab updates** pull request and then click on the **Files changed** tab to review the requested configuration changes. Note the addition of the `cloudbees-pipeline-policies` configuration at the top of the `jenkins.yaml` file. We also updated the bundle version and the Jenkins system message. ![PR Files Changed](pr-files-changed.png?width=50pc)
3. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
5. Navigate to the **config-bundle-ops** Multibranch Pipeline project under the **template-jobs** folder on your CloudBees CI managed controller.
6. Shortly after the **main** branch job completes successfully navigate to the top-level of your managed controller.
7. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code export and update** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
8.  On the next screen, click on the **Bundle Update** link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. 

{{% notice note %}}
If you don't see the new version available then click the **Check for Updates** button. Remember, the **config-bundle-ops** pipeline is triggering a job on another controller, so the update won't be available until that job has completed.
{{% /notice %}}
![Bundle Update](new-bundle-available.png?width=50pc)

9. After the updated configuration bundle has finished loading, click on the **Pipeline Policies** link in the left menu. ![Pipeline Policies Link](policies-click.png?width=50pc) 
10. Next, on the **Pipeline Policies** screen, you will see a policy with the following settings - matching the configuration from the updated CasC bundle:
    - **Name**: ***Timeout policy***
    - **Action**: ***Fail***
    - A **Rule** with a **Pipeline Timeout** of 30 MINUTES
   ![Create Policy](policy-timeout-form.png?width=50pc) 
11. Navigate to the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder, click on the **main** branch job and then click the **Build Now** link in the left menu. ![Build with Policy](build-with-policy.png?width=50pc) 
12. Navigate to the logs for that build and you will see that the build failed due to **Validation Errors**. ![Policy Error](pipeline-policy-error.png?width=50pc) 
13. To fix this we will have to once again update the `Jenkinsfile` of the **CloudBees CI Configuration Bundle** template in your copy of the `pipeline-template-catalog` repository - remember, even though we are building from the `cloudbees-ci-config-bundle` repository, the `Jenkinsfile` is actually coming from the **CloudBees CI Configuration Bundle** template. Navigate to that `Jenkinsfile` and click the **pencil icon** to open it in the GitHub file editor. ![Edit Timeout](pipeline-policy-open-jenkinsfile.png?width=50pc) 
14. In the GitHub file editor, change the `time` value of the `timeout` pipeline `option`  from `60` to `10` (it needs to be 30 minutes or less to successfully validate against the ***Timeout policy***) and then click the **Commit changes** *(directly to the `main` branch)* button to commit the updated `Jenkinsfile` to your **main** branch. ![Fix Timeout](pipeline-policy-fix-commit-jenkinsfile.png?width=50pc) 
{{%expand "expand to copy edited Jenkinsfile" %}}
```groovy
library 'pipeline-library'
pipeline {
  agent none
  options {
    buildDiscarder(logRotator(numToKeepStr: '2'))
    timeout(time: 10, unit: 'MINUTES')
  }
  stages {
    stage('Publish CasC Bundle Update Event') {
      agent { label 'default' }
      when {
        beforeAgent true
        branch 'main'
      }
      environment { CASC_UPDATE_SECRET = credentials('casc-update-secret') }
      steps {
        gitHubParseOriginUrl()
        publishEvent event:jsonEvent("""
          {
            'controller':{'name':'${BUNDLE_ID}','action':'casc_bundle_update','bundle_id':'${BUNDLE_ID}'},
            'github':{'organization':'${GITHUB_ORG}','repository':'${GITHUB_REPO}'},
            'secret':'${CASC_UPDATE_SECRET}',
            'casc':{'auto_reload':'false'}
          }
        """), verbose: true

        withCredentials([usernamePassword(credentialsId: 'api-token', usernameVariable: 'JENKINS_CLI_USR',     passwordVariable: 'JENKINS_CLI_PSW')]) {
          waitUntil {
            script {
              def UPDATE_AVAILABLE = sh (script: '''curl -s --user $JENKINS_CLI_USR:$JENKINS_CLI_PSW -XGET http://${BUNDLE_ID}.controllers.svc.cluster.local/${BUNDLE_ID}/casc-bundle-mgnt/check-bundle-update  | jq '.["update-available"]' | tr -d "\n" ''', 
                returnStdout: true) 
              echo "update available: ${UPDATE_AVAILABLE}"
              return (UPDATE_AVAILABLE=="true")
            }
          }
        }
      }
    }
  }
}
```
{{% /expand%}}

15. Next, to ensure that we are using the updated **CloudBees CI Configuration Bundle** template, we will check the Pipeline Template Catalog **Import Log**. Navigate to the top-level of your CloudBees CI ***managed controller*** and click on **Pipeline Template Catalogs** link in the left menu and then click the **workshopCatalog** link. 

{{% notice note %}}
Merging the updated `Jenkinsfile` for that template will trigger a GitHub webhook resulting in a re-import of the ***CloudBees CI Workshop Template Catalog***.
{{% /notice %}}
![workshop Catalog link](workshop-catalog-link.png?width=50pc) 

16.  On the next screen, click the **Import Log** link to ensure the catalog was imported successfully and recently. ![Import Now](click-import-log-link.png?width=50pc)
17.    After the import is complete, navigate back to the **main** branch job in the **config-bundle-ops** Mutlibranch project in the **template-jobs** folder and click the **Build Now** link in the left menu. The build will complete successfully and the logs for that build will show that the Pipeline policy validated successfully. ![Policy Success](pipeline-policy-success.png?width=50pc)


**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#pipeline-policies-overview">return to the workshop slides</a>**
