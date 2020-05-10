name: rollout-targeting-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# User Targeting

---
name: rollout-targeting-overview
# User Targeting

You may not always want everyone to receive the same experience when rolling out a new feature, or simply updating an existing feature. When working with a new front-end UX design, a back-end search improvement, or anything in between, targeting specific users can help ensure the best experience for all of your customers.
<br/>
<br/>
Target groups let you define groups of users based on one or more user properties or device attributes. CloudBees Rollout also includes built-in targeting using the format `rox.<attribute name>`.
<br/>
<br/>

Attribute Name | Notes
--- | ---
`rox.language` | &nbsp;&nbsp;Two letter language code, e.g., "en," "es," or "fr
`rox.platform` | &nbsp;&nbsp;OS name, e.g., "iOS" or "Android"
`rox.screen_height` | &nbsp;&nbsp;Screen height in pixels
`rox.screen_width` | &nbsp;&nbsp;Screen width in pixels

---
name: rollout-targeting-lab
# Lab - User Targeting

* In this lab you will use a custom property from our code and allow users in the Rollout dashboard to create a ruleset such that the sidebar element is only visible to users that have successfully logged in.
* The *User Targeting* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutTargeting/rolloutTargeting.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutTargeting/rolloutTargeting.md)

---
name: rollout-targeting-review

not sure review of the lab is necessary... thoughts?
