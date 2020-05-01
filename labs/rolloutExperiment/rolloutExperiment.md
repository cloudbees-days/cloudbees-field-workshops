# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Control the Value of a Flag with CloudBees Rollout


### Adding the Configuration Fetched Handler

The Configuration Fetched Handler allows us to control what happens whenever when a new configuration is fetched. In order for changes to be applied, an action has to take place, like a page refresh.
1. In Github, navigate to the root directory of the microblog-frontend repository.
2. Click `Branch: newSidebar`
3. Type `experiment` then click **Create branch: experiment from newSidebar** to finish creating a new branch.
4. Navigate to the `experiment` branch. Then, open flag.js file (`src/utils/flag.js`).
5. Insert the following code starting on line 6:
```javascript
export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
};
const options = {
  configurationFetchedHandler: configurationFetchedHandler
};
```
6. Make sure to include the `options` that contain the `configurationFetchedHandler` by adding it to the `Rox.setup()` call:
```javascript
Rox.setup("<ROLLOUT_ENV_KEY>", options);
```
7. The `flags.js` should be
<details><summary>this:</summary>

```javascript
import Rox from 'rox-browser'
import { store } from '../store'

export const Flags = {
  sidebar: new Rox.Flag(false)
};

export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
};
const options = {
  configurationFetchedHandler: configurationFetchedHandler
};

Rox.register('default', Flags);
Rox.setup("<ROLLOUT_ENV_KEY>", options);
	
```
</details>
8. Create a commit message and select **Commit directly to the `experiment` branch** radio button.
9. Click **Commit new file**
10. **Need to edit** Create a pull request from experiment to `Development` branch. Merge.
11. **Need to edit** Open the URL produced from the Core Development branch job.

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
