---
title: "Provisioning Controllers with CloudBees CI Configuration Bundles"
chapter: false
weight: 5
--- 

While the parent `base` bundle we explored in the previous lab is also configured to be the default bundle and would allow you to easily manage configuration across all of your organization's controllers, it does not allow for any differences in configuration bundles between controllers. Also, the number of manual steps to provision a controller and apply controller specific bundles to numerous controllers wastes time and is prone to errors. Imagine if you had dozens or even hundreds of controllers (like we do in this workshop), things would quickly become very difficult to manage.

In this lab we will explore  a GitOps approach for automating the process of provisioning a controller to include automating the configuration and application of a controller specific configuration bundle. This approach is based on individual repositories representing individual controllers and takes advantage of the Jenkins GitHub Organization project type and CloudBees CI custom marker file. After we are done setting up the job configuration on your Ops controller then a new controller will be provisioned any time you add a new GitHub repository with a `bundle.yaml` file in it. The managed controller will have the same name as the repository and will be provisioned with the configuration bundle from the associated GitHub repository.

>**NOTE:** Another GitOps type approach you may be interested in is using one repository to declaratively represent an entire CloudBees CI cluster as explained here https://github.com/kyounger/cbci-helmfile. 

## GitOps for Controller Provisioning with CloudBees CI Configuration Bundles

Currently, programmatic provisioning of a managed controller requires running a Groovy script on CloudBees CI Operations Center and requires. This can easily be done from a Jenkins Pipeline by leveraging the Jenkins CLI and API tokens. However, for the purposes of the shared workshop environment we will be running the provisioning job from the workshop Ops controller and will leverage [CloudBees CI Cross Team Collaboration](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/cross-team-collaboration) to trigger that job with the required payload from your Ops controller.

>**NOTE:** Dynamically (or programmatically) creating a managed controller requires executing a Groovy script on CloudBees CI Cloud Operations Center and requires a Jenkins user API token that has administrative privileges. For the purpose of this workshop we will utilize the workshop Ops controller to execute the necessary CLI commands against the Operations Center to limit the exposure of the Operations Center administrator API token needed.

1. First we will examine the Jenkins declarative pipeline job that will be triggered by your Ops controller on the workshop Ops controller using CloudBees CI Cross Team Collaboration. 
```groovy
def event = currentBuild.getBuildCauses()[0].event
pipeline {
  agent none
  options { timeout(time: 10, unit: 'MINUTES') }
  triggers {
    eventTrigger jmespathQuery("controller.action=='provision'")
  }
  stages {
    stage('Provision Managed Controller') {
      agent  { label 'default-jnlp' }
      environment {
        PROVISION_SECRET = credentials('casc-workshop-controller-provision-secret')
        ADMIN_CLI_TOKEN = credentials('admin-cli-token')
        GITHUB_ORGANIZATION = event.github.organization.toString().replaceAll(" ", "-")
        GITHUB_REPOSITORY = event.github.repository.toString().toLowerCase()
        CONTROLLER_FOLDER = GITHUB_ORGANIZATION.toLowerCase()
        BUNDLE_ID = "${GITHUB_ORGANIZATION}-${GITHUB_REPOSITORY}"
        AVAILABILITY_PATTERN = "${GITHUB_ORGANIZATION}/${GITHUB_REPOSITORY}"
      }
      when {
        beforeAgent true
        allOf {
          triggeredBy 'EventTriggerCause'
          environment name: 'PROVISION_SECRET', value: event.controller.action.secret.toString()
        }
      }
      steps {
        sh '''
          curl -O http://cjoc/cjoc/jnlpJars/jenkins-cli.jar
          alias cli='java -jar jenkins-cli.jar -s http://cjoc/cjoc/ -webSocket -auth $ADMIN_CLI_TOKEN_USR:$ADMIN_CLI_TOKEN_PSW'
          cli casc-bundle-set-availability-pattern --bundle-id $BUNDLE_ID --availability-pattern $AVAILABILITY_PATTERN
          cli groovy =<casc-workshop-provision-controller-with-casc.groovy $GITHUB_ORGANIZATION $GITHUB_REPOSITORY $CONTROLLER_FOLDER
        '''
      }
    }
  }
}
```
    1. The first step is to get the event payload and assign it to a global object available to the rest of the `pipeline`: `def event = currentBuild.getBuildCauses()[0].event`. We do this outside of the declarative `pipeline` block because you cannot assign objects to variables in declarative pipeline and we need the values before we can execute a `script` block in a `stage`.
    2. There is no `agent` at the global level as it will result in the unnecessary provisioning of an agent if the `when` conditions are not met.
    3. An `eventTrigger` is configured to only match a JSON payload containing `controller.action=='provision'`. We wil come back to this when we update the `controller-casc-automation` pipeline for your Ops controller.
    4. An agent is defined for the **Provision Managed Controller** `stage` as the `sh` steps require a normal (some times referred to as heavy-weight) executor (meaning it must be run on an agent since all managed controllers our configured with 0 executors): `agent { label 'default-jnlp' }`
    5. The declarative `environment` directive is used to capture values published by the Cross Team Collaboration `event`, to retrieve the controller provisioning secret value from the workshop Ops controller and to retrieve the Operations Center admin API token credential.
    6. Multiple `when` conditions are configured so the **Provision Managed Controller** `stage` will only run if the job is triggered by an `EventTriggerCause` and if the `PROVISION_SECRET` matches the event payload secret.
    7. Finally, the actual steps to provision a managed controller:
     - The `curl` command is used to download the `jenkins-cli.jar` from the Operations Center. A Docker container image could be used instead, but correct compatible version is guaranteed by downloading it every time.
     - An `alias` is created for the the Jenkins CLI connection command. This makes the pipeline more readable and allows reuse for multiple CLI commands.
     - Next, the `casc-bundle-set-availability-pattern` command of the [CLI for CloudBees CI Configuration as Code (CasC) for Controllers](https://docs.cloudbees.com/docs/admin-resources/latest/cli-guide/casc-bundle-management) is used to set the configuration bundle availability pattern for the provisioned controller's bundle.
     - Finally, a custom Groovy script, `casc-workshop-provision-controller-with-casc.groovy`, is executed on the Operations Center.
2. The `casc-workshop-provision-controller-with-casc.groovy` script is based on the Groovy script mentioned in this CloudBees Knowledge Base article *[How to create a Kubernetes Managed Master programmatically](https://support.cloudbees.com/hc/en-us/articles/360035632851-How-to-create-a-Kubernetes-Managed-Master-programmatically)* and can be found in the [CloudBees `jenkins-scripts` public repository](https://github.com/cloudbees/jenkins-scripts/blob/master/createManagedMasterK8s.groovy). The script we are using in the workshop differs in a few ways:
   1. The workshop script defines the controller provision properties as YAML instead of using Java setters. These properties include mounting a volume for the Container Storage Interface secrets and the `GITHUB_ORGANIZATION` environment variable used by the workshop configuration bundles:
    ```yaml
    provisioning:
      cpus: 1
      disk: 20
      memory: 4000
      yaml: |
        kind: Service
        metadata:
          annotations:
            prometheus.io/scheme: 'http'
            prometheus.io/path: '/${controllerFolderName}-${controllerName}/prometheus'
            prometheus.io/port: '8080'
            prometheus.io/scrape: 'true'
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
   2. The next difference is that workshop controllers are created in a folder that matches the name of your workshop GitHub Organization. This makes it easier to configure RBAC across multiple controllers.
    ```groovy
    def controllerFolder = Jenkins.instance.getItem(controllerFolderName) 
    ManagedMaster controller = controllerFolder.createProject(ManagedMaster.class, controllerName)
    ```
   3.  