# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> CloudBees Rollout and Analytics

## Forwarding Flag Data to Analytics Platform
This lab will leverage CloudBees Rollout's `impressionHandler` to forward flag information to a more robust analytics platform (we will use Google Analytics for this lab, but the abstracted process remains the same for integration with other tools). We can pass information about feature flags values evaluated on each client back for analysis. We'll set-up the beginning process for A/B testing process.


### Adding the ImpressionHandler to Code
**TO DO, add brief explanation on the ImpressionHandler**

1. Switch tabs to bring up the microblog-frontend repository. Within the root directory, on the `development` branch, navigate to the public folder. Then select the `index.html` file.
2. Google Analytics requires a site tag. Select the pencil icon to edit the `index.html` file, and remove the comments on **Line 5** and **Line 13** so that the `gtag.js` can be seen.

3. Review the edits below in
<details><summary>Updated <code>index.html</code></summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-165275127-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-165275127-1');
    </script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title>microblog</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css">
</head>
<body>
<noscript>
    <strong>We're sorry but microblog-frontend doesn't work properly without JavaScript enabled. Please enable it to
        continue.</strong>
</noscript>
<div id="app"></div>
<!-- built files will be auto injected -->
</body>
</html>

```
</details>

4. Create a commit message (e.g. "insert gtag.js"). Then **Commit changes** directly to `development` branch.
5. From the microblog's root directory on the `development` branch, navigate to the `flags.js` file (`src/utils/flags.js`).
6. We want to send data to Google Analytics, but may only want to send _some_ of the flag data, like only if the flag data is used in our A/B **title** experiment. Click the pencil to edit the file. On **Line 16** insert a new line then implement `impresionHandler` constant seen below:
```javascript
export const impressionHandler = (reporting, experiment) => {
  if (experiment.name === 'title') {
    console.log('Title flag, ' + reporting.name + ' ,value is ' + reporting.value)
    gtag('event', experiment.name, {
      'event_category': reporting.name,
      'event_label': reporting.value
    })
  } else {
    console.log('Not in title experiment. Flag ' + reporting.name + '. default value ' + reporting.value + ' was used')
  }
};
```

7. Within the `options` constant, include a call to the newly defined `impressionHandler`. After the configurationFetchedHandler call, insert a comma then and make the `impressionHandler` part of the options as seen below:
```javascript
const options = {
  configurationFetchedHandler: configurationFetchedHandler,
  impressionHandler: impressionHandler
}
```

8. Review the edits below in
<details><summary>Final <code>flags.js</code>:</summary>

```javascript
import Rox from 'rox-browser'
import { store } from '../store'
import { betaAccess } from './users'

export const Flags = {
  sidebar: new Rox.Flag(false)
};

export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
};

export const impressionHandler = (reporting, experiment) => {
  if (experiment.name === 'title') {
    console.log('Title flag, ' + reporting.name + ' ,value is ' + reporting.value)
    gtag('event', experiment.name, {
      'event_category': reporting.name,
      'event_label': reporting.value
    })
  } else {
    console.log('Not in title experiment. Flag ' + reporting.name + '. default value ' + reporting.value + ' was used')
  }
};

const options = {
  configurationFetchedHandler: configurationFetchedHandler,
  impressionHandler: impressionHandler
};

Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);
Rox.setCustomBooleanProperty('hasBetaAccess', betaAccess())

Rox.register('default', Flags);
Rox.setup(process.env.VUE_APP_ROLLOUT_KEY, options);

```
</details>

9. Include a commit message (e.g. "Add impressionHandler"), before commiting changes directly to `development` branch.

### Split Based Test for Title Experiment

1. Navigate to the Rollout dashboard, and bring up the **title** experiment.
2. Select the trashcan icon to the right of the first condition to **remove** it.
3. The premise of this A/B test will be to route 50% of all users to a **True** value and the other 50% to a **False** value. This can be accomplished by changing **False** to **Split** within the drop down menu. The default split experiment should reflect these weightings to each value.
4. **Update Audience** to apply the changes made in this experiment.

### SA Leads GA Discussion on Dashboard


**TODO**
* Include SA Discussion points
* Make an option to include their own GA property tag

### Lab 6 Completed!
You have successfully completed the introductory CloudBees Rollout workshop!

Please return to the [main page](../../README.md#workshop-labs) for other workshops and labs.
