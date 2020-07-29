name: core-hibernate-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Core Hibernating Managed Jenkins Instances

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Configuration as Code (CasC) with CloudBees CI
5. Pipeline Manageability & Governance with Templates and Policies
6. Cross Team Collaboration
7. .blue-bold[Hibernating Managed Jenkins Instances]

---
name: hibernate-overview

# CloudBees CI Hibernating Managed Jenkins Instances

* [CloudBees CI Managed Jenkins instance hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) takes advantage of running CloudBees CI on Kubernetes by automatically shutting down or hibernating Team/Managed Jenkins instance. This is done by scaling the Kubernetes StatefulSet down to zero replicas.
* Hibernation was enabled for everyones' Team (Jenkins instance) earlier in the CasC lab and everyones' Teams (Jenkins instance) will hibernate after 30 minutes of inactivity.
* Filtered web activity and direct web access will **wake up** the Team (Jenkins instance). If a Team (Jenkins instance) is hibernating - signified by the light blue **pause** icon next to it in the classic UI of Operations Center - all you need to do is click on it and it will be up and running in a few minutes.

???
The workshop clusters will continue to be available for both CloudBees CI and CloudBees Feature Flags for as long as necessary after the workshop. We need to make sure that all CloudBees CI attendees are aware that their Team (Jenkins instance) will most likely be hibernating when they come back to complete any labs and that they just need to click on it to ‘wake it up’ from the classic UI of Operations Center.

---
name: hibernate-screenshot
class: center

![:scale 80%](img/hibernating-master.png)

---
name: hibernating-masters-cost-saving

# How Hibernating Managed Jenkins Instances Reduce Infrastructure Costs

There are several ways that costs may be reduced with Managed Jenkins Instances hibernation:

1. When using Kubernetes auto-scaling and a Managed Jenkins Instances is hibernated then the Kubernetes cluster has the potential to downscale by removing a node.
2. When a Managed Jenkins Instances is hibernated you immediately gain additional CPU and memory on the node where your Team/Managed Jenkins Instances pod was running - this additional capacity is immediately available for Kubernetes based agents reducing the possibility of agents queueing and/or triggering an upscaling of your Kubernetes cluster. 

---

# Lab - Configuring Webhooks for Hibernating Managed Jenkins Instances

* The *Configuring Webhooks for Hibernating Managed Jenkins Instances* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating/hibernating.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating-masters/hibernating-masters.md)

???

All presenters should familiarize themselves with the hibernation monitor design document: https://github.com/cloudbees/managed-master-hibernation-monitor/blob/master/design.md 