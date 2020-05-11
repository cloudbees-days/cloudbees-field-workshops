# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Control the Value of a Flag with CloudBees Rollout

## Control the Value of a Feature Flag
In this lab, you will use the CloudBees Rollout dashboard to remotely configure the values of the `title` and `sidebar` feature flags. Additionally, we will introduce the Flag Override tool, and walk through a scenario where developers may need to alter a flag's for local testing without affecting the values for others.

### Creating a Rollout Experiment

1. Bring up to the Rollout Dashboard.
2. On the left-hand side of the screen, click the **Development** environment, and then select **Experiments** from the expanded list. From the view that follows, click the **Create a New Experiment** button.

<p><img src="images/ProdCreateNewExp.png" />

3. In the pop-up menu, choose the "default.title" flag from the drop-down. To set up the experiment, choose the **Set Audience** button.
4. Right now, the new title is hidden for all. And the title experiment reflects this: the only condition uses the `title` flag's default value (False). This default experiment is set for the audience defined on **All Versions** (the microblog only has 1 version) and **All Users**.
5. Let's change the flag's experiment so that all users will see the new title. Click the current **False** behavior value, and from the drop-down menu, choose **True** to edit the `title` flag experiment.
6. When changes to an experiment are applied, a new configuration file is written and delivered to the devices. Select **Update Audience** button to send the new configuration with its updated `title` flag value.
<p><img src="images/UpdateAudience.gif" />

7. Switch tabs to bring up the Microblog website. Thanks to the `configurationFetchedHandler` implemented in the previous lab, the page refreshes automatically and the new configuration applied. Then the new title should appear!
8. Switch tabs to bring CloudBees Core into view. The _most recent_ should be the deployment induced from adding the configurationFetchedHandler to `flags.js` in the previous lab. We have successfully changed the behavior of feature flag gated code from an dashboard and **without additional code deployments**. 
6. Navigate back to the Rollout dashboard.
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
