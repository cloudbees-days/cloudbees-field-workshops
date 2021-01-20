name: hibernate-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Hibernating Managed Controllers

---
name: agenda-templates
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. <a class="no-style" href="#pipeline-policies-title">Pipeline Manageability & Governance with Policies</a>
7. <a class="no-style" href="#rbac-casc-title">Delegating Administration with RBAC</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. .blue-bold[Hibernating Managed Controllers]

---
name: hibernate-overview

# CloudBees CI Hibernating Managed Controllers

* [CloudBees CI Managed Controller hibernation](https://docs.cloudbees.com/docs/cloudbees-core/latest/cloud-admin-guide/managing-masters#_hibernation_in_managed_masters) takes advantage of running CloudBees CI on Kubernetes by automatically shutting down or hibernating ***managed controllers***. This is done by scaling the Kubernetes StatefulSet down to zero replicas.
* Hibernation is enabled for everyones' *managed controller* provisioned earlier in the workshop and everyones' *managed controller* will hibernate after 30 minutes of inactivity.
* Filtered web activity and direct web access will **wake up** the *managed controller*. If a *managed controller* is hibernating - signified by the light blue **pause** icon next to it in the classic UI of Operations Center - all you need to do is click on it and it will be up and running in a few minutes.

???
The workshop clusters will continue to be available for both CloudBees CI and CloudBees Feature Flags for as long as necessary after the workshop. We need to make sure that all CloudBees CI attendees are aware that their *managed controller* will most likely be hibernating when they come back to complete any labs and that they just need to click on it to ‘wake it up’ from the classic UI of Operations Center.

---
name: hibernate-screenshot
class: center

![:scale 80%](img/hibernating-master.png)

---
name: hibernating-masters-cost-saving

# How Hibernating Managed Controllers Optimize Resources

There are several ways to optimize continuous integration resources with ***managed controller*** hibernation:

1. When using Kubernetes auto-scaling and a *managed controller* is hibernated then the Kubernetes cluster has the potential to scale down by removing a node.
2. When a *managed controller* is hibernated you immediately gain additional CPU and memory on the node where your *managed controller* pod was running - this additional capacity is immediately available for Kubernetes based agents reducing the possibility of agents queueing and/or triggering an upscaling of your Kubernetes cluster. 

---

# Lab - Configuring Webhooks for Hibernating Managed Controllers

* The *Configuring Webhooks for Hibernating Managed Controllers* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-2/hibernating/

???

All presenters should familiarize themselves with the hibernation monitor design document: https://github.com/cloudbees/managed-master-hibernation-monitor/blob/master/design.md 