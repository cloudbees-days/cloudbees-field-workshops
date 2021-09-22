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

1. Select the **Service catalog** link from the banner at the top. ![Service catalog in banner](te-service-catalog-banner.png?width=50pc) 
2. Create a new catalog by selecting the plus button (**+**) in the upper right.
3. Select **Create new** on the **New Catalog** dialog.
4. Provide a name for the catalog such as *Trial Catalog* and select your *Trial Project* target project for it, and then click **OK**. ![New Catalog dialog](te-service-catalog-new-dialog.png?width=50pc) 

## Add a catalog item

1. After you create the *Trial Catalog* the Service Catalog Item dialog appears. Enter a **name**, such as *Hello Catalog Item*, an item **description** and then click the **Define** button. ![New Catalog Item](te-service-catalog-new-item.png?width=50pc)
2. The New Catalog item definition dialog appears.
3. In the **Display** section, locate the **Select Button Label** field. Select **Execute**.

{{% notice note %}}
The **Button Label** of a Service Catalog Item is just a descriptive label of what end users should expect as an outcome of using the Service Catalog Item and does in any way control what the Service Catalog item does. Also, besides the explicit options there is also an **Other...** option that allows you to provide whatever label you want.
{{% /notice %}}

4. Next, in the search input for the icon, enter  *Automation* and select the **Automation** icon. ![Catalog Item label and icon](te-service-catalog-item-label-icon.png?width=50pc)
5. Scroll down to the **Definition** section.
6. Select the **Procedure** option on the left, and then select the project and procedure you created in the previous lab. ![Catalog Item definition](service-catalog-item-definition.png?width=50pc)

{{% notice note %}}
There are three types of Service Catalog Item definitions: DSL, Plugin and Procedure. You can learn more [here](https://docs.cloudbees.com/docs/cloudbees-cd/latest/self-service/#_catalog_items).
{{% /notice %}}

7. Select **OK** to save the Service Catalog Item definition.

## Run the Service Catalog item

1. At the top of the Service Catalog page, select **View Catalog**. ![Execute the catalog item](te-view-catalog-execute.png?width=50pc) 
2. Click the **Execute** button of the Service Catalog item you just created.
3. Select **OK**.
4. The Job Details appear. Verify that the procedure ran as expected.
