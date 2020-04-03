# <img src="images/cloudbeescore_logo.png" alt="CloudBees Core Logo" width="40" align="top"> CloudBees Core - Pipeline Template Catalogs & Pipeline Policies

Pipeline Template Catalogs help ensure that Pipeline jobs conform to organizational standards.

## Import Pipeline Template Catalog
1. Fork https://github.com/cloudbees-days/pipeline-template-catalog
2. Navigate to team master level and click on "Pipeline Template Catalogs"<p><img src="images/Initial-template-click.png" width=800/>
3. Click on "Add catalog"<p><img src="images/Add-template-click.png" width=800/>
4. Fill out the catalog import parameters:
   1. **Branch or tag for this template catalog**: master
   2. Check off **Git**
   3. **Project Repository**: The Git URL for the forked pipeline template catalog repo created in step 1.
   4. **Credentials**: select the *username/password* credential you created for the the CloudBees Core workshop - it will show up as - [GitHub username]/******
   5. Click the **Save** button<p><img src="images/Add-catalog-info.png" width=800/>
5. You should see the following once your catalog has been succesfully imported<p><img src="images/Succesful-template-import.png" width=800/>
6. Navigate back inside your team master and click in to the folder with your team name<p><img src="images/team-folder-click.png" width=800/>
7. Click on the **New Item** link in the left menu<p><img src="images/new-item-click.png" width=800/>
8. We will now create a new folder called "**Template Jobs**"<p><img src="images/new-folder-click.png" width=800/>
9. Inside of the folder configuration click on "**Restrict the kind of children in this folder**" and then select "**VueJS**" only and then hit save<p><img src="images/restricted-items-check.png" width=800/>

## Create a Pipeline Policy
[Pipeline Policies for CloudBees Core](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.

In this exercise you will create a Pipeline Policy to ensure that all Pipeline jobs that run on your Team Master have a `timeout` set.

## Create vue.js Job from Pipeline Template Catalog
In this exercise you will create a new Multibranch Pipeline job from the Pipeline Template Catalog you added above.

Congratulations! You have imported a pipeline template catalog into your team master and then created a folder where only the job from that template can be created.

You may proceed to the next lab: [*Hibernating Masters*](../hibernating-masters/hibernating-masters.md) or choose another lab on the [main page](../../README.md#workshop-labs).
