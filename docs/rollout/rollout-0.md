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
2. Adding a Sidebar to the Microblog
3. Controlling the Value of a Feature Flag
4. User Targeting
5. Analytics and A/B testing
6. Rollout Configuration as Code

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
name: rollout-overview-content

(we need some stat on the rise of flagging or something)

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
# CloudBees Rollout on AWS

*super dope architecture diagram*
