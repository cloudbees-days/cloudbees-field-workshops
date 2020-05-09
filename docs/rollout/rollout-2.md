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
name: rollout-sidebar-lab

# Lab - Gating Code with CloudBees Feature Flags

* In this lab, you will create a sidebar component and add it to the **microblog-frontend** sample application. Since this component is *experimental*, we will gate it behind our previously created feature flag (`sidebar: new Rox.flag(false)`) that will initially hide it. Then, using Rollout's dashboard, we will remotely configure the value of the flag, enabling the sidebar.

* The *Gating Code with CloudBees Feature Flags* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md)

---
name: rollout-sidebar-review

# Gating Code with CloudBees Feature Flags Lab Review

* You created an experimental component.
* You created a `show_sidebar` function that returned the boolean value assigned to our `sidebar` feature flag.
* You wrapped your experimental component in conditional logic to only display when `show_sidebar` is `True`.
* You committed your code back to your `development` branch.
