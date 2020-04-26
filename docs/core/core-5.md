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
]

---
name: cross-team-syntax

# Cross Team Collaboration Publish and Trigger Syntax

At its most basic, publishing an event is as simple as adding the following step:
`publishEvent simpleEvent('helloWorld')`. In this case, we're using the string 'helloWorld' and any matching listeners will receive it.

```groovy
pipeline {
    agent any
    stages {
        stage('Publish event') {
            steps {
                publishEvent simpleEvent('helloWorld')
            }
        }
    }
}
```

Now we just need another job that listens for the 'helloWorld' event. We can see there is a new `eventTrigger` type of job trigger specific for cross team collaboration.

```groovy
pipeline {
    agent any

    triggers {
        eventTrigger simpleMatch("helloWorld")
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
name: cross-team-lab

## Lab  

[https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md](https://github.com/cloudbees-days/core-rollout-flow-workshop/blob/master/labs/cross-team-collaboration/cross-team-collaboration.md)