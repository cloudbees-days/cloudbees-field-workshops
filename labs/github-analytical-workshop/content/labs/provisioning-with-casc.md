---
title: "Provisioning Controllers with CloudBees CI Configuration Bundles"
chapter: false
weight: 5
--- 

The parent `base` bundle we explored in the previous lab is also configured to be the default bundle for all managed controllers that do not specify a bundle. This allows you to easily manage configuration across all of your organization's managed controllers, but it does not allow for any variations in configuration bundles between controllers. Also, the number of manual steps to provision a managed controller, and apply controller specific bundles across numerous controllers, wastes time and is prone to configuration errors. Imagine if you had dozens or even hundreds of controllers (like we do in this workshop), things would quickly become very difficult to manage.

In this lab we will explore a GitOps approach for automating the process of provisioning a controller, to include automating the configuration and assignment of a controller specific configuration bundle. This approach is based on individual repositories representing individual controllers, and takes advantage of the Jenkins GitHub Organization project type and CloudBees CI custom marker file like we used earlier. After we add a new `controller-provision` GitHub Organization folder job to your `ops-controller`, a new controller will be provisioned any time you add a new GitHub repository with a `controller.yaml` file to your workshop GitHub Organization. The managed controller will be provisioned with the configuration bundle from that new GitHub repository (one other approach may be to use folders in one repository to represent each controller).

{{% notice note %}}
If we wanted to use an **SCM** CasC storage service for your controllers' bundles then we would have to either add everyone's bundles to one branch of one repository or add an additional **SCM** *external* storage configuration to Operations Center for every controller.
{{% /notice %}}

## GitOps for Controller Provisioning with CloudBees CI Configuration Bundles

We will be using CasC for Operations Center and CasC HTTP API endpoints to dynamically provision controllers using the `controller.yaml` file and bundle files from your controller repository.  For the purposes of the shared workshop environment we will be running the provisioning job from the workshop Ops controller and will leverage [CloudBees CI Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration), triggering the job with the required payload from your Ops controller.

### Review the Jenkins declarative pipeline job that will be triggered by your Ops controller on the workshop Ops controller using CloudBees CI Cross Team Collaboration. 
```groovy
def event = currentBuild.getBuildCauses()[0].event
library 'pipeline-library'
pipeline {
  agent none
  environment {
    OPS_PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret')
    CONTROLLER_PROVISION_SECRET = event.secret.toString()
  }
  options { timeout(time: 10, unit: 'MINUTES') }
  triggers {
    eventTrigger jmespathQuery("controller.action=='provision'")
  }
  stages {
    stage('Provision Managed Controller') {
      agent {
        kubernetes {
          yaml libraryResource ('podtemplates/kubectl.yml')
        }
      }
      environment {
        ADMIN_CLI_TOKEN = credentials('admin-cli-token')
        WORKSHOP_ID="cloudbees-ci-casc-workshop"
        GITHUB_ORGANIZATION = event.github.organization.toString().replaceAll(" ", "-")
        GITHUB_REPOSITORY = event.github.repository.toString().toLowerCase()
        CONTROLLER_FOLDER = GITHUB_ORGANIZATION.toLowerCase()
        BUNDLE_ID = "${CONTROLLER_FOLDER}-${GITHUB_REPOSITORY}"
        AVAILABILITY_PATTERN = "${WORKSHOP_ID}/${GITHUB_ORGANIZATION}/${GITHUB_REPOSITORY}"
      }
      when {
        triggeredBy 'EventTriggerCause'
        environment name: 'CONTROLLER_PROVISION_SECRET', value: OPS_PROVISION_SECRET
      }
      steps {
        container("kubectl") {
          sh '''
            rm -rf ./${BUNDLE_ID} || true
            rm -rf ./checkout || true
            mkdir -p ${BUNDLE_ID}
            mkdir -p checkout
            git clone https://github.com/${GITHUB_ORGANIZATION}/${GITHUB_REPOSITORY}.git checkout
          '''
          dir('checkout/bundle') {
            sh '''
              cp --parents `find -name \\*.yaml*` ../../${BUNDLE_ID}//
            '''
          }
          sh '''
            ls -la ${BUNDLE_ID}
            kubectl cp --namespace cbci ${BUNDLE_ID} cjoc-0:/var/jenkins_config/jcasc-bundles-store/ -c jenkins
          '''
        }
        sh '''
          curl --user "$ADMIN_CLI_TOKEN_USR:$ADMIN_CLI_TOKEN_PSW" -XPOST \
            http://cjoc/cjoc/load-casc-bundles/checkout
          curl --user "$ADMIN_CLI_TOKEN_USR:$ADMIN_CLI_TOKEN_PSW" -XPOST \
            http://cjoc/cjoc/casc-items/create-items?path=/$WORKSHOP_ID \
            --data-binary @./controller.yaml -H 'Content-Type:text/yaml'
        '''
      }
    }
  }
}
```
1. The first step is to get the event payload and assign it to a global variable available to the rest of the `pipeline`: `def event = currentBuild.getBuildCauses()[0].event`. We do this outside of the declarative `pipeline` block because you cannot assign objects to variables in declarative pipeline and we need the values before we can execute a `script` block in a `stage`.
2. There is no `agent` at the global level as it would result in the unnecessary provisioning of an agent if the `when` conditions are not met.
3. An `eventTrigger` is configured to only match a JSON payload containing `controller.action=='provision'`. We wil come back to this when we update the `controller-casc-update` pipeline for your Ops controller.
4. An agent is defined for the **Provision Managed Controller** `stage` as the `sh` steps require a normal (some times referred to as heavy-weight) executor (meaning it must be run on an agent since all managed controllers our configured with 0 executors): `agent { label 'default-jnlp' }`
5. The declarative `environment` directive is used to capture values published by the Cross Team Collaboration `event`, to retrieve the controller provisioning secret value from the workshop Ops controller and to retrieve the Operations Center admin API token credential.
6. Multiple `when` conditions are configured so the **Provision Managed Controller** `stage` will only run if the job is triggered by an `EventTriggerCause` and if the `PROVISION_SECRET` matches the event payload secret.
7. The `kubectl` CLI tool is used to copy CasC bundle files to Operations Center **Local folder** we have configured.
8. Finally, the `curl` command is used to post the contents of the `controller.yaml` file to the `/casc-items/create-items` CloudBees CI CasC HTTP API endpoint which will result in the provisioning of a managed controller.

### Create Ops controller Job to Trigger Provisioning
Now that we have reviewed the pipeline script for the workshop provisioning of managed controllers, we need to create a new GitHub Organization Folder project that will publish a Cross Team Collaboration event to trigger that pipeline.

1. Navigate to your `ops-controller` repository in your workshop GitHub Organization, click on the **Pull requests** link and click on the **Bundle Provision** pull request. ![Provision PR link](provision-pr-link.png?width=50pc) 
2. Next, click on the **Files changed** tab to review the configuration changes. First, click on the `items.yaml` file and note the new `organizationFolder` item using `controller.yaml` as the `marker` and the `controller-provision` Declarative Pipeline script. 
3. Next, click on the `credentials.yaml` file and note the we are adding a new `restrictedSystem` credential with an `id` of `casc-workshop-controller-provision-secret` that matches the id used in the `controller-provision` Declarative Pipeline script below. ![Restricted credential](restricted-credential.png?width=50pc)
4. Finally, let's take a look at the new file `controller-provision`. Notice that the `controller-provision` Declarative Pipeline script is loading the `credential` with an id of `casc-workshop-controller-provision-secret` that was added to the `credentials.yaml` above and is using the `publishEvent` to publish an event that will trigger the workshops Ops controller job we reviewed above.

```groovy
library 'pipeline-library'
pipeline {
  agent any
  options {
    timeout(time: 10, unit: 'MINUTES')
  }
  stages {
    stage('Publish Provision Controller Event') {
      when {
        branch 'main'
      }
      environment { PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret') }
      steps {
        gitHubParseOriginUrl()
        publishEvent event:jsonEvent("""
          {'controller':{'name':'${GITHUB_REPO}','action':'provision'},'github':{'organization':'${GITHUB_ORG}','repository':'${GITHUB_REPO}','user':'${GITHUB_USER}'},'secret':'${PROVISION_SECRET}'}
        """), verbose: true
      }
    }
  }
}
```
5. Once you have finished reviewing the changes, click on the **Conversation** tab of the **Bundle Provision** pull request, scroll down and click the green **Merge pull request** button and then click the **Confirm merge** button.
6. Navigate to the `main` branch job of the `controller-casc-update` `ops-controller` Multibranch pipeline project on your Ops controller. ![ops-controller Mulitbranch](ops-controller-multibranch-jcasc.png?width=50pc)
7. After the the `main` branch job has completed successfully, navigate to the `controller-jobs` folder and refresh the page until the `controller-provision` job appears. ![controller-provision-job](controller-provision-job.png?width=50pc)

### Create a new managed controller repository
In the previous section you added the `controller-provision` Organization Folder job to your Ops controller to publish an event to trigger the provisioning of a managed controller. Now you will trigger the provisioning of a new managed controller by adding a `controller.yaml` file (and a simple CasC bundle) to the `main` branch of your copy of the `dev-controller` repository in your workshop GitHub Organization.

1. Navigate to your copy of the `dev-controller` repository in GitHub, click on the **Pull requests** tab and then click on the link for the **Provision Controller** pull request. ![Provision Controller PR link](provision-controller-pr-link.png?width=50pc)
2. On the next screen, click on the **Files changed** tab to review the `bundle/bundle.yaml` and `controller.yaml` files being added to your `dev-controller` repository. Note that the `bundle/bundle.yaml` file does include any other configuration files but it does specify `parent: base`. ![files changed](provision-controller-files-changed.png?width=50pc)
3. Once you have reviewed the changed files, click on the **Conversation** tab, scroll down and click the green **Merge pull request** button and then the **Confirm merge** button.
4. Next, navigate to the top level of your Ops controller, click the on the `controller-jobs` folder and then click on the `controller-provision` job. There should now be a `dev-controller` folder under the `controller-provision` job for your `dev-controller` repository. ![dev-controller job](dev-controller-job.png?width=50pc)
5. Navigate to the `main` branch of the **dev-controller** Multi-branch pipeline job on your Ops controller and click on the **Build Now** link in the left menu. Once the job completes you should see an **Event JSON** in the build logs similar to the one below (of course the GitHub information will be unique to you). ![Event JSON log output](event-json-log-output.png?width=50pc)
6. A few minutes after the **dev-controller** **main** branch job completes you will have a new managed controller named **dev-controller** in the same folder as your Ops controller. ![New dev-controller](new-dev-controller.png?width=50pc)
