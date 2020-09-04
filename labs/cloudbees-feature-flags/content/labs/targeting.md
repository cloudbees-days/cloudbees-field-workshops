---
title: "User Targeting in CloudBees Feature Flags"
chapter: false
weight: 3
--- 

## Changing Flag Behavior for a Defined Audience
The goal of this lab is route a _subset_ of the microblog's audience to experience one value of a feature flag, while the rest of the users will see a separate value. The intended sub-group that will be created in the CloudBees Feature Flags interface and defined by properties in code and communicated to the CloudBees Feature Flags dashboard through the `setup` function in the `flags.js` file. This lab will implement logic to _display the sidebar_ **only for logged in, Beta Users**.

### Add Properties from Code to CloudBees Feature Flags Dashboard

1. First we need to make sure the `isLoggedIn` and `betaAccess` functions are available to be used in the `flags.js` file. In the `development` branch of the microblog repository, navigate to the `flags.js` file (`src/utils/flags.js`). Click the pencil icon to edit the file.
2. Allow `flags.js` to call `isLoggedIn` and `betaAccess` functions. Import `store` and `betaAccess` from their respective definition files. Starting on **Line 2**, include the following import calls:
```javascript
import store from '../store'
import { betaAccess } from './users'
```

3. The `isLoggedIn` and `betaAccess` boolean functions have to be communicated to the CloudBees Feature Flags dashboard. To accomplish this, set up a `setCustomBooleanProperty` call for each of the functions. Before the `Rox.register` line, add the following lines:
```javascript
Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);
Rox.setCustomBooleanProperty('hasBetaAccess', betaAccess());
```

4. Review your edits with updated code below
<details><summary>Updated <code>flags.js</code></summary>

```javascript
import Rox from 'rox-browser'
import store from '../store'
import { betaAccess } from './users'

export const Flags = {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
};

export const configurationFetchedHandler = fetcherResults => {
  console.log('The configuration status is: ' + fetcherResults.fetcherStatus)
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
  else if (fetcherResults.fetcherStatus === 'ERROR_FETCH_FAILED') {
    console.log('Error occured! Details are: ' + fetcherResults.errorDetails)
  }
};

const options = {
  configurationFetchedHandler: configurationFetchedHandler
};

Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);
Rox.setCustomBooleanProperty('hasBetaAccess', betaAccess());

Rox.register('default', Flags);
Rox.setup(process.env.VUE_APP_ROLLOUT_KEY, options);

```
</details>

5. Create a commit message (e.g. "Added setCustomBooleanProperty"). **Commit changes** directly to the `development` branch.

### Segment Title Experiment Using A Single Property

1. Switch tabs to bring up the microblog website. To check the current width, bring up Developer Tools. In the console, type `window.innerWidth` and note the value returned.
2. We will initially segment a flag's value based on a _single_ property (`rox.screen_width`). Bring up the CloudBees Feature Flags dashboard, and within the Development environment view, select the **title** experiment.
3. To segment users, we need to select **Add New Condition** that begins to create the `if-else` structure of the resulting configuration.
4. We will limit the availability of the title feature to a subset of users, an audience defined by the screen's width property as the sole criterion. Within this newly added condition, change **All Users** to **Property** match. Set the new condition's remaining behavior such that _if the rox.screen_width is less than or equal to `<=` **half** of the width value returned from Step 1, **then** the title flag should be **True**_.
5. Edit the older condition that became the **else** block, such that the _title flag is **False**_.
6. Apply this new segmented audience experiment by clicking **Update Audience**.
7. Switch tabs to bring the Microblog's website into view. Copy your unique Microblog URL. _Open a new private browser window_ such that there is only one tab in the new session with a clear cache. Bring up **Developer Tools**, and modify the session's screen width to be _less than the value set in title's experiment_. Only after the session window has been resized, **paste** and go to your Microblog URL. The new title should be displayed in this size, but not in the larger sized browsing session. After noting the distinction, close Developer Tools and the smaller sized browsing session.

### Create a Target Group Based on Custom Properties

1. In the CloudBees Feature Flags dashboard, navigate to the **Target Groups** displayed on the left. Select the **Create a New Group** button in the middle of the resulting page.
2. We are going to create a new Target Group, _useful when defined by 2 or more `customProperties`_. First name the new group **BetaUsers**, a subset that will be defined by the `isLoggedIn` and `betaAccess` properties.
3. A microblog user is considered part of the **BetaUsers** group when **both** of the following conditions are met:
* `isLoggedIn` is **True**
* `hasBetaAccess` is **True**

Reflect this logic in the **BetaUsers** Target Group Window by _first_ defining that the `isLoggedIn` property is **True**. Then, **Add a New Condition**, select the subsequent _Matches All Conditions_ option, and ensure that `betaAccess` must also be **True**.

4. The **BetaUsers** Target Group definition should look similar to that below. Then click **Create Group** so the defined Target Group can be used in experiments.


### Using a Target Group in an Experiment

1. Within the CloudBees Feature Flags dashboard, navigate to the **Development** experiment, and bring up the **sidebar** experiment.
2. Create a new condition by selecting **Add New Condition**. Within new condition, change the audience selection from **All Users** to **Target Group**. Edit the remainder of the `if` condition block so that _for a Target Group that matches any of BetaUsers, the sidebar flag value is **True**_.
3. Edit the older condition that became the `else` block such that the sidebar flag value will be **False**. The experiment modifications should be appear similar to the below image.

4. Apply the experimentation changes through clicking **Update Audience**.
5. Navigate to the microblog website to test the configuration logic.
* Log in with the username `admin` and the password `admin` and then navigate back to the homepage. The sidebar should be hidden!
* Log out, and sign in with the username `betauser` and `betauser` password. Upon, navigating back to the homepage the sidebar is now displayed, as we configured it to be _only for Beta Users_.

### Lab 4 Completed!
Congratulations! You have finished Lab 4 of the CloudBees Feature Flags Workshop.

**For instructor led workshops please return to the workshop slides: https://cloudbees-days.github.io/core-rollout-flow-workshop/rollout/#27**
