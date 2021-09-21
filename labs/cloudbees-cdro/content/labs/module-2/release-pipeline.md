---
title: "Running a Release Pipeline"
chapter: false
weight: 3
--- 

Releases are used to manage the tasks associated with releasing multiple applications or components together.

Perform these steps to create and run a CloudBees CD/RO release pipeline that does the following:
- Invokes the procedure
- Invokes the Tomcat and Helm Chart application models you created in earlier examples
- Implements manual and automated gates

## Create a new release

1. From the main menu, navigate to **Release Orchestration > Releases**. ![Releases from main menu](te-main-menu-releases.png?width=20pc) 
2. Select **There are no releases. Add one +** or **New +**. The New Release dialog appears.
3. Provide a release name such as Trial Release, and select a project (for example, Trial Guide).
4. Select **OK** to create the new release definition.

## Add stage details

1. Rename the stage from **Stage 1** to QA.
    - Select the stage menu on the right and then select **Stage Details**.
    - Enter QA for the name of the stage, then select **OK** to save the change.
2. Create a stage called UAT.
    - From the Hierarchy Menu on the left, select the plus (**+**) next to Stages. The New Stage Dialog appears. ![Add a stage from the Hierarchy Menu](te-release-add-stage.png?width=40pc) 
    - In the New Stage dialog, enter name UAT and then select **OK** to create the new stage.

## Add a procedure task

1. Add the procedure created earlier to the QA stage. ![Add procedure to QA stage](te-release-add-procedure.png?width=20pc) 
2. Select **Add +**.
3. Enter a task name such as Greeting, then select **Select Task Type**.
4. Select **Procedure** as the task type. ![Select task type](te-release-task-type.png?width=40pc) 
5. Select **Define** in the New Task box.
6. Select the project and procedure for the procedure definition you created earlier. Then select the right arrow beside **Input Parameters** to enter the parameters. ![Add input Parameters](te-release-input-params.png?width=40pc)
7. Provide parameter values:
    - In the **Greet Name** field, enter **DevOpsGuru**.
    - In the CD User field, select one of the users from the list.
8. Select **OK**.
9. Select the right arrow beside the **Output Parameter**. Check the **Show in Stage Summary as** box, and then select **OK** to save the task definition.

## Start the release and run the release pipeline

1. Select the **Run** button, and then select **Start Release**. ![Start the release](te-release-start.png?width=20pc) 
2. Select **Run**. Note the stages running.
3. Once complete, select the **Summary** link on the **QA** stage and note how the procedure output was propagated up.
4. Select the task name to view the job details, and then close the dialog to continue.

## Add a pipeline parameter

1. Use the breadcrumbs to return to the release definition editor. ![Trial release definition editor](te-release-breadcrumb.png?width=30pc) 
2. From the Hierarchy Menu, select the context menu beside the **Pipeline: pipeline_Trial Release**.
3. Select **Parameters** and add a parameter, *helloUser*.
4. Select **OK** to save, and then exit the Parameters dialog.
5. Modify the task to use the parameter value.

{{% notice tip %}}
Select the task name.
{{% /notice %}}

6. Modify the procedure task Greet Name to be `$[helloUser]`.

## Run the release pipeline

1. From the release options menu on the right, select **Last Run**, and then select **Run**. ![Rerun the pipeline](te-release-last-run.png?width=20pc)
2. To see where this value was applied, look at the job results.

{{% notice tip %}}
Display the job details by selecting the task name.
{{% /notice %}}

3. Open the log associated with the **Hello <greetName>** step.
4. Examine the pipeline runtime properties and parameters.
    - Select **Pipeline Runs** at the top of the screen.
    - Select the Actions menu to view the properties and parameters.
    - Select Expand to view the tasks. Select the task menu button to view the task properties. ![View task properties](te-release-task-properties.png?width=20pc)
    - Open the Jobs Details to view the job properties and parameters.

## Add a manual gate

1. Use the breadcrumbs to navigate back to the release definition editor.
2. Select the **+** on the upper right side of a task to open the gates view. Select **Add +** to create a new rule for the gate.
3. Provide a name for the new rule, such as Approve. Select **Select Rule type** and **Approval** as the type.
4. Select **Define**.
5. Enter your username under **Assignees**, and then select **OK** to complete the gate definition. ![Edit a gate rule](te-release-edit-rule.png?width=40pc)

## Run a new release pipeline

1. In the Actions menu, select the **Last Run** option to reuse the parameter value you selected earlier, and then select **Run**.
2. The pipeline halts because it is waiting for the manual approval. (If configured, an email will also be sent with options to approve).
3. Select the **Response required** pull-down to select the user designated to approve.
4. Select **Approve** and provide a comment, and then select **OK**.

## Examine the audit report

1. Use the pipeline runtime Actions menu to access the audit reports. 
2. Select **Audit Reports**.

## Add a deployer to each stage

1. Use the breadcrumb to return to the release definition editor. Add a new task called *Deploy* in each stage. ![Add a Deploy task](te-release-add-deploy.png?width=40pc)
2. Select Select Task Type and choose Deployer for both Deploy tasks.
3. Select Define.
4. Select Deploy Serially.
5. Select OK to complete the task definition.

## Add the applications to the release

1. In the Hierarchy Menu on the left, select the plus (+) next to **Applications and Microservices**. ![Add the application to the release](te-release-add-application.png?width=40pc)
2. Select both applications, and select the blue double-arrow button (**>>**) to add the applications. Then select the back button (**<**) to close the selection view.
3. Select the snapshot for the jpetstore application that you created earlier.
4. Select **OK**.

## Configure the application to run in QA and UAT environments

1. Select the right arrow next to **Environments and Configurations** in the Hierarchy Menu on the left.
2. Select the cell under the QA column for **jpetstore** and then select the **Environment** tab.
3. Select the QA environment from the Trial Guide project, and then select **OK**.
4. Select the **Process** tab, and then select **Deploy**. ![Deploy QA environment](te-release-deployQA-env.png?width=40pc)
5. Do the same for the jpetstore application under **UAT**. But this time, select the **Trial Guide UAT** environment.
6. Similarly, set up the RSS application to point to the Helm Deploy QA and UAT environments. ![Configure all environments](te-release-envs-configs.png?width=40pc)
7. Select **OK** to save the environment configuration.

## Run the final release pipeline

1. Select the Actions menu, and then select **Last Run**.
2. Once the Deploy task has started, select **Summary** in the QA stage. ![View the stage summary](te-release-stage-summary.png?width=40pc)
3. Allow the release pipeline to complete.
4. Provide the required response to continue the pipeline. Note the new path to production view.
5. Select the Actions menu, and then select **Audit Reports** to view the Audit Report.
