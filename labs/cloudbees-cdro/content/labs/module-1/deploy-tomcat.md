---
title: "Deploying a Tomcat Application"
chapter: false
weight: 4
--- 

In this lab, you will use a Service Catalog item to build out a Tomcat application model. You will then create a few environment models and map them to the application so that the Tomcat application can be deployed to those environments.

## CloudBees CD/RO Application Models

CloudBees CD/RO deploy makes deployments manageable, reproducible, and error-proof by modeling application tiers or microservices, the environments to which it are be deployed, and automating the workflow needed for the deployment. The model can be broken into these parts of your application tiers or microservice deployment.

- What: the files or microservices being deployed
- Where: the environments to which the application or microservices are deployed.
- How: the processes that orchestrate deployment of the application tiers or microservices to the environment.

{{% notice note %}}
You must have access to GitHub to complete this exercise.
{{% /notice %}}

## Use the Tomcat Service Catalog item to create a model

1. From GitHub, download [jpetstore.war](https://github.com/o2platform/Demos_Files/blob/master/jPetStore%20-%20O2%20Demo%20Pack/apache-tomcat-7.0.16/webapps/jpetstore.war) to your computer.
2. Select the **Service catalog** link from the banner at the top.
3. Navigate (scroll down) to the **Tomcat Application Model** Service Catalog item. ![Tomcat catalog item](te-tomcat-item.png?width=20pc) 
4. Click the **Create** link and the **Tomcat Application Model** dialog appears.
5. In the **Application details** section, enter these field values:
    - **Application Name**: *jpetstore*
    - **Application Version**: *1.0*
    - **Application Project Name**: *Trial Guide*
6. Next, scroll down to the **Artifact details** section (you may need to expand it) and enter the following:
    - **Group Id**: *com.acme*
    - **Artifact Key**: *jpetstore*
    - **Version**: *7.0.16*
    - **Filename**: *jpetstore.war*
![Tomcat Application details](te-tomcat-app-details.png?width=40pc) 
7. For **File to upload**: Click the **Choose File** button to upload the *jpetstore.war* file you downloaded earlier.
8. Scroll down to the **Deployment details** section (you may need to expand it) and enter the following:
    - **Retrieve to Folder**: */tmp*
    - **Tomcat Config**: *Tomcat*
    - **Context Path**: *jpetstore*
9. Click **OK** to generate the Application model. A "success" message is displayed and you are asked to navigate to the new Application model. ![Successful creation of Application model](te-ss-cataolog-success-msg.png?width=40pc)
10. Select **Yes** to navigate to the new application model. ![Tomcat Application model](tomcat-application-model.png?width=40pc)

## Create the QA environment

In this exercise we will map a deployment environment to your Tomcat application model.

1. Click the **Requires Setup** for the **Map to environment** menu item to open the **Create Environment** dialog. ![Map to Environment](te-ss-catalog-app-hier-menu.png?width=40pc)
2. Select **Create from this Application**. ![Create environment from application](te-tomcat-create-uat-env.png?width=40pc)
3. Enter *QA* for the environment name and select the **Trial Guide** project you created earlier. Select **OK** to create the environment.
4. Select the Resources plus (**+**) button. ![Select Resources](te-ss-catalog-webtier-resources-plus.png?width=20pc)
5. Select **Add resources**. ![Add Resources](add-resources.png?width=40pc)
6. Choose **tomcat_mysql_qa** then select **OK**. ![Select QA resource](select-qa-resource.png?width=70pc)
7. Return to the application by selecting the **Application: jpetstore** link in the **Hierarchy Menu**.

## Deploy the application

1. Select **Run** and then **New Run**. The **Run Application** dialog appears. ![Run deploy](run-deploy.png?width=70pc)
2. Set **Deploy**  as the *process* and **QA** as the *environment*, and turn off the **Smart Deploy**, **Check Dependency** and **Artifact Staging** options. Select **OK**. ![Run Application selections](te-run-app-selections.png?width=40pc)
3. Once the application deployment completes click on the job details link. ![Deploy Job Details link](deploy-job-details-link.png?width=70pc)
4. Next, on the **Job Details** page click on the link for the *tomcat_mysql_qa* **Resource** for the **DeployApp** step. ![Resource link](deploy-resource-link.png?width=70pc)
5. Under the **Resource Details** find the **Agent Host Name** and copy the IP address. ![Resource IP address](te-app-resource-details-ip.png?width=70pc)
6. Use the IP address of the resource to access the application by appending `:8080/jpetsore` to the IP address that you copied. For example, **http://35.202.90.57:8080/jpetstore/** ![jepetstore-webpage](te-app-jpetstore-webpage.png?width=70pc)
7. Close the Job Details dialog to return to the **Deploy** run.
8. Navigate to the environment where the application was deployed by clicking **QA** in the breadcrumbs. ![Navigate to QA Environment](deploy-qa-env-link.png?width=70pc)
9. Click on the **Inventory** link in the top navigation. ![QA Inventory link](qa-inventory-link.png?width=70pc)
10. Create a snapshot by clicking the snapshot (camera) icon under the **Actions** column and clicking the **New Snapshot** link. ![QA Inventory New Snapshot](qa-inventory.png?width=70pc)
11. In the **New Snapshot** dialog enter *jpetstore-qa** as the **Name** and then click the **Next** button. ![New QA Snapshot](new-qa-snapshot.png?width=70pc) 
12. Click the **OK** button to save a new snapshot of this artifact. ![Snapshot of artifact](te-app-snapshot-details.png?width=70pc)

