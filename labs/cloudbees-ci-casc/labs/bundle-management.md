---
title: "CloudBees CI Configuration Bundle Management"
chapter: false
weight: 3
--- 

CloudBees CI configuration bundles are centrally managed and stored in the `jcasc-bundles-store` directory in the Operations Center Jenkins home directory. In order to make a bundle available for a controller or to update an existing bundle the bundle files must be copied to the `jcasc-bundles-store` directory.

>NOTE: While Operations Center simplifies the management of bundles, it is possible to configure a controller with a bundle without Operations Center using the `-Dcore.casc.config.bundle=/path/to/casc-bundle` Java system property.

The labs in this section will explore:

- storing configuration bundles on Operations Center
- setting a default bundle
- using the CasC HTTP API with GitOps for CloudBees CI configuration bundles

## Managing Configuration Bundles on Operations Center

This lab will provide an overview of how configuration bundles are managed via the Operations Center UI and how to manually apply a configuration bundle to a controller. The first part of the overview will be on the Operations Center **Configuration as Code bundles** settings page that attendees don't have access. Therefore the first part of this lab will explore the 3 major components on the Operations Center **Configuration as Code bundles** settings page without attendees following along.

![Operations Center Configuration as Code bundles settings pag](ops-center-config-bundle-settings.png?width=50pc)

1. By checking the **Availability pattern** checkbox, any configuration bundle that has an empty **Availability pattern** can be used by any controller.
2. The **Default bundle** drop-down allows you to automatically apply a default configuration bundle to any controller that does not specify a different configuration bundle. However, the **Availability pattern** checkbox must be checked for this feature to work.
3. The configuration bundle **Availability pattern** allows assigning regular expressions that must match the full path to one or more controllers in order to use that bundle. For the `base` bundle the **Availability pattern** is empty and this typically would not match any path, but since the **Availability pattern** checkbox is checked it is available to all controllers.
4. For the `ops` bundle the **Availability pattern** is set to `operations/ops` so that means only a controller with the name **ops** in the **operations** folder can use this bundle. If the **Availability pattern** were set to `operations/*` then any controller in the **operations** folder could use this bundle.
5. To actually apply a bundle to a controller you must select the bundle from the **Bundle** drop-down on the controller configuration page. To do this navigate to the top level of Operations Center and click on the **Manage** icon for your Ops controller. ![Manage controller link](manage-controller-link.png?width=50pc)
6. On the controller manage screen click on the **Configure** link in the left menu. ![Configure controller link](configure-controller-link.png?width=50pc)
7. On the configure controller screen, scroll down to the **Configuration as Code (CasC)** section and expand the **Bundle** drop down. ![Bundle dropdown](bundle-dropdown.png?width=50pc)
8. Note that the bundle matching the name of your Ops controller is selected and the `base` bundle is also available, but the `ops` bundle is not available to select. ![Bundle dropdown expanded](bundle-dropdown-expanded.png?width=50pc)
9. We do not actually need to change the configured bundle so just click on the breadcrumb link for your Ops controller to exit from the controller configuration page. ![Controller breadcrumb link](controller-breadcrumb-link.png?width=50pc)

## GitOps for CloudBees CI Configuration Bundles

In this lab we will create a Jenkins Pipeline to automatically update our controllers' configuration bundles whenever any changes are committed.
 
1. Navigate to the `configuration-bundles` repository in your workshop GitHub Organization.
2. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
3. On the next screen name the new file `Jenkinsfile` and enter the following contents:
```yaml
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
        not { triggeredBy 'UserIdCause' }
      }
      steps {
        container("kubectl") {
          sh "mkdir -p ${BRANCH_NAME}"
          sh "cp *.yaml ${BRANCH_NAME}"
          sh "kubectl cp --namespace sda ${BRANCH_NAME} cjoc-0:/var/jenkins_home/jcasc-bundles-store/ -c jenkins"
        }
      }
    }
  }
}
```
4. On the first line you will see that we are using the Pipeline shared library defined in your Ops controller configuration bundle. The Pipeline shared library contains a number of Jenkins Kubernetes Pod templates that can be leveraged across all the controllers. We are utilizing the `kubectl.yml` Pod template so we can use the `kubectl cp` command to copy the Ops controller configuration bundle files into the `jcasc-bundles-store` directory on Operations Center. Once you have finished reviewing the `Jenkinsfile` contents, commit directly to your Ops controller branch. ![Commit Jenkinsfile](commit-jenkinsfile.png?width=50pc)
5. Navigate to the top-level of your Ops controller and click the **Create a job** link. ![Create job link](create-job-link.png?width=50pc)
6. Name the project **configuration-bundles**, select **Mulitbranch Pipeline** as the project type and click the **OK** button.
7. On the Multibranch project configuration page enter the url for your copy of the **configuration-bundles** repository in your workshop GitHub Organization, select the GitHub App credential and then click the **Save** button.