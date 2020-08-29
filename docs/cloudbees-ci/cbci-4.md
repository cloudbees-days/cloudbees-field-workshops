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
4. Pipeline Manageability & Governance with Templates
5. Configuration as Code (CasC) with CloudBees CI
6. .blue-bold[Pipeline Manageability & Governance with Policies]
7. Contextual Feedback for Pipelines
8. Cross Team Collaboration
9. Hibernating Managed Controllers

---
name: pipeline-policies

# CloudBees Pipeline Policies

* [Pipeline Policies for CloudBees CI](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.
* Pipeline Policies are centrally managed runtime validations that support both scripted and declarative pipelines.
* Pipeline Policies provide administrators a way to include warnings for or block the execution of pipelines that do not comply with certain regulatory requirements or best practice guidelines captured as policy rules.
* There are currently 4 supported policy rules:
  * AgentTimeoutRule - validates that a timeout period was set for tasks executed on agents.
  * PausedActionTimeoutRule - validates that pipeline steps that require an external condition must be defined within a timeout.
  * PausedActionInAgentRule - validates that a paused action step isn’t executed on an agent.
  * EntirePipelineTimeoutRule - validates that a timeout period was set for the entire Pipeline execution.
* CloudBees CI provides a CLI for managing Pipeline Policies at scale

---
name: pipeline-policies-lab-link
class: compact

# Labs - Enforcing Pipeline Timeouts with Pipeline Policies and GitOps for Pipeline Policies

* In the following labs:
  *  You will create a Pipeline Policy that will require that all Pipeline jobs on your ***managed controller*** be configured with a 30 minute (or greater) global timeout.
  *  You will explore GitOps for Pipeline Policies.
* The *Enforcing Pipeline Timeouts with Pipeline Policies* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-1/pipeline-policies/


---
name: pipeline-policies-overview

# Pipeline Policies Overview

* Created a Pipeline Policy to enforce a minimum 30 minute global timeout for all Pipeline jobs on your ***managed controller***
* Updated the **CloudBees CI Configuration Bundle** template with a time out to validate successfully against the **Timeout policy** you created
* Created a job to export Pipeline Policies from your ***managed controller*** to source control and to update the Pipeline Policies on your ***managed controller*** from source control.
