---
title: "Pipeline Template Catalogs"
chapter: false
weight: 1
---

## Import Pipeline Template Catalog
Although you can add Pipeline Template Catalogs via the managed controller UI, this lab will explore how to manage CloudBees CI Pipeline Template Catalogs with the CloudBees CI command-line interface (CLI). 

1. Navigate to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **New Item** in the left menu<p>![New Item](create-new-item.png?width=60pc)
2. Enter ***import-catalog*** as the **item name**, select **Pipeline** and the click the **OK** button.<p>![import-catalog Pipeline](create-pipeline-item.png?width=60pc)
3. Scroll down to the **Pipeline** section of the job configuration and select ***Pipeline script from SCM*** for the **Definition**. <p>![Pipeline Definition](pipeline-definition.png?width=60pc)
4. Select ***Git*** as the **SCM** type and then:
   1. Enter the URL for your fork of the **pipeline-template-catalog** as the value for the **Repository URL** - ***https://github.com/{YOUR_GITHUB_ORGANIZATION}/pipeline-template-catalog.git***
   2. Select ***77562/\*\*\*\*\*\* (CloudBees CI Workshop GitHub App credential)*** for the **Credentials** value. The rest of the default values are sufficient.
   3. Click the **Save** button. <p>![Pipeline SCM Configuration](pipeline-scm-config.png?width=60pc)
5. Click **Build Now** in the left navigation menu.
6. Once the job is complete you should see the following success message in the build log:
   
   ```
   {
     "message" : "Successfully imported Pipeline Template Catalogs.",
     "status" : "SUCCESS"
   }
   ```

7. Navigation to the top-level of your ***managed controller*** and then click on the **Pipeline Template Catalogs** link in the menu on the left. <p>![Pipeline Template Catalogs link](catalog-link.png?width=60pc)
8. Click on **Add catalog**<p><img src="Add-template-click.png" width=800/>
9. Fill out the **Catalog source control options**:
   1. **Branch or tag for this template catalog**: master
   2. Select **GitHub** under **Catalog source code repository location**
   3. **Credentials**: select the *username/password* credential you created for the CloudBees CI workshop - it will show up as - `[GitHub username]/****** (GitHub PAT from JCasC - username/password)`
   4. **Repository HTTPS URL**: The GitHub URL for your forked copy of the **pipeline-template-catalog** repository. In the example below the GitHub Organization being used is **bee-cd** so the *repository URL* would be `https://github.com/bee-cd/pipeline-template-catalog.git`. **NOTE:** You need to use the repository URL for the GitHub Organization you created for this workshop in the CloudBees CI workshop setup lab - so `bee-cd` would be replaced with your GitHub Organization.
   5. Next, click the **Validate** button to ensure your credentials and repository URL are set correctly. If the validation fails, please check that you selected the correct GitHub credentials and that the **Repository HTTPS URL** points to the fork of the **pipeline-template-catalog** repository in the GitHub Organization that you created for this workhsop.
   6. Finally, click the **Save** button <p><img src="add-catalog-save.png" width=800/>
10. Once the import is complete, click on the **CloudBees Days Workshop Catalog** link. <p><img src="catalog-link.png" width=800/>
11. The Pipeline Template Catalog you imported will have 5 templates to include the **VueJS** template which we will be using in the next lab. <p><img src="Succesful-template-import.png" width=800/>
12. On your CloudBees CI managed controller (Jenkins instance) navigate to the folder with the same name as your CloudBees CI managed controller (Jenkins instance) (you should see the `workshop-setup` Pipeline job) and then click on the **New Item** link in the left menu<p><img src="new-item-click.png" width=800/>
13. For the **item name** enter ***template-jobs***, select **Folder** and then click the **OK** button. <p><img src="new-folder-click.png" width=800/>
14. Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **VueJS** and then hit the **Save** button. <p><img src="restricted-items-check.png" width=800/>
   
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/cloudbees-ci/#31).**
