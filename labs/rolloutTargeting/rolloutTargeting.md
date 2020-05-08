# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> User Targeting in CloudBees Rollout

The goal of this lab is to use a property from our code, and allow users in the Rollout dashboard to create a ruleset such that the `sidebar` element is only visible to users that have successfully logged in.

### Using `setCustomProperty`

1. First we need to make sure the `isLoggedIn` function is available to the `flags.js` file. Navigate to the microblog-frontend repository in Github. In the `src\utils\flags.js` file, add the following import line on **Line 2**:
```javascript
import store from '../store'
```
2. To allow the Rollout dashboard to target specific users using the `isLoggedIn` property, we need pass the property from the code to the dashboard. This is a similar process to using `Rox.register` to make the flags visible to the dashboard. Before the `Rox.register` line, add the following line:
```javascript
Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);
```

3. The final `flags.js` should be
<details><summary>this:</summary>

```javascript
import Rox from 'rox-browser'
import store from '../store'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
};

export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
};

const options = {
  configurationFetchedHandler: configurationFetchedHandler
};

Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);

Rox.register('default', Flags);
Rox.setup(process.env.VUE_APP_ROLLOUT_KEY, options);
	
```
</details>

4. Create a commit message (e.g. "Added setCustomBooleanProperty"). Commit directly to the `development` branch. Then click **Commit changes**.

### Checking

1. Navigate to CloudBees Core.
2. Navigate to `microblog-frontend`
3. Open Blue Ocean
4. Click `development` branch to see the pipeline.
5. Click deploy, and the last shell script. Open the URL.

### Target Users Based on Properties
1. In the Rollout dashboard, on the left hand side of the screen, click **Development**, and then **Experiments** from the drop down menu.
2. Select the *sidebar** experiment.
3. Create a new condition by selecting **Add New Condition**. Instead of targeting **All Users**, select **Property**, then select the **isLoggedIn** and ensure it will check **isLoggedIn** is set to `True`. Then for this group the `sidebar` should be set to `True`.
4. In the `ELSE` condition, set the `sidebar` to `False` for all ussers and click **Update Audience**.
5. Navigate to the microblog to test the configuration logic. Log in with ther username `admin` and the password `admin` and then navigate back to the homepage. The sidebar should be displayed! Log out and see that it's hidden.

6. **For instructor led workshops please return to the [workshop slides](https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#1)**

Otherwise, you may proceed to the next lab: [**User Targeting**](../rolloutAnalytics/rolloutAnalytics.md) or choose another lab on the [main page](../../README.md#workshop-labs).