---
title: "Exploring the CloudBees CD/RO DSL"
chapter: false
weight: 7
--- 

The CloudBees CD/RO Domain Specific Language (DSL) can be used to manage configurations and also run CloudBees CD/RO APIs.

## Examine the DSL for the release

1. Use the breadcrumbs to navigate to the release definition, and then select **DSL Editor** from the banner at the top.
2. Make an edit, such as setting the plannedEndDate to a later date. Select the Save icon to apply the change.
3. Select **Release Editor** to view the change.

## Export the project DSL

1. Navigate to the project that you used to store the procedure, application, and release.
2. Select **DSL Export** from the project Actions menu.
3. Select **Export**. Save locally and examine the file contents.

## Use the DSL IDE to create a procedure

1. From the left navigation pane, select **DevOps Essentials > DSL IDE**.
2. Select **Procedure** from the **Examples** dropdown to access the sample DSL code to create a procedure.
3. Apply the DSL by selecting the **Run** button.
4. From the main menu, navigate to **DevOpsEssentials > Procedures**.
5. Use the filter to limit results to the Trial Project and the new procedure project, Hello Project. Select **Apply**.
6. Select the Run button, and then select **New Run**.
7. Select **OK**.
8. Examine the log for the *"Hello World"* message.

## Invoke the API command using the DSL IDE

1. Navigate to the DSL IDE.
2. Clear the editor and add the command `getUsers()`, and then apply the command.
3. From the **Examples** dropdown, select **Collect Objects**.
