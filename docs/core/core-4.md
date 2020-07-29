name: pipeline-policies-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Pipeline Policies

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Configuration as Code (CasC) with CloudBees CI
5. .blue-bold[Pipeline Manageability & Governance with] Templates and .blue-bold[Policies]
6. Cross Team Collaboration
7. Hibernating Managed Jenkins Instances

---
name: pipeline-policies

# CloudBees Pipeline Policies .badge-red[PREVIEW]

* [Pipeline Policies for CloudBees CI](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.
* Pipeline Policies are centrally managed runtime validations that support both scripted and declarative pipelines.
* Pipeline Policies provide administrators a way to include warnings for or block the execution of pipelines that do not comply with certain regulatory requirements or best practice guidelines captured as policy rules.
* There are currently 4 supported policy rules:
  * AgentTimeoutRule - validates that a timeout period was set for tasks executed on agents.
  * PausedActionTimeoutRule - validates that pipeline steps that require an external condition must be defined within a timeout.
  * PausedActionInAgentRule - validates that a paused action step isn’t executed on an agent.
  * EntirePipelineTimeoutRule - validates that a timeout period was set for the entire Pipeline execution.

---
name: pipeline-policies-lab-link
class: compact

# Lab - Enforcing Pipeline Timeouts with Pipeline Policies

* In the following lab you will create a Pipeline Policy that will require that all Pipeline jobs on your Team (Jenkins instance) be configured with a 30 minute (or greater) global timeout.
* The *Enforcing Pipeline Timeouts with Pipeline Policies* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-policies/pipeline-policies.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-policies/pipeline-policies.md)


---
name: pipeline-policies-overview

# Pipeline Policies Overview

* Created a Pipeline Policy to enforce a minimum 30 minute global timeout for all Pipeline jobs on your Team (Jenkins instance)
* Updated the **VueJS** template with a time out to validate successfully against the **Timeout policy** you created
