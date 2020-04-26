name: cross-team-title
class: title, shelf, no-footer, fullbleed
background-image: linear-gradient(135deg,#279be0,#036eb4)
count: false

# CloudBees Cross Team Collaboration

---
name: cross-team overview

# Cross Team Collaboration

.img-left[
![Hibernating Masters Diagram](https://docs.cloudbees.com/docs/cloudbees-common/latest/_images/cross-team-collaboration-screenshots/cross-team-diagram.abf4b33.png)
]

.no-bullet[
* CloudBees Core [Cross Team Collaboration](https://docs.cloudbees.com/docs/cloudbees-core/2.204.2.2/cloud-admin-guide/cross-team-collaboration) simplifies the cumbersome and complicated tasks of triggering downstream jobs by eliminating the need to identify and maintain the full path for every downstream job. Prior to this feature, the details of every downstream job (Jenkins instance ID, full job name, Git branch name) all had to meticulously specified in the upstream job. If the job name changed, the upstream job had to be refactored, creating a maintenance burden and discouraging the adoption of event-based triggers.
* Cross Team Collaboration essentially allows a Pipeline to create a notification event to be consumed by other Pipelines waiting on it. It consists of a Publishing Event and a Trigger Condition.
* The Cross Team Collaboration feature has a configurable router for routing events either across all Masters connected via Core Operations Center or locally within one Master. It needs to be enabled and configured on your Team Master before you will be able to receive an event published by another Pipeline. 
]

---
name: cross-team-syntax
class: compact

# Cross Team Collaboration Syntax

* Publish an event: In this case, we're using the string 'helloWorld' and any matching subscriber will receive it.

```groovy
pipeline {
    agent any
    stages {
        stage('Publish event') {
            steps {
*               publishEvent simpleEvent('helloWorld')
            }
        }
    }
}
```

* Subscribe to an event: the following Pipeline will be triggered whenever the **helloWorld** event is published.

```groovy
pipeline {
    agent any
    triggers {
*       eventTrigger simpleMatch("helloWorld")
    }
    stages {
        stage('Example') {
            steps {
                echo 'received helloWorld'
            }
        }
    }
}
```

---
name: cross-team-event-types

# Publish Event Types for Cross Team Collaboration

* **`simpleEvent`**
* **`jsonEvent`**

---
name: cross-team-lab

# Lab - Triggering Pipelines with Cross Team Collaboration

* In this lab we will take advantage of CloudBees Core cross team collaboration by adding an event trigger listener so that when the job for our base image is complete, it will kick off our frontend application job. This is a common real world scenario where your container base image may receive security patches or minor updates and you want all applications using that base image to be updated. Rather than asking everyone to make sure their application containers are rebuilt with the new base image version, this can be triggered automatically. 
* The *Triggering Pipelines with Cross Team Collaboration* lab instructions are available at: 
  * [https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md)

