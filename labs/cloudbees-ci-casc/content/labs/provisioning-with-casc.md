---
title: "Provisioning Controllers with CloudBees CI Configuration Bundles"
chapter: false
weight: 5
--- 

While the parent `base` bundle we explored in the previous lab is also configured to be the default bundle and would allow you to easily manage configuration across all of your organization's controllers, it does not allow for any differences in configuration bundles between controllers. Also, the number of manual steps to provision a controller and apply controller specific bundles to numerous controllers wastes time and is prone to errors. Imagine if you had dozens or even hundreds of controllers (like we do in this workshop), things would quickly become very difficult to manage.

In this lab we will explore  a GitOps approach for automating the process of provisioning a controller to include automating the configuration and application of a controller specific configuration bundle. This approach is based on individual repositories representing individual controllers and takes advantage of the Jenkins GitHub Organization project type and CloudBees CI custom marker file. After we are done setting up the job configuration on your Ops controller then a new controller will be provisioned any time you add a new GitHub repository with a `bundle.yaml` file in it. The managed controller will have the same name as the repository and will be provisioned with the configuration bundle from the associated GitHub repository.

>**NOTE:** Another GitOps type approach you may be interested in is using one repository to declaratively represent an entire CloudBees CI cluster as explained here https://github.com/kyounger/cbci-helmfile. 

## GitOps for Controller Provisioning with CloudBees CI Configuration Bundles

Currently, programmatic provisioning of a managed controller requires running a Groovy script on CloudBees CI Operations Center and requires. This can easily be done from a Jenkins Pipeline by leveraging the Jenkins CLI and API tokens. However, for the purposes of the shared workshop environment we will be running the provisioning job from the workshop Ops controller and will leverage CloudBees CI Cross Team Collaboration to trigger that job with the required payload from your Ops controller.

1. Dynamically or programmatically creating a managed controller requires executing a Groovy script on CloudBees CI Cloud Operations Center and requires a Jenkins user API token that has administrative privileges. 
2.  