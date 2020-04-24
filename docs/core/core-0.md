name: core-title-slide
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false


# CloudBees Core Workshop
.one-third-up[![:scale 10%](../img/Core-white.svg)]
???
This workshop introduces attendees to the features for CloudBees Core.

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

1. Workshop Tools Overview
2. CloudBees Core Overview
3. Setup for Labs
4. Configuration as Code (CasC) with CloudBees Core
5. Pipeline Manageability & Governance with Templates and Policies
6. Cross Team Collaboration
7. Hibernating Masters

---
name: workshop-tools
# Workshop Tools Overview

* We will be using Zoom breakout rooms for the majority of the workshop material.
* Please use the Zoom chat to introduce yourself and if you have any questions.
* We will have a short poll where you will be able to assess your experience level in a few technical areas. Based on your responses to the poll questions you will be asked to rank your overall experience level as a **1**, **2** or a **3**, and then rename yourself in Zoom by adding that number before your name.
* After an overview of CloudBees Core you will grouped by experience level into Zoom breakout rooms.
* Once in the breakout rooms please feel free to ask questions via audio or via the Zoom. You may also use the Zoom *Nonverbal* feedback feature to raise your hand or to ask you instructor to slow down or speed up. NOTE: The chat is only broadcast to your breakout room.

---
name: workshop-zoom
# Workshop Zoom Overview

TOOD - Will add a screenshot of Zoom showing how to rename and highlight the features discussed in the previous slide.

---
name: lab-environment
# Lab Environment
* This workshop uses a CloudBees Core cluster, an enterprise version of Jenkins, running on the Google Kubernetes Engine (GKE)
  * Each attendee will provision their own Jenkins instance for the labs by leveraging the scalability of CloudBees Core on Kubernetes
* All the instructions for the labs and these slides are publicly available in GitHub
* Attendees will be using their own GitHub accounts 

---
name: core-overview-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Core Overview

???
Notes

---
name: core-overview-content
class: compact

# CloudBees Core
### *Manage the Volume, Variety and Complexity of Pipelines*

Faster innovation
.no-bullet[
* Free developers to innovate more using toolchain automation
]

Optimize delivery
.no-bullet[
* Reduce administration overhead and optimize software delivery
]

Reduce risk
.no-bullet[
* Ensure compliance through global policy enforcement
]

---
name: core-k8s-architecture
class: middle, center

![:scale 80%](img/core-k8s-architecture.svg)

CloudBees Core on Kubernetes

---
name: core-overview-scale

# Manage Jenkins at Scale
* Curated and verified Jenkins plug-ins with **CloudBees Assurance Program** ensures you are using the most up-to-date and secure versions via monthly security and functionality releases 
* Configuration as Code for Jenkins and Core commercial components
* Enables Comprehensive Jenkins Team Management including:
  * Masters per Team
  * Centrally managed Role Based Access Control (RBAC)
  * Centralized Credentials Management
  * Manage inbound events across multiple Masters
