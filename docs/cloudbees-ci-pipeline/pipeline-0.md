name: core-title-slide
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false


# CloudBees CI Workshop
.one-third-up[![:scale 10%](../img/CloudBees-Submark-White.svg)]
???
This workshop introduces attendees to Declarative Pipelines for Jenkins.

---
layout: true

.header[
]

.footer[
- © 2021 CloudBees, Inc.
- ![:scale 100%](../img/CloudBees-Submark-Full-Color.svg)
]
---
name: workshop-tools
# Workshop Tools Overview

* We highly recommend using Google Chrome as the web browser - other browsers will work, but we have found Chrome to work best with the GitHub editor.
* We will be using Zoom breakout rooms for the majority of the workshop material.
* Please use the Zoom chat to introduce yourself and if you have any questions.
* After an overview of CloudBees CI you will be grouped into Zoom breakout rooms where you will complete the workshop labs.
* Once in the breakout rooms please feel free to ask questions via audio or via the Zoom chat. You may also use the Zoom *Nonverbal* feedback feature to raise your hand or to ask you instructor to slow down or speed up. NOTE: The chat is only broadcast to your breakout room.

---
name: lab-environment
# Lab Environment
* This workshop uses a CloudBees CI cluster, an enterprise version of Jenkins, running on the Google Kubernetes Engine (GKE)
  * Each attendee will have their own Jenkins instance provisioned as if you were a team. We refer to these as a ***managed controller*** since they are dynamical provisioned on Kubernetes and their full lifecycle is **managed** by the CloudBees CI Operations Center.
* All the instructions for the labs and these slides are publicly available
* Attendees will be using their own GitHub accounts 
* **IMPORTANT:** If you haven't already completed the *Pre-Workshop Setup* then do so here: https://cloudbees-ci-pipeline.labs.cb-sa.io/getting-started/pre-workshop-setup/


.footnote[.bold[*] Please note, if we do not get through all the material, all of the lab material is freely available on GitHub and can be self-led. The CloudBees CI lab environment will be available until next Monday if you would like to complete any labs we don't get through.]