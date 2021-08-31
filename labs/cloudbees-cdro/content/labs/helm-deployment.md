---
title: "Running a Helm Chart Deployment"
chapter: false
weight: 5
--- 

In this lab, you create an application model that runs a Helm chart deployment.

## Application Model Helm Chart Deployment

1. From the main menu, navigate to Deployment Automation Applications. ![Applications from main menu](te-main-menu-applications.png?width=20pc)
2. Select **New**. The New Application dialog appears.
3. Select **Create New**.
4. Fill in the Application name, RSS and select the project, Trial Guide. Select the Application type **Microservice**, and then select **OK**.
5. Select the New microservice icon (**+**) to define the new microservice. ![Add a new microservice](te-helm-new-microservices.png?width=40pc)
6. Select Next to use the default New microservices selection.
7. In the New microservice dialog, complete the information as follows:
    - **Name**: *freshrss*
    - **Definition type**: Helm
    - **Definition source**: Helm repository
    - **Repository URL**: https://halkeye.github.io/helm-charts
    - **Repository name**: *halkeye*
    - **Release name**: *freshrss*
    - **Chart**: *halkeye/freshss*
8. Add the following code for the additional options:
```
--set=ingress.enabled=true
--set=ingress.hosts[0]=$[/javascript server.hostName.replace("sda","$[/myJob/ec_microservice_deployment_parameters/$[/myMicroservice]/clusterDefinition/namespace]")]
```
9. Select **OK**.
10. In the **New environment** object, select the New cluster (**+**) button. ![Add a new cluster](te-helm-new-cluster.png?width=40pc)
11. Select **Next** to accept the default action to create a new environment.
12. In the **Edit microservice** dialog, complete the information as follows:
    - Enter the Environment name as RSS - QA.
    - Select the **Trial Guide** project. In the **Cluster name** field, enter qa.
    - In **Configuration provider**, select **Kubernetes - Helm**.
    - In **Configuration name**, select **Helm**.
    - In **Utility resource name**, enter "Kubernetes".
    - In **Resource**, select **k8s-agent**.
    - Select **OK**.
![Mapped RSS-QA environment](te-helm-mapped-enviro.png?width=40pc)
13. Create the RSS - UAT environment. Select the plus sign (**+**) the RSS - QA environment and perform the steps above again but this time using **uat** instead of **qa**.

{{% notice tip %}}
If the **Deploy** button is not activated, make sure the microservice is mapped to the new environment. Select the **freshrss** Helm component menu and select **Add Mapping**. Drag the end point to the **RSS - UAT** environment.
{{% /notice %}}
![Mapped RSS-UAT environment](te-helm-mapped-rss-uat.png?width=40pc)
14. Select **Deploy Application** and **RSS - QA** as the target environment.
15. To view the inventory, select the **RSS - QA** link from the bread crumb, then select Inventory.
16. View the microservices deployment details by selecting **Details** from the menu for freshrss microservice.
17. Access the application. Note the URL above on line 10; this URL can be used to access the deployed application.
