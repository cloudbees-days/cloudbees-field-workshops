---
title: "Creating a Service Catalog Item"
chapter: false
weight: 3
--- 

Use the CloudBees CD/RO Service Catalog to package up easy-to-use functionality such as:

- **Creating models from parameterized templates**

    Create models from templates by wrapping DSL code that is executed by a Service Catalog item.

- **Running custom automation**

    Invoke a procedure from a Service Catalog item to implement automated tasks.

In this lab you will create a Service Catalog, and then create and run a [procedure based Service Catalog item](https://docs.cloudbees.com/docs/cloudbees-cd/latest/self-service/#_procedure_based_catalog_items) using the procedure you created earlier.

## Create a new catalog

1. Select **Service catalog** from the banner at the top. ![Service catalog in banner](te-service-catalog-banner.png?width=50pc) 
2. Create a new catalog by selecting the plus button (**+**) in the upper right.
3. Select **Create new** on the **New Catalog** dialog.
4. Provide a name for the catalog such as *Trial Catalog* and select your *Trial Project* target project for it, and then click **OK**. ![New Catalog dialog](te-service-catalog-new-dialog.png?width=50pc) 

## Add a catalog item

1. Select the (**+**) beside the New Catalog Item icon in the upper right. The New Catalog dialog appears.
2. Provide a name such as Hello Catalog Item and a description item, and then select **Done**.

## Add a procedure to the item definition

1. Select **Requires Definition**. The New Catalog Item dialog appears.
2. In the **Display** section, locate the **Select Button Label** field. Select **Execute**.
3. Scroll down to display the **Definition** section.
4. Select the **Procedure** option on the left, and then select the project and procedure you created earlier.
5. Select **OK**.

## Run the catalog item with parameter values

1. At the top of the service catalog, select **View Catalog**. ![Execute the catalog item](te-view-catalog-execute.png?width=50pc) 
2. Select **Execute** on the catalog item.
3. Provide input parameter values (for example, **Greet Name** is **ScrumMaster**). In the **CD User** field, select from the drop-down. Select **OK**.
4. The Job Details appear. Verify that the procedure ran as expected.
