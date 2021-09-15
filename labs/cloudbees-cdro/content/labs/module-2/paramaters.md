---
title: "Parameters for Procedures"
chapter: false
weight: 5
--- 

Each procedure can define parameters, which are values provided to the procedure when it is invoked. Each parameter value is placed in a property associated with the job and the procedure can use the property to control its execution. For example, a parameter might specify a particular branch of a product to build; another parameter might indicate whether unit tests should be run during this build.

When you define a parameter, indicate whether the parameter is required (meaning the procedure will not run unless a value is provided for the parameter). Also, you can provide a default parameter value and a description to help callers understand how to use the parameter.

In this lab you will update the procedure you created in *Module 1* by adding different types of parameters to include:

- Accepts input from parameters (both static and dynamic).
- Runs steps conditionally.

You also customize the runtime job name and step summaries.

## Add a parameter

1. From the breadcrumb at the top of the window, return to the procedure by selecting **Trial Procedure**.
2. Open the Procedure menu on the right and then select **Parameters**. ![Procedures menu](te-procedure-menu.png?width=30pc)
3. Add a parameter by selecting **There are no Parameters. Add one +**. The New Input Parameter dialog appears.
4. Provide the the following values:
    - **Name** - *greetName*
    - **Description** - *Name to use for the "Hello" greeting*
    - **Label** - *Greet Name*
5. Select **Custom Validation** to enter a validation script. ![New input parameter](te-new-input-param.png?width=70pc)
6. In the **Provide DSL** box, enter the following DSL code. This code prevents entries that include the space character.
```groovy
if(args.parameters['greetName']?.contains(" "))
    return "No spaces allowed!"
else
    return null
```
7. Select **OK**.

{{% notice note %}}
When the validation script is saved, CloudBees CD/RO runs the DSL script to validate it. The `args.parameters['greetName']` returns null in this context because the parameter hasn’t been set yet. The question mark tells DSL to ignore what follows when this is null.
{{% /notice %}}

8. Select **OK** to complete the parameter definition.
9. To exit the Parameters dialog, select **X** in the upper left or the **Esc** key.

## Use the parameter in a step

1. Duplicate the Hello World step by selecting the Step icon in the upper right, or the plus **(+)** next to **Steps** in the Hierarchy Menu on the left.
2. Select **Copy Existing**.
3. Select the *Hello World* step to copy.
4. Enter the new step name *Hello <greetName>* and update the description with the text: *A step to echo out a greeting to someone*. Select **OK**. (The new step name appears after the step is saved.)
5. To edit the new step, select the step name or select **Step Definition** under the Actions menu.
6. Modify the command block so that it includes only the command: `echo "Hello $[greetName]"` ![Edit the command](te-edit-command-in-param.png?width=50pc)
7. Select **OK**.

## Run the modified procedure

1. Select the Run Procedure button (green arrow) to select a run option.
2. Select either **New Run** or **Last Run**. The latter will remember any user-supplied parameter settings. (In this case, there were none, so both options behave the same way.)
3. Try supplying this name, which includes spaces: *A DevOps Guru*. (Because of the validation code you supplied, this parameter field does not accept such an entry.)
4. Now enter the name *DevOpsGuru* (without spaces) and select **OK**. ![Run modified procedure](te-run-trial-procedure-1.png?width=50pc)
5. Navigate to the Job Details using the **Action** menu and examine the step’s log file. You should see **Hello DevOpsGuru**.
6. Exit this job’s dialog.

{{% notice tip %}}
The **Rerun** button (green arrow in a circle) can be used to run the procedure again with this job’s parameter values already filled in, based on the previous run.
{{% /notice %}}

## Create a multi-option parameter

Create a new input parameter that enables you to select from a list of options before running the procedure.

1. Navigate to the procedure using the breadcrumbs.
2. Using the **Procedure** menu on the right, select **Parameters**. The Parameters dialog appears.
3. Create a new input parameter by selecting **Input+** in the upper right. Supply the following information:
    - **Name** - *cdUser*
    - **Description** - *A list of users from CloudBees CD*
    - **Label** - *CD User*
4. In **Parameter Type**, select **Dropdown Menu**, and then select **Load options using DSL**.
5. Supply the following DSL code:

```groovy
import com.electriccloud.domain.FormalParameterOptionsResult

def options = new FormalParameterOptionsResult()
getUsers().users.each { aUser -> options.add(aUser.userName, aUser.fullUserName)}
return options
```
![New input parameter](te-input-param-cdUser.png?width=70pc)

6. Select **OK** to save the new parameter and then close the Parameters dialog. You are returned to the step object list.

## Use the multi-option parameter in a step

Duplicate the second step and modify it to use the new parameter.

1. From the list of step objects, create a new step using one of the methods discussed earlier.
2. In the New Procedure Step dialog, select **Copy Existing**, and then select the Hello <greetName> step.
3. Change the name of the step to Hello CD User.
4. Select **Definition**.
5. Modify the Command block to include the parameter substitution `$[cdUser]` so that the new command block is `echo "Hello $[cdUser]"`.
6. Select **OK**.

### Rerun the procedure

1. Select the Run button (green arrow) and then select **Last Run**.
2. Fill in the parameter values. The pull-down options are populated with a list of users that have been defined in your CloudBees CD/RO instance. ![Rerun procedure with parameter values](te-run-cduser.png?width=60pc)
3. To view the step log for the Hello CD User step, select **Job Details** from the **Actions** menu, then select the **View Log** icon in the upper right. You should see your "Hello" text displayed.

## Customize the job name and job step summary

Now, modify the procedure to create a job name based on the name of the procedure and a count.

1. Navigate to the Trial Procedure editor using the breadcrumb, and then select **Details** from the Procedure menu on the right.
2. In the **Job Name Template** field, add the following syntax to override the blank default value:
```groovy
$[/myProcedure]-$[/increment /myProcedure/count]
```
3. This code creates a job name based on the name of the procedure (from `/myProcedure`) and a property (count) stored on the procedure property sheet (`/myProcedure`). The increment function creates the property if it doesn’t exist, and increments it by one.
4. Select **OK**.
5. Edit the last step definition using the **Action** menu. In the **Command** field, below the echo command, add the following:
```groovy
ectool setProperty /myJobStep/summary "Hello $[cdUser]"
```
![Edit step command](te-edit-hello-command.png?width=50pc)

## Run the procedure with the new job name

1. Select the Run button and select **Last Run**. Note the new job name format.
2. Navigate to the job details and note the new job step summary value.

## Create and use an output parameter

Navigate to the Trial procedure to create an output parameter.

1. From the Trial procedure, select the Procedure menu on the right, and then select **Parameters**. The Parameters dialog appears.
2. Select the **Output Parameters** tab and add an output parameter called **whoRanMe**. ![Add an output parameter](te-add-output-param.png?width=30pc)
3. Add a new procedure step and name it *Set output parameter*.

{{% notice tip %}}
Select the **+** beside **Steps** in the Hierarchy Menu to add a step.
{{% /notice %}}

4. Navigate to the **Definition** tab.
5. Add the following shell command in the **Command** field:
```groovy
ectool setOutputParameter whoRanMe "$[/myJob/launchedByUser]"
```
6. Select **OK**.
7. Run the procedure using the **Last Run** option to reuse the parameter values previously entered.
8. Navigate to the job details and select **Parameters**. Note that the **Output Parameter** value *whoRanMe* is set as expected.

## Create a step condition

1. Navigate to the procedure editor using the breadcrumb.
2. Open the first step, *Hello World*, and select the **Condition** tab on the upper right.
3. Add the following **Run Condition** (not **Precondition**) expression so that the step runs only after the procedure has been run five times:
```groovy
$[/javascript myProcedure.count > 5]
```
4. Select **OK**.
5. Run the procedure. Use the **Last Run** option.
6. Select **Rerun** a few more times.

Note that the *Hello World* step runs after the count property exceeds five. Here is an example of the results after eight runs.
![Example after eight runs](te-trial-procedure-run-count.png?width=70pc)