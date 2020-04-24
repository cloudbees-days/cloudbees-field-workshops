# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Pipeline Template Catalogs

## Import Pipeline Template Catalog
1. Navigate to the top-level of your Team Master level and click on **Pipeline Template Catalogs** in the left menu<p><img src="images/Initial-template-click.png" width=800/>
2. Click on **Add catalog**<p><img src="images/Add-template-click.png" width=800/>
3. Fill out the catalog import parameters:
   1. **Branch or tag for this template catalog**: master
   2. Check off **Git**
   3. **Project Repository**: The Git URL for your forked Pipeline Template Catalog repository.
   4. **Credentials**: select the *username/password* credential you created for the CloudBees Core workshop - it will show up as - `[GitHub username]/******`
   5. Click the **Save** button<p><img src="images/Add-catalog-info.png" width=800/>
4. You should see the following once your catalog has been successfully imported<p><img src="images/Succesful-template-import.png" width=800/>
5. Navigate back inside your team master and click in to the folder with your team name<p><img src="images/team-folder-click.png" width=800/>
6. Click on the **New Item** link in the left menu<p><img src="images/new-item-click.png" width=800/>
7. We will now create a new folder called "**Template Jobs**"<p><img src="images/new-folder-click.png" width=800/>
8. Inside of the folder configuration click on "**Restrict the kind of children in this folder**" and then select "**VueJS**" only and then hit save<p><img src="images/restricted-items-check.png" width=800/>
   
## Create vue.js Job from Pipeline Template Catalog
In this lab you will create a new Multibranch Pipeline job from the **VueJS** template provided by the Pipeline Template Catalog you added above.

1. On your Team Master navigate to the **template-jobs** folder
2. Click on the ***New VueJS*** link in the left menu <p><img src="images/template_link.png" width=800/>
3. Enter an item name of your **[GitHub username]-hello**, select **VueJS**  and click the **OK** button<p><img src="images/item_form.png" width=800/>
4. Fill out the template parameters:
   1. **Repository Owner**: the GitHub Organization your created for the CloudBees Core workshop
   2. **Repository**: The name of your forked repository, "microblog-frontend"
   3. **GitHub Credential ID**: select the *username/password* credential you created for the the CloudBees Core workshop - it will show up as - [GitHub username]/******
   4. Click the **Save** button<p><img src="images/template_parameters.png" width=800/>
5. After the initial scan you should see two jobs, for the two branches in your forked repository<p><img src="images/one_job.png" width=800/>

## Deploy to Staging
Both jobs should automatically start running for both branches, however only the master branch job will deploy because of the way the Pipeline was written.

The templated job will build a Docker image for your **microblog-frontend** application, push the image to the Google Container Registry (GCR), and then deploy your containerized application to a staging environment in Kubernetes - a link to your application will be available in the logs of your job. 

### GitOps with Core v2
As part of the deployment to *staging* the Pipeline Template Catalog job will create a new **environment-staging** repository in your workshop GitHub Organization with the generated Kubernetes deployment yaml used for the deployment to the K8s *staging* environment.

Congratulations! You have imported a Pipeline Template Catalog into your Team Master and then created a folder where only the job from that template can be created.

You may proceed to the next lab: [*CloudBees Pipeline Policies*](../pipeline-policies/pipeline-policies.md) or choose another lab on the [main page](../../README.md#workshop-labs).
