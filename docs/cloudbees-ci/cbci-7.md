name: core-hibernate-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Core Hibernating Managed Controllers

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. Pipeline Manageability & Governance with Policies
7. Contextual Feedback for Pipelines
8. Cross Team Collaboration
9. .blue-bold[Hibernating Managed Controllers]

---
name: hibernate-overview

# CloudBees CI Hibernating Managed Controllers

* [CloudBees CI Managed Controller hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) takes advantage of running CloudBees CI on Kubernetes by automatically shutting down or hibernating ***managed controllers***. This is done by scaling the Kubernetes StatefulSet down to zero replicas.
* Hibernation is enabled for everyones' ***managed controller*** provisioned earlier in the workshop and everyones' ***managed controller*** will hibernate after 30 minutes of inactivity.
* Filtered web activity and direct web access will **wake up** the ***managed controller***. If a ***managed controller*** is hibernating - signified by the light blue **pause** icon next to it in the classic UI of Operations Center - all you need to do is click on it and it will be up and running in a few minutes.

???
The workshop clusters will continue to be available for both CloudBees CI and CloudBees Feature Flags for as long as necessary after the workshop. We need to make sure that all CloudBees CI attendees are aware that their ***managed controller*** will most likely be hibernating when they come back to complete any labs and that they just need to click on it to ‘wake it up’ from the classic UI of Operations Center.

---
name: hibernate-screenshot
class: center

![:scale 80%](img/hibernating-master.png)

---
name: hibernating-masters-cost-saving

# How Hibernating Managed Controllers Reduce Infrastructure Costs

There are several ways that costs may be reduced with ***managed controller*** hibernation:

1. When using Kubernetes auto-scaling and a ***managed controller*** is hibernated then the Kubernetes cluster has the potential to scale down by removing a node.
2. When a ***managed controller*** is hibernated you immediately gain additional CPU and memory on the node where your ***managed controller*** pod was running - this additional capacity is immediately available for Kubernetes based agents reducing the possibility of agents queueing and/or triggering an upscaling of your Kubernetes cluster. 

---

# Lab - Configuring Webhooks for Hibernating Managed Controllers

* The *Configuring Webhooks for Hibernating Managed Controllers* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating/hibernating.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/hibernating-masters/hibernating-masters.md)

???

All presenters should familiarize themselves with the hibernation monitor design document: https://github.com/cloudbees/managed-master-hibernation-monitor/blob/master/design.md 