---
title: "Provisioning Controllers with CloudBees CI Configuration Bundles"
chapter: false
weight: 5
--- 

While the default bundle we explored in a previous lab would allow you to easily manage configuration across all of your organization's controllers, it does not allow for any differences in configuration bundles between controllers. Also, the number of manual steps to configure and apply controller specific bundles to a larger number of controllers wastes time and is prone to errors. 

In this lab we will explore the manual process for configuring and applying controller specific configuration bundles, taking advantage of bundle inheritance to reduce the complexity and size of controller specific bundles, and then we will look at a GitOps approach for automating the process of provisioning a controller to include automating the configuration and application of a controller specific configuration bundle.


We will be using GitHub branches in the `configuration-bundles` repository to represent individual controllers. You may decide that it makes more sense to use individual repositories or folders within one repository to manage the configuration bundles across multiple controllers. However, by using Git branches we can easily leverage the Jenkins Mulitbranch pipeline project type to automatically manage the Pipeline jobs to automate controller provisioning with unique bundles and automate the updating of bundles as we have already done for your Ops controller.

1. 