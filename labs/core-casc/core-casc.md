# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Configuration as Code

CasC for CloudBees Core consists of a configuration bundle that includes four files:

1. 

## Enabling CasC for a Core Managed Master
A directory with the same name as your Team Master must be created in the `jcasc-...` directory in the CloudBees Operations Center Jenkins home directory. The `workshop-setup` job that you just ran did this for everyone.

## Configuration Components

### Credentials
Secrets for credentials can be managed in a few different ways:
  1. As properties files in the Jenkins Master file system.
  2. As Jenkins encrypted values used directly in the JCasC yaml configuration.

### Master Level Kubernetes Agent Templates
The CloudBees Kube Management plugin provides...

## GitOps for Core CasC
One of the main reasons to manage configurations as code is to allow it to be managed in source control like GitHub.
* Create a Jenkins Pipeline job on your Team Master to automatically update the Core configuration bundle for your Team Master.
* Add some configuration to the `jenkins.yaml` JCasC configuration in your **core-config-bundle** repository and commit the changes to tigger an update.

You may proceed to the next lab: [*Pipeline Template Catalogs*](../pipeline-template-catalog/pipeline-template-catalog.md) or choose another lob on the [main page](../../README.md#workshop-labs).




