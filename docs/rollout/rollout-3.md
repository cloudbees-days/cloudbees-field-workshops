name: rollout-control-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Controlling the Value of a Feature Flag

---
name: rollout-control-overview
# Controlling the Value of a Feature Flag

In order to control the value of a feature flag with CloudBees Rollout for this lab, we will be creating an experiment in the dashboard.
<br/>
<br/>
Experiments are how you use your feature flags to expose your target groups to different application behaviors.

---
name: rollout-control-override

# Introduction to Flags Override View

The *Flags Override view* is useful for debugging purposes. It allows developers to expose a view that shows the current status for each flag, and it allows the user to override these flags. This view is usually exposed to only developers, the QA team, and the product team.
<br/>
<br/>
In the *Flags Override view*, a flag can appear in the following states:
* The *flag is on* state means the value from the server of a flag is on and is not overridden on the device.
* The *flag is off* state means the value from the server of a flag is off and isn’t overridden on the device.
* The *flag is overridden* state means the value from the server is overridden on this specific device.

---
name: rollout-control-lab
# Lab - Controlling the Value of a Feature Flag

* In this lab you will control the value of a flag by creating an experiment via the Rollout dashboard.
* For local testing or development, we may need to specify values for each flags on our local machines. In order to do this without affecting others' work, we will implement the Flag Override and toggle the values as needed.
* The *Controlling the Value of a Feature Flag* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutExperiment/rolloutExperiment.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutExperiment/rolloutExperiment.md)

---
name: rollout-control-review

# Controlling the Value of a Feature Flag Lab Review

Experiments are an important concept in CloudBees Rollout. With this lab complete, you can now control the value of "default.sidebar" by creating an experiment via the Rollout dashboard.
<br/>
<br/>
You also used the *Flags Override view* UI element to modify flag values to allow for validation on your local machine without affecting others' work. 
