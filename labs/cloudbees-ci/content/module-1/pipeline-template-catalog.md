---
title: "Pipeline Template Catalogs"
chapter: false
weight: 1
---

## Import Pipeline Template Catalog
Although you can add Pipeline Template Catalogs via the managed controller UI, this lab will explore how to manage CloudBees CI Pipeline Template Catalogs with the CloudBees CI command-line interface (CLI). 

1. Navigate to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **New Item** in the left menu. <p>![New Item](create-new-item.png?width=60pc)
2. Enter ***import-catalog*** as the **item name**, select **Pipeline** and the click the **OK** button.<p>![import-catalog Pipeline](create-pipeline-item.png?width=60pc)
3. Scroll down to the **Pipeline** section of the job configuration and select ***Pipeline script from SCM*** for the **Definition**. <p>![Pipeline Definition](pipeline-definition.png?width=60pc)
4. Select ***Git*** as the **SCM** type and then:
   1. Enter the URL for your fork of the **pipeline-template-catalog** as the value for the **Repository URL** - ***https://github.com/{YOUR_GITHUB_ORGANIZATION}/pipeline-template-catalog.git***
   {{% notice tip %}}
   {{%expand "Copy GitHub Repository URL" %}}If you navigate to your GitHub repository and click on the **Code** button and then click on the *clipboard* icon to copy the Git URL for your repository. <p>![Copy Repo Git URL](copy-repo-url.png?width=40pc){{% /expand%}}
   {{% /notice %}}
   1. Select ***77562/\*\*\*\*\*\* (CloudBees CI Workshop GitHub App credential)*** for the **Credentials** value. The rest of the default values are sufficient.
   2. Click the **Save** button. <p>![Pipeline SCM Configuration](pipeline-scm-config.png?width=60pc)
5. Click **Build Now** in the left navigation menu.
6. Once the job is complete you should see the following success message in the build log:
   
   ```
   {
     "message" : "Successfully imported Pipeline Template Catalogs.",
     "status" : "SUCCESS"
   }
   ```

7. Navigate to the top-level of your ***managed controller*** and then click on the **Pipeline Template Catalogs** link in the menu on the left. <p>![Pipeline Template Catalogs link](catalog-link.png?width=60pc)
8. On the **Pipeline Template Catalogs** page click on the line for the **workshopCatalog**. <p>![workshopCatalog link](workshopcatalog-link.png?width=50pc)
9.  On the **CloudBees CI Workshop Template Catalog** screen you will see the following templates listed: <p>![Template List](workshop-template-list.png?width=50pc)

## Enforce the Use of Templates at the Folder Level
The CloudBees CI Folders Plus feature allows you to restrict the type of items 

1. Navigate back to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **New Item** in the left menu.
2. For the **item name** enter ***template-jobs***, select **Folder** and then click the **OK** button. <p><img src="new-folder-click.png" width=800/>
3. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **CloudBees CI Configuration Bundle** and **Maven Pipeline Template**, and then hit the **Save** button. <p>![Restricted Folder Items](restricted-items-check.png?width=60pc)
4. Now when you click on **New Item** in the **template-jobs** folder you will only have the **CloudBees CI Configuration Bundle** and **Maven Pipeline Template** item types available to select.
   
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#31).**
