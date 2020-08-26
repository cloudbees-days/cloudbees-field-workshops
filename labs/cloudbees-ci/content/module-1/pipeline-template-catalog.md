---
title: "Pipeline Template Catalogs"
chapter: false
weight: 1
---

[Instructor led video of lab.](https://youtu.be/YBoX-bE3YYQ)

## Import Pipeline Template Catalog
1. Navigate to the top-level of your CloudBees CI managed controller (Jenkins instance) and click on **Pipeline Template Catalogs** in the left menu<p><img src="Initial-template-click.png" width=800/>
2. Click on **Add catalog**<p><img src="Add-template-click.png" width=800/>
3. Fill out the **Catalog source control options**:
   1. **Branch or tag for this template catalog**: master
   2. Select **GitHub** under **Catalog source code repository location**
   3. **Credentials**: select the *username/password* credential you created for the CloudBees CI workshop - it will show up as - `[GitHub username]/****** (GitHub PAT from JCasC - username/password)`
   4. **Repository HTTPS URL**: The GitHub URL for your forked copy of the **pipeline-template-catalog** repository. In the example below the GitHub Organization being used is **bee-cd** so the *repository URL* would be `https://github.com/bee-cd/pipeline-template-catalog.git`. **NOTE:** You need to use the repository URL for the GitHub Organization you created for this workshop in the CloudBees CI workshop setup lab - so `bee-cd` would be replaced with your GitHub Organization.
   5. Next, click the **Validate** button to ensure your credentials and repository URL are set correctly. If the validation fails, please check that you selected the correct GitHub credentials and that the **Repository HTTPS URL** points to the fork of the **pipeline-template-catalog** repository in the GitHub Organization that you created for this workhsop.
   6. Finally, click the **Save** button <p><img src="add-catalog-save.png" width=800/>
4. Once the import is complete, click on the **CloudBees Days Workshop Catalog** link. <p><img src="catalog-link.png" width=800/>
5. The Pipeline Template Catalog you imported will have 4 templates to include the **VueJS** template which we will be using next. <p><img src="Succesful-template-import.png" width=800/>
6. On your CloudBees CI managed controller (Jenkins instance) navigate to the folder with the same name as your CloudBees CI managed controller (Jenkins instance) (you should see the `workshop-setup` Pipeline job) and then click on the **New Item** link in the left menu<p><img src="new-item-click.png" width=800/>
7. For the **item name** enter ***template-jobs***, select **Folder** and then click the **OK** button. <p><img src="new-folder-click.png" width=800/>
8.  Scroll to the bottom of the folder configuration and click on **Restrict the kind of children in this folder** - a [CloudBees Folders Plus](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-secure-guide/folders-plus) feature - and then select **VueJS** and then hit the **Save** button. <p><img src="restricted-items-check.png" width=800/>
   
**For instructor led workshops please returns to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/core/#31).**
