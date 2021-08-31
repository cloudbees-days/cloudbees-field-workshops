---
title: "Deploying a Tomcat Application"
chapter: false
weight: 4
--- 

In this exercise, you use a service catalog item to build out a Tomcat application model. You also create a few environment models and map them to the application so that the Tomcat application can be deployed to the environments.

{{% notice note %}}
You must have access to GitHub to complete this exercise.
{{% /notice %}}

## Use the Tomcat service catalog item to create a model

1. From GitHub, download [jpetstore.war](https://github.com/o2platform/Demos_Files/blob/master/jPetStore%20-%20O2%20Demo%20Pack/apache-tomcat-7.0.16/webapps/jpetstore.war) to your computer.
2. Select **Service catalog** from the banner.
3. Navigate (scroll down) to the Tomcat Application Model. ![Tomcat catalog item](te-tomcat-item.png?width=20pc) 
4. Select **Create**. The New Tomcat Application Model dialog appears.
5. In the **Application details** section, enter these field values:
    - **Application Name**: *jpetstore*
    - **Application Version**: *1.0*
    - **Application Project Name**: *Trial Guide*
6. Using the expansion controls on the right, expand the Artifact details section and provide this information:
    - **Group Id**: *com.acme*
    - **Artifact Key**: *jpetstore*
    - **Version**: *7.0.16*
    - **Filename**: *jpetstore.war*
![Tomcat Application details](te-tomcat-app-details.png?width=40pc) 
7. **File to upload**: Select **Choose File** to upload the jpetstore.war file you downloaded earlier.
8. Expand the Deployment details section and add this information:
    - **Retrieve to Folder**: */tmp*
    - **Tomcat Config**: *Tomcat*
    - **Context Path**: *jpetstore*
9. Select **OK** to generate the Application model. A "success" message is displayed and you are asked to navigate to the new Application model. ![Successful creation of Application model](te-ss-cataolog-success-msg.png?width=40pc)
10. Select **Yes** to navigate to the new application model.

## Create the QA environment

1. Select **Requires Setup** to open the Create Environment dialog. ![Map to Environment](te-ss-catalog-app-hier-menu.png?width=40pc)
2. Select **Create from this Application**. ![Create environment from application](te-tomcat-create-uat-env.png?width=40pc)
3. Enter QA for the environment name and select the project. Select **OK** to create the environment.
4. Select the Resources plus (**+**) button. ![Select Resources](te-ss-catalog-webtier-resources-plus.png?width=20pc)
5. Select **Add resources**.
6. Choose **tomcat_mysql_qa** then select **OK**.
7. Return to the application by selecting the **Application: jpetstore** link in the Hierarchy Menu.

## Create the UAT environment

1. Use the plus (+) option on **Map to Environment** to create the UAT environment. The New Environment dialog appears.
2. Select the resource **tomcat_mysql_uat**.
3. Navigate back to the application model.

## Deploy the application

1. Select **Run** and then **New Run**. The Deployment dialog appears.
2. Set **Deploy** to **QA** and turn off the **Smart Deploy**, **Check Dependency** and **Artifact Staging** options. Select **OK**. ![Run Application selections](te-run-app-selections.png?width=40pc)
3. Select the job name to examine the Job Details.
4. Select the resource where the application was deployed and note the IP address. ![Resource IP address](te-app-resource-details-ip.png?width=20pc)
5. Use the IP address of the resource to access the application. For example, **http://35.202.90.57:8080/jpetstore/** ![jepetstore-webpage](te-app-jpetstore-webpage.png?width=20pc)
6. Close the Job Details dialog to return to the Deployment run.
7. Navigate to the environment where the application was deployed, which is QA.
8. Examine the inventory.
9. Create a snapshot by selecting the snapshot (camera) icon. The New Snapshot dialog appears.
10. Enter version number 1.0 in the top field, and then select **Next**. You now have a snapshot of this artifact. ![Snapshot of artifact](te-app-snapshot-details.png?width=20pc)

