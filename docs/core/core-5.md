name: cross-team-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Cross Team Collaboration

---
name: agenda-templates
# Agenda

1. Workshop Tools Overview
2. CloudBees CI Overview
3. Setup for Labs
4. Configuration as Code (CasC) with CloudBees CI
5. Pipeline Manageability & Governance with Templates and Policies
6. .blue-bold[Cross Team Collaboration]
7. Hibernating Managed Jenkins Instances

---
name: cross-team overview
class: compact, middle

# Cross Team Collaboration

.img-left[
![Cross Team Collaboration Diagram](img/cross-team-diagram.png)
]

.no-bullet.img-right[
* CloudBees CI [Cross Team Collaboration](https://docs.cloudbees.com/docs/cloudbees-core/2.204.2.2/cloud-admin-guide/cross-team-collaboration) simplifies the cumbersome and complicated tasks of triggering downstream jobs by eliminating the need to identify and maintain the full path for every downstream job. Prior to this feature, the details of every downstream job had to meticulously specified in the upstream job. If the job name changed, the upstream job had to be refactored, creating a maintenance burden and discouraging the adoption of event-based triggers.
* Cross Team Collaboration essentially allows a Pipeline to create a notification event to be consumed by other Pipelines waiting on it. It consists of a Publishing Event and a Trigger Condition.
* The Cross Team Collaboration feature has a configurable router for routing events either across all Managed Jenkins instances connected via CloudBees CI Operations Center or locally within one Managed Jenkins instance. It needs to be enabled and configured on your Team (Jenkins instance) before you will be able to receive an event published by another Pipeline. 
]

---
name: cross-team-publish-types

# Publish Event Types for Cross Team Collaboration

There are two types of events that can be published for the `publishEvent` step:
* **`simpleEvent`** - a publish event type that only allows including a single string as the event payload. The supplied string value will be dynamically *wrapped* as the value of the `event` JSON key.

```groovy
publishEvent simpleEvent('helloWorld')
```

* **`jsonEvent`** - a more complex publish event type, it allows you to specify any valid JSON as the event payload.

```groovy
publishEvent event: jsonEvent('{"event":"imagePush","name":"node","tag":"14.0.0-alpine3.11"}')
```

---
name: cross-team-trigger-types

# Event Trigger Types for Cross Team Collaboration

Just as there are two types of publish events, there are also two corresponding `eventTrigger` types:
* **`simpleMatch`** - this `eventTrigger` type is used for events that are published as a `simpleEvent` and will only match against simple strings.

```groovy
pipeline {
    agent any
    triggers {
*       eventTrigger simpleMatch("helloWorld")
    }
...
```

* **`jmespathQuery`** - this `eventTrigger` allows the use of complex queries against JSON event payloads.

```groovy
pipeline {
  agent none
  triggers {
*   eventTrigger jmespathQuery("event=='imagePush' && name=='node'")
  }
```

---
name: collab-lab
class: compact

# Lab - Triggering Pipelines with Cross Team Collaboration

* In this lab we will use CloudBees CI cross team collaboration by adding an event trigger listener so that when the job for our base image is complete, it will kick off our frontend application job with an event payload that includes the information for the `node` image to use.
* First, to figure out what we're dealing with, let's look at the part of the `Dockerfile` for the `microblog-frontend` application. By default, it will use the `node:lts-alpine` image:

```Dockerfile
ARG NODE_IMAGE=node:lts-alpine
...
```
  * The **VueJS** template (and supporting Pipeline Shared Library) will be updated to override the `NODE_IMAGE` argument with a value from the payload of a published event.
* The *Triggering Pipelines with Cross Team Collaboration* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md)


---
name: collab-overview

# Cross Team Collaboration Lab Overview

* Enabled **Notifications** for CloudBees Cross Team Collaboration on your Team (Jenkins instance)
* Updated the **VueJS** template of your Pipeline Template Catalog with an event trigger
* Created a Pipeline job that publishes an event to trigger the jobs based on the **VueJS** template