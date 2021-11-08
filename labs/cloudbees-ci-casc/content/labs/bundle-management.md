---
title: "CloudBees CI Configuration Bundle Management"
chapter: false
weight: 3
--- 

CloudBees CI configuration bundles are centrally managed and stored in the `jcasc-bundles-store` directory in the Operations Center Jenkins home directory. In order to make a bundle available for a controller or to update an existing bundle the bundle files must be copied to the `jcasc-bundles-store` directory.

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

In this lab we will create a Jenkins Pipeline to automatically update our controllers' configuration bundles whenever any changes are committed to the GitHub branch for the controller's configuration bundle. We will actually be creating a [GitHub Organization Folder project](https://www.jenkins.io/doc/book/pipeline/multibranch/#organization-folders) with a [custom marker file](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-as-code#custom-pac-scripts). Instead of using the typical `Jenkinsfile` we will use `bundle.yaml` as our custom marker file. By using the custom marker file with a GitHub Organization Folder project, a Multibranch Pipeline project will automatically be created for all repositories in your workshop GitHub Organization when they have at least one branch containing a `bundle.yaml` file.
 
1. Navigate to the `ops-controller` repository in your workshop GitHub Organization.
2. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
3. On the next screen name the new file `controller-casc-automation` and enter the following contents:
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
        sh "curl -O https://raw.githubusercontent.com/cloudbees-days/ops-workshop-setup/master/groovy/reload-casc.groovy"
        sh "curl -O http://${GITHUB_ORG}-${GITHUB_REPO}/${GITHUB_ORG}-${GITHUB_REPO}/jnlpJars/jenkins-cli.jar"
        withCredentials([usernamePassword(credentialsId: 'admin-cli-token', usernameVariable: 'JENKINS_CLI_USR', passwordVariable: 'JENKINS_CLI_PSW')]) {
            sh """
              alias cli='java -jar jenkins-cli.jar -s http://${GITHUB_ORG}-${GITHUB_REPO}/${GITHUB_ORG}-${GITHUB_REPO}/ -auth $JENKINS_CLI_USR:$JENKINS_CLI_PSW'
              cli casc-bundle-check-bundle-update
              cli casc-bundle-reload-bundle
            """
        }
      }
    }
  }
}
```
4. On the first line you will see that we are using the Pipeline shared library defined in your Ops controller configuration bundle. The Pipeline shared library contains a number of Jenkins Kubernetes Pod templates that can be leveraged across all the controllers. We are utilizing the `kubectl.yml` Pod template so we can use the `kubectl cp` command to copy your `ops-controller` configuration bundle files into the `jcasc-bundles-store` directory on Operations Center. Finally, we use a the [CasC CLI](https://docs.cloudbees.com/docs/admin-resources/latest/cli-guide/casc-bundle-management) `casc-bundle-reload-bundle` command  to automatically reload the bundle as long as it can be reloaded without a restart of the controller. Once you have finished reviewing the `controller-casc-automation` pipeline contents, commit directly to the main branch of your Ops controller repository. ![Commit Jenkinsfile](commit-jenkinsfile.png?width=50pc)

{{% notice info %}}
In a production environment we recommend placing Operations Center and the Ops Controller in the same Kubernetes `namespace`, and isolating all managed controllers in one or more other Kubernetes `namespaces`.
{{% /notice %}}

5. Navigate to the top level of your Ops controller and click the **Create a job** link. ![Create job link](create-job-link.png?width=50pc)
6. Name the project `cbci-casc-automation`, select **GitHub Organization** as the project type and then click the **OK** button. ![Create job](create-job.png?width=50pc)
7. On the GitHub Organization project configuration page, under **Projects** click on the **Add** button and then select **GitHub Organization**. ![Select Source](select-source.png?width=50pc)
8. **Projects** tab and select ***CloudBees CI CasC Workshop GitHub App credential*** for the **Credentials** value. Note that the **Owner** input should match your workshop GitHub Organization name. In the screenshot below, the workshop GitHub Organization is `cbci-casc-workshop` but yours will be different. Leaving the **API endpoint** field empty will default to ***https://api.github.com***, which is what we want. ![Select GitHub App credentials](select-credentials.png?width=50pc)
8. Next, scroll down to the **Project Recognizers** section and delete the **Pipeline Jenkinsfile** project recognizer. Then click the **Add** button and select **Custom script** as the project recognizer. ![Delete Jenkinsfile project recognizer](delete-project-recognizer.png?width=50pc)
9. For the **Custom script** configuration enter `bundle.yaml` as the **Marker file** so pipeline jobs will only be created for repository branches with a `bundle.yaml` file. ![Custom script config](custom-script-config.png?width=50pc)
10. For the **Definition** of the **Pipeline** select ***Pipeline script from SCM*** and then select ***Git*** as the **SCM**
11. Enter the URL for your copy of the `ops-controller` repository in your workshop GitHub Organization as the **Repository URL** and select ***CloudBees CI CasC Workshop GitHub App credential*** for the **Credentials**. 

{{% notice tip %}}
If you navigate to your GitHub `ops-controller` repository in your workshop GitHub Organization, and click on the Code button, you can then click on the clipboard icon to copy the Git URL for your repository. ![GitHub copy repo url](github-copy-repo-url.png?width=50pc)
{{% /notice %}}

12. Under **Branches to build** change ***master*** to ***main*** for the **Branch Specifier**. 
13. For the **Script Path** replace `Jenkinsfile` with `controller-casc-automation`. All of the rest of the default values are fine, so click the **Save** button.
14. Once the GitHub Organization scan is complete click on the the **Status** link in the left menu and you will see a Multibranch pipeline project for your `ops-controller` repository. ![Ops controller Multibranch pipeline](ops-controller-multibranch-job.png?width=50pc)
15. Click on the `ops-controller` Multibranch pipeline project and then click on the pipeline job for the `main` branch of your `ops-controller` repository. ![Ops controller job](ops-controller-job.png?width=50pc)
16. On the **Branch main** screen wait for the job to complete. ![Ops controller main branch job](ops-controller-main-branch-job.png?width=50pc)
17. After the job has completed successfully, navigate to the top level of your Ops controller and you will see that the **controller-jobs** folder has been added back. ![CasC bundle updated](casc-bundle-updated.png?width=50pc)
18. Besides being an example of configuration bundle `items` configuration, another reason we created a folder is because it is considered a best practice to keep all of your Jenkins jobs organized with folders - some of the advantages of folders include fine grained access control and credentials, folder specific environment variables, the ability to restrict job types that can be create and easily moving or copying jobs across controllers. Therefore we will move your GitHub Organization project into the **controller-jobs** folder. To do so, click on your GitHub Organization project and then click the **Move/Copy/Promote** link in the left menu. ![Move multibranch job](move-github-org-job.png?width=50pc)
19. On the **Move/Copy/Promote** place your mouse cursor in the **Destination** select box next to **ops-controller**, select **controller-jobs** from the drop down and then click the **Move** button. ![Select folder and move](select-folder-move.png?width=50pc)
20. Once the move has completed successfully click on the **Close** button. ![Move close](move-close.png?width=50pc)

