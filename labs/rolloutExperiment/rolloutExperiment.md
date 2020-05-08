# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Control the Value of a Flag with CloudBees Rollout

### Control the Value of a Feature Flag

1. Navigate to the Rollout Dashboard.
2. On the left-hand side of the screen, click Production, and then Experiments from the expanded list. Then, click "Create a New Experiment" button.
<p><img src="images/ProdCreateNewExp.png" />

3. In the pop-up, ensure the "default.sidebar" flag is selected from the drop-down menu before clicking "Set Audience."
<p><img src="images/CreateNewSidebarExp.png" />

4. Right now, the sidebar is not shown because the value of the feature flag is set to `False` by default. Click on the drop-down menu next to then and select `True`. Finally, to update the `sidebar` flag's boolean value, click "Update Audience" button.
<p><img src="images/UpdateAudience.gif" />
	
5. Navigate back to the micro-blog. Since the `configurationFetchedHandler` calls a page refresh, you should that the sidebar is now visible.
6. **For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1)**

Otherwise, you may proceed to the next lab: [**User Targeting**](../rolloutTargeting/rolloutTargeting.md) or choose another lab on the [main page](../../README.md#workshop-labs).
