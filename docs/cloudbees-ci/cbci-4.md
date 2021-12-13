name: pipeline-policies-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees CI<br>Pipeline Policies

---
name: agenda-templates
class: compact

# Agenda

1. <a class="no-style" href="#workshop-tools">Workshop Tools Overview</a>
2. <a class="no-style" href="#core-overview-title">CloudBees CI Overview</a>
3. <a class="no-style" href="#core-setup-overview">Setup for Labs</a>
4. <a class="no-style" href="#pipeline-template-catalog-title">Pipeline Manageability & Governance with Templates</a>
5. <a class="no-style" href="#casc-title">Configuration as Code (CasC) with CloudBees CI</a>
6. .blue-bold[Pipeline Manageability & Governance with Policies]
7. <a class="no-style" href="#rbac-casc-title">Delegating Administration with RBAC</a>
7. <a class="no-style" href="#dev-centric-title">A Developer Centric Experience</a>
8. <a class="no-style" href="#using-templates-title">Using Pipeline Templates</a>
9. <a class="no-style" href="#casc-dev-title">Configuration as Code (CasC) for Developers</a>
10. <a class="no-style" href="#contextual-feedback-title">Contextual Feedback for Pipelines</a>
11. <a class="no-style" href="#cross-team-title">Cross Team Collaboration</a>
12. <a class="no-style" href="#hibernate-title">Hibernating Managed Controllers</a>

---
name: pipeline-policies

# CloudBees Pipeline Policies

* [Pipeline Policies for CloudBees CI](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.
* Pipeline Policies are centrally managed runtime validations that support both scripted and declarative pipelines.
* Pipeline Policies provide administrators a way to include warnings for or block the execution of pipelines that do not comply with certain regulatory requirements or best practice guidelines captured as policy rules.
* There are currently 4 supported policy rules:
  * **AgentTimeoutRule** - validates that a timeout period was set for tasks executed on agents.
  * **PausedActionTimeoutRule** - validates that pipeline steps that require an external condition must be defined within a timeout.
  * **PausedActionInAgentRule** - validates that a paused action step isn’t executed on an agent.
  * **EntirePipelineTimeoutRule** - validates that a timeout period was set for the entire Pipeline execution.
* CloudBees CI provides [Configuration-as-Code support for Pipeline Policies](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-policies#_managing_pipeline_policies_with_configuration_as_code). There is also a [CLI for managing Pipeline Policies in bulk](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines/pipeline-policies#_managing_pipeline_policies_in_bulk).

---
name: pipeline-policies-lab-link
class: compact

# Labs - Enforcing Pipeline Timeouts with Pipeline Policies and GitOps for Pipeline Policies

* In the following labs:
  *  You will use CasC for CloudBees CI to create a Pipeline Policy that will require that all Pipeline jobs on your ***managed controller*** be configured with a 30 minute (or shorter) global timeout.
* The *Enforcing Pipeline Timeouts with Pipeline Policies* lab instructions are available at: 
  * https://cloudbees-ci.labs.cb-sa.io/module-1/pipeline-policies/


---
name: pipeline-policies-overview

# Pipeline Policies Overview

* Used CasC to create a Pipeline Policy to enforce a minimum 30 minute global timeout for all Pipeline jobs on your ***managed controller***
* Updated the **CloudBees CI Configuration Bundle** template with a time out to validate successfully against the **Timeout policy** you created

