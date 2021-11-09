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

- storing configuration bundles on Operations Center
- setting a default configuration bundle
- setting up GitOps for automating CloudBees CI configuration bundle updates

## Managing Configuration Bundles on Operations Center

This lab will provide an overview of how configuration bundles are managed via the Operations Center UI and how to manually apply a configuration bundle to a controller. The first part of the overview will be on the Operations Center **Configuration as Code bundles** settings page that is only accessible by workshop instructors. Therefore the first part of this lab will explore the 3 major components on the Operations Center **Configuration as Code bundles** settings page without attendees following along.

![Operations Center Configuration as Code bundles settings pag](ops-center-config-bundle-settings.png?width=70pc)

1. By checking the **Availability pattern** checkbox, any configuration bundle that has an empty **Availability pattern** can be used by any controller.
2. The **Default bundle** drop-down allows you to automatically apply a default configuration bundle to any controller that does not specify a different configuration bundle. However, the **Availability pattern** checkbox must be checked for this feature to work.
3. The **cog** icon signifies that the bundle's availability pattern has been defined in the UI, to include overriding availability patterns set in the `bundle.yaml`.
4. The **bundle** icon signifies that the availability pattern was set in the `bundle.yaml` via the `availabilityPattern` field. Note that setting the **Availability pattern**  with the `availabilityPattern` field allows managing this value with each individual bundle rather than having to specify it in the UI.
5. The configuration bundle **Availability pattern** allows assigning regular expressions that must match the full path to one or more controllers in order to use that bundle. For the `base` bundle the **Availability pattern** is empty and this typically would not match any path, but since the **Availability pattern** checkbox is checked it is available to all controllers.
6. For the `ops` bundle the **Availability pattern** is set to `operations/ops` so that means only a controller with the name **ops** in the **operations** folder can use this bundle. If the **Availability pattern** were set to `operations/*` then any controller in the **operations** folder could use this bundle.

### Applying Bundles to Controllers
1. To actually apply a bundle to a controller you must select the bundle from the **Bundle** drop-down on the controller configuration page. To do this navigate to the top level of Operations Center and click on the **Manage** icon for your Ops controller. ![Manage controller link](manage-controller-link.png?width=60pc)
2. On the controller manage screen click on the **Configure** link in the left menu. ![Configure controller link](configure-controller-link.png?width=50pc)
3. On the configure controller screen, scroll down to the **Configuration as Code (CasC)** section and expand the **Bundle** drop down. ![Bundle dropdown](bundle-dropdown.png?width=50pc)
4. Note that the bundle matching the name of your Ops controller is selected and the `base` bundle is also available, but the `ops` bundle is not available to select. ![Bundle dropdown expanded](bundle-dropdown-expanded.png?width=50pc)
5. We do not actually need to change the configured bundle so just click on the breadcrumb link for your Ops controller to exit from the controller configuration page. ![Controller breadcrumb link](controller-breadcrumb-link.png?width=50pc)

## GitOps for CloudBees CI Configuration Bundles

In this lab we will update the `cbci-casc-automation` job (created by CasC) to automatically update our controllers' configuration bundles whenever any changes are committed to the GitHub `main` branch for the controller's configuration bundle. The `cbci-casc-automation` job is acutally [GitHub Organization Folder project](https://www.jenkins.io/doc/book/pipeline/multibranch/#organization-folders) with a [custom marker file](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-as-code#custom-pac-scripts). Instead of using the typical `Jenkinsfile` we will use `bundle.yaml` as our custom marker file. By using the custom marker file with a GitHub Organization Folder project, a Multibranch Pipeline project will automatically be created for all repositories in your workshop GitHub Organization when they have at least one branch containing a `bundle.yaml` file.
 
1. Navigate to the `ops-controller` repository in your workshop GitHub Organization.
2. Next click on the`cbci-casc-automation`file to open it. It will match the contents of the file below. ![Open pipeline file](open-pipeline-file.png?width=50pc)
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
        echo "begin config bundle reload"
        script {
          try {
            withCredentials([usernamePassword(credentialsId: 'admin-cli-token', usernameVariable: 'JENKINS_CLI_USR', passwordVariable: 'JENKINS_CLI_PSW')]) {
                sh '''
                  curl --user $JENKINS_CLI_USR:$JENKINS_CLI_PSW -XGET http://${GITHUB_ORG}-${GITHUB_REPO}/${GITHUB_ORG}-${GITHUB_REPO}/casc-bundle-mgnt/check-bundle-update 
                  curl --user $JENKINS_CLI_USR:$JENKINS_CLI_PSW -XPOST http://${GITHUB_ORG}-${GITHUB_REPO}/${GITHUB_ORG}-${GITHUB_REPO}/reload-bundle/
                '''
            }
          } catch (Exception e) {
              echo 'Exception occurred: ' + e.toString()
          }
        }
      }
    }
  }
}
```
4. On the first line you will see that we are using the Pipeline shared library defined in your Ops controller configuration bundle. The Pipeline shared library contains a number of Jenkins Kubernetes Pod templates that can be leveraged across all the controllers. We are utilizing the `kubectl.yml` Pod template, so we can use the `kubectl cp` command to copy your `ops-controller` configuration bundle files into the `jcasc-bundles-store` directory on Operations Center. Finally, we use the [CasC HTTP API](https://docs.cloudbees.com/docs/cloudbees-ci-api/latest/bundle-management-api) to check for an update and then automatically reload the bundle as long as it can be reloaded without a restart of the controller. Once you have finished reviewing the `controller-casc-automation` pipeline contents, navigate to the top level of your Ops controller and click the on the `controller-jobs` folder.

{{% notice info %}}
In a production environment we recommend placing Operations Center and the Ops Controller in the same Kubernetes `namespace`, and isolating all managed controllers in one or more other Kubernetes `namespaces`.
{{% /notice %}}

5. Inside of the `controller-jobs` folder, click on the `cbic-casc-automation` job. ![CasC job link](casc-job-link.png?width=50pc)
6. On the next screen, you will see **This folder is empty**. The reason it is empty is because the GitHub Folder branch scan did not find any matches. Click on the **Configure** link in the left menu so we can fix that.  ![CasC job config link](casc-job-config-link.png?width=50pc)
7. Scroll down to the **Project Recognizers** section and under **Custom script** notice how the **Marker file** is configured. ![Wrong marker file](wrong-marker-file.png?width=50pc)
8. With the regular **project recognizer** the file you specify (usually `Jenkinsfile`) is used not only the the Pipeline script to run, but also as the **marker file** - that is, the file that indicates which repositories and branches should be processed by the Pipeline job. However,  with the CloudBees **custom script** project recognizer for Mulitbranch and Org Folder Pipeline jobs, the **marker file** and the **script file** are separated, allow you to specify an arbitrary file as the **marker file** and subsequently use an embedded Pipeline script or pull in a Pipeline file from a completely different source control repository. So, in order for a GitHub `branch` to be *recognized*, the `branch` must contain the **marker file**.
9. Navigate to the top level of you `ops-controller` repository in your workshop GitHub Organization. Notice that there is no Jenkinsfile. ![No Jenkinsfile](no-jenkinsfile.png?width=50pc)
10. But remember, the **marker file** can be an file, and we want this Org Folder Pipeline job to support CasC automation for other repository in your GitHub Organization. So we want to use the `bundle.yaml` file as the **marker file**, so that anytime there is a repository with a `bundle.yaml` file it will automatically keep its `main` branch in-sync. But before we update the job on your controller to use `bundle.yaml` as the marker file, we have to update the `items.yaml`. Otherwise the job on your controller would updated to use `Jenkinsfile` - we need to update it on both places only this once, and must update the value in the `items.yaml` first. Click on the `items.yaml` file and then click on the ***Edit this file*** pencil button.
11. Scroll down to line 27 and change `markerFile: Jenkinsfile` to `markerFile: bundle.yaml` and then commit directly to the `main` branch. ![Commit items.yaml](commit-items.png?width=50pc)
12. Navigate back to the `cbic-casc-automation` job on your Ops controller and update the **Marker file** to `bundle.yaml` and the click the **Save** button. ![Update job config](update-job-config.png?width=50pc)
14. Once the GitHub Organization scan is complete click on the the **Status** link in the left menu and you will see a Multibranch pipeline project for your `ops-controller` repository. ![Ops controller Multibranch pipeline](ops-controller-multibranch-job.png?width=50pc)
15. Click on the `ops-controller` Multibranch pipeline project and then click on the pipeline job for the `main` branch of your `ops-controller` repository. ![Ops controller job](ops-controller-job.png?width=50pc)
16. On the **Branch main** screen wait for the job to complete. ![Ops controller main branch job](ops-controller-main-branch-job.png?width=50pc)
17. After the job has completed successfully, navigate to the top level of your Ops controller.

