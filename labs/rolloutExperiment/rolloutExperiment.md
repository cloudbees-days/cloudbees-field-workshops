# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> Control the Value of a Flag with CloudBees Rollout


### Adding the Configuration Fetched Handler
The Configuration Fetched Handler allows us to control what happens whenever when a new configuration is fetched. In order for changes to be applied, an action has to take place, like a page refresh.
1. In Github, navigate to the `newSidebar` branch. Then, open flag.js file (`src/utils/flag.js`).
2. Insert the following code starting on line 6:
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
3. Make sure to include the `options` that contain the `configurationFetchedHandler` by adding it to the `Rox.setup()` call:
```javascript
Rox.setup("<ROLLOUT_ENV_KEY>", options);
```
4. The `flags.js` should be
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

### Control the Value of a Feature Flag
1. Navigate to the Rollout Dashboard.
2. On the left-hand side of the screen, click Production, and then Experiments from the expanded list. Then, click "Create a New Experiment" button.
<p><img src="images/ProdCreateNewExp.png" />

3. In the pop-up, ensure the "default.sidebar" flag is selected from the drop-down menu before clicking "Set Audience."
<p><img src="images/CreateNewSidebarExp.png" />

4. Right now, the sidebar is not shown because the value of the feature flag is set to `False` by default. Click on the drop-down menu next to then and select `True`. Finally, to update the `sidebar` flag's boolean value, click "Update Audience" button.
<p><img src="images/UpdateAudience.gif" />
	
5. Navigate back to the micro-blog and verify that the sidebar is now visible.
6. Congratulations! You have completed this lab and are ready.

TODO:
* Add next lab link for step 6
* Add image for micro-blog with sidebar shown to step 5