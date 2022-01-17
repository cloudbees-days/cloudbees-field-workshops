---
title: "Configuration as Code"
chapter: false
weight: 2
---

In this lab we will setup [GitOps](https://www.gitops.tech/) for [CloudBees CI Configuration as Code (CasC) ](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/core-casc-modern) so that any CloudBeees CI configuration changes you make in source control will be made available to reload in your CloudBees CI ***managed controller*** (Jenkins instance). 

## GitOps for CloudBees CI CasC

In this lab you will:
* merge a pull request in your copy of the `cloudbees-ci-config-bundle` repository with some CasC changes and add the necessary Pipeline Template `marker` file to the `main` branch, so it will trigger the `main` branch job for your ***config-bundle-ops*** Mutlibranch project.
* update the ***CloudBees CI Configuration Bundle*** Pipeline Catalog template to use [CloudBees CI Cross Team Collaboration feature](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration) to trigger a job on another controller, with permissions to use `kubectl` to copy files to the Operations Center `pod`, by publishing a notification event.

1.  Navigate back to your CloudBees CI ***managed controller*** and ensure that you are in the **config-bundle-ops** Multi-branch Project in the **template-jobs** folder. Click on the **Scan Repository Log** link in the left menu to see the results of the branch indexing scan. ![Scan Log](bundle-scan-log.png?width=50pc) 
2.  Next, click on the **config-bundle-ops** link in the menu at the top of page and you will see that there are no jobs for **Branches** and 5 jobs for **Pull Requests**.  Click on the **Pull Requests** tab. ![Scan Log](bundle-no-branch-jobs.png?width=50pc) 
3.  In the **Pull Requests** view of your Multibranch project click on the link for **PR-1**. ![PR-1 Link](pr-link.png?width=50pc)
4.  On the build screen for **PR-1** click on the **GitHub** link in the left navigation menu that will take you to the pull request page in GitHub. ![PR-1 GitHub Link](pr-github-link.png?width=50pc)
5.  To review the changes that will be made to your CloudBees CI configuration bundle for your CloudBees CI ***managed controller***, click on the **Files changed** tab and scroll down to see the differences. 
    - The `version` of the `bundle.yaml` file was updated to **2**, this is no longer required to trigger a reload of the configuration bundle from CloudBees CI Operations Center to your managed controller, but it is useful for tracking bundle changes.
    - `items.yaml` was added to the list of files in the `bundle.yaml` file and the `items.yaml` file that is being added includes the configuration for the `template-jobs` folder and the `config-bundle-ops` Pipeline Template Catalog job. ![Adding items](pr-files-changed-items.png?width=50pc)
    - The `cloudbees-pipeline-policies` plugin, that we will need for the next lab, was added to the `plugins.yaml` file. ![Scan Log](pr-files-changed.png?width=50pc)
    - A pod template was added to provide ephemeral agents for maven tasks.
6. Once you have reviewed the changes, click back on the **Conversation** tab and then click the green **Merge pull request** button and then the **Confirm merge** button. ![Merge PR](merge-pr.png?width=50pc)
7. Navigate back to your CloudBees CI ***managed controller*** and then navigate to the ***main*** branch job of your **config-bundle-ops** Multi-branch Project in the **template-jobs** folder.

{{% notice note %}}
A job was created for the `main` branch of your copy of the `cloudbees-ci-config-bundle` repository because when you merged the pull request it added the `.markerfile` to your `main` branch and that triggered the ***config-bundle-ops*** Multibranch Pipeline template to create the job.
{{% /notice %}}

8. The job will fail with the following error:

```
Error from server (Forbidden): pods "cjoc-0" is forbidden: User "system:serviceaccount:controllers:jenkins" cannot get resource "pods" in API group "" in the namespace "cbci"
```
9. The reason you get this error is because your **controller** has been provisioned to a different Kubernetes `namespace` than Operations Center and no agent `pod` in the `controllers` namespace will have the permissions to copy files with `kubectl` (a CLI tool for Kubernetes) to the Operations Center Kubernetes `pod`. To fix this, you must update the ***CloudBees CI Configuration Bundle*** Pipeline Catalog template to trigger a job on another controller that is able to use `kubectl` to copy updated bundle files to Operations Center. 

{{% notice note %}}
Provisioning controllers and agents in a different namespace than Operations Center provides additional isolation and more security for Operations Center. By default, when controllers are created in the same namespace as Operations Center and agents, they can provision an agent that can run the `pod` `exec` command against any other `pod` in the `namespace` - including the Operations Center's `pod`.
{{% /notice %}}

10. Navigate to your copy of the `pipeline-template-catalog` repository in your workshop GitHub Organization and open the `Jenkinsfile` for the ***CloudBees CI Configuration Bundle*** Pipeline Catalog template in the `templates/casc-bundle/` directory. ![casc-bundle Jenkinsfile path](casc-bundle-template-path.png?width=50pc)
11. Click the **pencil icon** to open it in the GitHub file editor and replace the entire contents with the following and click on the **Commit changes** button to commit to the `main` branch:

```groovy
library 'pipeline-library'
pipeline {
  agent none
  options {
    buildDiscarder(logRotator(numToKeepStr: '2'))
    timeout(time: 60, unit: 'MINUTES')
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
      }
    }
  }
}
```

Note that we replaced the previous `steps` with the `publishEvent` step (along with the `gitHubParseOriginUrl` pipeline library utility step). The `publishEvent` step with send a notification to a message bus on Operations Center and result in the triggering of any job that is configured to listen for that event. The configuration for the job that it triggers [is available here](https://github.com/cloudbees-days/cloudbees-ci-casc-bundle-update/blob/main/Jenkinsfile).

12. Navigate back to your CloudBees CI ***managed controller*** and then navigate to the ***main*** branch job of your **config-bundle-ops** Multi-branch Project in the **template-jobs** folder and click the **Build Now** link in the left menu. After the job successfully completes, navigate to the top-level of your ***managed controller***. ![CasC Update Success](casc-job-success.png?width=50pc)

{{% notice note %}}
After you commit the changes to the `main` branch, a GitHub webhook will trigger the updating of the ***CloudBees CI Workshop Template Catalog*** on your controller. This may take longer than it takes you to re-trigger the job, so if it fails again, just wait a few seconds and click **Build Now** again.
{{% /notice %}}

13. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code export and update** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
14.  On the next screen, click on the **Bundle Update** link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. 

{{% notice note %}}
If you don't see the new version available then click the **Check for Updates** button. Also, once you click **Yes** it may take a few minutes for the bundle update to reload.
{{% /notice %}}
![Bundle Update](new-bundle-available.png?width=50pc)

15. Navigate back to the top-level of your ***managed controller***. Among other configuration changes, you will now see a link for **Pipeline Polices** in the left navigation menu and an updated system message for your CloudBees CI managed controller. ![New CasC applied](casc-update-applied.png?width=50pc)

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#casc-lab-review">return to the workshop slides</a>**
