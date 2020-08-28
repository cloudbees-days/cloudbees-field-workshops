---
title: "Pipeline Template Catalogs"
chapter: false
weight: 1
---

## Import Pipeline Template Catalog
Although you can add Pipeline Template Catalogs via the managed controller UI, this lab will explore how to manage CloudBees CI Pipeline Template Catalogs with the CloudBees CI command-line interface (CLI). 

1. Navigate to the top-level of Operations Center - **Jenkins** - and click on the link for your ***managed controller***. ![Managed Controller link](managed-controller-link.png?width=60pc)
2. At the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **New Item** in the left menu. ![New Item](create-new-item.png?width=60pc)
3. Enter ***import-catalog*** as the **item name**, select **Pipeline** and the click the **OK** button.<p>![import-catalog Pipeline](create-pipeline-item.png?width=60pc)
4. Scroll down to the **Pipeline** section of the job configuration and select ***Pipeline script from SCM*** for the **Definition**. <p>![Pipeline Definition](pipeline-definition.png?width=60pc)
5. Select ***Git*** as the **SCM** type and then:
   - Enter the URL for your fork of the `pipeline-template-catalog` as the value for the **Repository URL** - ***https:\//github.com/{YOUR_GITHUB_ORGANIZATION}/pipeline-template-catalog.git***
   - If you navigate to your GitHub `pipeline-template-catalog` repository, and click on the **Code** button, you can then click on the *clipboard* icon to copy the Git URL for your repository. ![Copy Repo Git URL](copy-repo-url.png?width=40pc)
   - Select ***77562/\*\*\*\*\*\* (CloudBees CI Workshop GitHub App credential)*** for the **Credentials** value. The rest of the default values are sufficient.
   - Click the **Save** button. <p>![Pipeline SCM Configuration](pipeline-scm-config.png?width=60pc)
6. Click **Build Now** in the left navigation menu.
7. Once the job is complete you should see the following success message in the build log:
   
   ```
   {
     "message" : "Successfully imported Pipeline Template Catalogs.",
     "status" : "SUCCESS"
   }
   ```

8. Navigate to the top-level of your ***managed controller*** and then click on the **Pipeline Template Catalogs** link in the menu on the left. <p>![Pipeline Template Catalogs link](catalog-link.png?width=60pc)
9. On the **Pipeline Template Catalogs** page ensure that the **workshopCatalog** catalog's **Status** is ***Healthy*** and then click on the **workshopCatalog** link. <p>![workshopCatalog link](workshopcatalog-link.png?width=50pc)
10. On the **CloudBees CI Workshop Template Catalog** screen you will see the following templates listed: ![Template List](workshop-template-list.png?width=50pc)

## Enforce the Use of Templates at the Folder Level
The [CloudBees CI Folders Plus plugin](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/folders-plus) includes the ability to restrict the type of items/jobs allowed to be created in a folder. When this capability is used with CloudBees CI RBAC you can easily enforce that all your CloudBees CI users use an approved (and tested) Pipeline template.

1. Navigate back to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **New Item** in the left menu.
2. For the **item name** enter ***template-jobs***, select **Folder** (be sure to select **Folder** and not **Folder Template**) as the item type and then click the **OK** button. ![Restricted Folder Item](new-folder-click.png?width=50pc)
3. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **CloudBees CI Configuration Bundle** and **Maven Pipeline Template**, and then hit the **Save** button. ![Restricted Folder Items](restricted-items-check.png?width=60pc)
4. Now when you click on **New Item** in the **template-jobs** folder you will only have the **CloudBees CI Configuration Bundle** and **Maven Pipeline Template** item types available to select. ![Restricted Folder New Item](restricted-folder-new-item.png?width=60pc)
   
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#21).**
