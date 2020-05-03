name: rollout-control-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Controlling the Value of a Feature Flag

---
name: rollout-control-overview
# Controlling the Value of a Feature Flag

In order to control the value of a feature flag with CloudBees Rollout for this lab, we need to know a few key pieces of information:
1. Has the flag value changed?
2. From where was the value change initiated?


You can identify when Rollout SDK has loaded configuration from local storage or network by adding the `configurationFetchedHandler`.


The `configurationFetchedHandler` returns `fetcherResult` which has the following information regarding the actual fetch:
* `fetcherStatus` - an enum that identifies which configuration was fetched (from the network, from local storage, an error occurred)
* `creationDate` - Date of configuration creation
* `errorDetails` - The description of the error if one exists
* `hasChanges` - Boolean `True` if the configuration differ from the one it is replacing

---
name: rollout-control-lab
# Lab - Controlling the Value of a Feature Flag

* In this lab you will add a configuration fetched handler to apply changes to microblog on page refresh
* You will control the value of a flag by creating an experiment via the Rollout dashboard
* The *Controlling the Value of a Feature Flag* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutExperiment/rolloutExperiment.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutExperiment/rolloutExperiment.md)

---
name: rollout-control-review

not sure review of the lab is necessary... thoughts?
