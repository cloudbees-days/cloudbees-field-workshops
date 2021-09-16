---
title: "Creating and Running Procedures"
chapter: false
weight: 2
--- 

Procedures are the basic automation objects in CloudBees CD/RO. They are used to implement tool integrations and can be used for almost any automation task, such as running scripts and command line actions. They can also be used as one of the Service Catalog item types, as you will see in the next lab.

Procedures are made up of steps. A command step invokes a block of shell or script commands on a CloudBees CD/RO agent.

In this example, you create a very simple procedure that:

- Produces standard I/O output from a CloudBees CD/RO agent machine.


Because procedures run inside of projects, you must create a project first.

## Create a Project

Before you create a procedure, you need to create a container for the procedure, which is called a project. Projects are root-level objects that can contain procedures, pipelines, releases, applications, and other modeling objects. For more information about objects, see [Understanding CloudBees CD/RO objects](https://docs.cloudbees.com/docs/cloudbees-cdro-eval/latest/eval/objects).

To create a project:

1. Select the CloudBees CD/RO main menu (the hamburger icon in the top left). ![CD/RO main menu](te-cdro-main-menu-icon.png?width=25pc) 
2. Navigate to **DevOps Essentials > Projects**. The project list appears. ![Project list](te-main-menu-select-devops-projects.png?width=40pc) 
3. Select **New +** in the upper right. The **New Project** dialog appears.
4. Select **Create New**.
5. Enter the project name *Trial Guide* (or similar name) and then select **OK**. You will not be using credentials (secrets), so when asked if you want to create or edit credentials, select **No**.  

{{% notice note %}}
Although we are not using credentials with this simple procedure you will definitely need to create/use credentials from more complicated procedures. Credentials are used to access services and resources used during application deployments, release pipeline execution, or any other automated process orchestrated by CloudBees CD/RO. When a run-time object is configured to run as a specific user other than that defined at install time, CloudBees CD/RO retrieves the user name and password from a stored credential. The credential is passed to the CloudBees CD/RO agent over an encrypted channel so the agent can authenticate itself to the operating system and set up a security context where the object runs with the user permissions in the credential.
{{% /notice %}}

6. After the project is created, search for it by name by entering *Trial Guide* in the project search box and hitting **return**. When it is displayed, select the menu under **Actions** (three vertical dots) to access the project’s attributes. ![Search project](te-project-list.png?width=70pc) 

## Create a procedure

Now that you have a project to contain objects, do the following to create a procedure.

1. From the CloudBees CD/RO main menu (top left), navigate to **DevOps Essentials > Procedures**. The list of procedure objects displays.
2. Select **New +** in the upper right to add a procedure to your project. The **New procedure** dialog displays.
3. Select **Create New**.
4. Enter a procedure name such as *Trial Procedure*. Select the target project that you created above (for example, *Trial Guide*) and then select **OK** (the other default values are fine for this simple procedure). ![create procedure](te-add-procedure.png?width=70pc) 
5. You are now in a procedure. The **Hierarchy Menu** on the left appears, as well as a procedure menu on the right. ![procedures menu](te-procedures-menus.png?width=70pc) 

## Add a procedure step

In order for a procedure to actually do anything it needs 1 or more steps. When a procedure is first created, it has no steps to execute, so you must add steps.

1. Select the **There are no Steps. Add one +** link to begin adding a step. The **New Procedure Step** dialog appears.
2. Select **Create New**.
3. Provide a name, *Hello World*, and a description for the step — *A step to echo out a simple message*.
4. Select **Definition** in the upper right of the dialog to define the functionality of the step.
5. In the **Command** field, enter the following command to be run: 

```groovy
echo "Hello world"
```

6. Select **OK**. ![Add a new step to the procedure](te-new-procedure-step.png?width=70pc) 
7. Your *Hello World* step is displayed in the list of steps and the **Hierarchy Menu** of your *Trial Procedure*. ![Step list](te-procedure-step-list.png?width=70pc) 

## Run the procedure for the first time

1. Select the Run Procedure icon (green arrow) on the right, and then select **New Run**. The Run Procedure dialog box appears. Select **OK**. Note the job’s progress. ![Run procedure](te-run-procedure.png?width=70pc) 
2. View the job details by selecting **Procedure Runs** at the top of the page, then selecting the job number. Select the job once again to be able to view the log.
3. Select the icon under **Log** to view the job output. ![View the log after running a procedure](te-log-details-procedure.png?width=30pc)
4. You will now see the *Hello world* message.
5. Close the job dialog.
