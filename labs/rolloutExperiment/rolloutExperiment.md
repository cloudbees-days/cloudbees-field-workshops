# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Control the Value of a Flag with CloudBees Rollout

### Control the Value of a Feature Flag

1. Navigate to the Rollout Dashboard.
2. On the left-hand side of the screen, click Development, and then Experiments from the expanded list. Then, click "Create a New Experiment" button.
<p><img src="images/ProdCreateNewExp.png" />

3. In the pop-up, ensure the "default.title" flag is selected from the drop-down menu before clicking **Set Audience**.
4. Right now, the title is not updated is not because the value of the feature flag is set to `False` by default. Click on the drop-down menu next to then, and select `True`. Finally, to update the `title` flag's boolean value, click "Update Audience" button.
<p><img src="images/UpdateAudience.gif" />

5. Navigate to the Microblog website, and ensure that the page refreshes automatically. Then the new title should appear!
6. Navigate back to the Rollout Dashboard.
7. On the left-hand side of the screen, click Development, and then Experiments from the expanded list. Then, click "Create a New Experiment" button. In the pop-up, select "default.sidebar" before clicking **Set Audience**.
<p><img src="images/CreateNewSidebarExp.png" />	
8. Remotely configure the value of the `sidebar` flag from `False` to `True`.
7. Navigate back to the Microblog website, and because the configurationFetchedHandler refreshes the page when a new configuration is seen, the changes should be applied!

### Flag Override
For local testing or development, we may need to specify values for each flags on our local machines. In order to do this without affecting others' work, we can implement the **Flag Override** and toggle the values as needed.

`src/components/Nav.vue`
1. In the Microblog header, click DEV. A pop-up window should appear in the lower right hand corner of the screen.
2. Right now, both `title` and `sidebar` flags are set to true. Select a different value and refresh the page. 
3. To simulate another tester on a different device, open the Microblog URL in a different internet browser. Again, click DEV in the header, and set the flags to different values, and refresh the page.
4. Each user (represented by the microblog in separate browsers) can now set their own personal feature flag values for local testing or development. Close this browser when finished. Back in origal browser, click **Reset All Overrides** from the FlagOverride menu, and refresh the page.
5. Navigate to the Github repository, and ensure you are on the `development` branch.
6. Navigate to `src/components/Nav.vue` by clicking the `src` folder, then `components` folder, and finally the `Nav.vue` file.
* Note that on **Line 16**, we are including the rolloutOverride view made available when clicked on the DEV link.
* The DEV link in the header is gated by the function `isDev`.
* The `Rox.showOverrides()` functionality is implemented by importing the `Rox` library on **Line 45** and defined on **Line 53**.
* Since we don't want end-users on `Production` to have this functionality, we gated the component with `isDev` defined on **Line 58**. This ensures that we only limit this functionality to lower level environments when CloudBees Core deploys from `development` branch

7. **For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1)**

Otherwise, you may proceed to the next lab: [**User Targeting**](../rolloutTargeting/rolloutTargeting.md) or choose another lab on the [main page](../../README.md#workshop-labs).
