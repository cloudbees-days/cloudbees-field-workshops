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
2. Gating Code with CloudBees Feature Flags
3. Controlling the Value of a Feature Flag
4. User Targeting
5. Analytics and A/B testing
6. Rollout Configuration as Code

---
name: rollout-lab-environment
# Lab Environment

* This workshop uses the CloudBees Rollout SaaS running on AWS
  * Each attendee will sign up for a CloudBees Rollout trial account
  * If you are already a Rollout customer, simply sign in as usual
* This workshop leverages CloudBees Core for automating the build and deployment of the sample application
  * Each attendee will create their own CloudBees Core Jenkins Master that they will provision as part of the setup
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
class: roomy

# What is Feature Flagging?

.no-bullet[
* Feature flagging is a practice of wrapping new functionality in conditional code blocks.
* Feature flags are used to hide, enable or disable features during runtime. With feature flags, a software feature can be tested even before it is completed and ready for release.  For example, during the development process, a developer can enable the feature for local testing and disable it for all other users. 
* Feature flagging also provides an alternative to maintaining multiple feature branches in source code.
* This technique offers many other benefits and will be discussed in greater detail in this workshop.
]

---
name: rollout-overview-content

.italic[
  *95% of respondent's organizations have implemented, begun implementing, or plan to implement feature flags in the future* <br>- Atlassian / Rollout market research report 2018
]

# Lack of Feature Flag Management
* Costly, Manual, Development Headaches
* Risk in Testing and Production
* Slow Time to Market
* Non-granular, Inflexible
* Need for Experimentation & Innovation

---
name: rollout-overview-value
class: compact

# CloudBees Feature Management Solution

.italic[
### *Rollout is a multi-platform, Infrastructure as Code, SaaS feature management and remote configuration solution.*
]

### Faster Delivery
.no-bullet[
* Don’t wait for a feature to trickle out across multiple servers in a highly scaled application; turn it on all at once when it’s ready, or selectively enable it for targeted users.
]

### Safer Releases
.no-bullet[
* Test new code safely in production with blue/green and canary deployments. If a bug is discovered, just turn off that feature right away and then fix it.
]

### Experimentation
.no-bullet[
* Determine the impact of a feature on your revenue, user engagement, etc. Enable features only for your QA team to allow validation with production data.
]

### Customization
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
