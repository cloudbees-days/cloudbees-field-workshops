name: rollout-title-slide
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false


# CloudBees Rollout Workshop
.one-third-up[![:scale 10%](../img/Rollout-white.svg)]
???
This workshop introduces attendees to the features for CloudBees Rollout.

---
layout: true

.header[
]

.footer[
- © 2020 CloudBees, Inc.
- ![:scale 100%](../img/CloudBees-Submark-Full-Color.svg)
]
---
name: agenda
# Agenda

1. Rollout Workshop Setup
2. Adding a Title to the Microblog
3. Controlling the Value of a Feature Flag
4. User Targeting
5. Rollout Configuration as Code
6. Analytics and A/B testing

**Please note, it is unlikely that we will get through all the material. However, all of the lab material is freely available on GitHub and can be self-led. The Core lab environment will be available until next Monday and the Rollout trial is available for 14 days if you would like to complete any labs we don't finish today.**

---
name: workshop-tools
# Workshop Tools Overview

* We will be using Zoom breakout rooms for the majority of the workshop material.
* Please use the Zoom chat to introduce yourself and if you have any questions.
* We will be grouping attendees in Zoom breakout rooms based on if you did the CloudBees Core workshop just before this one. If you did the Core workshop rename yourself in Zoom by adding the number **1** before your name.
* After an overview of CloudBees Core you will be grouped into Zoom breakout rooms where you will complete the workshop.
* Once in the breakout rooms please feel free to ask questions via audio or via the Zoom chat. You may also use the Zoom *Nonverbal* feedback feature to raise your hand or to ask you instructor to slow down or speed up. NOTE: The chat is only broadcast to your breakout room.

---
name: workshop-zoom
class: center

![:scale 90%](img/zoom-tools.png)

---
name: rollout-lab-environment
# Lab Environment

* This workshop uses CloudBees Rollout SaaS version running on AWS
  * Each attendee will sign up for a CloudBees Rollout account
  * If you are already a Rollout customer, simply sign in as usual
* All the instructions for the labs and these slides are publicly available in GitHub
* Attendees will be using their own GitHub accounts

---
name: rollout-overview-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Rollout Overview

---
name: feature-flag-background
# What is Feature Flagging?

At its most simplistic, feature flagging is a practice of wrapping new functionality in conditional code blocks.
<br/>
<br/>
Feature flags are used to hide, enable or disable features during runtime. With feature flags, a software feature can be tested even before it is completed and ready for release.  For example, during the development process, a developer can enable the feature for local testing and disable it for all other users. Feature flagging also provides an alternative to maintaining multiple feature branches in source code.
<br/>
<br/>
This technique offers many other benefits and will be discussed in greater detail in this workshop.

---
name: rollout-overview-content

.italic[
  *95% of respondent's organizations have implemented, begun implementing, or plan to implement feature flags in the future* - Atlassian / Rollout market research report 2018
]

# Feature Flag Management
* Costly, Manual, Development Headaches
* Risk in Testing and Production
* Slow Time to Market
* Non-granular, Inflexible
* Need for Experimentation & Innovation

---
name: rollout-overview-value

# CloudBees Feature Management Solution

.italic[
*Rollout is a multi-platform, Infrastructure as Code,
SaaS feature management and remote configuration solution.*
]

Faster Delivery
.no-bullet[
* Don’t wait for a feature to trickle out across multiple servers in a highly scaled application; turn it on all at once when it’s ready, or selectively enable it for users.
]

Safer Releases
.no-bullet[
* Test new code  safely in production with blue/green and canary deployments. If a bug is discovered, just turn off that feature right away and then repair it.
]

Experimentation
.no-bullet[
* Determine the impact of a feature on your revenue, user engagement, etc. Enable features only for your QA team to allow validation with production data.
]

Customization
.no-bullet[
* Turn specific features on or off for particular customers, based on preferences, location, licensing, etc.
]

---
name: rollout-overview-architecture
class: middle, center

# CloudBees Rollout Flag Update Process
![:scale 75%](img/rollout_saas_arch.jpg)

???
Starting from dashboard on bottom left, we process configuration on the rollout server to generate a JSON config file and we sign that JSON file with a public and private key and save the file to a cloud service, specifically amazon s3.

And then the Client side SDKs (mobile, web, backend service etc) download that JSON file so all the processing and all the decision points happen on the target device itself.

The entire architecture is stateless, for 2 main reasons
1. privacy and security: we do not want you to share your user info with us. All we know are experiment names, target group names, feature flags name, but we do not know user information.
2. we want to ensure there is no impact to your services. Even if we have an outage and our servers are down, at maximum you will not be able to make a configuration change via the dashboard. Your service will not be impacted because at the end you are just reading a JSON file. We also try to mitigate service issues during network outages because our feature flags always have default values, we also use local caching on the device and other mechanisms to ensure there is no impact if Rollout has a problem.

Lastly, we are using Server sent event protocol to notify the SDKs that they need to download a JSON file when there is a change in the dashboard. The idea is to ensure that every change to the dashboard is received as fast as possible on the end devices.
