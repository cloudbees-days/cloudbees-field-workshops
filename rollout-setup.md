![Rollout.io](img/rollout/rollout-logo.svg)
# Rollout Set-Up

In this lab, we will introduce CloudBees Rollout for feature flag management. We first need to connection to the Rollout Dashboard by leveraging the appropriate SDK. This will allow us to control newly created feature flags in later lags.

## Assumptions
Need to know what their initial view will look like. Aka, what is the outcome of Pre-Requisites/Rollout sign up script

## Dashboard Set-Up and SDK Connection
1. Log in to the [Rollout dashboard](https://app.rollout.io/login) using the account created previously.
2. Within the navigation menu, located on the far left side of the dashobard, click the App Settings option.
3. From the resulting App Settings page, navigate to the "Environments" tab, and copy your unique key associated with the Production environment.
4. TODO: SET VUE_APP_ROLLOUT_KEY environment variable.
5. Open a terminal at the root directory of your frontend forked repository and add the Rollout library to your application with the following command:
```
$ npm install rox-browser --save
```
6. Add a new directory called **utils** directly beneath src directory.
```
$ cd src
$ mkdir utils
```
6. Within the new **utils** directory, create a new file called **flags.js** with the following code:
```javascript
import Rox from 'rox-browser'

export const Flags = {
	sidebar: new Rox.Flag(false)
};

Rox.register('default', Flags);

Rox.setup(process.env.VUE_APP_ROLLOUT_KEY);
```
7. Run the application using:
```
$ yarn serve
```
and navigate to [localhost:8080](https://localhost:8080).