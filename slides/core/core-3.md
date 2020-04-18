name: core-setup-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Pipeline Template Catalogs & Pipeline Policies

---
name: pipeline-template-catalog

# Pipeline Template Catalogs

Pipeline Template Catalogs help ensure that Pipeline jobs conform to organizational standards.

Benefits of using Pipeline Template Catalogs include:

* Providing developers with a simplified and directed experience for configuring Pipeline in “domain specific” terms that make sense for an organization. Thus, developers can focus on shipping products.
* Organizing Pipelines per projects and/or teams. Similar-looking jobs that only differ in a few aspects can be parameterized per project. When you change a template, all the jobs created from that template get updated automatically.

???
Pipeline Template Catalogs help ensure that Pipeline jobs conform to organizational standards and when used in combination with Shared Libraries provide reusable Pipelines — boosting cross-team collaborations, saving time and reducing errors.

---
name: lab-link-pipeline-template-catalog

# Lab - Import Pipeline Template Catalog

[https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-template-catalog/pipeline-template-catalog.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/pipeline-template-catalog/pipeline-template-catalog.md)

---
name: pipeline-policies
class: compact

# Pipeline Policies

[Pipeline Policies for CloudBees Core](https://docs.cloudbees.com/docs/admin-resources/latest/pipelines-user-guide/pipeline-policies) allow organizations to enforce standards across Pipeline jobs.

* Pipeline Policies are runtime validations that support both scripted and declarative pipelines.
* Pipeline Policies provide administrators a way to include warnings for or block the execution of pipelines that do not comply with certain regulatory requirements rules or best practice guidelines captured as policy rules.
* There are currently 4 supported policy rules:
  * AgentTimeoutRule - validates that a timeout period was set for tasks executed on agents.
  * PausedActionTimeoutRule - validates that pipeline steps that require an external condition must be defined within a timeout.
  * PausedActionInAgentRule - validates that a paused action step isn’t executed on an agent.
  * EntirePipelineTimeoutRule - validates that a timeout period was set for the entire Pipeline execution.
