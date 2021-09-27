---
title: "User Targeting"
chapter: false
weight: 3
--- 

## Changing Flag Behavior for a Defined Audience
The goal of this lab is route a _subset_ of the microblog's audience to experience one value of a feature flag, while the rest of the users will see a separate value. The intended sub-group will be created in the CloudBees Feature Management interface and defined by properties in code, and then communicated to the CloudBees Feature Management dashboard through the `setup` function in the `flags.js` file. This lab will implement logic to _display the sidebar_ **only for logged in, Beta Users**.

### Add Properties from Code to CloudBees Feature Management Dashboard

1. First we need to make sure the `isLoggedIn` and `betaAccess` functions are available to be used in the `flags.js` file. Make sure you are on the `development` branch of the `microblog-frontend` repository, navigate to the `flags.js` file (`src/utils/flags.js`). Click the pencil icon to edit the file. ![Edit flags.js on development branch](images/edit-flags-deve-branch.png?width=50pc)
2. Allow `flags.js` to call `isLoggedIn` and `betaAccess` functions. Import `store` and `betaAccess` from their respective definition files. Starting on **Line 2**, include the following import calls:
```javascript
import store from '../store'
import { betaAccess } from './users'
```

3. The `isLoggedIn` and `betaAccess` boolean functions have to be communicated to the CloudBees Feature Management dashboard. To accomplish this, set up a `setCustomBooleanProperty` call for each of the functions. Before the `Rox.register` line, add the following lines:
```javascript
Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn)
Rox.setCustomBooleanProperty('hasBetaAccess', betaAccess())
```

4. Review your edits with updated code below:
{{%expand "expand for complete updated file" %}}

```javascript
import Rox from 'rox-browser'
import store from '../store'
import { betaAccess } from './users'

export const Flags = 
  {
  sidebar: new Rox.Flag(false),
  title: new Rox.Flag(false)
}

export const configurationFetchedHandler = fetcherResults => {
  console.log('The configuration status is: ' + fetcherResults.fetcherStatus)
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  } else if (fetcherResults.fetcherStatus === 'ERROR_FETCH_FAILED') {
    console.log('Error occured! Details are: ' + fetcherResults.errorDetails)
  }
}

async function initCloudBees () {
    const options = {
    configurationFetchedHandler: configurationFetchedHandler
  }
  Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn)
  Rox.setCustomBooleanProperty('hasBetaAccess', betaAccess())
  Rox.register('default', Flags);
  await Rox.setup(process.env.VUE_APP_CLOUDBEES_KEY, options);
}

initCloudBees().then(function () {
  console.log('Done loading CloudBees Feature Management')
})

```
{{% /expand%}}

5. Create a commit message (e.g. "Added setCustomBooleanProperty"). **Commit changes** directly to the `development` branch.
6. Once the commit has finished being built on the open pull request, open the new deployment URL so that the properties can be created to the Feature Management dashboard.

### Create a Target Group Based on Custom Properties

1. In the CloudBees Feature Management dashboard, navigate to the **Target Groups** displayed on the left. Select the **Create a New Group** button in the middle of the resulting page.
2. We are going to create a new Target Group, _useful when defined by 2 or more `customProperties`_. Enter ***BetaUsers*** as the **Name** of the new group, a subset that will be defined by the `isLoggedIn` and `betaAccess` properties.
3. A microblog user is considered part of the **BetaUsers** group when **both** of the following conditions are met:
   * `isLoggedIn` is **True**
   * `hasBetaAccess` is **True**
   * Reflect this logic in the **BetaUsers** Target Group Window be defining the first **Condition** as `isLoggedIn` **Is True**. Then, **Add a New Condition**, select the ***Matches All Conditions*** option, and the select the `betaAccess` **Property** as **Is True**.

4. Once your **BetaUsers** New Target Group definition looks similar to screenshot below click **Create Group** button so it can be used in experiments. ![New target group](images/new-target-group.png?width=50pc)


### Using a Target Group in a Configuration

1. Within the CloudBees Feature Management dashboard, navigate to the **Development** environment, and click on the **sidebar** configuration.
2. Create a new condition by selecting **Add New Condition**. Within the new condition, change the audience selection from **All Users** to **Target Group**. Edit the remainder of the `if` condition block so that _for a Target Group that matches any of BetaUsers, the sidebar flag value is ***True***.
3. Edit the older condition that became the `else` block such that the sidebar flag value will be **False**. The configuration modifications should match the following screenshot. ![Update sidebar experiment](images/update-sidebar-experiment.png?width=50pc)
4. Apply the configuration changes by clicking **Save Targeting**.
5. Navigate to the microblog website to test the configuration logic.
   * Log in with the username `admin` and the password `admin` and then navigate back to the homepage. The sidebar should be hidden!
   * Log out, and sign in with the username `betauser` and `betauser` password. Upon, navigating back to the homepage the sidebar is now displayed (you may need to refresh the browser page), as we configured it to be _only for Beta Users_.

### Lab 3 Completed!
Congratulations! You have finished Lab 3 of the CloudBees Feature Management Workshop.

**For instructor led workshops please <a href="https://cloudbees-days.github.io/cloudbees-field-workshops/cloudbees-feature-management/#27">return to the workshop slides</a>**
