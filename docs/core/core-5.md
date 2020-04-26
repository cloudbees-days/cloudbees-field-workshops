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
* The [Cross Team Collaboration](https://docs.cloudbees.com/docs/cloudbees-core/2.204.2.2/cloud-admin-guide/cross-team-collaboration) functionality in CloudBees Core allows you to create events and listeners to trigger jobs across Core Masters. It provides a pub/sub relationship where jobs can send an event with data, and the jobs listening for it can trigger and process the data.
* 
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

