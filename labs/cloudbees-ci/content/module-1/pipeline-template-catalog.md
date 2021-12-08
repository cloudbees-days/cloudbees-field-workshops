---
title: "Pipeline Template Catalogs"
chapter: false
weight: 1
---

Managing Pipeline Template Catalogs across a large number of ***managed controllers*** using the graphical user interface (GUI) is time consuming and prone to human error due to the repetitive nature of the task.

Configuration as Code (CasC) for CloudBees CI allows for managing Pipeline Template Catalogs as code across multiple managed controllers as code, which reduces efforts and ensures consistency across all of your teams, while increasing the security and traceability of changes by managing the configuration as code.


## Explore Pipeline Template Catalog
This lab will explore how to manage CloudBees CI Pipeline Template Catalogs with the CloudBees CI Configuration as Code. This will be a brief introduction to CloudBees CI Configuration as Code which we will explore more in the next section.

1. Navigate to your copy of the `cloudbees-ci-config-bundle` repository in your workshop GitHub Organization, click on the `jenkins.yaml` file and scroll down to the `globalCloudBeesPipelineTemplateCatalog` CasC entry:

```yaml
globalCloudBeesPipelineTemplateCatalog:
  catalogs:
  - branchOrTag: "main"
    scm:
      github:
        configuredByUrl: true
        credentialsId: "cloudbees-ci-workshop-github-app"
        repoOwner: "${GITHUB_ORGANIZATION}"
        repository: "pipeline-template-catalog"
        repositoryUrl: "https://github.com/${GITHUB_ORGANIZATION}/pipeline-template-catalog.git"
        traits:
        - gitHubBranchDiscovery:
            strategyId: 1
        - gitHubPullRequestDiscovery:
            strategyId: 1
        - gitHubForkDiscovery:
            strategyId: 1
            trust: "gitHubTrustPermissions"
    updateInterval: "1d"
```

{{% notice note %}}
Notice the `${GITHUB_ORGANIZATION}` variable placeholders. These will be replaced by environmental variables applied to your controller when it was provisioned and is similar to how secrets can be injected into a Jenkins Configuration as Code file, as we will see in the next section on CloudBees CI Configuration as Code.
{{% /notice %}}

2. Next, navigate to the top-level of CloudBees CI Operations Center - **Dashboard** - and click on the link for your Managed Controller that is named **controller** (it will be in a folder with the same name as your workshop GitHub Organization). ![Managed Controller link](managed-controller-link.png?width=60pc)
3. At the top-level of your managed controller, click on the **Pipeline Template Catalogs** link in the menu on the left. ![Pipeline Template Catalogs link](catalog-link.png?width=40pc)
4. On the **Pipeline Template Catalogs** page ensure that the **workshopCatalog** catalog's **Status** is ***Healthy*** and then click on the **workshopCatalog** link. <p>![workshopCatalog link](workshopcatalog-link.png?width=50pc)
5.  On the **CloudBees CI Workshop Template Catalog** screen you will see the following templates listed: ![Template List](workshop-template-list.png?width=50pc)

## Enforce the Use of Templates at the Folder Level
The [CloudBees CI Folders Plus plugin](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/folders-plus) includes the ability to restrict the type of items/jobs allowed to be created in a folder. When this capability is used with [CloudBees CI RBAC](https://docs.beescloud.com/docs/cloudbees-ci/latest/cloud-secure-guide/rbac) you can easily enforce the use of approved (and tested) Pipeline templates across all your CloudBees CI users.

1. Navigate back to the top-level of your CloudBees CI Managed Controller (Jenkins instance) and click on **New Item** in the left menu (notice how many different items are listed).
2. For the **item name** enter ***template-jobs***, select **Folder** (be sure to select **Folder** and not **Folder Template**) as the item type and then click the **OK** button. ![Restricted Folder Item](new-folder-click.png?width=50pc)
3. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **CloudBees CI Configuration Bundle** and **Maven Pipeline Template** (the template jobs we will be using throughout the rest of the workshop) - and then hit the **Save** button. ![Restricted Folder Items](restricted-items-check.png?width=40pc)
4. Now when you click on **New Item** in the **template-jobs** folder you will be restricted to the **CloudBees CI Configuration Bundle** and **Maven Pipeline Template** item types. This reduces confusion of what job types to use and enforces the use of approved templates. ![Restricted Folder New Item](restricted-folder-new-item.png?width=30pc)

## Create a Job from Pipeline Template

In this lab you will create a Multibranch Pipeline job from a Pipeline template on your CloudBees CI managed controller to automatically update the [CloudBees CI configuration bundle](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-admin-guide/ci-casc-modern#_creating_a_configuration_bundle) for your CloudBees CI ***managed controller***.

1. Navigate into the **template-jobs** folder on your managed controller.
2. Click on the **New Item** link in the left navigation menu.
3. Enter ***config-bundle-ops*** as the **Item Name**, select **CloudBees CI Configuration Bundle** as the item type and then click the **OK** button. ![New Update Bundle](new-bundle-template-job.png?width=50pc)
4. On the next screen, fill in the **GitHub Organization** template parameter with the name of the GitHub Organization you created for this workshop (all the other default values should be correct) and then click the **Save** button. ![Config Bundle Template Parameters](bundle-template-params.png?width=50pc) 

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-ci/#pipeline-template-catalog-overview">return to the workshop slides</a>**   
