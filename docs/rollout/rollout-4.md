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
Target groups let you define groups of users based on one or more user properties or device attributes. CloudBees Rollout also includes built-in targeting using the format
<br/>
`rox.<attribute_name>`.
<br/>
<br/>

Attribute Name | Notes
--- | ---
`rox.language` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two letter language code, e.g., "en," "es," or "fr
`rox.platform` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OS name, e.g., "iOS" or "Android"
`rox.screen_height` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Screen height in pixels
`rox.screen_width` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Screen width in pixels

---
name: rollout-targeting-lab
# Lab - User Targeting

* In this lab you will use a custom property from our code and allow users in the Rollout dashboard to create a ruleset such that the sidebar element is only visible to users that have successfully logged in.
* The *User Targeting* lab instructions are available at:
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutTargeting/rolloutTargeting.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/rolloutTargeting/rolloutTargeting.md)

---
name: rollout-targeting-review

User targeting is an important concept in Rollout. With this lab complete, you can now offer a different user experience based on known attributes and you defined a custom property `isLoggedIn`. In this case, our microblog now has an additional UI element for the users with an account compared to those who do not. 
