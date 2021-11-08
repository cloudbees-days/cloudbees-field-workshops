---
title: "Provisioning Controllers with CloudBees CI Configuration Bundles"
chapter: false
weight: 5
--- 

The parent `base` bundle we explored in the previous lab is also configured to be the default bundle for all managed controllers that do not specify one. This allows you to easily manage configuration across all of your organization's managed controllers, but it does not allow for any variations in configuration bundles between controllers. Also, the number of manual steps to provision a managed controller, and apply controller specific bundles to numerous controllers, wastes time and is prone to configuration errors. Imagine if you had dozens or even hundreds of controllers (like we do in this workshop), things would quickly become very difficult to manage.

In this lab we will explore a GitOps approach for automating the process of provisioning a controller to include automating the configuration and application of a controller specific configuration bundle. This approach is based on individual repositories representing individual controllers, and takes advantage of the Jenkins GitHub Organization project type and CloudBees CI custom marker file we setup earlier. After we are done updating the `controller-casc-automation` Jenkins pipeline script in our copy of the `ops-controller` repository, a new controller will be provisioned any time you add a new GitHub repository with a `bundle.yaml` file to your workshop GitHub Organization. The managed controller will have the same name as the repository and will be provisioned with the configuration bundle from the associated GitHub repository (one other approach may be to use folders in one repository to represent each controller).

{{% notice note %}}
Another GitOps type approach you may be interested in is using CloudBees CI CasC for CloudBees CI Cloud Operations Center which allows you define individual managed controllers as `items`. However, as of the `2.303.3.3` release, the managed controllers are not automatically provisioned when the bundle is loaded but will be available in a future version of CloudBees CI on Kubernetes.
{{% /notice %}}

## GitOps for Controller Provisioning with CloudBees CI Configuration Bundles

Currently, automatic and dynamic provisioning of a managed controller requires running a Groovy script on CloudBees CI Operations Center. This can easily be done from a Jenkins Pipeline by leveraging the Jenkins CLI and an administrator Jenkins API token. However, for the purposes of the shared workshop environment we will be running the provisioning job from the workshop Ops controller and will leverage [CloudBees CI Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration), triggering the job with the required payload from your Ops controller.

### Review the Jenkins declarative pipeline job that will be triggered by your Ops controller on the workshop Ops controller using CloudBees CI Cross Team Collaboration. 
```groovy
def event = currentBuild.getBuildCauses()[0].event
pipeline {
  agent none
  environment {
    PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret')
    PUBLISHED_SECRET = event.secret.toString()
  }
  options { timeout(time: 10, unit: 'MINUTES') }
  triggers {
    eventTrigger jmespathQuery("controller.action=='provision'")
  }
  stages {
    stage('Provision Managed Controller') {
      agent  { label 'default-jnlp' }
      environment {
        ADMIN_CLI_TOKEN = credentials('admin-cli-token')
        GITHUB_ORGANIZATION = event.github.organization.toString().replaceAll(" ", "-")
        GITHUB_REPOSITORY = event.github.repository.toString().toLowerCase()
        GITHUB_USER = event.github.user.toString().toLowerCase()
        CONTROLLER_FOLDER = GITHUB_ORGANIZATION.toLowerCase()
        BUNDLE_ID = "${CONTROLLER_FOLDER}-${GITHUB_REPOSITORY}"
        AVAILABILITY_PATTERN = "${GITHUB_ORGANIZATION}/${GITHUB_REPOSITORY}"
      }
      when {
        triggeredBy 'EventTriggerCause'
        environment name: 'PUBLISHED_SECRET', value: PROVISION_SECRET
      }
      steps {
        sh '''
          curl -O http://cjoc/cjoc/jnlpJars/jenkins-cli.jar
          alias cli='java -jar jenkins-cli.jar -s http://cjoc/cjoc/ -webSocket -auth $ADMIN_CLI_TOKEN_USR:$ADMIN_CLI_TOKEN_PSW'
          cli casc-bundle-set-availability-pattern --bundle-id $BUNDLE_ID --availability-pattern $AVAILABILITY_PATTERN
          cli groovy =<casc-workshop-provision-controller-with-casc.groovy $GITHUB_ORGANIZATION $GITHUB_USER $GITHUB_REPOSITORY $CONTROLLER_FOLDER
        '''
      }
    }
  }
}
```
1. The first step is to get the event payload and assign it to a global variable available to the rest of the `pipeline`: `def event = currentBuild.getBuildCauses()[0].event`. We do this outside of the declarative `pipeline` block because you cannot assign objects to variables in declarative pipeline and we need the values before we can execute a `script` block in a `stage`.
2. There is no `agent` at the global level as it would result in the unnecessary provisioning of an agent if the `when` conditions are not met.
3. An `eventTrigger` is configured to only match a JSON payload containing `controller.action=='provision'`. We wil come back to this when we update the `controller-casc-automation` pipeline for your Ops controller.
4. An agent is defined for the **Provision Managed Controller** `stage` as the `sh` steps require a normal (some times referred to as heavy-weight) executor (meaning it must be run on an agent since all managed controllers our configured with 0 executors): `agent { label 'default-jnlp' }`
5. The declarative `environment` directive is used to capture values published by the Cross Team Collaboration `event`, to retrieve the controller provisioning secret value from the workshop Ops controller and to retrieve the Operations Center admin API token credential.
6. Multiple `when` conditions are configured so the **Provision Managed Controller** `stage` will only run if the job is triggered by an `EventTriggerCause` and if the `PROVISION_SECRET` matches the event payload secret.
7. Finally, the actual steps to provision a managed controller:
    - The `curl` command is used to download the `jenkins-cli.jar` from the Operations Center. A Docker container image could be used instead, but correct compatible version is guaranteed by downloading it every time.
    - An `alias` is created for the the Jenkins CLI connection command. This makes the pipeline more readable and allows reuse for multiple CLI commands.
    - Next, the `casc-bundle-set-availability-pattern` command of the [CLI for CloudBees CI Configuration as Code (CasC) for Controllers](https://docs.cloudbees.com/docs/admin-resources/latest/cli-guide/casc-bundle-management) is used to set the configuration bundle availability pattern for the provisioned controller's bundle.
    - Finally, a custom Groovy script, `casc-workshop-provision-controller-with-casc.groovy`, is executed on the Operations Center and contains the Groovy code to provision a managed controller with a configuration bundle.

### Review the Controller with CasC Provisioning Groovy Script
The `casc-workshop-provision-controller-with-casc.groovy` script is based on the Groovy script mentioned in this CloudBees Knowledge Base article *[How to create a Kubernetes Managed Master programmatically](https://support.cloudbees.com/hc/en-us/articles/360035632851-How-to-create-a-Kubernetes-Managed-Master-programmatically)* and can be found in the [CloudBees jenkins-scripts public repository](https://github.com/cloudbees/jenkins-scripts/blob/master/createManagedMasterK8s.groovy). The script we are using in the workshop differs in a few ways:
1. The workshop script, [available here](https://github.com/cloudbees-days/controller-provisioning/blob/main/casc-workshop-provision-controller-with-casc.groovy), defines the controller provision properties as YAML instead of using Java setters. These properties include mounting a volume for the Container Storage Interface secrets, and the `GITHUB_ORGANIZATION` and `GITHUB_USER` environment variable used by the workshop configuration bundles:
```yaml
provisioning:
  cpus: 1
  disk: 20
  memory: 4000
  domain: "${controllerFolderName}-${controllerName}"
  yaml: |
    kind: "StatefulSet"
    spec:
      template:
        spec:
          containers:
          - name: "jenkins"
            env:
            - name: "SECRETS"
              value: "/var/jenkins_home/jcasc_secrets"
            - name: "GITHUB_ORGANIZATION"
              value: "/${gitHubOrganization}"
            - name: "GITHUB_USER"
              value: "/${gitHubUser}"
            volumeMounts:
            - name: "jcasc-secrets"
              mountPath: "/var/jenkins_home/jcasc_secrets"
          volumes:
          - name: "jcasc-secrets"
            csi:
              driver: secrets-store.csi.k8s.io
              readOnly: true
              volumeAttributes:
                secretProviderClass: "cbci-mc-secret-provider"
```
2. The next difference is that workshop controllers are created in a folder that matches the name of your workshop GitHub Organization that is in a workshop specific folder. This makes it easier to configure RBAC across multiple controllers in the same folder.
```groovy
def controllerFolder = Jenkins.instance.getItem(controllerFolderName) 
ManagedMaster controller = controllerFolder.createProject(ManagedMaster.class, controllerName)
```
3.  Finally, in addition to configuring the controller's bundle properties(`ConnectedMasterTokenProperty` and `ConnectedMasterCascProperty`), the controller is also configured to opt out of Operations Center authorization. This is currently required to use CasC for RBAC as we will see in the next lab.
```groovy
controller.properties.replace(new com.cloudbees.opscenter.server.security.SecurityEnforcer.OptOutProperty(com.cloudbees.opscenter.server.sso.AuthorizationOptOutMode.INSTANCE, false, null))
//set casc bundle, but not for CasC workshop
controller.properties.replace(new ConnectedMasterTokenProperty(hudson.util.Secret.fromString(UUID.randomUUID().toString())))
controller.properties.replace(new ConnectedMasterCascProperty("$controllerFolderName-$controllerName"))
```

### Add Event Publishing Stage to your Ops controller controller-casc-automation pipeline script
Now that we have reviewed the pipeline and Groovy script for the workshop provisioning of managed controllers with configuration bundles, we need to publish a Cross Team Collaboration event in the `controller-casc-automation` pipeline script.

1. Navigate to your copy of the `ops-controller` repository in your workshop GitHub Organization.
2. Part of the JSON payload that we need to send to the workshop Ops controllers is a provisioning secret. So, we need to add a new **secret text** credential type to your `jcasc/credentials.yaml` and then apply the updated configuration bundle to your Ops controller.
3. Click on the `jcasc/credentials.yaml` and then click on the ***Edit this file*** pencil button.
4. Add the following new `credential` under `restrictedSystem`->`domainCredentials`:
```yaml
    - allowList: "controller-jobs/cbci-casc-automation/**/*"
      credentials:
        string:
          description: "CasC Workshop Controller Provision Secret"
          id: "casc-workshop-controller-provision-secret"
          scope: GLOBAL
          secret: "${cbciCascWorkshopControllerProvisionSecret}"
```

{{%expand "expand for complete jcasc/credentials.yaml file" %}}
```yaml
credentials:
  restrictedSystem:
    domainCredentials:
    - allowList: "controller-jobs/cbci-casc-automation/**/*"
      credentials:
        string:
          description: "CasC Workshop Controller Provision Secret"
          id: "casc-workshop-controller-provision-secret"
          scope: GLOBAL
          secret: "${cbciCascWorkshopControllerProvisionSecret}"
    - allowList: "controller-jobs/cbci-casc-automation/**/*"
      credentials:
        gitHubApp:
          apiUri: "https://api.github.com"
          appID: "${cbciCascWorkshopGitHubAppId}"
          description: "CloudBees CI CasC Workshop GitHub App credential"
          id: "cloudbees-ci-casc-workshop-github-app"
          owner: "${GITHUB_ORGANIZATION}"
          privateKey: "${cbciCascWorkshopGitHubAppPrivateKey}"
  system:
    domainCredentials:
    - credentials:
      - string:
          description: "Webhook secret for CloudBees CI Workshop GitHub App"
          id: "cloudbees-ci-workshop-github-webhook-secret"
          scope: SYSTEM
          secret: "${gitHubWebhookSecret}"
```
{{% /expand%}}

5. Commit the `jcasc/credentials.yaml` file directly to the `main` branch of your `ops-controller` repository. ![Commit credentials.yaml](commit-credentials.png?width=50pc)
6. Navigate to the `main` branch job of the `ops-controller` Multibranch pipeline project on your Ops controller. ![ops-controller Mulitbranch](ops-controller-multibranch-jcasc.png?width=50pc)
7. After the the `main` branch job has completed successfully, navigate to the top level of your Ops controller, click on the **Manage Jenkins** link in the left menu, and then click on the **Manage Credentials** link. ![Manage Credentials link](manage-credentials-link.png?width=50pc)
11. On the **Credentials** management page you will see a new **CasC Workshop Controller Provision Secret** credential.  ![New Credential](new-credential.png?width=50pc)
11. Return to your copy of the `ops-controller` repository, click on the `controller-casc-automation` pipeline script and then click on the ***Edit this file*** pencil button.
11. Add the following `stage` after the existing **Update Config Bundle** `stage`. It is important that the **Publish Provision Controller Event** `stage` comes after the **Update Config Bundle** `stage` as the managed controller's configuration bundle must exist before it can be provisioned with a configuration bundle. Also recall from the review above that the target job's `eventTrigger` is looking to match `controller.action=='provision'` and will validate the `PROVISION_SECRET` we are passing in.
```groovy
    stage('Publish Provision Controller Event') {
      when {
        branch 'main'
      }
      environment { PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret') }
      steps {
        publishEvent event:jsonEvent("""
          {'controller':{'name':'${GITHUB_REPO}','action':'provision'},'github':{'organization':'${GITHUB_ORG}','repository':'${GITHUB_REPO}','user':'${GITHUB_USER}'},'secret':'${PROVISION_SECRET}'}
        """), verbose: true
      }
    }
```

{{%expand "expand for complete controller-casc-automation pipeline file" %}}
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
          sh "kubectl cp --namespace sda ${GITHUB_ORG}-${GITHUB_REPO} cjoc-0:/var/jenkins_home/jcasc-bundles-store/ -c jenkins"
        }
      }
    }
    stage('Publish Provision Controller Event') {
      when {
        branch 'main'
      }
      environment { PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret') }
      steps {
        publishEvent event:jsonEvent("""
          {'controller':{'name':'${GITHUB_REPO}','action':'provision'},'github':{'organization':'${GITHUB_ORG}','repository':'${GITHUB_REPO}','user':'${GITHUB_USER}'},'secret':'${PROVISION_SECRET}'}
        """), verbose: true
      }
    }
  }
}
```
{{% /expand%}}

12. Commit the changes directly to the `main` branch. ![Commit pipeline job](commit-pipeline.png?width=50pc)
13. After you commit the file, your GitHub Organization pipeline job for the `main` branch of your `ops-controller` repository will be triggered. However, nothing will actually be updated or created because your Ops controller already exists and there were no configuration bundle changes. But we are now ready to dynamically provision a new managed controller for your GitHub Organization.

### Create a new managed controller repository
In the previous section you updated your Ops controller `controller-casc-automation` pipeline script to publish an event to trigger the provisioning of a managed controller with a configuration bundle. Now you will triggers the provisioning of a managed controller by creating a new GitHub repository in your workshop GitHub Organization and adding a `bundle.yaml` file to it.

1. At the top level of your GitHub Organization click on the link for the **dev-controller** repository. ![dev-controller repo link](github-dev-controller-repo-link.png?width=50pc)
2. Next click on the **Add file** button and then select **Create new file**. ![Create new file in GitHub](github-create-new-file.png?width=50pc)
```yaml
apiVersion: "1"
version: "1"
id: "cbci-casc-workshop-dev-controller"
description: "CloudBees CI configuration bundle for the cbci-casc-workshop dev-controller Controller"
parent: "base"
```
3. On the next screen, name the new file `bundle.yaml`, enter the contents from above into the editor. Note that the `parent` is specified as `base`. Commit the new `bundle.yaml` file directly to the `main` branch of your **dev-controller** GitHub repository.
4. Once you commit the `bundle.yaml` file to the `main` branch of your **dev-controller** GitHub repository it will trigger the creation of a new Multi-branch pipeline job on your Ops controller.  ![dev-controller Multi-branch job](dev-controller-multibranch-job.png?width=50pc)
5. Navigate to the `main` branch of the **dev-controller** Multi-branch pipeline job on your Ops controller and you should see an **Event JSON** in the build logs similar to the one below (of course the GitHub information will be unique to you). ![Event JSON log output](event-json-log-output.png?width=50pc)
6. A few minutes after the **dev-controller** **main** branch job completes you will have a new managed controller named **dev-controller** in the same folder as your Ops controller. ![New dev-controller](new-dev-controller.png?width=50pc)
