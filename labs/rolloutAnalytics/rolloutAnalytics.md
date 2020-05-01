# <img src="images/Rollout-blue.svg" alt="CloudBees Rollout Logo" width="40" align="top"> CloudBees Rollout and Analytics

1. Set up 50% split for sidebar test

2. `public/index.html`

```html
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-165275127-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-165275127-1');
</script>
```

3. `src/utils/flag.js` impressionHandler
```javascript
export const impressionHandler = (reporting, experiment) => {
  if (experiment) {
    console.log('flag ' + reporting.name + ' value is ' + reporting.value + ', it is part of ' + experiment.name + ' experiment')
    analytics.page('Home', {
      experiment: experiment.name,
      flag: reporting.name,
      value: reporting.value
    })
  } else {
    console.log('No experiment configured for flag ' + reporting.name + '. default value ' + reporting.value + ' was used')
  }
};
```
4. Add to options
```javascript
const options = {
  configurationFetchedHandler: configurationFetchedHandler,
  impressionHandler: impressionHandler
}
```
4. The final `flags.js` should be
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

export const impressionHandler = (reporting, experiment) => {
  if (experiment) {
    console.log('flag ' + reporting.name + ' value is ' + reporting.value + ', it is part of ' + experiment.name + ' experiment')
    analytics.page('Home', {
      experiment: experiment.name,
      flag: reporting.name,
      value: reporting.value
    })
  } else {
    console.log('No experiment configured for flag ' + reporting.name + '. default value ' + reporting.value + ' was used')
  }
};

const options = {
  configurationFetchedHandler: configurationFetchedHandler,
  impressionHandler: impressionHandler
};

Rox.setCustomBooleanProperty('isLoggedIn', store.getters.isLoggedIn);
Rox.register('default', Flags);
Rox.setup("<ROLLOUT_ENV_KEY>", options);
	
```
</details>
