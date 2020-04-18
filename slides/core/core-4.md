name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Pipeline Policies

---
name: pipeline-policies
class: compact

# CloudBees Pipeline Policies .badge-red[PREVIEW]

[Pipeline Policies for CloudBees Core](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.

* Pipeline Policies are runtime validations that support both scripted and declarative pipelines.
* Pipeline Policies provide administrators a way to include warnings for or block the execution of pipelines that do not comply with certain regulatory requirements rules or best practice guidelines captured as policy rules.
* There are currently 4 supported policy rules:
  * AgentTimeoutRule - validates that a timeout period was set for tasks executed on agents.
  * PausedActionTimeoutRule - validates that pipeline steps that require an external condition must be defined within a timeout.
  * PausedActionInAgentRule - validates that a paused action step isn’t executed on an agent.
  * EntirePipelineTimeoutRule - validates that a timeout period was set for the entire Pipeline execution.