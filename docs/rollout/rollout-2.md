name: rollout-sidebar-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Gating Code with CloudBees Feature Flags

---
name: rollout-sidebar-overview
# Gating Code with CloudBees Feature Flags

Feature flags allow you to put gates around new feature code.

* Flags are added to the source code of an application.
* A flag is then used to wrap the code of a new feature.
* There are SDKs that support both frontend and backend development.

---
name: rollout-control-overview
class: compact

# Introduction to Configuration Fetching
<br/>
In order to see our gated code on our example application, we need to know a few key pieces of information:
1. Has the flag value changed?
2. From where was the value change initiated?
<br/>
<br/>
<br/>
You can identify when Rollout SDK has loaded configuration from local storage or network by adding the `configurationFetchedHandler`. The `configurationFetchedHandler` returns `fetcherResult` which has the following information regarding the actual fetch:
* `fetcherStatus` - an enum that identifies which configuration was fetched (from the network, from local storage, an error occurred)
* `creationDate` - Date of configuration creation
* `errorDetails` - The description of the error if one exists
* `hasChanges` - Boolean `True` if the configuration differ from the one it is replacing

---
name: rollout-sidebar-lab

# Lab - Gating Code with CloudBees Feature Flags

* In this lab, you will create a title component and add it to the **microblog-frontend** sample application. Since this component is *experimental*, we will gate it behind our previously created feature flag (`title: new Rox.flag(false)`) that will initially hide it.
* Using Rollout's dashboard, we will remotely configure the value of the flag, enabling the title.
* The *Gating Code with CloudBees Feature Flags* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md)

---
name: rollout-sidebar-review

# Gating Code with CloudBees Feature Flags Lab Review

* You created an experimental component.
* You created a `show_title` function that returned the boolean value assigned to our `title` feature flag.
* You wrapped your experimental component in conditional logic to only display when `show_title` is `True`.
* You defined a `configurationFetchedHandler` and added it to your `options` to alert your application that a configuration value has changed and allowed for updated config values to be applied on an action (page refresh).
* You committed your code back to your `development` branch.
