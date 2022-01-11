---
title: "CloudBees CI Configuration Bundle Management"
chapter: false
weight: 3
--- 

CloudBees CI configuration bundles are centrally managed and stored in the `jcasc-bundles-store` directory in the Operations Center Jenkins home directory. In order to make a bundle available for a controller, or to update an existing bundle, the bundle files must be copied to the `jcasc-bundles-store` directory.

{{% notice note %}}
While Operations Center simplifies the management of bundles, it is possible to configure a controller with a bundle without Operations Center using the `-Dcore.casc.config.bundle=/path/to/casc-bundle` Java system property.
{{% /notice %}}

The labs in this section will explore:

- storing and managing configuration bundles on Operations Center
- setting a default configuration bundle
- setting up GitOps for automating CloudBees CI configuration bundle updates

## Managing Configuration Bundles on Operations Center

This lab will provide an overview of how configuration bundles are managed via the Operations Center UI and how to manually apply a configuration bundle to a controller. The first part of the overview will be on the Operations Center **Configuration as Code bundles** settings page that is only accessible by workshop instructors. Therefore, the first part of this lab, that will explore the 3 major components on the Operations Center **Configuration as Code bundles** settings page, wont' have any hands-on material.

![Operations Center Configuration as Code bundles settings pag](ops-center-config-bundle-settings.png?width=70pc)

1. By checking the **Availability pattern** checkbox, any configuration bundle that has an empty **Availability pattern** can be used by any controller.
2. The **Default bundle** drop-down allows you to automatically apply a default configuration bundle to any controller that does not specify a different configuration bundle.
3. The **cog** icon signifies that the bundle's availability pattern has been defined in the UI, to include overriding availability patterns set in the `bundle.yaml`.
4. The **bundle** icon signifies that the availability pattern was set in the `bundle.yaml` via the `availabilityPattern` field. Note that setting the **Availability pattern**  with the `availabilityPattern` field allows managing this value with each individual bundle rather than having to specify it in the UI.
5. The configuration bundle **Availability pattern** allows assigning regular expressions that must match the full path to one or more controllers in order to use that bundle. For the `base` bundle, the **Availability pattern** is empty and this typically would not match any path, but since the **Availability pattern** checkbox is checked it is available to all controllers.
6. For the `ops` bundle, the **Availability pattern** is set to `operations/ops`. So that means only a controller with the name **ops** in the **operations** folder can use this bundle. If the **Availability pattern** were set to `operations/*` then any controller in the **operations** folder could use this bundle.

### Applying Bundles to Controllers
1. To actually apply a bundle to a controller, you must select the bundle from the **Bundle** drop-down on the controller configuration page. To do this navigate to the top level of Operations Center and click on the **Manage** icon for your Ops controller. ![Manage controller link](manage-controller-link.png?width=60pc)
2. On the controller manage screen click on the **Configure** link in the left menu. ![Configure controller link](configure-controller-link.png?width=50pc)
3. On the configure controller screen, scroll down to the **Configuration as Code (CasC)** section and expand the **Bundle** drop down. ![Bundle dropdown](bundle-dropdown.png?width=50pc)
4. Note that the bundle matching the name of your Ops controller is selected and the `base` bundle is also available, but the `ops` bundle is not available to select. ![Bundle dropdown expanded](bundle-dropdown-expanded.png?width=50pc)
5. We do not actually need to change the configured bundle, so just click on the breadcrumb link for your Ops controller to exit from the controller configuration page. ![Controller breadcrumb link](controller-breadcrumb-link.png?width=50pc)

## GitOps for CloudBees CI Configuration Bundles

In this lab we will update the `controller-casc-update` job (created by CasC) to automatically update our controllers' configuration bundles whenever any changes are committed to the GitHub `main` branch for the controller's configuration bundle repository. The `controller-casc-update` job is actually a [GitHub Organization Folder project](https://www.jenkins.io/doc/book/pipeline/multibranch/#organization-folders) with a [custom marker file](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-as-code#custom-pac-scripts). Instead of using the typical `Jenkinsfile`, we will use `bundle.yaml` as our custom marker file. By using the custom marker file with a GitHub Organization Folder project, a Multibranch Pipeline project will automatically be created for all repositories in your workshop GitHub Organization when the `main` branch contains a `bundle.yaml` file.
 
1. Navigate to the `ops-controller` repository in your workshop GitHub Organization.
2. Next click on the`controller-casc-update`file to open it. It will match the contents of the file below.

```groovy
library 'pipeline-library'
pipeline {
  agent {
    kubernetes {
      yaml libraryResource ('podtemplates/kubectl.yml')
    }
  }
  options {
    timeout(time: 10, unit: 'MINUTES')
  }
  stages {
    stage('Update Config Bundle') {
      when {
        beforeAgent true
        branch 'main'
        not { triggeredBy 'UserIdCause' }
      }
      steps {
        gitHubParseOriginUrl()
        container("kubectl") {
          sh "mkdir -p ${GITHUB_ORG}-${GITHUB_REPO}"
          sh "find -name '*.yaml' | xargs cp --parents -t ${GITHUB_ORG}-${GITHUB_REPO}"
          sh "kubectl cp --namespace cbci ${GITHUB_ORG}-${GITHUB_REPO} cjoc-0:/var/jenkins_home/jcasc-bundles-store/ -c jenkins"
        }
      }
    }
  }
}
```

4. On the first line you will see that we are using the Pipeline shared library defined in your Ops controller configuration bundle. The Pipeline shared library contains a number of Jenkins Kubernetes Pod templates that can be leveraged across all the controllers. We are utilizing the `kubectl.yml` Pod template, so we can use the `kubectl cp` command to copy your `ops-controller` configuration bundle files into the `jcasc-bundles-store` directory on Operations Center. Once you have finished reviewing the `controller-casc-update` pipeline contents, navigate to the top level of your Ops controller and click the on the controller-jobs folder.

5. Once you have finished reviewing the `controller-casc-update` pipeline contents, navigate to the top level of your Ops controller and click the on the `controller-jobs` folder. Inside of the `controller-jobs` folder, click on the `controller-casc-update` job. ![CasC job link](casc-job-link.png?width=50pc)
6. On the next screen, you will see **This folder is empty**. The reason it is empty is because the GitHub Folder branch scan did not find any matches for the current *marker file*. Click on the **Configure** link in the left menu so we can fix that.  ![CasC job config link](casc-job-config-link.png?width=50pc)
7. Scroll down to the **Project Recognizers** section. Under **Custom script**, notice how the **Marker file** is configured. ![Wrong marker file](wrong-marker-file.png?width=50pc)
8. With the default **project recognizer**, the file you specify (usually `Jenkinsfile`) is used not only as the Pipeline script to run, but also as the **marker file** - that is, the file that indicates which repositories and branches should be processed by the SCM based Pipeline job. However,  with the [CloudBees custom script project recognizer](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-as-code#custom-pac-scripts) for Mulitbranch and Org Folder Pipeline jobs, the **marker file** and the **script file** are separated, allowing you to specify an arbitrary file as the **marker file** and subsequently use an embedded Pipeline script or pull in a Pipeline file from a completely different source control repository. But in order for a GitHub `branch` to be *recognized*, the `branch` must contain the **marker file**.
9. Navigate to the top level of you `ops-controller` repository in your workshop GitHub Organization. Notice that there is no *Jenkinsfile*. ![No Jenkinsfile](no-jenkinsfile.png?width=50pc)
10. Remember, the **marker file** can be any arbitrary file, and it doesn't have to be the file with the pipeline script. We want this Org Folder Pipeline job to support CasC automation for other repositories in your GitHub Organization. So we want to use the `bundle.yaml` file as the **marker file**, so that anytime there is a repository with a `bundle.yaml` file, it will automatically keep its `main` branch in-sync and CasC bundle up to date. But before we update the job on your controller to use `bundle.yaml` as the marker file, we have to update the `items.yaml` of the CasC bundle. Otherwise, the job on your controller would be updated to use `Jenkinsfile` - we need to update it on both places only this once, and must update the value in the `items.yaml` first. Click on the `items.yaml` file and then click on the ***Edit this file*** pencil button.
11. Scroll down to line 42 and change `markerFile: Jenkinsfile` to `markerFile: bundle.yaml` and then commit directly to the `main` branch. ![Commit items.yaml](commit-items.png?width=50pc)
12. Navigate back to the `controller-casc-update` job on your Ops controller and update the **Marker file** to `bundle.yaml`, and the click the **Save** button. ![Update job config](update-job-config.png?width=50pc)
13. Once the GitHub Organization scan is complete click on the the **Status** link in the left menu and you will see a Multibranch pipeline project for your `ops-controller` repository. ![Ops controller Multibranch pipeline](ops-controller-multibranch-job.png?width=50pc)
15. Click on the `ops-controller` Multibranch pipeline project and then click on the pipeline job for the `main` branch of your `ops-controller` repository. ![Ops controller job](ops-controller-job.png?width=50pc)
16. On the **Branch main** screen, wait for the job to complete and you will see that the job fails with the following error:

```
Error from server (Forbidden): pods "cjoc-0" is forbidden: User "system:serviceaccount:controllers:jenkins" cannot get resource "pods" in API group "" in the namespace "cbci"
```

17. The reason you get this error is because your **controller** has been provisioned to the `controllers` `namespace` which is a different Kubernetes `namespace` than Operations Center and no agent `pod` in the `controllers` namespace will have the permissions to copy files with `kubectl` (a CLI tool for Kubernetes) to the Operations Center Kubernetes `pod`. To fix this, you must update the `controller-casc-update` pipeline script in your `ops-controller` repository to trigger a job (with the [CloudBees CI Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration) feature) on another controller that does have permissions to use `kubectl` to copy updated bundle files to Operations Center. 

{{% notice note %}}
Provisioning controllers and agents in a different Kubernetes `namespace` than Operations Center provides additional isolation and more security for Operations Center on Kubernetes. By default, when controllers are created in the same `namespace` as Operations Center and agents, they can provision an agent that can run the `pod` `exec` command against any other `pod` in the `namespace` - including the Operations Center's `pod`.
{{% /notice %}}

18. Navigate to your copy of the `ops-controller` repository in your workshop GitHub Organization and open the `controller-casc-update` pipeline script.
19. Click the **pencil icon** to open it in the GitHub file editor and replace the entire contents with the following and click on the **Commit changes** button to commit to the `main` branch:

```groovy
library 'pipeline-library'
pipeline {
  agent none
  options {
    timeout(time: 10, unit: 'MINUTES')
    skipDefaultCheckout()
  }
  stages {
    stage('Update Config Bundle') {
      agent { label 'default' }
      when {
        beforeAgent true
        branch 'main'
        not { triggeredBy 'UserIdCause' }
      }
      environment { CASC_UPDATE_SECRET = credentials('casc-update-secret') }
      steps {
        checkout scm
        gitHubParseOriginUrl()
        publishEvent event:jsonEvent("""
          {
            'controller':{'name':'${env.GITHUB_ORG}-${GITHUB_REPO}','action':'casc_bundle_update','bundle_id':'${env.GITHUB_ORG}-${GITHUB_REPO}'},
            'github':{'organization':'${env.GITHUB_ORG}','repository':'${GITHUB_REPO}'},
            'secret':'${CASC_UPDATE_SECRET}',
            'casc':{'auto_reload':'false'}
          }
        """), verbose: true
      }
    }
  }
}
```
Note that we replaced the previous `steps` with the `publishEvent` step (along with the `gitHubParseOriginUrl` pipeline library utility step that will provide the GitHub repository the bundle is being updated from). The `publishEvent` step with send a notification to a message bus on Operations Center and result in the triggering of any job that is configured to listen for that event. The configuration for the job that it triggers [is available here](https://github.com/cloudbees-days/cloudbees-ci-casc-bundle-update/blob/main/Jenkinsfile).

20. Navigate back to your CloudBees CI ***managed controller*** and then navigate to the ***main*** branch job of your **ops-controller** Multi-branch Project in the **controller-casc-update** Organization Folder project. After the job successfully completes, navigate to the top-level of your ***managed controller***. 
21. Click on the **Manage Jenkins** link in the left navigation menu and then click on the **CloudBees Configuration as Code export and update** configuration link. ![CloudBees Configuration config](config-bundle-system-config.png?width=50pc)
22.  On the next screen, click on the **Bundle Update** link and you should see that a new version of the configuration bundle is available. Click the **Reload Configuration** button and on the next screen click the **Yes** button to apply the updated configuration bundle. 

{{% notice note %}}
If you don't see the new version available then click the **Check for Updates** button. Also, once you click **Yes** it may take a few minutes for the bundle update to reload.
{{% /notice %}}
![Bundle Update](new-bundle-available.png?width=50pc)
23. Navigate to the `controller-jobs` folder and click on **New Item** in the left menu and note that the **Freestyle** job type is not available. ![No freestyle job](no-freestyle-job.png?width=50pc)

## Auto-Updating with the CloudBees CI CasC HTTP API

Although we have enabled GitOps to automatically update your CasC bundle on Operations Center whenever there is a commit to the `main` branch of your `ops-controller` repository, checking for and applying the bundle updates on your controller is still a manual process. CloudBees CI CasC provides [HTTP API endpoints](https://docs.cloudbees.com/docs/cloudbees-ci-api/latest/bundle-management-api) (and a CLI) for managing CasC bundles, to include endpoints to check for controller bundle updates and reloading a controller bundle:

- GET `${JENKINS_URL}/casc-bundle-mgnt/check-bundle-update`
- POST `${JENKINS_URL}/casc-bundle-mgnt/reload-bundle`

The pipeline snippet below is used by the *bundle update* job, triggered by your **controller-casc-update ops-controller** `main` branch job, to check for a bundle update and then reload the bundle for your controller:

```groovy
        stage('Auto Reload Bundle') {
          when {
            environment name: 'AUTO_RELOAD', value: "true"
          }
          steps {
            echo "begin config bundle reload"
            withCredentials([usernamePassword(credentialsId: 'admin-cli-token', usernameVariable: 'JENKINS_CLI_USR', passwordVariable: 'JENKINS_CLI_PSW')]) {
                sh '''
                  curl --user $JENKINS_CLI_USR:$JENKINS_CLI_PSW -XGET http://${BUNDLE_ID}.controllers.svc.cluster.local/${BUNDLE_ID}/casc-bundle-mgnt/check-bundle-update 
                  curl --user $JENKINS_CLI_USR:$JENKINS_CLI_PSW -XPOST http://${BUNDLE_ID}.controllers.svc.cluster.local/${BUNDLE_ID}/casc-bundle-mgnt/reload-bundle
                '''
            }
          }
        }
```

So, all you have to do to enable automatic reloading is update the value of the `casc.auto_reload` portion of the event payload to `true`:

1. Navigate to your copy of the `ops-controller` repository in your workshop GitHub Organization and open the `controller-casc-update` pipeline script.
2. Click the **pencil icon** to open it in the GitHub file editor, then modify `'casc':{'auto_reload':'true'}` to `'casc':{'auto_reload':'false'}` and click on the **Commit changes** button to commit to the `main` branch. The complete updated contents should match the following:

```groovy
library 'pipeline-library'
pipeline {
  agent none
  options {
    timeout(time: 10, unit: 'MINUTES')
    skipDefaultCheckout()
  }
  stages {
    stage('Update Config Bundle') {
      agent { label 'default' }
      when {
        beforeAgent true
        branch 'main'
        not { triggeredBy 'UserIdCause' }
      }
      environment { CASC_UPDATE_SECRET = credentials('casc-update-secret') }
      steps {
        gitHubParseOriginUrl()
        publishEvent event:jsonEvent("""
          {
            'controller':{'name':'${env.GITHUB_ORG}-${GITHUB_REPO}','action':'casc_bundle_update','bundle_id':'${env.GITHUB_ORG}-${GITHUB_REPO}'},
            'github':{'organization':'${env.GITHUB_ORG}','repository':'${GITHUB_REPO}'},
            'secret':'${CASC_UPDATE_SECRET}',
            'casc':{'auto_reload':'true'}
          }
        """), verbose: true
      }
    }
  }
}
```

3. Now, the next time you update any of the bundle files on the `main` branch of your `ops-controller` repository, the changes will be automatically applied to your controller.

