name: rollout-sidebar-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# Adding a Sidebar to the Microblog

---
name: rollout-sidebar-overview
# Adding a Sidebar to the Microblog

Is there really a need for intro slide here?

---
name: rollout-sidebar-lab
# Lab - Adding a Sidebar to the Microblog

* In this lab, you will create a sidebar component and add it to the microblog. Since this component is *experimental*, we will gate it behind our previously created feature flag (`sidebar: new Rox.flag(false)`) that will initially hide it. Then using Rollout's dashboard, we will remotely configure the value of the flag, thus enabling the sidebar.

* The *Adding a Sidebar to the Microblog* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutFeature/rolloutFeature.md)

---
name: rollout-sidebar-review
# Adding a Sidebar to the Microblog Lab Review

* You created an experimental component.
* You created a `show_sidebar` function that returned the boolean value assigned to our `sidebar` feature flag.
* You wrapped your experimental component in conditional logic to only display when `show_sidebar` is `True`.
* You committed your code back to your `development` branch.
